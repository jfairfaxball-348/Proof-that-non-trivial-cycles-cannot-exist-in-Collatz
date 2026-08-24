from math import gcd

# RL17 finite structural audit for the strengthened full-D sparse reduction.
# This is a verifier for the algebraic identities on all constructive
# gcd(A,L)=3, gcd(A,m)=1, e=+3 radius-3 structural solutions with A<25.
# The infinite lemma is proved algebraically in RL17_FULL_D_SPARSE_PROMOTION.md.


def Qword(w):
    pos = [i + 1 for i, b in enumerate(w) if b]
    L = len(pos)
    return sum((1 << (p - 1)) * 3 ** (L - k - 1) for k, p in enumerate(pos))


def rot(w, m):
    return w[m:] + w[:m]


def prefix_diff(source, target):
    A = len(source)
    out = [0]
    s = 0
    for i in range(A - 1):
        s += target[i] - source[i]
        out.append(s)
    return out


def solve_rotation_from_flow(A, m, F):
    delta = [0] * A
    prev = 0
    for i in range(A - 1):
        delta[i] = F[i] - prev
        prev = F[i]
    delta[A - 1] = -prev
    H = gcd(A, m)
    partial = [{}]
    for r0 in range(H):
        vals = {r0: 0}
        r = r0
        while True:
            nr = (r + m) % A
            nv = vals[r] + delta[r]
            if nr in vals:
                if nv != vals[nr]:
                    return []
                break
            vals[nr] = nv
            r = nr
        lo = min(vals.values())
        hi = max(vals.values())
        if hi - lo > 1:
            return []
        opts = []
        for c in range(-lo, 2 - hi):
            z = {r: vals[r] + c for r in vals}
            if all(v in (0, 1) for v in z.values()):
                opts.append(z)
        if not opts:
            return []
        partial = [{**base, **o} for base in partial for o in opts]
    return [[z[i] for i in range(A)] for z in partial]


checks = 0
sparse_implication_checks = 0
phase_checks = 0
equal_spacing_checks = 0
trivial_equal_spacing_cases = []

for A in range(6, 25, 3):
    a = A // 3
    for m in range(1, A):
        if gcd(A, m) != 1:
            continue
        for j in range(1, A - 1):
            for k in range(j + 1, A - 1):
                F = [0] * (A - 1)
                F[0] = F[j] = F[k] = -1
                for d in solve_rotation_from_flow(A, m, F):
                    L = sum(d)
                    if gcd(A, L) != 3:
                        continue
                    ell = L // 3
                    D = (1 << A) - 3 ** L
                    if D <= 1:
                        continue
                    p = sum(d[:m])
                    if a * p - m * ell != 1:
                        continue

                    X = 1 << a
                    Y = 3 ** ell
                    C = X * X + X * Y + Y * Y
                    assert D == (X - Y) * C
                    assert gcd(Y, D) == 1

                    omega = X * pow(Y, -1, D) % D
                    assert pow(omega, 3, D) == 1

                    theta = pow(pow(2, m, D), -1, D) * pow(3, p, D) % D
                    rho = pow(theta, -1, D)
                    assert pow(theta, a, D) == 3 * pow(omega, -m, D) % D
                    assert pow(theta, ell, D) == 2 * pow(omega, -p, D) % D
                    assert 27 * pow(rho, 3 * a, D) % D == 1

                    target = rot(d, m)
                    G = prefix_diff(d, target)
                    events = []
                    N = 0
                    S = 0
                    for t in range(A):
                        i = (t * m) % A
                        Pi = sum(d[:i])
                        K = a * Pi - i * ell
                        assert (K - (t - a * N)) % (3 * a) == 0
                        T = p * i - m * Pi
                        assert i == m * K + a * T
                        assert (T - m * N) % 3 == 0

                        W = pow(2, i, D) * pow(pow(3, Pi, D), -1, D) % D
                        phase = pow(rho, t, D) * pow(3, N, D) % D
                        assert W == phase
                        phase_checks += 1
                        S = (S + W) % D

                        if G[i]:
                            assert G[i] == -1
                            events.append(t)
                            N += 1

                    assert len(events) == 3 and N == 3
                    alpha, beta, gamma = events
                    sparse = (
                        pow(rho, alpha, D)
                        + 3 * pow(rho, beta, D)
                        + 9 * pow(rho, gamma, D)
                    ) % D
                    assert ((1 - rho) * S - 2 * rho * sparse) % D == 0
                    assert (4 * Qword(d) - pow(3, L, D) * S) % D == 0
                    if Qword(d) % D == 0:
                        assert sparse == 0
                    sparse_implication_checks += 1

                    # If the three gaps were exactly a,a,a, the normalized
                    # sparse factor would equal 1+omega^m+omega^(2m).
                    sing = (1 + 3 * pow(rho, a, D) + 9 * pow(rho, 2 * a, D)) % D
                    cubic_sum = (1 + pow(omega, m, D) + pow(omega, 2 * m, D)) % D
                    assert sing == cubic_sum
                    assert cubic_sum == C * pow(Y, -2, D) % D
                    if sing == 0:
                        assert X - Y == 1
                        assert (a, ell) == (2, 1)
                        trivial_equal_spacing_cases.append((A, L, m))
                    equal_spacing_checks += 1
                    checks += 1

print('RL17 full-D sparse structural audit: PASS')
print('exact gcd(A,L)=3 one-orbit structural solutions audited:', checks)
print('full-D phase identity checks:', phase_checks)
print('full-D sparse implication checks:', sparse_implication_checks)
print('equal-spacing full-D factor checks:', equal_spacing_checks)
print('structural cases where the equal-spacing factor vanishes:', trivial_equal_spacing_cases)

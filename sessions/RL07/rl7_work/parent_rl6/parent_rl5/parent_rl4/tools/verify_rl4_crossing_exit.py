#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def vp(n: int, p: int) -> int:
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def v2(n: int) -> int:
    return vp(n, 2)


def v3(n: int) -> int:
    return vp(n, 3)


def inv_step(y: int, d: int):
    n = (1 << d) * y - 1
    if n % 3:
        return None
    x = n // 3
    if x <= 0 or x % 2 == 0:
        return None
    return x


def inv_states(y: int, exps):
    xs = [y]
    x = y
    for d in exps:
        x = inv_step(x, d)
        if x is None:
            return None
        xs.append(x)
    return xs


def xi(y: int) -> int:
    m = v3(y + 1)
    return (1 << m) * ((y + 1) // (3**m))


# 1. RL-L23: exact relative-product identity and first-crossing cumulative catch-up.
# For same-endpoint inverse branches x_0=y_0, the exact identity is
# x_h/y_h = 2^(D_h-E_h) * prod_i (3+1/y_i)/(3+1/x_i).
# If x_1>y_1 and H is the first h with x_H<y_H, then D_H<=E_H.
product_checks = 0
downcross_checks = 0
upcross_checks = 0
equal_depth_checks = 0
for y in range(1, 120, 2):
    if y % 3 == 0:
        continue
    paths = []
    for exps in product(range(1, 7), repeat=4):
        xs = inv_states(y, exps)
        if xs is not None:
            paths.append((exps, xs))
    for exps, xs in paths:
        for h in range(1, 5):
            D = sum(exps[:h])
            lhs = Fraction(xs[h], y)
            rhs = Fraction(1 << D, 1)
            for i in range(1, h + 1):
                rhs *= Fraction(3 * xs[i] + 1, xs[i])
                rhs /= Fraction(3 * xs[i] + 1, xs[i])  # neutral sanity anchor
            # Direct one-branch identity: 2^D = (x_h/y)*prod(3+1/x_i).
            one = Fraction(xs[h], y)
            for i in range(1, h + 1):
                one *= Fraction(3 * xs[i] + 1, xs[i])
            assert one == (1 << D)
            product_checks += 1

    # Pair only branches with distinct first reverse exponent.
    for dword, xs in paths:
        for eword, ys in paths:
            if dword[0] == eword[0]:
                continue
            # Equal-depth physical collision would force the deterministic forward words equal.
            for h in range(1, 5):
                assert xs[h] != ys[h]
                equal_depth_checks += 1

            if dword[0] <= eword[0] or xs[1] <= ys[1]:
                continue
            H = None
            for h in range(2, 5):
                if xs[h] < ys[h]:
                    H = h
                    break
            if H is None:
                continue

            D = sum(dword[:H])
            E = sum(eword[:H])

            # Exact relative product identity.
            rel = Fraction(1 << (D - E), 1) if D >= E else Fraction(1, 1 << (E - D))
            for i in range(1, H + 1):
                rel *= Fraction(3 * ys[i] + 1, ys[i])
                rel /= Fraction(3 * xs[i] + 1, xs[i])
            assert rel == Fraction(xs[H], ys[H])

            # First crossing forces cumulative exponent catch-up.
            assert D <= E
            gap0 = dword[0] - eword[0]
            assert gap0 > 0
            assert sum(eword[1:H]) - sum(dword[1:H]) >= gap0
            downcross_checks += 1

# Symmetric audit: if the branch starts below and first crosses above, D_H>=E_H.
for y in range(1, 120, 2):
    if y % 3 == 0:
        continue
    paths = []
    for exps in product(range(1, 7), repeat=4):
        xs = inv_states(y, exps)
        if xs is not None:
            paths.append((exps, xs))
    for dword, xs in paths:
        for eword, ys in paths:
            if dword[0] >= eword[0] or xs[1] >= ys[1]:
                continue
            H = None
            for h in range(2, 5):
                if xs[h] > ys[h]:
                    H = h
                    break
            if H is None:
                continue
            D = sum(dword[:H])
            E = sum(eword[:H])
            assert D >= E
            gap0 = eword[0] - dword[0]
            assert sum(dword[1:H]) - sum(eword[1:H]) >= gap0
            upcross_checks += 1

# 2. RL-L24: height is dominated by least-red prefix slack.
# Audit exact rational inequality on ordinary accelerated prefixes that stay >= their start.
height_slack_checks = 0
slack_debt_checks = 0
for R in range(3, 600, 2):
    if R % 3 == 0:
        continue
    states = [R]
    exps = []
    x = R
    for _ in range(10):
        n = 3 * x + 1
        a = v2(n)
        x = n >> a
        if x < R:
            break
        exps.append(a)
        states.append(x)
        nsteps = len(exps)
        S = sum(exps)
        # r_n * 2^S * R^(n-1) <= (3R+1)^n
        assert states[-1] * (1 << S) * (R ** (nsteps - 1)) <= (3 * R + 1) ** nsteps
        height_slack_checks += 1

    # If a true orbit predecessor x1 has an alternative smaller-exponent predecessor y1
    # of its endpoint c0, audit the exact slack-debt implication using integer powers.
    for nsteps in range(1, len(states)):
        x1 = states[nsteps]
        # endpoint after x1 on the true orbit
        nn = 3 * x1 + 1
        d = v2(nn)
        c0 = nn >> d
        for e in range(d - 2, 0, -2):
            y1 = inv_step(c0, e)
            if y1 is None or y1 <= R:
                continue
            m = (d - e) // 2
            assert x1 == (4**m) * y1 + (4**m - 1) // 3
            assert x1 > (4**m) * R
            S = sum(exps[:nsteps])
            # sigma_n>2m <=> (3R+1)^n > 2^(S+2m) R^n.
            assert (3 * R + 1) ** nsteps > (1 << (S + 2 * m)) * (R ** nsteps)
            N1 = sum(a == 1 for a in exps[:nsteps])
            # Equivalent exact form of N1 > n(2-beta_R)+2m:
            # 2^(2n+2m-N1) R^n < (3R+1)^n.
            assert (1 << (2 * nsteps + 2 * m - N1)) * (R ** nsteps) < (3 * R + 1) ** nsteps
            slack_debt_checks += 1

# 3. RL-L25 algebra: tail suffix lower bound from total prefix slack, plus periodic phase decomposition.
phase_checks = 0
for k in range(2, 10):
    for b in product(range(1, 5), repeat=k):
        B = sum(b)
        for H in range(1, k + 1):
            prefix = sum(b[:k-H])
            suffix = sum(b[k-H:])
            assert suffix == B - prefix
            # Symbolic beta check at several rational beta surrogates > 1.
            for beta in (Fraction(8, 5), Fraction(5, 3), Fraction(7, 4)):
                if prefix <= beta * (k - H):
                    s = beta * k - B
                    assert suffix >= beta * H - s
                    phase_checks += 1

for L in range(2, 8):
    for a in product(range(1, 5), repeat=L):
        A = sum(a)
        for H in range(0, 4 * L + 1):
            q, r = divmod(H, L)
            Eminus = sum(a[L-r:]) if r else 0
            # Periodically unwrapped reverse block ending at phase 0.
            block = []
            for j in range(H):
                block.append(a[(L - 1 - j) % L])
            EH = sum(block)
            assert EH == q * A + Eminus
            phase_checks += 1

# 4. RL-L26/L27: k=0 neutral spine and first exit arithmetic.
neutral_checks = 0
exit_checks = 0
allowed_small_s = {2: {1}, 3: {1}, 4: {1}}
for s in range(2, 24):
    allowed_by_inequality = set()
    for t in range(1, 40):
        r = v3((1 << t) - 1)
        # t < (s-r) log2(3/2) in exact integer form.
        if s > r and (1 << (t + s - r)) < 3 ** (s - r):
            allowed_by_inequality.add(t)
    if s in allowed_small_s:
        assert allowed_by_inequality == allowed_small_s[s]

    for q in range(1, 500, 2):
        if q % 3 == 0:
            continue
        R = (1 << s) * q - 1
        # Exact initial exponent-1 neutral spine.
        c = R
        for j in range(s):
            assert c + 1 == (1 << (s - j)) * (3**j) * q
            assert xi(c) == R + 1
            if j < s - 1:
                n = 3 * c + 1
                assert v2(n) == 1
                c = n >> 1
            neutral_checks += 1

        # Exit exponent and exit state.
        t = v2((3**s) * q - 1)
        aexit = t + 1
        z = ((3**s) * q - 1) >> t
        assert v2(3 * c + 1) == aexit
        assert ((3 * c + 1) >> aexit) == z

        # Whenever the two necessary cycle inequalities hold, the theorem's valuation
        # and sharpened exponent inequality must hold.
        if z >= R + 2 and xi(z) >= R + 3:
            # First minimum inequality implies t < s log2(3/2), hence t<s.
            assert (1 << (t + s)) < 3**s
            assert t < s
            rz = v3(z + 1)
            rt = v3((1 << t) - 1)
            assert rz == rt
            if t % 2:
                assert rt == 0
            else:
                assert rt == 1 + v3(t // 2)
            assert (1 << (t + s - rt)) < 3 ** (s - rt)
            exit_checks += 1

# 5. RL-L28/L29: general exponent-1 plateau normal form and regular-exit descent certificate.
plateau_checks = 0
plateau_ratio_checks = 0
regular_exit_checks = 0
regular_descent_checks = 0
deep_exit_diagnostics = 0
for y in range(1, 120000, 2):
    if y % 3 == 0:
        continue
    s2 = v2(y + 1)
    mu = v3(y + 1)
    q0 = (y + 1) // ((1 << s2) * (3**mu))
    assert q0 % 2 == 1 and q0 % 3 != 0
    n = s2 + mu
    W = (1 << n) * q0
    assert W == xi(y)

    cur = y
    for j in range(s2 - 1):
        nn = 3 * cur + 1
        assert v2(nn) == 1
        cur = nn >> 1
        assert xi(cur) == W
    assert cur + 1 == 2 * (3 ** (n - 1)) * q0

    t = v2((3**n) * q0 - 1)
    z = ((3**n) * q0 - 1) >> t
    assert ((3 * cur + 1) >> (t + 1)) == z
    mnext = v3(z + 1)
    r = v3((1 << t) - 1)
    # General valuation split.
    if r < n:
        assert mnext == r
    elif r > n:
        assert mnext == n
    else:
        assert mnext >= n

    Wnext = xi(z)
    # RL-L30 single-plateau xi-ratio identity (rational form before logs).
    eps_factor = Fraction((3**n) * q0 + (1 << t) - 1, (3**n) * q0)
    scale = (Fraction(3, 2) ** (n - mnext)) * Fraction(1, 1 << t)
    assert Fraction(Wnext, W) == scale * eps_factor
    plateau_ratio_checks += 1
    plateau_checks += 1

    # On a shallow/regular exit t<n, r<t<n, so the next 3-adic valuation is exactly r.
    if t < n:
        assert r < n and mnext == r
        low = (1 << (n + t - r)) < 3 ** (n - r)
        high = (1 << (n + t - r)) > 3 ** (n - r)
        assert low ^ high  # no equality between powers of 2 and 3 here
        if low:
            assert Wnext > W
        if Wnext <= W:
            assert high
            regular_descent_checks += 1
        regular_exit_checks += 1
    else:
        deep_exit_diagnostics += 1

# 6. RL-G8: exact Haar-measure series for the one-exit filter.
# Conditional on R == 3 mod4: P(s)=2^(1-s), and conditional on s, P(t)=2^(-t).
# Let s_min(t) be the first s satisfying the sharpened exit inequality.
def s_min_for_t(t: int):
    r = v3((1 << t) - 1)
    s = max(2, r + 1)
    while not ((1 << (t + s - r)) < 3 ** (s - r)):
        s += 1
    return s, r

measure_terms = 30
mu30 = Fraction(0, 1)
for t in range(1, measure_terms + 1):
    smin, r = s_min_for_t(t)
    # Sum_{s>=smin} 2^(1-s) = 2^(2-smin).
    mu30 += Fraction(1, 2 ** (t + smin - 2))

# The omitted t-tail is < sum_{t>30}2^-t = 2^-30.
assert mu30 > Fraction(1, 2)
assert float(mu30) > 0.540299068
assert float(mu30) < 0.540299070

tail_bound = Fraction(1, 2**measure_terms)

print('RL-4 crossing / cycle-exit verifier: PASS')
print(f'relative one-branch product checks: {product_checks}')
print(f'equal-depth noncollision checks: {equal_depth_checks}')
print(f'first down-cross catch-up checks: {downcross_checks}')
print(f'first up-cross catch-up checks: {upcross_checks}')
print(f'height-slack prefix checks: {height_slack_checks}')
print(f'entry slack-debt checks: {slack_debt_checks}')
print(f'phase/slack algebra checks: {phase_checks}')
print(f'neutral-spine checks: {neutral_checks}')
print(f'cycle-exit implication checks: {exit_checks}')
print(f'general plateau normal-form checks: {plateau_checks}')
print(f'plateau xi-ratio checks: {plateau_ratio_checks}')
print(f'regular plateau-exit checks: {regular_exit_checks}')
print(f'regular xi-descent checks: {regular_descent_checks}')
print(f'deep-exit diagnostics: {deep_exit_diagnostics}')
print('one-exit survivor measure 30-term partial:', mu30, float(mu30))
print('omitted measure tail <', tail_bound, float(tail_bound))
print('scope: finite exact audits of analytic statements; no nontrivial-cycle exclusion is claimed')

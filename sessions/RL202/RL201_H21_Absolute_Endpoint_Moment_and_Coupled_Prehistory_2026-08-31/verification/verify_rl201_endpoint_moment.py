#!/usr/bin/env python3
"""Exact toy regressions, not actual-branch word certificates.

For all a,n in the stated bounded toy ranges which meet the protected-window
hypotheses, check direct z transport, complete p-chain inversion, moving-window
K coefficients and the independently formed fixed-moment endpoint formula.
No floating-point arithmetic is used.
"""

from fractions import Fraction as F


def pows2(n):
    return F(2 ** n) if n >= 0 else F(1, 2 ** (-n))


def data(A, L, p, u, q):
    assert A * p - u * L == 1
    lam = F(2 ** A, 3 ** L)
    alpha = F(3 ** p, 2 ** u)
    beta = (alpha - 1) / (lam - 1)
    assert lam > 1 and alpha > 1 and beta > 0
    rho = [pows2(A * i // L) / (3 ** i) for i in range(L)]

    def lift(j):
        turns, rem = divmod(j, L)
        return q[rem] * (lam ** turns)

    C = [sum((lift(j) for j in range(i, i + p)), F(0)) for i in range(L)]
    Y = [sum((lift(j) for j in range(i, i + L)), F(0)) for i in range(L)]
    K = [(alpha * C[i] + beta * Y[i]) / 3 for i in range(L)]
    z = [Y[i] / (3 * (lam - 1)) for i in range(L)]
    x = [z[i] / rho[i] for i in range(L)]
    Q = sum(q, F(0))
    P = [sum(q[:i], F(0)) for i in range(L + 1)]

    # Affine transport checked independently of the prefix construction.
    for i in range(L):
        znext = z[i + 1] if i + 1 < L else lam * z[0]
        assert 3 * (znext - z[i]) == q[i]
        assert z[i] == Q / (3 * (lam - 1)) + P[i] / 3

    # Complete rank-gap reconstruction, including its unique carry.
    I = [(p * r) % L for r in range(L)]
    gaps = [K[i] / rho[i] for i in I]
    assert sum(gaps, F(0)) == x[0]
    for r in range(L):
        i = I[r]
        expected = x[I[r + 1]] - x[i] if r + 1 < L else 2 * x[0] - x[i]
        assert gaps[r] == expected
        assert x[i] == sum(gaps, F(0)) + sum(gaps[:r], F(0))

    # Fixed-K0 formula for every canonical absolute coordinate; height one
    # is needed only if eta is interpreted as an H21 integer lift.
    for a in range(L):
        J = alpha * P[p] - (alpha - 1) * P[a]
        assert 3 * (alpha - 1) * rho[a] * x[a] == 3 * K[0] - J
        eta_coordinate = (1 + 2 * x[a]) / (2 ** 34)
        assert eta_coordinate == F(1, 2 ** 34) + (3 * K[0] - J) / (
            3 * (alpha - 1) * rho[a] * (2 ** 33)
        )

    # Canonical coefficient enumeration, with real lifted windows.
    coefficient_set = {beta, beta + alpha, lam * beta, lam * (beta + alpha)}
    for i in range(L):
        for j in range(L):
            cq = F(0)
            yq = F(0)
            for k in range(i, i + p):
                turns, rem = divmod(k, L)
                if rem == j:
                    cq += lam ** turns
            for k in range(i, i + L):
                turns, rem = divmod(k, L)
                if rem == j:
                    yq += lam ** turns
            assert alpha * cq + beta * yq in coefficient_set
    return lam, alpha, beta, rho, K, x, P


def run_case(A, L, p, u):
    rho = [pows2(A * i // L) / (3 ** i) for i in range(L)]
    count = 0
    for a in range(1, L):
        for n in range(4):
            if not (a + n + 1 < p and a + p + n + 1 < L):
                continue
            q = [F(3, 5) * r for r in rho]
            q[0] = rho[0]
            q[p] = rho[p]
            for j in list(range(a, a + n + 1)) + list(range(a + p, a + p + n + 1)):
                q[j] = rho[j] / 2
            baseline = data(A, L, p, u, q)
            lam, alpha, beta, _, K, x, _ = baseline
            b, d = a + n + 1, a + p + n + 1
            Tminus = min(q[b] / beta, (rho[d] - q[d]) / (beta + alpha))
            Tplus = min((rho[b] - q[b]) / beta, q[d] / (beta + alpha))
            assert Tminus > 0 and Tplus > 0
            for t in (-Tminus / 2, Tplus / 2):
                changed = list(q)
                changed[b] += beta * t
                changed[d] -= (beta + alpha) * t
                assert all(0 < changed[i] <= rho[i] for i in range(L))
                _, _, _, _, Knew, xnew, _ = data(A, L, p, u, changed)
                assert Knew[0] == K[0]
                assert changed[0] == q[0] and changed[p] == q[p]
                for i in range(a, a + n + 1):
                    assert changed[i] == q[i] and changed[i + p] == q[i + p]
                    assert Knew[i] == K[i]
                    displacement = -alpha * t / (3 * (lam - 1) * rho[i])
                    assert xnew[i] - x[i] == displacement != 0
                    assert xnew[i + p] - x[i + p] == displacement
                bound = lam * (beta + alpha) * (2 * beta + alpha) * abs(t) / 3
                assert all(abs(Knew[i] - K[i]) <= bound for i in range(L))
                count += 1
    return count


if __name__ == "__main__":
    # Actual-constant comparison accompanying the analytic alpha/rho bounds.
    actual_L = 137528045312
    actual_p = 65470613321
    assert actual_p < 2 ** 36
    assert F(29 * 2 ** 33, 32 * actual_L) > F(1, 20)
    assert F(21 * 2 ** 33, 10 * actual_L - 7) < F(2, 15)
    assert F(25, 36) < F(7, 10)
    print("PASS actual-constant rational comparisons: 1/20 < D_a < 2/15")
    results = []
    for spec in ((27, 17, 12, 19), (46, 29, 12, 19)):
        results.append((spec, run_case(*spec)))
    assert all(count > 0 for _, count in results)
    for spec, count in results:
        print(f"PASS toy Bezout {spec}: {count} exact signed perturbations")
    print("PASS exact absolute-endpoint, p-chain, fixed-moment and coupled-fiber regression")
    print("Scope: toy algebra only; no actual high-branch height-word or eta-class certificate")

#!/usr/bin/env python3
"""RL269 analytic finite-reduction verifier for determinant-one [1,1,1,1,1]."""
from math import comb, gcd, log

NONBRACKET_CUTOFF = 1713   # A >= 1713 excluded
BRACKET_CUTOFF = 690205
EXPECTED_ROWS = 36
EXPECTED_PAIRS = 2234
EXPECTED_MAX_A = 690
EXPECTED_GAPS = 618_391_058_390

EXPECTED_COARSE = [
    (5, 3, 3, 2),
    (8, 5, 3, 2),
    (27, 17, 19, 12),
    (46, 29, 19, 12),
    (65, 41, 19, 12),
    (149, 94, 84, 53),
    (233, 147, 84, 53),
]

def positive_D(A, L):
    return (1 << A) - 3 ** L

def mixed_bound(A, L, m, q):
    U5 = (4 * A) // 5
    r = q if m <= A - m else L - q
    return 5 * 3 ** (7 + r) * 2 ** (U5 - r)

def determinant_pair(A, L):
    if L <= 1 or gcd(A, L) != 1:
        return None
    q = pow(A, -1, L)
    if not (0 < q < L):
        return None
    num = q * A - 1
    if num % L:
        return None
    m = num // L
    if not (0 < m < A):
        return None
    assert q * A - m * L == 1
    return m, q

def stern_brocot_rows_exact(cutoff):
    # Exact path around alpha=log(3)/log(2), avoiding repeated huge
    # exponentiation. For a mediant, the corresponding powers multiply.
    ln, ld = 1, 1
    un, ud = 2, 1
    l2, l3 = 2, 3
    u2, u3 = 4, 3
    rows = []
    while True:
        mn, md = ln + un, ld + ud
        if un > cutoff and mn > cutoff:
            break
        m2, m3 = l2 * u2, l3 * u3
        if m2 > m3:  # mediant > alpha iff 2^mn > 3^md
            un, ud = mn, md
            u2, u3 = m2, m3
        else:
            ln, ld = mn, md
            l2, l3 = m2, m3
        A, L, m, q = un, ud, ln, ld
        if A <= cutoff and 0 < m < A and 0 < q < L:
            assert q * A - m * L == 1
            assert (1 << A) > 3 ** L
            assert (1 << m) < 3 ** q
            row = (A, L, m, q)
            if not rows or rows[-1] != row:
                rows.append(row)
    return rows

def complete_survivors():
    out = set()
    for A in range(2, NONBRACKET_CUTOFF):
        for L in range(2, A):
            D = positive_D(A, L)
            if D <= 1:
                continue
            p = determinant_pair(A, L)
            if p is None:
                continue
            m, q = p
            if D <= mixed_bound(A, L, m, q):
                out.add((A, L, m, q))

    rows = stern_brocot_rows_exact(BRACKET_CUTOFF)
    assert len(rows) == EXPECTED_ROWS
    coarse = []
    for row in rows:
        A, L, m, q = row
        if positive_D(A, L) <= mixed_bound(A, L, m, q):
            coarse.append(row)
            out.add(row)
    assert coarse == EXPECTED_COARSE
    return sorted(out), rows

def check_analytic_constants():
    beta = log(2) / log(3)
    delta = log(2) / 5 - (beta / 2) * log(3 / 2)
    Clog = log(5) + 7.5 * log(3)
    assert delta > 0

    assert Clog - delta * 1713 < log(log(2) / (2 * 1713))
    assert Clog - delta * 1712 >= log(log(2) / (2 * 1712))
    assert Clog - delta * 984 < log(0.5)

    root = (log(2) + Clog + 22 * 21**2 * log(2) * log(3)) / delta
    assert 690205 < root < 690206

    K = 22 * log(2) * log(3)
    transition = __import__("math").exp(20.94) / (1 / log(3) + 1 / log(2))
    def upper_M(A):
        return log(A * (1 / log(3) + 1 / log(2))) + 0.06
    def F_upper(A):
        return log(2) + Clog - delta * A + K * upper_M(A) ** 2
    assert F_upper(transition) < 0
    deriv = -delta + 2 * K * upper_M(transition) / transition
    assert deriv < 0

def main():
    check_analytic_constants()
    pairs, rows = complete_survivors()
    assert len(pairs) == EXPECTED_PAIRS
    assert max(A for A, _, _, _ in pairs) == EXPECTED_MAX_A
    gap_total = sum(2 * comb(A - 6, 4) for A, _, _, _ in pairs if A >= 10)
    assert gap_total == EXPECTED_GAPS
    print("RL269 analytic finite reduction: PASS")
    print("stern_brocot_rows =", len(rows))
    print("coarse_survivors =", len(EXPECTED_COARSE))
    print("pairs =", len(pairs))
    print("max A =", max(A for A, _, _, _ in pairs))
    print("naive_two_order_gap_configurations =", gap_total)
    print("RL269_ANALYTIC_PASS")

if __name__ == "__main__":
    main()

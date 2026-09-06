#!/usr/bin/env python3
"""RL268 analytic and determinant-pair certificate verifier."""

from math import comb, gcd, log

NONBRACKET_CUTOFF = 375
BRACKET_CUTOFF = 163052
EXPECTED_PAIRS = 967
EXPECTED_MAX_A = 174
EXPECTED_GAPS = 179_403_060


def positive_D(A, L):
    return (1 << A) - 3 ** L


def mixed_bound(A, L, m, q):
    U4 = (3 * A + 1) // 4
    r = q if m <= A - m else L - q
    return 5 * 3 ** (7 + r) * 2 ** (U4 - r)


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


def above_alpha(n, d):
    # n/d > log(3)/log(2) iff 2^n > 3^d.
    return (1 << n) > 3 ** d


def stern_brocot_rows(cutoff):
    ln, ld = 1, 1
    un, ud = 2, 1
    rows = []
    while True:
        mn, md = ln + un, ld + ud
        if un > cutoff and mn > cutoff:
            break
        if above_alpha(mn, md):
            un, ud = mn, md
        else:
            ln, ld = mn, md
        A, L, m, q = un, ud, ln, ld
        if A <= cutoff and 0 < m < A and 0 < q < L:
            assert q * A - m * L == 1
            row = (A, L, m, q)
            if not rows or rows[-1] != row:
                rows.append(row)
    return rows


def complete_survivors():
    out = set()

    # Every non-bracketing survivor has A <= 374. Enumerating all
    # determinant-one pairs in this range also harmlessly includes the
    # small bracketing rows.
    for A in range(2, NONBRACKET_CUTOFF):
        for L in range(2, A):
            if positive_D(A, L) <= 1:
                continue
            p = determinant_pair(A, L)
            if p is None:
                continue
            m, q = p
            if positive_D(A, L) <= mixed_bound(A, L, m, q):
                out.add((A, L, m, q))

    rows = stern_brocot_rows(BRACKET_CUTOFF)
    assert len(rows) == 35
    coarse = []
    for A, L, m, q in rows:
        if positive_D(A, L) <= mixed_bound(A, L, m, q):
            coarse.append((A, L, m, q))
            out.add((A, L, m, q))

    assert coarse == [
        (5, 3, 3, 2),
        (8, 5, 3, 2),
        (27, 17, 19, 12),
        (46, 29, 19, 12),
        (65, 41, 19, 12),
        (149, 94, 84, 53),
    ]
    return sorted(out)


def check_analytic_constants():
    beta = log(2) / log(3)
    delta = log(2) / 4 - (beta / 2) * log(3 / 2)
    Clog = log(5) + 7.5 * log(3) + 0.25 * log(2)
    assert delta > 0

    assert Clog - delta * 375 < log(log(2) / (2 * 375))
    assert Clog - delta * 374 >= log(log(2) / (2 * 374))
    assert Clog - delta * 237 < log(0.5)

    necessary_root = (log(2) + Clog + 22 * 21**2 * log(2) * log(3)) / delta
    assert 163052 < necessary_root < 163053


def main():
    check_analytic_constants()
    pairs = complete_survivors()
    assert len(pairs) == EXPECTED_PAIRS
    assert max(A for A, _, _, _ in pairs) == EXPECTED_MAX_A
    gap_total = sum(4 * comb(A - 6, 3) for A, _, _, _ in pairs if A >= 9)
    assert gap_total == EXPECTED_GAPS
    print("RL268 analytic certificate: PASS")
    print("pairs =", len(pairs))
    print("max A =", max(A for A, _, _, _ in pairs))
    print("gap configurations =", gap_total)


if __name__ == "__main__":
    main()

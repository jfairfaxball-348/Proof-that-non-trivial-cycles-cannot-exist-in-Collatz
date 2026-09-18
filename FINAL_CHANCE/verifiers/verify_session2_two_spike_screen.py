#!/usr/bin/env python3
"""FINAL_CHANCE Session 2 two-spike verifier/screen.

Screens every admissible area-2 two-spike profile h_p=h_q=1 with
1 <= p < q <= 1000 for the first-survivor g=1 counts
A=217976794617, L=137528045312.

There are 584 admissible spike positions and C(584,2)=170236 pairs.
For every pair this script evaluates an outward interval for

    Q_{p,q}/D = [S - (rho_p+rho_q)/2] / [3(exp(Delta)-1)],

where
    D     = 2^A - 3^L,
    Delta = A ln 2 - L ln 3,
    b_j   = floor(A j/L),
    rho_j = 2^b_j / 3^j,
    S     = sum_{j=0}^{L-1} rho_j.

S and exp(Delta)-1 are computed by the same rigorous machinery as the
Session 1 verifier.  The screen itself therefore ranks interval-certified
miss distances; it is not a machine-float search.

Only the Python standard library is required.  This file expects
verify_session1_interval.py in the same directory.
"""

from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
from math import comb

from verify_session1_interval import (
    A, L, PREC, Interval,
    iadd, isub, imul, idiv,
    rat_interval, fraction_interval,
    floor_sum_F, ln_integer_bounds, expm1_bounds,
)

LIMIT = 1000


def b(j):
    return (A * j) // L


def nearest_integer_distance_interval(x):
    """Return (d_lo,d_hi,nearest) for distance to nearest integer."""
    flo = x.lo.to_integral_value(rounding=ROUND_FLOOR)
    cei = x.hi.to_integral_value(rounding=ROUND_CEILING)

    candidates = {flo, flo + 1, cei - 1, cei}
    best = None
    for n in candidates:
        if x.lo <= n <= x.hi:
            dlo = Decimal(0)
            dhi = max(n - x.lo, x.hi - n)
        elif n < x.lo:
            dlo = x.lo - n
            dhi = x.hi - n
        else:
            dlo = n - x.hi
            dhi = n - x.lo
        item = (dlo, dhi, n)
        if best is None or item[1] < best[1]:
            best = item
    return best


def main():
    l2_lo, l2_hi = ln_integer_bounds(2, 300)
    l3_lo, l3_hi = ln_integer_bounds(3, 400)
    delta_lo = A * l2_lo - L * l3_hi
    delta_hi = A * l2_hi - L * l3_lo
    e_lo, e_hi = expm1_bounds(delta_lo, delta_hi, 20)
    E = Interval(fraction_interval(e_lo).lo, fraction_interval(e_hi).hi)

    S = floor_sum_F(L, A, rat_interval(1, 3), Interval(2))
    denom = imul(Interval(3), E)
    base = idiv(S, denom)
    half_over_denom = idiv(Interval(1), imul(Interval(6), E))

    admissible = [
        p for p in range(1, LIMIT + 1)
        if b(p) - b(p - 1) == 2
    ]
    assert len(admissible) == 584
    assert comb(len(admissible), 2) == 170_236

    rho = {}
    for p in admissible:
        rho[p] = rat_interval(2 ** b(p), 3 ** p)

    pair_count = 0
    best = None
    second = None
    possible_owner = None

    for ii, p in enumerate(admissible):
        for q in admissible[ii + 1:]:
            pair_count += 1
            qint = isub(base, imul(half_over_denom, iadd(rho[p], rho[q])))
            dlo, dhi, nearest = nearest_integer_distance_interval(qint)

            if dlo == 0:
                possible_owner = (p, q, qint, nearest)
                break

            item = (dhi, dlo, p, q, qint, nearest)
            if best is None or item[0] < best[0]:
                second = best
                best = item
            elif second is None or item[0] < second[0]:
                second = item
        if possible_owner is not None:
            break

    assert pair_count == 170_236
    assert possible_owner is None
    assert best is not None and second is not None

    best_hi, best_lo, p, q, qint, nearest = best
    second_hi, second_lo, p2, q2, qint2, nearest2 = second

    assert (p, q) == (498, 972)
    assert best_hi < second_lo

    c497 = b(498) - b(497)
    c498 = b(499) - b(498)
    c971 = b(972) - b(971)
    c972 = b(973) - b(972)
    a497 = c497 - 1
    a498 = c498 + 1
    a971 = c971 - 1
    a972 = c972 + 1
    assert min(a497, a498, a971, a972) >= 1

    print("FINAL_CHANCE Session 2 two-spike screen: PASS")
    print("A =", A)
    print("L =", L)
    print("screen phases = 1..", LIMIT)
    print("admissible spike positions =", len(admissible))
    print("screened pairs =", pair_count)
    print("formula = (S-(rho_p+rho_q)/2)/(3*(exp(Delta)-1))")
    print("Delta = A*ln(2)-L*ln(3)")
    print("rho_j = 2^floor(A*j/L)/3^j")
    print("S = sum_{j=0}^{L-1} rho_j")
    print("precision_digits =", PREC)
    print("possible owned pair in screen = False")
    print("closest pair =", (p, q))
    print("b_p,b_q =", (b(p), b(q)))
    print("modified exponents a_497,a_498,a_971,a_972 =",
          (a497, a498, a971, a972))
    print("Q_pq/D lower =", qint.lo)
    print("Q_pq/D upper =", qint.hi)
    print("interval width =", qint.hi - qint.lo)
    print("nearest integer =", nearest)
    print("closest miss distance lower =", best_lo)
    print("closest miss distance upper =", best_hi)
    print("second closest pair =", (p2, q2))
    print("second miss distance lower =", second_lo)
    print("second miss distance upper =", second_hi)
    print("best-vs-second certified separation =", second_lo - best_hi)


if __name__ == "__main__":
    main()

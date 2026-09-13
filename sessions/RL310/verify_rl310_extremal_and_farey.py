#!/usr/bin/env python3
"""
RL310 exact arithmetic verifier.

Certificates:
1. First-Farey physical packing cap:
   for p*=114208327604, q*=72057431991, R0=2^71,
   epsilon = p* ln 2 - q* ln 3,
   the inequality

       g*epsilon <= 1/(3R0)
                    + (1/9) ln(1 + 3(g*q*-1)/(R0-1))

   can hold only for g <= 22,623,517,356.

   All logarithms are enclosed by exact Fraction intervals using
   ln(x)=2*atanh((x-1)/(x+1)) after power-of-two range reduction.

2. The elementary inequality used in the universal extremal low/high split:
   for integer R>=5,

       16/(R+2) > 3/R + 1/(R-1),

   because the difference is
       3(4R^2-7R+2)/(R(R-1)(R+2)) > 0.

No floating-point comparison is used for certification.
"""

from fractions import Fraction

P = 114_208_327_604
Q = 72_057_431_991
R0 = 2**71
GMAX = 22_623_517_356
TERMS = 260


def atanh_log_interval_unit_to_two(x: Fraction, terms: int = TERMS):
    """Exact interval for ln(x), assuming 1 <= x <= 2."""
    assert Fraction(1) <= x <= Fraction(2)
    y = (x - 1) / (x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for k in range(terms):
        s += Fraction(2, 2*k + 1) * yp
        yp *= y2
    # positive tail:
    # 2 sum_{k>=terms} y^(2k+1)/(2k+1)
    # <= 2 y^(2terms+1)/((2terms+1)(1-y^2))
    tail = Fraction(0) if y == 0 else (
        Fraction(2, 2*terms + 1) * yp / (1 - y2)
    )
    return s, s + tail


def log_interval(x: Fraction, terms: int = TERMS):
    """Exact rational enclosure for ln(x), x>0."""
    assert x > 0
    if x < 1:
        lo, hi = log_interval(1/x, terms)
        return -hi, -lo

    k = 0
    z = x
    while z > 2:
        z /= 2
        k += 1

    zlo, zhi = atanh_log_interval_unit_to_two(z, terms)
    l2lo, l2hi = atanh_log_interval_unit_to_two(Fraction(2), terms)

    return zlo + k*l2lo, zhi + k*l2hi


def epsilon_interval():
    l2lo, l2hi = log_interval(Fraction(2))
    l3lo, l3hi = log_interval(Fraction(3))
    return P*l2lo - Q*l3hi, P*l2hi - Q*l3lo


def packing_rhs_interval(g: int):
    arg = Fraction(
        (R0 - 1) + 3*(g*Q - 1),
        R0 - 1,
    )
    llo, lhi = log_interval(arg)
    base = Fraction(1, 3*R0)
    return base + llo/9, base + lhi/9


def main():
    eps_lo, eps_hi = epsilon_interval()
    assert eps_lo > 0

    # GMAX still survives the necessary packing inequality.
    b_lo, b_hi = packing_rhs_interval(GMAX)
    f_hi = GMAX*eps_hi - b_lo
    assert f_hi < 0

    # GMAX+1 fails it.
    gp = GMAX + 1
    b_lo, b_hi = packing_rhs_interval(gp)
    f_lo = gp*eps_lo - b_hi
    assert f_lo > 0

    # Thereafter F(g)=g*epsilon-B(g) is strictly increasing:
    # B'(g)=Q/[3((R0-1)+3(gQ-1))], and B' decreases with g.
    deriv_at_gp = Fraction(
        Q,
        3*((R0 - 1) + 3*(gp*Q - 1)),
    )
    assert eps_lo > deriv_at_gp

    # Elementary universal extremal inequality.
    # 4R^2-7R+2 is positive at R=5 and increasing thereafter.
    assert 4*5*5 - 7*5 + 2 > 0
    assert 8*5 - 7 > 0

    print("RL310 exact verifier: PASS")
    print("epsilon interval width:", float(eps_hi - eps_lo))
    print("epsilon approx:", float((eps_lo + eps_hi)/2))
    print("certified first-Farey g cap:", GMAX)
    print("F(GMAX) < 0 and F(GMAX+1) > 0: PASS")
    print("monotonic tail after GMAX+1: PASS")
    print("universal extremal elementary inequality for R>=5: PASS")


if __name__ == "__main__":
    main()

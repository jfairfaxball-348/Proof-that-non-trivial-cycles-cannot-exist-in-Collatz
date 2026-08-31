#!/usr/bin/env python3
"""RL201 verified support: repair-check the signed atanh tail in inherited RL200.

This script certifies the unchanged mathematical lower-wall conclusion using a
valid logarithm interval for the argument KLO/2**37 < 1. No authority is edited.
"""

from fractions import Fraction as Q

A = 217_976_794_617
L = 137_528_045_312
B = A-L
p = 65_470_613_321
T = 7*3**35
KLO, KHI = 128_081_997_553, 146_795_909_391


def ln_bounds(x, terms=110):
    """Exact rational enclosure of ln(x) for every positive rational x.

    ln(x)=2*sum(z**(2*j+1)/(2*j+1)), z=(x-1)/(x+1).
    The omitted tail has the sign of z and absolute value at most
    2*abs(z)**(2*N+1)/((2*N+1)*(1-z*z)).
    """
    x = Q(x)
    assert x > 0
    assert isinstance(terms, int) and terms > 0
    z = (x-1)/(x+1)
    z2 = z*z
    term = z
    partial = Q(0)
    for j in range(terms):
        partial += term/(2*j+1)
        term *= z2
    partial *= 2
    tail = 2*abs(term)/((2*terms+1)*(1-z2))
    return (partial, partial+tail) if z >= 0 else (partial-tail, partial)


def mul(c, bounds):
    lo, hi = bounds
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)


LN2 = ln_bounds(2)
LN3 = ln_bounds(3)
LN87 = ln_bounds(Q(8, 7))


def log_k_over_u(r, u):
    """ln[(rho(r)*T/2**21)/u] for positive rational u."""
    i = p*r % L
    n = (A*i-r)//L
    assert 0 <= r < L and A*i == n*L+r
    ulog = ln_bounds(Q(u)/2**37)
    pieces = [mul(n-55, LN2), mul(35-i, LN3),
              (-LN87[1], -LN87[0]), (-ulog[1], -ulog[0])]
    return sum(x[0] for x in pieces), sum(x[1] for x in pieces)


if __name__ == "__main__":
    # The old partial+tail enclosure fails for x<1; the corrected endpoints
    # match minus the valid positive-argument reciprocal enclosure exactly.
    x = Q(KLO, 2**37)
    assert x < 1
    inv = ln_bounds(1/x)
    direct = ln_bounds(x)
    assert direct == (-inv[1], -inv[0])
    delta_lo = A*LN2[0] - L*LN3[1]
    delta_hi = A*LN2[1] - L*LN3[0]
    assert 0 < delta_lo < delta_hi < Q(1, 2**40)
    assert LN2[0] > L*delta_hi
    assert log_k_over_u(25_583_192_105, KHI)[0] > 0
    assert log_k_over_u(25_583_192_106, KHI)[1] < 0
    corrected_lo = log_k_over_u(41_775_866_136, KLO)[0]
    tail = direct[1]-direct[0]
    # For x<1 the inherited helper returns (partial,partial+tail), while
    # the corrected helper returns (partial-tail,partial). In the lower
    # log(K/KLO) endpoint, the term is minus the helper's upper endpoint.
    # Hence the inherited used lower bound is corrected_lo-tail, which is
    # still conservative. Its positivity sufficed for the original claim.
    inherited_used_lo = corrected_lo-tail
    assert 0 < inherited_used_lo < corrected_lo
    # All other used log arguments are >1 and were correctly enclosed.
    assert Q(KHI, 2**37) > 1
    # Certify over seven billion units of surplus at the lower wall.
    assert log_k_over_u(41_775_866_136, KLO+7_000_000_000)[0] > 0
    print("PASS signed-log enclosure repair check: all RL200 crossing claims unchanged")

#!/usr/bin/env python3
"""RL318 exact consumer checks for the external 2^71 convergence dependency.

This verifier does NOT reproduce Barina's exhaustive computation.
It checks only the exact arithmetic by which the frozen external result is
consumed inside the RL proof programme.
"""
from fractions import Fraction
from math import gcd, isqrt

A = 217_976_794_617
L = 137_528_045_312
R0 = 1 << 71
RL317_FIRST_FIBRE_STATE_CEILING = 1_311_372_708_449

CF_EXPECTED = [
    1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8
]


def ln_interval(x: Fraction, N=260):
    """Rigorous atanh-series enclosure for log((1+x)/(1-x))."""
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term/(2*k+1)
        term *= x2
    lo = 2*s
    tail = 2*term/(2*N+1)/(1-x2)
    return lo, lo + tail


def cf_interval(lo: Fraction, hi: Fraction, terms=30):
    out = []
    for _ in range(terms):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1
        out.append(a0)
        lo -= a0
        hi -= a0
        assert lo > 0
        lo, hi = 1/hi, 1/lo
    return out


ln2_lo, ln2_hi = ln_interval(Fraction(1,3))
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))

# Direct first-fibre elimination once n<2^71 convergence is admitted.
assert RL317_FIRST_FIBRE_STATE_CEILING < R0

# Reproduce the inherited RL131 denominator wall consumed by RL315.
qmax = isqrt((3*R0*ln2_lo.numerator - 1) // (2*ln2_lo.denominator))
assert qmax == 49_547_666_543
assert 2*qmax*qmax*ln2_lo.denominator < 3*R0*ln2_lo.numerator

# Locate the first above-resonance convergent after that denominator wall.
beta_lo = ln3_lo/ln2_hi
beta_hi = ln3_hi/ln2_lo
assert cf_interval(beta_lo, beta_hi) == CF_EXPECTED

pm2, pm1 = 0, 1
qm2, qm1 = 1, 0
conv = []
for c in CF_EXPECTED:
    p = c*pm1 + pm2
    q = c*qm1 + qm2
    conv.append((p,q))
    pm2, pm1 = pm1, p
    qm2, qm1 = qm1, q

assert conv[22] == (103_768_467_013, 65_470_613_321)  # below resonance
assert conv[23] == (A, L)                              # above resonance
assert gcd(A,L) == 1

delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0
assert delta_hi < Fraction(L, 3*R0)

# RL318 red-team: generic RL310 packing does not kill this survivor.
x = Fraction(3*(2*L-1), R0-1)
packing_rhs_lower = Fraction(1, 3*R0) + Fraction(1,9)*(x/(1+x))
assert packing_rhs_lower > Fraction(108,5) * (2*delta_hi)  # > 21.6 times needed LHS

print("RL318 external-floor consumer verifier: PASS")
print(f"external_floor=2^71={R0}")
print(f"rl317_first_fibre_state_ceiling={RL317_FIRST_FIBRE_STATE_CEILING}")
print(f"reduced_qmax={qmax}")
print(f"conditional_reduced_ell_frontier={qmax+1}")
print(f"first_above_resonance_survivor=({A},{L})")
print("generic_RL310_packing_margin_gt_21.6x=PASS")
print("scope=consumer arithmetic only; Barina exhaustive computation not rerun")

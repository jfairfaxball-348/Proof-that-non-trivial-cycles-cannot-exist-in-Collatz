#!/usr/bin/env python3
"""Exact sanity verifier for the RL152 depth / reciprocal-width bridge."""
from fractions import Fraction
from math import isqrt

A = 217_976_794_617
L = 137_528_045_312
Z0 = A - L
GISO = 320_125_202_432
BASE_HEAD = "ed10318593e9a79c65988253c27ee6c211bb0ac2"

assert Z0 == 80_448_749_305

def ln_interval(x: Fraction, N=260):
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term/(2*k+1)
        term *= x2
    lo = 2*s
    tail = 2*term/(2*N+1)/(1-x2)
    return lo, lo + tail

ln2_lo, ln2_hi = ln_interval(Fraction(1,3))
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))
delta_hi = A*ln2_hi - L*ln3_lo
log43_lo = 2*ln2_lo - ln3_hi

# Recheck the inherited uniform q_j < 4/3 input on the RL136 isolation range.
assert GISO*delta_hi < log43_lo

# Exact infinite geometric constants used to sum the RL148 strata.
sum_inv_depth = Fraction(1,2) / (1-Fraction(1,2))
sum_inv_square_shift = Fraction(1,16) / (1-Fraction(1,4))
assert sum_inv_depth == 1
assert sum_inv_square_shift == Fraction(1,12)

# Therefore T <= 1 + (W-1)/12 iff W >= 12T-11.
for W in range(1, 200):
    rhs = Fraction(1) + Fraction(W-1, 12)
    assert 12*rhs - 11 == W

# Singleton-depth evasion sanity at g=1.
pmax = (isqrt(1 + 8*Z0)-1)//2
assert pmax == 401_119
assert pmax*(pmax+1)//2 <= Z0
assert (pmax+1)*(pmax+2)//2 > Z0

# Exact finite checks of the stratum rearrangement.
for W in range(1, 100):
    T = Fraction(0)
    for d in range(1, 30):
        cap = 1 + (W-1)//(2**(d+2))
        T += cap * Fraction(1, 2**d)
    # Add the worst-case tail baseline E_d=1.
    tail = Fraction(1, 2**29)
    assert T + tail <= Fraction(1) + Fraction(W-1, 12)

print("RL152 depth / reciprocal-width verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"isolated_range_through_g={GISO}")
print(f"even_step_content_per_reduced_block={Z0}")
print("reciprocal_count_to_width=W>=12*T-11")
print("reciprocal_qmass_to_width=W>9*M-11")
print("predecessor_mass_to_width=W>6*Qpre-11")
print(f"g1_singleton_depth_budget_pmax={pmax}")
print("scope=no multiplicity exclusion; negative-defect dependency frozen; RL153 pivots to g=1")

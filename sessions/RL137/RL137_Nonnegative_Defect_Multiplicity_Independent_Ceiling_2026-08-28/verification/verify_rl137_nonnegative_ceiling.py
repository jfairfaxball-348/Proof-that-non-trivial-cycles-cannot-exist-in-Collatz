#!/usr/bin/env python3
"""Exact rational certificate for RL137's no-negative branch constant."""
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
GSTAR = 771_316_334_039
BASE_HEAD = "95775968a7344b69e01c1f880d050d1a9480708c"


def ln_interval(x: Fraction, N=260):
    x2 = x*x
    term = x
    total = Fraction(0)
    for k in range(N):
        total += term/(2*k+1)
        term *= x2
    lo = 2*total
    tail = 2*term/(2*N+1)/(1-x2)
    return lo, lo + tail


ln2_lo, ln2_hi = ln_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_interval(Fraction(1, 2))
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0

# RL134's independent one-period mechanical-weight enclosure.
x_lo = ln2_lo/L
exp1_up = 1/(1-delta_hi)
den_lo = x_lo-x_lo*x_lo/2
geom_up = 1/(2*den_lo)
rho_sum_up = 1 + exp1_up*(geom_up-1)
rho_sum_ceil = (rho_sum_up.numerator + rho_sum_up.denominator - 1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478

# Under h_j>=0, q_j<=rho_j. Exact block repetition and the ordinary cycle
# identity cancel exp(g Delta)-1, leaving m<R/[3(exp(Delta)-1)]<R/(3 Delta).
m_no_negative_up = rho_sum_up/(3*delta_lo)
assert m_no_negative_up < (1 << 75)
assert GSTAR > 320_125_202_432

print("RL137 no-negative ceiling verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"survivor_A={A} survivor_L={L}")
print(f"one_defect_endpoint_g={GSTAR}")
print(f"rho_sum_upper_ceiling={rho_sum_ceil}")
print("no_negative_branch=m<2^75 independently of g")
print("scope=conditional branch ceiling only; no multiplicity exclusion; Gate A/B open; Collatz not proved")

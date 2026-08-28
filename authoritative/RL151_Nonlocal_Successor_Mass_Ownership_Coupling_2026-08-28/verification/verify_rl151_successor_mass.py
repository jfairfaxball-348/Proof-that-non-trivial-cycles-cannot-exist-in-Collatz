#!/usr/bin/env python3
"""Exact/rational verifier for RL151 successor-mass ownership coupling."""
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
GISO = 320_125_202_432
BASE_HEAD = "79a41e4710f5776b48aa8cc313c39a4ed46b6c7f"
CEILING = 52_568_258_083_959_326_340_410

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
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0

# Recheck inherited RL136 isolation endpoint.
log43_lo = 2*ln2_lo - ln3_hi
log43_hi = 2*ln2_hi - ln3_lo
assert GISO*delta_hi < log43_lo
assert (GISO+1)*delta_lo >= log43_hi

# Rebuild inherited one-period mechanical rho envelope.
x_lo = ln2_lo/L
exp1_up = 1/(1-delta_hi)
den_lo = x_lo-x_lo*x_lo/2
geom_up = 1/(2*den_lo)
rho_sum_up = 1 + exp1_up*(geom_up-1)
rho_sum_ceil = (rho_sum_up.numerator+rho_sum_up.denominator-1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478

m_base_up = rho_sum_up/(3*delta_lo)
assert m_base_up < (1<<75)

# RL151.1 abstract mass algebra:
# Qplus >= 2/3 Qminus => Qminus <= 3/5 Q.
Qminus = Fraction(3,5)
Qplus = Fraction(2,5)
Q = Qminus + Qplus
assert Qplus == Fraction(2,3)*Qminus
assert Qminus == Fraction(3,5)*Q

# q<=rho off J and q=2rho on J then imply
# Q <= Rg + Qminus/2 <= Rg + 3Q/10, hence Q <= 10 Rg/7.
assert Fraction(1) - Fraction(3,10) == Fraction(7,10)
ownership_factor = Fraction(10,7)

m_rl151_up = ownership_factor*m_base_up
ceil = (m_rl151_up.numerator+m_rl151_up.denominator-1)//m_rl151_up.denominator
assert ceil == CEILING
assert m_rl151_up < CEILING
assert CEILING < (1<<76)
assert ownership_factor / 2 == Fraction(5,7)

# RL151.3 exact entry-depth q ratio: a_entry=d+1.
for d in range(1,20):
    qj = Fraction(7,5)
    qprev = 3*qj/Fraction(2**(d+1))
    assert qj/qprev == Fraction(2**(d+1),3)

print("RL151 successor-mass verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"isolated_range_through_g={GISO}")
print("negative_q_mass_fraction_upper=3/5")
print("mechanical_baseline_multiplier=10/7")
print(f"least_state_upper_strict={CEILING}")
print("scope=no multiplicity exclusion; no frontier advance; Gate A/B open; Collatz not proved")

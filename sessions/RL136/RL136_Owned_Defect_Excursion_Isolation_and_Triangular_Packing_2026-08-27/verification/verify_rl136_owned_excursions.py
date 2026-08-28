#!/usr/bin/env python3
"""Exact/rational verifier for RL136 owned defect-excursion results."""
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
Z = A - L
BASE_HEAD = "fb5066f21a4b63f86d5e96b51c03d87a1d5a59b5"
GSTAR = 771_316_334_039
GISO = 320_125_202_432
G75_NEW = 56_336_298_016
G75_OLD = 28_000_000_000


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


def exp_interval_pos(x: Fraction, N=24):
    """Rigorous positive-x Taylor enclosure for exp(x)."""
    assert x >= 0
    term = Fraction(1)
    s = term
    for k in range(1, N+1):
        term = term*x/k
        s += term
    nxt = term*x/(N+1)
    ratio = x/Fraction(N+2)
    assert ratio < 1
    tail = nxt/(1-ratio)
    return s, s + tail


ln2_lo, ln2_hi = ln_interval(Fraction(1,3))
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0

theta_lo = L*delta_lo/ln2_hi
theta_hi = L*delta_hi/ln2_lo
assert 5*theta_hi < 1
assert GSTAR*theta_hi < L

# RL136.1: physical isolation threshold exp(g Delta) < 4/3.
log43_lo = 2*ln2_lo - ln3_hi
log43_hi = 2*ln2_hi - ln3_lo
assert GISO*delta_hi < log43_lo
assert (GISO+1)*delta_lo >= log43_hi
# In the same range every positive determinant shell lies in the c_j=2 region.
assert GISO*theta_hi < Z

# Inherited one-period rho envelope from RL134/RL135.
x_lo = ln2_lo/L
x_hi = ln2_hi/L
exp1_up = 1/(1-delta_hi)
den_lo = x_lo-x_lo*x_lo/2
geom_up = 1/(2*den_lo)
rho_sum_up = 1 + exp1_up*(geom_up-1)
rho_sum_ceil = (rho_sum_up.numerator+rho_sum_up.denominator-1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478
m_base_up = rho_sum_up/(3*delta_lo)
assert m_base_up < (1<<75)


def triangular_candidate_up(g: int):
    """Safe O(1) upper envelope for the number of physical h=-1 phases.

    For determinant r>=1, translate count is <= g-floor(r/theta).
    Replacing theta by theta_hi and floor(x)>=x-1 gives a triangular
    envelope.  The final continuous relaxation P <= theta_hi*(g+1)^2/2
    is convenient because the resulting state envelope is monotone for g>=1.
    """
    gq = Fraction(g)
    return theta_hi*(gq+1)*(gq+1)/2


def refined_m_up(g: int):
    gq = Fraction(g)
    P = triangular_candidate_up(g)
    # exp(g Delta) <= 1/(1-g delta_hi), while exp(g Delta)-1 > g delta_lo.
    # This is deliberately coarser than direct Taylor evaluation but makes
    # the promoted through-g statement monotone and auditable.
    return m_base_up + P/(6*gq*delta_lo*(1-gq*delta_hi))

# RL136.3: improved contiguous internal least-state ceiling.
assert refined_m_up(G75_OLD) < (1<<75)
assert refined_m_up(G75_NEW) < (1<<75)
assert refined_m_up(G75_NEW+1) >= (1<<75)  # threshold of this monotone envelope

# Low-multiplicity physical windows used in the report.
def gap_ceil(n):
    # exp(n Delta)-1 < n Delta_hi/(1-n Delta_hi)
    up = Fraction(n)*delta_hi/(1-Fraction(n)*delta_hi)*(1<<75)
    return (up.numerator+up.denominator-1)//up.denominator

assert gap_ceil(1) == 33_950_221_135
assert gap_ceil(5) == 169_751_105_674
assert gap_ceil(10) == 339_502_211_350

print("RL136 owned-defect verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"survivor_A={A} survivor_L={L}")
print(f"one_defect_endpoint_g={GSTAR}")
print(f"isolated_negative_excursions_through_g={GISO}")
print("terminal_negative_requirement=(g-j/L)*theta>1; hence >5 reduced blocks remain")
print(f"triangular_m_lt_2^75_through_g={G75_NEW}")
print(f"monotone_triangular_envelope_next_integer_fails={G75_NEW+1}")
print(f"last_shell_translate_gap_upper={gap_ceil(1)}")
print(f"det_plus2_all_g_le_16_gap_upper={gap_ceil(5)}")
print(f"det_plus1_all_g_le_16_gap_upper={gap_ceil(10)}")
print("scope=no multiplicity exclusion; no frontier advance; Gate A/B open; Collatz not proved")

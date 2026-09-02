#!/usr/bin/env python3
"""
RL232 checkpoint:
H17 scalar moving-window saturation barrier.

This is a necessary-state / method-barrier certificate only.
It does NOT construct a physical orbit, realize an H17 event, prove the
combined H17 incidence cap, close the sole high branch, Gate A, Gate B,
or the global Collatz problem.
"""
from fractions import Fraction
from functools import lru_cache

# Inherited constants.
A = 217_976_794_617
L = 137_528_045_312
p = 65_470_613_321
u = 103_768_467_013
B = A - L

K_LO = 128_081_997_553
K_HI = 146_795_909_391
K0 = 2**37

# RL231 exact H17 terminal families.
TA = 20_383_222_077_370_251  # 11*3^32
TB = 27_795_302_832_777_615  # 5*3^33
H = 17
RAW_A = (5_377_348_952, 28_746_802_249)
RAW_B = (72_797_034_370, 103_818_202_602)

# RL194 exact full-period q-mass enclosure at the canonical origin.
Y0_LO = 67_236_063_233
Y0_HI = 80_336_439_250

# An algebraic witness value inside the inherited Y0 enclosure.
# This is NOT asserted to be the physical Y0.
Y_STAR = 74_000_000_000

assert A*p - L*u == 1
assert B == 80_448_749_305
assert Y0_LO < Y_STAR < Y0_HI

def ln_bounds_int(x, N=100):
    """Exact rational enclosure for ln(x), x a positive integer."""
    x = Fraction(x)
    z = (x - 1) / (x + 1)
    z2 = z*z
    term = z
    s = Fraction(0)
    for n in range(N):
        s += term / Fraction(2*n + 1)
        term *= z2
    lo = 2*s
    tail = 2*term / Fraction(2*N + 1) / (1 - z2)
    return lo, lo + tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x, N=50):
    """Exact rational enclosure for exp(x), 0<=x<1."""
    assert 0 <= x < 1
    term = Fraction(1)
    s = term
    for k in range(1, N + 1):
        term = term*x/k
        s += term
    nxt = term*x/Fraction(N + 1)
    tail = nxt/(1 - x/Fraction(N + 2))
    return s, s + tail

l2_lo, l2_hi = ln_bounds_int(2)
l3_lo, l3_hi = ln_bounds_int(3)

# delta = ln(lambda), s = ln(alpha).
d_lo = A*l2_lo - L*l3_hi
d_hi = A*l2_hi - L*l3_lo
s_lo = p*l3_lo - u*l2_hi
s_hi = p*l3_hi - u*l2_lo
assert 0 < d_lo < d_hi < Fraction(1, 1000)
assert 0 < s_lo < s_hi < Fraction(1, 1000)

alpha_lo, _ = exp_bounds_pos(s_lo)
_, alpha_hi = exp_bounds_pos(s_hi)
lambda_lo, _ = exp_bounds_pos(d_lo)
_, lambda_hi = exp_bounds_pos(d_hi)

assert 1 < alpha_lo < alpha_hi
assert 1 < lambda_lo < lambda_hi

# beta=(alpha-1)/(lambda-1), outward-rounded by monotonicity.
beta_lo = (alpha_lo - 1)/(lambda_hi - 1)
beta_hi = (alpha_hi - 1)/(lambda_lo - 1)
assert 0 < beta_lo < beta_hi

def K_bounds(T, r):
    """
    Exact enclosure for the terminal K corresponding to terminal rank r:
      K=(T/2^H)*exp(-(r*s + floor(pr/L)*delta)).
    """
    q = (p*r)//L
    x_lo = r*s_lo + q*d_lo
    x_hi = r*s_hi + q*d_hi
    assert 0 <= x_lo <= x_hi < 1
    ex_lo, _ = exp_bounds_pos(x_lo)
    _, ex_hi = exp_bounds_pos(x_hi)
    D = Fraction(T, 2**H)
    return D/ex_hi, D/ex_lo

# Exact K-compatible cores, with adjacent boundary certification.
A_CORE=(11_443_822_977,28_746_802_249)
B_CORE=(72_981_981_437,100_039_806_527)

# Strict monotonicity of K in rank follows from positive s,delta.
# Certifying the neighboring integer endpoints proves the full cuts.
assert K_bounds(TA,A_CORE[0]-1)[0] >= K_HI
assert K_bounds(TA,A_CORE[0])[1] < K_HI
assert K_bounds(TA,A_CORE[1])[0] > K_LO

assert K_bounds(TB,B_CORE[0]-1)[0] >= K_HI
assert K_bounds(TB,B_CORE[0])[1] < K_HI
assert K_bounds(TB,B_CORE[1])[0] > K_LO
assert K_bounds(TB,B_CORE[1]+1)[1] <= K_LO

# A genuine H17-A boundary restriction: the whole K-compatible A core
# lies above this explicit K floor.
A_K_FLOOR = 134_536_495_104
assert K_bounds(TA, A_CORE[1])[0] > A_K_FLOOR

# -------------------------------------------------------------------------
# Scalar moving-window barrier.
#
# RL194 proves:
#   3K_i = alpha*C_i + beta*Y_i,
#   0<C_i<Y_i,
#   Y_i = Y_0 + (lambda-1)P_i,  with 0<P_i<Y_0 canonically.
#
# If the algebraic witness Y_0=Y_STAR is inserted, then every canonical
# Y_i lies strictly between Y_STAR and lambda*Y_STAR.
#
# The next two inequalities certify that EVERY K in the inherited corridor
# has a positive C below Y for EVERY Y in that entire witness band:
#
#   beta*Y < 3K             -> C>0
#   3K < (alpha+beta)Y      -> C<Y
#
# Thus positivity of the RL194 scalar windows does not refine the K corridor.
# This is an algebraic necessary-state witness, NOT a physical q-sequence.
# -------------------------------------------------------------------------

assert beta_hi*lambda_hi*Y_STAR < 3*K_LO
assert 3*K_HI < (alpha_lo + beta_lo)*Y_STAR

# Conservative compatible-C bounds over the whole corridor/witness-Y band.
C_MIN = (3*K_LO - beta_hi*lambda_hi*Y_STAR)/alpha_hi
C_MAX = (3*K_HI - beta_lo*Y_STAR)/alpha_lo
assert 0 < C_MIN
assert C_MAX < Y_STAR

# -------------------------------------------------------------------------
# H17 zero-prefix effect on C.
#
# On a zero-defect ordinary source f_i=0. RL194 gives
#   alpha*q_(i+p)=q_i,
# while C_(i+1)-C_i=q_(i+p)-q_i.
# Hence
#   C_(i+1)-C_i=-(1-alpha^-1)q_i.
#
# An H17-A event has a 32-transition zero prefix; H17-B has 33.
# Since 0<q_i<1 canonically, the ENTIRE internal C drop of either prefix is
# less than 34*(1-alpha^-1), and therefore less than 2^-32.
# -------------------------------------------------------------------------

# 1 - alpha^-1 < alpha - 1 for alpha>1.
assert 34*(alpha_hi - 1) < Fraction(1, 2**32)

# The purely chronological disjoint-block packing baseline.
# Every A terminal is preceded by 32 zero-defect positions (block length 33);
# every B terminal is preceded by 33 (block length 34). Thus a uniform
# combined spacing consequence can use only length 33 without more state.
PACKING_CAP = L//33
assert PACKING_CAP == 4_167_516_524
assert PACKING_CAP > 1_615

def dec(x):
    return f"{float(x):.12f}"

print("PASS: RL232 H17 scalar moving-window saturation checkpoint")
print(f"H17_A_K_compatible_core={A_CORE}")
print(f"H17_B_K_compatible_core={B_CORE}")
print(f"H17_A_terminal_K_gt={A_K_FLOOR}")
print(f"witness_Y0={Y_STAR}")
print(f"compatible_C_lower_gt={dec(C_MIN)}")
print(f"compatible_C_upper_lt={dec(C_MAX)}")
print("moving_window_positivity_refines_K_corridor=no")
print("H17_internal_zero_prefix_C_drop_lt=2^-32")
print(f"uniform_disjoint_block_packing_cap={PACKING_CAP}")
print("required_combined_H17_incidence_cap=1615")
print("combined_H17_incidence_cap_1615_proved=no")
print("missing_state=long_range_endpoint_return_defect_or_owned_macro_reset_cost")
print("classification=EXACT_METHOD_BARRIER_PLUS_BOUNDARY_RESTRICTION")

#!/usr/bin/env python3
"""Exact arithmetic verifier for RL134 multiplicity determinant-strip and g=1 physical windows.

The analytic least-state prefix theorem and physical ownership arguments are
proved in the report. This script verifies the finite/rational constants used
by those arguments. Any consequence using R0=2^71 remains explicitly
conditional on that inherited external input.
"""
from fractions import Fraction
from math import gcd, isqrt

A = 217_976_794_617
L = 137_528_045_312
R0 = 1 << 71
BASE_HEAD = "196ee7fe627c09889664f3508962b7a1e12025bf"

CF_EXPECTED = [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]
U = (103_768_467_013, 65_470_613_321)  # det -1, below beta
V = (10_439_860_591, 6_586_818_670)    # det +2, above beta
W = (114_208_327_604, 72_057_431_991)  # det +1, intermediate above


def ln_interval(x: Fraction, N=260):
    """atanh-series enclosure: log((1+x)/(1-x))."""
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
    out=[]
    for _ in range(terms):
        a0=lo.numerator//lo.denominator
        a1=hi.numerator//hi.denominator
        assert a0==a1
        out.append(a0)
        lo-=a0; hi-=a0
        assert lo>0
        lo,hi=1/hi,1/lo
    return out


ln2_lo, ln2_hi = ln_interval(Fraction(1,3))
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))
beta_lo = ln3_lo/ln2_hi
beta_hi = ln3_hi/ln2_lo
assert cf_interval(beta_lo,beta_hi) == CF_EXPECTED

# Reconstruct neighborhood.
pm2,pm1=0,1
qm2,qm1=1,0
conv=[]
for a in CF_EXPECTED:
    p=a*pm1+pm2; q=a*qm1+qm2
    conv.append((p,q))
    pm2,pm1=pm1,p; qm2,qm1=qm1,q
assert conv[21] == V
assert conv[22] == U
assert conv[23] == (A,L)
assert W == (U[0]+V[0], U[1]+V[1])
assert gcd(A,L)==1
assert U[0]*L-U[1]*A == -1
assert W[0]*L-W[1]*A == 1
assert V[0]*L-V[1]*A == 2

# Rigorous survivor discrepancy.
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0
assert delta_hi < Fraction(L,3*R0)

# Incoming conditional frontier, retained.
n,d=ln2_lo.numerator,ln2_lo.denominator
qmax=isqrt((3*R0*n-1)//(2*d))
assert qmax == 49_547_666_543
assert 2*qmax*qmax*d < 3*R0*n

# RL133 floor lock retained.
assert L*delta_hi < ln2_lo

# epsilon = Delta/log2; theta = L epsilon.
eps_lo = delta_lo/ln2_hi
eps_hi = delta_hi/ln2_lo
theta_lo = L*eps_lo
theta_hi = L*eps_hi

# Certified shell thresholds.
assert 5*theta_hi < 1
assert 11*theta_hi < 2
assert 12*theta_lo > 2

# A^{-1} mod L comes from the determinant -1 neighbor U.
u, q = U
assert (q*A) % L == 1

# Base determinant-one discrepancy intervals.
s,t = W
dplus_lo = s*ln2_lo - t*ln3_hi
dplus_hi = s*ln2_hi - t*ln3_lo
dminus_lo = u*ln2_lo - q*ln3_hi
dminus_hi = u*ln2_hi - q*ln3_lo

# Exact inequalities used in the g<=11 classification.
assert dplus_lo > 6*delta_hi
assert dplus_hi < 7*delta_lo
assert dminus_lo > -6*delta_hi
assert dminus_hi < -5*delta_lo

# In particular g=6 has no off-axis positive shell.
assert dplus_lo > 6*delta_hi
assert dminus_hi + 5*delta_hi < 0
assert dminus_lo + 6*delta_lo > 0

# Check the translate parametrization on the r=-2..2 bases.
def base_for_det(r):
    jr = (-r*q) % L
    sr_num = jr*A + r
    assert sr_num % L == 0
    sr = sr_num//L
    assert sr*L-jr*A == r
    return sr,jr

assert base_for_det(-1) == U
assert base_for_det(1) == W
assert base_for_det(2) == V
rminus2 = base_for_det(-2)
assert rminus2 == (207_536_934_026,130_941_226_642)

# Safe exact upper bound on sum rho_j, inherited construction.
x_lo=ln2_lo/L
x_hi=ln2_hi/L
exp_up=1/(1-delta_hi)
den_lo=x_lo-x_lo*x_lo/2
geom_up=1/(2*den_lo)
rho_sum_up=1+exp_up*(geom_up-1)
rho_sum_ceil=(rho_sum_up.numerator+rho_sum_up.denominator-1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478

# RL134.3: m < sum rho/[3 Delta] < 2^75.
m_upper = rho_sum_up/(3*delta_lo)
assert m_upper < (1<<75)

# Conditional lower force on sum q.
t_lo = 3*R0*delta_lo

# Top-N rho selection bound:
# 1 + exp(Delta)*sum_{r=1}^{N-1} exp(-r log2/L).
# We safely omit the leading exp(-x) factor in the geometric sum.
def top_rho_upper(N):
    assert 0 <= N <= L
    if N == 0:
        return Fraction(0)
    if N == 1:
        return Fraction(1)
    n=N-1
    y=n*x_hi
    assert y < 1
    # 1-e^-y <= y-y^2/2+y^3/6 (alternating Taylor upper bound here).
    num_up=y-y*y/2+y*y*y/6
    # 1-e^-x >= x-x^2/2.
    return Fraction(1) + exp_up*(num_up/den_lo)


def shallow_min(k):
    M=1<<(k+1)
    lo,hi=0,L
    while lo<hi:
        mid=(lo+hi)//2
        cap=rho_sum_up/Fraction(M) + Fraction(M-1,M)*top_rho_upper(mid)
        if cap >= t_lo:
            hi=mid
        else:
            lo=mid+1
    # Verify exact threshold separation.
    assert lo > 0
    prev=lo-1
    cap_prev=rho_sum_up/Fraction(M) + Fraction(M-1,M)*top_rho_upper(prev)
    cap_here=rho_sum_up/Fraction(M) + Fraction(M-1,M)*top_rho_upper(lo)
    assert cap_prev < t_lo
    assert cap_here >= t_lo
    return lo

n3=shallow_min(3)
n4=shallow_min(4)
assert n3 == 176_421_674
assert n4 == 3_399_794_205

# Absolute physical windows:
# rho_j>1/2 and y_j < lambda*2^h*m/rho_j.
# lambda=e^Delta <= exp_up and m<m_upper.
assert 16*exp_up*m_upper < (1<<79)  # h<=3 => factor <2^(3+1)
assert 32*exp_up*m_upper < (1<<80)  # h<=4 => factor <2^(4+1)

# Decimal display only after all exact assertions.
theta_mid=float((theta_lo+theta_hi)/2)
print("RL134 multiplicity/physical-window verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"survivor_A={A} survivor_L={L} gcd={gcd(A,L)}")
print(f"inherited_qmax={qmax} conditional_frontier={qmax+1}")
print(f"theta=L*Delta/log2≈{theta_mid:.16f}")
print("shell_thresholds=5theta<1; 11theta<2<12theta")
print(f"det_minus1_base={U[0]}/{U[1]}")
print(f"det_plus1_base={W[0]}/{W[1]}")
print("det_plus1_discrepancy_between_6Delta_and_7Delta=PASS")
print("det_minus1_discrepancy_between_-6Delta_and_-5Delta=PASS")
print("positive_prefix_classification_g_le_6=canonical_only")
print("positive_prefix_classification_7_le_g_le_11=canonical_plus_det_pm1_translates")
print("g1_least_state_upper=m<2^75")
print(f"shallow_defect_h_le_3_min={n3}")
print(f"shallow_defect_h_le_4_min={n4}")
print("h_le_3_physical_states_below=2^79")
print("h_le_4_physical_states_below=2^80")
print("scope=no frontier advance; multiplicity not bounded; shallow populations conditional on external R#>=2^71")

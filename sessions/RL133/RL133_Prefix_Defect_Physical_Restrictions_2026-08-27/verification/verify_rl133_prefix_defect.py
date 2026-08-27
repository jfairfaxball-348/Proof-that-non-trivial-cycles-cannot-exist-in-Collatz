#!/usr/bin/env python3
"""Exact arithmetic verifier for RL133's first-survivor prefix-defect restrictions.

This verifier checks only arithmetic/combinatorial constants. The least-state
prefix theorem itself is analytic and is proved in the accompanying report.
All externally assisted consequences remain explicitly conditional on R#>=2^71.
"""
from fractions import Fraction
from math import gcd, isqrt

A = 217_976_794_617
L = 137_528_045_312
R0 = 1 << 71
CF_EXPECTED = [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]
U = (103_768_467_013, 65_470_613_321)  # previous convergent, below beta
V = (10_439_860_591, 6_586_818_670)    # convergent before U, above beta
W = (114_208_327_604, 72_057_431_991)  # U+V, intermediate above side


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
cf = cf_interval(beta_lo,beta_hi)
assert cf == CF_EXPECTED

# Reconstruct convergents exactly and locate the first survivor neighborhood.
pm2,pm1=0,1
qm2,qm1=1,0
conv=[]
for i,a in enumerate(cf):
    p=a*pm1+pm2; q=a*qm1+qm2
    conv.append((p,q))
    pm2,pm1=pm1,p; qm2,qm1=qm1,q
assert conv[21] == V
assert conv[22] == U
assert conv[23] == (A,L)
assert (2*U[0]+V[0],2*U[1]+V[1]) == (A,L)
assert W == (U[0]+V[0],U[1]+V[1])
assert gcd(A,L)==1

# Rigorous logarithmic discrepancy for the survivor.
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0
assert delta_hi < Fraction(L,3*R0)  # genuinely survives the inherited product gate

# Incoming RL131 denominator gate (rechecked compactly).
n,d=ln2_lo.numerator,ln2_lo.denominator
qmax=isqrt((3*R0*n-1)//(2*d))
assert qmax == 49_547_666_543
assert 2*qmax*qmax*d < 3*R0*n

# Floor-lock: beta lies less than 1/L^2 below A/L.
# This guarantees floor(j beta)=floor(Aj/L) for every 1<=j<L.
assert L*delta_hi < ln2_lo

# Neighbor / determinant arithmetic used in the mechanical extremal analysis.
assert U[0]*V[1]-V[0]*U[1] == -1
assert W[0]*L-W[1]*A == 1
assert U[0]*L-U[1]*A == -1
assert V[0]*L-V[1]*A == 2
assert 1 < Fraction(A,L) < 2

# Exact external-floor lower force on sum q_j.
t_lo = 3*R0*delta_lo

# Safe exact upper bound on sum rho_j.
# For proper j, Aj mod L permutes 1..L-1 and
# rho_j=exp((j/L)Delta)*2^(-(Aj mod L)/L).
# exp(Delta)<=1/(1-Delta_hi), and
# 1-exp(-x)>=x-x^2/2 for x=ln2/L.
x_lo=ln2_lo/L
exp_up=1/(1-delta_hi)
den_lo=x_lo-x_lo*x_lo/2
geom_up=1/(2*den_lo)  # upper bound for sum_{r=0}^{L-1} 2^{-r/L}
rho_sum_up=1+exp_up*(geom_up-1)
rho_sum_ceil=(rho_sum_up.numerator+rho_sum_up.denominator-1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478

# If N_k is the number of odd phases with defect h_j<=k, then
# sum q_j <= rho_sum/M + (1-1/M)N_k, M=2^(k+1).
def shallow_min(k):
    M=1<<(k+1)
    lower=(M*t_lo-rho_sum_up)/Fraction(M-1)
    return lower.numerator//lower.denominator+1

n3=shallow_min(3)
n4=shallow_min(4)
assert n3 == 176_343_262
assert n4 == 3_370_832_656

# The zero-defect rational mechanical word has a determinant-one shift.
s,t=W
assert s*L-t*A == 1
assert 0<s<A and 0<t<L
# Its length-s cyclic window counts are t except once t+1, so RL123's exact
# window-dispersion formula gives cyclic adjacent-transposition distance 1.
# Primitivity follows from gcd(A,L)=1.

print('RL133 prefix-defect verifier: PASS')
print(f'base_head=1ccace214c348589f5771f786dbbad03bb54a433')
print(f'survivor_A={A} survivor_L={L} gcd={gcd(A,L)}')
print(f'inherited_qmax={qmax} conditional_frontier={qmax+1}')
print(f'previous_below={U[0]}/{U[1]} preceding_above={V[0]}/{V[1]}')
print(f'intermediate_neighbor={W[0]}/{W[1]} determinant_to_survivor=1')
print('floor_lock=L*Delta<ln2: PASS')
print(f'rho_sum_upper_ceil={rho_sum_ceil}')
print(f'shallow_defect_h_le_3_min={n3}')
print(f'shallow_defect_h_le_4_min={n4}')
print('zero_defect_mechanical_shift_distance=1')
print('scope=coprime g=1 realization of first reduced survivor; population bounds conditional on external R#>=2^71')

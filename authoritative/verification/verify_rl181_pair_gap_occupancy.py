#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

# RL181 exact verifier.  Frozen RL180 certified inputs are used only where
# explicitly marked; all new transcendental comparisons use rational bounds.
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
t=L-p
assert A*p-L*u==1

# Frozen RL180 certified inputs for the surviving (37,0,23,-1) branch.
W_UPPER=28_070_867_755
M_UPPER=3*(2**73)
SHALLOW={
    1:73_801_609_945,
    2:81_605_820_006,
    3:84_804_722_294,
    4:86_264_134_824,
}
K0=2**37

# Exact rational logarithm enclosure (atanh series).
def ln_bounds_int(x, N=80):
    x=Fraction(x)
    z=(x-1)/(x+1)
    z2=z*z
    term=z
    s=Fraction(0)
    for n in range(N):
        s += term/Fraction(2*n+1)
        term *= z2
    lo=2*s
    tail=2*term/Fraction(2*N+1)/(1-z2)
    return lo, lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x, N=36):
    assert 0 <= x < 1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s, s+tail

def exp_interval(lo,hi):
    assert 0 <= lo <= hi < 1
    elo,_=exp_bounds_pos(lo)
    _,ehi=exp_bounds_pos(hi)
    return elo,ehi

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u*l2_hi
s_hi=p*l3_hi-u*l2_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
assert 0<s_lo<s_hi<Fraction(1,1000)

ed_lo,ed_hi=exp_interval(d_lo,d_hi)
eds_lo,eds_hi=exp_interval(d_lo+s_lo,d_hi+s_hi)
F2_hi=3*(2**37)*(ed_hi-1)

# RL181.1/2: all negative corrected-flow terms can be charged injectively to
# mechanical loss, with source/target rho ratio <= exp(s+Delta).  Thus
# N^- <= exp(s+Delta) W and every prefix K lies in this corridor.
K_LO=128_081_997_553
K_HI=146_795_909_391
lower=Fraction(K0)-eds_hi*W_UPPER/3
upper=Fraction(K0)+(eds_hi*W_UPPER+F2_hi)/3
assert lower > K_LO
assert upper < K_HI

# The residue envelope from RL180 gives omega_r<1 for r>0 once
# Delta < log(2)/L; omega_0=1 and all omega_r>1/2.
assert d_hi < l2_lo/L

# RL181.3: directed-cycle adjacency lower bounds for the shallow sets.
EDGES={k:2*n-L for k,n in SHALLOW.items()}
assert EDGES=={
    1:10_075_174_578,
    2:25_683_594_700,
    3:32_081_399_276,
    4:35_000_224_336,
}
# At most one such edge is the wrap/carry edge.  Pigeonhole over ordered
# endpoint-height types gives the following noncarry multiplicities.
def ceil_div(a,b): return (a+b-1)//b
assert ceil_div(EDGES[1]-1,4)==2_518_793_645
assert ceil_div(EDGES[4]-1,25)==1_400_008_974

# RL181.4: minimum total normalized width occupied by E shallow-shallow
# p-shift gaps.  RL180 gives omega_r < exp(Delta) 2^(-r/L), hence
# 1/omega_r > exp(-Delta) 2^(r/L).  For E selected residues the minimum
# right-hand side is the first E terms of the increasing geometric sequence.
x_lo=l2_lo/L
x_hi=l2_hi/L
_,ex1_hi=exp_interval(x_lo,x_hi)
edneg_lo=Fraction(1,ed_hi)

def recip_sum_lower(E):
    ylo=Fraction(E,L)*l2_lo
    yhi=Fraction(E,L)*l2_hi
    ey_lo,_=exp_interval(ylo,yhi)
    return edneg_lo*(ey_lo-1)/(ex1_hi-1)

# Clean certified fractions of the complete normalized width m.
OCCUPANCY={
    1:(11,256),
    2:(15,128),
    3:(5,32),
    4:(11,64),
}
for k,E in EDGES.items():
    width_lo=K_LO*recip_sum_lower(E)
    num,den=OCCUPANCY[k]
    assert den*width_lo > num*M_UPPER

print('PASS: RL181 pair-gap corridor and shallow occupancy certificate')
print('K_corridor=',K_LO,K_HI)
for k in sorted(EDGES):
    print(f'h_le_{k}_pair_edges_lower={EDGES[k]}')
print('h_le_1_noncarry_same_type_lower=2518793645')
print('h_le_4_noncarry_same_type_lower=1400008974')
print('occupancy_h_le_1_gt=11/256')
print('occupancy_h_le_2_gt=15/128')
print('occupancy_h_le_3_gt=5/32')
print('occupancy_h_le_4_gt=11/64')

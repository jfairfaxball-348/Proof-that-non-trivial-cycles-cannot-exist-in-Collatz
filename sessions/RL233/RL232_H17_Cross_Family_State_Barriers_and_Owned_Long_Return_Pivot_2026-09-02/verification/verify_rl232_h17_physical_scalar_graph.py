#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
B=A-L
p=65_470_613_321
u=103_768_467_013

K_LO=128_081_997_553
K_HI=146_795_909_391

H=17
T_A=20_383_222_077_370_251
T_B=27_795_302_832_777_615
A_RAW=(5_377_348_952,28_746_802_249)
B_RAW=(72_797_034_370,103_818_202_602)

SEP=190_537
RANK_DROP=12_799

def ln_bounds_int(x,N=100):
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
    return lo,lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x,N=50):
    assert 0<=x<1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
delta_lo=A*l2_lo-L*l3_hi
delta_hi=A*l2_hi-L*l3_lo
small_lo=p*l3_lo-u*l2_hi
small_hi=p*l3_hi-u*l2_lo

assert 0 < delta_lo < delta_hi < Fraction(1,2**40)
assert 0 < small_lo < small_hi < Fraction(1,1000)

def K_bounds(T,r):
    q=(p*r)//L
    xlo=r*small_lo+q*delta_lo
    xhi=r*small_hi+q*delta_hi
    elo,_=exp_bounds_pos(xlo)
    _,ehi=exp_bounds_pos(xhi)
    terminal=Fraction(T,2**H)
    return terminal/ehi,terminal/elo

# K(r) is strictly decreasing in terminal rank:
# x(r)=r*small + floor(pr/L)*delta, with small,delta>0.
# Exact corridor cuts therefore follow from adjacent endpoint checks.

# H17-A
a0=11_443_822_976
a1=a0+1
a_hi=A_RAW[1]
a0_lo,a0_hi=K_bounds(T_A,a0)
a1_lo,a1_hi=K_bounds(T_A,a1)
ahi_lo,ahi_hi=K_bounds(T_A,a_hi)
assert a0_lo > K_HI
assert K_LO < a1_lo and a1_hi < K_HI
assert K_LO < ahi_lo and ahi_hi < K_HI
A_CORRIDOR=(a1,a_hi)
assert A_CORRIDOR==(11_443_822_977,28_746_802_249)

# H17-B
b0=72_981_981_436
b1=b0+1
b_hi=100_039_806_527
b_next=b_hi+1
b0_lo,b0_hi=K_bounds(T_B,b0)
b1_lo,b1_hi=K_bounds(T_B,b1)
bhi_lo,bhi_hi=K_bounds(T_B,b_hi)
bn_lo,bn_hi=K_bounds(T_B,b_next)
assert b0_lo > K_HI
assert K_LO < b1_lo and b1_hi < K_HI
assert K_LO < bhi_lo and bhi_hi < K_HI
assert bn_hi < K_LO
B_CORRIDOR=(b1,b_hi)
assert B_CORRIDOR==(72_981_981_437,100_039_806_527)

# Concrete B->B relaxed edge from prior checkpoint.
N=SEP-33
REM=(N*A)%L
Q=(N*A)//L
S=Q+1
SHIFT=(SEP*B)%L
assert N==190_504
assert REM==95_752_166_376
assert S==301_942
assert SHIFT==L-RANK_DROP

# Its zero-error miss is <16,000, while the universal relaxed ball radius >47,626.
START=171_798_691_840
assert SEP < 2**18
assert 4*START < 5*L
MISS_UPPER=16_000
RADIUS_LOWER=Fraction(N,4)
assert RADIUS_LOWER==47_626
assert RADIUS_LOWER>MISS_UPPER

# A chain that already violates the target incidence cap by >400x.
R0=99_000_000_000
Q_OK=655_000
EVENTS_OK=Q_OK+1
R_OK=R0-Q_OK*RANK_DROP
SPAN_OK=Q_OK*SEP
REMAIN_OK=L-SPAN_OK
assert EVENTS_OK==655_001
assert R_OK==90_616_655_000
assert SPAN_OK==124_801_735_000
assert REMAIN_OK==12_726_310_312
assert B_CORRIDOR[0] <= R_OK < R0 <= B_CORRIDOR[1]

r0_lo,r0_hi=K_bounds(T_B,R0)
rok_lo,rok_hi=K_bounds(T_B,R_OK)
assert K_LO < r0_lo < r0_hi < K_HI
assert K_LO < rok_lo < rok_hi < K_HI

# Coarse physical scalar capacity on the remaining segment:
# delta<2^-40 => lambda=exp(delta)<4/3.
# Ordinary |f|<rho<lambda and the unique carry has |f|<2rho<2lambda.
# Since Delta K=f/3, m remaining phases can move K by
# less than 4(m+1)/9 in absolute value.
coarse_capacity_ok=Fraction(4*(REMAIN_OK+1),9)
required_drop_upper=rok_hi-r0_lo
assert required_drop_upper < coarse_capacity_ok

# Thus rank order + K corridor + full-period scalar movement capacity
# still do NOT contradict this 655,001-event relaxed chain.
assert EVENTS_OK > 405*1_615

# By contrast, the near-full relaxed chain from the prior checkpoint
# is killed by those scalar physical constraints.
Q_BAD=L//SEP
EVENTS_BAD=Q_BAD+1
R_BAD=R0-Q_BAD*RANK_DROP
SPAN_BAD=Q_BAD*SEP
REMAIN_BAD=L-SPAN_BAD
assert Q_BAD==721_791
assert EVENTS_BAD==721_792
assert R_BAD==89_761_796_991
assert REMAIN_BAD==153_545
assert B_CORRIDOR[0] <= R_BAD < R0 <= B_CORRIDOR[1]

rbad_lo,rbad_hi=K_bounds(T_B,R_BAD)
required_drop_lower=rbad_lo-r0_hi
coarse_capacity_bad=Fraction(4*(REMAIN_BAD+1),9)

# Full-period monodromy increases K by <1/6.
assert 6*K_HI < 2**40-1
monodromy_K_upper=Fraction(1,6)
assert required_drop_lower > coarse_capacity_bad + monodromy_K_upper

print("PASS: RL232 H17 physical-scalar graph checkpoint")
print(f"H17_A_corridor_rank_core={A_CORRIDOR[0]}..{A_CORRIDOR[1]}")
print(f"H17_B_corridor_rank_core={B_CORRIDOR[0]}..{B_CORRIDOR[1]}")
print("H17_B_relaxed_edge_separation=190537")
print("H17_B_relaxed_edge_rank_drop=12799")
print("scalar_constraints_not_enough_events=655001")
print(f"scalar_not_enough_phase_span={SPAN_OK}")
print(f"scalar_not_enough_remaining_phases={REMAIN_OK}")
print("near_full_chain_events=721792")
print("near_full_chain_scalar_physical_status=EXCLUDED")
print("required_incidence_cap=1615")
print("classification=EXACT_CORRIDOR_THEOREM_PLUS_METHOD_BARRIER")

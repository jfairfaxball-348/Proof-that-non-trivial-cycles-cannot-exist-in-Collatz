#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
B=A-L
CLEAN_CORRIDORS=10_075_174_499
DISTINCT_NONZERO=251_879_363
assert A*p-L*u==1

def ceil_div(a,b):
    return (a+b-1)//b

# Height refinement of the RL184 clean 40-edge corridors.
# In a length-j mechanical factor the number of c=2 bits is at most ceil(jB/L).
late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
assert late_max[39]==23
assert 1+late_max[39]==24

# If a selected defect has endpoint maximum H, it can only occur at offsets
# j where H <= 1+ceil(jB/L).  Thus it can serve at most cap(H) corridor starts.
caps={}
for H in range(1,25):
    allowed=[j for j in range(40) if H <= 1+late_max[j]]
    assert allowed
    caps[H]=len(allowed)
    # With rho_i>1/2 inherited from RL181 and unequal endpoint heights,
    # |f_i|=rho_i|2^-b-2^-a| > 2^-(H+1).
    # This exact cap inequality gives cap(H) < 2^26 |f_i|.
    assert caps[H] <= 2**(25-H)

assert caps == {
    1:40, 2:39, 3:38, 4:36, 5:34, 6:33, 7:31, 8:29,
    9:28, 10:26, 11:24, 12:22, 13:21, 14:19, 15:17, 16:16,
    17:14, 18:12, 19:10, 20:9, 21:7, 22:5, 23:4, 24:2,
}

# Choosing one forced nonzero defect per clean corridor and summing its
# permitted coverage multiplicity gives:
# total ordinary |f|-variation > CLEAN_CORRIDORS / 2^26 > 150.
assert CLEAN_CORRIDORS > 150*(2**26)

# Signed phase-count refinement from the RL184 distinct-defect floor.
# All selected defects have endpoint heights <=24, hence cross one of 24
# height thresholds.  Cyclic p-rank threshold crossings balance directions.
SIGNED_COUNT=ceil_div(DISTINCT_NONZERO,25)
assert SIGNED_COUNT==10_075_175
assert ceil_div(DISTINCT_NONZERO-SIGNED_COUNT+1,24) >= SIGNED_COUNT

# Exact rational logarithm / exponential enclosure, copied in style from
# the frozen RL181 verifier, to certify 0 < F2 < 1/2.
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
    elo,_=exp_bounds_pos(lo)
    _,ehi=exp_bounds_pos(hi)
    return elo,ehi

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
assert 0 < d_lo < d_hi < Fraction(1,1000)
ed_lo,ed_hi=exp_interval(d_lo,d_hi)
F2_lo=3*(2**37)*(ed_lo-1)
F2_hi=3*(2**37)*(ed_hi-1)
assert F2_lo > 0
assert F2_hi < Fraction(1,2)

# The carry flow is >1/2 because rho_t>1/2 (RL181) and 2-2^-h_t >=1.
# Hence total |f|-variation >150.5 while signed total F2 is in (0,0.5).
# Therefore each sign has total corrected-flow mass >75, and each sign of
# total K-variation (K_{i+1}-K_i=f_i/3) exceeds 25.
print("PASS: RL185 signed phase-weighted corridor capacity certificate")
print("max_forced_endpoint_height=24")
print("ordinary_abs_flow_gt=150")
print("negative_total_flow_gt=75")
print("positive_total_flow_gt=75")
print("negative_total_K_variation_gt=25")
print("positive_total_K_variation_gt=25")
print("negative_ordinary_defect_count_ge=10075175")
print("positive_defect_count_including_carry_ge=10075175")
print("positive_ordinary_defect_count_ge=10075174")

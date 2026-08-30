#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
B=A-L
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
CLEAN=10_075_174_499
assert A*p-L*u==1

def ceil_div(a,b):
    return (a+b-1)//b

# RL185 mechanical height envelope.
late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
assert height_envelope[39]==24

# RL186.1/RL186.2: first-defect arithmetic in the late tail.
# If tau>0, the zero prefix gives 2^D C_tau = 3^tau C_0.
# Since the first defect has odd C_tau, D=v2(C_0) and
# C_tau=3^tau*oddpart(C_0).  Enumerate every admissible shallow C_0
# divisible by 2^tau for tau>=28 and every H allowed by the physical
# normalized-gap corridor and the RL185 mechanical envelope.
tail_H={}
for tau in range(28,40):
    possible=set()
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        kmin=lo//step+1
        kmax=(hi-1)//step
        for k in range(kmin,kmax+1):
            C0=k*step
            D=(C0 & -C0).bit_length()-1
            odd=C0>>D
            Ct=(3**tau)*odd
            for H in range(1,height_envelope[tau]+1):
                if GAP_LOWER*(2**H) < Ct < GAP_UPPER*(2**H):
                    possible.add(H)
    tail_H[tau]=tuple(sorted(possible))

expected_tail={
    28:(7,8,9,10,11,12,13,14,15,16,17,18),
    29:(8,9,10,11,12,13,14,15,16,17,18),
    30:(10,12,13,14,15,16,17,18,19),
    31:(12,13,14,15,16,17,18,19,20),
    32:(13,15,16,17,18,19,20),
    33:(15,16,17,18,19,20,21),
    34:(16,18,19,20,21),
    35:(18,19,20,21,22),
    36:(19,20,21,22),
    37:(21,23),
    38:(23,),
    39:(24,),
}
assert tail_H==expected_tail

# Conservative early offsets plus exact late-tail vocabulary.
allowed_by_tau={}
for tau in range(40):
    if tau<28:
        allowed_by_tau[tau]=tuple(range(1,height_envelope[tau]+1))
    else:
        allowed_by_tau[tau]=tail_H[tau]

# A physical first defect at height H can discharge at most one start per tau.
caps={H:sum(H in allowed_by_tau[t] for t in range(40)) for H in range(1,25)}
expected_caps={
    1:28,2:27,3:26,4:24,5:22,6:21,7:20,8:19,
    9:18,10:17,11:14,12:14,13:14,14:11,15:11,16:11,
    17:8,18:8,19:7,20:6,21:5,22:2,23:2,24:1,
}
assert caps==expected_caps
for H in range(1,25):
    assert caps[H] <= 2**(24-H)

# Baseline first-defect charging already doubles RL185.
assert CLEAN > 300*(2**25)

# RL186.4: the inherited tau=39 extremal start has C0=2^39 and d0=1.
# Its next zero-edge numerator is 3*2^38.  If that edge were shallow
# (common height <=1), its normalized gap would exceed GAP_UPPER.
C1=3*(2**38)
assert C1//2 > GAP_UPPER
# Hence a tau=39 shallow start is isolated from later shallow starts in
# its zero block.  A zero block contributing tau>=37 shallow starts has
# density at most 2/39 around the cyclic period.
TAIL37_CAP=(2*L)//39
assert TAIL37_CAP==7_052_720_272
LOW_COUNT=CLEAN-TAIL37_CAP
assert LOW_COUNT==3_022_454_227

# H<=22 defects have cap(H)*2^(H+1) <= 5*2^22.
low_charge=max(caps[H]*(2**(H+1)) for H in range(1,23))
high_charge=max(caps[H]*(2**(H+1)) for H in (23,24))
assert low_charge==5*(2**22)==20_971_520
assert high_charge==2**25==33_554_432
flow_floor=Fraction(LOW_COUNT,low_charge)+Fraction(TAIL37_CAP,high_charge)
assert flow_floor==Fraction(7_430_404_397,20_971_520)
assert flow_floor>354

# Re-certify inherited exact total 0<F2<1/2 for the signed consumer.
def ln_bounds_int(x,N=80):
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
def exp_bounds_pos(x,N=36):
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
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
ed_lo,_=exp_bounds_pos(d_lo)
_,ed_hi=exp_bounds_pos(d_hi)
F2_lo=3*(2**37)*(ed_lo-1)
F2_hi=3*(2**37)*(ed_hi-1)
assert F2_lo>0
assert F2_hi<Fraction(1,2)

# Carry flow >1/2 is inherited from rho_t>1/2.
# Ordinary |f| >354, so full |f| >354.5 while net F2<0.5.
# Therefore each signed flow mass >177 and each K-directional variation >59.
print("PASS: RL186 first-defect tail capacity certificate")
print("tau37_heights=21,23")
print("tau38_heights=23")
print("tau39_height=24")
print("first_defect_cap_H23=2")
print("first_defect_cap_H24=1")
print("tau_ge_37_clean_starts_le=7052720272")
print("tau_le_36_clean_starts_ge=3022454227")
print("ordinary_abs_flow_gt=354")
print("negative_total_flow_gt=177")
print("positive_total_flow_gt=177")
print("negative_total_K_variation_gt=59")
print("positive_total_K_variation_gt=59")

#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
CLEAN=10_075_174_499
ELO=72_797_034_370
EHI=103_818_202_602
N36=7_238_318_174
N37=7_052_720_272

assert B==80_448_749_305
assert R==57_079_296_007

def overlap(sep):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        lo=max(ELO,ELO-sh+k*L)
        hi=min(EHI,EHI-sh+k*L)
        if lo<=hi:
            out.append((lo,hi))
    return sh,out

sh41,ov41=overlap(41)
assert sh41==135_253_679_329
assert ov41==[(75_071_400_353,103_818_202_602)]
assert 40-35 >= 4

def cbit(r):
    return 1 if r<R else 2

def word4(r):
    return tuple(cbit((r+j*B)%L) for j in range(4))

lo,hi=ov41[0]
assert word4(lo)==(2,1,2,1)
assert word4(90_789_138_715)==(2,1,2,1)
assert word4(90_789_138_716)==(2,1,2,2)
assert word4(hi)==(2,1,2,2)

events={lo,hi+1}
for j in range(4):
    for target in (R,0):
        for k in range(-5,6):
            x=target-j*B+k*L
            if lo < x <= hi:
                events.add(x)
events=sorted(events)
parts=[]
for a,b in zip(events[:-1],events[1:]):
    if a<=b-1:
        parts.append((a,b-1,word4(a)))
assert parts==[
    (75_071_400_353,90_789_138_715,(2,1,2,1)),
    (90_789_138_716,103_818_202_602,(2,1,2,2)),
]

delta0=Fraction(3**37,2**21)

def evolve(word):
    center=delta0
    radius=Fraction(0)
    for c in word:
        center=Fraction(3,2**c)*center
        radius=Fraction(3,2**c)*radius+Fraction(1,2**c)
    return center,radius

c2121,r2121=evolve((2,1,2,1))
c2122,r2122=evolve((2,1,2,2))
assert c2121==Fraction(3**41,2**27)
assert r2121==Fraction(119,64)
assert c2122==Fraction(3**41,2**28)
assert r2122==Fraction(119,128)

T37=Fraction(2**37)
T38=Fraction(2**38)
N=2**65-3**41
assert N==420_491_770_248_316_829
assert abs(c2121-T38)==Fraction(N,2**27)>r2121
assert abs(c2121-T37)>r2121
assert abs(c2122-T37)==Fraction(N,2**28)>r2122
assert abs(c2122-T38)>r2122

sh42,ov42=overlap(42)
assert sh42==78_174_383_322
assert ov42==[]
assert min(sh42,L-sh42)==59_353_661_990 > EHI-ELO

for S in range(36,1000):
    assert Fraction(3,43) >= (Fraction(3)+Fraction(2*S,37))/Fraction(38+S)
assert 25*36-555>0

N35=(3*L)//43
assert (3*L)%43==21
assert N35==9_594_979_905
early=CLEAN-N35
assert early==480_194_594

U=Fraction(1,2**25)
flat=Fraction(1,3*(2**22))
assert flat==Fraction(8,3)*U
assert 2*flat+flat==8*U

a=CLEAN-N35
b=N35-N36
assert a==480_194_594
assert b==2_356_661_731
slope=Fraction(b)-Fraction(a,2)
assert slope==2_116_564_434>0

ymax=Fraction(8,3)*U
x_at_ymax=(8*U-ymax)/2
assert ymax==flat and x_at_ymax==flat

ordinary_floor=Fraction(2_787_212_689,6_291_456)
assert ordinary_floor>443

print("PASS: RL189 phase-41/42 spacing and N35 charging certificate")
print("terminal_spacing_ge=43")
print("N35_le=9594979905")
print("clean_tau_le_34_ge=480194594")
print("two_level_short_weight_opt=1/(3*2^22)")
print("ordinary_abs_flow_inherited_gt=2787212689/6291456")

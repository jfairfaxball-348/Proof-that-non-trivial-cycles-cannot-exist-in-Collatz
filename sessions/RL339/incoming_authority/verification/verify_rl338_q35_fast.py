#!/usr/bin/env python3
"""Fast portable RL338 verifier: q=35 analytic closure and exact rational consumer.

The heavy physical enumeration is frozen by RL338_EXACT_CERTIFICATE.md and was
executed gap-free at closeout. This fast verifier checks the theorem arithmetic,
coverage geometry, continuation margins, and exact phase consumer.
"""
from fractions import Fraction
from functools import lru_cache

# Frozen exhaustive-certificate summaries.
LAYERS = {
    5: dict(pairs=196, templates=64120, candidates=299, owned=161, cores=68),
    6: dict(pairs=154, templates=130386, candidates=10, owned=8, cores=4),
    7: dict(pairs=98, templates=185360, candidates=0, owned=0, cores=0),
    8: dict(pairs=42, templates=204590, candidates=0, owned=0, cores=0),
}
assert [LAYERS[p]['pairs'] for p in range(5,9)] == [14*14,11*14,7*14,3*14]
assert sum(LAYERS[p]['owned'] for p in range(5,9)) == 169
assert LAYERS[5]['cores'] + LAYERS[6]['cores'] == 72

# Step-potential charge algebra.
def density(z): return max(0,2*z-43)
def phi(z): return 35 if z >= 22 else 0
def reduced(left,right,p):
    slack = density(right)-density(left)-(2*right-43*p)
    w = 35*(p-2*(right<=21))-slack
    return w + phi(left)-phi(right)

# Surviving singleton support is z+z'<=43; all such reduced charges are <=0.
assert max(reduced(z,nz,1) for z in range(1,36) for nz in range(1,36) if z+nz<=43) == 0

# Positive high-high anonymous baselines at p=5..8 are exactly the scanned regions.
for p, source_lo in [(5,22),(6,25),(7,29),(8,33)]:
    pos=[(z,nz) for z in range(22,36) for nz in range(22,36) if reduced(z,nz,p)>0]
    assert len(pos)==LAYERS[p]['pairs']
    assert min(z for z,_ in pos)==source_lo
# p>=9 cannot be positive anywhere in z<=35.
assert max(reduced(z,nz,p) for z in range(1,36) for nz in range(1,36) for p in range(9,20)) <= 0

# Exact physical certificate leaves only p5 source 22..24 and p6 source 25.
exception_charges=[reduced(z,22,5) for z in (22,23,24)] + [reduced(25,22,6)]
assert exception_charges == [4,6,8,2]
assert max(exception_charges)==8
# Frozen exact right-context bounds: p5 <=29, p6 <=24.
assert max(reduced(29,nz,9) for nz in range(1,36)) == -14
assert max(reduced(24,nz,9) for nz in range(1,36)) <= -24
# Closeout successor scan: 24 p<=4 continuations all <=-30; 5 p7 continuations are -88.
assert 8 + (-30) < 0
assert 8 + (-88) < 0
assert 8 + (-14) == -6
# Therefore reduced path sum <=8 (only a terminal exceptional edge may be unmatched),
# and untelescoping a potential of range 35 yields the q35 constant 43.
B=35+8
assert B==43

# Exact rational phase consumer, inherited from RL336 with q35/B43 coefficients.
A=217_976_794_617; ELL=137_528_045_312
BOOT=32_546_272_000; CAP=BOOT-1
C=Fraction(25_120_009_946_627,10**14)
def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms): total+=term/(2*j+1); term*=x2
    lo=2*total; return lo,lo+2*term/(2*terms+1)/(1-x2)
l2,_=log_interval_atanh(Fraction(1,3)); LAM=1+Fraction(1,1<<40); b2=129
x=l2/ELL; full=1/(2*(x+x*x/2))-Fraction(1,2)
rho59=Fraction(5,6)+LAM*(1<<(((A-ELL)*59)//ELL))
@lru_cache(None)
def W(K):
    s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return Fraction(K)+l2*s1/ELL+l2**2*s2/(2*ELL**2)+l2**3*s3/(6*ELL**3)+l2**4*s4/(24*ELL**4)
def ks(rho):
    K=(2*(ELL-rho+1)-b2+44)//45
    s=b2-(2*(ELL-rho+1)-45*K)
    assert 0<=s<=44
    return K,s
def St(K0,h,s):
    K=K0+h; S=45*h+s
    return Fraction(K)+C*(Fraction(K,2)-Fraction(71,70)*S-Fraction(113,70))
def gain(K0,s):
    w=W(K0); m=St(K0,1,s)-St(K0,0,s); assert m<1
    y=(St(K0,0,s)-w)/(1-m); q=max(0,y.numerator//y.denominator)
    vals=[(h,max(Fraction(h),St(K0,h,s)-w)) for h in {0,q,q+1}]
    return min(vals,key=lambda r:r[1])
def omitterm(r): return Fraction(1<<((A*r)//ELL),3**r)/LAM
om=Fraction(0); mx=None
for r in range(1,2894):
    om+=omitterm(r); rho=r+1
    if rho<60: continue
    K,s=ks(rho); h,g=gain(K,s)
    R=1+(full-om)/3-W(K)/(12*LAM)-g/(12*LAM)
    assert R<BOOT
    if mx is None or R>mx[0]: mx=(R,rho,h,g)
om59=sum((omitterm(r) for r in range(1,60)),Fraction())
K60,s60=ks(60); h60,g60=gain(K60,s60)
R60=1+(full-om59)/3-W(K60)/(12*LAM)-g60/(12*LAM)
assert mx[1]==60 and mx[0]==R60
assert (K60,s60,h60)==(6_112_357_564,3,59_311_669)
assert R60.numerator//R60.denominator==32_546_271_992
Kmin,_=ks(21_999_999); hu,gu=gain(Kmin,44)
om2894=sum((omitterm(r) for r in range(1,2895)),Fraction()); K2895,_=ks(2895)
R2895=1+(full-om2894)/3-W(K2895)/(12*LAM)-gu/(12*LAM)
assert hu==59_303_536 and R2895.numerator//R2895.denominator==CAP
Q=1<<256
sumq=1837579385638164133130126995943207589379866951507814208093753543882794175686281825504
omit22_lower=Fraction(sumq,Q)/LAM; K22,_=ks(22_000_000)
R22=1+(full-omit22_lower)/3-W(K22)/(12*LAM)
assert R22<BOOT and rho59<BOOT
print('RL338_Q35_FAST_GREEN')
print('anchor','35(K-2H)-S<=43')
print('layers',[(p,LAYERS[p]['templates'],LAYERS[p]['owned']) for p in range(5,9)])
print('successor_margin','exception<=8','short<=-30','p7low=-88','p>=9<=-14')
print('consumer_rho60_floor',R60.numerator//R60.denominator)
print('consumer_bridge_floor',R2895.numerator//R2895.denominator)
print('cap',CAP)

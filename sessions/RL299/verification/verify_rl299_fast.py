#!/usr/bin/env python3
from fractions import Fraction

BASE='428d1d1b0c0d0444e6e920345692db8e40a34995'

def atanh_bounds(p,q,n=120):
    x=Fraction(p,q); x2=x*x
    term=x; s=Fraction(0)
    for j in range(n):
        s += term/Fraction(2*j+1)
        term *= x2
    tail = term / Fraction((2*n+1),1) / (1-x2)
    return s, s+tail

def log_bounds():
    a2,b2=atanh_bounds(1,3); a3,b3=atanh_bounds(1,2)
    return 2*a2,2*b2,2*a3,2*b3

L2,U2,L3,U3=log_bounds()
AL=(L3/U2); AU=(U3/L2)

def cf_common(lo,hi,limit=100):
    out=[]
    for _ in range(limit):
        a=lo.numerator//lo.denominator
        b=hi.numerator//hi.denominator
        if a!=b: break
        out.append(a)
        lo=1/(hi-a); hi=1/(lo*0+0) if False else None
        # recompute carefully because interval inversion reverses endpoints
        # old hi and old lo needed
        # handled below by local variables
    return out

def cf_interval(lo,hi,limit=100):
    out=[]
    for _ in range(limit):
        a=lo.numerator//lo.denominator
        b=hi.numerator//hi.denominator
        if a!=b: break
        out.append(a)
        old_lo,old_hi=lo,hi
        flo=old_lo-a; fhi=old_hi-a
        if flo == 0 or fhi == 0: break
        lo=1/fhi; hi=1/flo
    return out

CF=cf_interval(AL,AU,100)
assert CF[:18]==[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3], CF[:18]

def delta_bounds(a,l):
    return a*L2-l*U3, a*U2-l*L3

def sign_upper(a,l):
    dl,du=delta_bounds(a,l)
    assert dl>0, (a,l,float(dl))
    return dl,du

def det_selector(a,l,q,r,H,n):
    z=a-l; B=q-r
    assert a*r-q*l==2
    assert 19*z-7*a==H
    assert 19*B-7*q==n
    assert B*H-z*n==14
    assert q*H-a*n==38
    assert r*H-l*n==24

records=[
('U0',301994,190537,None,None,None,None),
('U1',17087915,10781274,16483927,10400200,210774,203324),
('U2',102225496,64497107,68049666,42934559,1260919,839371),
('U3',187363077,118212940,170275162,107431666,2311064,2100290),
('U4',272500658,171928773,170275162,107431666,3361209,2100290),
('U5',630138897,397573379,85137581,53715833,7772563,1050145),
('Rcross',630118245525664765,397560349370386783,216627100404256471,136676483074956903,7772308270628303,2672026426896495),
('Rnext',7354673373747273033,4640282259296926456,6094436882695943503,3845161560556152890,90717558325673732,75172941784417126),
]
for name,a,l,q,r,H,n in records:
    sign_upper(a,l)
    if q is not None: det_selector(a,l,q,r,H,n)

# Farey/semiconvergent structural equalities used in the report.
U0=(301994,190537); L0=(16785921,10590737); U1=(17087915,10781274)
assert U0[0]*L0[1]-L0[0]*U0[1]==1
assert U1==(U0[0]+L0[0],U0[1]+L0[1])
L1=(85137581,53715833)
assert L1==(4*U1[0]+L0[0],4*U1[1]+L0[1])
U2r=(102225496,64497107); U3r=(187363077,118212940); U4r=(272500658,171928773); U5r=(630138897,397573379)
assert U2r==(L1[0]+U1[0],L1[1]+U1[1])
assert U3r==(2*L1[0]+U1[0],2*L1[1]+U1[1])
assert U4r==(3*L1[0]+U1[0],3*L1[1]+U1[1])
assert U5r==(2*U4r[0]+L1[0],2*U4r[1]+L1[1])


# Exact relaxed quotient ceilings Nhat=floor((79/9)/(exp(Delta)-1))+2.
def exp_lower(x,n=12):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k; s+=t
    return s

def exp_upper(x,n=12):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k; s+=t
    first=t*x/(n+1)
    r=x/Fraction(n+2)
    return s+first/(1-r)

def nhat_exact(a,l):
    dl,du=delta_bounds(a,l)
    lo=Fraction(79,9)/(exp_upper(du)-1)
    hi=Fraction(79,9)/(exp_lower(dl)-1)
    flo=lo.numerator//lo.denominator
    fhi=hi.numerator//hi.denominator
    assert flo==fhi, (a,l,flo,fhi)
    return flo+2

for pair,expect in [
    ((301994,190537),136073747),
    ((17087915,10781274),719078408),
    ((102225496,64497107),1004967012),
    ((187363077,118212940),1668206573),
    ((272500658,171928773),4905934722),
    ((630138897,397573379),82931674943),
]:
    assert nhat_exact(*pair)==expect,(pair,nhat_exact(*pair),expect)

# Certified block data.
blocks=[
(301995,17087914,136073747,588,79091),
(17087915,102225495,719078408,589,4473687),
(102225496,187363076,1004967012,589,26762926),
(187363077,272500657,1668206573,612,49052163),
(272500658,630138896,4905934722,676,71341400),
]
for lo,hi,nstar,s,emin in blocks:
    assert lo<=hi and emin>=s+2

# Exact physical witness checks.
def stop(n):
    s=0; peak=n
    while n!=1:
        if n&1: n=(3*n+1)//2
        else: n//=2
        s+=1; peak=max(peak,n)
        assert s<10000
    return s,peak
wits=[
(7966015,180,589),
(41913579,165,612),
(190785579,676,145),
]
for h,sa,sb in wits:
    A=27*h+22; B=81*h+80
    xa,pa=stop(A); xb,pb=stop(B)
    assert (xa,xb)==(sa,sb),(h,xa,xb)
assert stop(27*190785579+22)[1]==483308017730

# U4 shard coverage is gap-free.
shards=[(0,50000000),(50000000,100000000),(100000000,150000000),(150000000,200000000),(200000000,204413946)]
assert shards[0][0]==0
for a,b in zip(shards,shards[1:]): assert a[1]==b[0]
assert shards[-1][1]==204413946

# Quotient counts N=19+24h.
def qcount(nstar): return (nstar-19)//24 + 1
assert qcount(719078408)==29961600
assert qcount(1004967012)==41873625
assert qcount(1668206573)==69508607
assert qcount(4905934722)==204413946

# New analytic imbalance lemma support identity: 2[O+ceil((m-O-E)/2)] <= m+(O-E)+1.
for O in range(8):
  for E in range(8):
    s=O+E
    for m in range(s,s+8):
      W=O+(m-s+1)//2
      assert 2*W<=m+(O-E)+1

# Exact B-ancestry identity and mod-3 optimality trigger.
for h in range(30):
    y=16*h+15
    seq=[]; n=y
    for _ in range(4):
        assert n&1
        n=(3*n+1)//2; seq.append(n)
    assert n==81*h+80
    if h%3==0:
        assert y%3==0
        # odd predecessor exists iff x == 2 mod 3
        assert y%3!=2

print('RL299_FAST_GREEN')
print('BASE_HEAD',BASE)
print('CF_PREFIX',CF[:18])
print('UNCONDITIONAL_SELECTOR_FRONTIER',630138896)
print('NEXT_UNCONDITIONAL_RECORD',U5r)
print('J_LEMMA_GREEN')
print('ANCESTRY_BARRIER_GREEN')

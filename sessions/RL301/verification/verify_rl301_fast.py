#!/usr/bin/env python3
from fractions import Fraction

BASE_HEAD = "056aaa4132ba5bccf11e3c8678f500e6ecfd7797"
BASE_TREE = "342d852af648746aba850007fe0fbe42c213b7cc"
INCOMING_FRONTIER = 206745572560704146
PROMOTED_FRONTIER = 7354673373747273032
EXTERNAL_LIMIT = 46_500_000_000_000_000_000
EXTERNAL_RECORD = 28_019_077_177_231_758_495
EXTERNAL_RECORD_DELAY = 2456
CF_EXPECT = [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8,1,11,1,20,2,1,10,1,4,1,1,1,1,1]
EXPECTED_RECORDS = [
    (206745572560704147,130441933147714940),
    (630118245525664765,397560349370386783),
    (7354673373747273033,4640282259296926456),
    (43497921996957973433,27444133206411171953),
    (123139092617126647266,77692117359936589403),
    (325919355854421968365,205632218873398596256),
]
EXPECTED_NHAT = {
    EXPECTED_RECORDS[0]: 4_894_841_535_700_125_438,
    EXPECTED_RECORDS[1]: 57_867_840_550_427_715_479,
    EXPECTED_RECORDS[2]: 325_482_729_518_061_951_549,
    EXPECTED_RECORDS[3]: 867_000_121_638_085_493_948,
    EXPECTED_RECORDS[4]: 2_578_333_030_765_879_156_031,
    EXPECTED_RECORDS[5]: 98_618_348_177_372_075_480_759,
}
EXPECTED_YMAX = {
    EXPECTED_RECORDS[0]: 3_263_227_690_466_750_287,
    EXPECTED_RECORDS[1]: 38_578_560_366_951_810_319,
    EXPECTED_RECORDS[2]: 216_988_486_345_374_634_367,
    EXPECTED_RECORDS[3]: 578_000_081_092_056_995_967,
    EXPECTED_RECORDS[4]: 1_718_888_687_177_252_770_687,
    EXPECTED_RECORDS[5]: 65_745_565_451_581_383_653_839,
}

def atanh_bounds(p,q,n=260):
    x=Fraction(p,q); x2=x*x
    term=x; s=Fraction(0)
    for j in range(n):
        s += term/Fraction(2*j+1)
        term *= x2
    tail = term/Fraction(2*n+1)/(1-x2)
    return s,s+tail

def log_bounds():
    a2,b2=atanh_bounds(1,3)
    a3,b3=atanh_bounds(1,2)
    return 2*a2,2*b2,2*a3,2*b3

L2,U2,L3,U3=log_bounds()
AL,AU=L3/U2,U3/L2

def cf_interval(lo,hi,limit=100):
    out=[]
    for _ in range(limit):
        a=lo.numerator//lo.denominator
        b=hi.numerator//hi.denominator
        if a!=b:
            break
        out.append(a)
        flo=lo-a; fhi=hi-a
        if flo==0 or fhi==0:
            break
        lo=1/fhi; hi=1/flo
    return out

CF=cf_interval(AL,AU,100)
assert CF[:len(CF_EXPECT)]==CF_EXPECT

def delta_bounds(a,l):
    return a*L2-l*U3, a*U2-l*L3

def semiconvergents(cf):
    pm2,pm1=0,1; qm2,qm1=1,0
    out=[]
    for n,an in enumerate(cf):
        for t in range(1,an+1):
            p=pm2+t*pm1; q=qm2+t*qm1
            if q:
                out.append((p,q,n,t))
        p=pm2+an*pm1; q=qm2+an*qm1
        pm2,pm1=pm1,p; qm2,qm1=qm1,q
    return out

upper=[]
for a,l,n,t in semiconvergents(CF_EXPECT):
    dl,du=delta_bounds(a,l)
    if dl>0:
        upper.append((a,l,n,t,dl,du))
    else:
        assert du<0, ("ambiguous sign",a,l)
upper.sort()
records=[]; best_lo=best_hi=None
for a,l,n,t,dl,du in upper:
    if best_lo is None:
        records.append((a,l)); best_lo,best_hi=dl,du
    elif du < best_lo:
        records.append((a,l)); best_lo,best_hi=dl,du
    else:
        assert dl >= best_hi, ("ambiguous record comparison",a,l)

tail=[p for p in records if EXPECTED_RECORDS[0][0] <= p[0] <= EXPECTED_RECORDS[-1][0]]
assert tail==EXPECTED_RECORDS, (tail,EXPECTED_RECORDS)

def exp_lower(x,n=18):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k; s+=t
    return s

def exp_upper(x,n=18):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k; s+=t
    first=t*x/(n+1); r=x/Fraction(n+2)
    assert r<1
    return s+first/(1-r)

def nhat_exact(a,l):
    dl,du=delta_bounds(a,l); assert dl>0
    lo=Fraction(79,9)/(exp_upper(du)-1)
    hi=Fraction(79,9)/(exp_lower(dl)-1)
    flo=lo.numerator//lo.denominator; fhi=hi.numerator//hi.denominator
    assert flo==fhi, ("ambiguous Nhat",a,l,flo,fhi)
    return flo+2

def physical_values(nhat):
    h=(nhat-19)//24
    nmax=19+24*h
    A=27*h+22
    B=81*h+80
    Y=16*h+15
    return h,nmax,A,B,Y

for rec in EXPECTED_RECORDS:
    n=nhat_exact(*rec)
    assert n==EXPECTED_NHAT[rec], (rec,n)
    y=physical_values(n)[-1]
    assert y==EXPECTED_YMAX[rec], (rec,y)

# Exact four-odd-step B ancestry as affine forms a*h+b.
def odd_affine(pair):
    a,b=pair
    assert a%2==0 and b%2==1
    return (3*a//2,(3*b+1)//2)
p=(16,15)
chain=[p]
for _ in range(4):
    p=odd_affine(p); chain.append(p)
assert chain==[(16,15),(24,23),(36,35),(54,53),(81,80)]

# New certificate covers the first two record blocks and fails at the next record.
assert EXPECTED_YMAX[EXPECTED_RECORDS[0]] < EXTERNAL_LIMIT
assert EXPECTED_YMAX[EXPECTED_RECORDS[1]] < EXTERNAL_LIMIT
assert EXPECTED_YMAX[EXPECTED_RECORDS[2]] > EXTERNAL_LIMIT
assert PROMOTED_FRONTIER == EXPECTED_RECORDS[2][0]-1
assert INCOMING_FRONTIER == EXPECTED_RECORDS[0][0]-1

# Replay load-bearing external holder delay.
def ordinary_delay(n):
    s=0
    while n!=1:
        n=n//2 if n%2==0 else 3*n+1
        s+=1
        assert s<100000
    return s
assert ordinary_delay(EXTERNAL_RECORD)==EXTERNAL_RECORD_DELAY

# D(Y)<=2456 => half stopping <=2456 => J_Y<=2456; four initial odd
# half-steps are removed at B0, hence J_B<=2452.
JY_BOUND=EXTERNAL_RECORD_DELAY
JB_BOUND=JY_BOUND-4
assert JB_BOUND==2452
REQUIRED=JB_BOUND+2
assert REQUIRED==2454
# Retained selector floor ell >= ceil(147a/233) implies
# 2ell-a+26 >= 61a/233 + 26; check at the smallest newly exposed a.
a0=EXPECTED_RECORDS[0][0]
assert Fraction(61*a0,233)+26 > REQUIRED

print("RL301_FAST_GREEN")
print("BASE_HEAD",BASE_HEAD)
print("BASE_TREE",BASE_TREE)
print("CF_PREFIX_LEN",len(CF_EXPECT))
print("FIRST_NEW_RECORD",EXPECTED_RECORDS[0])
print("SECOND_NEW_RECORD",EXPECTED_RECORDS[1])
print("BOUNDARY_RECORD",EXPECTED_RECORDS[2])
print("EXTERNAL_LIMIT",EXTERNAL_LIMIT)
print("EXTERNAL_RECORD",EXTERNAL_RECORD,"DELAY",EXTERNAL_RECORD_DELAY)
print("SECOND_RECORD_NHAT",EXPECTED_NHAT[EXPECTED_RECORDS[1]])
print("SECOND_RECORD_YMAX",EXPECTED_YMAX[EXPECTED_RECORDS[1]])
print("BOUNDARY_NHAT",EXPECTED_NHAT[EXPECTED_RECORDS[2]])
print("BOUNDARY_YMAX",EXPECTED_YMAX[EXPECTED_RECORDS[2]])
print("JB_BOUND",JB_BOUND)
print("PROMOTED_EXTERNAL_CERT_FRONTIER",PROMOTED_FRONTIER)
print("LADDER_NEXT_YMAX",EXPECTED_YMAX[EXPECTED_RECORDS[3]],EXPECTED_YMAX[EXPECTED_RECORDS[4]],EXPECTED_YMAX[EXPECTED_RECORDS[5]])

#!/usr/bin/env python3
from fractions import Fraction

BASE_HEAD = "d1564092e4f43fb2ab2347398455ccb7c4f1a211"
BASE_TREE = "4758d988ce85327975d68a724bc17ee86d86c851"
CF_EXPECT = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, 1, 1, 15, 1, 9, 2, 5, 7, 1, 1, 4, 8, 1, 11, 1, 20]
EXPECTED_RECORDS = [
    (630138897,397573379),
    (10439860591,6586818670),
    (114208327604,72057431991),
    (217976794617,137528045312),
    (1411629234715,890638885193),
    (2605281674813,1643749725074),
    (3798934114911,2396860564955),
    (4992586555009,3149971404836),
    (6186238995107,3903082244717),
    (7379891435205,4656193084598),
    (8573543875303,5409303924479),
    (18340740190704,11571718688839),
    (101470897268921,64021008208555),
    (184601054347138,116470297728271),
    (267731211425355,168919587247987),
    (350861368503572,221368876767703),
    (433991525581789,273818166287419),
    (517121682660006,326267455807135),
    (600251839738223,378716745326851),
    (683381996816440,431166034846567),
    (1449894150711097,914781359212850),
    (2216406304605754,1398396683579133),
    (2982918458500411,1882012007945416),
    (3749430612395068,2365627332311699),
    (4515942766289725,2849242656677982),
    (5282454920184382,3332857981044265),
    (6048967074079039,3816473305410548),
    (6815479227973696,4300088629776831),
    (7581991381868353,4783703954143114),
    (8348503535763010,5267319278509397),
    (9115015689657667,5750934602875680),
    (18996543533209991,11985484530117643),
    (28878071376762315,18220034457359606),
    (38759599220314639,24454584384601569),
    (48641127063866963,30689134311843532),
    (58522654907419287,36923684239085495),
    (68404182750971611,43158234166327458),
    (78285710594523935,49392784093569421),
    (88167238438076259,55627334020811384),
    (98048766281628583,61861883948053347),
    (107930294125180907,68096433875295310),
    (117811821968733231,74330983802537273),
    (127693349812285555,80565533729779236),
    (137574877655837879,86800083657021199),
    (147456405499390203,93034633584263162),
    (157337933342942527,99269183511505125),
    (167219461186494851,105503733438747088),
    (177100989030047175,111738283365989051),
    (186982516873599499,117972833293231014),
    (196864044717151823,124207383220472977),
    (206745572560704147,130441933147714940),
]
EXTERNAL_RECORD = 3571472436310255273
EXTERNAL_NEXT = 4761963248413673697
EXTERNAL_RECORD_DELAY = 2334
EXTERNAL_NEXT_DELAY = 2337
FRONTIER = 206745572560704146

def atanh_bounds(p,q,n=180):
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
        old_lo,old_hi=lo,hi
        flo=old_lo-a; fhi=old_hi-a
        if flo==0 or fhi==0:
            break
        lo=1/fhi; hi=1/flo
    return out

CF=cf_interval(AL,AU,100)
assert CF[:len(CF_EXPECT)]==CF_EXPECT

def delta_bounds(a,l):
    return a*L2-l*U3, a*U2-l*L3

def semiconvergents(cf):
    pm2,pm1=0,1
    qm2,qm1=1,0
    out=[]
    for n,an in enumerate(cf):
        for t in range(1,an+1):
            p=pm2+t*pm1
            q=qm2+t*qm1
            if q:
                out.append((p,q,n,t))
        p=pm2+an*pm1
        q=qm2+an*qm1
        pm2,pm1=pm1,p
        qm2,qm1=qm1,q
    return out

upper=[]
for a,l,n,t in semiconvergents(CF_EXPECT):
    dl,du=delta_bounds(a,l)
    if dl>0:
        upper.append((a,l,n,t,dl,du))
    else:
        assert du<0, ("ambiguous sign",a,l)
upper.sort()

records=[]
best_lo=best_hi=None
for a,l,n,t,dl,du in upper:
    if best_lo is None:
        records.append((a,l))
        best_lo,best_hi=dl,du
    elif du < best_lo:
        records.append((a,l))
        best_lo,best_hi=dl,du
    else:
        assert dl >= best_hi, ("ambiguous record comparison",a,l)

tail=[p for p in records if p[0]>=EXPECTED_RECORDS[0][0] and p[0]<=EXPECTED_RECORDS[-1][0]]
assert tail==EXPECTED_RECORDS, (len(tail),len(EXPECTED_RECORDS))
assert len(tail)==51

def exp_lower(x,n=12):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k
        s+=t
    return s

def exp_upper(x,n=12):
    s=Fraction(1); t=Fraction(1)
    for k in range(1,n+1):
        t=t*x/k
        s+=t
    first=t*x/(n+1)
    r=x/Fraction(n+2)
    assert r<1
    return s+first/(1-r)

def nhat_exact(a,l):
    dl,du=delta_bounds(a,l)
    assert dl>0
    lo=Fraction(79,9)/(exp_upper(du)-1)
    hi=Fraction(79,9)/(exp_lower(dl)-1)
    flo=lo.numerator//lo.denominator
    fhi=hi.numerator//hi.denominator
    assert flo==fhi, ("ambiguous Nhat",a,l,flo,fhi)
    return flo+2

def physical_max(nhat):
    h=(nhat-19)//24
    return 27*h+22, 81*h+80

assert nhat_exact(630138897,397573379)==82931674943
last_safe=EXPECTED_RECORDS[-2]
boundary=EXPECTED_RECORDS[-1]
assert last_safe==(196864044717151823,124207383220472977)
assert boundary==(206745572560704147,130441933147714940)

nh_last=nhat_exact(*last_safe)
assert nh_last==1250146787826445598
A_last,B_last=physical_max(nh_last)
assert A_last==1406415136304751277
assert B_last==4219245408914253845
assert B_last<EXTERNAL_NEXT

nh_boundary=nhat_exact(*boundary)
assert nh_boundary==4894841535700125438
A_boundary,B_boundary=physical_max(nh_boundary)
assert B_boundary==16520090182987923332
assert B_boundary>EXTERNAL_NEXT
assert FRONTIER==boundary[0]-1

for p in EXPECTED_RECORDS[:-1]:
    n=nhat_exact(*p)
    A,B=physical_max(n)
    assert A<=B<=B_last<EXTERNAL_NEXT

def ordinary_delay(n):
    s=0
    while n!=1:
        n=n//2 if n%2==0 else 3*n+1
        s+=1
        assert s<100000
    return s

def half_delay_and_J(n):
    s=O=E=0
    while n!=1:
        if n&1:
            n=(3*n+1)//2
            O+=1
        else:
            n//=2
            E+=1
        s+=1
        assert s<100000
    return s,O-E

assert ordinary_delay(EXTERNAL_RECORD)==EXTERNAL_RECORD_DELAY
assert ordinary_delay(EXTERNAL_NEXT)==EXTERNAL_NEXT_DELAY
sh,jh=half_delay_and_J(EXTERNAL_RECORD)
assert sh<=EXTERNAL_RECORD_DELAY and jh<=sh

J_BOUND=EXTERNAL_RECORD_DELAY

a0=EXPECTED_RECORDS[0][0]
assert Fraction(61*a0,233)+26 > J_BOUND+2

print("RL300_FAST_GREEN")
print("BASE_HEAD",BASE_HEAD)
print("CF_PREFIX_LEN",len(CF_EXPECT))
print("RESONANCE_RECORDS_U5_TO_BOUNDARY",len(EXPECTED_RECORDS))
print("EXTERNAL_RECORD",EXTERNAL_RECORD,"DELAY",EXTERNAL_RECORD_DELAY)
print("EXTERNAL_NEXT",EXTERNAL_NEXT,"DELAY",EXTERNAL_NEXT_DELAY)
print("LAST_SAFE_RECORD",last_safe)
print("LAST_SAFE_NHAT",nh_last)
print("LAST_SAFE_BMAX",B_last)
print("BOUNDARY_RECORD",boundary)
print("BOUNDARY_NHAT",nh_boundary)
print("BOUNDARY_BMAX",B_boundary)
print("PROMOTED_EXTERNAL_CERT_FRONTIER",FRONTIER)

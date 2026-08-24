from fractions import Fraction
from math import gcd
from collections import defaultdict

ZCAP = Fraction(16,15)   # valid rational consequence of z^2<16/15
BUDGET4 = Fraction(31,4) # G(1+1/z)>31/4 when G>=4


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q


def area_pair(alpha,beta):
    d=0; area=0
    for x,y in zip(alpha,beta):
        area += d
        d += y-x
    assert d==0
    return area


def suffix_peak(beta):
    h=len(beta)
    peak=Fraction(1)
    ones=0
    for j in range(h-1,-1,-1):
        ones += beta[j]
        peak=max(peak,Fraction(3**ones,2**(h-j)))
    return peak


def canonical_positive_excursions(maxarea):
    """All alpha,beta with prefix count(beta)-count(alpha)>0 internally.
    Area is sum of the positive prefix gap before each local column.
    h<=area+1, so the recursion is finite under maxarea.
    """
    out=[]
    def rec(alpha,beta,d,area):
        if d==0:
            rec((0,),(1,),1,0) # a positive excursion must open 0/1
            return
        area2=area+d
        if area2>maxarea:
            return
        # close only from height one via 1/0
        if d==1:
            out.append((alpha+(1,),beta+(0,),area2))
        # continue while staying strictly positive
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd>0:
                rec(alpha+(x,),beta+(y,),nd,area2)
    rec((),(),0,0)
    return out


def raw_K(r):
    return (Fraction(3,2)**r-Fraction(1))/2

# ----------------------------------------------------------------------
# Exact local enumeration through area 15.
# ----------------------------------------------------------------------
by=defaultdict(list)
for alpha,beta,r in canonical_positive_excursions(15):
    assert area_pair(alpha,beta)==r
    assert sum(alpha)==sum(beta)
    h=len(alpha); p=sum(alpha)
    # Ordered-one transport identity and p<=rho.
    ia=[i for i,b in enumerate(alpha) if b]
    ib=[i for i,b in enumerate(beta) if b]
    assert all(j<i for i,j in zip(ia,ib))
    assert sum(i-j for i,j in zip(ia,ib))==r
    assert p<=r

    D=Qword(alpha)-Qword(beta)
    assert D>0
    raw=Fraction(D,1<<h)
    M=suffix_peak(beta)
    strong=raw*min(Fraction(1),ZCAP/M)
    assert raw<=raw_K(r)
    by[r].append({
        'strong':strong,'D':D,'h':h,'p':p,'M':M,
        'alpha':''.join(map(str,alpha)),'beta':''.join(map(str,beta)),
        'raw':raw,
    })

counts_expected={1:1,2:2,3:4,4:9,5:20,6:46,7:105,8:242,9:557,
                 10:1285,11:2964,12:6842,13:15793,14:36463,15:84187}
assert {r:len(by[r]) for r in range(1,16)}==counts_expected

E={r:max(x['strong'] for x in by[r]) for r in range(1,16)}
expected_E={
 1:Fraction(1,4), 2:Fraction(16,27), 3:Fraction(13,16),
 4:Fraction(188,135), 5:Fraction(53,32), 6:Fraction(560,243),
 7:Fraction(377,135), 8:Fraction(401,128), 9:Fraction(5068,1215),
 10:Fraction(1321,270), 11:Fraction(1369,256), 12:Fraction(13552,2187),
 13:Fraction(8713,1215), 14:Fraction(8929,1080), 15:Fraction(9121,1024),
}
assert E==expected_E

# Raw envelope superadditivity through the relevant finite range (analytic proof is in note).
for r in range(1,16):
    for s in range(1,16-r):
        assert raw_K(r+s)>=raw_K(r)+raw_K(s)
assert raw_K(6)<BUDGET4

# Integer partitions and effective-envelope viability.
def partitions(n,maxpart=None):
    if n==0:
        yield ()
        return
    if maxpart is None or maxpart>n: maxpart=n
    for p in range(maxpart,0,-1):
        for tail in partitions(n-p,p):
            yield (p,)+tail

def env(part): return sum(E[p] for p in part)

for rho in range(1,14):
    assert max(env(p) for p in partitions(rho))<BUDGET4

viable14=[p for p in partitions(14) if env(p)>BUDGET4]
viable15=[p for p in partitions(15) if env(p)>BUDGET4]
assert viable14==[(14,)]
assert viable15==[(15,),(14,1),(13,2)]

# Since total effective envelope <15.5 through rho=15, G cannot be >=8.
for rho in (14,15):
    assert max(env(p) for p in partitions(rho))<Fraction(31,2)

# Candidate uniqueness forced by the strict 31/4 sign-reversal budget.
a14=[x for x in by[14] if x['strong']>BUDGET4-E[1]]
assert len(a14)==1
assert (a14[0]['D'],a14[0]['h'],a14[0]['p'],a14[0]['alpha'],a14[0]['beta']) == \
       (8929,10,6,'0000111111','1011010110')

a13=[x for x in by[13] if x['strong']>BUDGET4-E[2]]
assert len(a13)==1
assert (a13[0]['D'],a13[0]['h'],a13[0]['p'],a13[0]['alpha'],a13[0]['beta']) == \
       (8713,10,6,'0000111111','1010110110')

# Once the unique area-13 candidate is used, area 2 must be its strong type.
need2=BUDGET4-a13[0]['strong']
a2=[x for x in by[2] if x['strong']>need2]
assert len(a2)==1
assert (a2[0]['D'],a2[0]['h'],a2[0]['p'],a2[0]['alpha'],a2[0]['beta']) == \
       (5,3,2,'011','110')

# ----------------------------------------------------------------------
# Exact reduced near-resonance scan: no g=2 pair with ell<=17.
# g=2 means gcd(a,ell)=1, z=2^a/3^ell and 1<z^2<16/15.
# ----------------------------------------------------------------------
def near_resonant(a,ell):
    lhs=1 << (2*a)
    y2=3**(2*ell)
    return y2 < lhs and 15*lhs < 16*y2

small_pairs=[]
for ell in range(1,18):
    for a in range(1,2*ell+3):
        if gcd(a,ell)==1 and near_resonant(a,ell):
            small_pairs.append((a,ell))
assert small_pairs==[]
first=None
for ell in range(1,30):
    for a in range(1,2*ell+3):
        if gcd(a,ell)==1 and near_resonant(a,ell):
            first=(a,ell); break
    if first: break
assert first==(46,29)

# ----------------------------------------------------------------------
# G=4 prefix lemma sanity: common prefix cannot be 10 for least odd R>13.
# If R mod 4=1, split mod 8. One of T^2(R),T^2(R+4) is odd and <R.
# ----------------------------------------------------------------------
for residue in (1,5):
    # choose representatives R=residue mod 8, R>13
    for R in range(residue,200,8):
        if R<=13: continue
        x=R+4
        u2=(3*R+1)//4
        v2=(3*x+1)//4
        assert (3*R+1)%4==0 and (3*x+1)%4==0
        if residue==1:
            assert u2%2==1 and u2<R
        else:
            assert v2%2==1 and v2<R
# Hence under leastness the first two common bits are 11 and prefix odd weight is 2.

# Terminal synchronized common suffix has odd weight zero when G=4:
# U-V=4(X+Y), and 3 does not divide X+Y because Y=3^ell and X=2^a.
for a in range(1,20):
    ell=3
    assert ((1<<a)+3**ell)%3!=0

# ----------------------------------------------------------------------
# Exact two-excursion elimination for rho=15 viable multi-partitions.
# Normalize all inequalities by Y and use 1<z<16/15.
# ----------------------------------------------------------------------
# [14,1], big excursion first:
assert Fraction(8929,3**8) + ZCAP*Fraction(1,16) < 2
# [14,1], area-1 first, big last but one or more columns before maximal start:
assert Fraction(1,27) + ZCAP*Fraction(8929,8192) < 2
# At maximal start the exact equations force z<1, both signs of first term.
z141_plus=Fraction(106496,130491)
z141_minus=Fraction(114688,130491)
assert z141_plus<1 and z141_minus<1

# [13,2], big excursion first:
assert Fraction(8713,3**8) + ZCAP*Fraction(5,32) < 2
# [13,2], area-2 first, big last but one or more columns before maximal start:
assert Fraction(5,81) + ZCAP*Fraction(8713,8192) < 2
# At maximal start exact equations again force z<1.
z132_plus=Fraction(16384,19683)
z132_minus=Fraction(352256,373977)
assert z132_plus<1 and z132_minus<1

# ----------------------------------------------------------------------
# Synchronized-run gap divisibility / exponential-anchor sanity.
# For a run word w of length h, choose minimal compatible gap 2^h.
# At its kth odd column the gap is >=2*3^(k-1).
# ----------------------------------------------------------------------
for h in range(1,9):
    for mask in range(1<<h):
        w=[(mask>>j)&1 for j in range(h)]
        Delta=1<<h
        k=0
        for j,b in enumerate(w):
            if b:
                k+=1
                assert Delta >= 2*3**(k-1)
                Delta=3*Delta//2
            else:
                Delta//=2
        assert Delta==3**sum(w)

print('RL37 g=2 sign-reversal / half-population bridge verifier: PASS')
print('canonical positive excursions checked through area 15 =',sum(counts_expected.values()))
print('strong envelopes E(13),E(14),E(15) =',E[13],E[14],E[15])
print('viable area partitions at rho=14 =',viable14)
print('viable area partitions at rho=15 =',viable15)
print('first reduced near-resonant pair =',first)
print('certified low-transport consequence: rho >= 16')

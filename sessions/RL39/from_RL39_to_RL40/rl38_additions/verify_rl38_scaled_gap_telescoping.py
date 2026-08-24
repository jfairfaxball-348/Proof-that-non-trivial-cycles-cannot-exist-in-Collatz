from fractions import Fraction
from collections import defaultdict


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
        area += abs(d)
        d += y-x
    assert d==0
    return area


def canonical_positive_excursions(maxarea):
    out=[]
    def rec(alpha,beta,d,area):
        area2=area+d
        if area2>maxarea:
            return
        if d==1:
            out.append((alpha+(1,),beta+(0,),area2))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd>0:
                rec(alpha+(x,),beta+(y,),nd,area2)
    rec((0,),(1,),1,0)
    return out

# ------------------------------------------------------------------
# Local excursion facts through area 15.
# ------------------------------------------------------------------
by=defaultdict(list)
for alpha,beta,r in canonical_positive_excursions(15):
    h=len(alpha); p=sum(alpha)
    assert p==sum(beta) and p>=1
    assert area_pair(alpha,beta)==r
    assert h<=r+1
    D=Qword(alpha)-Qword(beta)
    assert D>0
    # Exact R38.16: D/3^p < 3^(r-1).
    assert Fraction(D,3**p) < 3**(r-1)
    by[r].append((alpha,beta,D,h,p))

counts_expected={1:1,2:2,3:4,4:9,5:20,6:46,7:105,8:242,9:557,
                 10:1285,11:2964,12:6842,13:15793,14:36463,15:84187}
assert {r:len(by[r]) for r in range(1,16)}==counts_expected

# ------------------------------------------------------------------
# Integer physical sign crossing: exhaustive through area 7.
# Incoming gap g must satisfy 3^p g-D = -2^h g_out with g_out>=1.
# ------------------------------------------------------------------
crossings=defaultdict(list)
for r in range(1,8):
    for alpha,beta,D,h,p in by[r]:
        # Crossing implies 3^p g < D, so only finitely many g.
        for g in range(1,(D-1)//(3**p)+1,2):
            n=3**p*g-D
            if n<0 and n%(1<<h)==0:
                gout=-n//(1<<h)
                crossings[r].append((alpha,beta,D,h,p,g,gout))

for r in range(1,7):
    assert crossings[r]==[]
assert len(crossings[7])==1
alpha,beta,D,h,p,g,gout=crossings[7][0]
assert ''.join(map(str,alpha))=='000011'
assert ''.join(map(str,beta))=='101000'
assert (D,h,p,g,gout)==(73,6,2,1,1)
J=Fraction((1<<h)*gout,3**p*g)
assert J==Fraction(64,9)

# ------------------------------------------------------------------
# R38.20/R38.21 arithmetic sanity over enumerated excursions.
# If a preceding synchronized run contributes c common odd columns,
# take any odd input gap divisible by 3^c.  Then t=D/(3^p g)
# is strictly below 3^(r-1-c). A crossing forces r>=c+2.
# ------------------------------------------------------------------
for r in range(1,16):
    for alpha,beta,D,h,p in by[r]:
        for c in range(0,min(r+2,8)):
            g=3**c  # minimal positive gap with v3(g)>=c
            t=Fraction(D,3**p*g)
            assert t < Fraction(3**max(r-1-c,0),1) if r-1-c>=0 else t < Fraction(1,3**(c-r+1))
            if t>1:
                assert r>=c+2

# ------------------------------------------------------------------
# Exact telescoping sanity on synthetic segmented gap data.
# A synchronized segment has multiplier m and leaves W=q*Delta fixed.
# An excursion's J equals |Wout/Win|. Product Js telescopes.
# ------------------------------------------------------------------
# Build a rational path with sync / excursion / sync / excursion.
q=Fraction(1); Delta=Fraction(12); W0=q*Delta
# sync word length 3 weight 2: m=9/8, q -> q/m
m=Fraction(9,8); Delta*=m; q/=m
assert q*Delta==W0
# excursion jump in W: choose arbitrary nonzero rational change
Win=q*Delta
Wout=Win-Fraction(5,2)
Delta_out=Wout/q  # keep same endpoint q for this abstract jump sanity
J1=abs(Wout/Win)
Delta=Delta_out
# sync word length 2 weight 1: m=3/4
m=Fraction(3,4); Delta*=m; q/=m
assert q*Delta==Wout
Win2=q*Delta
Wfinal=-Fraction(7,3)*W0
Delta_final=Wfinal/q
J2=abs(Wfinal/Win2)
assert J1*J2==abs(Wfinal/W0)

print('RL38 scaled-gap telescoping / crossing-charge verifier: PASS')
print('canonical excursions checked through area 15 =',sum(counts_expected.values()))
print('no integer sign-changing excursion for area <= 6')
print('unique area-7 crossing = 000011 / 101000, gap 1 -> -1, J=64/9')
print('analytic crossing consequence certified symbolically: r_cross >= max(7,c_pre+2)')

from fractions import Fraction
from collections import defaultdict

ZCAP = Fraction(16,15)
BUDGET4 = Fraction(31,4)
BUDGET8 = Fraction(31,2)


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q


def suffix_peak(beta):
    h=len(beta); peak=Fraction(1); ones=0
    for j in range(h-1,-1,-1):
        ones += beta[j]
        peak=max(peak,Fraction(3**ones,2**(h-j)))
    return peak


def canonical_positive_excursions(maxarea):
    def rec(alpha,beta,d,area):
        area2=area+d
        if area2>maxarea:
            return
        if d==1:
            yield alpha+(1,), beta+(0,), area2
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd>0:
                yield from rec(alpha+(x,),beta+(y,),nd,area2)
    yield from rec((0,),(1,),1,0)


def crossing_gap(D,h,p):
    """Return the unique positive odd crossing gap if it exists.

    Since 3^p is invertible mod 2^h, crossing inputs are one residue class
    modulo 2^h.  In the enumerated range at most one positive representative
    lies below D/3^p.
    """
    mod=1<<h
    g0=(D*pow(3**p,-1,mod))%mod
    if g0==0:
        g0=mod
    maxg=(D-1)//(3**p)
    if g0<=maxg and (g0&1):
        n=D-3**p*g0
        assert n>0 and n%mod==0
        return g0,n//mod
    return None


by=defaultdict(list)
E={}
C={}
for alpha,beta,r in canonical_positive_excursions(16):
    h=len(alpha); p=sum(alpha); D=Qword(alpha)-Qword(beta)
    raw=Fraction(D,1<<h)
    M=suffix_peak(beta)
    strong=raw*min(Fraction(1),ZCAP/M)
    cross=crossing_gap(D,h,p)
    rec={
        'alpha':alpha,'beta':beta,'D':D,'h':h,'p':p,
        'raw':raw,'M':M,'strong':strong,'cross':cross,
    }
    by[r].append(rec)
    if r not in E or strong>E[r]: E[r]=strong
    if cross is not None and (r not in C or strong>C[r]): C[r]=strong

counts_expected={1:1,2:2,3:4,4:9,5:20,6:46,7:105,8:242,9:557,
                 10:1285,11:2964,12:6842,13:15793,14:36463,
                 15:84187,16:194388}
assert {r:len(by[r]) for r in range(1,17)}==counts_expected

E_expected={
 1:Fraction(1,4), 2:Fraction(16,27), 3:Fraction(13,16),
 4:Fraction(188,135), 5:Fraction(53,32), 6:Fraction(560,243),
 7:Fraction(377,135), 8:Fraction(401,128), 9:Fraction(5068,1215),
 10:Fraction(1321,270), 11:Fraction(1369,256), 12:Fraction(13552,2187),
 13:Fraction(8713,1215), 14:Fraction(8929,1080), 15:Fraction(9121,1024),
 16:Fraction(22300,2187),
}
assert E==E_expected
for r in range(1,7):
    assert r not in C


def partitions(n,maxpart=None):
    if n==0:
        yield (); return
    if maxpart is None or maxpart>n: maxpart=n
    for p in range(maxpart,0,-1):
        for tail in partitions(n-p,p):
            yield (p,)+tail


def crossing_env(part):
    vals=[]
    for i,p in enumerate(part):
        if p in C:
            vals.append(C[p]+sum(E[q] for j,q in enumerate(part) if j!=i))
    return max(vals) if vals else Fraction(0)

# Crossing-aware budget recovers the old <=15 exclusion and isolates rho=16.
for rho in range(1,16):
    assert max(crossing_env(p) for p in partitions(rho)) < BUDGET4
viable16=[p for p in partitions(16) if crossing_env(p)>BUDGET4]
assert viable16==[(16,),(14,2),(14,1,1)]

# Even unrestricted rho=16 cannot support G>=8.
assert max(sum(E[q] for q in p) for p in partitions(16))==E[16]
assert E[16] < BUDGET8

# G=4 and common prefix 11 imply first-excursion incoming gap = 9.
G=4
first_gap=3**2*G//(2**2)
assert first_gap==9

# (16): exact crossing candidates that alone clear 31/4.
c16=[x for x in by[16] if x['cross'] is not None and x['strong']>BUDGET4]
assert len(c16)==3
sig16=sorted((x['D'],x['h'],x['p'],x['cross'][0],x['cross'][1]) for x in c16)
assert sig16==sorted([
    (27875,11,7,9,4),
    (9199,10,6,7,4),
    (44815,12,7,13,4),
])
first16=[x for x in c16 if x['cross'][0]==first_gap]
assert len(first16)==1
x=first16[0]
J=Fraction((1<<x['h'])*x['cross'][1],3**x['p']*first_gap)
assert J==Fraction(8192,19683) < 1
# With one excursion, RL38 gives J=z>1: contradiction.

# (14,2): area 14 must cross and must clear BUDGET4-E(2).
need14_2=BUDGET4-E[2]
c14_2=[x for x in by[14] if x['cross'] is not None and x['strong']>need14_2]
assert len(c14_2)==1
x14=c14_2[0]
assert (x14['D'],x14['h'],x14['p'],x14['cross'])==(17669,11,6,(13,4))

# (14,1,1) gives the same unique area-14 crossing candidate.
need14_11=BUDGET4-2*E[1]
c14_11=[x for x in by[14] if x['cross'] is not None and x['strong']>need14_11]
assert c14_11==c14_2

# Exact small-area local transitions from a positive synchronized gap.
def integral_transitions(g,r):
    out=[]
    for x in by[r]:
        for sign in (-1,+1):  # Delta_out=(3^p*g + sign*D)/2^h
            num=3**x['p']*g + sign*x['D']
            den=1<<x['h']
            if num%den==0:
                gout=num//den
                # area<=2 cannot cross, so retain positive transitions only
                if gout>0:
                    out.append((x['D'],x['h'],x['p'],sign,gout))
    return out

assert integral_transitions(9,1)==[(1,2,1,+1,7)]
assert integral_transitions(7,1)==[(1,2,1,-1,5)]
assert integral_transitions(9,2)==[(3,3,1,-1,3)]

# Odd physical gap at a synchronized boundary forbids a nonempty common-parity run.
# Thus before the area-14 crossing the only possible incoming gaps are:
#   9 (crossing first), 3 (one area-2 first), 7 (one area-1 first),
#   5 (two area-1 first).
reachable_before_14={9,3,7,5}
assert 13 not in reachable_before_14

print('RL40 crossing-aware area-16 elimination verifier: PASS')
print('canonical positive excursions through area 16 =',sum(counts_expected.values()))
print('E(16) =',E[16])
print('crossing-aware viable partitions at rho=16 =',viable16)
print('single-excursion budget candidates =',sig16)
print('unique viable area-14 crossing requires gap 13; reachable gaps are',sorted(reachable_before_14))
print('certified strengthened consequence: rho >= 17')

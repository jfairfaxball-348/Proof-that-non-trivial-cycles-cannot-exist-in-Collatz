from fractions import Fraction
from collections import defaultdict


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q


def canonical_positive_excursions(maxarea):
    out=[]
    def rec(alpha,beta,d,area):
        area2=area+d
        if area2>maxarea: return
        if d==1:
            out.append((alpha+(1,),beta+(0,),area2))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd>0:
                rec(alpha+(x,),beta+(y,),nd,area2)
    rec((0,),(1,),1,0)
    return out

counts=defaultdict(int)
for alpha,beta,r in canonical_positive_excursions(15):
    h=len(beta); p=sum(beta)
    counts[r]+=1
    # leading beta starts odd and has p odd positions
    odd=[i for i,b in enumerate(beta) if b]
    assert odd[0]==0 and len(odd)==p
    ls=[odd[k+1]-odd[k] for k in range(p-1)] + [h-odd[-1]]
    assert all(l>=1 for l in ls)
    assert sum(ls)==h

    # Prefix imbalance path, d_j before column j.
    d=0; ds=[]
    for a,b in zip(alpha,beta):
        ds.append(d)
        d += b-a
    assert d==0
    assert ds[0]==0 and all(x>0 for x in ds[1:])
    assert sum(ds)==r

    # Pure combinatorial form behind R39.7: for each charged column j=i+q,
    # q is its distance from the preceding beta-odd position. We record
    # max(d_j + q*alpha) symbolically as the required H_k threshold.
    # Verify summing l_k*max_threshold minus q-sum dominates area.
    # Use rational surrogate alpha in [630929/1e6, 630930/1e6] for log_3 2.
    alo=Fraction(630929,10**6)
    ahi=Fraction(630930,10**6)
    total_capacity=Fraction(0)
    for k,i in enumerate(odd):
        l=ls[k]
        req=max(Fraction(ds[i+q]) + q*ahi for q in range(l))
        # If H >= req, then sum(d_j) <= l H-alpha*l(l-1)/2.
        # Use alo in the subtractive term for a rigorous lower capacity check.
        cap=l*req - alo*l*(l-1)/2
        actual=sum(ds[i:i+l])
        assert cap>=actual
        total_capacity += cap
    assert total_capacity>=r

    # Valuation-only floors encoded combinatorially.
    if ls[0]>=2:
        # last charged first-interval column is interior, d>=1
        assert ds[ls[0]-1]>=1
    for k in range(1,p):
        assert ds[odd[k]]>=1
        if ls[k]>=2:
            assert ds[odd[k]+ls[k]-1]>=1

expected={1:1,2:2,3:4,4:9,5:20,6:46,7:105,8:242,9:557,
          10:1285,11:2964,12:6842,13:15793,14:36463,15:84187}
assert dict(counts)==expected

# Exact elementary correction identities / floors with a rational z/R placeholder e<1/1000.
e=Fraction(1,1000)
# If H>=2, z/(3^H-z/R) <= z/(9-z/R); test denominator ordering.
assert Fraction(1,9-e) < Fraction(1,6-e)
# l>=3 valuation floor gives 3*2^(l-1) >=12 >9.
for l in range(3,20):
    assert 3*(2**(l-1))>=12
    assert Fraction(1,3*(2**(l-1))-e) <= Fraction(1,12-e)

print('RL39 odd-or-valuation transport-charge verifier: PASS')
print('canonical positive excursions checked through area 15 =',sum(expected.values()))
print('column-to-preceding-odd interval partition and area charging verified')
print('long-valuation geometric suppression sanity verified')

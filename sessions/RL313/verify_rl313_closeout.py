#!/usr/bin/env python3
"""Portable regression verifier for the RL313 closeout.

The promoted theorems are analytic.  This script checks the finite arithmetic
certificates, the two-active-cut structural classification at small row sizes,
and the explicit fully-active ownership-blind countermodel.
"""
from fractions import Fraction
from math import gcd

R0 = 2**71

def Q(w):
    L=sum(w); seen=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-seen)
            seen += 1
    return q

def upper_mechanical(a,l):
    C=[(r*l+a-1)//a for r in range(a+1)]
    return [C[r+1]-C[r] for r in range(a)]

def primitive(w):
    A=len(w)
    return all(w != w[k:]+w[:k] for k in range(1,A))

def terminal_ds(l):
    # n>=2 and lambda<3 imply 3^l < 2^d < sqrt(3)*3^l.
    return [d for d in range(1, 2*l+10)
            if 3**l < 2**d and 2**(2*d) < 3**(2*l+1)]

def boundary_upper(d,l):
    X=2**d; Y=3**l
    qmax=2**(d-l)*(Y-2**l)
    return qmax//(X-Y)

# 1. The terminal state-floor certificate.
cand=[]
for l in range(1,116):
    ds=terminal_ds(l)
    assert len(ds) <= 1
    if ds:
        d=ds[0]
        cand.append((l,d,boundary_upper(d,l)))
assert len(cand)==91
assert all(u<R0 for _,_,u in cand)
assert max(cand, key=lambda t:t[2]) == (
    111,176,751281177470410612498
)
first=None
for l in range(1,200):
    ds=terminal_ds(l)
    if ds:
        d=ds[0]
        u=boundary_upper(d,l)
        if u>=R0:
            first=(l,d,u); break
assert first == (116,184,2804721460384257848662)

# Reduced denominator check: ell<=16 has no possible c reaching the floor;
# the first reduced ell is 17, at (a,c)=(27,7).
for ell in range(1,17):
    for a in range(1,2*ell+10):
        if gcd(a,ell)!=1 or 2**a<=3**ell:
            continue
        c=1
        while 2**(2*c*a) < 3**(2*c*ell+1):
            assert boundary_upper(c*a,c*ell) < R0
            c += 1
ell=17; a=27
assert gcd(a,ell)==1 and 2**a>3**ell
for c in range(1,7):
    assert 2**(2*c*a) < 3**(2*c*ell+1)
    assert boundary_upper(c*a,c*ell) < R0
assert 2**(2*7*a) < 3**(2*7*ell+1)
assert boundary_upper(7*a,7*ell) == 3809524945262048704667 >= R0

# 2. Idempotent divisor descent arithmetic and coarsening gcd formula.
for g in range(2,50):
    for m in range(1,g):
        c=gcd(g,m)
        assert gcd(g,c)==c
        for a in range(2,8):
            A=g*a; d=a*c; n=g//c
            for q in range(1,n):
                assert gcd(A,q*d)==d*gcd(n,q)

# 3. Two-active-cut row classification regression.
# A cut j means the prefix of length j, with 1<=j<d.
classes_checked=0
for d in range(3,11):
    X=2**d
    rows_by_weight={}
    for mask in range(1<<d):
        w=[(mask>>i)&1 for i in range(d)]
        rows_by_weight.setdefault(sum(w),[]).append(w)
    for l,rows in rows_by_weight.items():
        if l==0 or l==d or X<=3**l: continue
        Ps={tuple(w): [sum(w[:j]) for j in range(d+1)] for w in rows}
        for j1 in range(1,d):
            for j2 in range(j1+1,d):
                active={j1,j2}
                groups={}
                for w in rows:
                    P=Ps[tuple(w)]
                    sig=tuple(P[j] for j in range(d+1) if j not in active)
                    groups.setdefault(sig,[]).append(w)
                for fam in groups.values():
                    if len(fam)<2: continue
                    varying={j for j in range(1,d)
                             if len({Ps[tuple(w)][j] for w in fam})>1}
                    if varying != active: continue
                    classes_checked += 1
                    # All variation is either one 3-bit fixed-weight window
                    # (adjacent cuts), or two disjoint adjacent 10/01 swaps.
                    if j2==j1+1:
                        lo=j1-1; hi=j2+1
                        assert all(w[:lo]==fam[0][:lo] and w[hi:]==fam[0][hi:]
                                   for w in fam)
                        sums={sum(w[lo:hi]) for w in fam}
                        assert len(sums)==1 and next(iter(sums)) in (1,2)
                    else:
                        p1=j1-1; p2=j2-1
                        for w in fam:
                            assert w[:p1]==fam[0][:p1]
                            assert w[j1+1:p2]==fam[0][j1+1:p2]
                            assert w[j2+1:]==fam[0][j2+1:]
                            assert w[p1]+w[p1+1]==fam[0][p1]+fam[0][p1+1]==1
                            assert w[p2]+w[p2+1]==fam[0][p2]+fam[0][p2+1]==1
                    # Remove the maximal common 2^u 3^v monomial from all
                    # numerator differences; the normalized alphabet range is < X.
                    qs=[Q(w) for w in fam]
                    q0=min(qs)
                    diffs=[q-q0 for q in qs if q!=q0]
                    assert diffs
                    def v_p(n,p):
                        v=0
                        while n%p==0:
                            n//=p; v+=1
                        return v
                    u=min(v_p(z,2) for z in diffs)
                    v=min(v_p(z,3) for z in diffs)
                    C=2**u*3**v
                    assert all(z%C==0 for z in diffs)
                    assert max(z//C for z in diffs) < X
assert classes_checked>0

# 4. Fixed-leading-bit span barrier in the large terminal regime.
for l in range(5,201):
    ds=terminal_ds(l)
    if not ds: continue
    d=ds[0]; X=2**d; Y=3**l
    delta0=(2**(d-l)-2)*(Y-2**l)
    delta1=2*(2**(d-l)-1)*(3**(l-1)-2**(l-1))
    assert delta0 > X+Y
    assert delta1 > X+Y

# 5. Explicit ownership-blind fully-active countermodel.
a,l,g=27,17,10
B=upper_mechanical(a,l)
assert sum(B)==l
w=B*g
ins=a + next(i for i,b in enumerate(B) if b==0)
rem=3*a + next(i for i,b in enumerate(B) if b==1)
assert w[ins]==0 and w[rem]==1
A=len(w)
sep=(rem-ins)%A
assert sep>a and A-sep>a
w=w[:]
w[ins]=1; w[rem]=0
assert sum(w)==g*l
assert primitive(w)
assert 3**(g*l) < 2**(g*a) < 3*3**(g*l)

C=0; Ts=[]
for i in range(A+1):
    Ts.append(Fraction(C,1)-Fraction(i*l,a))
    if i<A: C+=w[i]
assert min(Ts)==0
assert max(Ts)==Fraction(53,27)
E=[]
for j in range(g+1):
    E.append(sum(w[:j*a])-j*l)
assert E[:5]==[0,0,1,1,0]

s=a; p=l
Ws=[sum(w[(i+t)%A] for t in range(s)) for i in range(A)]
G=[p-z for z in Ws]
active=[]
for r in range(a):
    vals=[G[i] for i in range(r,A,a)]
    assert sum(vals)==0
    if any(vals):
        active.append(r)
        assert vals.count(1)==1 and vals.count(-1)==1
assert len(active)==a
assert sum(abs(x) for x in G)==2*a

print("RL313 closeout verifier: PASS")
print(f"two-active structural classes checked: {classes_checked}")
print("terminal cutoff: ell0>=116, d>=184; reduced ell>=17")
print("countermodel: (a,ell,g)=(27,17,10), max T=53/27, all 27 orbits active")

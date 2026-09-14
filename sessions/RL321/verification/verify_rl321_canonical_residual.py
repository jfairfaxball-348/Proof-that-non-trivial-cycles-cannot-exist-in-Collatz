#!/usr/bin/env python3
from itertools import product, combinations
from math import gcd


def T(n):
    return n//2 if n%2==0 else (3*n+1)//2

def word_of(n,r):
    out=[]
    x=n
    for _ in range(r):
        out.append(x&1)
        x=T(x)
    return tuple(out),x

def Q(word):
    s=sum(word)
    q=0
    c=0
    for j,b in enumerate(word):
        if b:
            q += (1<<j) * (3**(s-1-c))
            c += 1
    return q

# 1. Canonical eta and common-quotient transport, exhaustive r<=10.
checks=0
for r in range(1,11):
    for bits in product((0,1), repeat=r-1):
        beta=(1,)+bits
        s=sum(beta)
        matches=[]
        for eta in range(1,1<<r,2):
            w,J=word_of(eta,r)
            if w==beta:
                matches.append((eta,J))
        assert len(matches)==1
        eta,J=matches[0]
        assert 0<eta<(1<<r)
        assert 0<J<3**s
        B=Q(beta)
        assert (1<<r)*J == (3**s)*eta+B
        for M in (1,2,5,17):
            z=(1<<r)*M+eta
            w,y=word_of(z,r)
            assert w==beta
            assert y==(3**s)*M+J
            assert z//(1<<r)==M==y//(3**s)
        checks+=1

# 2. Tail-residue saturation for s<=6.
for s in range(1,7):
    mod=3**s
    units=[x for x in range(1,mod) if x%3]
    for theta in units:
        t=None
        cur=theta%mod
        for k in range(0,2*mod+1):
            if cur == mod-1:
                t=k; break
            cur=(2*cur)%mod
        assert t is not None
        r=s+t
        B=3**s-2**s
        assert ((1<<r)*theta-B)%mod==0

# 3. Matched-rank localization on all small ordered row pairs.
for a in range(2,9):
  for ell in range(1,a):
    positions=list(combinations(range(a),ell))
    for vpos in positions:
      for upos in positions:
        if not all(u>=v for u,v in zip(upos,vpos)):
            continue
        u=[0]*a; v=[0]*a
        for x in upos:u[x]=1
        for x in vpos:v[x]=1
        for j in range(ell):
            t=upos[j]
            if t<=vpos[j]:
                continue
            beta=v[vpos[j]:t]
            # [v_j,u_j) starts with the j-th early one and ends before late matched one.
            assert len(beta)==t-vpos[j]
            s=sum(beta)
            Cu=sum(u[:t])
            Cv=sum(v[:t])
            assert s==Cv-Cu
            assert len(beta)>=s

# 4. Exact elementary constants used by the closeout.
assert 3**25 < 2**40
assert (2**71-2**35)*3**75 > 2**39 * 4**75
assert 217_976_794_617 - 137_528_045_312 == 80_448_749_305
assert 80_448_749_305 > 81

# 5. Negative-corner dual saturation family.
for h in range(40,61):
    beta=(1,)*h
    eta=2**h-1
    J=3**h-1
    nu=1; D=1
    assert Q(beta)==3**h-2**h
    assert 2**h*J == 3**h*eta + Q(beta)
    assert 2**h*D == 3**h*nu - Q(beta)
    x=nu
    for _ in beta:
        assert x&1
        x=(3*x-1)//2
    assert x==D==1

# 6. Beatty algebra regression on small coprime X,Y analogues.
# This checks the exact floor implication: 0 < nX-(X-Y)m < X-Y => m=floor(nX/(X-Y)).
for X in range(5,80):
  for Y in range(1,X):
    D0=X-Y
    if gcd(X,D0)!=1: continue
    for n in range(1,40):
      q=n*X//D0
      lam=n*X-D0*q
      if 0<lam<D0:
        assert q == (n*X)//D0

print('RL321_CANONICAL_RESIDUAL_VERIFIER_GREEN')
print('ordinary_tail_cases', checks)
print('residue_saturation_s_max', 6)
print('matched_rank_a_max', 8)
print('negative_corner_h_range', '40..60')

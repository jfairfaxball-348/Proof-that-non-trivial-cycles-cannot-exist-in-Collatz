#!/usr/bin/env python3
"""Finite stress tests for RL312 single-active-shift-orbit theorem.

The theorem is analytic.  This verifier exhausts primitive positive-D binary
words through A=14, identifies every balanced shift whose canonical flow is
nonzero on exactly one shift-orbit, and checks the exact row rigidity and
rank-one numerator factorization used in the proof.
"""
from itertools import product
from math import gcd


def primitive(w):
    A=len(w)
    return all(tuple(w)!=tuple(w[k:]+w[:k]) for k in range(1,A))


def rot(w,k):
    return w[k:]+w[:k]


def Q(w):
    L=sum(w); P=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-P)
            P += 1
    return q


def balanced_flow(w,s):
    A=len(w); L=sum(w)
    if (s*L)%A:
        return None
    p=s*L//A
    W=[sum(w[(i+t)%A] for t in range(s)) for i in range(A)]
    f=[p-z for z in W]
    assert sum(f)==0
    for i in range(A):
        assert f[(i+1)%A]-f[i] == w[i]-w[(i+s)%A]
    return f


checked=0
for A in range(3,15):
    for bits in product((0,1), repeat=A):
        w=list(bits); L=sum(w)
        if L==0 or not primitive(w):
            continue
        if (1<<A)-3**L <= 1:
            continue
        for s in range(1,A):
            f=balanced_flow(w,s)
            if f is None or not any(f):
                continue
            d0=gcd(A,s)
            active=sorted({i%d0 for i,x in enumerate(f) if x})
            if len(active)!=1:
                continue

            r=active[0]
            # Start rows at residue r-1, making the active flow column 1.
            start=(r-1)%d0
            wr=rot(w,start)
            fr=rot(f,start)
            assert {i%d0 for i,x in enumerate(fr) if x}=={1}

            n=A//d0
            assert n>1 and d0>=2
            rows=[wr[k*d0:(k+1)*d0] for k in range(n)]

            # Exact row rigidity: fixed suffix, variable adjacent 10/01 pair.
            fixed=rows[0][2:]
            assert all(row[2:]==fixed for row in rows)
            assert all(row[0]+row[1]==1 for row in rows)
            types={tuple(row[:2]) for row in rows}
            assert types=={(1,0),(0,1)}

            weights={sum(row) for row in rows}
            assert len(weights)==1
            l0=next(iter(weights))
            assert L==n*l0

            X0=1<<d0
            Y0=3**l0
            D0=X0-Y0
            D=X0**n-Y0**n
            assert D0>0 and D>0 and D%D0==0
            H=D//D0
            assert H==sum(X0**k*Y0**(n-1-k) for k in range(n))

            B10=[1,0]+fixed
            B01=[0,1]+fixed
            Q10=Q(B10)
            Q01=Q(B01)
            C0=Q01-Q10
            assert C0==3**(l0-1)

            eps=[1 if row[:2]==[0,1] else 0 for row in rows]
            S=sum(eps[k]*X0**k*Y0**(n-1-k) for k in range(n))
            assert 0<S<H
            assert Q(wr)==Q10*H+C0*S
            assert gcd(H,C0)==1

            # If full-D ownership were present, D|Q would imply H|S,
            # contradicting the strict interval above.
            assert not (S%H==0)
            checked += 1

assert checked==1046, checked
print(f"RL312 single-shift-orbit verifier: PASS ({checked} exhaustive cases)")

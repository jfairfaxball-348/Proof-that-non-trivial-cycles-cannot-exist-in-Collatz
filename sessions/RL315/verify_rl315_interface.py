#!/usr/bin/env python3
"""Portable small-instance regression for RL315 analytic normal forms.

This is a regression/sanity checker, not the proof of the analytic theorems.
"""
from itertools import combinations
from math import gcd

def Q(w):
    L=sum(w)
    seen=0
    q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-seen)
            seen += 1
    return q

def interface_normal_form(w, g):
    A=len(w); L=sum(w)
    assert A%g==0 and L%g==0
    a=A//g; ell=L//g
    rows=[w[k*a:(k+1)*a] for k in range(g)]
    E=[0]
    for row in rows:
        E.append(E[-1]+sum(row)-ell)
    assert E[-1]==0
    H=[]
    for k,row in enumerate(rows):
        p=0; arr=[]
        for j in range(a+1):
            arr.append(E[k]+p)
            if j<a: p+=row[j]
        H.append(arr)
    m=[min(H[k][j] for k in range(g)) for j in range(a+1)]
    tau=[m[j+1]-m[j] for j in range(a)]
    assert all(t in (0,1) for t in tau)
    assert sum(tau)==ell
    f=[[H[k][j]-m[j] for j in range(a+1)] for k in range(g)]
    assert all(min(f[k][j] for k in range(g))==0 for j in range(a))
    for k in range(g):
        for j in range(a):
            if j+1==a:
                rhs=tau[j]+f[(k+1)%g][0]-f[k][j]
            else:
                rhs=tau[j]+f[k][j+1]-f[k][j]
            assert rhs==rows[k][j]
    return tau,f

checked=0
for A in range(4,11):
    for L in range(1,A):
        g=gcd(A,L)
        if g<=1: continue
        a=A//g; ell=L//g
        for ones in combinations(range(A),L):
            w=[0]*A
            for i in ones: w[i]=1
            Ns=[sum(w[(r+t)%A] for t in range(a)) for r in range(A)]
            assert sum(Ns)==a*L
            assert ell in Ns
            tau,f=interface_normal_form(w,g)
            assert len(tau)==a and sum(tau)==ell
            checked+=1

inj=0
for a in range(2,13):
    for ell in range(1,a):
        seen={}
        for ones in combinations(range(a),ell):
            w=[0]*a
            for i in ones: w[i]=1
            r=Q(w)%(1<<a)
            assert r not in seen
            seen[r]=ones
            inj+=1

for a in range(2,7):
    for ell in range(1,a):
        A=2*a; L=2*ell
        for ones in combinations(range(A),L):
            w=[0]*A
            for i in ones: w[i]=1
            for r in range(A):
                n=sum(w[(r+t)%A] for t in range(a))
                if n==ell:
                    comp=sum(w[(r+a+t)%A] for t in range(a))
                    assert comp==ell
                    break
            else:
                raise AssertionError("universal balanced window failed")

print("RL315 portable regression: PASS")
print("small interface/window words checked:", checked)
print("fixed-weight Q residues checked:", inj)

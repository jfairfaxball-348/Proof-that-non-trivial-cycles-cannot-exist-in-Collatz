#!/usr/bin/env python3
"""Dependency-free exact verifier for RL159 joint distinguished-root SNF consequences."""
from math import gcd


def bareiss_det(M):
    A=[list(map(int,row)) for row in M]
    n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            r=next((r for r in range(k+1,n) if A[r][k]),None)
            if r is None: return 0
            A[k],A[r]=A[r],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]


def rows(A,L):
    M=A-L
    out=[]
    # ascending coefficient basis 1,T,...,T^(A-1)
    for i in range(M):
        r=[0]*A; r[i]-=1; r[i+L]+=2; out.append(r)
    for j in range(L):
        r=[0]*A; r[j]-=2; r[j+M]+=3; out.append(r)
    assert len(out)==A
    return out


def rho_mod(A,L,d):
    if L==1:
        p=1; u=A-1
    else:
        p=pow(A,-1,L); u=(A*p-1)//L
    assert A*p-u*L==1
    return pow(2,u,d)*pow(pow(3,p,d),-1,d)%d


def peval(c,x,m):
    return sum(a*pow(x,i,m) for i,a in enumerate(c))%m


def max_minor_gcd(M):
    # M has n+1 rows and n columns: gcd of all n x n row-deletion minors.
    n=len(M[0]); assert len(M)==n+1
    g=0
    for skip in range(n+1):
        sub=[row for i,row in enumerate(M) if i!=skip]
        g=gcd(g,abs(bareiss_det(sub)))
    return g

# Structural exact checks over a nontrivial grid.
for A in range(3,11):
    for L in range(1,A):
        if gcd(A,L)!=1: continue
        d=abs(2**A-3**L)
        if d<=1: continue
        assert gcd(d,6)==1
        S=rows(A,L)
        assert abs(bareiss_det(S))==d
        rho=rho_mod(A,L,d)
        # Both row families evaluate to zero at the physical root.
        assert all(peval(r,rho,d)==0 for r in S)
        # Deterministic dense test row; the augmented index must be gcd(d,P(rho)).
        P=[((k+1)*(A+2*L)+3)%7-3 for k in range(A)]
        delta=max_minor_gcd(S+[P])
        assert delta==gcd(d,peval(P,rho,d))

# RL158 counterexample / RL159 red-team.
A,L=13,8; M=5; d=1631; rho=1377
S=rows(A,L)
assert abs(bareiss_det(S))==d
P=[2,2,1,2,2,2,2,1]+[0]*(A-8)
assert peval(P,rho,d)==17
assert max_minor_gcd(S+[P])==1

# Exact polynomial identity helpers in ascending coefficient arrays.
def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(a,s): return [s*x for x in a]

B1=[-1]+[0]*7+[2]
B2=[-2]+[0]*4+[3]
UD=[6561,7776,9216,8748,10368]
VD=[-4096,-3888,-4608,-4374,-5184,-6144,-5832,-6912]
UT=[-5535,-6561,-7776,-7380,-8748]
VT=[3456,3280,3888,3690,4374,5184,4920,5832]
UP=[-21,-30,-39,-30,-42]
VP=[18,14,19,14,20,26,20,28]

def lhs(U,V): return add(mul(U,B1),mul(V,B2))
assert lhs(UD,VD)==[1631]
assert lhs(UT,VT)==[-1377,1]
Pshort=[2,2,1,2,2,2,2,1]
Pminus17=Pshort[:]; Pminus17[0]-=17
assert lhs(UP,VP)==Pminus17

print('RL159 joint distinguished-root SNF consequences: PASS')
print('grid determinant/evaluation/augmented-minor checks: PASS')
print('RL158 red-team: d=1631, P(rho)=17, augmented divisor=1: PASS')
print('explicit Bezout identities for d, T-rho, P-17: PASS')
print('scope=exact structural theorem + tautology barrier; no global gate closure')

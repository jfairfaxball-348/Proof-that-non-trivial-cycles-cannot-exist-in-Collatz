#!/usr/bin/env python3
"""Exact dependency-free audit for RL158."""
from math import gcd


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def sylvester_resultant(f,g):
    f=trim(f); g=trim(g)
    m=len(f)-1; n=len(g)-1
    # descending coefficients
    F=list(reversed(f)); G=list(reversed(g))
    N=m+n
    M=[]
    for i in range(n): M.append([0]*i+F+[0]*(n-1-i))
    for i in range(m): M.append([0]*i+G+[0]*(m-1-i))
    # fraction-free Bareiss determinant
    A=[row[:] for row in M]
    sign=1; prev=1
    for k in range(N-1):
        if A[k][k]==0:
            r=next(r for r in range(k+1,N) if A[r][k]!=0)
            A[k],A[r]=A[r],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,N): A[i][k]=0
        for j in range(k+1,N): A[k][j]=A[k][j]
    return sign*A[-1][-1]

def peval(c,x,m):
    return sum(a*pow(x,i,m) for i,a in enumerate(c))%m

A,L=13,8
h=[0,0,1,1,0,0,0,0,0]
b=[(A*j)//L for j in range(L+1)]
assert h[0]==h[-1]==0 and max(h)>0 and all(v>=0 for v in h)
S=[b[j]-h[j] for j in range(L+1)]
assert all(S[j+1]-S[j]>=1 for j in range(L))
D=2**A-3**L
assert D==1631 and D==7*233 and gcd(A,L)==1
p=pow(A,-1,L); u=(A*p-1)//L
assert (p,u)==(5,8) and A*p-u*L==1
rho=pow(2,u,D)*pow(pow(3,p,D),-1,D)%D
assert rho==1377
H=max(h)
P=[0]*L
for j in range(L): P[(A*j)%L]+=2**(H-h[j])
assert P==[2,2,1,2,2,2,2,1]
B1=[-1]+[0]*(L-1)+[2]
B2=[-2]+[0]*(A-L-1)+[3]
R1=sylvester_resultant(B1,P)
R12=sylvester_resultant(B1,B2)
assert R1==D
assert abs(R12)==D
assert peval(P,rho,D)==17
assert peval(B1,rho,D)==0 and peval(B2,rho,D)==0
for q,common,twist in [(7,2,6),(233,19,221)]:
    rq=rho%q
    roots1=[x for x in range(q) if peval(B1,x,q)==0]
    rootsP=[x for x in roots1 if peval(P,x,q)==0]
    roots12=[x for x in roots1 if peval(B2,x,q)==0]
    assert rootsP==[common]
    assert roots12==[rq]
    z=common*pow(rq,-1,q)%q
    assert z==twist and z!=1 and pow(z,L,q)==1
    assert peval(P,rq,q)!=0 and peval(B2,common,q)!=0
print('RL158 resultant-character ambiguity: PASS')
print('example=(A,L)=(13,8), D=1631=7*233, Res(B1,P)=1631, P(rho)=17')
print('nonphysical twists: mod7=6, mod233=221')
print('distinguished companion: B2=3T^5-2; |Res(B1,B2)|=1631')
print('scope=method barrier + next arithmetic interface; no singleton exclusion')

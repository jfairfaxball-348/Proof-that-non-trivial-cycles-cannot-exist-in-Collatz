#!/usr/bin/env python3
from fractions import Fraction

def v2_int(n):
    assert n
    n=abs(n); return (n & -n).bit_length()-1

def v2_rat(q):
    q=Fraction(q)
    return v2_int(q.numerator)-v2_int(q.denominator)

def collatz_affine(word):
    A=1; Q=0; t=0; r=0
    for b in word:
        if b=='1':
            A*=3; Q=3*Q+2**t; r+=1
        t+=1
    return A,Q,t,r

def C(word,z):
    A,Q,t,r=collatz_affine(word)
    return Fraction(A*z+Q,2**t)

def step(d,J,x):
    K=J+2**d-1
    if K%2==0:
        if x:d2,K2=d,3*K//2
        else:d2,K2=d,(K+3**d-1)//2
    else:
        if x:
            if d<=1:return None
            d2,K2=d-1,(K-1)//2
        else:d2,K2=d+1,3*(K+3**d)//2
    return d2,K2-2**d2+1,d-1
checks=0
for word in ('','0','1','00','01','10','11','00101','110010'):
    A,Q,t,r=collatz_affine(word); assert A==3**r
    for alpha in (Fraction(-1),Fraction(-2,3)):
        rho=Fraction(2**t*alpha-Q,3**r); assert C(word,rho)==alpha
        for n in (-17,-5,1,7,42):
            if Fraction(n)!=rho:
                assert v2_rat(C(word,Fraction(n))-alpha)==v2_rat(Fraction(n)-rho)-t; checks+=1
for c in (-9,-5,-1,1,3,7,27):
    for nstar in (-11,0,6):
        for rho in (Fraction(-1),Fraction(-2,3),Fraction(13,9)):
            sigma=(rho-nstar)/c
            for u in (-8,-1,0,3,19):
                if Fraction(nstar+c*u)!=rho:
                    assert v2_rat(Fraction(nstar+c*u)-rho)==v2_rat(Fraction(u)-sigma); checks+=1
x='10000011'; y='10010010'; d,J,H=1,-13,0; trace=[]
for bit in x:
    o=step(d,J,int(bit)); assert o is not None
    d,J,c=o; H+=c; trace.append((d,J,H))
assert trace==[(1,-19,0),(1,-9,0),(1,-4,0),(2,-3,0),(2,1,1),(2,3,2),(2,6,3),(1,3,4)]
apos=[i+1 for i,b in enumerate(x) if b=='1']; bpos=[i+1 for i,b in enumerate(y) if b=='1']
disp=[a-b for a,b in zip(apos,bpos)]
assert disp==[0,3,1] and sum(disp)==4 and sum(v!=0 for v in disp)==2
n=1; haz=[]; seen=set()
while n not in seen:
    seen.add(n)
    if n%2==0:haz.append(v2_int(3*n+2));n//=2
    else:haz.append(v2_int(n+1));n=(3*n+1)//2
assert haz==[1,3] and max(haz)==3
print('RL293 danger-tree pullback/support barrier regression: PASS')
print('static_and_pullback_identity_checks=',checks)
print('fixed_seed_witness_endpoint=(d1,J3,H4)')
print('witness_rank_displacements=',disp)
print('witness_displaced_rank_support=2')
print('witness_boundary_Beta=3')
print('classification_candidates=FIXED_SEGMENT_STATIC_DANGER_TREE_ODD_AFFINE_PULLBACK_ISOMETRY;DANGER_TREE_SUPPORT_COUNT_AND_EXCURSION_COUNT_CHARGE_BARRIER')

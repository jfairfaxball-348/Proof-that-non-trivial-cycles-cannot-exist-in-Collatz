#!/usr/bin/env python3
from math import gcd
import sympy as sp

# Audited RL43 proper-factor countermodel.
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split()
loops=15
pairs=[(0,1)]
for token in path:
    if token=='PUMP': pairs += [(1,1)]*loops
    else: pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
beta=[y for x,y in pairs]
v=[1,1]+beta

def Q(w):
    rem=sum(w); out=0
    for i,b in enumerate(w):
        if b:
            out += (1<<i)*3**(rem-1); rem-=1
    return out

def runs(w):
    out=[];rank=0;i=0
    while i<len(w):
        if not w[i]: i+=1; continue
        t=i;m=rank+1;k=0
        while i<len(w) and w[i]: rank+=1;k+=1;i+=1
        out.append((t,m,k))
    return out

a=len(v); ell=sum(v); q=a-ell
assert (a,ell,q)==(65,41,24)
X=1<<a;Y=3**ell;M=X-Y
x=sp.symbols('x')
f=3*x**q-2
P=sp.Integer(4)
for t,m,k in runs(v):
    b=a*m-ell*t
    c=b+k*q
    P += 3*(x**b-x**c)

# Direct exact resultant.
Rdirect=int(sp.resultant(f,P,x))

def strip3(n):
    n=abs(n); s=0
    while n%3==0:
        n//=3;s+=1
    return n,s
R3,v3=strip3(Rdirect)

# Exact remainder in QQ[x] and resultant.  Res(f,P)=3^(deg(P)-deg(rem))*Res(f,rem)
# when P is replaced by its Euclidean remainder modulo f; therefore the 3-free part is unchanged.
rem=sp.rem(P,f,domain=sp.QQ)
Rrem=sp.resultant(f,rem,x)
num,den=sp.fraction(sp.cancel(Rrem))
num=int(num); den=int(den)
assert den>0
# denominator is a power of 3 only
facden=sp.factorint(den)
assert set(facden).issubset({3})
num3,v3n=strip3(num)
assert num3==R3

assert R3>M
assert R3 > (1<<592)*M
assert gcd(R3,M)==1
print('RL45 resultant-benchmark obstruction verifier: PASS')
print('a,ell,q =',a,ell,q)
print('deg(P) =',sp.degree(P,x),'deg(remainder) =',sp.degree(rem,x))
print('direct resultant bit length =',abs(Rdirect).bit_length(),'v3 =',v3)
print('3-free resultant bit length =',R3.bit_length())
print('X-Y bit length =',M.bit_length())
print('bit-length gap =',R3.bit_length()-M.bit_length())
print('3-free resultant > X-Y =',R3>M)
print('3-free resultant > 2^592*(X-Y) =',R3 > (1<<592)*M)
print('gcd(3-free resultant, X-Y) =',gcd(R3,M))
print('distinct reduced exponents =',len(sp.Poly(rem,x).terms()))

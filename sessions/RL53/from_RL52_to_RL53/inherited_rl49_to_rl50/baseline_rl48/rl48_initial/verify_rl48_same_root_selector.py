#!/usr/bin/env python3
from math import gcd

# Audited RL43/RL45 proper-factor countermodel, copied from the inherited
# RL45 resultant verifier for an independent same-root regression.
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split()
loops=15
pairs=[(0,1)]
for token in path:
    if token=='PUMP':
        pairs += [(1,1)]*loops
    else:
        pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
beta=[y for x,y in pairs]
v=[1,1]+beta

def runs(w):
    out=[]; rank=0; i=0
    while i<len(w):
        if not w[i]:
            i+=1; continue
        t=i; m=rank+1; k=0
        while i<len(w) and w[i]:
            rank+=1; k+=1; i+=1
        out.append((t,m,k))
    return out

def Q(w):
    rem=sum(w); out=0
    for i,b in enumerate(w):
        if b:
            out += (1<<i)*3**(rem-1)
            rem -= 1
    return out

def egcd(a,b):
    if b==0:
        return (1,0,a)
    x,y,g=egcd(b,a%b)
    return (y, x-(a//b)*y, g)

a=len(v); ell=sum(v); q=a-ell
assert (a,ell,q)==(65,41,24)
X=1<<a; Y=3**ell; M=X-Y
assert M>0 and gcd(M,6)==1 and gcd(q,ell)==1

u,wbez,g=egcd(q,ell)
assert g==1 and u*q+wbez*ell==1

# rho=(2/3)^u (1/2)^v = 2^(u-v) 3^(-u), using modular unit powers.
def upow(base, exp):
    if exp>=0:
        return pow(base,exp,M)
    return pow(pow(base,-1,M),-exp,M)

rho=(upow(2,u-wbez)*upow(3,-u))%M
assert (3*pow(rho,q,M)-2)%M==0
assert (2*pow(rho,ell,M)-1)%M==0

# Direct phase evaluation from exponents b,c.
p_direct=4
for t,m,k in runs(v):
    Z=t-(m-1)
    b=q*m+ell*(1-Z)
    c=b+k*q
    assert b==a*m-ell*t
    p_direct=(p_direct+3*(pow(rho,b,M)-pow(rho,c,M)))%M

# Run-boundary scalar evaluation.
p_runs=4
for t,m,k in runs(v):
    num=(pow(2,t,M)*(pow(3,k,M)-pow(2,k,M)))%M
    den=pow(3,m+k-1,M)
    p_runs=(p_runs+num*pow(den,-1,M))%M

# Collapse to Q(v)/3^ell.
qv=Q(v)
p_q=(4+(qv%M)*pow(Y,-1,M))%M

assert p_direct==p_runs==p_q
assert (p_q*Y-(qv+4*Y))%M==0
assert p_q!=0
assert gcd(p_q,M)==1

print('RL48 canonical same-root selector verifier: PASS')
print('a,ell,q =',a,ell,q)
print('Bezout (u,v) =',u,wbez)
print('rho mod M =',rho)
print('f(rho) mod M = 0')
print('L(rho) mod M = 0')
print('P(rho) mod M =',p_q)
print('gcd(P(rho),M) =',gcd(p_q,M))
print('P(rho) == 4+Q(v)/3^ell mod M: PASS')

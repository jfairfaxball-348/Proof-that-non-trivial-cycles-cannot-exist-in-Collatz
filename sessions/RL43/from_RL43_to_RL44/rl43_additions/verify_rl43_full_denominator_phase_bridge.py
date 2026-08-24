#!/usr/bin/env python3
from math import gcd
from fractions import Fraction

# Q convention used by the retained half-word identities.
def Q(w):
    rem=sum(w)
    out=0
    for i,b in enumerate(w):
        if b:
            out += (1<<i)*3**(rem-1)
            rem-=1
    return out

def runs(w):
    # (start position, start rank 1-based, length)
    out=[];rank=0;i=0
    while i<len(w):
        if not w[i]:
            i+=1;continue
        t=i;m=rank+1;k=0
        while i<len(w) and w[i]:
            rank+=1;k+=1;i+=1
        out.append((t,m,k))
    return out

def primitive(w):
    n=len(w)
    for d in range(1,n):
        if n%d==0 and w==w[:d]*(n//d):
            return False
    return True

def bezout_phase(a,l):
    # positive representative sufficient for this verifier
    for p in range(1,l+1):
        n=a*p-1
        if n%l==0:
            return n//l,p
    raise AssertionError

# ------------------------------------------------------------------
# Explicit proper-factor countermodel from the quotient excursion automaton.
# ------------------------------------------------------------------
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split()
loops=15
pairs=[(0,1)]
for token in path:
    if token=='PUMP':
        pairs += [(1,1)]*loops
    else:
        pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
alpha=[x for x,y in pairs]
beta=[y for x,y in pairs]

# Canonical one-excursion condition.
d=0
for idx,(x,y) in enumerate(pairs):
    d += y-x
    if idx<len(pairs)-1:
        assert d>0
assert d==0
assert sum(alpha)==sum(beta)==39
apos=[i for i,b in enumerate(alpha) if b]
bpos=[i for i,b in enumerate(beta) if b]
deltas=[i-j for i,j in zip(apos,bpos)]
assert all(q>=1 for q in deltas)
assert sum(deltas)==65
assert sum(q-1 for q in deltas)==26

u=[1,1]+alpha
v=[1,1]+beta
a=len(u);l=sum(u)
assert (a,l)==(65,41)
assert sum(v)==l and gcd(a,l)==1
X=1<<a;Y=3**l
assert X>Y and 15*X*X<16*Y*Y
U=Q(u);V=Q(v);Fp=X+Y;Fm=X-Y;D=X*X-Y*Y
assert U-V==4*Fp
assert primitive(u+v)

Quv=Y*U+X*V
Qvu=Y*V+X*U
assert Qvu-Quv==D*4
assert Quv%D !=0 and Qvu%D !=0
assert (V+4*Y)%Fm !=0

# Exact factorization identity, independent of divisibility.
assert Quv==Fp*(V+4*Y)
assert gcd(Fp,Fm)==1

# Phase relation modulo X-Y.
m0,p0=bezout_phase(a,l)
assert a*p0-m0*l==1
rho=(pow(2,m0,Fm)*pow(pow(3,p0,Fm),-1,Fm))%Fm
assert (3*pow(rho,a,Fm)-1)%Fm==0
assert (2*pow(rho,l,Fm)-1)%Fm==0
qshort=a-l
assert (3*pow(rho,qshort,Fm)-2)%Fm==0

R=runs(v)
# beta has 24 zeroes and ends zero; full v has the same 23 one-runs here.
assert len(R)==23
phase=4
for t,m,k in R:
    b=a*m-l*t
    c=a*(m+k)-l*(t+k)
    assert b>0 and c>b
    phase += 3*(pow(rho,b,Fm)-pow(rho,c,Fm))
phase%=Fm
direct=(V*pow(Y,-1,Fm)+4)%Fm
assert phase==direct and phase!=0

# Run compression exact over rationals after multiplying by Y.
run_value=0
for t,m,k in R:
    # Y * 3(2^t 3^-m - 2^(t+k)3^-(m+k))
    run_value += 3*(Fraction((1<<t)*3**(l-m),1) - Fraction(1<<(t+k),3**(m+k-l))) if m+k>l else 3*((1<<t)*3**(l-m) - (1<<(t+k))*3**(l-m-k))
assert run_value==V

# ------------------------------------------------------------------
# Small exhaustive sanity check of the factor identity and phase transform
# for every equal-weight pair whose U-V is divisible by X+Y.
# ------------------------------------------------------------------
checked=0; phase_checked=0
for a0 in range(3,10):
    for l0 in range(1,a0):
        if gcd(a0,l0)!=1: continue
        X0=1<<a0;Y0=3**l0
        if X0<=Y0: continue
        Fp0=X0+Y0;Fm0=X0-Y0;D0=X0*X0-Y0*Y0
        m,p=bezout_phase(a0,l0)
        rho0=(pow(2,m,Fm0)*pow(pow(3,p,Fm0),-1,Fm0))%Fm0 if Fm0>1 else 0
        words=[]
        for mask in range(1<<a0):
            if mask.bit_count()==l0:
                w=[(mask>>i)&1 for i in range(a0)]
                words.append((w,Q(w)))
        for u0,U0 in words:
            for v0,V0 in words:
                diff=U0-V0
                if diff%Fp0: continue
                G=diff//Fp0
                Quv0=Y0*U0+X0*V0
                assert Quv0==Fp0*(V0+Y0*G)
                assert (Quv0%D0==0)==((V0+Y0*G)%Fm0==0)
                checked+=1
                if Fm0>1:
                    ph=G
                    for t,mm,k in runs(v0):
                        b=a0*mm-l0*t
                        c=a0*(mm+k)-l0*(t+k)
                        ph += 3*(pow(rho0,b,Fm0)-pow(rho0,c,Fm0))
                    assert ph%Fm0==(V0*pow(Y0,-1,Fm0)+G)%Fm0
                    phase_checked+=1

print('RL43 full-denominator phase bridge verifier: PASS')
print('explicit countermodel: (a,ell)=(65,41), one excursion p=39, rho_exc=65, e=26')
print('proper factor U-V=4(X+Y): PASS; full D divisibility: FAIL as intended')
print('one-excursion phase runs =',len(R),'support bound =',2*26+3)
print('small factor identities checked =',checked,'phase identities =',phase_checked)

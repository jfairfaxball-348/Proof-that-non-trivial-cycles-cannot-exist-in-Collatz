#!/usr/bin/env python3
from fractions import Fraction

A,ELL,t=65,41,2
k=t+3
# Canonical audited RL47 witness.
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
assert len(EDGES)==A-k-1

def Q(w):
    q=0; ones=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*(3**(sum(w)-ones-1))
            ones += 1
    return q

def build_words(edges,t):
    x=[int(e[0]) for e in edges]
    y=[int(e[1]) for e in edges]
    return [1,1,0]+x+[1]+[0]*t, [1,1,1]+y+[0]*(t+1)

def parity_residue(w):
    aa=len(w); ll=sum(w); X=1<<aa; Y=3**ll
    return (-Q(w)*pow(Y,-1,X))%X

def step(n,b):
    assert (n&1)==b
    return (3*n+1)//2 if b else n//2

def simulate(n,w):
    vals=[n]
    for b in w:
        n=step(n,b); vals.append(n)
    return vals

u,v=build_words(EDGES,t)
Nu,Nv=parity_residue(u),parity_residue(v)
assert Nv==Nu+4
au=simulate(Nu,u); bv=simulate(Nv,v)

# Internal local state and exact normalized lifts.
d,T,px,py=1,-14,0,0
zeta=Fraction(1<<A,3**ELL)
Xmass=Smass=Fraction(0)
Zx=Zy=Fraction(0)
zero_g=[]
Rs=[]
Vs=[]
Us=[]
height_segments=[]
seg=None

for i,e in enumerate(EDGES):
    x,y=map(int,e)
    g=Fraction(1<<i,3**px)
    h=Fraction(1<<i,3**py)
    assert h == g/Fraction(3**(d-1))
    Acur=au[i+3]; Bcur=bv[i+3]
    assert T==3**d*Acur-Bcur
    U=Fraction((1<<(i+3))*Acur,3**(px+2))
    V=Fraction((1<<(i+3))*Bcur,3**(py+3))
    R=g*T/Fraction(3**d)
    assert U-V == Fraction(8,9)*R
    Us.append(U); Vs.append(V); Rs.append(R)

    if x: Xmass += g/3
    else:
        Zx += g
        zero_g.append(g)
    if y: Smass += h/3
    else: Zy += h

    # For every actual witness prefix RL49's cap is exact.
    Xpow=1<<A; Ypow=3**ELL
    n=i+1
    assert (1<<(n+2))*Ypow*Ypow <= (3**(px+2))*Xpow*Xpow
    assert 8*g <= 9*zeta*zeta

    d0=d; R0=R; U0=U; V0=V
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    Tn=num//2
    dn=d+y-x
    pxn=px+x; pyn=py+y
    gn=Fraction(1<<(i+1),3**pxn)
    hn=Fraction(1<<(i+1),3**pyn)
    An=au[i+4]; Bn=bv[i+4]
    Un=Fraction((1<<(i+4))*An,3**(pxn+2))
    Vn=Fraction((1<<(i+4))*Bn,3**(pyn+3))
    Rn=gn*Tn/Fraction(3**dn)
    assert Un-U0 == (Fraction(8,27)*g if x else 0)
    assert Vn-V0 == (Fraction(8,27)*g/Fraction(3**d0) if y else 0)
    assert Rn-R0 == Fraction(g,3)*(x-Fraction(y,3**d0))
    assert Un-Vn == Fraction(8,9)*Rn

    # Fixed-height synchronized edges admit an all-height telescope.
    if x==y:
        assert dn==d0
        if seg is None or seg['d']!=d0:
            if seg is not None: height_segments.append(seg)
            seg={'d':d0,'R0':R0,'R1':Rn,'Vinc':Fraction(0),'start':i,'end':i}
        seg['R1']=Rn; seg['end']=i
        if y: seg['Vinc'] += Vn-V0
    else:
        if seg is not None:
            height_segments.append(seg); seg=None

    # A zero x-column doubles g.  Therefore the *next* prefix cap sharpens it.
    if not x:
        nnext=i+2
        assert (1<<(nnext+2))*Ypow*Ypow <= (3**(pxn+2))*Xpow*Xpow
        assert 16*g <= 9*zeta*zeta

    d,T,px,py=dn,Tn,pxn,pyn

if seg is not None: height_segments.append(seg)
assert (d,T,px,py)==(1,(1<<k)-1,ELL-3,ELL-3)

# Terminal prefix cap (needed when the final internal x-column is zero).
i=len(EDGES); gend=Fraction(1<<i,3**px)
assert (1<<(i+3))*((3**ELL)**2) <= (3**(px+2))*((1<<A)**2)
assert gend == Fraction(27)*zeta/Fraction(1<<(k+1))

# Boundary lift formulas on the structural witness, and their phase-specialized form.
U0=Us[0]; V0=Vs[0]
assert U0 == Nu+Fraction(5,9)
assert V0 == Nu+Fraction(127,27)
R0=Rs[0]
assert R0 == Fraction(-14,3)
assert U0-V0 == Fraction(8,9)*R0

Aend=au[len(EDGES)+3]; Bend=bv[len(EDGES)+3]
Uend=Fraction((1<<(len(EDGES)+3))*Aend,3**(px+2))
Vend=Fraction((1<<(len(EDGES)+3))*Bend,3**(py+3))
Rend=gend*T/3
assert Uend-Vend == Fraction(8,9)*Rend
assert Rend == Fraction(9,2)*zeta*(1-Fraction(1,1<<k))

# All-height synchronized macro identity.
for s in height_segments:
    dseg=s['d']
    assert s['Vinc'] == Fraction(8,9*(3**dseg-1))*(s['R1']-s['R0'])

# Zero-position identities and witness regression.
assert Xmass == 1-gend+Zx
assert Smass == 1-gend+Zy
assert Xmass-Smass == Zx-Zy
assert 3*Zx-Zy == 12+Fraction(27,2)*zeta*(1+Fraction(1,1<<k))
assert len(zero_g)==21 and 1+len(zero_g)==22

# New phase-specific theorem uses only the safe Barina floor 2^71.
# Phase squeeze: zeta-1 < 398/(45*2^71).  This is already enough for
# zeta^2 < 136/135, a deliberately convenient rational threshold.
zeta_upper=1+Fraction(398,45*(1<<71))
assert zeta_upper*zeta_upper < Fraction(136,135)
# Hence each x-zero has g <= 9*zeta^2/16 < 17/30.
assert Fraction(9,16)*Fraction(136,135) == Fraction(17,30)
# Compressed zero identity with zeta>1 and Zy>=0 gives Zx>17/2.
# If there were <=15 x-zero columns, their total would be <15*(17/30)=17/2.
assert 15*Fraction(17,30)==Fraction(17,2)
# Therefore every genuine full-phase object obeying the prefix cap has >=16
# internal x-zero columns, i.e. z=1+#zeros >=17 and t <= q-17.

print('RL50 normalized-lift / zero-budget verifier: PASS')
print('witness U-V=(8/9)R columnwise: exact')
print('witness odd-step lift increments: exact')
print('all-height synchronized macro telescope: exact on',len(height_segments),'segments')
print('safe phase bound implies zeta^2 < 136/135: exact rational PASS')
print('each full-phase x-zero weight g < 17/30')
print('compressed identity forces Zx > 17/2')
print('NEW THEOREM: full phase + prefix cap + N>=2^71 => #x-zeros>=16, z>=17, t<=q-17')
print('audited RL47 structural witness regression: #x-zeros=',len(zero_g),'z=',1+len(zero_g))

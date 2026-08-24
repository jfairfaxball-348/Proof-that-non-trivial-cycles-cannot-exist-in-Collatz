#!/usr/bin/env python3
from fractions import Fraction

# RL50 exact verifier for:
#  (i) zero-position displacement H/E representation on the audited witness;
# (ii) height-one complete-excursion macro identities;
# (iii) denominator-independent sequential-prefix-cap zero-mass certificates.

A,ELL,t=65,41,2
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()

def jstep(d,J,x,y):
    if (x,y)==(0,0): return d,(J+3**d-2**d)//2
    if (x,y)==(1,1): return d,(3*J+2**d-1)//2
    if (x,y)==(0,1): return d+1,(3*J+3**(d+1)-2**d-1)//2
    if (x,y)==(1,0): return d-1,J//2
    raise AssertionError

def winc(d,g,x,y):
    if (x,y)==(0,0): return g*Fraction(3**d-2**d,3**d)
    if (x,y)==(1,1): return g*Fraction(2**d-1,3**(d+1))
    if (x,y)==(0,1): return g*Fraction(3**(d+1)-2**d-1,3**(d+1))
    if (x,y)==(1,0): return Fraction(0)
    raise AssertionError

def eps(d,g,x,y):
    ds = g/Fraction(3**d) if y else Fraction(0)
    dz = g if not x else Fraction(0)
    return 3*winc(d,g,x,y)-ds-dz

# --- audited-witness zero-position representation and excursion macros ---
d,J,px,py=1,-13,0,0
H=0
Zx=Fraction(0); Zy=Fraction(0)
X=Fraction(0); S=Fraction(0)
xzero=[]; yzero=[]
excursions=[]
in_exc=False
exc=None

for i,e in enumerate(EDGES):
    x,y=map(int,e)
    assert d==1+py-px
    g=Fraction(1<<i,3**px)
    h=Fraction(1<<i,3**py)
    assert h==g/Fraction(3**(d-1))

    if not x:
        xzero.append((i,g))
        Zx += g
    else:
        X += g/3
    if not y:
        yzero.append((i,h))
        Zy += h
    else:
        S += g/Fraction(3**d)

    if d==1 and (x,y)==(0,1) and not in_exc:
        in_exc=True
        L0=g*Fraction(J-1,2)
        exc=dict(L0=L0,E=Fraction(0),S=Fraction(0),energy=Fraction(0))

    if in_exc:
        exc['E'] += (g/3 if x else 0) - (g/Fraction(3**d) if y else 0)
        exc['S'] += g/Fraction(3**d) if y else 0
        exc['energy'] += eps(d,g,x,y)

    H += d-1
    d2,J2=jstep(d,J,x,y)
    px += x; py += y
    g2=Fraction(1<<(i+1),3**px)

    if in_exc and d2==1:
        L1=g2*Fraction(J2-1,2)
        exc['L1']=L1
        excursions.append(exc)
        in_exc=False; exc=None

    d,J=d2,J2

assert not in_exc
assert d==1
assert len(xzero)==len(yzero)
assert H==104
E=X-S
assert E==Zx-Zy

# Pair the j-th x-zero and y-zero.
Hzeros=0
Ezeros=Fraction(0)
for (u,w),(v,hy) in zip(xzero,yzero):
    assert u<=v
    r=v-u
    Hzeros += r
    assert hy == w*Fraction(2**r,3**r)
    Ezeros += w*(1-Fraction(2**r,3**r))
assert Hzeros==H
assert Ezeros==E

# Every complete excursion has exact macro energy 2E, S<=E, and
# Delta L = S + 3E/2.
for ex in excursions:
    assert ex['energy']==2*ex['E']
    assert ex['E']>=0
    assert ex['S']<=ex['E']
    dL=ex['L1']-ex['L0']
    assert dL==ex['S']+Fraction(3,2)*ex['E']
    assert Fraction(3,2)*ex['E'] <= dL <= Fraction(5,2)*ex['E']

# --- sequential prefix-cap certificate ---
# Safe phase gives every prefix g<17/15.  Immediately before an x-zero,
# the next prefix doubles g, so relaxing strictness gives g<=17/30.
CAP=Fraction(17,30)

# Exact decision search. State g=2^i/3^p, with rem zero actions left.
# An arbitrary number of x=1 actions is allowed.  Memoization keeps only
# the largest accumulated zero mass reaching the same future state.
# Future zero mass is bounded both by rem*CAP and by (2^rem-1)*g if all
# future contractions/cap restrictions are discarded.
def can_exceed_with_n_zeros(n,target):
    seen={}
    p2=[1]
    p3=[1]
    nodes=0

    def gval(i,p):
        while len(p2)<=i: p2.append(p2[-1]*2)
        while len(p3)<=p: p3.append(p3[-1]*3)
        return Fraction(p2[i],p3[p])

    def rec(i,p,rem,total):
        nonlocal nodes
        nodes += 1
        key=(i,p,rem)
        old=seen.get(key)
        if old is not None and total<=old:
            return False
        seen[key]=total
        g=gval(i,p)
        if rem==0:
            return total>target
        ub=total+min(rem*CAP,(2**rem-1)*g)
        if ub<=target:
            return False
        # x=0 (zero): reward g, next scalar 2g.  Legal only if the
        # relaxed post-zero prefix cap remains satisfied.
        if g<=CAP and rec(i+1,p,rem-1,total+g):
            return True
        # x=1: no zero reward, scalar -> 2g/3.
        return rec(i+1,p+1,rem,total)

    hit=rec(0,0,n,Fraction(0))
    return hit,nodes,len(seen)

hit18,n18,s18=can_exceed_with_n_zeros(18,Fraction(17,2))
assert not hit18
hit25,n25,s25=can_exceed_with_n_zeros(25,Fraction(143,12))
assert not hit25

# Clean symbolic implications used in the note.
assert Fraction(51,2)-Fraction(5,3)==Fraction(143,6)
assert Fraction(143,6)/2==Fraction(143,12)
assert Fraction(5,2)*Fraction(5,3)==Fraction(25,6)
assert (2*Fraction(25,6)+Fraction(17,15))/3==Fraction(142,45)

print('RL50 zero-displacement / excursion-return macro verifier: PASS')
print('audited witness: H=sum zero delays and E=sum w*(1-(2/3)^delay) exactly')
print('complete d=1 return excursions: energy=2E, S<=E, Delta L=S+3E/2')
print('safe survivor interface: total excursion Delta L <25/6; first positive return W<142/45')
print('sequential-cap exact certificate: 18 zeros cannot exceed Zx=17/2',f'(nodes={n18}, states={s18})')
print('sequential-cap exact certificate: 25 zeros cannot exceed Zx=143/12',f'(nodes={n25}, states={s25})')
print('NEW UNIFORM FULL-PHASE BOUND: internal x-zeros >=19, hence z>=20')
print('NEW SAFE-SURVIVOR BOUND: internal x-zeros >=26, hence z>=27')

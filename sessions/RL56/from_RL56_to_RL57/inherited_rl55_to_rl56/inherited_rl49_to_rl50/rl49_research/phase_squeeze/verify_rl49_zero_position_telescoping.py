#!/usr/bin/env python3
from fractions import Fraction

EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
A,L,t=65,41,2
k=t+3
r=L-3
m=A-k-1
assert len(EDGES)==m
assert sum(e[0]=='1' for e in EDGES)==r
assert sum(e[1]=='1' for e in EDGES)==r

px=py=0
g=Fraction(1)
h=Fraction(1)
Xn=Fraction(0); S=Fraction(0)
Zx=Fraction(0); Zy=Fraction(0)
for i,e in enumerate(EDGES):
    x,y=map(int,e)
    assert g == Fraction(1<<i,3**px)
    assert h == Fraction(1<<i,3**py)
    if x:
        Xn += g/3
    else:
        Zx += g
    if y:
        S += h/3
    else:
        Zy += h
    g *= Fraction(2,3**x)
    h *= Fraction(2,3**y)
    px += x; py += y

assert px==py==r
assert g==h
gend=g
zeta=Fraction(1<<A,3**L)
assert gend == Fraction(27)*zeta/Fraction(1<<(k+1))

# Exact zero-position telescoping identities.
assert Xn == 1-gend+Zx
assert S  == 1-gend+Zy
E=Xn-S
assert E==Zx-Zy

# Rank-transport terminal identity in compressed zero form.
Lam=Fraction(14)+Fraction(27,2)*zeta*(1-Fraction(1,1<<k))
assert 3*Xn-S==Lam
assert 3*Zx-Zy == 12+Fraction(27,2)*zeta*(1+Fraction(1,1<<k))

# Full-phase scalar identity is algebraic (the structural witness need not be phase-valid).
# Define formal Ndelta := (Q(v)+4Y)/Y. It equals (127+8S)/27 identically.
formal_Ndelta=Fraction(127+8*S,27)
assert formal_Ndelta == 5+Fraction(8,27)*(Zy-gend)

# Prefix cap implies g_i <= (9/8) zeta^2 at every actual prefix in this witness.
X=1<<A; Y=3**L
px=0
for i,e in enumerate(EDGES):
    n=i+1
    cap=(1<<(n+2))*Y*Y <= (3**(px+2))*X*X
    assert cap
    gi=Fraction(1<<i,3**px)
    assert 8*gi <= 9*zeta*zeta
    px += int(e[0])

print('RL49 zero-position telescoping verifier: PASS')
print('Xn = 1-g_end+Zx: exact')
print('S  = 1-g_end+Zy: exact')
print('E  = Zx-Zy: exact')
print('compressed rank identity: exact')
print('formal phase scalar 27*Ndelta = 127+8S: exact')
print('prefix cap 8*g_i <= 9*zeta^2: exact on audited witness')

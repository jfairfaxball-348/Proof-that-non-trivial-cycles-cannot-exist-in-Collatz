#!/usr/bin/env python3
from fractions import Fraction

# Exact RL50 verifier for the monotone J-lift
#   W = g J / 3^d,    J = T + 3^d - 2^d,
# and the resulting positive local decomposition of the global rank defect E.

A,ELL,t=65,41,2
k=t+3
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
assert len(EDGES)==A-k-1

# Closed J transition formulas and W increments.
def jstep(d,J,x,y):
    if (x,y)==(0,0):
        return d, (J + 3**d - 2**d)//2
    if (x,y)==(1,1):
        return d, (3*J + 2**d - 1)//2
    if (x,y)==(0,1):
        return d+1, (3*J + 3**(d+1) - 2**d - 1)//2
    if (x,y)==(1,0):
        return d-1, J//2
    raise AssertionError

def w_increment(d,g,x,y):
    if (x,y)==(0,0):
        return g * Fraction(3**d-2**d,3**d)
    if (x,y)==(1,1):
        return g * Fraction(2**d-1,3**(d+1))
    if (x,y)==(0,1):
        return g * Fraction(3**(d+1)-2**d-1,3**(d+1))
    if (x,y)==(1,0):
        return Fraction(0)
    raise AssertionError

def local_energy(d,g,x,y):
    # 3 Delta W minus this column's S-mass and x-zero mass.
    sinc = g/Fraction(3**d) if y else Fraction(0)
    zinc = g if not x else Fraction(0)
    return 3*w_increment(d,g,x,y)-sinc-zinc

# Symbolic/integer sign checks over a wide height window; the displayed
# formulas prove the sign for all d>=1.
for d in range(1,100):
    g=Fraction(1)
    e00=local_energy(d,g,0,0)
    e11=local_energy(d,g,1,1)
    e01=local_energy(d,g,0,1)
    e10=local_energy(d,g,1,0)
    assert e00 == 2-Fraction(2**d,3**(d-1))
    assert e11 == Fraction(2**d-2,3**d)
    assert e01 == 2-Fraction(2**d+2,3**d)
    assert e10 == 0
    assert min(e00,e11,e01,e10) >= 0
    if d==1:
        assert e00==e11==e10==0 and e01==Fraction(2,3)
    else:
        assert e00>0 and e11>0 and e01>0 and e10==0

# Exact audited-witness regression from (d,T,J,g)=(1,-14,-13,1).
d,T,J,px=1,-14,-13,0
W=Fraction(-13,3)
S=Fraction(0)
Zx=Fraction(0)
X=Fraction(0)
energy=Fraction(0)
H=0

for i,e in enumerate(EDGES):
    x,y=map(int,e)
    g=Fraction(1<<i,3**px)
    assert J == T + 3**d - 2**d
    assert W == g*J/Fraction(3**d)

    H += d-1
    if x: X += g/3
    else: Zx += g
    if y: S += g/Fraction(3**d)

    inc=w_increment(d,g,x,y)
    en=local_energy(d,g,x,y)
    assert inc>=0 and en>=0
    energy += en

    # Compare the closed J map to the inherited T recurrence.
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    Tn=num//2
    dn=d+y-x
    Jn=Tn+3**dn-2**dn
    d2,J2=jstep(d,J,x,y)
    assert (d2,J2)==(dn,Jn)

    pxn=px+x
    gn=Fraction(1<<(i+1),3**pxn)
    Wn=gn*Jn/Fraction(3**dn)
    assert Wn-W == inc

    d,T,J,px,W=dn,Tn,Jn,pxn,Wn

assert d==1 and T==(1<<k)-1 and J==(1<<k)
zeta=Fraction(1<<A,3**ELL)
gend=Fraction(1<<len(EDGES),3**px)
assert gend == Fraction(27)*zeta/Fraction(1<<(k+1))
assert W == Fraction(9,2)*zeta
assert W-Fraction(-13,3) == Fraction(13,3)+Fraction(9,2)*zeta

E=X-S
assert energy == 2*E
assert H==104

# The identity is structural: summing local energies gives
#   3 Delta W - (S+Zx).
# The inherited exact zero/rank identities reduce this to exactly 2E.
assert energy == 3*(Fraction(13,3)+Fraction(9,2)*zeta) - (S+Zx)

# A useful corollary: every x-zero costs at least g/3 in W, so
# Zx <= 3 Delta W.  Likewise every y=1 S increment costs at least 1/3
# of its mass in W, and the stronger combined inequality holds locally:
# S+Zx <= 3 Delta W.
assert S+Zx <= 3*(Fraction(13,3)+Fraction(9,2)*zeta)

print('RL50 monotone J-lift / defect-energy verifier: PASS')
print('W=gJ/3^d is nondecreasing on all four edge types')
print('Delta W total = 13/3 + (9/2) zeta (independent of denominator length)')
print('local energy eps=3 Delta W - Delta S - Delta Zx is nonnegative')
print('eps=0 exactly for 10 at any height and 00/11 at height one')
print('GLOBAL IDENTITY: sum eps = 2E exactly')
print('candidate-use interface: E<5/3 => total defect energy <10/3')
print('live-floor interface: E<3/2 => total defect energy <3')
print('audited witness regression: H=',H,'E=',E,'energy=',energy)

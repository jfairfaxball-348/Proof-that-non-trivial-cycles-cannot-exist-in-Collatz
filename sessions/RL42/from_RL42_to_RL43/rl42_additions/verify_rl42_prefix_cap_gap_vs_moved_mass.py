#!/usr/bin/env python3
from fractions import Fraction

# Retained RL21 g=2 proper-factor countermodel.
a=65; ell=41
u='11011011010110110110101101110011011100110110110101110101011011100'
v='11111111110111000111110011011011110101010111110011101000011100000'
assert len(u)==len(v)==a and u.count('1')==v.count('1')==ell

def Qword(w):
    p=0; q=0
    for i,b in enumerate(w):
        if b=='1':
            q += (1<<i)*3**(ell-1-p)
            p += 1
    return q

iu=[i for i,b in enumerate(u) if b=='1']
iv=[i for i,b in enumerate(v) if b=='1']
Pplus=sum(i>j for i,j in zip(iu,iv))
Pminus=sum(i<j for i,j in zip(iu,iv))
P=Pplus+Pminus
rho=sum(abs(i-j) for i,j in zip(iu,iv))
X=1<<a; Y=3**ell
G=(Qword(u)-Qword(v))//(X+Y)
assert Qword(u)-Qword(v)==(X+Y)*G
assert G==4
assert Pplus==39 and Pminus==0 and P==39
assert rho==170
# Uniform analytic consequence P_+ > (45/8)G is satisfied strictly.
assert Fraction(Pplus,1) > Fraction(45,8)*G
# Exact stronger z-dependent inequality from R42G.4.
z=Fraction(X,Y)
assert Fraction(Pplus,1) > 3*(z+1)*G/(z*z)
# Gap-vs-P consequence.
assert Fraction(G,1) < Fraction(8,45)*Pplus

print('RL42 prefix-cap gap-vs-moved-mass verifier: PASS')
print('RL21 countermodel: G =',G,'P+ =',Pplus,'P- =',Pminus,'rho =',rho)
print('certified sanity: P+ > (45/8)G and exact z-dependent bound')

# Exact low-resonance thresholds from R42G.12.
for aa,ll in ((46,29),(65,41)):
    zz=Fraction(1<<aa,3**ll)
    threshold=12*(zz+1)/(zz*zz)
    assert threshold>23 and threshold<24
print('resonance sanity: (46,29) and (65,41) both force P+ >= 24 when G=4')

# Uniform gap-area consequences from rho > (45/8)G.
assert Fraction(45,1) <= Fraction(45,8)*8   # rho<=45 cannot permit G=8 because inequality is strict
assert Fraction(67,1) <= Fraction(45,8)*12 # rho<=67 cannot permit G=12
print('uniform consequence: rho<=45 => G=4; rho<=67 => G in {4,8}')

#!/usr/bin/env python3
from fractions import Fraction

A,ELL=65,41
X=1<<A; Y=3**ELL
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()

def cap_ok(n,pa):
    return (1<<(n+2))*Y*Y <= (3**(pa+2))*X*X

def phi(d,T,n,pa):
    return Fraction((1<<n)*(T+3**d-1),3**(pa+d))

d,T,z,pa,n,H=1,-14,1,0,1,0
P0=phi(d,T,n,pa)
assert P0 == -8
assert cap_ok(n,pa)
neutral_num=3*(-2)+3-1
assert neutral_num//2 == -2 and neutral_num%2==0

for edge in EDGES:
    x,y=map(int,edge)
    assert cap_ok(n,pa), (n,pa,'terminal-dead prefix in certified witness')
    oldphi=phi(d,T,n,pa)
    s=Fraction(1<<n,3**pa)
    expected=s*((1-x)-Fraction(1-y,3**d))
    num=(3**y)*T + x*3**(d+y-1)-y
    assert num%2==0
    H2=H+d-1
    d2=d+y-x
    T2=num//2
    z2=z+1-x
    pa2=pa+x
    n2=n+1
    newphi=phi(d2,T2,n2,pa2)
    assert newphi-oldphi == expected, (edge,d,T,n,pa,newphi-oldphi,expected)
    if edge=='11':
        assert newphi==oldphi
    d,T,z,pa,n,H=d2,T2,z2,pa2,n2,H2

assert (d,T,z,pa,n,H)==(1,31,22,38,60,104)
assert cap_ok(n,pa)
t=2
zeta=Fraction(1<<A,3**ELL)
terminal=9*zeta*(1+Fraction(1,2**(t+3)))
assert phi(d,T,n,pa)==terminal
assert T+1==1<<(t+3)
assert z+t==A-ELL
print('RL47 phase-coordinate verifier: PASS')
print('start Phi = -8')
print('terminal state =', (d,T,z,pa,n,H))
print('terminal Phi = 9*zeta*(1+2^-(t+3)) exactly')
print('every 11 edge has Delta Phi = 0 on the certified (65,41) witness')

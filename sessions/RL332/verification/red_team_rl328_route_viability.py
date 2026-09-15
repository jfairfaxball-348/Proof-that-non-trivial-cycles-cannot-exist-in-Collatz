#!/usr/bin/env python3
from fractions import Fraction
ELL=137_528_045_312; T=ELL-60
for n in (1,2,10,1000):
    assert Fraction(49*n,3*n)==Fraction(49,3)
k1=112_933_933_538; k2=64_392_480_586
r1=Fraction((T+1)-k1,k1); r2=Fraction((T+1)-k2,k2)
assert r1<Fraction(218,1000)
assert r2<Fraction(1136,1000)
assert Fraction(49,3)>r2>r1
kg=(3*(T+1)+51)//52
assert kg==7_934_310_304 and kg<k2<k1<T+1
print('RL328_ROUTE_VIABILITY_RED_TEAM_GREEN')
print('critical_repeatable_ratio',float(Fraction(49,3)))
print('required_ratio_current',float(r1))
print('required_ratio_factor2',float(r2))

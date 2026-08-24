#!/usr/bin/env python3
from fractions import Fraction

# Exact endpoint inequality used to force the first 72 ranks to be cap-limited.
assert 3**72 < 5*(2**112)

# C < 2/5 follows exactly from zeta^2 < 16/15:
# (3/8)*(16/15)=2/5.
assert Fraction(3,8)*Fraction(16,15)==Fraction(2,5)

# The target comparison at zeta=1 after k>=5:
# 73*C_min = 73*(3/8) = 219/8,
# target <= 14+(27/2)*(31/32) = 14+837/64.
margin=Fraction(219,8)-14-Fraction(837,64)
assert margin==Fraction(19,64)>0

# Derivative of the comparison polynomial on zeta>=1 is positive:
# d/dz [(219/8)z^2 - 14 - (837/64)z]
# = (219/4)z - 837/64 >= value at z=1 >0.
derivative_at_1=Fraction(219,4)-Fraction(837,64)
assert derivative_at_1>0

# A simple numerical-independent check that q>=44 cannot coexist with ell<=75
# in the retained window.  We avoid logarithms by using
# zeta^2 = 2^(2(ell+q))/3^(2ell) < 16/15.
# For q>=44, the smallest left side at fixed ell occurs at q=44.
# Check ell=1..75 all violate the upper window; hence ell>=76.
for ell in range(1,76):
    assert 15*(1 << (2*(ell+44))) >= 16*(3**(2*ell))

print('RL48 rank-relaxation barrier verifier: PASS')
print('endpoint 3^72 < 5*2^112: PASS')
print('target margin at zeta=1 =',margin)
print('q>=44 plus zeta^2<16/15 forces ell>=76: PASS')
print('conclusion: RL47 separable relaxation cannot exclude z=q-t>=42')

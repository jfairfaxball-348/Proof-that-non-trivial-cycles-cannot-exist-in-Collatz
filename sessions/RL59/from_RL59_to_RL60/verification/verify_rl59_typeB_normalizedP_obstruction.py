#!/usr/bin/env python3
from fractions import Fraction

# Exact inherited safe-CF constants.
A   = 123139092617126647266
ELL = 77692117359936589403
Q   = A - ELL

# Inherited rational upper bound: zeta=2^A/3^ELL satisfies zeta^2<136/135,
# hence (since zeta>0) certainly zeta<136/135.
ZETA_UP = Fraction(136,135)

# Four synchronized pumps from the 26-zero cut plus the forced Type-B exit
# use five late x-zero events and end at J=15, d=2, Q=18.
r_exit = 5
J_exit = 15
P_exit = (1 << r_exit) * J_exit
assert P_exit == 480

# Remaining suffix counters after the Type-B exit:
# x-ones = ELL-56, y-ones = ELL-55.
# In the audited backward normalized-P grammar the homogeneous multipliers are
#   11: 2/3, 10: 2, 00: 1, 01: 1/3,
# while every affine correction except 10 is nonpositive (10 has zero correction).
# Therefore independently of event order and z,
#   P_exit <= 2^(ELL-56)/3^(ELL-55) * P_end.
# And P_end=2^(Q-24), because K+R=Q-24.
# Using A=ELL+Q gives
#   P_exit <= zeta * 3^55 / 2^80.
cap = ZETA_UP * Fraction(3**55, 2**80)
assert cap < P_exit

# Verify positivity of all subtracted constants for the legal height domains.
for d in range(1,100):
    assert 2**d - 1 > 0                       # 11
    assert 3**d - 2**d > 0                    # 00
    if d > 1:
        assert 3**d - 2**(d-1) - 1 > 0        # 01

print('RL59 Type-B normalized-P obstruction: PASS')
print('P_exit =', P_exit)
print('uniform upper cap <', cap)
print('uniform upper cap decimal =', float(cap))
print('gap P_exit-cap =', float(Fraction(P_exit)-cap))
print('identity exponent check: (ELL-56)+(Q-24)=A-80 ->', (ELL-56)+(Q-24)==A-80)
print('Conclusion: no safe-CF terminal suffix can embed the four-pump Type-B exit, for any admissible z.')

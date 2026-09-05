#!/usr/bin/env python3
from fractions import Fraction
assert Fraction(7,19) < Fraction(24,65)
assert 19*Fraction(24,65)-7 == Fraction(1,65)
assert 19*2 == 38 and 7*2 == 14
assert 14+8 == 22
assert 28+1 == 29
assert 29 > 22
for d in (1,2):
    assert Fraction(1,65) < Fraction(1,d)
print("RL253 verifier: PASS")

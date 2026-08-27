#!/usr/bin/env python3
from fractions import Fraction

L = 56
Z = 1
while 2 ** (L + Z) <= 3 ** L:
    Z += 1
D = 2 ** (L + Z) - 3 ** L
N = 2 ** (Z - 1) * (3 ** L - 2 ** L)
ratio = Fraction(N, D)
assert Z == 33 and ratio.numerator // ratio.denominator == 23_506_639_475
assert D > 0 and 2 ** (L + Z - 1) - 3 ** L < 0
assert 2 ** Z * (3 ** L - 2 ** L) * D < 2 ** (Z - 1) * (3 ** L - 2 ** L) * (2 ** (L + Z + 1) - 3 ** L)
print('RL131 L=56 quotient-bound verifier: PASS')
print(f'L={L} positivity_Z={Z} quotient_floor={ratio.numerator // ratio.denominator}')

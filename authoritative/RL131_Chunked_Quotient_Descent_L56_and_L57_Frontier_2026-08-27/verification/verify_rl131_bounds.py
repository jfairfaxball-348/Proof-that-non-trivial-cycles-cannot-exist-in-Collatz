#!/usr/bin/env python3
from fractions import Fraction

rows = []
for L in (56, 57):
    Z = 1
    while 2 ** (L + Z) <= 3 ** L:
        Z += 1
    D = 2 ** (L + Z) - 3 ** L
    N = 2 ** (Z - 1) * (3 ** L - 2 ** L)
    r = Fraction(N, D)
    rows.append((L, Z, r.numerator // r.denominator))
    assert D > 0 and 2 ** (L + Z - 1) - 3 ** L < 0
    assert 2 ** Z * (3 ** L - 2 ** L) * D < 2 ** (Z - 1) * (3 ** L - 2 ** L) * (2 ** (L + Z + 1) - 3 ** L)
assert rows == [(56, 33, 23506639475), (57, 34, 14888509893)]
print('RL131 quotient-bound verifier: PASS')
for L, Z, q in rows: print(f'L={L} positivity_Z={Z} quotient_floor={q}')

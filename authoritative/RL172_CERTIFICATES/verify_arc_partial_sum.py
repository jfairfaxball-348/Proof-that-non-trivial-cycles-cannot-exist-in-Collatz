#!/usr/bin/env python3
"""Exact audit for the inverse-phase arc partial-z-sum identity."""
from fractions import Fraction
from itertools import product


def check(word, start, width):
    length = len(word)
    y = Fraction(1)
    q = Fraction(1)
    z0 = q * y
    partial = Fraction(0)
    B = 0
    C = 0
    prefix = 0
    for t in range(width):
        partial += q / 3
        C += 3 ** (width - 1 - t) * (1 << prefix)
        exponent = word[(start + t) % length]
        B += exponent
        prefix += exponent
        y = (3 * y + 1) / (1 << exponent)
        q = q * (1 << exponent) / 3
    assert (1 << B) * y == 3 ** width + C
    assert q * y - z0 == partial
    assert Fraction(C, 3 ** width) == partial


checks = 0
for length in range(1, 6):
    for word in product(range(1, 5), repeat=length):
        for start in range(length):
            for width in range(1, length + 1):
                check(word, start, width)
                checks += 1

assert checks > 0
print('RL172 arc partial-sum verifier: PASS')
print(f'ordinary cyclic arc cases checked: {checks}')

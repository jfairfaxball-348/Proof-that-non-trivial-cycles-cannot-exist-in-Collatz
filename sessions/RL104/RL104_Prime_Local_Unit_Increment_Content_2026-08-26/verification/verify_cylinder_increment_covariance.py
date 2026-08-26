#!/usr/bin/env python3
"""Exact finite audit of inverse-word cylinder covariance for T_s cycles."""

from itertools import product
from math import gcd


def numerator(word):
    total, later = 0, sum(word)
    for i, bit in enumerate(word):
        if bit:
            later -= 1
            total += (1 << i) * 3**later
    return total


def is_primitive(word):
    return all(len(word) % d or tuple(word) != tuple(word[:d]) * (len(word) // d)
               for d in range(1, len(word)))


checks = 0
for length in range(2, 14):
    for word in product((0, 1), repeat=length):
        weight = sum(word)
        if weight in (0, length) or not is_primitive(word):
            continue
        d = 2**length - 3**weight
        if d <= 0:
            continue
        q = numerator(word)
        common = gcd(d, q)
        increment, root = d // common, q // common
        states = [root]
        for bit in word:
            states.append(states[-1] // 2 if bit == 0
                          else (3 * states[-1] + increment) // 2)
        assert states[-1] == root
        start = max(range(length), key=lambda i: states[i])
        m = states[start]
        assert m % 2 == 0
        # Read the predecessor parities backwards from the actual maximum.
        backward = [word[(start - i) % length] for i in range(1, length + 1)]
        n, odd = 0, 0
        for depth, bit in enumerate(backward, 1):
            if bit == 0:
                n *= 2
            else:
                n = 2 * n + 3**odd
                odd += 1
            modulus = 3**odd
            assert (2**depth * m - increment * n) % modulus == 0
            # The unique even lift c modulo 2*3^odd is the s=1 cylinder
            # residue; the actual T_s maximum is s*c modulo that modulus.
            residue = (pow(2**depth, -1, modulus) * n) % modulus
            c = residue if residue % 2 == 0 else residue + modulus
            assert m % (2 * modulus) == (increment * c) % (2 * modulus)
            checks += 1

print("RL103 inverse-cylinder increment covariance: PASS")
print("primitive generalized-cycle prefix checks =", checks)

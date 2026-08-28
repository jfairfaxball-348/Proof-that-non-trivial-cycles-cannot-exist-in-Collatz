#!/usr/bin/env python3
"""Exact small-word audit for the RL164 overlapping arc-content identity."""
from itertools import product
from math import gcd


def arc_content(a, start, length):
    """Return (total exponent, positive ordinary +1 numerator)."""
    n = len(a)
    total = 0
    content = 0
    for t in range(length):
        # The term for the t-th +1 has the exponents already crossed.
        content += 3 ** (length - 1 - t) * (1 << total)
        total += a[(start + t) % n]
    return total, content


tested = 0
for A, L in ((5, 3), (7, 4), (8, 5), (11, 7), (13, 8)):
    assert L < A < 2 * L and gcd(A, L) == 1
    b = [(A * j) // L for j in range(L + 1)]
    p = pow(A, -1, L)
    for interior in product(range(4), repeat=L - 1):
        h = [0, *interior, 0]
        a = [b[j + 1] - b[j] + h[j] - h[j + 1] for j in range(L)]
        if not all(x >= 1 for x in a):
            continue
        for j in range(L):
            B, C = arc_content(a, j, p)
            Bnext, Cnext = arc_content(a, (j + 1) % L, p)
            assert C & 1 and Cnext & 1
            # Delete the first step and append the next physical step.
            assert B + a[(j + p) % L] == a[j] + Bnext
            assert 3 * C + (1 << B) == 3**p + (1 << a[j]) * Cnext
            # The inverse-cylinder class has one residue modulo 2^B.
            residue = (-C * pow(3, -p, 1 << B)) % (1 << B)
            assert (3**p * residue + C) % (1 << B) == 0
            tested += 1

print('RL164 overlapping arc-content verifier: PASS')
print(f'exact local arcs checked: {tested}')

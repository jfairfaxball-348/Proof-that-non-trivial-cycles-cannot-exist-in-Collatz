#!/usr/bin/env python3
"""Finite arithmetic audit for the RL104 denominator/cylinder CRT barrier."""

from math import gcd


checks = 0
for a in range(2, 41):
    for ell in range(1, a):
        d = 2**a - 3**ell
        if d <= 0:
            continue
        for o in range(1, ell + 1):
            cylinder = 2 * 3**o
            assert gcd(d, cylinder) == 1
            # The CRT construction explicitly realizes every pair of residue
            # classes; no direct D-versus-cylinder compatibility remains.
            inv = pow(d, -1, cylinder)
            for c in range(0, min(cylinder, 24), 2):
                for r in range(min(d, 19)):
                    k = ((c - r) * inv) % cylinder
                    m = r + d * k
                    assert m % d == r and m % cylinder == c
                    checks += 1

print("RL104 denominator/cylinder CRT audit: PASS")
print("exact CRT residue-pair checks =", checks)

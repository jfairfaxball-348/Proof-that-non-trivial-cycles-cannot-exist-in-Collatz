#!/usr/bin/env python3
"""Exact audit of the count inequality behind the RL106 low-population note."""

from fractions import Fraction


checks = 0
for p in range(2, 30):
    for q in range(1, p):
        rho = Fraction(2**p, 3**q)
        if rho <= 1:
            continue
        for g in range(2, 12):
            if rho**g >= 2:
                continue
            for h in range(1, g):
                # d_h >= 1 gives x_(hp)/M < rho^h/3.
                assert rho**h / 3 < Fraction(2, 3)
                checks += 1

assert checks > 100
print("RL106 internal low-population verifier: PASS")
print("exact (p,q,g,h) count inequalities =", checks)

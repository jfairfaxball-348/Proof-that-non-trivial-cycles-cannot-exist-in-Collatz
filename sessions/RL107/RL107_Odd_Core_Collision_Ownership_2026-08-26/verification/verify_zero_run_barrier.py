#!/usr/bin/env python3
"""Exact audit for the RL106 aligned all-even-run exclusion."""

from fractions import Fraction

C = 400_000_000_000
q = 72_057_431_991

# (3/4)^5 < 1/4, so at q >= 100 the common right-hand factor is < 1.
assert 3**5 < 2**8
assert q >= 100
assert C // 2 < 2**38
assert Fraction(C, 2) * Fraction(3, 4) ** 100 < 1

checks = 0
for g in range(2, 301):
    r = (g + 1) // 2
    base = Fraction(3, 2) ** g / 3**r
    assert base <= Fraction(3, 4)
    # The combined lower/upper bounds would require this to exceed 2^70.
    # Since q >= 100 and 0 < base < 1, this is an exact upper bound for
    # the right side of (106.6), without materializing an enormous power.
    rhs_upper = Fraction(C, g) * base**100
    assert rhs_upper < 1
    assert rhs_upper < 2**70
    checks += 1

print("RL106 aligned all-even-run verifier: PASS")
print("exact multiplicity thresholds checked =", checks)

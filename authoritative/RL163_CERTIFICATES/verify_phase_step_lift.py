#!/usr/bin/env python3
"""Exact audit for the RL163 inverse-phase physical-arc identity.

The exhaustive small cases are a guard against indexing/wrap errors.  The
large first-survivor constants are checked with integer arithmetic only.
"""
from itertools import product
from math import gcd


def audit(A, L, exhaustive=False, large_constant_check=False):
    assert L < A < 2 * L and gcd(A, L) == 1
    p = pow(A, -1, L)
    u = (A * p - 1) // L
    assert A * p == u * L + 1
    assert 0 < p < L
    assert (L - p) * A % L == L - 1

    if large_constant_check:
        # Do not scan the 137-billion-point period.  At h=0 the arc total is
        # the difference of two lifted floor values, so a few exact boundary
        # samples certify the carry placement while the proof handles all j.
        for j in (0, 1, L - p - 1, L - p, L - 1):
            sigma = (j + p) % L
            B = (A * (j + p)) // L - (A * j) // L
            carry = int((A * j) % L == L - 1)
            assert B == u + carry
            assert carry == int(j == L - p)
            assert sigma == (j + p) % L
        return p, u, 0
    b = [(A * j) // L for j in range(L + 1)]
    residues = [(A * j) % L for j in range(L)]
    starts = range(L)
    height_words = product(range(4), repeat=L - 1) if exhaustive else [()]
    tested = 0
    for interior in height_words:
        h = [0, *interior, 0] if exhaustive else [0] * (L + 1)
        a = [b[j + 1] - b[j] + h[j] - h[j + 1] for j in range(L)]
        if not all(x >= 1 for x in a):
            continue
        assert sum(a) == A
        for j in starts:
            sigma = (j + p) % L
            B = sum(a[(j + t) % L] for t in range(p))
            carry = int(residues[j] == L - 1)
            assert B == u + carry + h[j] - h[sigma]
            assert carry == int(j == L - p)
        tested += 1
    return p, u, tested


# Exhaust all bounded endpoint-zero defect paths for several small coprime
# slopes.  Positivity is imposed before the arc formula is checked.
small_cases = [(5, 3), (7, 4), (8, 5), (11, 7), (13, 8)]
small_total = 0
for A, L in small_cases:
    _, _, count = audit(A, L, exhaustive=True)
    assert count > 0
    small_total += count

# The current reduced first survivor.  Its size prevents word enumeration;
# the same identity is checked on the mechanical (h=0) specialization and
# the constants/carry location are checked exactly.
A = 217_976_794_617
L = 137_528_045_312
p, u, _ = audit(A, L, large_constant_check=True)
assert p == 65_470_613_321
assert u == 103_768_467_013
assert L - p == 72_057_431_991

print('RL163 inverse-phase physical-arc verifier: PASS')
print(f'exhaustive bounded-defect small-word cases checked: {small_total}')
print(f'first survivor: p={p}, u={u}, exceptional start={L-p}')

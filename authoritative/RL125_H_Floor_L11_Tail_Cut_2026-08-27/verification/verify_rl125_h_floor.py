#!/usr/bin/env python3
"""Exact finite arithmetic checks for the RL125 L=11 tail cut."""

L = 11


def side_floor(n, t, base, zero_side=False):
    best = 0
    for k in range(1, n + 1):
        c = max(n - t * (k - 1), 0)
        if not c:
            break
        best = max(best, (c - 1) * base**k + (1 if zero_side else 0))
    return best


def h_floor(z):
    return min(
        max(side_floor(L, t, 3), side_floor(z, t, 2, True), 6 * (t - 1))
        for t in range(1, min(L, z) + 1)
    )


assert h_floor(34) == 89
assert all(h_floor(z + 1) >= h_floor(z) for z in range(L, 80))

# 86D-B = 1029*2^Z - 15,059,543, positive from Z=14 onward.
for z in range(14, 80):
    D = 2 ** (L + z) - 3**L
    B = (2**z - 1) * (3**L - 2**L)
    assert 86 * D - B == 1029 * 2**z - 15_059_543
    assert 86 * D - B > 0

print('RL125 H-floor tail verifier: PASS')
print('H(11,34) =', h_floor(34))
print('for Z >= 34, H(11,Z) >= 89 and B/D < 86')

#!/usr/bin/env python3
"""Exact audit for the RL165 shallow-population phase-pair countergrammar."""
from math import gcd

A = 217_976_794_617
L = 137_528_045_312
N4 = 3_399_794_205  # RL134 conditional shallow-population lower bound
assert gcd(A, L) == 1 and L < A < 2 * L
p = pow(A, -1, L)
assert p == 65_470_613_321
assert A > 3 * L // 2


def c(j):
    return A * (j + 1) // L - A * j // L


# Start with h=0, then use five permitted c=2 rises to reach height 5.
rises = []
j = N4
while len(rises) < 5:
    assert c(j) in (1, 2)
    if c(j) == 2:
        rises.append(j)
    j += 1
assert len(rises) == 5
assert rises[-1] + 1 < min(p, L - p)


def h(j):
    if j == L:
        return 0
    return sum(r < j for r in rises)


# h<=4 exactly on the initial physical interval 0..rises[-1].
R = rises[-1] + 1
assert h(0) == 0 and h(rises[-1]) == 4
assert h(R) == 5
assert R >= N4 and R < min(p, L - p)

# Positivity can be checked symbolically: only rise positions and the final
# return have nonzero h differences.  Also sample all exceptional points.
exceptional = set(rises) | {L - 1}
for j in exceptional:
    a = c(j) + h(j) - h(j + 1)
    assert a >= 1
for j in rises:
    assert c(j) == 2 and h(j + 1) == h(j) + 1
assert h(L - 1) == 5 and h(L) == 0

# The phase successor is physical shift p.  Its translate of [0,R) is
# disjoint because both circular gaps p and L-p exceed R.
assert R <= p and R <= L - p

print('RL165 shallow-population phase-pair nonforcing verifier: PASS')
print(f'rise positions: {rises}')
print(f'shallow physical interval size: {R}')
print(f'phase gaps: p={p}, L-p={L-p}')

#!/usr/bin/env python3
"""Exact audit for RL166's product-mass-compatible phase-pair grammar."""
from math import gcd

A = 217_976_794_617
L = 137_528_045_312
R0 = 1 << 71
R = 30_000_000_000
assert gcd(A, L) == 1 and L < A < 2 * L
p = pow(A, -1, L)
assert p == 65_470_613_321 and R < min(p, L - p)

# RL134 certifies 5*theta<1, with theta=L*Delta/log(2).  Since log(2)<1,
# Delta<1/(5L).  The shallow h=0 prefix alone has q_j=rho_j>1/2.
assert 5 * L * R > 6 * R0


def c(j):
    return A * (j + 1) // L - A * j // L


rises = []
j = R
while len(rises) < 5:
    if c(j) == 2:
        rises.append(j)
    j += 1
assert len(rises) == 5 and rises[-1] + 1 < min(p, L - p)


def h(j):
    if j == L:
        return 0
    return sum(r < j for r in rises)

for j in set(rises) | {L - 1}:
    assert c(j) + h(j) - h(j + 1) >= 1
assert h(0) == 0 and h(rises[-1]) == 4 and h(rises[-1] + 1) == 5

# The shallow interval has size rises[-1]+1 >= R and is disjoint from its
# phase-successor translate because both circular gaps exceed its size.
S_size = rises[-1] + 1
assert S_size >= R and S_size < min(p, L - p)

print('RL166 product-mass phase-pair nonforcing verifier: PASS')
print(f'rise positions: {rises}')
print(f'shallow interval size: {S_size}')
print('formal shallow mass > R/2 > 3*2^71*Delta (using Delta < 1/(5L))')

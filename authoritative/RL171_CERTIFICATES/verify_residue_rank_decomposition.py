#!/usr/bin/env python3
"""Exact finite audit for RL171's residue-coordinate rank decomposition."""
from itertools import product
from math import gcd


def check(A, L, heights):
    assert gcd(A, L) == 1
    p = pow(A, -1, L)
    # heights are supplied in chronological j order.
    exponents = []
    for i in range(L):
        next_height = heights[i + 1] if i + 1 < L else 0
        exponents.append(A * (i + 1) // L - A * i // L + heights[i] - next_height)
    prefixes = [0]
    for exponent in exponents:
        prefixes.append(prefixes[-1] + exponent)
    E = [A * j - L * prefixes[j] for j in range(L)]
    # The direct E expression must match the height form.
    for j in range(L):
        assert E[j] == (A * j) % L + L * heights[j]
    assert len(set(E)) == L
    for r in range(L):
        j = (p * r) % L
        H = heights[j]
        rank = sum(e < E[j] for e in E)
        expected = sum(x < H for x in heights) + sum(heights[(p * s) % L] == H for s in range(r))
        assert rank == expected
        sigma = (j + p) % L
        carry = int(r == L - 1)
        assert E[sigma] - E[j] == 1 - L * carry + L * (heights[sigma] - heights[j])


cases = 0
for L in range(2, 8):
    for A in range(L + 1, 2 * L + 1):
        if gcd(A, L) != 1:
            continue
        c = [A * (j + 1) // L - A * j // L for j in range(L)]
        for heights_mid in product(range(4), repeat=L - 1):
            h = (0,) + heights_mid
            # endpoint closure is h_L=h_0=0; retain positive exponents.
            a = [c[j] + h[j] - (h[(j + 1) % L] if j + 1 < L else 0) for j in range(L)]
            if min(a) < 1 or sum(a) != A:
                continue
            check(A, L, h)
            cases += 1

assert cases > 0
print('RL171 residue-rank decomposition verifier: PASS')
print(f'bounded positive-defect paths checked: {cases}')

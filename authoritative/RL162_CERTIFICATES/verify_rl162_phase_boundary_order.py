#!/usr/bin/env python3
"""Exact audit for the RL162 phase-boundary order-separation family."""
from math import gcd

for n in range(2, 65):
    A, L = 4 * n, 2 * n + 1
    assert gcd(A, L) == 1
    D = (1 << A) - 3**L
    assert D > 0
    p, u = n, 2 * n - 1
    assert A * p - u * L == 1
    rho = (pow(2, u, D) * pow(pow(3, p, D), -1, D)) % D
    assert (2 * pow(rho, L, D) - 1) % D == 0
    assert (3 * pow(rho, A - L, D) - 2) % D == 0
    assert gcd(rho - 1, D) == 1
    b = [(A * j) // L for j in range(L + 1)]
    h = [0] * (L + 1)
    for j in range(2, n + 2):
        h[j] = 1
    a = [b[j + 1] - b[j] + h[j] - h[j + 1] for j in range(L)]
    assert all(x >= 1 for x in a)
    assert sum(a) == A and h[0] == h[L] == 0
    residues = [(A * j) % L for j in range(L)]
    E = {residues[j] for j in range(L) if h[j] == 1}
    assert len(E) == n
    physical = sum(h[j] != h[(j - 1) % L] for j in range(L))
    phase = sum((r in E) != ((r - 1) % L in E) for r in range(L))
    assert physical == 2 and phase == 2 * n
    P = (sum(2 * pow(rho, r, D) for r in range(L)) - sum(pow(rho, r, D) for r in E)) % D
    S = sum(pow(rho, r, D) for r in E) % D
    B = (1 + (rho - 1) * S) % D
    assert B == (-(rho - 1) * P) % D

print('RL162 phase-boundary order-separation verifier: PASS')
print('family checked: n = 2..64')
print('physical boundary count = 2; phase-residue boundary count = 2n')

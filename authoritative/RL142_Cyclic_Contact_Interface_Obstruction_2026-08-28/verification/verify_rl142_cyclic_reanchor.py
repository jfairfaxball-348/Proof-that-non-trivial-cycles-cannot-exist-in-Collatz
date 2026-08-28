#!/usr/bin/env python3
"""Exact checks for RL142 block-boundary re-anchoring."""

from itertools import product


def numerator(exponents):
    prefix = [0]
    for a in exponents:
        prefix.append(prefix[-1] + a)
    n = len(exponents)
    return sum(3**(n - 1 - j) * 2**prefix[j] for j in range(n))


def check(A, L, g, h, cut_block):
    n = g*L
    b = [(A*j)//L for j in range(n + 1)]
    c = [b[j + 1] - b[j] for j in range(n)]
    a = [c[j] + h[j] - h[j + 1] for j in range(n)]
    if min(a) < 1:
        return
    cut = cut_block*L
    height = h[cut]
    extended = h[:-1] + h[:-1] + [h[0]]
    hp = [extended[cut + j] - height for j in range(n + 1)]
    ap = [c[j] + hp[j] - hp[j + 1] for j in range(n)]
    assert ap == a[cut:] + a[:cut]
    D = 2**(g*A) - 3**(g*L)
    assert (numerator(a) % D == 0) == (numerator(ap) % D == 0)
    B = [3**(n - 1 - j) * 2**b[j] for j in range(n)]
    qc, q = sum(B), numerator(ap)
    if set(hp).issubset({0, 1}):
        assert 2*q == qc + sum(B[j] for j in range(n) if hp[j] == 0)
    if set(hp).issubset({-1, 0}):
        assert q == qc + sum(B[j] for j in range(n) if hp[j] == -1)


for A, L in ((3, 2), (5, 3)):
    for g in (2, 3):
        n = g*L
        for middle in product((0, 1), repeat=n - 1):
            h = [0, *middle, 0]
            for cut_block in range(g):
                check(A, L, g, h, cut_block)

print('RL142 cyclic re-anchor identities: PASS')

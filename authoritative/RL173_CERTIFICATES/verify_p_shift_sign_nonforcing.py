#!/usr/bin/env python3
"""Exact audit for RL173 p-shift weighted-flow sign nonforcing."""
from fractions import Fraction
from math import gcd


def flow(word):
    L = len(word)
    A = sum(word)
    assert gcd(A, L) == 1 and (1 << A) > 3 ** L
    S = [0]
    for x in word:
        S.append(S[-1] + x)
    h = [A * j // L - S[j] for j in range(L)]
    assert min(h) >= 0 and h[0] == 0 and S[-1] == A
    p = pow(A, -1, L)
    q = [Fraction(1 << S[j], 3 ** j) for j in range(L)]
    G = []
    for i in range(L):
        shifted = S[(i + p) % L] + (A if i + p >= L else 0)
        G.append(shifted - S[p] - S[i])
    def power(g):
        return Fraction(1, 3 ** g) if g >= 0 else Fraction(3 ** (-g), 1)
    F = sum(q[i] * (power(G[i]) - 1) for i in range(L))
    return A, L, h, p, F

neg = flow((1, 4))
pos = flow((1, 4, 3))
assert neg == (5, 2, [0, 1], 1, Fraction(-52, 81))
assert pos == (8, 3, [0, 1, 0], 2, Fraction(176, 27))
assert neg[-1] < 0 < pos[-1]
print('RL173 p-shift sign nonforcing verifier: PASS')
print(f'negative local witness: {neg}')
print(f'positive local witness: {pos}')

#!/usr/bin/env python3
"""Exact finite algebra checks for the RL140 one-deviant-block theorem."""

from itertools import product


def numerator(exponents):
    prefix = [0]
    for exponent in exponents:
        prefix.append(prefix[-1] + exponent)
    n = len(exponents)
    return sum(3**(n - 1 - j) * 2**prefix[j] for j in range(n))


def check_height_one_identity(A, L, g, h):
    n = g * L
    b = [(A*j)//L for j in range(n + 1)]
    c = [b[j + 1] - b[j] for j in range(n)]
    a = [c[j] + h[j] - h[j + 1] for j in range(n)]
    if min(a) < 1:
        return
    B = [3**(n - 1 - j) * 2**b[j] for j in range(n)]
    qh = numerator(a)
    qc = sum(B)
    r0 = sum(B[j] for j in range(n) if h[j] == 0)
    assert 2*qh == qc + r0


def contact_data(A, L, g, blocks):
    X, Y = 2**A, 3**L
    W = [3**(L - 1 - r) * 2**((A*r)//L) for r in range(L)]
    scale = [X**t * Y**(g - 1 - t) for t in range(g)]
    weights = [sum(W[r] for r in block) for block in blocks]
    R = sum(scale[t] * weights[t] for t in range(g))
    F = sum(scale)
    return X, Y, W, weights, R, F


def check_one_deviant_block(A, L, g):
    X, Y = 2**A, 3**L
    assert X > Y
    assert all(2**((A*r)//L) < 3**r for r in range(1, L))
    W0 = [3**(L - 1 - r) * 2**((A*r)//L) for r in range(L)]
    Q0 = sum(W0)
    assert all(w < X//3 + (1 if X % 3 else 0) for w in W0)
    assert Q0 < X**2
    subsets = [set(r for r in range(L) if mask >> r & 1)
               for mask in range(1 << L)]
    for common in subsets:
        common_weight = sum(W0[r] for r in common)
        for deviant in subsets:
            for exceptional_block in range(g):
                blocks = [set(common) for _ in range(g)]
                blocks[exceptional_block] = set(deviant)
                _, _, _, weights, R, F = contact_data(A, L, g, blocks)
                delta = weights[exceptional_block] - common_weight
                scale = X**exceptional_block * Y**(g - 1 - exceptional_block)
                assert R - common_weight*F == scale*delta
                assert (R % F == 0) == (delta % F == 0)
                if deviant != common:
                    assert delta != 0
                if g >= 3 and R % F == 0:
                    assert deviant == common
                if g == 2 and len(common ^ deviant) <= 3 and R % F == 0:
                    assert deviant == common


for A, L in ((3, 2), (5, 3)):
    for g in (1, 2, 3):
        n = g*L
        for middle in product((0, 1), repeat=n - 1):
            check_height_one_identity(A, L, g, [0, *middle, 0])

for A, L in ((5, 3), (8, 5)):
    check_one_deviant_block(A, L, 2)
    check_one_deviant_block(A, L, 3)

print('RL140 one-deviant-block obstruction: PASS')

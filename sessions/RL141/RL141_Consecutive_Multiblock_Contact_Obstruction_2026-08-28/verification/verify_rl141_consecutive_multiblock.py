#!/usr/bin/env python3
"""Exact checks for the RL141 consecutive multiblock factor reduction."""


def contact_data(A, L, g, blocks):
    X, Y = 2**A, 3**L
    W = [3**(L - 1 - r) * 2**((A*r)//L) for r in range(L)]
    scales = [X**t * Y**(g - 1 - t) for t in range(g)]
    weights = [sum(W[r] for r in block) for block in blocks]
    R = sum(scales[t] * weights[t] for t in range(g))
    return X, Y, W, weights, R, sum(scales)


def check(A, L, g, ell):
    X = 2**A
    assert 2**A > 3**L and ell < X and g >= ell + 3
    assert all(2**((A*r)//L) < 3**r for r in range(1, L))
    W = [3**(L - 1 - r) * 2**((A*r)//L) for r in range(L)]
    Q0 = sum(W)
    assert Q0 < X**2
    subsets = [set(r for r in range(L) if mask >> r & 1)
               for mask in range(1 << L)]
    for common in subsets:
        common_weight = sum(W[r] for r in common)
        def visit(prefix):
            if len(prefix) == ell:
                for start in range(g - ell + 1):
                    blocks = [set(common) for _ in range(g)]
                    blocks[start:start + ell] = prefix
                    _, Y, _, weights, R, F = contact_data(A, L, g, blocks)
                    deltas = [weights[start + i] - common_weight
                              for i in range(ell)]
                    E = sum(X**i * Y**(ell - 1 - i) * deltas[i]
                            for i in range(ell))
                    scale = X**start * Y**(g - start - ell)
                    assert R - common_weight*F == scale*E
                    assert (R % F == 0) == (E % F == 0)
                    if any(deltas):
                        assert E != 0
                        assert abs(E) < F
                        assert R % F != 0
                return
            for subset in subsets:
                visit(prefix + [subset])
        visit([])


for A, L, g, ell in ((5, 3, 4, 1), (5, 3, 5, 2), (8, 5, 4, 1)):
    check(A, L, g, ell)

print('RL141 consecutive multiblock obstruction: PASS')

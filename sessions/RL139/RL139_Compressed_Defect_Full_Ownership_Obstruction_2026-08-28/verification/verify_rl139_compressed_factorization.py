#!/usr/bin/env python3
"""Finite exact checks of the RL139 affine-numerator factorization."""

def numerator(exponents):
    n = len(exponents)
    sums = [0]
    for a in exponents:
        sums.append(sums[-1] + a)
    return sum(3**(n-1-j)*2**sums[j] for j in range(n))


for A, L in ((3, 2), (5, 3), (8, 5)):
    assert L < A < 2*L
    c0 = [(A*(j+1))//L - (A*j)//L for j in range(L)]
    assert sum(c0) == A
    q0 = numerator(c0)
    d0 = 2**A - 3**L
    for g in range(1, 6):
        c = c0*g
        n = g*L
        h = [0, 0] + [1]*(n-2) + [0]
        a = [c[j] + h[j] - h[j+1] for j in range(n)]
        assert all(x >= 1 for x in a)
        assert sum(a) == g*A
        qc = numerator(c)
        qa = numerator(a)
        f = sum(2**((g-1-t)*A)*3**(t*L) for t in range(g))
        assert qc == q0*f
        assert 2**(g*A)-3**(g*L) == d0*f
        assert 2*qa == qc + 5*3**(n-2)
        if g > 1:
            assert f > 5 and f % 3 != 0
            assert (2*qa) % f == (5*3**(n-2)) % f

print('RL139 compressed numerator factorization: PASS')

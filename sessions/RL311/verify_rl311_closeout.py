#!/usr/bin/env python3
"""RL311 closeout sanity/regression verifier.

This script does not prove existence/nonexistence of Collatz cycles. It checks the
finite/algebraic bookkeeping used in the RL311 closeout: Bellman path replays,
D0 zero-ray merge, boundary-credit identities, U-step identity, rounding logic,
and balanced-level pigeonhole bounds.
"""
from fractions import Fraction
import math

# Bellman K-coordinate transition and area cost.
def step(state, bit):
    d, K = state
    cost = d - 1
    if K % 2 == 0:
        if bit == 1:
            return (d, 3*K//2), cost
        return (d, (K + 3**d - 1)//2), cost
    else:
        if bit == 1:
            assert d > 1
            return (d-1, (K-1)//2), cost
        return (d+1, 3*(K + 3**d)//2), cost

def replay(state, word):
    c = 0
    for ch in word:
        state, dc = step(state, int(ch))
        c += dc
    return state, c

# J->K conversion: K=J+2^d-1.
def JK(d, J):
    return (d, J + 2**d - 1)

# Exact Gate-A replays.
assert replay(JK(2, -84), "101011101100000") == (JK(4, 21), 8)
assert replay(JK(2, -84), "101001000") == (JK(5, 104), 11)
assert replay(JK(1, 8), "0000100") == (JK(5, 252), 14)

# Y all-zero ray and area.
Y = JK(6, 504)
st, cost = replay(Y, "0"*62)
assert st == (41, 3**41 - 3)
assert cost == 1528
# D0 V_3 -> V_41 via 76 zeros (00 raises d by one).
D0 = JK(3, 17)
st2, cost2 = replay(D0, "0"*76)
assert st2 == st
assert cost2 == 1558
assert cost2 - cost == 30

# Boundary-credit saturation identities.
for d in range(3, 101):
    CA = d*d - 2*d - 1
    CF = d*d - d - 2
    assert (2*d-5) + (d-2)**2 == CA
    assert (2*d-4) + (d-2)*(d-1) == CF

# U-step identity, checked symbolically on integer sample states.
# even: x' = x/2, q'=2q; odd: x'=(3x+1)/2, q'=2q/3.
for x in range(2, 100, 2):
    q = Fraction(7, 11)
    lhs = 2*q*(4*Fraction(x,2)+1)
    rhs = q*(4*x+1)+q
    assert lhs == rhs
for x in range(1, 100, 2):
    q = Fraction(7, 11)
    lhs = Fraction(2,3)*q*(4*Fraction(3*x+1,2)+1)
    rhs = q*(4*x+1)+q
    assert lhs == rhs

# Correct rounding consequence: integer E < mu+1 implies E <= ceil(mu),
# not generally <= floor(mu).
mu = Fraction(23, 10)
assert 3 < mu + 1
assert 3 <= math.ceil(float(mu))
assert not (3 <= math.floor(float(mu)))

# Pigeonhole: values in {0,...,h}; among h+2 consecutive positions,
# a repeated value occurs with gap <= h+1.
from itertools import product
for h in range(0, 5):
    n = h + 2
    vals = range(h+1)
    for seq in product(vals, repeat=n):
        best = None
        for i in range(n):
            for j in range(i+1, n):
                if seq[i] == seq[j]:
                    gap = j-i
                    best = gap if best is None else min(best, gap)
        assert best is not None and best <= h+1

# Determinant divisibility by global gcd is algebraic.
for g in range(1, 20):
    for a in range(2, 8):
        for ell in range(1, a):
            A, L = g*a, g*ell
            for d in range(1, A):
                for o in range(1, L+1):
                    k = A*o-d*L
                    assert k % g == 0

print("RL311 closeout sanity/regression verifier: PASS")

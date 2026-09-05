#!/usr/bin/env python3
"""Portable arithmetic verifier for RL252 closeout."""
from math import gcd

A, ELL, Z, Q, R = 783, 494, 289, 317, 200
D_Q = Q - R - 1

assert A - ELL == Z
assert A * R - Q * ELL == 2
assert D_Q == 116
assert A == 2 * Q + 149
assert gcd(A, Q) == 1

for t in range(46, 57):
    s0 = A - t
    s5 = (s0 + 5 * (Q + 8)) % A
    l5 = t - 45
    e5 = s5 + l5 - 1
    assert s5 == 59 - t
    assert e5 == 13
    assert l5 >= 1
    lower = 2 * D_Q + t + 1 + l5
    assert lower == 2 * t + 188
    assert (lower > Z) == (t >= 51)

for t in range(51, 57):
    for j in range(5):
        assert t - 9*j >= 10
    assert 3 <= 59 - t <= 8
    assert t + 14 <= 149

assert 2 * 50 + 188 == 288
assert 2 * 51 + 188 == 290
assert 50 + 3 == 53
assert 291 - 53 == 238

print("RL252 verifier: PASS")
print("frontier=(783,494,289,317,200)")
print("contracted_k_range=31..53")
print("t_max=50")
print("m_min=238")
print("classification=R4_BRIDGE_REDUCED")

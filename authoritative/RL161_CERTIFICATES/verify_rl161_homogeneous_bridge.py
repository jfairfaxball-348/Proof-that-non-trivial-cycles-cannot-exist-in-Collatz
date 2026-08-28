#!/usr/bin/env python3
"""Exact finite audit of the RL161 scaling interfaces."""
from fractions import Fraction
from itertools import product
from math import gcd


def qword(w):
    L = w.count('1'); seen = total = 0
    for i, b in enumerate(w):
        if b == '1':
            seen += 1
            total += (1 << i) * 3 ** (L - seen)
    return total


def rot(w, i):
    return w[i:] + w[:i]


def primitive(w):
    return all(len(w) % d != 0 or w != w[:d] * (len(w) // d) for d in range(1, len(w)))


def step(n, s):
    return n // 2 if n % 2 == 0 else (3 * n + s) // 2


words = scale_checks = 0
for A in range(2, 11):
    for bits in product('01', repeat=A):
        w = ''.join(bits); L = w.count('1')
        if L == 0 or not primitive(w):
            continue
        D = (1 << A) - 3 ** L
        if D <= 0:
            continue
        qs = [qword(rot(w, i)) for i in range(A)]
        g = gcd(D, qs[0]); s = D // g; ns = [q // g for q in qs]
        assert all(n > 0 and gcd(n, s) == 1 for n in ns)
        assert len(set(ns)) == A
        for i, b in enumerate(w):
            assert ns[i] % 2 == int(b)
            assert step(ns[i], s) == ns[(i + 1) % A]
        normalized = [Fraction(n, s) for n in ns]
        assert normalized == [Fraction(q, D) for q in qs]
        raw = sum(abs(ns[i] - ns[j]) for i in range(A) for j in range(i + 1, A))
        norm = Fraction(raw, s)
        for c in (3, 5):
            scaled = [c * n for n in ns]
            assert all(step(scaled[i], c * s) == scaled[(i + 1) % A] for i in range(A))
            assert [Fraction(n, c * s) for n in scaled] == normalized
            scaled_raw = sum(abs(scaled[i] - scaled[j]) for i in range(A) for j in range(i + 1, A))
            assert scaled_raw == c * raw
            assert Fraction(scaled_raw, c * s) == norm
            scale_checks += 1
        words += 1

print('RL161 homogeneous global-bridge verifier: PASS')
print('primitive generalized cycles checked =', words)
print('odd scale-covariance checks =', scale_checks)

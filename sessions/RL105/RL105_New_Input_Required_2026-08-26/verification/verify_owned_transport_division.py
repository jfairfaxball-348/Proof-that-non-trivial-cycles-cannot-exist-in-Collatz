#!/usr/bin/env python3
"""Exact finite audit: owned rotation transport cancels the full D."""
from itertools import product


def q(word):
    total, later = 0, sum(word)
    for i, bit in enumerate(word):
        if bit:
            later -= 1
            total += (1 << i) * 3**later
    return total


checks = 0
for n in range(2, 13):
    for word in product((0, 1), repeat=n):
        if sum(word) in (0, n):
            continue
        d = 2**n - 3**sum(word)
        full = q(word)
        if d <= 0 or full % d:
            continue
        m = full // d
        for cut in range(1, n):
            a, b = word[:cut], word[cut:]
            rotated = q(b + a)
            assert rotated % d == 0
            x = rotated // d
            assert 2**cut * x - 3**sum(a) * m == q(a)
            checks += 1
print("RL104 owned transport division: PASS")
print("owned word/split checks =", checks)

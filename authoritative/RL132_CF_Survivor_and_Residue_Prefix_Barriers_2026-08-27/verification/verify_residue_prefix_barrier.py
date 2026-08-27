#!/usr/bin/env python3
"""Exact diagnostic for fixed-depth halved-Collatz residue descent.

For each odd class modulo 2^k, determine its first k parity steps and the
affine formula T^k(n)=(3^s*n+c)/2^k.  A class is uniformly descending above M
only when 3^s<2^k and (2^k-3^s)*M>c.  This is diagnostic only: uncovered
classes are never interpreted as cycles.
"""
from collections import Counter


def row(k: int, M: int):
    modulus = 1 << k
    covered = 0
    runs = Counter()
    all_ones = None
    for r in range(1, modulus, 2):
        x = r
        s = 0
        for _ in range(k):
            if x & 1:
                x = (3*x + 1) >> 1
                s += 1
            else:
                x >>= 1
        # c is recovered exactly from T^k(r) and its affine coefficient.
        c = modulus*x - 3**s*r
        assert c >= 0
        if 3**s < modulus and (modulus - 3**s)*M > c:
            covered += 1
        else:
            runs[s] += 1
        if r == modulus - 1:
            all_ones = (s, c)
    return covered, runs, all_ones


M = 984_572_842_735  # RL130's first-wall odd ceiling, used only as a diagnostic threshold.
for k in (8, 12, 16, 20):
    covered, uncovered, all_ones = row(k, M)
    total = 1 << (k-1)
    print(f'k={k} total_odd_classes={total} covered={covered} uncovered={total-covered}')
    print(f'uncovered_by_one_count={dict(sorted(uncovered.items()))}')
    print(f'class_-1_mod_2^k: ones={all_ones[0]} c={all_ones[1]}')

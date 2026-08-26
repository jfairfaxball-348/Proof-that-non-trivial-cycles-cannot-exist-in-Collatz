#!/usr/bin/env python3
"""Exact combinatorial audit for the corrected RL107 boundary-core bound."""

checks = 0
for g in range(2, 1001):
    n = g - 1
    max_run = (g + 1) // 2 - 1
    max_class = max_run + 1
    lower = (n + max_class - 1) // max_class

    # Consecutive index intervals realize the pure combinatorial lower bound.
    # This is not asserted to be a physical Collatz cycle realization.
    blocks = [list(range(a, min(a + max_class, n + 1)))
              for a in range(1, n + 1, max_class)]
    assert len(blocks) == lower
    assert all(group[-1] - group[0] <= max_run for group in blocks)

    expected = 1 if g in (2, 3) else 2
    assert lower == expected
    checks += 1

assert checks == 999
print("RL107 odd-core collision geometry verifier: PASS")
print("exact multiplicity class bounds checked =", checks)
print("corrected endpoints: g=2,3 -> 1; g>=4 -> 2")

#!/usr/bin/env python3
"""Exact finite audit for the RL106 roof-chain basin-delay family."""


def t(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


checks = 0
max_delay = 0
for k in range(3, 3001, 2):
    if k % 3:
        continue
    # This is the RL80 LTE comb member B(2,k).
    q = 4 * (2**k + 1) // 9 - 1
    p = (2 ** (k + 1) - 1) // 3
    m = 2**k
    assert q % 8 == 3
    assert 4 * m - 9 * q == 5
    assert t(q) == p and t(p) == m
    x = q
    delay = 0
    while x != 1:
        x = t(x)
        delay += 1
        assert delay <= k + 2
    assert delay == k + 2
    max_delay = max(max_delay, delay)
    checks += 1

assert checks == 500
assert max_delay == 2999
print("RL106 roof-chain basin-delay verifier: PASS")
print("exact LTE roof-chain family checks =", checks)
print("largest checked time to 1 =", max_delay)

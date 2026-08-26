#!/usr/bin/env python3
"""Exact checks for the RL105 roof-chain factor-5 route barrier.

This is a finite sanity audit of the displayed identities.  It does not
search for, assume, or certify a nontrivial ordinary Collatz cycle.
"""

from math import gcd


def t1(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def ts(n, s):
    return n // 2 if n % 2 == 0 else (3 * n + s) // 2


# The ordinary two-odd-predecessor chain is exact whenever the necessary
# roof congruence M == 8 (mod 18) holds.  These are finite path checks only.
ordinary_checks = 0
for a in range(1, 10_001):
    m = 18 * a + 8
    p = (2 * m - 1) // 3
    q = (4 * m - 5) // 9
    assert t1(q) == p and t1(p) == m
    assert q < m // 2 < p < m
    assert 4 * m - 9 * q == 5
    assert gcd(m, q) == gcd(m, 5)
    ordinary_checks += 1

# The generalized primitive word 10 gives the positive T_s cycle
# s -> 2s -> s.  It rules out a uniform >9/4 max/min theorem in the
# generalized-increment setting; for s=1 this is only the trivial cycle.
generalized_checks = 0
for s in range(3, 20_001, 2):
    r, m = s, 2 * s
    assert ts(r, s) == m and ts(m, s) == r
    assert m * 4 < r * 9
    generalized_checks += 1

# The existing raw-g maximum envelope is compatible with the inherited
# external R >= 2^71 after the 9/4 bridge.  We only need a small-exponent
# lower comparison: U_g > (3/2)^(gq)-1 >= (3/2)^q-1.
q_first_farey = 72_057_431_991
assert 3**8 > 2**12
assert q_first_farey >= 150
# (3/2)^q > 2^(q/2) >= 2^75, and 2^75-1 > 9*2^69.
assert 2**75 - 1 > 9 * 2**69

print("RL105 roof factor-5 barrier verifier: PASS")
print("ordinary roof-chain checks =", ordinary_checks)
print("generalized word-10 checks =", generalized_checks)
print("envelope compatibility exponent q =", q_first_farey)

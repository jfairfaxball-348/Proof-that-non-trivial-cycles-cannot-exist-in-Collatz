#!/usr/bin/env python3
"""Exact finite audits for RL108 word-arithmetic claims.

Analytic claims (primitive-root proof, prefix-collapse theorem, LTE depth rigidity)
are proved in the report.  This script checks the quoted finite addresses and
word/cylinder identities exactly.
"""


def dlog2_mod3pow(M: int, O: int) -> int:
    assert O >= 1 and M % 3 == 2
    k = 1
    assert pow(2, k, 3) == M % 3
    for r in range(1, O):
        step = 2 * 3 ** (r - 1)
        mod = 3 ** (r + 1)
        hits = [d for d in range(3) if pow(2, k + d * step, mod) == M % mod]
        assert len(hits) == 1
        k += hits[0] * step
    assert 0 <= k < 2 * 3 ** (O - 1)
    assert pow(2, k, 3 ** O) == M % (3 ** O)
    return k


# Primitive-root order certificate for the finite depths used by the report.
for O in range(1, 25):
    order = 2 * 3 ** (O - 1)
    mod = 3 ** O
    assert pow(2, order, mod) == 1
    if order > 1:
        assert pow(2, order // 2, mod) != 1
    if O > 1:
        assert pow(2, order // 3, mod) != 1

assert dlog2_mod3pow(26, 4) == 9
assert dlog2_mod3pow(80, 4) == 27
assert dlog2_mod3pow(152, 4) == 51
assert dlog2_mod3pow(512, 6) == 9
assert dlog2_mod3pow(1106, 6) == 45
assert dlog2_mod3pow(890, 17) == 34_572_879

# Exact first-crossing sizes for the two local examples and RL108 witness.
assert 2 ** 9 <= 3 ** 6 < 2 ** 10
assert 2 ** 26 <= 3 ** 17 < 2 ** 27

# RL107 two-odd roof identity and RL108 non-dyadic witness.
assert (4 * 890 - 5) % 9 == 0
assert (4 * 890 - 5) // 9 == 395
assert 890 & (890 - 1) != 0

print("RL108 word arithmetic verifier: PASS")
print("kappa_17(890) =", dlog2_mod3pow(890, 17))

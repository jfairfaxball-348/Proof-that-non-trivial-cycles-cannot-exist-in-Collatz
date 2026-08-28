#!/usr/bin/env python3
"""Fast exact algebra/sanity checks for the RL147 layered-carry reduction."""
from itertools import product

# Exhaustively check the superlevel expansion and numerator identity in small
# mechanical examples.  This is a sanity check, not a substitute for the proof.
checked = 0
for A, L, g in ((3, 2, 2), (5, 3, 2), (7, 4, 2)):
    N = g * L
    b = [(A * j) // L for j in range(N + 1)]
    B = [3 ** (N - 1 - j) * 2 ** b[j] for j in range(N)]
    for H in (0, 1, 2, 3):
        for middle in product(range(H + 1), repeat=N - 1):
            h = (0,) + middle + (0,)
            a = [b[j + 1] - b[j] + h[j] - h[j + 1] for j in range(N)]
            if min(a) < 1 or max(h) != H:
                continue
            q = sum(3 ** (N - 1 - j) * 2 ** (b[j] - h[j]) for j in range(N))
            qc = sum(B)
            rhs = qc + sum(2 ** (H - ell) * sum(B[j] for j in range(N) if h[j] < ell)
                           for ell in range(1, H + 1))
            assert 2 ** H * q == rhs
            checked += 1
assert checked > 100

# RL146's local strict-order lemma remains true for the height-one digit set.
for a in (1, 2):
    M = 2 ** a
    for yt, ys, ut, unextt, us, unexts in product(range(-8, 9), range(-8, 9), (0, 1), (0, 1), (0, 1), (0, 1)):
        if yt <= ys:
            continue
        nt, ns = 3 * yt + ut - unextt, 3 * ys + us - unexts
        if nt % M == 0 and ns % M == 0:
            assert nt // M > ns // M

# At height two the exact allowed digit values are {0,1,3}; strict order can
# collapse for either allowed mechanical increment.
for a in (1, 2):
    M = 2 ** a
    assert (3 * 1 + 0 - 3) // M == 0
    assert (3 * 0 + 3 - 3) // M == 0

print("RL147 fast verifier: PASS")
print("checked bounded-height numerator identities =", checked)
print("scope = algebra/sanity only; no mixed-height exclusion")

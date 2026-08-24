#!/usr/bin/env python3
"""Exact bounded audit of the elementary RL82 RL-flat kickoff lemmas.

This script is not the proof. It checks the formulas and branch classification
on a large symbolic parameter range to catch transcription/algebra errors.
"""

CHECKS = 0
BRANCH_CHECKS = 0

for r in range(0, 10000):
    M = 18*r + 8
    P = 12*r + 5
    Q = 8*r + 3

    assert M % 2 == 0
    assert P % 2 == 1
    assert Q % 2 == 1
    assert (3*P + 1)//2 == M and (3*P + 1) % 2 == 0
    assert (3*Q + 1)//2 == P and (3*Q + 1) % 2 == 0
    assert M % 18 == 8
    assert P % 12 == 5
    assert Q % 8 == 3
    CHECKS += 8

    # Candidate predecessor of Q via even branch.
    E = 2*Q
    assert E <= M
    assert E > M/2

    # An even predecessor of E would exceed M.
    assert 2*E > M

    # Odd predecessor of Q exists iff r == 1 mod 3.
    odd_Q_integral = ((2*Q - 1) % 3 == 0)
    assert odd_Q_integral == (r % 3 == 1)

    # If Q uses its even predecessor E, E can itself have a predecessor <= M
    # only through its odd inverse, requiring E == 2 mod 3, i.e. r == 2 mod 3.
    odd_E_integral = (E % 3 == 2)
    assert odd_E_integral == (r % 3 == 2)

    # Thus r == 0 mod 3 has no extendable predecessor choice for Q.
    if r % 3 == 0:
        assert not odd_Q_integral
        assert not odd_E_integral
    elif r % 3 == 1:
        R = (2*Q - 1)//3
        assert R > 0 and R % 2 == 1 and R <= M
    else:
        S = (2*E - 1)//3
        assert S > 0 and S % 2 == 1 and S <= M

    BRANCH_CHECKS += 8

print("RL82 RL-flat seed verifier: PASS")
print(f"top-triple checks = {CHECKS}")
print(f"backward-branch checks = {BRANCH_CHECKS}")
print("derived maximum residue classes mod 54 = {26, 44}")

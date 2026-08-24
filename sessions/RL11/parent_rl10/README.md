# RL-10 handover

This directory continues the RL branch from RL-9.

Main result: `RL10_RADIUS3_FLOW_AND_THREE_JUMP_REDUCTION_2026-08-20.md`.

RL-10 does **not** claim radius 3 is completely closed. It proves the exact radius-3 flow classification, closes the connected branch analytically, derives the common-base/geometric-`Q` identities, and reduces the remaining coprime one-orbit branches to explicit sparse three-jump congruences.

Verifier: `verify_rl10_radius3_flow.py`.

The exact constructive scan through `A<=40` finds only the nonprimitive repeated trivial word `(10)^3` as a `D`-divisible radius-3 survivor.

# Collatz R# RL-4 Seed

This bundle continues the RL branch from the RL-3 handover.

## Main new file

- `RL4_CROSSING_SLACK_AND_CYCLE_EXIT_2026-08-19.md`

## What changed

- `k>0`: first order crossing is now controlled by an exact relative product identity, cumulative exponent catch-up, and a phase/slack threshold. The first-crossing state no longer needs a free continuous ratio interval.
- `k=0`: equality in the xi barrier is classified exactly on the minimum rotation; every exponent-1 plateau now has an exact compressed normal form. The root exit obeys a coupled 2-adic/3-adic inequality, and periodic return forces a later high/deep xi descent. The first root-exit filter prunes about 46% of the ordinary 2-adic root cylinder but leaves positive measure. Scalar plateau telescoping is proved equivalent to the existing cycle-product slope, so the next gain must come from discrete valuation transitions.

## Verification

Run:

`python3 tools/verify_rl4_crossing_exit.py`

Expected result: `RL-4 crossing / cycle-exit verifier: PASS`.

RL remains open. No file in this bundle claims a proof of the Collatz conjecture or exclusion of all nontrivial cycles.

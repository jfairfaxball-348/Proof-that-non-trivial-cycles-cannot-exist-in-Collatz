# Session Provenance — RL-6

**Date:** 2026-08-19

Input seed: `Collatz_Rsharp_RL5_Seed_2026-08-19.zip` supplied by the user.

Inherited verifier `parent_rl5/tools/verify_rl5_anchor_grammar.py` was rerun and passed.

New analytic work:

- positive-total height-word cycle lemma -> 3-adically good rotation;
- exact boundary numerator transport/cancellation gate;
- generalized realization criterion including exact boundaries;
- minimum-anchor denominator-defect/error-budget inequality.

New exact computation:

- `tools/verify_rl6_boundary_good_rotation.py`.

External literature was checked only as a guardrail. Barina's 2025 published verification through `2^71` and Hercher's `m>=92` theorem remain consistent with the inherited register. A 2026 faster verification algorithm was noted but not used as a stronger completed verification bound.

No claim of a Collatz proof is made.

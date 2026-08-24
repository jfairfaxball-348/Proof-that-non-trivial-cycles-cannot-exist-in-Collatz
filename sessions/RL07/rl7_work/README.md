# Collatz R# RL-7 handover

Primary new report:

- `RL7_MIXED_DIVISIBILITY_AND_CHRISTOFFEL_GAP_2026-08-19.md`

Canonical delta and roadmap:

- `RL7_CANONICAL_REGISTER_DELTA_2026-08-19.md`
- `RL7_ROADMAP_UPDATE_2026-08-19.md`
- `NEXT_SESSION_KICKOFF_PROMPT.md`

Verification:

- `tools/verify_rl7_mixed_invariants.py`
- `logs/RL7_MIXED_INVARIANT_VERIFICATION_LOG.txt`
- `logs/RL6_INHERITED_RECHECK_LOG.txt`

`parent_rl6/` contains the complete RL-6 work tree for self-contained continuation.

**Verdict:** RL remains open. The unit-edge route is now classified: one-edge self-rotations are exactly primitive Christoffel classes, which are internally excluded by divisibility. The next route is weighted paths of length >=2. The main quantitative result is the explicit non-Christoffel numerator gap `>3^(L-1)/4`, now internal for every primitive nontrivial cycle.

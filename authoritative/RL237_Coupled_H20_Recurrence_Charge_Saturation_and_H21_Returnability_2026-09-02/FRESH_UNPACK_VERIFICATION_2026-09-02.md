# RL237 fresh-unpack verification — 2026-09-02

Status: **PASS**.

A deterministic canonical ZIP was reconstructed from the frozen RL237 package, extracted into a clean directory, and checked without repository-relative dependencies.

Clean-unpack fast checks passed:

- every entry listed in `SHA256SUMS.txt`;
- exact reconstruction of all `7531` retained full-prefix atomic cells;
- generic-budget discharge of all but `17` candidate cells;
- exact local K-pricing and coverage on those `17` candidates;
- final invariant-specific cap arithmetic;
- final coupled charge lower bound and saturation slope;
- `verification/verify_rl237_proof_state.py`;
- freeze/pivot guard: RL238 is Gate B / radius 4 and is NOT STARTED.

The three promoted chronological recurrence certificates are expensive finite certificates and are handled under verification economy:

- their exact in-session run output is frozen in `DEEP_RECURRENCE_OUTPUT.txt`;
- their exact self-contained replay source is `verification/verify_rl237_deep_recurrence.py`;
- the routine clean-unpack fast suite does not re-run the 278,049-atom H20 spacing-5597 scan.

The package is portable and self-contained for both fast verification and optional deep replay.

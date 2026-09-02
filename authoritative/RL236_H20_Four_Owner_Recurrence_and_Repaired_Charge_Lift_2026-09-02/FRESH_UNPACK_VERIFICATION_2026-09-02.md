# RL236 fresh-unpack verification — 2026-09-02

Status: **PASS**.

A deterministic canonical ZIP was reconstructed from the frozen package, extracted into a clean directory, and checked without repository-relative dependencies.

Checks passed:

- every entry listed in `SHA256SUMS.txt`;
- `verification/verify_rl236_recurrence_and_charge.py`;
- `verification/verify_rl236_proof_state.py`;
- exact H20 four-owner recurrence scan through separation 3031;
- repaired charge coverage at the corrected final early-band boundary;
- correction guard withdrawing the uncovered `>763` scratch lift;
- successor and Gate-state guard.

The package is portable and self-contained for the promoted RL236 result.

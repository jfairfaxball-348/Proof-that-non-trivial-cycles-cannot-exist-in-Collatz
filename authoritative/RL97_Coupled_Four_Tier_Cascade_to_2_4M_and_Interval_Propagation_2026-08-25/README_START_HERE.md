# RL97 handover bundle — start here

This bundle freezes the completed RL96 corrected coupled-cascade extension.

Read in this order:

1. `RL96_COUPLED_FOUR_TIER_CASCADE_TO_2_4M_AND_INTERVAL_PROPAGATION.md`
2. `RL96_SESSION_STATE_AND_RL97_KICKOFF_2026-08-25.md`
3. `RL97_COUPLED_CASCADE_BEYOND_2_4M_TARGET.md`
4. `notes/RL96_CORRECTION_AND_DEMOTION_LEDGER.md`

Verification:

- run `verification/run_fast_rl96_verifiers.sh`;
- `verification/RL96_SCAN_CERTIFICATE.txt` summarizes the exact completed scan ranges;
- `verification/raw_rl96/` contains every load-bearing RL96 scan record;
- `SHA256SUMS.txt` authenticates every file in the bundle except itself.

The frozen status remains branch-specific: Gate A odd `k>=27` is globally open, Gate B is globally open, RL/nontrivial-cycle exclusion is open, and the Collatz conjecture is not proved.

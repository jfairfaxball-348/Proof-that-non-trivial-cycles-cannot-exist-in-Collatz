# RL98 handover bundle — start here

This bundle freezes the completed RL97 sustained corrected coupled-cascade extension from deep radius `2,400,000` to `3,000,000`.

Read in this order:

1. `RL97_SESSION_STATE_AND_RL98_KICKOFF_2026-08-25.md`
2. `RL97_COUPLED_FOUR_TIER_CASCADE_TO_3M_AND_INTERVAL_PROPAGATION.md`
3. `RL98_COUPLED_CASCADE_BEYOND_3M_TARGET.md`
4. `notes/RL97_CORRECTION_AND_DEMOTION_LEDGER.md`
5. `verification/RL97_SCAN_CERTIFICATE.txt`
6. run `verification/run_fast_rl97_verifiers.sh`

The `verification/raw_rl97/` files contain the completed gap-free RL97 scan records. `SHA256SUMS.txt` authenticates every bundle file except itself.

Frozen branch-specific endpoint: all odd `k` through `2,921,801,521` are excluded on the exact first-Farey/full-phase Gate-A branch; first live odd is `2,921,801,523`.

The frozen global status remains unchanged: Gate A odd `k>=27` is globally open, Gate B is globally open, RL/nontrivial-cycle exclusion is open, and the Collatz conjecture is not proved.

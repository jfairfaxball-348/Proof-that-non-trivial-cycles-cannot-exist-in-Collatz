# RL95 handover — start here

Authoritative continuation state after RL94.

Read in this order:

1. `RL94_SESSION_STATE_AND_RL95_KICKOFF_2026-08-25.md`
2. `RL94_COUPLED_FOUR_TIER_CASCADE_TO_2M_AND_INTERVAL_PROPAGATION.md`
3. `RL95_COUPLED_CASCADE_BEYOND_2M_TARGET.md`
4. `notes/RL94_CORRECTION_AND_DEMOTION_LEDGER.md`
5. `verification/RL94_SCAN_CERTIFICATE.txt`

Run `verification/run_fast_rl94_verifiers.sh` from the bundle root before accepting the frozen state.

Verification economy applies: the new RL94 scan outputs are exact completed chunks and are checked by aggregation; do not recursively replay inherited expensive scans unless a verifier fails, a dependency is unresolved, or a stop-and-repair event is triggered.

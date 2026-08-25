# RL96 handover — start here

Authoritative continuation state after RL95.

Read in this order:

1. `RL95_SESSION_STATE_AND_RL96_KICKOFF_2026-08-25.md`
2. `RL95_COUPLED_FOUR_TIER_CASCADE_TO_2_2M_AND_ULTRA_FLOOR_REPAIR.md`
3. `RL96_CORRECTED_COUPLED_CASCADE_BEYOND_2_2M_TARGET.md`
4. `notes/RL95_CORRECTION_AND_DEMOTION_LEDGER.md`
5. `verification/RL95_SCAN_CERTIFICATE.txt`

Run

`verification/run_fast_rl95_verifiers.sh`

from the bundle root before accepting the frozen state.

Verification economy applies: the new RL95 scan outputs are exact completed records and are checked by aggregation; do not recursively replay inherited expensive scans unless a verifier fails, a dependency is unresolved, or a stop-and-repair event is triggered.

Key live change: the ultra extension found a new global bit-length minimum `15,000,037 at r=575,974`, so the full-radius ultra safe depth is now `D_u=15,000,035`.

The next live candidate is `k6=2,921,766,551`.

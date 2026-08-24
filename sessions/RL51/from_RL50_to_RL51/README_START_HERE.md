# RL50 -> RL51 handover — START HERE

This bundle is the session handover after RL50.

## First actions

1. Verify the outer `.zip.sha256` sidecar.
2. Extract the ZIP.
3. Run:

   `bash verification/run_all_rl50_handover_verifiers.sh`

4. Read:

   `RL50_FINAL_PROOF_STATE_AND_RL51_ROADMAP.md`

5. Use:

   `RL51_RESEARCH_KICKOFF_PROMPT_2026-08-22.md`

   as the kickoff for the next research session.

## Critical proof-state warnings

- RL / Collatz is not closed.
- The direct full-phase -> radius-3 shortcut is dead.
- The Ansari-based strengthened external floor is demoted; use stable `2^71` unless a stronger floor is independently re-audited.
- The current stable first target is the tiny `z=27` coupled gap; after that the old separable rank relaxation should be abandoned in favor of terminal-power / synchronized-return arithmetic.

## Bundle layout

- `rl50_research/`: all RL50 notes and exact verifiers available at handover time.
- `inherited_rl49_to_rl50/`: the complete prior handover tree, preserved for provenance.
- `source_bundle/`: exact prior outer ZIP and checksum sidecar.
- `verification/`: portable handover verifier runner and the explicit stale-path repair verifier.

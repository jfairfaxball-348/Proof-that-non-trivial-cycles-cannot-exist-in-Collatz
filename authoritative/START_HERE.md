# RL346 authoritative start

Status: RL345 CLOSED/FROZEN; RL346 is the unique incoming research session and has not started.

Transport is the committed flat Git-tree authority. Git tree/blob identities and the RL345 atomic commit/readback are the current lossless transport checks. Historical ZIP/sidecar pairs and older target files are provenance only.

## Unique RL346 target

Read and execute only `RL346_R1_CRT_COMPLETION_TARGET.md` after the start gate.

## Current proof state

R1 Parent Bridge is OPEN at 94% obligation-level progress.

RL345 strengthened Phase 4 to an exact 23-source/72-endpoint singleton interface. A fixed 23-gap source prefix is unique inside the RL344 `<2^37` phase window after odd parity is included, and a fixed 72-gap suffix has at most one viable endpoint. The only low-modulus 72-gap cases were exhaustively eliminated by a 135,356-endpoint escape certificate with an independent red team.

Phase 4 remains OPEN: the singleton interfaces still require complete predecessor/successor CRT, ownership, row-contact/wrap, phase-sign, and least-state-descent intersection. Phase 5 remains scratch-only and must not resume until Phase 4 closes. Phase 6 is conditional.

Read `RL345_PROOF_LEDGER.md`, `RL345_EXACT_CERTIFICATE.md`, `RL345_CORRECTION_AND_DEMOTION_LEDGER.md`, `RL345_GLOBAL_PROOF_ROADMAP_STATUS.md`, and `RL345_SESSION_STATE_AND_RL346_KICKOFF.md`.

## Current portable verification

Run:
- `python3 -I verification/verify_rl345_fast.py`
- `python3 -I verification/red_team_rl345.py`

Both must be GREEN.

Knowledge catalogues are stale/deferred.

# RL340 closeout verification

Date: 2026-09-16
Status: GREEN FOR THE PROMOTED SCOPED CLAIMS; stronger `92/91` candidate explicitly UNPROMOTED.

Incoming BASE_HEAD: `3504e01531b7c45699f35a4fbb42460008b83b73`.

Connector closeout uses the committed flat Git-tree transport permitted by `AGENTS.md` and `docs/VERIFICATION_AND_CLOSEOUT.md`. Before promotion, live `main` was read back and remained exactly at BASE_HEAD. `verification/verify_rl340_fast.py` and independently coded `verification/red_team_rl340.py` both reconstructed 52 factors, 684 templates, 10 rows / 10 distinct sources, maximum escape depth 29. The direct-consumer arithmetic reproduced carry gap `12,146,996,285` and proved required inherited weighted-support gain exceeds 145 billion and 23 times the rho=60 minimal positive-rank count. The algebraic equivalence of the frozen `92/91` candidate was checked, but its complete finite edge/potential certificate was not available at closeout, so it is explicitly unpromoted.

Current fast verifier: `python3 -I authoritative/verification/verify_rl340_fast.py` -> `RL340_FAST_GREEN`.
Independent red team: `python3 -I authoritative/verification/red_team_rl340.py` -> `RL340_RED_TEAM_GREEN`.

No current ZIP/sidecar transport is used. Committed Git tree/blob identities and post-commit readback are the lossless transport checks. Relevant prior ledgers/verifier provenance are copied under `authoritative/inherited/`. Knowledge catalogues are `stale/deferred`.

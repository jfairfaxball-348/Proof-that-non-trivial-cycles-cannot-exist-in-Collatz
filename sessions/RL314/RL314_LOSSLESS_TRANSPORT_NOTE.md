# RL314 lossless closeout transport note

Date: 2026-09-13

RL314 is promoted using one atomic Git-object transition from incoming HEAD
`e443671d71b2320d42ba3d420bda33df55d7fb44`.

The exact incoming authoritative files are archived by reusing their immutable
Git blob identities:

- incoming `authoritative/START_HERE.md` blob:
  `c62213e25d1b6c6367240c5f9edb49db3f0092be`;
- incoming `authoritative/RL314_FULL_STRATEGIC_AUDIT_TARGET.md` blob:
  `851805aca90e030dfb16060c3966ec7bdfa788b0`.

No ZIP or lossy reconstruction is used.

The closeout transition must:

1. preserve those blobs under `sessions/RL314/`;
2. add the audit report, correction/splice ledger, and closeout;
3. remove the old RL314 target from `authoritative/`;
4. install exactly one RL315 target plus `authoritative/START_HERE.md`;
5. move `main` by one fast-forward commit only after the complete tree exists.

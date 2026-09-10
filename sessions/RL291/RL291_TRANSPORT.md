# RL291 transport

Date: 2026-09-10

RL291 closeout is transported directly by Git objects from exact incoming parent

`c438c06b7a18c9b46e59096c19864f898baf751f`.

The RL291 session tree contains:

- `RL291_SYNTHESIS_AND_FAST_TRACK_REPORT.md`;
- `RL291_CLOSEOUT.md`;
- `RL291_TRANSPORT.md`;
- `RL292_FIXED_SEED_BELLMAN_DANGER_SET_CONTRACTION_GATE_A_TARGET.md`.

The successor target is duplicated losslessly under `authoritative/`, and `authoritative/START_HERE.md` advances to RL292.

The old authoritative RL291 target is removed in the same tree transition.

This closeout uses direct Git-object transport: the parent commit, resulting tree, per-file blob identities, and final commit provide the lossless provenance. No ZIP or outer sidecar is used.

Generated `knowledge/` catalogues are not regenerated and remain `stale/deferred`.

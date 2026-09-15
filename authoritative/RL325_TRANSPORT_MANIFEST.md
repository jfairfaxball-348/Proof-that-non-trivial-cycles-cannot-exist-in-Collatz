# RL325 transport manifest

Date: 2026-09-15
Transport: LOSSLESS CONNECTOR GIT-TREE RECONSTRUCTION

## Authority transition

Incoming RL: RL325
Successor RL: RL326
BASE_HEAD: `e12cbd171fd9b4920c32ba10f1066faea77ad1b1`
Incoming root tree: `1c4fae10be12219b8eeade1f6f02d399e4e50a9e`
Incoming authoritative tree: `de88537d481a1f4496af2802e9989bccc6bfd368`

## Candidate files

- `RL324_LOCAL_PROPAGATION_BARRIER.md`
- `RL325_CLOSEOUT.md`
- `RL325_CORRECTION_AND_DEMOTION_LEDGER.md`
- `RL325_FRESH_RECONSTRUCTION_VERIFICATION.md`
- `RL325_GLOBAL_PROOF_ROADMAP_STATUS.md`
- `RL325_PARENT_BRIDGE_GLOBAL_OWNERSHIP_TELESCOPE_TARGET.md`
- `RL325_PROOF_LEDGER.md`
- `RL325_RED_TEAM_REPORT.md`
- `RL325_SESSION_STATE_AND_RL326_KICKOFF.md`
- `RL325_TRANSPORT_MANIFEST.md`
- `RL325_VERIFIER_OUTPUT.txt`
- `RL326_PARENT_BRIDGE_FINITE_ENDGAME_AND_CARRY_DESCENT_TARGET.md`
- `SHA256SUMS.txt`
- `START_HERE.md`
- `verification/verify_rl325_global_ownership.py`

`SHA256SUMS.txt` covers every file above except itself.

## Reused provenance identities

The inherited barrier and incoming RL325 target are preserved verbatim from BASE_HEAD. Their Git blob identities before promotion are:

- `RL324_LOCAL_PROPAGATION_BARRIER.md`: `02cb76a5001a2ac322d3f84fa997531b3233e64b`
- `RL325_PARENT_BRIDGE_GLOBAL_OWNERSHIP_TELESCOPE_TARGET.md`: `88c83b3a0a783f7e0a9b39ef89752d8255964d33`

## Verification policy

No ZIP is used in this connector closeout. Therefore no outer ZIP sidecar applies.

Losslessness is checked by:

1. internal SHA-256 manifest;
2. clean reconstruction;
3. portable exact verifier;
4. candidate Git blob/tree identities;
5. final remote readback of both `sessions/RL325/` and successor `authoritative/`.

Knowledge catalogues are `stale/deferred` and are intentionally unchanged.

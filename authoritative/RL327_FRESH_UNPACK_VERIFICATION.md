# RL327 fresh unpack verification

Date: 2026-09-15
Status: VERIFIED FOR CLOSEOUT

## Environment

Connector-worker closeout. The Codex working ZIP was independently unpacked in the local sandbox, its verifier rerun, and the red team rerun after a mechanical sibling-path portability repair. No repository-shell command is claimed.

## Incoming authority snapshot

`BASE_HEAD = f37a2984065548440a8ae0973060f97a40a44a2b`

Incoming root tree:

`40912ad9871fd29e4f32116944c714eb2e79eae7`

Incoming `authoritative/` tree:

`154b9f1a91b25842aff9e6c798ebbd14263559e6`

These identities are the concurrency snapshot for promotion.

## Candidate verification

The corrected portable verifier and red team both pass. The main verifier emits `RL327_OWNED_EXCESS_DENSITY_VERIFIER_GREEN`; the red team emits `RL327_OWNED_EXCESS_RED_TEAM_GREEN`.

The session scratch parity omission is explicitly demoted and no invalidated count appears in the promoted ledger.

## Fresh reconstruction

The final deterministic handover ZIP is unpacked into clean temporary storage during closeout. Its outer SHA-256 sidecar, internal `SHA256SUMS.txt`, and both portable scripts are checked before promotion.

## Catalogue status

Generated `knowledge/` catalogues are **stale/deferred** for this connector transition. They are not part of the mathematical promotion gate.

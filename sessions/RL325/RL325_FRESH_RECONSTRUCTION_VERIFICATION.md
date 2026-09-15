# RL325 fresh reconstruction verification

Date: 2026-09-15
Status: VERIFIED FOR CLOSEOUT

## Environment

Connector-worker closeout. Repository-shell commands were not claimed or required. The equivalent closeout checks were performed from the frozen candidate files, exact hashes, Git tree/blob identities, and a clean local reconstruction.

## Incoming authority snapshot

`BASE_HEAD = e12cbd171fd9b4920c32ba10f1066faea77ad1b1`

Incoming root tree:

`1c4fae10be12219b8eeade1f6f02d399e4e50a9e`

Incoming `authoritative/` tree:

`de88537d481a1f4496af2802e9989bccc6bfd368`

These identities are the concurrency snapshot for promotion.

## Candidate reconstruction

The RL325 handover was reconstructed into clean temporary storage from the candidate text payloads plus the two inherited verbatim provenance files:

- `RL324_LOCAL_PROPAGATION_BARRIER.md`;
- `RL325_PARENT_BRIDGE_GLOBAL_OWNERSHIP_TELESCOPE_TARGET.md`.

The internal `SHA256SUMS.txt` was then checked from the clean reconstruction.

Result: **PASS**.

## Portable verifier

Command-equivalent invocation:

`python3 -I verification/verify_rl325_global_ownership.py`

Result: **PASS** with first line

`RL325_GLOBAL_OWNERSHIP_VERIFIER_GREEN`.

The frozen stdout is in `RL325_VERIFIER_OUTPUT.txt`.

## Red team

`RL325_RED_TEAM_REPORT.md` result: **GREEN**.

In particular the root-aligned `G<2^35` scope transfer was caught and demoted before promotion.

## Transport

Transport mode is documented lossless Git object/tree reconstruction, permitted by the connector-worker closeout protocol. No ZIP was required, so an outer `.zip.sha256` sidecar is not applicable.

The internal SHA-256 manifest plus Git blob/tree identities provide the lossless transport check.

## Catalogue status

Generated `knowledge/` catalogues were not regenerated in the connector environment and remain **stale/deferred**. They are not part of the mathematical promotion gate.

## Promotion readiness

Candidate mathematical state: verified.
Candidate internal manifest: verified.
Portable fast verifier: green.
Red team: green.
Incoming snapshot identity: recorded and must be reconfirmed immediately before ref advancement.
Successor number: RL326, exactly one ahead of incoming RL325.

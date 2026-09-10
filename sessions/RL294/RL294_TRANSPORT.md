# RL294 transport

Date: 2026-09-10

RL294 closeout is transported directly by Git objects from exact incoming parent

`c1a030735ae853a1ff55d563e75e1ab8a31e86f5`.

The frozen RL294 session contains the report transport index, lossless report, closeout, scratch freeze, portable verifier/output, target-specific red team, SHA256 manifest, transport record, and the duplicated RL295 successor target.

The successor target is duplicated losslessly under `authoritative/`, and `authoritative/START_HERE.md` advances uniquely to RL295. The old authoritative RL294 target is removed in the same atomic tree transition.

This closeout uses direct Git-object transport. The parent commit, resulting tree, per-file blob identities, internal SHA256 manifest and final commit provide lossless provenance; no ZIP or outer sidecar is used, consistent with the current connector-worker convention inherited from RL292/RL293.

Generated `knowledge/` catalogues are not regenerated and remain `stale/deferred`.

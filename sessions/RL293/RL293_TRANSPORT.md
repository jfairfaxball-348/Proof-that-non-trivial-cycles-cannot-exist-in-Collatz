# RL293 transport

Date: 2026-09-10

RL293 closeout is transported directly by Git objects from exact incoming parent

`afce6e5659343daf37c78c967c452e60eb57b373`.

The frozen RL293 session contains the report transport index plus lossless report parts, closeout, scratch freeze, portable verification sources/outputs, target-specific red team, SHA256 manifest, transport record, and the duplicated RL294 successor target.

The successor target is duplicated losslessly under `authoritative/`, and `authoritative/START_HERE.md` advances uniquely to RL294. The old authoritative RL293 target is removed in the same atomic tree transition.

This closeout uses direct Git-object transport. The parent commit, resulting tree, per-file blob identities, internal SHA256 manifest and final commit provide lossless provenance; no ZIP or outer sidecar is used, consistent with the current connector-worker convention inherited from RL292.

Generated `knowledge/` catalogues are not regenerated and remain `stale/deferred`.

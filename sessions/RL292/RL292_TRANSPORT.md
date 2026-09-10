# RL292 transport

Date: 2026-09-10

RL292 closeout is transported directly by Git objects from exact incoming parent

`6133a02d8d141ce9714190e9c8772e904832f95b`.

The frozen RL292 session contains the main-report transport index plus lossless report parts, closeout, scratch-freeze transport index plus lossless scratch parts, verification sources/outputs, SHA256 manifest, transport record, and the duplicated RL293 successor target.

The successor target is duplicated losslessly under `authoritative/`, and `authoritative/START_HERE.md` advances uniquely to RL293. The old authoritative RL292 target is removed in the same atomic tree transition.

This closeout uses direct Git-object transport. The parent commit, resulting tree, per-file blob identities, internal SHA256 manifest and final commit provide lossless provenance; no ZIP or outer sidecar is used, consistent with the connector-worker convention.

Generated `knowledge/` catalogues are not regenerated and remain `stale/deferred`.

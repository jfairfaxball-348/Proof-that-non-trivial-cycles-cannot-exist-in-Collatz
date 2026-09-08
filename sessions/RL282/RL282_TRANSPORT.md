# RL282 connector-worker lossless transport

RL282 is closed by a connector worker using direct Git-object transport rather than a ZIP archive.

The complete frozen handover is the committed `sessions/RL282/` tree itself. Losslessness/integrity is established by:

- Git blob/tree identities in the atomic RL282 transition commit;
- `SHA256SUMS.txt` over every frozen handover payload file except the manifest itself;
- the portable verifier script and recorded clean verifier stdout;
- candidate-hash verification before promotion;
- post-commit readback of the frozen session and successor authority.

No ZIP is used, so no outer `.zip.sha256` sidecar applies.

The large `H<=26` scratch search is preserved only as unpromoted historical evidence in the report; it is not part of the closeout verification gate.

Generated `knowledge/` catalogues are unchanged and are `stale/deferred`, as permitted for connector-worker closeout.

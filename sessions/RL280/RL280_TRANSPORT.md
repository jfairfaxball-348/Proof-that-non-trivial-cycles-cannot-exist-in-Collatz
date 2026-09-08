# RL280 connector-worker lossless transport

RL280 is closed by a connector worker using direct Git-object transport rather than a ZIP archive.

The complete frozen handover is the committed `sessions/RL280/` tree itself. Losslessness/integrity is established by:

- Git blob/tree identities in the atomic RL280 transition commit;
- `SHA256SUMS.txt` over every frozen handover payload file except the manifest itself;
- the portable verifier script and recorded clean verifier stdout;
- candidate-hash verification before promotion;
- post-commit readback of the frozen session and successor authority.

No ZIP is used, so no outer `.zip.sha256` sidecar applies.

Generated `knowledge/` catalogues are unchanged and are `stale/deferred`, as permitted for connector-worker closeout.

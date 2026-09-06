# RL264 lossless transport note

Date: 2026-09-06
Status: VERIFIED CANDIDATE TRANSPORT

This connector-worker closeout uses the committed Git tree itself as the lossless transport, following the established recent repository convention.

No ZIP is required for this generation.

Integrity is provided by:

- `SHA256SUMS.txt` over every RL264 session artifact except the manifest itself;
- portable verifier source under `verification/`;
- fresh verifier output;
- one atomic Git-tree transition;
- post-commit remote-ref and file readback.

Knowledge catalogues are unchanged and therefore stale/deferred.

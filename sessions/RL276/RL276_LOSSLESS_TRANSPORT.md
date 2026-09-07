# RL276 lossless transport note

Date: 2026-09-07
Status: VERIFIED CANDIDATE TRANSPORT

This connector-worker closeout uses the committed Git tree itself as the lossless transport, following the repository's documented connector convention.

No ZIP is required for this generation.

Integrity is provided by:

- `SHA256SUMS.txt` over every frozen RL276 session artifact except the manifest itself;
- portable verifier source and frozen verifier output;
- candidate hashes checked in clean local reconstruction;
- one atomic Git-tree transition based on the recorded incoming tree;
- one remote `main` ref advance;
- post-commit remote-ref, session, manifest, verifier-output and successor-authority readback.

Incoming `BASE_HEAD`:

`987001e70dfe46b856c83c4fb22afb554b44761d`

Knowledge catalogues are unchanged and `stale/deferred`.

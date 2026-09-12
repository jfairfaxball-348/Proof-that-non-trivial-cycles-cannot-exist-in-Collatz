# RL305 lossless transport note

Closeout transport uses individual UTF-8 Git repository blobs in one atomic tree/commit transition. No opaque archive is required.

The incoming RL305 authoritative target is preserved byte-for-byte as `RL305_INCOMING_TARGET.md`; its Git blob identity is `abca09904b669e8e53101fcffba5b13a018d4bae`.

The audit result is frozen in `RL305_REPORT.md`, `RL305_PROOF_AND_SCOPE.md`, and `RL305_RED_TEAM.md`. Unpromoted successor leads are preserved in `RL305_SCRATCH_FREEZE.md`.

`SHA256SUMS.txt` covers every frozen RL305 session file except itself. The portable scalar-audit verifier is self-contained and is replayed before promotion.

Generated knowledge catalogues are unchanged and explicitly `stale/deferred`.

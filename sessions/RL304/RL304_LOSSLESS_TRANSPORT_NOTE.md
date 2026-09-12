# RL304 lossless transport note

Closeout transport uses individual UTF-8 Git repository blobs in one atomic tree/commit transition, matching the connector-supported convention used by RL303. No opaque archive is required.

The incoming RL304 target is preserved byte-for-byte as `RL304_INCOMING_TARGET.md`.

The theorem-grade fixed-96 and six-column grammar results are frozen in `RL304_REPORT.md` and `RL304_PROOF_AND_SCOPE.md`; exploratory witnesses, failed recurrences, and residual leads are retained in `RL304_SCRATCH_FREEZE.md`.

`SHA256SUMS.txt` covers every frozen session file except itself. The portable verifier is self-contained and is replayed before promotion.

# RL302 lossless transport note

Closeout transport uses individual UTF-8 repository blobs in one atomic Git tree/commit transition. No opaque archive is required.

The authoritative incoming RL302 target is preserved byte-for-byte as `RL302_INCOMING_TARGET.md` (Git blob SHA `ef9f4d09fddfb3115d60221ba0aa32b2c1b62dbf`).

The chronological scratch state is condensed in `RL302_SCRATCH_FREEZE.md`; all promoted load-bearing formulas are restated in `RL302_REPORT.md` and checked by the self-contained structural verifier. `SHA256SUMS.txt` covers every frozen session file except itself and is intended for clean-reconstruction integrity checking.

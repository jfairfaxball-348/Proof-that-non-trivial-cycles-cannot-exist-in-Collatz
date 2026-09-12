# RL303 lossless transport note

Closeout transport uses individual UTF-8 repository blobs in one atomic Git tree/commit transition. No opaque archive is required.

The authoritative incoming RL303 target is preserved byte-for-byte as `RL303_INCOMING_TARGET.md` using the existing Git blob `4305d5a2c130bb165e86268f1da9f3ad77305a78`.

The chronological scratch state is condensed in `RL303_SCRATCH_FREEZE.md`; all promoted load-bearing formulas are restated in `RL303_REPORT.md` and checked by the self-contained structural verifier where computational regression is appropriate. `SHA256SUMS.txt` covers every frozen session file except itself and is used for clean-reconstruction integrity checking.

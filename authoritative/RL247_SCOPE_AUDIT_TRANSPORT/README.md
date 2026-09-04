# RL247 closeout transport

Lossless `base64(xz(zip))` transport for the canonical RL247 scope-audit bundle.

Classification: **R3_R4_SCOPE_AUDIT_PASS**.
Canonical ZIP SHA256: `0f7e750190ea1f32854887ac44627d3238114919597535450331fc3c143237cf`.

Verify `PART_SHA256SUMS.txt`, reconstruct the payload, verify the outer ZIP hash, fresh-unpack, verify internal `SHA256SUMS.txt`, then run `verify_rl247_regressions.py`.

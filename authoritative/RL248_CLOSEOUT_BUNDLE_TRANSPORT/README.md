# RL248 closeout transport

Lossless `base64(xz(zip))` transport for the canonical RL248 bundle.

Classification: **R4_BRIDGE_REDUCED**.
Canonical ZIP SHA256: `b151319d108d11f31796bfd5071a309567e9cebafeccd127c234df4e1d4bf32c`.

Verify `PART_SHA256SUMS.txt`, reconstruct the payload, verify the outer ZIP hash, fresh-unpack, verify internal `SHA256SUMS.txt`, then run `verification/run_fast_suite.py`.

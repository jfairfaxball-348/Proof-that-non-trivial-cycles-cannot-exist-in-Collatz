# RL135 bundle transport

The RL135 mathematical handover was built and fresh-unpack verified locally as a 17,429-byte ZIP with SHA-256

`12e7124e4167ae8422481b29829f8f908883eba9563ae35d2da2e8a0e9501c01`.

This directory is the lossless GitHub-safe transport representation of that exact verified ZIP. The `RL135_bundle.zip.b64.partNN` files are byte-exact ASCII chunks whose concatenation is the base64 encoding of the ZIP.

Run:

`python reconstruct_rl135_bundle.py`

The script reconstructs `RL135_Multiplicity_Defect_Lift_and_Mesoscopic_State_Ceilings_2026-08-27.zip`, checks the exact 17,429-byte size, verifies SHA-256, checks every transport-part SHA-256, and checks all ZIP member CRCs. The `.zip.sha256` sidecar in `authoritative/` authenticates the reconstructed ZIP.

The direct binary ZIP is intentionally not committed through the connector because the immediately preceding RL134 promotion exposed a reproducible binary-transfer truncation defect. The extracted authoritative tree plus this transport are the canonical repository representation.

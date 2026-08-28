# RL136 bundle transport

The RL136 mathematical handover was built and fresh-unpack verified locally as an 18,061-byte ZIP with SHA-256

`6da49c03461eae98825181b5f1741386dcb5bf210dc086295bf3e164c8001856`.

This directory is the lossless GitHub-safe transport representation of that exact verified ZIP. `RL136_bundle.zip.b64.part01` is the byte-exact ASCII base64 encoding of the ZIP.

Run:

`python reconstruct_rl136_bundle.py`

The script reconstructs `RL136_Owned_Defect_Excursion_Isolation_and_Triangular_Packing_2026-08-27.zip`, checks the exact 18,061-byte size, verifies SHA-256, checks the transport-part SHA-256, and checks all ZIP member CRCs. The `.zip.sha256` sidecar in `authoritative/` authenticates the reconstructed ZIP.

The direct binary ZIP is intentionally absent because the recorded connector binary-transfer defect makes the ASCII transport the safe canonical repository representation.

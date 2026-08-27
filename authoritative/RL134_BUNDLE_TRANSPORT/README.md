# RL134 bundle transport repair

The RL134 mathematical handover was built and fresh-unpack verified locally as a 16,940-byte ZIP with SHA-256

`6ff26609ee5414dc7a2434b6bb3b7993577936894eb7c392395edf36ab6b21ec`.

During the original GitHub promotion commit `90849d0d268994dfdb3fde70df2d2e1c3e74fdfe`, the connector truncated the binary ZIP while leaving the extracted authoritative tree intact. The corrupt direct ZIP is therefore deliberately removed by the repair commit rather than retained as if valid.

This directory is a lossless transport representation of the exact verified ZIP. The eight `RL134_bundle.zip.b64.partNN` files are byte-exact ASCII chunks whose concatenation is the base64 encoding of that ZIP.

Run:

`python reconstruct_rl134_bundle.py`

The script reconstructs `RL134_Multiplicity_Determinant_Strip_and_Physical_Windows_2026-08-27.zip`, checks the exact 16,940-byte size, checks the SHA-256 above, and checks all ZIP member CRCs. The existing `.zip.sha256` sidecar in `authoritative/` names and authenticates this reconstructed ZIP.

No mathematical result, proof-state classification, frontier, or next-session target is changed by this transport repair.

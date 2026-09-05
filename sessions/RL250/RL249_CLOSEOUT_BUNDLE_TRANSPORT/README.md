# RL249 closeout bundle transport

Lossless transport for the canonical RL249 ZIP.

Reconstruct by concatenating `RL249_bundle.zip.b64.part*` in lexical order, base64-decoding the result, and checking the SHA256 in `TRANSPORT_MANIFEST.json` / the outer `.zip.sha256` sidecar. Then unzip, verify `SHA256SUMS.txt`, and run both scripts under `verification/`.

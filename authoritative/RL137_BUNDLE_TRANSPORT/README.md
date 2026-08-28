# RL137 bundle transport

This is the lossless ASCII transport for the verified 10,007-byte RL137 ZIP.
Run `python3 reconstruct_rl137_bundle.py`; it checks the base64 part hash,
decoded size, ZIP hash, and every ZIP member CRC. The root `.zip.sha256`
sidecar records the same ZIP hash. The binary ZIP is omitted from the tracked
handover; it is regenerated from this transport.

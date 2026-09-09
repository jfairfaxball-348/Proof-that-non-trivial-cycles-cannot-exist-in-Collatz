# RL286 connector-worker lossless transport

RL286 is closed using direct GitHub object/content transport.

The committed `sessions/RL286/` tree is the frozen handover. Integrity is represented by:

- Git commit/blob identities;
- `SHA256SUMS.txt` over every frozen RL286 payload except the manifest itself;
- the portable verifier and recorded PASS output;
- post-promotion readback of `authoritative/START_HERE.md`.

No ZIP archive is required.

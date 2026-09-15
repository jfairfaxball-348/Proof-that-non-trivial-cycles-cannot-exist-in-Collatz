# RL326 transport manifest

Date: 2026-09-15
Transport: physical deterministic ZIP plus outer SHA-256 sidecar

Incoming RL: RL326
Successor RL: RL327
BASE_HEAD: `82d9102e013fcf5d239e3cfee4a9b4c69b82fa00`

Canonical bundle: `RL326_to_RL327_Handover.zip`
Outer sidecar: `RL326_to_RL327_Handover.zip.sha256`

The ZIP contains the complete flat handover package rooted at `START_HERE.md`. Its internal `SHA256SUMS.txt` covers every package file except itself. The portable verifier is `verification/verify_rl326_mechanical_density.py`.

The deterministic ZIP uses sorted paths, stored file mode `0644`, timestamp `2020-01-01T00:00:00`, and deflate compression.

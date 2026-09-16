# RL336 clean fresh-unpack verification

Date: 2026-09-16. Status: GREEN.

Bundle: `RL336_HANDOVER_BUNDLE.zip`; SHA-256 `4ca58d766deaa2efb157286f7b38a00b2432ae68cd3e9a8938df843ddb3d69ec`. The outer `.zip.sha256` sidecar matches. A clean unpack passed safe path extraction, all 29 internal `SHA256SUMS.txt` entries, and exact byte-for-byte comparison with the frozen successor candidate.

All 10 `verify_*.py` portable scripts and `red_team_rl336.py` passed from the clean unpack under 120-second per-script limits. The 37 zero-run factors and 36 zero-run factors are each partitioned into disjoint verified ranges, with no gap or overlap. Exact q=32 prefix, potential, rational consumer, and independent red-team checks passed.

This report precedes atomic Git promotion. Remote-ref advance and post-commit readback remain mandatory.

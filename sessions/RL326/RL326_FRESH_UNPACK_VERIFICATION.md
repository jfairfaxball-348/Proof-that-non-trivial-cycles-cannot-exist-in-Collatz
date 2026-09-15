# RL326 fresh-unpack verification

Date: 2026-09-15
Status: VERIFIED FOR CLOSEOUT

The deterministic physical ZIP was reconstructed into a new temporary directory. The outer SHA-256 sidecar, internal `SHA256SUMS.txt`, exact package file set, and portable verifier were checked from that clean unpack.

Results:

- outer sidecar: PASS;
- internal manifest: PASS;
- candidate/unpack file identity: PASS;
- `python3 -I verification/verify_rl326_mechanical_density.py`: PASS;
- red team: GREEN.

The incoming authority remained at BASE_HEAD `82d9102e013fcf5d239e3cfee4a9b4c69b82fa00` with authoritative tree `e62ca5b1472e439ac8565007ddfe115fae491923` immediately before candidate construction. It must be reconfirmed immediately before promotion.

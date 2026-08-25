# Incoming RL90 verification

Date: 2026-08-25

Authoritative incoming archive:

`RL90_Near_Capacity_2Adic_Transition_Obstruction_2026-08-25.zip`

Outer SHA-256 supplied and independently reproduced:

`9955f9b12981b40e64886e78d212fc8c3e42f60e4fc7a196f47db6a0156bc84d`

Checks performed:

- outer sidecar: PASS;
- fresh unpack: PASS;
- internal `SHA256SUMS.txt`: PASS;
- supplied `RL90_FRESH_UNPACK_VERIFICATION_2026-08-25.txt`: PASS;
- `bash verification/run_fast_rl89_verifiers.sh`: PASS.

Verification economy was then applied. The frozen RL89 proof-state ledger was treated as authoritative and historical expensive certificates were not recursively replayed.

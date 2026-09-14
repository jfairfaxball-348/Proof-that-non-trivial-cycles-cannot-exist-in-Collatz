# RL319 -> RL320 fresh-unpack verification

Date: 2026-09-14
Status: PASS

Canonical bundle: `RL319_to_RL320_Handover.zip`
Outer SHA-256:
`ee0b2327bba4d891360ce2723985ac97b202c5a19ed5e0a236795a06b63dac9a`

Frozen source Git blobs:

- `RL319_CLOSEOUT.md`: `9e2560df0de3abb891843c57078eda6dac493e8c`
- `RL319_PROOF_LEDGER.md`: `1af057cfc3d2e65bacda06dad0c460a7d865d2f7`
- `RL319_RED_TEAM_REPORT.md`: `6356a7514353f413719f2840eeae1da437494da8`
- `RL319_SESSION_STATE_AND_RL320_KICKOFF.md`: `477b74bf00da884a4f93c1af0d0f5800900937b4`
- `RL320_LATE_ROW_HEIGHT_AND_ROOT_ALIGNED_CARRY_TARGET.md`: `6e284338b0e1d349ea3466f421d36649b1dae93e`
- `RL319_VERIFIER_OUTPUT.txt`: `383455407f309858814aa345eff33b343119dcb0`

Verification performed:

1. outer SHA-256 recomputed and matched the sidecar;
2. clean fresh unpack succeeded;
3. every internal `SHA256SUMS.txt` record matched;
4. fresh-unpacked closeout, proof ledger, red team, handover, and successor
   target matched the frozen session sources byte-for-byte;
5. all five portable verifiers passed from the clean unpack;
6. bounded word/state loops remained classified as regression evidence;
7. exact rational-log checks certified `G<2^35`, `v2(G)<=34`, and
   `kappa<2^34` in the stated root-aligned first-survivor scope.

RL320 status after verification: PREPARED, NOT STARTED.

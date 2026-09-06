# RL266 fresh-unpack verification

Date: 2026-09-06

Bundle: `RL266_Radius5_Kappa1_32_Closure_2026-09-06.zip`  
SHA256: `08ad7e1ab8a5f05830a8843db8087df0d5c5d66967f99ad773004047c2944a07`

Checks performed in clean temporary storage:
- ZIP extracted successfully;
- internal `SHA256SUMS.txt` verified all 11 entries;
- `verification/verify_rl266_kappa1_32.py` exit code 0;
- fresh fast-verifier stdout exactly matched frozen `verification/output.txt`;
- `verification/redteam_rl266_kappa1_32.py` exit code 0;
- fresh red-team stdout exactly matched frozen `verification/redteam_output.txt`;
- successor copies in `successor/` are byte-identical to the proposed authoritative RL267 files.

Result: **PASS**.

Execution environment: connector worker with local sandbox. Repository shell conveyor commands were not claimed; their bundle/manifest/fresh-unpack/verifier invariants were checked directly.

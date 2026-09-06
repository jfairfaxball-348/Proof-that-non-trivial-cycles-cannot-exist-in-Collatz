# RL267 fresh-unpack verification

Date: 2026-09-06

Bundle: `RL267_Radius5_Kappa1_311_221_Closure_2026-09-06.zip`  
SHA256: `412a96aa16b58db5184a5e263a424668bc8bb453a1b9a2711ad8c09e95fca0d9`

Checks performed in clean temporary storage:
- ZIP extracted successfully;
- internal `SHA256SUMS.txt` verified every bundled core file;
- `verification/run_fast_suite.sh` completed successfully;
- fresh analytic verifier stdout exactly matched frozen `verification/analytic_output.txt`;
- fresh `[3,1,1]` verifier stdout exactly matched frozen `verification/output_311.txt`;
- fresh `[2,2,1]` verifier stdout exactly matched frozen `verification/output_221.txt`;
- successor copies in `successor/` are the exact proposed RL268 authoritative files.

Pre-packaging independent red teams also passed and their sources/stdout are included in the bundle:
- complete independent `[3,1,1]` reconstruction;
- complete independent two-order `[2,2,1]` reconstruction;
- direct positive-domain brute-force replay through `A<=18`.

Result: **PASS**.

Execution environment: connector worker with local sandbox. Repository shell conveyor commands were not claimed; their bundle/manifest/fresh-unpack/verifier invariants were checked directly.

Repository lossless base64 transport was independently reconstructed after the fresh-unpack check; the reconstructed bytes matched the canonical ZIP exactly and reproduced SHA256 `412a96aa16b58db5184a5e263a424668bc8bb453a1b9a2711ad8c09e95fca0d9`.

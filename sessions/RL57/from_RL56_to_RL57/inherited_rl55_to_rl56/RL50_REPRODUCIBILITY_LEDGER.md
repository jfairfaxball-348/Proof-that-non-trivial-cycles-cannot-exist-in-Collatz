# RL50 reproducibility ledger

Date: 2026-08-22

- Source bundle: `Collatz_Rsharp_RL49_to_RL50_Handover_2026-08-22.zip`.
- Its supplied outer SHA-256 matched before RL50 work began.
- Original inherited files are preserved under `inherited_rl49_to_rl50/`.
- Known inherited plumbing defect: `rl49_research/verify_rl49_half_rotation_metric.py` hard-codes an obsolete `/mnt/data/RL49_work_2026-08-22/...` path.
- This handover does not modify that inherited file. It supplies `verification/verify_rl49_half_rotation_metric_portable.py`, identical in mathematics but resolving the bundled RL48 verifier relative to the handover root.
- The Ansari strengthened-floor verifier remains runnable as historical arithmetic/provenance. Its strengthened external premise is explicitly demoted by RL50 and must not be treated as accepted proof input.
- `SHA256SUMS.txt` covers the static handover contents except itself and `HANDOVER_VERIFICATION_RUN.txt`.
- `HANDOVER_VERIFICATION_RUN.txt` records the final release-verifier execution performed after the static manifest was generated.

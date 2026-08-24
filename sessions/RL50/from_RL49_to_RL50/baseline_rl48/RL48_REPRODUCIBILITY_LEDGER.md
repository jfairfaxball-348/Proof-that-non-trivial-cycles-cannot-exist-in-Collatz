# RL48 Reproducibility Ledger

Date: 2026-08-22

## 1. Handover integrity

From bundle root:

```bash
sha256sum -c SHA256SUMS.txt
```

This checks all files in the RL48->RL49 bundle except `SHA256SUMS.txt` itself.

## 2. Current RL48 verifier suite

Run:

```bash
bash verification/run_rl48_handover_verifiers.sh
```

This performs:

1. internal checksum verification of `rl48_initial/`;
2. `rl48_initial/run_all_rl48_progress_verifiers.sh`;
3. internal checksum verification of `rl48_continued/`;
4. `rl48_continued/run_all_rl48_continued_verifiers.sh`;
5. sidecar verification of all three inherited ZIP bundles.

Expected conclusions include:

- `RL48 canonical same-root selector verifier: PASS`;
- `RL48 rank-relaxation barrier verifier: PASS`;
- `RL48 phase-to-rank-defect algebra verifier: PASS`;
- `RL48 progress verifiers: PASS`;
- `RL48 four-swap/factorization verifier: PASS`;
- `RL48 two-trajectory semantic verifier: PASS`.

The inherited RL47 and RL45 examples must continue to fail the full phase scalar; a change to a zero phase remainder is a red flag, not a success.

## 3. q=134 baseline

`rl48_initial/RL47_Q134_STRESS_RERUN_RL48_BASELINE.txt` records the full rerun through `t=16`, all `hit 0`.

This is retained as a finite stress baseline only. It does not prove the uniform terminal theorem.

## 4. Inherited provenance bundles

The `inherited/` directory contains intact copies of:

- `Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip` and sidecar;
- `Collatz_Rsharp_RL48_Research_Output_2026-08-22.zip` and sidecar;
- `Collatz_Rsharp_RL48_Continued_2026-08-22.zip` and sidecar.

The first bundle contains the RL45/RL46/RL47 provenance needed to reconstruct the phase and transport conventions.

## 5. Historical radius-3 dependency

The exact RL18/RL19 radius-3 source bundle is not present here. This is intentional and explicitly tracked as the next audit dependency. If available elsewhere in the project, use the original source bundle and verify it before importing any theorem.

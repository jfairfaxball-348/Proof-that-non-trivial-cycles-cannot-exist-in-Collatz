# RL262 lossless transport note

Date: 2026-09-06
Status: VERIFIED CANDIDATE

The committed Git tree is the lossless transport for RL262; no binary ZIP is required, following the established connector-worker convention used by RL261.

The frozen session contains the incoming authority snapshot and target, exact fourth-selector elimination certificate, corrected global ordered-phase reduction, correction/demotion ledger, closeout report, fresh verification transcript, portable verifier and fast runner, successor target, session handover, and SHA-256 manifest.

`SHA256SUMS.txt` covers every frozen RL262 artifact except the manifest itself. A fresh checkout can verify integrity with `sha256sum -c SHA256SUMS.txt` from `sessions/RL262/`, then run `bash verification/run_fast_rl262_verifiers.sh`.

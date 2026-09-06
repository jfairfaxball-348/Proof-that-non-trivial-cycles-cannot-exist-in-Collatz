# RL261 lossless transport note

Date: 2026-09-06
Status: VERIFIED CANDIDATE

The committed Git tree is the lossless transport for RL261; no binary ZIP is
required, following the established connector-worker convention.

The frozen session contains the incoming authority snapshot and target, exact
full-phase selector-elimination certificate, correction/demotion ledger,
closeout report, fresh verification transcript, portable verifier and fast
runner, successor target, session handover, and SHA-256 manifest.

`SHA256SUMS.txt` covers every frozen RL261 artifact except the manifest itself.
A fresh checkout can verify integrity with `sha256sum -c SHA256SUMS.txt` from
`sessions/RL261/`, then run `bash verification/run_fast_rl261_verifiers.sh`.

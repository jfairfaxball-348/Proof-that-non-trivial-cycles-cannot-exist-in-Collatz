# RL260 lossless transport note

Date: 2026-09-05
Status: VERIFIED

The committed Git tree is the lossless transport for RL260; no binary ZIP is required.

The frozen session contains the incoming target, exact certificate report,
correction/demotion ledger, closeout report, fresh verification transcript,
portable Python/C++ verifier sources, deterministic low-case certificate,
successor target, session handover, and SHA-256 manifest.

`SHA256SUMS.txt` covers every frozen RL260 artifact except the manifest itself.
A fresh checkout can verify integrity with `sha256sum -c SHA256SUMS.txt` from
`sessions/RL260/`, then run `bash verification/run_fast_rl260_verifiers.sh`.

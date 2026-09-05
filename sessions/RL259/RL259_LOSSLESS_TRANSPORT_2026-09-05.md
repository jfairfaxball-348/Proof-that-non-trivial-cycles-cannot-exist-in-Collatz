# RL259 lossless transport note

Date: 2026-09-05
Status: VERIFIED

The committed Git tree is the lossless transport for RL259.  No binary ZIP is
required.

The session directory contains the frozen incoming target, theorem/certificate
report, correction/demotion ledger, closeout report, fresh verifier transcript,
portable verifier source, successor target, and SHA-256 manifest.

`SHA256SUMS.txt` covers every frozen RL259 artifact except the manifest itself.
A fresh checkout can verify integrity with `sha256sum -c SHA256SUMS.txt` from
`sessions/RL259/`, then rerun
`python3 verification/verify_rl259_second_selector.py`.

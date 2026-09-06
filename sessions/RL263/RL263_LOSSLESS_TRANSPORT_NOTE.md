# RL263 lossless transport note

Date: 2026-09-06
Status: VERIFIED CANDIDATE

The committed Git tree is the lossless transport for RL263; no binary ZIP is required.

The frozen session contains the incoming authority snapshot, the physical-gap theorem/method barrier, the RL262 modulus correction, closeout report, fresh verification transcript, portable verifier and fast runner, successor target, session handover, and SHA-256 manifest.

`SHA256SUMS.txt` covers every frozen RL263 artifact except the manifest itself. From `sessions/RL263/`, verify with `sha256sum -c SHA256SUMS.txt`, then run `bash verification/run_fast_rl263_verifiers.sh`.

# RL318 fresh verification record

Date: 2026-09-14
Closeout mode: connector-equivalent branch-staged atomic promotion

## Incoming authority

Incoming `main` before closeout:

`dbc49cfb64272761fdf2304aee4c1f3321b4c06c`

RL318 closeout was staged on branch `rl318-closeout` created exactly from that commit.  No research mutation was made on `main` before final promotion.

## Local exact consumer verifier

Verifier:

`sessions/RL318/verification/verify_rl318_external_floor_consumer.py`

SHA-256 of verifier text:

`5185ca1e15382550cf195d14fc2ab86c2ecba7a26059bd4160538621fb208b2e`

Result: PASS.

Recorded output:

- `external_floor=2^71=2361183241434822606848`
- `rl317_first_fibre_state_ceiling=1311372708449`
- `reduced_qmax=49547666543`
- `conditional_reduced_ell_frontier=49547666544`
- `first_above_resonance_survivor=(217976794617,137528045312)`
- `generic_RL310_packing_margin_gt_21.6x=PASS`

The verifier does **not** rerun or emulate Barina's exhaustive convergence computation.  It checks only the exact arithmetic used to consume the frozen external certificate.

## Historical verification economy

No expensive historical RL131/RL317 finite computation was rerun.  Their frozen verified outputs are inherited under the repository verification-economy policy.  RL318 replays only the new external-floor consumer arithmetic and the continued-fraction splice needed for the new checkpoint.

## Closeout integrity

The final closeout is valid only if all newly written authoritative/session files are read back from the staged branch and `main` is then fast-forwarded to that exact branch tip.  The final session response must report the resulting `main` commit.

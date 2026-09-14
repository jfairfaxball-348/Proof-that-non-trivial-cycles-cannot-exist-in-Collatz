# RL318 → RL319 handover manifest

Date: 2026-09-14
Transport mode: connector-native text handover

This closeout was staged on branch `rl318-closeout` from incoming `main` commit

`dbc49cfb64272761fdf2304aee4c1f3321b4c06c`.

The canonical handover consists of:

1. `RL318_PROOF_LEDGER.md`
2. `RL318_RED_TEAM_REPORT.md`
3. `RL318_EXTERNAL_2P71_DEPENDENCY.md`
4. `RL318_FRESH_VERIFICATION.md`
5. `RL318_VERIFIER_OUTPUT.txt`
6. `RL318_SESSION_STATE_AND_RL319_KICKOFF.md`
7. `RL319_CUT_SAFE_FIRST_EXTERNAL_SURVIVOR_G2_TARGET.md`
8. `sessions/RL318/RL318_CLOSEOUT.md`
9. `sessions/RL318/verification/verify_rl318_external_floor_consumer.py`
10. updated `START_HERE.md`

No binary ZIP is generated in this connector closeout.  Integrity is instead enforced by:

- branch staging from the exact incoming HEAD;
- local exact verifier replay;
- readback of all load-bearing files from the staged branch;
- one final fast-forward of `main` to the verified staged tip.

The verifier source SHA-256 is

`5185ca1e15382550cf195d14fc2ab86c2ecba7a26059bd4160538621fb208b2e`.

The final promoted `main` commit must be recorded in the user-facing closeout response after readback.

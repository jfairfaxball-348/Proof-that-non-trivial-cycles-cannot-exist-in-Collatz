# RL327 correction and demotion ledger

Date: 2026-09-15
Status: FROZEN FOR RL327 CLOSEOUT

## C1 — scratch-only omission of initial endpoint odd parity

An early exploratory singleton enumerator accepted endpoint lifts without explicitly requiring the initial endpoint to be odd. The independent red team detected the omission before promotion.

All counts produced by that enumerator are **discarded and non-authoritative**. The singleton range 47 through 98, two-positive range 47 through 98, and later total-46 bootstrap layer were rerun with explicit endpoint odd parity and complete recurrence reconstruction. Only the corrected counts in `RL327_PROOF_LEDGER.md` are promoted.

Classification: **scratch-only correction before promotion; no prior authoritative theorem is changed**.

## C2 — pre-repair total-46 exploration invalidated

Any total-46 exploratory output produced before C1 was fixed is likewise discarded. The promoted 2,414-endpoint / 187-pair / 9-link bootstrap certificate was generated only after the parity repair and independently red-teamed.

Classification: **scratch-only invalidation and clean rerun**.

## C3 — abandoned short-left lift enumeration

A naive route attempted endpoint lifts modulo `3^(z_left-1)` for short left plateaux. It was computationally intractable and interrupted. No partial output is trusted or promoted. The successful route instead solves the full bridge word modulo `3^(z_left+z_right)` and enumerates every lift in the finite state band.

Classification: **failed route / barrier, not a mathematical demotion**.

## C4 — red-team path repair during connector closeout

The Codex scratch red-team script referred to `.rl-work/RL327/verify_rl327_owned_excess_density.py`. In the connector fresh reconstruction that relative scratch path was absent, so the first invocation failed before executing the red-team checks. The closeout package replaces only that file-location lookup with a sibling-file lookup via `Path(__file__)`. The mathematical checks are unchanged. The repaired portable script passes in a clean unpack.

Classification: **mechanical packaging/path repair; no proof-state change**.

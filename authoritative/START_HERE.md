# Authoritative research entry point

Date: 2026-09-14
Incoming RL: RL317
Session type: ABSOLUTE DUAL-SHADOW `D0` OWNERSHIP ATTACK

## Read first

1. `AGENTS.md`
2. `docs/RL_RESEARCH_PROTOCOL.md`
3. `docs/RL_STATE_MACHINE.md`
4. `RL316_PROOF_LEDGER.md`
5. `RL316_RED_TEAM_REPORT.md`
6. `RL317_ABSOLUTE_DUAL_SHADOW_D0_OWNERSHIP_TARGET.md`
7. `sessions/RL316/RL316_CLOSEOUT.md` only when full frozen provenance is needed

Portable incoming regressions:

`python3 verification/verify_rl316_row_energy.py`

`python3 verification/verify_rl316_g2_dual_shadow.py`

The repository is authoritative. Conversation memory is not.

## Why RL317 has priority

RL316 closed the unsigned row-energy calculation and proved an exact dual
rational-shadow bracket for `g=2`.  The frozen RL21 witness saturates the
`X+Y` factor, envelope gap, and row-decoding coordinate while failing only the
absolute `X-Y` factor.

The highest-leverage remaining question is therefore whether genuine `D0`
ownership can consume the dual-shadow bracket without reverting to the old
simultaneous-factor statement.

## Frozen alternatives

Do not automatically resume unsigned row totals, `H`-only geometry, support
`3,4,5,...` grammar, fixed-96 P/Q, Radius 6+, H21, or raw Gate-A ancestry.

The `g=1` Bezout/ordinary-`+1` branch remains separate.

## Binding scope

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.
Lean formalisation is a separate project.
Knowledge catalogues are stale/deferred as of this freeze.

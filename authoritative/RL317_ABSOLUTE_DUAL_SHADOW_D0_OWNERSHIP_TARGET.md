# RL317 — absolute dual-shadow `D0` ownership target

Date prepared: 2026-09-14
Status: PREPARED, NOT STARTED
Session type: SUPPORT-INDEPENDENT ABSOLUTE-FACTOR ATTACK AFTER RL316

## Absolute objective

Continue toward proving that a positive non-trivial Collatz cycle cannot exist.

## Authoritative starting point

Read:

1. `AGENTS.md`
2. `docs/RL_RESEARCH_PROTOCOL.md`
3. `docs/RL_STATE_MACHINE.md`
4. `RL316_PROOF_LEDGER.md`
5. `RL316_RED_TEAM_REPORT.md`
6. `sessions/RL316/RL316_CLOSEOUT.md` when full proof detail is needed.

Treat the repository as authoritative.

## Exact inherited `g=2` object

For a genuine balanced return, put

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`.

Label the boundary states `R<x=R+G`.  Let `tau` and `sigma` be the rankwise
late and early envelope words, with numerators `q_tau,q_sigma`.  There is an
integer `epsilon>=0` such that

`q_tau=D0R+XG+epsilon`,

`q_sigma=D0R-YG-epsilon`.

The rational fixed states satisfy

`0<q_sigma/D0<R<x<q_tau/D0`,

with equal outer clearance and sum `R+x`.

The RL315 cofactor quotient is

`n=q_tau-D0R=XG+epsilon`,

and

`n+q_sigma=D0x`.

For fixed `tau`, `n mod X` uniquely determines the outgoing balanced row.

## Primary target

Prove a support-independent theorem of the form:

> Genuine absolute ownership `D0 | q_tau+q_sigma`, together with the exact
> dual-shadow bracket and integer path ownership, forbids a nonzero primitive
> `g=2` interface.

Equivalent acceptable outcomes:

- force `epsilon=0` and then force row repetition;
- force a bounded dual-shadow/interface certificate already excluded;
- reduce every survivor to a finite exact certificate independent of an
  unbounded support parameter;
- derive a new absolute-factor invariant that applies beyond `g=2`.

## First attack order

1. Use both equations `q_tau+q_sigma=D0(R+x)` and
   `n+q_sigma=D0x` simultaneously; do not treat either as local ownership.
2. Test whether positivity of the early shadow below `R`, combined with genuine
   integer path ownership, gives an order/product obstruction unavailable to a
   rational orbit.
3. Use `n mod X` row decoding together with `D0 | q_tau-n`; seek a bounded
   carry or quotient theorem involving both moduli `X` and `D0`.
4. If this collapses to the old simultaneous-factor equations, record the
   barrier precisely and independently replay the first reduced fibre with a
   portable exact verifier.

## Binding red teams

1. The late and early shadows are rational fixed orbits, not integer cycles.
2. `q_sigma/D0<R` is not by itself a contradiction to physical leastness.
3. The frozen RL21 `(65,41)` witness saturates the envelope gap, bracket, and
   `n=XG` lower edge while failing only `D0` ownership.
4. Unsigned row totals telescope to inherited numerator ownership.
5. `H | q_0-q_1` alone is insufficient.
6. Do not infer local denominator ownership.
7. Respect RL206 additive compatibility and RL233 finite-modulus barriers.
8. Do not promote the exploratory `a<=22` scan.
9. Do not silently promote RL315's unreplayed first-fibre/descent constants.
10. Keep `g=1` separate.
11. Do not replace the interface route with support-by-support grammar.

## Fallback

If the absolute-factor route hits a precise equivalence/barrier, independently
replay RL315's first reduced fibre:

- regenerate all constants from source;
- use a portable exact verifier;
- preserve contiguous range coverage and checksums;
- mark partial work NOT PROMOTED with exact gaps.

## Scope

RL316 is closed and frozen.
Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains separate.

# RL318 — non-homogeneous cross-content and ordered-row target

Date prepared: 2026-09-14
Status: PREPARED, NOT STARTED
Session type: ORDINARY-`+1` CONSUMER AFTER EXACT `T_h` REDUCTION

## Absolute objective

Continue toward proving that a positive non-trivial Collatz cycle cannot exist.

## Authoritative starting point

Read:

1. `AGENTS.md`
2. `docs/RL_RESEARCH_PROTOCOL.md`
3. `docs/RL_STATE_MACHINE.md`
4. `RL317_PROOF_LEDGER.md`
5. `RL317_RED_TEAM_REPORT.md`
6. `sessions/RL317/RL317_CLOSEOUT.md` when full proof detail is needed.

Treat the repository as authoritative.

## Exact inherited `g=2` dichotomy

With `X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`, the late/early shadow
composition has defect `epsilon>=0`.

Every least-state primitive `g=2` candidate lies in exactly one live branch:

1. **ordered-row branch:** `epsilon=0`, hence `tau=u`, `sigma=v`, with the two
   rows rankwise ordered but still distinct;
2. **cross-content branch:** `epsilon>0`, `H` does not divide `epsilon`. Put
   `d=gcd(H,epsilon)`, `h=H/d>1`, `E=epsilon/d`. The physical cycle scaled by
   `h` is a content-`h` `T_h` orbit at `hR,hx`; the shadow is a primitive
   coprime-content `T_h` orbit at `hR-E,hx+E`.

The cross-content branch also has complementary full-D remainders and a forced
integer wrong-bit phase decoded by `n mod X`.

## Primary target

Prove a genuinely non-homogeneous ordinary-`+1` theorem that eliminates at
least one branch and materially contracts the other. Acceptable strong forms:

- force `h=1` from the coupled content/coprime-content `T_h` pair;
- show the ordered rows must agree, contradicting primitivity;
- produce a support-independent bounded certificate covering both branches;
- derive an ordinary-increment invariant that extends beyond `g=2`.

## First attack order

1. Compare the content-`h` and coprime-content `T_h` trajectories at their
   first parity disagreement. Use the additive increment and exact symmetric
   gap `E`; do not normalize by `h`.
2. In the `epsilon=0` branch, combine rankwise row dominance with genuine
   `D0|U+V`, the physical state swap `R<x`, and integer parity ownership.
3. Test whether the two mismatch clocks and complementary full-D remainders
   force a bounded carry independent of support.
4. If no analytic consumer survives red team, use the certified first-fibre
   split: `g<=56` with `R<=710,220,447,737`, versus
   `57<=g<=9,355,556`, without enumerating word supports.

## Binding red teams

1. Standalone `T_h` moments, products, permutation identities, normalized
   rational states, and homogeneous invariants are the RL79 barrier.
2. A second `T_h` cycle is not itself a contradiction.
3. `epsilon=0` gives ordered rows, not row repetition; RL21 saturates this
   branch without `D0` ownership.
4. The neighboring-integer mismatch does not imply convergence or descent.
5. Do not infer local denominator ownership.
6. Respect RL206 additive compatibility and RL233 finite-modulus barriers.
7. Do not resume support-by-support grammar or the RL316 `a<=22` scan.
8. The first-fibre certificate bounds multiplicity and state but does not
   exclude a support.
9. RL315's distinct 19.67-billion run remains unpromoted and unnecessary.
10. Keep `g=1` separate.

## Certified fallback data

The first reduced fibre is `(a,ell)=(301994,190537)` with

`56theta<1<57theta`,

`R<=710,220,447,737` for `g<=56`,

`g<=9,355,556`,

and `R<=1,311,372,708,449` at the cap.

These are exact certificates under the inherited analytic and RL131 inputs.

## Scope

RL317 is closed and frozen.
Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains separate.

# RL315 — controlled-multiplicity full-D repeated-level target

Date prepared: 2026-09-13
Status: PREPARED, NOT STARTED
Session type: MATHEMATICAL EXECUTION AFTER RL314 WHOLE-PROGRAM AUDIT

## Absolute objective

Continue toward:

> Prove that a positive non-trivial Collatz cycle cannot exist.

RL315 is selected by the RL314 whole-program audit. It is not an automatic
continuation of the latest terminal-row route.

## Authoritative starting point

Read in order:

1. `AGENTS.md`
2. `docs/RL_RESEARCH_PROTOCOL.md`
3. `docs/RL_STATE_MACHINE.md`
4. `sessions/RL314/RL314_CLOSEOUT.md`
5. `sessions/RL314/RL314_AUDIT_REPORT.md`
6. `sessions/RL311/RL311_CLOSEOUT.md`
7. exact RL310/RL312/RL313 sources only as needed.

Treat the repository as authoritative.

## Exact inherited branch

In the active RL311 one-sided sector `lambda<3`, write

`A=ga`, `L=g ell`, `gcd(a,ell)=1`.

Let the canonical gcd-block imbalance levels be

`E_j = K_j-j ell`, `0<=j<g`.

RL311 proves

`0<=E_j<=h`

with

`h=ceil(log_3((4M+1)/(4R+1)))`,

and the exhaustive dichotomy:

- `g<=h+1`; or
- there is a proper pair of genuine full-cycle rotations at equal block level,
  separated by at most `h+1` reduced blocks, giving a genuine owned balanced
  return.

RL312/RL313 then supply strong consumers for the balanced-return branch.

Therefore the remaining complementary target is the controlled branch

`g<=h+1`.

## Primary target

Prove:

> In the RL311 `lambda<3` controlled branch, genuine full-D ownership forbids
> all proper gcd-block levels `E_0,...,E_(g-1)` from being distinct.

Equivalently, force

`E_j=E_k`

for some `0<=j<k<g`.

A repeated level gives an exact balanced segment with counts

`((k-j)a,(k-j)ell)`

between genuine full-cycle rotations.

This would remove the controlled branch and make the RL311 balanced-return
mechanism exhaustive throughout the one-sided sector.

## Why this target is parent-near

Success removes one of the two top-level RL311 branches.

It does not merely:
- improve a constant;
- deepen a finite grammar;
- exclude one support size;
- add another Bellman state;
- add another modulus.

It directly strengthens the global extractor.

## Required independent resource

A valid proof must use information beyond recurrence geometry alone.

Legitimate candidates include:
- global full-D divisibility/ownership of the genuine cycle rotations;
- integer quotient states `Q/D`;
- order-sensitive physical state information;
- a full-D geometric cofactor or global arithmetic relation that genuinely
  distinguishes ordinary Collatz ownership from rational cyclic countermodels;
- an independent physical packing resource in the same owned scale.

## Binding red teams

1. Do not infer local denominator ownership from global full-D ownership.
2. Do not revive RL20 whole-block coboundary cancellation.
3. Do not treat a recurrence/gauge normalization as an independent constraint.
4. Do not use the demoted global strip-width positivity claim.
5. Do not replace `g<=h+1` with another unbounded relation `g<=f(h)` and call it
   closure.
6. Do not equate canonical flow mass with optimal cyclic transport radius.
7. Do not resume support `3,4,5,...` terminal grammar.
8. Do not resume fixed-96 P/Q automatically.
9. Do not escalate to Radius 6+ without a proved encounter theorem.
10. Preserve the corrected RL314 terminal-spacing interpretation: the spacing
    lemma is valid, but the inherited `lambda<3` row-multiplicity restriction
    prevents the earlier over-optimistic arbitrary-`n` use.

## First attack order

1. Express distinct-level controlled configurations in an exact ownership-aware
   global form.
2. Ask whether full-D divisibility or quotient integrality forces a collision
   among the `g` levels.
3. Stress-test any proposed invariant against RL206/RL233 killed families and
   RL313 ownership-blind rational countermodels.
4. Only if the distinct-level theorem fails for a precise structural reason,
   pivot to the universal quotient route rather than adding another local
   grammar.

## Success ladder

Full/strong success:
- prove a repeated gcd-block level in every controlled survivor;
- or otherwise eliminate `g<=h+1` by a genuinely global full-D theorem.

Meaningful partial success:
- reduce the controlled branch to a genuinely finite exhaustion independent of
  unbounded `h`;
- produce an independent ownership constraint that removes an unbounded
  parameter.

Insufficient / pivot:
- another coordinate change;
- another recurrence identity;
- another finite-modulus residue;
- another fixed-depth grammar;
- another inequality with an unbounded right-hand scale;
- support-by-support terminal exclusion.

## Fallback ranking from RL314

If the primary route hits a precise barrier:

1. universal quotient / ordinary `+1` order-sensitive route;
2. RL312/RL313 balanced-return route only through a support-independent full-D
   theorem;
3. reduced RL305-RL308 Gate-A scalar front.

## Scope

RL314 is closed and frozen.
Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains separate.
Knowledge catalogues remain stale/deferred.

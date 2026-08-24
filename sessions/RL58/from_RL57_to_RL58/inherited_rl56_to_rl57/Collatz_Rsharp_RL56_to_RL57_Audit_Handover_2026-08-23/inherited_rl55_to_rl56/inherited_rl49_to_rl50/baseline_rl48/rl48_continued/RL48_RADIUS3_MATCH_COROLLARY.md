# RL48 continuation — exact radius-3 match point

Date: 2026-08-22

## Proven input from the current bundle

For every genuine retained one-excursion geometry, the full words have the form

`u=110 x 1 0^t`, `v=111 y 0^(t+1)`

and satisfy

`Q(u)-Q(v)=4(2^a+3^ell)`.

If the full phase condition holds, then there is a positive integer

`N=(Q(v)+4*3^ell)/(2^a-3^ell)`

such that the actual Collatz half-step trajectories obey

`N --u--> N+4`,

`N+4 --v--> N`.

In particular `N=3 (mod 8)`.  After the common leading `11` steps the two orbit values are separated by exactly `9`; the next local bits are `(0,1)`, and the RL coordinate is exactly `T=-14`.

## Conditional radius-3 closure corollary

Suppose the inherited audited radius-3 theorem has the following scope (or an equivalent formulation):

> a positive nontrivial Collatz cycle cannot contain a `4`-separated pair `N,N+4` in the canonical depth-three orientation `110... / 111...` (equivalently, the corresponding gap-9 local entrance is excluded by the radius-3 uniqueness theorem).

Then the live one-excursion full-phase RL branch is impossible immediately.

No low-area hypothesis `H<=t+2`, no resultant norm estimate, and no further same-root/subresultant lemma is needed for this implication.

## What must still be audited before promoting this to an unconditional closure

The exact RL18/RL19 radius-3 theorem statement is not in the RL47→RL48 archive.  Therefore one must check whether its actual hypotheses are exactly the canonical `4`-separated/depth-three pair above, or whether it additionally requires a sparse-support, orientation, gcd, boundary, or multiplicity hypothesis.

This is now a **provenance/hypothesis match problem**, not an algebraic phase-bridge problem.

If the theorem's input is the canonical radius-three pair itself, Gate B is closed.  If it is narrower, the only missing Gate-B lemma is the explicit implication from the pair above to those extra radius-3 hypotheses.

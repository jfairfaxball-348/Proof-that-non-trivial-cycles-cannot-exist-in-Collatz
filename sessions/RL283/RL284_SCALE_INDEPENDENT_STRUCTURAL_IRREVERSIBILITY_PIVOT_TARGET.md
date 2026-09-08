# RL284 — scale-independent structural / irreversibility exploratory pivot

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED

## Strategic status

RL284 is an **explicit exploratory strategic pivot**, prepared by direct user instruction.

It does **not** replace, demote, or discard the established Gate-A upstream programme.

The frozen Gate-A sufficient theorem remains:

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

Gate A remains open with exact residual:

`k>=25`, `k` odd, `H_can<k`.

If this pivot does not earn promotion through an actual theorem-sized advance, scalable reduction, or decisive barrier, recommend returning to that frozen upstream-reachability programme.

Gate B remains open/frozen. The fifth selector remains unscanned. Radius 6+ and unrelated research remain frozen unless RL284 proves a coupling that genuinely requires them.

## Purpose

Investigate whether non-trivial Collatz cycles can be excluded by a **scale-independent structural / irreversibility argument** rather than primarily by largest/smallest-number estimates.

The motivating closure principle is elementary:

- a closed cycle returns exactly to the same state;
- therefore every genuine state function has zero net change around the loop;
- but the dynamics may contain unavoidable asymmetric or irreversible events;
- if every non-trivial reduced traversal necessarily produces positive net structural increment while closure requires zero, one obtains an exact contradiction of the form

  `E_final=E_initial`

  and simultaneously

  `E_final>E_initial`.

"Energy" and "entropy" are analogies only. A viable candidate must be a precise mathematical invariant, cocycle, winding number, order, exact Lyapunov quantity, labelled-event structure, refinement measure, orientation datum, or other rigorously defined object with an exact transition law.

Do not merely rename a numerical size estimate "entropy".

## Primary parity / dissipation viewpoint

For an odd Collatz state `n`, write

`3n+1 = 2^a m`

with `m` odd. Then the accelerated odd-to-odd transition is

`n -> m = (3n+1)/2^a`

and

`a=nu_2(3n+1)`.

Investigate whether `a` has a useful exact interpretation as dissipation following an odd growth event.

The emphasis is qualitative/structural rather than absolute size.

Questions to attack:

1. Which exact events inject growth?
2. Which exact events dissipate it through powers of `2`?
3. Which events are genuinely neutral and should be quotiented out?
4. After quotienting neutral structures, can remaining events be canonically named, ordered, oriented, or ranked?
5. Is there a state function/cocycle whose transition increment is always nonnegative and is strictly positive somewhere on every non-trivial closed traversal?
6. Is there a cocycle whose exact total around a hypothetical cycle is forced nonzero while the recurrence forces total zero?
7. Can a distinguished event be forced to occur "after itself", acquire a strict successor label, reverse orientation, increase refinement, or create another impossible cyclic ordering?
8. Is there an acyclic labelled-event graph after neutral loops are quotiented?
9. Can the valuation `a` be decomposed into neutral compensation plus a strictly irreversible residue?
10. Does a sign-change or phase-change event carry an exact orientation/winding increment unavailable to neutral boundary dynamics?

## Explicit comparison with the earlier `n -> n+1` / encounter intuition

Revisit the earlier global encounter intuition only at the structural level.

Do not assume any unpublished encounter theorem.

Ask whether one can define a canonical marker/event so that traversing a non-trivial hypothetical cycle forces:

- a marker to have a strict successor;
- the successor eventually to be the original marker;
- but strict ordering to forbid cyclic closure.

Any such argument must identify the marker and the exact transition/order law. A verbal "something must increase" argument is insufficient.

## Prime-number overlay — critical, optional, disposable

Investigate whether prime structure adds deterministic leverage, but do so skeptically.

Except for `2`, primes are odd, and many composites share the same parity/valuation behavior. Do not assume primality is intrinsically special.

Test:

- whether prime states differ structurally from odd composites under accelerated Collatz;
- whether `(p-1)/3` predecessor structure gives useful residue or factor constraints;
- whether prime factorisation changes inverse-branch availability;
- whether multiplicative order, valuations of `3p+1`, or primes in arithmetic progressions yield exact cycle constraints;
- whether factorisation type, residue class, multiplicative order, or predecessor structure is the true useful object instead of primality;
- whether any prime claim survives replacing the prime by a composite in the same relevant residue classes.

If primes add no deterministic information beyond parity/valuation/factor structure, record that cleanly as a negative result and drop the prime overlay rather than forcing it.

## Structural proof architectures to prioritise

Prioritise exact scale-independent contradictions of these types:

- Lyapunov / entropy with an exact transition law;
- winding number / cocycle;
- impossible cyclic ordering;
- orientation/parity flip;
- unique-marker contradiction;
- irreversible information/refinement;
- labelled event graph becoming acyclic after neutral loops are quotiented;
- exact dissipation balance with a positive residual on every non-trivial closed traversal;
- topological or combinatorial first-return obstruction.

A useful quantity should ideally assign zero net change to already-known neutral loops rather than being immediately falsified by them.

## Mandatory stress tests from existing project mathematics

Use accumulated project results as structural input.

Every candidate should be tested against, as relevant:

- the trivial positive Collatz cycle;
- known negative and positive neutral boundary loops;
- RL279's neutral-loop families and boundary conjugacy;
- RL280/RL281 positive/negative excursion and sign-change gateway structure;
- RL282's exact local terminal families with arbitrarily long cheap boundary tails;
- parity-word and rank identities;
- canonical height and valuation structure;
- selector structure where already established;
- the proved Radius-4 local obstruction;
- RL283's high-divisibility/legality equivalence;
- RL283's adjacent-swap cancellation barrier;
- RL283's warning that aggregate zero-rank scalars may be dependent;
- RL283's strengthened noncrossing rank-relaxation barrier.

A proposed irreversibility quantity that is changed by a known neutral loop without compensating quotient structure is suspect and should be falsified early.

## Computation policy

Exact computation may be used for discovery and falsification.

Useful finite tests include:

- short exact Collatz trajectories;
- the trivial cycle;
- exact negative and positive neutral loops;
- sign-change gateways;
- positive checkpoint excursions;
- RL282 local-tail families;
- short canonical parity-word pairs;
- inverse-branch graphs;
- exact residue/factorisation classes.

Do not promote statistical tendencies, empirical average drift, random-orbit behavior, or "usually increases" claims as theorems.

Do not turn RL284 into a larger raw-height enumeration programme.

## What counts as a successful RL284 checkpoint

Work until one meaningful outcome is reached:

1. a concrete mathematically defined irreversibility / cocycle / event-ordering candidate survives serious falsification and has a plausible proof route; or
2. a precise parity-dissipation / prime-factor structural theorem is proved; or
3. primes are shown to add no deterministic leverage but the parity/irreversibility architecture remains viable; or
4. the pivot encounters a decisive barrier, which must be preserved cleanly and followed by a recommendation to return to the frozen Gate-A upstream-reachability programme.

Do not stop on a slogan, analogy, tiny numerical tendency, or merely renamed existing bound.

## Promotion discipline

This pivot is exploratory.

Do **not** let it overwrite the established Gate-A route unless it earns promotion through:

- an actual theorem-sized advance;
- a scalable structural reduction;
- or a decisive barrier that materially changes strategy.

If the outcome is only interesting intuition, preserve it as unpromoted scratch and return to the established programme.

## Explicit frozen fallback

The fallback route remains the RL283 target:

`globally reachable positive even d=1 checkpoint (J,H)
 => nu_2(J)<=H`.

The current evidence and barriers around that theorem are frozen in:

`sessions/RL283/RL283_UPSTREAM_2ADIC_EQUIVALENCE_AND_RELAXATION_BARRIERS_2026-09-08.md`.

Do not reinterpret RL284 as evidence that the Gate-A route has failed mathematically. RL283 found proof-method barriers, not a counterexample to the theorem.

## Forbidden scope drift

Unless a new proved coupling genuinely requires it, do not:

- merge Gate B into this pivot;
- scan the fifth selector;
- start Radius 6+;
- reopen unrelated historical branches;
- classify all Collatz cycles in a way that presupposes the desired result;
- use largest/smallest-number estimates merely under new terminology;
- promote empirical entropy/drift as exact mathematics.

RL284 starts only on a fresh kickoff after RL283 promotion.

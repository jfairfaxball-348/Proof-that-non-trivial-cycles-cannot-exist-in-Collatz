# RL285 — return to upstream 2-adic checkpoint reachability for Gate A

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED

## Incoming classification

RL284 closed as

`LABELLED_ACCELERATED_REVERSIBILITY_AND_LOCAL_IRREVERSIBILITY_BARRIERS_PROVED`

with subordinate results:

- `ACCELERATED_ODD_LABELLED_BIJECTION_PROVED`;
- `ADMISSIBLE_PREDECESSOR_RAY_PROVED`;
- `LOCAL_PRIMALITY_BRANCH_INDIFFERENCE_PROVED`;
- `MOD3_ORIENTATION_ACYCLICITY_BARRIER_PROVED`;
- `VALUATION_ONLY_CYCLE_CHARGE_BARRIER_PROVED`.

RL284 was an explicit exploratory pivot. It did not close Gate A and did not demote the established Gate-A route.

Its decisive conclusion is that the natural local “dissipation/entropy” mechanism does not provide an independent closure route:

- the accelerated odd map is exactly reversible once the valuation label `a=nu_2(3n+1)` is retained;
- admissible inverse branches form the residue-controlled affine ray `P_(a+2)=4P_a+1`;
- primality does not alter this local branch structure;
- mod-3 orientation is cyclic rather than acyclic;
- valuation-only additive charges are forced neutral on `a=1,2,4` by exact known cycles.

Therefore RL285 returns to the frozen Gate-A upstream programme.

## Exact inherited Gate-A state

Gate A remains open at terminal `d=1, J=2^k` with target `H_can>=k`.

The exact residual is

`k>=25`, `k` odd, `H_can<k`.

The preferred sufficient theorem remains

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

At a terminal `J=2^k`, this gives `k<=H`.

The RL282 exact `H<=22` certificate and all inherited contractions remain authoritative. RL283's bounded terminal regression remains evidence only.

## Required RL283 barriers to preserve

RL283 proved:

1. `J<=2^H` is false.
2. Local `nu_2` monotonicity is false.
3. A single ordered-rank displacement can raise the cleared-numerator valuation from `1` to `13`, so per-cell valuation-Lipschitz induction is false.
4. Integerized zero-rank 2-adic structure is the inherited `B` telescope in disguise, not an independent scalar.
5. High final divisibility in the ordered-rank formulation reconstructs prefix legality; the dangerous relaxation is equivalent to genuine reachability.
6. Strict noncrossing order does not rescue the old separable large-rank relaxation.

RL284 adds that local labelled reversibility, residue orientation, primality, and valuation-only entropy do not bypass these global reachability barriers.

## Mission

Attack directly:

`globally reachable positive even d=1 checkpoint (J,H)
 => nu_2(J)<=H`.

The key word is **globally reachable**. Local endpoint algebra alone is already known to admit dangerous-looking configurations.

Preferred order:

1. Work from the exact `(d,J,H)` transition system and the positive-checkpoint/excursion compression already proved in RL279–RL282.
2. Seek the minimal state augmentation that records enough upstream history to control final `2`-adic divisibility without reverting to the full raw path.
3. Exploit the distinction between locally legal terminal blocks and globally reachable checkpoint states established in RL282.
4. Use RL283's high-divisibility-implies-prefix-legality theorem positively: test proposed global invariants on exact prefixes rather than on misleading algebraic relaxations.
5. Treat the finite `H<=22` checkpoint certificate and bounded terminal regressions as discovery/falsification evidence only unless a new gap-free certificate is explicitly proved.
6. Seek either a proof of `nu_2(J)<=H`, an equivalent terminal theorem implying `H_can>=k`, or the strongest correct new global-reachability invariant materially contracting the residual.

## Structural leads still in scope

Potentially useful inherited exact structure includes:

- `K=J+2^d-1` run compression;
- positive-checkpoint potential `F=Q(J+3)`;
- positive/negative excursion mass budgets;
- one-zero valuation law;
- mod-3 reachability invariant;
- terminal-backward height-digit pricing;
- exact positive-checkpoint automaton data through `H<=22`;
- RL283 two-shadow affine representation and prefix-legality reconstruction.

Use these only where they give genuinely independent leverage. Do not double-count dependent endpoint telescopes.

## Forbidden repeats / scope

Do not:

- continue RL284 entropy/irreversibility exploration unless a genuinely new global coupling appears;
- force a prime-number overlay;
- restart `J<=2^H`;
- assume local `nu_2` monotonicity;
- revive per-cell rank valuation-Lipschitz induction;
- treat dependent zero-rank scalars as independent invariants;
- use the ordered-rank endpoint re-encoding as if it were an easier relaxation;
- make larger raw height-cap enumeration the principal route;
- merge Gate B into Gate A without a new proved coupling;
- scan the fifth selector;
- start Radius 6+.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

RL285 starts only on a fresh kickoff after RL284 promotion.

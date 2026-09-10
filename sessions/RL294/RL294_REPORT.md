# RL294 — canonical cascade algebra, all-depth checkpoint-2 domination, and owner-route contraction

Date: 2026-09-10

Primary classification:

`CANONICAL_CASCADE_ALGEBRA_AND_ALL_DEPTH_CHECKPOINT2_TO_P_BELLMAN_DOMINATION_PROVED`

Gate A remains open with exact authoritative residual

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and disposition

RL294 inherited RL293's exact first-d=1 P-owner certificate through historical height 60, conditional five-state Bellman-front-door reduction to P, principal-cylinder/high-signed-drift restriction for a dangerous first checkpoint, and exact residual `k>=31`.

The intended strongest target was the all-depth theorem

`m_P(B)<=H(B)-1`

for every genuine first positive `d=1` state B, followed by `Bcal(P)<=1`.

RL294 does not prove either statement. Instead it discovers and proves an exact cascade algebra for canonical states, promotes an all-depth Bellman domination theorem for checkpoint `2` by P, proves several exact factorisations and tower identities, and isolates a more concrete successor obstruction: wall refactorisation of an ordered cascade when one factor enters the formal rejected `d=0` tube.

The more aggressive `(4,39)` and P×P cascade contractions developed during the session are preserved in `RL294_SCRATCH_FREEZE.md` as unpromoted successor work.

## 2. Dual autonomous endpoint coordinates

Write

`K=J+2^d-1`,
`N=K+1=J+2^d`,
`T=K+1-3^d=J+2^d-3^d`.

Define the one-dimensional integer map

`G(z)=z/2` for even z,
`G(z)=(3z-1)/2` for odd z.

Then every legal canonical transition satisfies exactly:

- if the external bit is `x=0`, then `T'=G(T)`;
- if the external bit is `x=1`, then `N'=G(N)`.

The depth records the parity event. For `x=0`, odd T raises depth and even T preserves it. For `x=1`, even N lowers depth and odd N preserves it.

Equivalently, the physical state can be viewed as an interval

`[T,N]`

of exact length `3^d`. A `0` step evolves the left endpoint autonomously under G; a `1` step evolves the right endpoint autonomously under G.

Classification:

`DUAL_AUTONOMOUS_ENDPOINT_G_COORDINATES_PROVED`.

This is an exact reorganisation of RL288's corrected T recurrences, not a new local potential and not a Gate-A theorem.

## 3. Unified column recurrence

Let one canonical paired column have input bit x and output bit y. Then

`d'=d+y-x`

and the four canonical K recurrences unify to

`boxed: 2K' = 3^y K + (1-x)3^(d+y) - (1-y)`.

This identity is valid exactly for every legal column and will be the algebraic basis for the cascade law below.

## 4. Associative canonical cascade product

For formal/canonical K-states

`A=(a,K_A)`, `B=(b,K_B)`

define

`A o B = (a+b, 3^b K_A + K_B)`.

The product is associative.

Suppose A receives column `x->y` and B receives the propagated column `y->z`. Whenever both factor transitions are legal positive-depth transitions,

`boxed: (A o B)' = A' o B'`.

This follows directly from the unified column recurrence. The output z is automatically the canonical output of the composite because parity is multiplicative/additive mod 2:

`K_(A o B) == K_A + K_B (mod 2)`.

For an m-factor cascade over L synchronized columns, depth additivity gives the exact area ledger

`boxed: DeltaH_composite = sum_i DeltaH_i + (m-1)L`.

Classification:

`CANONICAL_CASCADE_SEMIDIRECT_PRODUCT_AND_AREA_LEDGER_PROVED`.

The product is an algebraic decomposition of physical recurrence. It does not assert that every chosen formal factor remains positive-depth legal forever.

## 5. Exact factorisation of the RL292 front door

Let `B_J=(1,J)` denote a depth-one state, expressed in K-coordinate by `K=J+1`. Let

`P=(2,J=3,K=6)`,
`R3=(2,J=-3,K=0)`,
`R6=(2,J=-6,K=-3)`.

Then the RL292 difficult positive front-door state factors exactly as

`(4,39)=P o R3`.

The other non-P RL292 front-door states also factor exactly:

`(2,-17)=B_-4 o B_-6`,
`(2,-84)=B_-19 o B_-28`,
`(3,-28)=B_-4 o P = R6 o B_-13`.

Thus the five-state front door is algebraically built from P and the already distinguished fixed-seed boundary/departure states rather than five unrelated K-states.

Classification:

`RL292_FRONT_DOOR_EXACT_CASCADE_FACTORISATION_PROVED`.

Important scope: these identities do not by themselves imply any Bellman inequality between the factors.

## 6. Z/E formal wall transducer

Define

`Z=(1,K=0)`,
`E=(1,K=1)`,
`I=(0,K=0)`.

Then `R3=Z o Z`.

The exact propagated one-column rules are

`Z --1--> Z`,
`Z --0--> E`,
`E --0--> P`,
`E --1--> I`.

The last edge is formal: at depth one it is precisely the illegal/rejected descent to depth zero. It must not be treated as a legal canonical edge.

This tiny transducer explains why the new cascade representation naturally encounters RL289's rejected-tube object at component walls. The formal identity I is compositionally neutral and must be quotiented rather than charged as a physical history state.

Classification:

`Z_E_FORMAL_WALL_TRANSDUCER_PROVED`.

## 7. All-depth checkpoint-2 domination by P

Let checkpoint `2` mean `(d,J,K)=(1,2,3)`. Its only legal first step is the zero-cost launch to

`R_2=(2,K=3^2)`.

More generally put

`R_d=(d,K=3^d)`

and

`S_d=(d-1,K=(3^d-1)/2)`.

At `R_d`:

- `x=0` sends `R_d` to `R_(d+1)`;
- `x=1` sends `R_d` to `S_d`.

Therefore every nonempty checkpoint-ending future from checkpoint 2 has a unique first tower departure at some `S_d`, `d>=2`. The source-2 cost to `S_d` is exactly

`C_2(d)=d(d-1)/2`.

From P the explicit word

`1 0^(d-2) 1`

reaches the identical physical state `S_d` at exact cost

`C_P(d)=d(d-1)/2+1=C_2(d)+1`.

Copying the unchanged future suffix from that identical state gives, for every nonempty checkpoint-ending future,

`hazard_from_2 <= Bcal(P)+1`.

The empty checkpoint-2 future has hazard `nu_2(2)=1`. P reaches checkpoint `8` by word `1111` at added cost 2, so `Bcal(P)>=3-2=1`, and the empty case is also covered.

Hence globally, with no height cap,

`boxed: Bcal(1,2) <= Bcal(P)+1`.

Classification:

`CHECKPOINT2_ALL_DEPTH_BELLMAN_DOMINATED_BY_P_PLUS_ONE_PROVED`.

This is a genuine all-depth strengthening of RL293's sharper but cost-29-bounded comparison of checkpoint 2 with checkpoint 8.

## 8. Exact all-depth checkpoint-8 path to the S_d tower

For every `d>=3`, checkpoint `8` has the explicit path

`0 (10)^(d-3) 0`

to the same `S_d` state, with exact cost

`(d-2)^2`.

Thus the comparison with checkpoint 2 is

`C_2(d)-(d-2)^2 = (-d^2+7d-8)/2`.

It is positive for `d=3,4,5` and reverses from `d=6`. This explains analytically why the strict checkpoint-8-over-checkpoint-2 domination used by RL293 is naturally a low-depth phenomenon rather than an obvious all-depth theorem.

Classification:

`CHECKPOINT8_TO_S_D_EXPLICIT_ALL_DEPTH_PATH_FORMULA_PROVED`.

## 9. Exact aligned base-9 carry system and scalar-correction barrier

For the two-level scale-lift geometry write

`K=9A+r`

using the unique even representative

`r in {0,2,4,6,8,10,12,14,16}`.

Then K and A have the same parity. After a common column with output bit y, write

`s=(r+8)/2` if `y=0`,
`s=3r/2` if `y=1`.

There is a unique decomposition

`s=r'+9c`

with r' again in the even representative set. The carry c stays in a finite small set.

A scalar correction depending only on r cannot absorb the carry into an ordinary canonical quotient. If `g(r)` existed, the correction equations would be

`c+g(r')=g(r)/2` for `y=0`,
`c+g(r')=3g(r)/2` for `y=1`.

But the four exact transitions

`0 --(y=1,c=0)--> 0`,
`0 --(y=0,c=0)--> 4`,
`4 --(y=1,c=0)--> 6`,
`6 --(y=1,c=1)--> 0`

force successively

`g(0)=g(4)=g(6)=0`

and then `1=0`.

Therefore the scale-lift carry cannot be replaced by a residue-only scalar endpoint potential.

Classification:

`BASE9_ALIGNED_FINITE_CARRY_AND_RESIDUE_ONLY_SCALAR_CORRECTION_BARRIER_PROVED`.

This is consistent with RL289/RL290's merger/gauge barriers and is not a new competing scalar-potential programme.

## 10. Wall interpretation and limitation

The cascade area identity does not by itself pay the full depth of a formal rejected tube. If one factor sits at formal depth zero for k-1 columns, its signed area contributes `-(k-1)`, while the composition cross-term contributes one unit per synchronized column. These terms can cancel to constant scale.

Thus the tempting theorem "cascade cross-term automatically pays rejected-tube depth" is false.

The correct residual problem is a wall-refactorisation/min-plus problem: when one component reaches depth zero with nonzero K, its formal evolution is exactly the rejected-tube phase of RL289; the neighboring positive-depth factor is what keeps the composite legal. A scalable proof must transfer or price that tube debt under refactorisation rather than ignore it.

Classification:

`CASCADE_CROSS_TERM_ALONE_DOES_NOT_PRICE_REJECTED_TUBE_DEPTH_BARRIER`.

## 11. Unpromoted positive route developed in RL294

The following work is preserved for RL295 but is not promoted as theorem in RL294:

1. T-coordinate owner geometry:
   - P has an exact `T=-2` tower;
   - the `(4,39)` all-zero spine reaches the same tower at `(6,663)`;
   - first-x1 exits give a finite cut, with several exits immediately P-owned.

2. P-avoidance exploration:
   - no undominated positive first-d=1 arrival appeared in the exact pruned exploratory trees examined through large historical costs;
   - apparent late escapes moved outward when the P-owner oracle cap increased;
   - these were oracle-cap effects, not owner-theorem counterexamples.

3. Corrected large example:
   - first boundary state `J=76611` on a long R6/P-avoidance history is strongly P-owned;
   - exploratory minimum P cost found was 25, superseding an earlier scratch value 26.

4. Hard `(4,39)` cascade contraction:
   - using `(4,39)=P o R3`, output-controlled factor analysis appears to reduce all non-exceptional futures to direct P ownership;
   - the surviving exceptional prefix is `00`, reaching `(5,191)` at source cost 6;
   - this reduction was not independently packaged to theorem standard during RL294 and remains unpromoted.

5. `(5,191)` / P×P continuation:
   - `(5,191)=(3,K=24) o P`;
   - exploratory first-output analysis isolates the states `(5,201)`, `(6,733)`, `(6,949)`, `(6,1273)` plus branches already P-owned or entering an eventually repeating coefficient tail;
   - the claimed finite preperiod/tail domination still requires a clean all-depth proof.

6. P×P finite falsification:
   - a large exploratory closure of `P o P=(4,45)` found no threatening finite counterexample in the tested range;
   - this is evidence only and is not used in any promoted theorem.

These are the principal momentum-bearing objects for RL295.

## 12. Relation to earlier promoted structure

RL294's cascade formulation does not supersede the static boundary danger tree.

RL289 proves that checkpoint valuation equals complete adjacent rejected-`d=0` tube depth. RL292/RL293 prove that arbitrary boundary danger has an exact static preimage-tree representation and that danger balls pull back isometrically through fixed legal segments. The cascade wall is precisely where this existing object reappears.

Likewise, RL279's all-one K-run compression remains useful inside cascade factors, and RL281's two-phase mass/height theorems remain valid auxiliary global constraints. No old theorem is demoted.

## 13. Proof state after RL294

Promoted analytic mathematics:

- dual autonomous G coordinate theorem;
- unified canonical column recurrence;
- associative cascade product and exact area ledger;
- exact factorisation of all non-P RL292 front-door states;
- Z/E formal wall transducer with explicit legality qualification;
- all-depth `Bcal(2)<=Bcal(P)+1`;
- all-depth checkpoint-8 explicit path to `S_d`;
- finite aligned base-9 carry system and residue-only scalar-correction impossibility;
- cascade-cross-term rejected-tube pricing barrier.

Not proved:

- all-depth first-positive first-d=1 P-owner theorem;
- `(4,39)` all-depth P-owner/Bellman domination;
- complete wall-refactorisation theorem;
- five-state front-door collapse to P;
- `Bcal(P)<=1`;
- full static danger-ball separation;
- any `k>=31` contraction;
- Gate A;
- Gate B, fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

The exact Gate-A residual therefore remains

`k>=31`, `k` odd, `H_can<k`.

## 14. Successor direction

RL295 should make the wall-refactorisation problem explicit and finite.

Primary attack:

1. independently prove or reject the unpromoted `(4,39)->(5,191)` cascade cut;
2. represent the surviving P×P/cascade preperiod by an ordered finite factor state plus formal `d=0` tube debt;
3. quotient identity factors immediately;
4. prove that every delayed departure in the eventual coefficient tail is P-dominated, leaving only a finite set of wall sectors;
5. use the new all-depth checkpoint-2-to-P theorem as a sink wherever a wall returns to checkpoint 2;
6. if `(4,39)` closes, apply the same exact cascade rules to `(2,-17)`, `(2,-84)`, `(3,-28)`;
7. only after the front door has collapsed should the tight `Bcal(P)<=1` principal-cylinder/static-danger-tree attack become primary.

Do not replace this with a raw H-cap or P-cone expansion.

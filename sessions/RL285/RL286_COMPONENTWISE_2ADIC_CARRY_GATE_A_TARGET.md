# RL286 — componentwise 2-adic carry budget for Gate A

Date prepared: 2026-09-09
Status: PREPARED, NOT STARTED

## Incoming classification

RL285 closed as

`GLOBAL_PREFIX_2ADIC_REFORMULATION_AND_FIRST_CARRY_BRIDGES_PROVED`.

RL285 did **not** close Gate A. It proved exact global-prefix/carry reformulations, a first-carry bridge to the first genuine excursion, and an exact finite `H<=22` all-raw-state certificate for the post-column candidate.

## Exact inherited Gate-A state

Gate A remains open at terminal `d=1,J=2^k` with target `H_can>=k`.

Exact residual:

`k>=25`, `k` odd, `H_can<k`.

The checkpoint theorem remains

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

RL285 introduced the exact all-depth formulation

`K=J+2^d-1`, `A=H+d-1`,

with conjectural global inequality

`nu_2(K-1)<=A`.

At `d=1` this is exactly the checkpoint theorem.

## Frozen RL285 bridges

Treat the following as established:

1. `A=H+d-1` is post-column depth area and equals prefix-dominance/rank displacement area, with unmatched ranks placed virtually at the endpoint.
2. Shifted shadows `W_empty=-6`, `W_{w0}=W_w+2^n`, `W_{w1}=3W_w` satisfy
   `2^n(K-1)=3^d W_x-W_y-2^n`.
3. Dangerous high divisibility plus prefix dominance reconstructs full canonical prefix legality.
4. A positive high-divisibility formal pair therefore reconstructs a genuine positive canonical violation.
5. The exact `H<=22` raw closure has 584,154 positive states and zero violations of `nu_2(K-1)<=H+d-1`; this is finite certificate only.
6. Ferrers-cell displacement gives
   `W_x-W_y=sum cells 2^p 3^s`.
7. The first displaced rank has rigid valuation
   `nu_2(W_x-W_y)=b_*`.
8. Endpoint divisibility then reconstructs the first legal off-boundary `01` ascent from an even `d=1` boundary state.
9. The terminal extension to `J=2` has signed area exactly `H-k`.

## Required barriers/corrections

Preserve all RL283 barriers and these RL285 additions:

- the scratch claim `nu_2(J)<=H-d+1` is false and must not be revived;
- `nu_2(K-1)<=H+d-1` is not locally inductive on arbitrary locally legal states;
- all four first-entrance branch congruences admit residue-admissible fake parents;
- shifted-shadow sign is the inherited zero-mass threshold in disguise;
- final scalar shadow/zero-mass data do not close Gate A;
- iterated per-cell carry peeling reconstructs the existing excursion decomposition and does not supply a per-cell valuation Lipschitz bound.

## Mission

Attack the missing global theorem at the level of **whole positive excursion components**.

Preferred target:

Find a componentwise state/carry budget `G` such that

- it is exactly closed under arbitrary zero-height positive boundary retention;
- for each genuine positive first-return excursion of added height `h`, its dangerous 2-adic carry capacity increases by at most `h` (or another proved quantity summing to `H`);
- terminal `J=2^k` forces carry demand at least `k`.

Equivalent acceptable outcomes:

1. prove `nu_2(K-1)<=H+d-1` globally;
2. prove the positive high-divisibility sign theorem in the prefix-dominant word formulation;
3. prove a componentwise theorem that directly implies `nu_2(J)<=H` at `d=1` checkpoints;
4. obtain a new exact structural invariant that materially contracts the residual without relying on larger raw enumeration.

## Preferred order

1. Condition on the first-carry theorem: the first mismatch is already a genuine excursion entry.
2. Compress the next portion as one exact first-return excursion, rather than peeling individual displacement cells.
3. Use the inherited RL280/RL281 excursion mass/state inequalities and exact boundary quotient to control the odd quotient/carry passed to the next component.
4. Seek a recursive carry budget over components that survives zero-height boundary loops parametrically.
5. Use the all-depth `K-1` formulation as a falsification target, not as an assumed invariant.

## Forbidden repeats / scope

Do not:

- promote the global post-column inequality from its `H<=22` finite certificate;
- restart local `nu_2` monotonicity or per-cell valuation-Lipschitz induction;
- replace component structure with a fixed finite shifted-valuation table;
- treat shifted shadows or zero-mass telescopes as independent scalar invariants;
- use endpoint-only relaxed rank data as if it retained canonical prefix legality;
- make a larger height-cap search the principal route;
- revive RL284 local entropy/primality exploration;
- merge Gate B into Gate A;
- scan the fifth selector;
- start Radius 6+.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

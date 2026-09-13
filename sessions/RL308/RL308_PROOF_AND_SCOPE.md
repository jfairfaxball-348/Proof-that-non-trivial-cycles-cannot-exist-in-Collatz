# RL308 proof and scope ledger

Date: 2026-09-13
Classification: `X_FIXED_RESIDUE_COMPLETE_PREFIX_CUT_TO_TWO_RESIDUALS_PROVED_AND_CURRENT_LOCAL_PROGRAMME_FROZEN_FOR_GLOBAL_MECHANICS_REVIEW`

## Promoted result P1 — complete conditional X dependency reduction

Let `X=(4,43)`.

Conditional on the inherited open obligation

`Bcal(2,-17)<=1`,

the twelve words

`010,011,100,101,110,111,0010,0011,00001,00011,00000,00010`

form a complete prefix-free cut of the legal binary future tree from X.

The ten non-residual leaves are exactly same-state owned from `(2,-17)` with X-branch Bellman bounds

`11,6,8,8,7,6,8,5,8,7`

in the displayed word order.

The residual leaves are

`00000 -> (7,2039)` at X cost 20,
`00010 -> (7,2546)` at X cost 20.

No proper internal cut node is a positive-even depth-one checkpoint.

Therefore

`Bcal(X) <= max(11, Bcal(7,2039)-20, Bcal(7,2546)-20)`

conditional on `Bcal(2,-17)<=1`.

Consequently

`Bcal(7,2039)<=31`
and
`Bcal(7,2546)<=31`

are sufficient, together with `Bcal(2,-17)<=1`, for `Bcal(X)<=11`.

Classification: exact finite certificate plus exact Bellman same-state splice.

## Exact finite certificate

The closeout verifier checks:

- all twelve X leaf endpoints and costs;
- all ten exact `(2,-17)` owner words and costs;
- all ten resulting branch bounds;
- pairwise prefix-freeness;
- Kraft sum exactly one;
- absence of a positive-even `d=1` checkpoint at every proper internal node;
- the two residual states and costs.

## Supporting exact identities, not closure claims

The following exact identities are preserved as scratch:

`8:011010 -> (2,19)` cost 4;
`X:11101 -> (2,19)` cost 11;

`X:1110111 -> (1,15)` cost 13;
`Y:1111111100 -> (1,15)` cost 19.

No forced-cylinder theorem is claimed.

## Supporting finite evidence, not promoted

Divisibility-shell minimum costs for k=6..13 were observed as:

- source 8: `9,10,11,12,13,13,15,15`;
- X: `16,17,18,19,20,20,22,22`;
- Y: `22,23,24,25,26,26,28,28`.

The excluded-prefix scan for X without `11101` was incomplete because the 1,000,000-state cap was reached. It is not a finite certificate.

## Method barriers / failed routes

1. `phi(d,J)=ceil(log2(K+1))+d` is not a Bellman dual: `(1,2) --0,cost0--> (2,6)` raises phi by 2.
2. A direct Y-by-X state-owner grammar proliferated; at depth 15 the attempted cut still had 11,459 unresolved states after only 310 were certified safe. No decreasing measure was found, so it is not promoted.
3. Finite coincidence of shortest high-valuation witnesses with the `(2,19)` / `(1,15)` common-state cylinders does not prove all dangerous futures enter those cylinders.

## Corrections / demotions

None.

No inherited theorem is invalidated.

## Explicit non-claims

RL308 does not prove:

- either residual `<=31` ceiling;
- `Bcal(X)<=11`;
- `Bcal(Y)<=12`;
- `Bcal(2,-17)<=1`;
- `Bcal(4,39)<=3`;
- `Bcal(2,-84)<=2`;
- `Bcal(3,-28)<=3`;
- `Bcal(8)<=3`;
- `Bcal(P)<=1`;
- Gate A;
- Gate B;
- O1/O2/P8;
- any global non-trivial-cycle exclusion.

## Strategic freeze

The Bellman/scalar programme remains mathematically live but loses automatic successor priority.

RL309 is a planning-only global architecture review. The frozen RL308 frontier may be resumed later only if the redesigned roadmap assigns it global priority.

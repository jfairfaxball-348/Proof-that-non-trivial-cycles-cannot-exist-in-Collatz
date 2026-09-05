# RL258 — k=31 two-flank canonical compatibility target

Date prepared: 2026-09-05  
Status: **PREPARED, NOT STARTED**

## Incoming exact state

At the unique first halving selector

`(a,ell,z,q,r,H_sel,n)=(1100,694,406,317,200,14,4)`

RL257 eliminates `k=33`.

Therefore the only remaining first-frontier terminal exponent is

`boxed: k=31}`.

Retain:

- `E_31<=27`;
- exact word form `u=110 x 1 0^28`;
- exact internal start `(d,J)=(1,-13)`;
- exact internal terminal boundary `(d,J)=(1,2^31)` before the omitted
  terminal `(1,0)`;
- first nine internal `x` bits: 199 legal possibilities and weighted right
  zero cost at least 11;
- exactly two right prefixes attain cost 11:
  `110110111`, `110111010`;
- final ten internal `x` bits have weighted left zero budget at most 16,
  hence at most five zeros;
- 141 universal left ten-bit x-patterns satisfy that budget;
- 3064 right/left flank x-pattern pairs satisfy `E_31<=27`;
- 2719 survive the exact complement isolated-root capacity test.

## Binding notation/indexing discipline

Use `H_sel` for `19z-7a=14`.

Use a separate symbol such as `H_can` for RL45/RL64 accumulated canonical
area. Do not identify them unless a new proof explicitly derives the equality.

The canonical terminal state `J=2^31` is at the end of the internal `x,y`
path, before the omitted terminal `(1,0)`.

## Primary target

1. For each left ten-bit `x` suffix admitted by the RL257 budget/capacity
   family, run the exact RL45/RL64 inverse transition from
   `(d,J)=(1,2^31)` and retain all legal predecessor `(d,J,y)` states.
2. Couple those terminal predecessor states to the canonically legal right
   nine-bit prefix states.
3. Use the exact internal length/weight data
   `m=a-k-1=1068`, `wt(x)=wt(y)=ell-3=691`,
   together with height positivity, full-phase extendability, q-window
   derivative/support data, and any safely inherited phase/rank identities.
4. Eliminate the finite family analytically or with a complete exact
   reproducible certificate. If it cannot be eliminated, contract it to the
   smallest explicit owned state family that can be handed forward.

Do not use relaxed MILP infeasibility as proof. Do not convert a local pattern
to Radius 4 without every audited primitive/full-D/exact-distance hypothesis.

Gate A open. Gate B open. Radius 4 not invoked. Radius 5 inactive.

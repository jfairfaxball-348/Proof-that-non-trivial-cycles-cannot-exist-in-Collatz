# RL270 mandatory red team

Date: 2026-09-07

## Structural completeness

- The certificate does not enumerate arbitrary raw five-gap words.
- It proves `X_t=sum_{j=0}^{L-1}H_(t+j)` from the determinant-one reconstruction equation.
- Singleton topology forces ten distinct boundary events.
- Binary reconstruction is equivalent to cyclic sign alternation of those ten events.
- The fixed `L` pairing is order-preserving around the cycle.
- Solving the positive boundary-gap equations leaves exactly four anchored cyclic families; no reflection quotient is used.

## Small direct-word replay

Independent exhaustive replay through `A<=18` reproduces:
- 8,996 `|kappa|=1` `[1,1,1,1,1]` instances;
- 4,498 / 4,498 orientation split;
- family split `3522 / 718 / 204 / 54` in both orientations;
- zero unclassified singleton matching patterns;
- zero full-`D` hits.

## Cut, wrap and numerator indices

For every `kappa=+1` small replay instance the word is cut at an actual positive singleton with preceding zero flow. The direct edge formula, reconstructed flow, cyclic `L`-window reconstruction and sparse polynomial agree modulo the complete `D`. Sparse-polynomial mismatches: **0**.

## Orientation

Every `kappa=-1` instance is replayed by exact source/target reversal: `y=rotate(x,m)`, `m'=A-m`. The resulting flow has `kappa=+1`, the numerator difference changes sign, and all 4,498 negative-orientation cases classify into the same four-family split. Orientation mismatches: **0**.

## Full D versus proper factors

- Every certificate hit test uses the complete positive `D=2^A-3^L`.
- No factor sieve is promoted as theorem evidence.
- The small replay has **714** proper-factor-only instances but **0** full-`D` hits.

## Negative domain

The permanent sentinel `A=11,L=7,D=-139,Q=18904` is retained and remains outside the theorem's `D>1` scope.

## Primitivity

No primitivity filter is used in the complete finite certificate. Therefore any nonprimitive structural candidate inside the positive determinant-one finite domain is tested rather than discarded.

## Complete finite replay

The self-contained certificate regenerates the inherited 2,234 determinant pairs, reproduces all four structural totals, and checks all exact meet-in-the-middle residue tables. It examines **14,539,631** side residues and finds **0** valid full-`D` matches.

Mandatory red-team status: **PASS**.

# RL253 — exact 38-window beta=6 obstruction

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

## Promoted theorem

No surviving Branch-C object has `beta(P)=6`.

## Inherited inputs

From the promoted Branch-C determinant/window/canonical-word machinery:

- `z=a-ell`;
- `a*r-q*ell=2`;
- setting `B=q-r` gives `q*z-a*B=2`;
- `P_i=r-W_i(q)`, where `W_i(q)` counts ones in the cyclic length-q window;
- for `beta(P)=6`, total positive P-mass is exactly `8`;
- the ratio corridor gives `7/19 < z/a <= 24/65`;
- the canonical word has a terminal zero run of length at least 28 cyclically adjacent to prefix `110`.

## Exact identity

Set `H=19z-7a` and `n=19B-7q`. The corridor gives `0<H<=a/65`.

Using `qz-aB=2`:
- `Hq=na+38`;
- `HB=nz+14`.

A q-window has zero count
`q-W_i(q)=q-r+P_i=B+P_i`.

Summing H q-windows whose starts advance by q gives
`HB + sum P = nz+14+sum P`.

Because `Hq=na+38`, the same multiset consists of n full cycles plus one cyclic 38-window. Therefore

`Z_38 = 14 + sum_{j=0}^{H-1} P_{s+jq}`

(up to the harmless cyclic translation/orientation convention).

From `qz-aB=2`, `gcd(a,q)` divides 2. Since `H<=a/65<a/2`, the sampled q-orbit sites are distinct. Their P-sum is at most total positive P-mass 8. Hence every cyclic 38-window satisfies

`Z_38<=22`.

The canonical terminal `0^28` plus the zero in prefix `110` yields a cyclic 31-window with at least 29 zeros, hence a containing 38-window with at least 29 zeros. Contradiction.

Thus beta(P)=6 Branch C is impossible.

## Scope

This eliminates the entire beta=6 Branch-C regime, strictly superseding RL252's first-frontier `k<=53` contraction.

Gate A remains open. Gate B remains open. Radius 4 is not invoked. Radius 5 remains inactive. No global non-trivial-cycle exclusion is claimed.

# RL48 continued progress — 2026-08-22

## Executive result

The continuation found a substantially simpler full-phase bridge.

The retained one-excursion words reconstruct as

`u=110 x 1 0^t`, `v=111 y 0^(t+1)`.

Using only the RL47 terminal `Qx,Qy` identity, their word polynomials satisfy

`Q(u)-Q(v)=4(2^a+3^ell)`.

For `X=2^a`, `Y=3^ell`, concatenation then factors exactly as

`Q(uv)=(X+Y)(Q(v)+4Y)`.

Therefore the RL48 full phase scalar

`X-Y | Q(v)+4Y`

is *exactly equivalent* to full cycle divisibility

`X^2-Y^2 | Q(uv)`.

If it holds, the quotient

`N=(Q(v)+4Y)/(X-Y)`

is positive and the two half-words are genuine Collatz trajectory segments

`N --u--> N+4`,

`N+4 --v--> N`.

Thus full phase produces a positive nontrivial cycle whose midpoint values differ by exactly `4`.

Because `u` starts `110` and `v` starts `111`, `N=3 mod 8`; after the first two common odd steps the pair becomes a literal gap-`9` pair, and the mandatory `(0,1)` local column gives the canonical RL state `T=-14`.  This recovers the physical gap-9 entrance directly from the phase quotient.

## Why this matters for radius 3

Gate B no longer needs a same-root resultant/subresultant construction.  The algebraic phase bridge is explicit and produces the canonical depth-three `4`-separated pair itself.

The only missing radius-3 step is now a provenance/hypothesis audit:

- if the audited RL18/RL19 radius-3 theorem excludes exactly a positive cycle containing such a canonical `N,N+4` pair, Gate B is closed immediately;
- if that theorem has additional sparse-support/orientation/gcd hypotheses, the remaining Gate-B task is only to check/derive those hypotheses from `u,v`.

The exact RL18/RL19 theorem statement is absent from the RL47→RL48 archive, so unconditional radius-3 closure is not claimed here.

## Additional semantic reconstruction

For the actual local trajectories `A_i,B_i` after the leading `11` and mandatory `01`, the RL coordinate is exactly

`T_i=3^(d_i) A_i-B_i`.

The recurrence is therefore not an abstract certificate variable: it is the scaled physical gap coordinate of the two `4`-separated half-cycle trajectories.

At terminal `T=2^(t+3)-1`.  The omitted terminal `(1,0)` pair makes the physical separation `2^(t+2)`, and the final `t` synchronized zero columns divide it back to exactly `4`.

This gives a direct orbit meaning to the terminal valuation problem `H>=t+3`.

## Verification

Two new exact regression verifiers pass on:

1. the audited RL47 `(65,41), t=2` structural witness;
2. the audited RL45 `(65,41), t=0` proper-factor countermodel.

They independently verify:

- the general `u,v` reconstruction on those sources;
- the `Q(u),Q(v)` formulas;
- derivation of `Q(u)-Q(v)=4(X+Y)` from the terminal identity;
- `Q(uv)=(X+Y)(Q(v)+4Y)`;
- 2-adic parity residues of `u,v` differ by exactly `4`;
- actual integer trajectory realization of the two words;
- `T_i=3^d A_i-B_i` at every internal column;
- terminal return to physical separation `4`.

Both inherited examples fail the full phase scalar, as they should; no countermodel has been promoted to an RL solution.

## Proof-state change

### Promoted to analytic from current-bundle material

- general one-excursion word reconstruction `u=110x10^t`, `v=111y0^(t+1)` from RL45 full-word convention + RL47 start/terminal convention;
- proper-factor identity reconstructed from RL47 terminal identity;
- full-denominator concatenation factorization;
- full phase iff exact positive `4`-swap return;
- physical meaning `T=3^dA-B`;
- canonical gap-9 entrance from the full phase quotient.

### Still open / audit-pending

- exact statement/hypothesis match to the inherited radius-3 theorem;
- uniform Gate-A theorem `H>=t+3` if it remains logically necessary after that radius-3 match;
- global RL closure.

## Recommended next step

Obtain the exact RL18/RL19 radius-3 theorem text and compare its hypotheses directly with the proven pair

`N --110 x 1 0^t--> N+4`,

`N+4 --111 y 0^(t+1)--> N`.

Do **not** return to global resultants unless that audit shows the radius-3 theorem needs a genuinely different algebraic input.

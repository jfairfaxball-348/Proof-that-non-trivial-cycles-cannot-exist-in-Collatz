# RL257 — endpoint repair, k=33 elimination, and k=31 flank contraction

Date: 2026-09-05  
Classification: **R4_BRIDGE_REDUCED**

## 0. Incoming exact state

RL256 leaves the unique first halving selector

`(a,ell,z,q,r,H_sel,n)=(1100,694,406,317,200,14,4)`

with

- `k in {31,33}`;
- `k=31 => E_31<=27`;
- `k=33 => beta(P)>=281`;
- `k=33 => E_33<=5`;
- for `k=33`, both adjacent four-one blocks are forced, including
  `u_3u_4u_5u_6=1111`.

The full half-word convention is

`u = 110 x 1 0^(k-3)`.

## 1. Mandatory historical endpoint repair

RL257 rechecked the exact-source-derived RL64 definition rather than inheriting
the wording of the RL256 closeout.

The internal canonical path starts after the mandatory local `(0,1)` column at

`(d_0,T_0,J_0)=(1,-14,-13)`,

where

`J=T+3^d-2^d`.

The exact RL64 full-phase-extendable definition requires the internal terminal
boundary

`d_m=1`,
`T_m=2^k-1`,
`J_m=2^k`.

Crucially, this boundary is **before** the omitted terminal local `(1,0)`
column. The omitted `(1,0)` and then the synchronized terminal zeros belong to
the full-word reconstruction outside the internal `x,y` path.

Therefore the RL257 kickoff sentence placing `J=2^k` after that omitted `10`
is corrected here.

This session does **not** resurrect RL256's demoted provisional backward tree;
it is unnecessary for the result below.

A second notation repair is binding:

- `H_sel=19z-7a=14` is the RL254/RL255 window-selector integer;
- `H_can` is the RL45/RL64 accumulated canonical area.

No equality `H_sel=H_can` is assumed or promoted.

## 2. Exact u-driven internal transition

From the frozen RL45/RL64 parity legality, an internal `u` bit `x` determines
the pair column from the parity of `J`.

If `J` is odd, the column is synchronized:

- `x=0`: `00`,
  `J'=(J+3^d-2^d)/2`, `d'=d`;
- `x=1`: `11`,
  `J'=(3J+2^d-1)/2`, `d'=d`.

If `J` is even, the column is skew:

- `x=0`: `01`,
  `J'=(3J+3^(d+1)-2^d-1)/2`, `d'=d+1`;
- `x=1`: `10`,
  `J'=J/2`, `d'=d-1`, legal only for `d>1`.

These are exact integer transitions, not a relaxed automaton.

## 3. k=33 is eliminated analytically

For `k=33`, RL256 proves `E_33<=5`. Every right-flank zero of weight at least
six is therefore impossible, so in particular

`u_3u_4u_5u_6=1111`.

Because `u=110 x 1 0^30`, physical position `3` is exactly the first internal
`x` bit. Hence a `k=33` survivor would have an internal prefix beginning
`111`.

Now start the exact canonical internal path at `(d,J)=(1,-13)`.

First internal one:

`(1,-13) --11--> (1,-19)`.

Second internal one:

`(1,-19) --11--> (1,-28)`.

At the third internal one, `J=-28` is even. Parity legality therefore forces
the skew column `10`. But a `10` descent is internal only when `d>1`, while
the current height is still `d=1`.

Contradiction.

Therefore

`boxed: k=33 is impossible at the exact first halving selector}`.

This uses only promoted RL256 flank forcing plus the exact historical
full-phase internal start and parity/height legality. It does not use the
demoted four-state tree, the exploratory MILP, Radius 4, or any identification
of `H_sel` with canonical area.

Thus the exact first halving frontier contracts to

`boxed: k=31 only}`.

## 4. k=31: exact canonical right-flank floor

For `k=31`, the terminal zeros occupy physical positions `[-28,-1]` and the
nineteen unknown flank sites have weights

- left `-39,...,-30`: `1,2,...,10`;
- right `3,...,11`: `9,8,...,1`.

The right flank is exactly the first nine internal `x` bits.

The bundled exact verifier enumerates all `2^9=512` candidate `x` words from
the fixed start `(d,J)=(1,-13)` under the deterministic transition above.

Exactly `199` nine-bit words are canonically legal.

Their weighted right-flank zero cost has exact minimum

`boxed: E_right >= 11}`.

Exactly two legal nine-bit words attain equality:

- `110110111`;
- `110111010`.

The running minimum weighted zero cost after prefix lengths `1,...,9` is

`0,0,7,7,7,7,10,10,11`.

This is a finite exact certificate, not a heuristic optimization.

## 5. k=31: terminal-side budget and finite flank family

RL256 gives

`E_31 = E_left + E_right <=27`.

Therefore the new right-flank floor gives

`boxed: E_left<=16}`.

The left ten sites carry weights `1,...,10`. Since

`1+2+3+4+5=15`,
`1+2+3+4+5+6=21>16`,

at most five of those ten sites can be zero. Hence at least five of the final
ten internal `x` bits are ones.

There are exactly `141` ten-bit left-flank `x` patterns with weighted zero
cost at most `16`.

For a sharper finite handover, the verifier then combines:

1. all `199` canonically legal right nine-bit prefixes;
2. all ten-bit left `x` patterns;
3. the exact total budget `E_31<=27`;
4. the RL256 seven-block complement;
5. terminal-zero and flank-zero root exclusions derived from
   `P_(i+1)-P_i=u_i-u_(i+q)`;
6. exact spacing-at-least-three capacity for isolated Branch-C `-1` roots.

There are exactly

`3064`

right/left flank `x`-pattern pairs after the `E_31` budget, and exactly

`boxed: 2719}`

remain after the exact complement-capacity test.

This `2719`-pair family is deliberately a **safe superset** of genuine
full-phase objects. RL257 has not yet imposed the exact backward terminal
`(d,J)` compatibility of the left ten `x` bits, nor coupled the two flanks
through the long middle internal word.

## 6. Scope

Promoted by RL257:

1. historical endpoint convention repaired:
   `J=2^k` is the internal terminal boundary before the omitted terminal `10`;
2. selector `H_sel=14` is kept distinct from canonical accumulated area;
3. `k=33` is analytically eliminated;
4. the first halving frontier is therefore `k=31` only;
5. for `k=31`, `E_right>=11`, with exactly two equality prefixes;
6. hence `E_left<=16`, at most five zeros occur among the final ten internal
   `x` bits, and only 141 universal left-flank `x` patterns remain;
7. exact flank/capacity enumeration leaves 2719 right/left `x`-pattern pairs
   as a safe finite superset for the next attack.

Not promoted:

- no Gate A closure;
- no Gate B closure;
- no Radius-4 application;
- no use of the exploratory MILP;
- no global non-trivial-cycle exclusion;
- no claim that any of the 2719 finite flank pairs extends to a genuine full
  phase.

Gate A remains open. Gate B remains open. Radius 5 remains inactive.

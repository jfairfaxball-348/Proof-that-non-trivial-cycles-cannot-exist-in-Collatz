# RL197 — H21 Height-Scale Selector and Owned p-Shift Zero-Edge Interface

Date: 2026-08-31  
Incoming authority: RL196 at `367377e425272d3badfcf19bacc0efbf55a6b985`.  
All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`.

## Outcome

RL197 turns the RL196 request for a second owned p-shift-compatible zero edge into one exact
binary H21 question.

For every surviving H21 `{33,34,35}` co-owned terminal, the three shallow starts at offsets
35, 34 and 33 have exactly six possible common-height triples:

`000, 010, 011, 100, 110, 111`.

The middle edge, from the `tau=34` start to the `tau=33` start, is simultaneously height-zero
on both p-shifted trajectories exactly in the two cases `000` and `100`.
Thus the bridge is equivalent to proving that the H21 `tau=34` common height equals zero.

RL197 also proves a sharp barrier: the already-certified H21 normalized gaps and predecessor
mod-3 condition cannot select that height. They are invariant under the allowed local height scale.
A successor must add a genuinely global height selector.

## 1. Exact H21 local mechanics

Use
`A=217976794617`, `L=137528045312`, `B=80448749305`, `R=57079296007`,
`p=65470613321`, `Ap-u0 L=1`.

The H21 family has terminal invariant
`T=7*3^35=350220815692997949`, `H=21`
and terminal core
`D_H21=[23369453298,41775866136]`
minus 14 inherited deletions.

For terminal rank `r`, the ranks at offsets `36,35,34,33` before terminal range exactly over

- `[15303429870,33709842708]` -> digit 1;
- `[95752179175,114158592013]` -> digit 2;
- `[38672883168,57079296006]` -> digit 1;
- `[119121632473,137528045311]` -> digit 2.

Hence the predecessor/start word is exactly `1|212`.

The p-shift common-mechanical seam ranks are `R-1` and `L-1`.
The last two intervals meet them only at terminal rank `41775866136`, already deleted.
Therefore every surviving H21 co-owner has an ordinary/common-mechanical `212` start interface.

## 2. Exact six-state height interface

Let `(e35,e34,e33)` be the common p-pair heights at starts `tau=35,34,33`.
The clean shallow-start ownership gives each in `{0,1}` and zero p-defect.

Across digit 2:
`a35=2+e35-e34 >=1`, automatically for binary heights.

Across digit 1:
`a34=1+e34-e33 >=1`, equivalently `e33<=e34`.

Thus exactly six triples survive:
`000,010,011,100,110,111`.

## 3. Exact owned zero-edge criterion

At the middle source both p-pair heights are `e34`; after one chronological step both are `e33`.
So the middle edge and its p-shifted copy are zero-zero exactly when `e34=e33=0`.
Within the six-state interface this is exactly `000` and `100`.
Since `e34=0` already forces `e33=0`, the bridge is precisely the one-bit selector `e34=0`.

If that selector is later proved, each such physical H21 co-owner supplies one canonical
p-shift-compatible zero edge at its `tau=34` source. RL197 does not prove the selector.

## 4. Height-scale blindness of inherited H21 normalization

RL190 gives `Delta35=7*2^35`. Zero-defect propagation through digits 2 then 1 gives

`4 Delta34=3 Delta35`, `2 Delta33=3 Delta34`,

hence
`Delta34=21*2^33`, `Delta33=63*2^32`.

For common height `e_j`,
`C_j=2^(e_j) Delta_j`.

Thus either height 0 or 1 yields the same normalized gap; changing height multiplies `C` by 2.
Because 2 is a unit modulo 3, divisibility by 3 is unchanged. In particular
`C35=7*2^(35+e35)` is nonzero modulo 3 at either height scale, so the inherited odd/nonzero
predecessor sensor is also scale blind.

This is a method barrier only. Stronger complete-word, global moment, K/rho phase, prehistory
or ownership constraints remain available.

## Classification

New analytic mathematics:
1. exact `1|212` H21 local mechanical interface;
2. exact six-state binary height classification;
3. exact two-state owned p-shift zero-edge criterion;
4. reduction to the single `tau=34` height selector;
5. scale-blindness theorem for inherited H21 normalized-gap/mod-3 constraints.

Exact finite certificate: `verification/verify_rl197_h21_height_scale.py`.

No H21 budget release or branch/global closure is claimed.

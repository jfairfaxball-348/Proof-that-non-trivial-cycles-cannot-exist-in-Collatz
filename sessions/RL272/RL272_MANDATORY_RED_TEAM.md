# RL272 mandatory red team

Date: 2026-09-07

Result: **PASS**.

## Orientation and median ties

The main certificate orients to `kappa=+3` only by exact source/target reversal. The independent replay enumerates **every optimal median**, not just the repository's lower-median convention.

Through `A<=15` it finds exactly 708 relevant height-two `4+1` optimal-flow occurrences:
- 354 with `kappa=+3`;
- 354 with `kappa=-3`.

There are 702 distinct word/shift instances because six `A=6` instances have two relevant optimal medians. This explicitly red-teams median-choice asymmetry.

## Exact numerator indexing

After reversal to `+3` and rotation to put the `1,2,1` core at indices `0,1,2`, every replayed instance satisfies exactly

`Q(y)-Q(x)=15*3^(L-2)-2^u 3^(L-R_u-1)`.

Formula mismatches: **0**.

The main finite solver independently reconstructs 149 canonical states and again reports zero formula mismatches.

## Full D versus proper factors

All theorem hit tests use the complete positive

`D=2^A-3^L`.

Main certificate:
- proper-factor-only difference cases: 5;
- full-`D` difference hits: 0.

Independent replay:
- proper-factor-only difference occurrences: 30;
- full-`D` difference hits: 0;
- actual full-`D` source words: 0.

No proper factor is substituted for `D`.

## Determinant endpoints and gcd sectors

The finite solver computes `q=(mL+3)/A` and accepts the full exact range `1<=q<=L`; it does not import RL271's rejected `q<L` shortcut.

The 149 reconstructed states include both `gcd(A,L)=1` and `gcd(A,L)=3` sectors, split 114/35. No determinant-one coprimality assumption is used.

All 149 finite states happen to have `gcd(m,A)=3`, but this is not promoted as an infinite prerequisite.

## Cyclic wrap and component placement

The canonical solver enumerates every
`4<=u<=A-2`
with no reflection quotient and every nontrivial shift `m`.

The independent replay starts from raw words and shifts instead, then normalizes only after detecting the topology. Its positive-orientation orbit count agrees exactly with the canonical state count through `A<=15`.

## Primitivity

The finite certificate does not filter by primitivity. Its zero-hit statement is therefore stronger than the written primitive theorem scope.

## Negative domain

The permanent sentinel

`A=11,L=7,D=-139,Q=18904,n=-136`

is reproduced exactly and remains outside the positive-domain theorem.

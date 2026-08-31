# RL208 layered root-cone theorem and exact rank certificate

Date: 2026-08-31.

## Scope and inherited inputs

This artifact works only inside the inherited H21 necessary-terminal interface.  It
uses the inherited constants

`L=137528045312`, `p=65470613321`, `B=80448749305`, `z=L-p=72057431991`,
`K_0=2^37`, terminal phase `i=I(r)=pr mod L`, and the strictly decreasing law

`K_H21(r)=rho_(I(r))*T/2^21`, `T=7*3^35`.

At every noncarry canonical source the inherited physical drift gives
`|K_(i+1)-K_i|<1/3`; the sole p-shift carry is `z -> z+1`.  Also
`0<K_L-K_0<1`.  No claim below relies on the unpromoted RL207 checkpoint.

## RL208-T1 — enlarged carry-free root cone

For every integer `N` with `1<=N<=2^35`, the selected forward path from phase 0
to any `0<=i<N` and the selected backward path from lifted phase L to any
`L-N<=i<L` avoid the unique carry, because

`2^35 < p-1 < z+1`.

Summing the inherited noncarry speed bound and using `0<K_L-K_0<1` proves

`K_0-N/3 < K_i < K_0+1+N/3`                                      (1)

through both half-open root windows.  This is a scoped analytic consequence of
inherited identities, not a statement across the carry and not a physical H21
occurrence claim.

## Exact 704-layer consumption

Put `N_0=2^24`.  For each `k=24,...,34` and `j=1,...,64`, define

`N_(k,j)=2^k + j*2^(k-6)`.

The 704 outer radii run consecutively from just above `2^24` through `2^35`.
For each outer radius N, let

`U_N=K_0+1+N/3`, `L_N=K_0-N/3`.

Strict decrease of `K_H21(r)` makes the exact safe rank band

`[s_lo(N),s_hi(N)]`,

where `s_lo(N)` is the first inherited-core rank with `K_H21(r)<U_N` and
`s_hi(N)` is one less than the first inherited-core rank with
`K_H21(r)<L_N`.  The verifier proves every adjacent boundary sign using exact
rational logarithm enclosures; no floating-point sign is promoted.

For consecutive radii `N_prev<N`, consume only the disjoint chronological layers

- forward `[N_prev,N)`;
- backward `[L-N,L-N_prev)`.

Equation (1) implies that a necessary H21 terminal in either layer must have rank
inside `[s_lo(N),s_hi(N)]`.  Therefore a terminal rank in that layer and outside
the safe band is impossible.

The modular permutation `r=iB mod L` is counted by exact floor sums.  An
independent coordinate-swapped recount uses `i=pr mod L` over rank intervals and
agrees on every one of the 704 layers.  The verifier also checks that the new
layers start outside the inherited `2^24` root windows, that forward/backward
layers are disjoint, and that no newly counted deletion hits any of the twelve
inherited isolated deletions or four anchor deletions.

The exact new exclusions are:

- forward layers: **1,382,560,101**;
- backward layers: **1,382,560,222**;
- total: **2,765,120,323**.

Thus the inherited necessary-terminal count falls exactly from
**16,188,727,234** to **13,423,606,911**.

The exact source-side split after transport by `a=i-34 mod L` is:

- canonical `a>p`: **7,099,572,324** survivors;
- canonical `a<p`: **6,324,034,587** survivors.

Before this RL208 deletion the corresponding `a>p` count was 8,482,132,546.

## Saturation of this conservative consumer

At `N=2^35`, exact boundary certification gives safe band
`[25583192106,41775866136]`, the whole inherited rank core.  Increasing the
common radius only weakens (1), so this specific conservative common-radius
consumer cannot delete additional ranks beyond that point.  This does not rule
out a sharper pointwise cone, another independent H21 consumer, or another Gate
route.

## Classification and locks

RL208-T1 is new proved analytic mathematics at the stated carry-free root-window
scope.  The 2,765,120,323 deletion is a new exact finite certificate represented
by the layer/rank predicate and exact counts; no huge materialized rank list is
required.

No eta class, e35 state, terminal sign, or valuation is selected.  Necessary
rank evidence is not a physical H21 realization or charge.  The sole high branch
`(37,0,23,-1)` is not contradicted.  Gate A remains open, Gate B remains open,
and global nontrivial-cycle exclusion remains open.

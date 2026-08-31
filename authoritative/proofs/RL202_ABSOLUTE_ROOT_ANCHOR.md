# RL202 — absolute root K cone and zero-height collision obstruction

Date: 2026-08-31. Incoming authority RL201 at
`934f1289d655734d3ea8d78b3677ca200aab1d57`.

## 1. Carry-free root speed limit

Put `v_i=2^(-h_i)`. The inherited physical drift at a noncarry source is

`3(K_(i+1)-K_i)=rho_i(v_(i+p)-v_i)`.                    (1)

Every `v` lies in `(0,1]`, canonical `rho_0=1` and `rho_i<1` for `0<i<L`.
Therefore every noncarry canonical source satisfies

`|K_(i+1)-K_i|<1/3`.                                   (2)

Let `N=2^24`. The unique p-shift carry source is
`z=L-p=72057431991`; directly `N<z<L-N`. Hence no source used while moving
from phase 0 to any `i in [0,N)`, or backward from lifted phase L to any
`i in [L-N,L)`, is the carry.

The exact anchor is `K_0=2^37` and `K_L=lambda K_0`. Since
`0<delta=ln(lambda)<2^-40` and `exp(x)-1<x/(1-x)` for `0<x<1`,

`0<K_L-K_0<(2^37)/(2^40-1)<1`.                          (3)

Summing (2), with the harmless common radius `N/3`, gives for either root
window

`K_0-N/3 < K_i < K_0+1+N/3`.                           (4)

No claim is made across the carry or outside these windows.

## 2. Consume the exact H21 terminal K law

For a necessary H21 terminal rank r, inherited RL200/RL201 gives

`K_i=K_H21(r)=rho_(I(r))*T/2^21`, `i=I(r)=pr modL`,      (5)

where `T=7*3^35`, and this quantity is strictly decreasing in r.
Define

`Klow=K_0-N/3`, `Khigh=K_0+1+N/3`.

The exact sign-correct logarithm certificate proves

`K_H21(38643145223)>Khigh`,
`K_H21(38643145224)<Khigh`,
`K_H21(38659291956)>Klow`,
`K_H21(38659291957)<Klow`.                              (6)

Strict rank monotonicity therefore implies:

**If an H21 terminal phase lies in either root window, its rank must lie in**

`[38643145224,38659291956]`.                            (7)

This is a conditional rank restriction, not a new global contiguous core.

## 3. Exact complete-window counts

Rank at canonical phase i is `iB modL`. Counting this modular permutation over
both complete length-N windows by exact floor sums yields:

- forward `[0,N)`: 1,975,360 inherited-core ranks, of which 1,969 lie in (7),
  hence 1,973,391 lie outside (7). Seven of those were already among RL201's
  12 isolated deletions, leaving **1,973,384 new exclusions**;
- backward `[L-N,L)`: 1,975,366 inherited-core ranks, again 1,969 in (7),
  hence **1,973,397 new exclusions**; no inherited deletion is among these.

The two phase windows are disjoint and rank-phase correspondence is bijective,
so the root-anchor speed consumer removes exactly

**3,946,781 previously surviving necessary ranks.**                  (8)

The set is represented exactly by the phase-window/rank predicate; no huge
materialized list is required.

## 4. Absolute zero-height anchor collision

Let a be the tau34 source phase. Its common height is one. For the next 33
chronological transitions the individual acceleration exponent is exactly one.
The height recurrence is

`h_(i+1)=h_i+c_i-a_i`, with `c_i in {1,2}`.

Thus along offsets `0<=t<=33`, starting at `h_a=1`, the height never decreases
below one. None of these phases may equal a globally anchored zero-height phase
`0,1,p,p+1` modulo L.

If anchor k is hit at offset t, then `a=k-t modL`. The terminal rank is 34
mechanical steps later, so

`r=((k+34-t)B) modL`.                                  (9)

Exhausting the exact 4 x 34 possibilities and retaining the RL201 core gives
eight unique ranks. Four are already inherited deletions

`26058127774,28746802250,36398517185,39087191661`,

and four are newly excluded:

**`26058127775,28746802251,36398517186,39087191662`.**   (10)

Their terminal phases are near p, not in the root windows, so (10) is disjoint
from (8).

## 5. Combined frontier and classification

RL201 had 16,192,674,019 necessary ranks. Subtracting (8) and (10) gives

**16,188,727,234 necessary ranks.**                      (11)

Equations (1)--(4) are analytic consequences of inherited physical identities;
(5) and its monotonicity are inherited; (6) and the complete-window counts are
exact finite certificates; (9)--(10) are finite exhaustive modular algebra.

No eta class, state e35, sign or valuation is selected. The dyadic joint-prefix
moment remains the principal unresolved selector after this absolute-anchor cut.
No physical occurrence, H21 charge, Gate or global cycle exclusion is claimed.

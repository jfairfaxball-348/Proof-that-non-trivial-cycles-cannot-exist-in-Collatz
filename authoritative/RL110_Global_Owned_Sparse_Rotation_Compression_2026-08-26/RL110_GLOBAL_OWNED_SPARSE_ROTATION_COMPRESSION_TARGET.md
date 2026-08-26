# RL110 target — global owned sparse-rotation compression on the radius-3 complement

Date: 2026-08-26

## Purpose

Attack the globally valid ordinary-ownership interface isolated by RL109. Do not return to local basin equality, raw Farey enumeration, or bulk cascade scanning.

## Setup

Let `w` be the primitive parity word of a hypothetical positive ordinary shortcut Collatz cycle. Put

- `A=|w|`;
- `L=#1(w)`;
- `D=2^A-3^L>0`;
- `R_* = min dist_cyc(rot_r(w),rot_s(w))` over distinct rotations.

RL109 proves `R_*<A`, so a closest pair has a zero-flow cut and a fixed-cut minimum adjacent-transposition path of length `R_*`.

For that pair `u,v`, the ordinary unit-increment numerator difference has the exact sparse form

`S = Q_1(v)-Q_1(u) = sum_(j=1)^(R_*) epsilon_j 2^(a_j)3^(b_j)`

with `epsilon_j in {+1,-1}`.

Because `u,v` are actual owned rotations,

`S = D(x_v-x_u)`,

so `S!=0` and `D|S`.

## Primary theorem target

Work under the complement of the inherited closed small-radius regime:

`R_*>=4`.

Prove

`0 < |S| < D`,

or a logically equivalent contradiction to `D|S`.

If the analysis instead forces `R_*<=3`, invoke the inherited closed primitive/full-`D` small-radius engine.

## First milestone

Derive the strongest globally valid independent upper bound on

`|S|/D`

for the canonical closest pair. Separate carefully:

1. what follows only from transposition geometry;
2. what uses least-root/final-return prefix/suffix ordering;
3. what uses actual physical-state ordering;
4. what uses full ordinary `D|Q` ownership;
5. what uses primitivity.

If the bound stalls at or above `1`, identify the exact support/coefficient statistic responsible. That obstruction is itself a valid RL110 outcome if proved sharply and should determine the next route.

## Allowed structural consumers

Priority consumers are:

- full ordinary `D|Q` content before normalization;
- actual state difference `x_v-x_u` with independently proved physical bounds;
- least-root/final-return prefix/suffix envelopes;
- RL101 two-sided physical excursion when its hypotheses genuinely apply;
- a new strip/packing bound on the signed monomial support;
- valuation or gcd structure of the sparse transport that is absent from generalized-increment fakes.

## Mandatory red teams

1. **RL20:** the argument must fail on the exact radius-4 local-grammar fake because that word has `D∤Q`.
2. **RL79:** do not normalize away the generalized increment. Ordinary ownership supplies unscaled `D|S`; generalized `T_s` ownership supplies only `D|sS` in general.
3. **RL81:** any `Q/D` state used in an inequality must be an actual owned physical state.
4. **Primitivity:** preserve the role of distinct rotations/states in `S!=0`.
5. **Raw scope:** do not introduce first-Farey/raw-`g=1` restrictions while claiming a global theorem.
6. **External input:** record any external least-cycle floor explicitly; prefer a theorem independent of it.
7. **Closure scope:** no branch-specific or finite result may be promoted to global RL closure.

## Stop conditions

Stop or pivot if the candidate:

- reduces to the identity `S=D(x_v-x_u)` with no independent inequality;
- becomes a normalized coboundary already frozen in RL20/RL72/RL102;
- survives unchanged under generalized-increment scaling;
- needs only local grammar and therefore is refuted by the RL20 fake;
- silently assumes the exact first-Farey/raw-`g=1` branch.

## Frozen fallback

Do not resume the coupled numerical cascade unless RL110 supplies a structural trigger with genuine global leverage or a new support/tier theorem with materially different economics.

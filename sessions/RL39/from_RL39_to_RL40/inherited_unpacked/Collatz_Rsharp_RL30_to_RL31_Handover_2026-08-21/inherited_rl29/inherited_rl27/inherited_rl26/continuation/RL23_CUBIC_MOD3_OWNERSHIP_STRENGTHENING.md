# RL23 — mod-3 ownership strengthens the order-3 cubic lattice

Date: 2026-08-21

## Status

Sections 1--4 are **ANALYTIC**. Section 5 is an **EXACT FINITE CERTIFICATE only for the additional strict-supercritical-prefix package inherited from RL22**.

This note strengthens the global order-3 cubic lower bound by combining the RL22 physical-gap lattice with the RL20 theorem that every actual phase state of a nontrivial positive cycle is nonzero modulo `3`.

## 1. A missing global residue constraint on the physical gaps

Use the RL22 balanced order-3 notation

`B=2^b`, `Y=3^e`,

with balanced block-start states

`R`, `x=R+G`, `y=R+H`,

and block numerators `U,V,W`.

RL22 proved

`U-W = BG+YH`,

`V-W = -YG+(B+Y)H`.                                       (R23C.1)

If the three blocks share `r` initial parity bits, then

`G=2^r N`, `H=2^r K`                                      (R23C.2)

for positive distinct integers `N,K` in a primitive cycle.

RL20 proved globally that every actual cycle phase is nonzero modulo `3`. Hence the three states `R,x,y` occupy only the two nonzero residue classes modulo `3`. Two of them must agree modulo `3`, so

`3 | G`, or `3 | H`, or `3 | (H-G)`.                      (R23C.3)

Because `2^r` is invertible modulo `3`, this is equivalent to

> **`3 | N`, or `3 | K`, or `3 | (K-N)`.**                (R23C.4)

This global ownership condition was not used in the RL22 shortest-vector estimate.

## 2. Strengthened shortest vector

Scale (R23C.1) by `2^r`:

`U-W = 2^r(YK+BN)`,

`V-W = 2^r((B+Y)K-YN)`.                                   (R23C.5)

Suppose first `N>K`. The only positive distinct pair with `N<3` is `(N,K)=(2,1)`, but it violates (R23C.4). Therefore `N>=3`, and

`YK+BN >= Y+3B`.

If `K>N`, the same argument gives `K>=3`, while

`(B+Y)K-YN = BK+Y(K-N) >= 3B+Y`.

Thus every non-diagonal primitive actual solution obeys

> **`max(|U-W|,|V-W|) >= 2^r(3B+Y)`.**                    (R23C.6)

The lattice-level constant is sharp: `(N,K)=(3,1)` attains `YK+BN=3B+Y`.

This strictly strengthens RL22's global bound `2^r(2B+Y)`.

## 3. Near-resonant shared-11 consequence

In the inherited three-way near-resonant branch

`lambda=(B/Y)^3<16/15`,

RL22 proved that all three balanced states lie in the low strip and therefore begin with parity prefix `11`. Hence `r>=2`.

Applying (R23C.6), every primitive actual three-way balanced return satisfies

> **`max(|U-W|,|V-W|) >= 4(3B+Y)`.**                       (R23C.7)

This adds a full `4B` to the previous global `4(2B+Y)` spread threshold.

### A genuine global numerator upper bound

The balanced-cut height sandwich also gives, with `z=B/Y`,

`0<G<(z^2-1)R`,

`0<H<(z-1)R`.

Substituting these directly into the physical lattice coordinates gives

`U-W = BG+YH < YR(z^3-1)=YR(lambda-1)`,

while the linear expression

`V-W=(B+Y)H-YG`

has absolute value strictly below

`Y R (z^2-1) < YR(lambda-1)`.

Therefore, without any strict-prefix hypothesis,

> **`max(|U-W|,|V-W|) < Y R (lambda-1)`.**                 (R23C.8)

This is the first clean global upper bound on the owned cubic numerator differences in this line of attack. It is not yet strong enough because the defect `R(lambda-1)` can still grow with the block weight.

Using the RL23 packing theorem

`log(lambda)/(3e) <= 319/[5(256R-319)]`

and `lambda<16/15`,

`R(lambda-1) < (163328/203205)e < (81/100)e`

for `R>=160`. Hence

> **`max(|U-W|,|V-W|) < (163328/203205)eY`.**              (R23C.9)

Combining this with (R23C.7) alone already forces `e>=20`. The stronger residue/gap argument below improves that small absolute consequence to `e>=24`, but the important structural point is that Track B now has a genuinely global upper bound: the remaining loss is an explicit factor of order `e`.

There is also a small radius-independent physical-gap consequence. Put `z=B/Y`, so `lambda=z^3`. The balanced-cut height sandwich gives

`G <= (z^2-1)R`,

`H <= (z-1)R`.                                             (R23C.10)

RL22's global packing theorem gives

`log z/e = log(lambda)/(3e) <= 1/(4R-1)`.                 (R23C.11)

Since `z^3<16/15<(46/45)^3`,

`z-1 <= z log z < (46/45)e/(4R-1)`,

and `z+1<91/45`. For `R>=160`, `R/(4R-1)<=160/639`. Exact rational comparison gives both

`G < (12/23)e`,

`H < (12/23)e`.                                            (R23C.12)

But (R23C.2)--(R23C.4) with `r>=2` imply `max(G,H)>=12`: if both scaled gaps `N,K` were at most `2`, they would have to be `1,2`, which violates the mod-3 condition.

Therefore

> **`e >= 24`.**                                           (R23C.13)

This is analytically global within the stated near-resonant order-3 balanced branch, though it is numerically tiny compared with the external-floor CF bounds when those are invoked.

## 4. Stronger conditional strict-prefix range theorem

Retain the extra RL22 hypothesis that every proper prefix of each macroblock is strictly supercritical. Under a shared prefix of length `r` containing `p` ones, RL22 proved the conditional range bound

`Delta < (e-p)B/3`.                                        (R23C.14)

Combining it with the new global lower bound (R23C.6), a non-diagonal solution under this additional package requires

> **`e-p > 3*2^r(3+Y/B)`.**                               (R23C.15)

Using only `Y/B>1/2`,

`e-p > (21/2)2^r`.                                         (R23C.16)

For the globally shared low-state prefix `11`, the conditional package has `r=2,p=2`, so a non-diagonal solution requires

> **`e>=45`.**                                             (R23C.17)

This improves the old conditional coarse threshold `e>=33`.

As before, (R23C.14)--(R23C.17) are **not** global cycle theorems unless the strict-supercritical-prefix package is established independently.

## 5. Exact conditional frontier

The verifier `verify_rl23_cubic_mod3_lattice.py` checks the strengthened lattice minimum on an exact integer box and reruns the RL22 dynamic program for strict-supercritical block `Q` extrema.

For near-resonant terminal pairs with `b<=120`, the first pair at which the exact conditional `Q` range reaches the strengthened shared-`11` threshold

`4(3B+Y)`

is

`(b,e)=(119,75)`.

This pair is already coprime, so the first coprime failure in the scanned range is also `(119,75)`.

For comparison, the old `4(2B+Y)` threshold first failed at `(92,58)` and its first coprime failure was `(100,63)`.

These are **conditional finite frontiers only**; they do not upgrade the strict-prefix hypothesis into a global ownership theorem.

## Strategic consequence

The order-3 interface is now stronger:

1. actual state ownership gives physical lattice coordinates;
2. shared `11` gives the factor `4`;
3. global nonzero-mod-3 phase ownership forbids the old shortest `(4,8)` gap pattern;
4. the cubic numerator spread is therefore at least `4(3B+Y)`.

This still does not close the bridge. RL23 now has a genuinely global upper bound, but it is too weak by an explicit factor of order `e`: the current sandwich is roughly `16B <= max|Delta Q| <= 0.8 e B`. The next Track-B target is therefore sharper and more concrete: remove or drastically reduce that `e` loss using suffix domination, block endpoint distribution, longer synchronization, or another nonlocal ownership mechanism. A longer common prefix or stronger residue structure would also raise the lower side of the sandwich.

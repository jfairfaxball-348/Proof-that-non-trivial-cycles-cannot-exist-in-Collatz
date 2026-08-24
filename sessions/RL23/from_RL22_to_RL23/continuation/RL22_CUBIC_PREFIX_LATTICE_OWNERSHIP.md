# RL22 — cubic prefix-lattice ownership

Date: 2026-08-21

## Status

Sections 1--4 are **ANALYTIC**. Section 5 is an **ANALYTIC CONDITIONAL LEMMA** under an additional strict-supercritical-prefix hypothesis. Section 6 is an **EXACT FINITE CERTIFICATE for that conditional package only**.

Important scope correction: strict supercriticality of every proper macroblock prefix is **not** a universal consequence of leastness.  The general/global content of this note is the lattice/state-gap structure in Sections 1--4.  The `Q`-range conclusions in Sections 5--6 apply only when the extra prefix envelope is separately available.

## 1. Three-way balanced cubic lattice

Let

`B=2^b`, `Y=3^e`, `C=B^2+B Y+Y^2`,

and let `u,v,w` be binary blocks of the same length `b` and weight `e`, with

`U=Q(u)`, `V=Q(v)`, `W=Q(w)`.

The relative cubic condition is

`C | Y^2 U + B Y V + B^2 W`.                               (R22C.1)

Since `B^2 == -BY-Y^2 (mod C)` and `Y` is a unit modulo `C`, this is equivalent to

`C | Y(U-W)+B(V-W)`.                                       (R22C.2)

Put

`a=U-W`, `c=V-W`.

Then for some integers `k,n`, exactly

`a=kY+nB`,

`c=k(B+Y)-nY`.                                              (R22C.3)

Indeed `Y a+B c=kC`; reduction modulo `B` gives `a==kY (mod B)`, producing `n`. Conversely (R22C.3) immediately gives `Ya+Bc=kC`.

So the cubic relative congruence is an explicit rank-2 lattice in the two block-numerator differences.

## 2. Actual-state ownership of the lattice coordinates

For an actual three-way balanced integer cycle, let the block-start states be

`R`, `x=R+G`, `y=R+H`,

where `R` is the least state.  The block equations are

`B x-YR=U`,

`B y-Yx=V`,

`B R-Yy=W`.                                                 (R22C.4)

Subtracting the third equation from the first two gives

`U-W = B G+Y H`,

`V-W = -Y G+(B+Y)H`.                                       (R22C.5)

Thus in an actual cycle the abstract lattice coordinates in (R22C.3) are exactly

`n=G=x-R`,

`k=H=y-R`.                                                  (R22C.6)

The Eisenstein norm becomes the exact physical-gap identity

`(U-W)^2-(U-W)(V-W)+(V-W)^2`
` = C [G^2-GH+H^2]`.                                       (R22C.7)

This is the real two-coordinate form of the RL21 Fourier/Eisenstein mode.

## 3. Common-prefix amplification

Suppose the three fixed-length/fixed-weight blocks share their first `r` bits, `0<=r<=b`.  Then their pairwise `Q` differences are divisible by `2^r`:

`2^r | U-W`,

`2^r | V-W`.                                                (R22C.8)

Because `C` is odd, (R22C.2)--(R22C.3) imply

`2^r|k`, `2^r|n`.                                           (R22C.9)

Write `k=2^r K`, `n=2^r N`.  Then

`U-W=2^r(YK+BN)`,

`V-W=2^r((B+Y)K-YN)`.                                      (R22C.10)

### General shortest vector

If `(K,N)!=(0,0)`, then

`max(|YK+BN|, |(B+Y)K-YN|) >= B`.                          (R22C.11)

For if both absolute values were `<B`, the inverse formula

`K=[Y A+B D]/C`

would give `|K|<B(B+Y)/C<1`, hence `K=0`, and then `A=NB` forces `N=0`.

Thus every non-diagonal cubic-relative solution sharing an `r`-bit prefix has

`max(|U-W|,|V-W|) >= 2^r B`.                               (R22C.12)

### Positive distinct state gaps

In a primitive actual cycle, the balanced states `R,x,y` are distinct and `R` is least, so

`G>0`, `H>0`, `G!=H`.

Hence `K,N` in (R22C.10) are positive and distinct.  Then the shortest-vector estimate improves to

`max(|YK+BN|, |(B+Y)K-YN|) >= 2B+Y`.                       (R22C.13)

Indeed, if `N>K`, then `YK+BN >= Y+2B`; if `K>N`, then `(B+Y)K-YN >= 2B+Y`.

Therefore a primitive integer cycle with a common `r`-bit prefix satisfies the stronger global lower bound

> **`max(|U-W|,|V-W|) >= 2^r(2B+Y)`.**                    (R22C.14)

## 4. Genuine near-resonant order-3 consequence: a `12B`-scale relative spread

Assume a three-way balanced return in the inherited near-resonant branch

`lambda=(B/Y)^3<16/15`.

RL21's balanced-cut height bounds give

`R < x < (16/15)R`,

`R < y < (16/15)R`.

All three block-start states `R,x,y` are below `(4R-1)/3` for every nontrivial least state.  The RL21 low-state lemma therefore forces each of them to begin with parity bits `11`.

Thus the three macroblocks share at least the first two bits, so `r>=2`.  Applying (R22C.14), every primitive actual order-3 balanced return obeys

> **`max(|U-W|,|V-W|) >= 4(2B+Y)`.**                       (R22C.15)

Since `Y>B/2` whenever a strict-supercritical terminal crossing is present, this would exceed `10B` in that stronger package; without that extra hypothesis the exact form `4(2B+Y)` is the correct global statement.

This is a genuine integrality/ownership lower bound.  It is not yet a contradiction because no universal upper bound of comparable size for arbitrary owned macroblock numerators has been proved.

## 5. Conditional range theorem under strict-supercritical macroblocks

This section adds the extra hypothesis

`3^(P_m)>2^m` for every `1<=m<b`                               (R22C.16)

**for each of the three macroblocks separately**.

This condition occurred in the strengthened rational countermodels and is useful for theorem testing, but it must not be silently promoted to a universal least-state fact.

Suppose the three blocks also share a prefix of length `r` containing `p` ones.  The contributions from those common ones cancel in pairwise `Q` differences.  For every later one at position `i`, (R22C.16) gives

`2^i 3^(e-1-P_i) < 3^(e-1)=Y/3 < B/3`.                    (R22C.17)

Hence the `Q`-range inside this common-prefix class has width

`Delta < (e-p)B/3`.                                        (R22C.18)

Combining with the primitive positive-gap lower bound (R22C.14), a non-diagonal solution under this **additional** package requires

> **`e-p > 3*2^r(2+Y/B)`.**                               (R22C.19)

Using only `Y/B>1/2`, this implies

`e-p > (15/2) 2^r`.                                        (R22C.20)

For the universally shared low-state prefix `11`, if the three macroblocks also satisfy (R22C.16), `r=2,p=2`, so a non-diagonal primitive solution requires at least

`e>=33`.                                                     (R22C.21)

If all three additionally share `1101`, then `r=4,p=3`, and the same coarse inequality requires

`e>=124`.                                                    (R22C.22)

Again: R22C.21--R22C.22 are conditional on the separate strict-supercritical macroblock envelope.

## 6. Exact finite frontier for the conditional package

The verifier `verify_rl22_cubic_prefix_lattice.py` checks the lattice/state/norm identities and computes exact `Q` extrema over all strict-supercritical blocks by dynamic programming.

For every near-resonant terminal pair with `b<=31`, the weaker range already satisfies `Delta<4B`; this explains the diagonal exhaustive searches in that small domain.

The first pair where `Delta<4B` itself can fail is `(b,e)=(35,22)`.  This is only a frontier for the **weak range criterion**.

If one uses the primitive positive-gap threshold `4(2B+Y)` instead, the first scanned near-resonant pair where the exact conditional `Q` range reaches that threshold is

`(b,e)=(92,58)`;

restricting to `gcd(b,e)=1`, the first scanned failure is

`(b,e)=(100,63)`.

These are finite facts about the extra strict-supercritical package, not global cycle exclusions.

## 7. Strategic consequence

The robust global interface is now:

1. cubic relative divisibility gives the lattice (R22C.3);
2. integer ownership identifies its coordinates with physical balanced gaps (R22C.6);
3. near-minimum ownership gives a common `11` prefix and hence gaps divisible by `4`;
4. primitivity/leastness upgrades this to the `4(2B+Y)` numerator-spread lower bound (R22C.15).

To turn this into the missing bridge one still needs a **global upper bound on owned macroblock `Q`-differences**, or stronger synchronization than the universal two parity bits.  The strict-supercritical range theorem shows what such an upper bound would buy, but does not supply it universally.

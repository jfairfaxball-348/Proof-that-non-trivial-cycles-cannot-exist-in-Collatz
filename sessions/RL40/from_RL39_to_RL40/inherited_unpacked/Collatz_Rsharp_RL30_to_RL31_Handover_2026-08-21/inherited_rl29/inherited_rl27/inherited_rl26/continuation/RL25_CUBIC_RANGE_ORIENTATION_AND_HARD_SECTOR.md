# RL25 — cubic range floor, orientation split, and isolation of the hard sector

Date: 2026-08-21

## Status

Sections 1--6 are **ANALYTIC** for the near-resonant three-way balanced branch, with `R>=161` where the RL24 packing majorant is invoked. Section 7 contains an **EXACT FINITE CERTIFICATE** about the first few integer terminal pairs; it is not needed for the analytic inequalities and should not be confused with the inherited external floor `R>=2^71`.

This note feeds the strongest RL24 packing theorem back into Track B and adds two pieces of structure which RL23 did not use:

1. every fixed-length/fixed-weight block numerator has a positive floor `Q>=3^e-2^e`;
2. the cyclic order of the two non-root balanced states matters.  If the later state is the larger one, two of the three block numerators lie above the common baseline `(B-Y)R`, which removes one full baseline contribution from the range estimate.

The result does **not** close RL.  It isolates a single genuinely hard cubic sector.

---

## 1. RL24 gives a clean `1/(4R)` majorant

Retain the RL24 rational majorant `C_H(R)` from `RL24_TYPEI_HIGH_START_SUPPORTING_LINE.md`:

`log(lambda)/L <= C_H(R)`.

The RL25 verifier clears denominators and proves, after `R=t+161`,

> **`R C_H(R) < 1/4` for every `R>=161`.**                 (R25C.1)

In the order-3 balanced branch `L=3e` and

`z=B/Y`, `lambda=z^3`.

Hence

`log z = log(lambda)/3 <= e C_H(R)`.                       (R25C.2)

Using `z^3<16/15<(46/45)^3`,

`z-1 < z log z < (46/45)e/(4R)`,

so

> **`R(z-1) < (23/90)e`.**                                (R25C.3)

Also `z+1<91/45`, hence

> **`R(z^2-1) < (2093/4050)e`.**                          (R25C.4)

These improve the RL23 physical-gap constants while keeping the proof radius-independent.

---

## 2. A fixed-weight floor for every block numerator

For a binary word of length `b`, weight `e`, with one-positions

`0<=i_0<...<i_(e-1)<b`,

its Collatz numerator is

`Q=sum_(j=0)^(e-1) 2^(i_j) 3^(e-1-j)`.

Since `i_j>=j`,

`Q >= sum_j 2^j 3^(e-1-j) = 3^e-2^e`.

Thus, with `Y=3^e`, every one of the three balanced block numerators obeys

> **`U,V,W >= q_0:=Y-2^e`.**                              (R25C.5)

Equality is attained by `1^e 0^(b-e)`, so this floor is exact at the fixed-weight word level.

The absolute cubic mode from RL21 is

`U+V+W=(B-Y)(R+x+y)`.                                     (R25C.6)

Let

`Delta=max(|U-V|,|V-W|,|W-U|)`.

For three nonnegative numbers each at least `q_0`,

`Delta=max-min <= (U+V+W)-3q_0`.                           (R25C.7)

The balanced-cut height bounds

`x<z^2R`, `y<zR`

give

`U+V+W < YR(z^3-1)=YR(lambda-1)`.

Therefore

> **`Delta < Y[R(lambda-1)-3+3(2/3)^e]`.**                (R25C.8)

Now `lambda-1<lambda log(lambda)`, `lambda<16/15`, `L=3e`, and (R25C.1) give

`R(lambda-1) < (16/15)*3e*R C_H(R) < (4/5)e`.

Hence the clean global range theorem

> **`Delta < Y[(4/5)e-3+3(2/3)^e]`.**                     (R25C.9)

This is stronger than the RL23 `~0.804 eY` upper bound and, importantly, contains the exact fixed-weight subtraction `3Y-3*2^e`.

By itself it still leaves the unwanted factor `e`.

---

## 3. Orientation matters: the `H>G` range loses a full baseline

Write

`x=R+G`, `y=R+H`, `0<G,H`, `G!=H`,

and put

`S_0=(B-Y)R`.

The exact block equations give

`U=S_0+BG`,

`V=S_0+BH-YG`,

`W=S_0-YH`.                                                (R25C.10)

Assume first

`H>G`.

Then

`U>S_0`,

and

`BH-YG=(B-Y)G+B(H-G)>0`,

so also

`V>S_0`.

Thus two of the three numerators lie strictly above `S_0`, while all three are at least `q_0`. Consequently the middle value is `>S_0`, and

`Delta < (U+V+W)-S_0-2q_0`.

Using

`x+y < R(z^2+z)`,

we obtain

> **`Delta < Y[R(lambda-z)-2+2(2/3)^e]`.**                (R25C.11)

Since

`lambda-z=z^3-z=z(z^2-1) < 2 lambda log z`,

(R25C.1)--(R25C.2) imply

`R(lambda-z) < (32/15)e R C_H(R) < (8/15)e`.

Therefore the increasing-orientation range satisfies

> **`Delta < Y[(8/15)e-2+2(2/3)^e]`.**                    (R25C.12)

Asymptotically this is a two-thirds version of the generic range coefficient.  This is a real orientation-sensitive gain, not a different linearization of the same bound.

---

## 4. Orientation/residue refinement of the cubic shortest vector

The universal low-state prefix `11` gives

`G=4N`, `H=4K`

with positive distinct integers `N,K`.

RL23's nonzero-mod-3 ownership gives

`3|N`, or `3|K`, or `3|(N-K)`.                             (R25C.13)

The cubic coordinates are

`U-W=4(YK+BN)`,

`V-W=4((B+Y)K-YN)`.                                       (R25C.14)

### Sector A: `G>H`

Here `N>K`.  The pair `(N,K)=(2,1)` violates (R25C.13), hence `N>=3`, and

> **`Delta >= 4(3B+Y)`.**                                  (R25C.15)

This is sharp at `(N,K)=(3,1)`.

### Sector B: `H>G`

Here `K>N`.  Again `(K,N)=(2,1)` is forbidden.  A short exact case split at `K=3` and `K>=4` gives

> **`Delta >= 4(2B+3Y)`.**                                 (R25C.16)

The value `2B+3Y` is attained at `(N,K)=(2,3)`.

Thus orientation alone already raises the relative lower scale from `~16Y` to `~20Y` when the later balanced state is larger.

### Residue split at the root

Because `4==1 (mod 3)`, if `R==2 (mod 3)`, the actual states

`R`, `R+4N`, `R+4K`

being nonzero modulo `3` force

`N,K !=1 (mod 3)`.

This excludes the weak `(3,1)` vector even when `G>H`; one obtains the same `~20Y` scale.  More precisely, the four orientation/residue sectors have minima

- `R==1 (mod3)`, `G>H`: `3B+Y` — **weak sector**;
- `R==1 (mod3)`, `H>G`: `3B+2Y`;
- `R==2 (mod3)`, `G>H`: `3B+2Y`;
- `R==2 (mod3)`, `H>G`: `2B+3Y`.

So the old RL23 shortest vector survives in exactly one sector:

> **`R==1 (mod3)` and `G>H`.**                             (R25C.17)

This is the new hard cubic sector.

---

## 5. Physical-gap consequence with common-prefix length `r`

The preceding orientation split can be made directly at the state-gap level.

If all three blocks share `r>=2` initial parity bits, write

`G=2^r N`, `H=2^r K`.

### If `H>G`

The forbidden `(2,1)` pair gives `K>=3`, hence

`H>=3*2^r`.

But `H<(z-1)R`, so by (R25C.3)

`3*2^r < (23/90)e`.

Therefore

> **`e > (270/23) 2^r`.**                                 (R25C.18)

In particular

- `r=2 => e>=47`;
- `r=3 => e>=94`;
- `r=4 => e>=188`.

### If `G>H`

Similarly `N>=3`, while `G<(z^2-1)R`.  From (R25C.4),

> **`e > (12150/2093) 2^r`.**                             (R25C.19)

Thus

- `r=2 => e>=24`;
- `r=3 => e>=47`;
- `r=4 => e>=93`.

This makes the asymmetry of the two balanced cuts explicit.  The later cut has the tighter `zR` height cap and therefore gives a much stronger consequence when it is also the larger physical gap.

---

## 6. The exact weak-vector equality pins the low residue geometry

Every near-minimum odd phase is `3 mod 4`.  A further elementary check excludes residue `3 mod 16`: if `s==3 (mod16)`, its first four parity bits are `1100` and

`T^4(s)=(9s+5)/16<R`

for `s<16R/15` and nontrivial `R`.  Hence every near-minimum balanced state lies in

`{7,11,15} (mod16)`.                                      (R25C.20)

In the unique weak cubic sector (R25C.17), equality in the shortest-vector bound forces

`N=3`, `K=1`.

At the universal shared prefix `r=2`, this means

`G=12`, `H=4`.

For `R`, `R+12`, and `R+4` all to lie in the allowed set (R25C.20), necessarily

`R==11 (mod16)`.

Together with the weak-sector condition `R==1 (mod3)`, this gives

> **`R==43 (mod48)`.**                                     (R25C.21)

The three four-bit prefixes are then exactly the three allowed classes

`1101`, `1110`, `1111`

in some fixed state order.

This is strategically important: the exact cubic lattice extremizer lands in the same modulo-48 root family as the inherited RL20 hard-root package (`43` or `91 mod144` are both `43 mod48`).  It does not prove those packages are identical, but it shows that the Track-B extremizer is not a generic residue phenomenon.

---

## 7. Exact finite terminal-pair localization

This section is **EXACT FINITE CERTIFICATE only** and is included to show what the analytic inequalities do at the first small near-resonant pairs.  Under the inherited external floor `R>=2^71`, the RL24 CF gate is vastly stronger than these small values.

An exact integer scan of

`1 < (2^b/3^e)^3 < 16/15`

for `e<188` gives only

`(b,e)=(65,41),(149,94),(214,135),(233,147)`.

Because `H>G` analytically forces `e>=47`, that orientation skips the only terminal pair below `94`; hence in the finite terminal arithmetic

> **`H>G => e>=94`.**                                      (R25C.22)

If one nevertheless inspects the first pair `(65,41)` without invoking the huge external CF floor, (R25C.3)--(R25C.4), `G>H`, nonzero-mod-3 ownership, and the allowed mod-16 low residues leave four coarse gap packages:

- `(G,H)=(12,4)`, `R==1 mod3`, `R==11 mod16`;
- `(12,8)`, `R==2 mod3`, `R==15 mod16`;
- `(16,4)`, `R==1 mod3`, `R==7 or 11 mod16`;
- `(20,8)`, `R==2 mod3`, `R==7 mod16`.

The monotone RL20 lift plus the exact floor `V>=q_0` gives, in the `G>H` orientation,

`x-y < z(z-1)R-z(1-(2/3)^e)`.                              (R25C.23)

At `e=41` the RL24 coarse cap makes the right side `<12`.  Therefore the two gap packages with `G-H=12` disappear, leaving only

> `(12,4)` in the `R==1 mod3`, `R==11 mod16` sector, or
>
> `(12,8)` in the `R==2 mod3`, `R==15 mod16` sector.        (R25C.24)

Again, this is a small finite localization, not a global RL theorem.

---

## Strategic consequence

RL25 makes the remaining Track-B defect much more precise.

The favorable three sectors gain either a stronger lattice vector, a stronger range upper, or both.  The truly resistant configuration is

> **root residue `R==1 mod3`, earlier balanced gap larger (`G>H`), and only the universal two-bit synchronization available.**

At exact shortest-vector equality this further collapses to

`G=12`, `H=4`, `R==43 mod48`.

That is now the natural target for any suffix-domination or block-endpoint argument.  A future theorem need not beat the entire `0.8 eY` range uniformly; it is enough to show that the two downward-oriented block numerators in this hard sector cannot simultaneously sit near their fixed-weight floor, or that the `43 mod48` state geometry forces additional synchronization/valuation ownership.

Verifier: `verify_rl25_cubic_range_orientation.py`.

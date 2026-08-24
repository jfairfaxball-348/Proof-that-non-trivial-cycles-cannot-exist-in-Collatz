# RL26 — five-bit low-state sieve and the cubic hard sector

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** for `R>=161` in the inherited near-resonant least-state branch. Section 6 contains an **EXACT FINITE TERMINAL-PAIR CERTIFICATE** used only to illustrate the small initial range. The inherited external floor `R>=2^71` is not used in the analytic residue sieve.

RL25 isolated the only cubic sector retaining the old shortest vector:

`R == 1 (mod3)`, `G>H`.

RL26 adds one more full-parity bit of genuine least-state ownership.  This is enough to show that the weak cubic vector survives in only one of the four possible near-minimum residue classes modulo `32`.

---

## 1. Near-minimum odd phases occupy only four classes modulo 32

RL21 already proved that every odd cycle phase

`R <= s < (16/15)R`

is `3 mod4`.

Thus modulo `32` the only candidates are

`3,7,11,15,19,23,27,31`.

Two pairs are immediately impossible.

### Residues `3,19 mod32`

They begin with full-parity prefix `1100`.  After four steps

`T^4(s)=(9s+5)/16`.

Using `s<16R/15`,

`T^4(s)<3R/5+5/16<R`

for every nontrivial least state in the present range.

### Residue `11 mod32`

The five-bit prefix is `11010`, and

`T^5(s)=(27s+23)/32`.

Hence

`T^5(s)<9R/10+23/32<R`

for `R>=161` (in fact for much smaller `R`).

### Residue `23 mod32`

The prefix is `11100`, and

`T^5(s)=(27s+19)/32<R`

under the same near-minimum bound.

Therefore every actual near-minimum odd phase satisfies

> **`s mod32 in {7,15,27,31}`.**                           (R26.1)

The verifier checks the complete five-bit affine table exactly.

A useful immediate corollary is that the inherited hard root beginning `1101` cannot continue with a zero.  A least hard root must actually begin

> **`11011...`**, hence `R==27 (mod32)`.                   (R26.2)

This is a genuine strengthening of the old `R==11 (mod16)` hard-root address.

---

## 2. Convert the mod-32 sieve into gap congruences

Stay in the RL25 hard cubic sector

`R==1 (mod3)`, `G>H`,

and use the universal shared prefix `11`:

`G=4N`, `H=4K`, `N>K>0`.

Because `R==1 mod3` and the two other balanced states are nonzero mod3,

`N,K !=2 (mod3)`.                                         (R26.3)

Now require all three states

`R`, `R+4N`, `R+4K`

to lie in the allowed set (R26.1).  According to the root residue modulo `32`, the possible gap quotients modulo `8` are

- `R==7 mod32`: `N,K mod8 in {0,2,5,6}`;
- `R==15 mod32`: `N,K mod8 in {0,3,4,6}`;
- `R==27 mod32`: `N,K mod8 in {0,1,3,5}`;
- `R==31 mod32`: `N,K mod8 in {0,2,4,7}`.                 (R26.4)

Intersecting these with (R26.3) and `N>K>0` gives the coordinate-minimal pairs

- `R==7 mod32`: `(N,K)=(10,6)`;
- `R==15 mod32`: `(N,K)=(4,3)`;
- `R==27 mod32`: `(N,K)=(3,1)`;
- `R==31 mod32`: `(N,K)=(7,4)`.                           (R26.5)

No approximation is involved; this is a finite congruence calculation modulo `24`.

---

## 3. Root-residue-specific cubic minima

For `G>H`, the first cubic coordinate

`YK+BN`

is positive and monotone in both `N,K`.  The coordinate-minimal pairs (R26.5) therefore give the exact sector minima:

> `R==7 mod32  => Delta >= 4(10B+6Y)`,
>
> `R==15 mod32 => Delta >= 4(4B+3Y)`,
>
> `R==27 mod32 => Delta >= 4(3B+Y)`,
>
> `R==31 mod32 => Delta >= 4(7B+4Y)`.                     (R26.6)

The verifier checks the full lattice expressions in representative near-resonant pairs and confirms that the second coordinate never lowers these exact minima.

Thus the RL23/RL25 weak vector

`4(3B+Y)`

survives **only** at

> **`R==27 (mod32)`.**                                    (R26.7)

Combining with the hard-sector residue `R==1 mod3` gives the single class

> **`R==91 (mod96)`.**                                    (R26.8)

This is a substantially sharper description of the cubic obstruction than the earlier `R==43 mod48` statement.

---

## 4. Physical-gap consequences in the other mod-32 sectors

RL25 proved

`H < (23/90)e`                                             (R26.9)

in the near-resonant order-3 branch.

The minimal `K` values in (R26.5) therefore give:

- `R==15 mod32`: `H>=12`, hence `e>=47`;
- `R==31 mod32`: `H>=16`, hence `e>=63`;
- `R==7 mod32`: `H>=24`, hence `e>=94`.                   (R26.10)

The weak root `27 mod32` has only `H>=4`, so this argument does not improve the global hard-sector threshold there.

The asymmetry is now explicit: all non-`27 mod32` hard-sector roots pay either a much larger cubic vector or a much larger mandatory later-state gap.

---

## 5. Interaction with the inherited hard-root package

The old hard-root branch had

`R==11 (mod16)`

and, after the RL20 mod-9 split,

`R==43 or 91 (mod144)`.

The forced fifth bit (R26.2) intersects these classes as

> `43 mod144` -> `187 mod288`,
>
> `91 mod144` -> `91 mod288`.                             (R26.11)

In particular the unique RL20 weak-close class

`R==91 mod144`, `n_close=t_close=1`

refines to

> **`R==91 (mod288)`**                                     (R26.12)

whenever the actual least-root five-bit continuation is included.

This does not by itself contradict the hard weak-close branch.  It simply removes half of the old 2-adic lifts.

### RL23 saturation witness refinement

RL23 recorded local packing saturation subfamilies with

`t==3 or 11 (mod24)`

as compatible with the then-frozen `R==91 mod144`, `R==11 mod16` package.

Adding the new least-root fifth-bit requirement `R==27 mod32` refines the parametric family to

> **`t==3 or 35 (mod48)`.**                                (R26.13)

Infinitely many saturation segments remain.  So this is a real sieve, not a destruction of the Track-A saturation mechanism.

---

## 6. Small terminal-pair consequence

This section is **EXACT FINITE CERTIFICATE only**.

For

`1<(2^b/3^e)^3<16/15`

with `e<94`, the only integer terminal pair is

`(b,e)=(65,41)`.

Every hard-sector root class other than `27 mod32` has analytic `e>=47` from Section 4 (and the `7 mod32` class already has `e>=94`).  Hence the first terminal pair can occur only in the unique weak root residue

`R==27 mod32`.

Combining the RL25 physical bounds, mod-3 ownership, and the five-bit sieve at `(65,41)` leaves only

`(G,H)=(12,4)`

with

`R==1 mod3`, `R==27 mod32`, i.e.

> **`R==91 mod96`.**                                      (R26.14)

The alternative RL25 small package `(12,8)` is eliminated because no root residue modulo `32` allows all three near-minimum states simultaneously.

Again, under the inherited external floor `R>=2^71`, the RL24 continued-fraction gate is enormously stronger than the small values in this section.  The value here is structural localization, not a new external-floor numerical bound.

---

## Strategic consequence

Track B is now concentrated on a very specific arithmetic geometry.

The genuinely weak order-3 sector requires all of the following simultaneously:

1. `G>H` (the earlier balanced state is the larger one);
2. `R==1 mod3`;
3. `R==27 mod32`, equivalently `R==91 mod96` after combining residues;
4. only the universal shared prefix `11` is available at the three-way level;
5. at exact shortest-vector equality, `(G,H)=(12,4)`.

The other mod-32 sectors already pay large cubic or physical-gap penalties.

This suggests a much narrower next attack than “remove the factor `e` globally”: attack the `R==91 mod96`, `G>H` sector using the newly forced root prefix `11011`, suffix ownership of the two downward macroblocks, or a block-type adjacency constraint.  The RL23 saturation family shows that residue information alone will still not be enough; the missing input must couple the weak cubic geometry to trajectory structure outside a single local block.

Verifier: `verify_rl26_cubic_mod32_hard_sector.py`.

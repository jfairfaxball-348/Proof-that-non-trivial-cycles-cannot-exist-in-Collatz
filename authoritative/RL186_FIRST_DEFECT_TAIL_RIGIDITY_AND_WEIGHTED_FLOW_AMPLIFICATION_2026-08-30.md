# RL186 — first-defect tail rigidity and weighted-flow amplification

Date: 2026-08-30

## 0. Outcome and classification

RL186 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

RL185 showed that every clean 40-edge shallow-start corridor contributes a selected nonzero defect of height at most 24 and converted that incidence into ordinary absolute corrected-flow variation `>150`. Its weakness was that a worst-case charge could place most selected defects near the late, high end of the window.

RL186 attacks the **first** defect. A zero prefix makes the physical numerator increasingly 2-adically constrained. At the first defect the numerator is odd, so the accumulated dyadic denominator is exactly recovered from the starting numerator valuation. This gives a closed arithmetic formula for the terminal numerator and permits complete exact enumeration of the late tail. The last offsets collapse sharply: offset 38 can only first-defect at height 23 and offset 39 only at height 24.

The extremal offset-39 run is also isolated from any later shallow start inside its zero block. Combining that with block packing caps the number of clean starts able to survive to offset 37. Feeding the resulting low/high split into RL185's flow charging raises the ordinary absolute-flow floor above 354 and both directional K-variation floors above 59.

Promoted results:

1. **RL186.1 — exact first-defect numerator law** (analytic).
2. **RL186.2 — late first-defect height vocabulary** (analytic + exact finite integer certificate).
3. **RL186.3 — refined first-defect coverage capacity** (analytic combinatorics + exact integer certificate).
4. **RL186.4 — tau-39 shallow isolation and tau>=37 block-capacity theorem** (analytic combinatorics + exact integer arithmetic certificate).
5. **RL186.5 — amplified weighted/signed corrected flow** (analytic + exact rational/integer certificate).

No correction/demotion event occurred.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `B=A-L=80448749305`.

Retain RL181:

- `128,081,997,553<K_i<146,795,909,391`;
- every normalized p-gap lies strictly in `(128,081,997,553,293,591,818,782)`;
- `K_(i+1)-K_i=f_i/3`;
- `1/2<rho_i<=1`.

Retain RL184/RL185:

- at least `10,075,174,499` clean 40-edge physical shallow-start corridors;
- every such corridor contains a nonzero ordinary defect;
- on a zero-defect common-mechanical transition `2^d C'=3C`, with `d>=1`;
- a 39-zero shallow-start run is rigid: `C_0=2^39`, every `d=1`, terminal common height 24 and terminal numerator `3^39`;
- ordinary flow `f_i=rho_i(2^-b-2^-a)`;
- exact full-period flow `F2` satisfies `0<F2<1/2`;
- the carry flow is positive `>1/2`.

All statements below remain internal to `(37,0,23,-1)`.

## 2. First-defect arithmetic

Fix one clean corridor and let `tau` be its first offset with `G_tau!=0`. RL184 gives `tau<=39`.

For `tau>0`, the prefix is homogeneous:

`2^D C_tau = 3^tau C_0`,
where `D=sum_(j=0)^(tau-1)d_j` and `D>=tau`.

Because `G_0=0`, the start has equal endpoint height `h_0 in {0,1}`. Hence its physical integer numerator obeys the strict interval

`2^h0 * 128,081,997,553 < C_0 < 2^h0 * 293,591,818,782`.

At the first defect `G_tau!=0`, so the RL183 parity sensor gives `C_tau` odd. Since `3^tau` is odd, taking 2-adic valuations in the homogeneous identity yields

`D=v_2(C_0)`.

Therefore

`C_tau = 3^tau odd(C_0)`,

and in particular `2^tau|C_0`.

This converts a long zero prefix from a qualitative divisibility statement into an exact terminal numerator.

## 3. Exact late-tail height vocabulary

For `tau>=28`, the shallow starting interval contains few enough multiples of `2^tau` for exhaustive exact integer enumeration. For each of the two starting heights, enumerate every

`C_0 = 2^tau k`

strictly inside its physical interval, compute `D=v_2(C_0)`, then

`C_tau=3^tau(C_0/2^D)`.

If the first-defect endpoint maximum is H, its normalized physical gap is `C_tau/2^H`. Retain every H satisfying both the inherited strict gap corridor and RL185's exact mechanical height envelope

`H<=1+ceil(tau B/L)`.

The complete necessary sets are:

| tau | possible H |
|---:|:---|
|28|7,8,9,10,11,12,13,14,15,16,17,18|
|29|8,9,10,11,12,13,14,15,16,17,18|
|30|10,12,13,14,15,16,17,18,19|
|31|12,13,14,15,16,17,18,19,20|
|32|13,15,16,17,18,19,20|
|33|15,16,17,18,19,20,21|
|34|16,18,19,20,21|
|35|18,19,20,21,22|
|36|19,20,21,22|
|37|21,23|
|38|23|
|39|24|

The enumeration is a necessary-capacity calculation only. It does not assert that every retained pair is physically realized.

The sharpest terminal facts are

- `tau=38 => H=23`;
- `tau=39 => H=24`.

## 4. First-defect coverage refinement

For offsets below 28, retain the conservative RL185 mechanical envelope. For offsets 28 through 39, use the exact table above.

A fixed physical phase selected as a **first** defect can correspond to at most one clean start for each admissible `tau`. Therefore the maximum number of starts it can discharge, by endpoint height `H=1,...,24`, is

`28,27,26,24,22,21,20,19,18,17,14,14,14,11,11,11,8,8,7,6,5,2,2,1`.

Every value satisfies

`cap_first(H)<=2^(24-H)`.

Since `|f_i|>2^-(H+1)`, this alone yields

`cap_first(H) < 2^25 |f_i|`.

Choosing the first defect in every clean corridor therefore gives

`sum_(ordinary i)|f_i|`
`> 10,075,174,499/2^25`
`>300`.

This is already a factor-two improvement in the universal charging constant over RL185.

## 5. The extremal tail cannot host another shallow start

The exact `tau=39` case carries more information than its endpoint height. RL184 gives

`C_0=2^39`, and `d_j=1` throughout the 39-zero run.

After the first zero transition,

`C_1=3C_0/2=3*2^38`.

If the edge at offset one were shallow and still zero-defect, its common height would be at most one, so its normalized gap would be at least

`C_1/2 = 3*2^37 = 412,316,860,416`,

contradicting the inherited upper gap bound `293,591,818,782`.

Thus offset one is not shallow. Moreover `d_j=1` and

`d_j=c_j+h_j-h_(j+1)`

on the common-height zero run, so

`h_(j+1)=h_j+c_j-1>=h_j`.

The common height is nondecreasing. No later zero edge in this extremal block can return to shallow height.

Now partition the cyclic defect sequence into zero blocks terminated by a nonzero defect. A clean shallow start with `tau>=37` can occur only at distance 37, 38, or 39 before the terminal nonzero edge.

- If distance 39 is shallow, the isolation theorem removes distances 38 and 37.
- Otherwise there are at most the two positions 37 and 38.
- A block with two such starts spans at least 39 phase positions.
- A block with only one has even smaller start density than `2/39`.

Summing over disjoint cyclic blocks gives

`N_37 := # clean starts with tau>=37`
`<= floor(2L/39)`
`= 7,052,720,272`.

Therefore

`10,075,174,499 - N_37`
`>= 3,022,454,227`

clean starts first-defect by offset 36. The late table then forces their selected defects to have `H<=22`.

## 6. Weighted-flow amplification

For a selected first defect of height H,

`|f_i|>2^-(H+1)`.

The refined coverage table gives, for `H<=22`,

`cap_first(H) 2^(H+1) <= 5*2^22 = 20,971,520`.

For `H=23,24`, the worst value is

`2^25 = 33,554,432`.

Let x be the number of clean starts whose first-defect height is at least 23. Section 5 gives `x<=7,052,720,272`. The charging lower bound is

`(10,075,174,499-x)/(5*2^22) + x/2^25`.

Because the high-height denominator is larger, the right side decreases with x, so the worst case is the maximum allowed x. Hence

`sum_(ordinary i)|f_i|`
`> 3,022,454,227/(5*2^22)`
`  + 7,052,720,272/2^25`
`= 7,430,404,397/20,971,520`
`>354`.

The full absolute flow is therefore `>354.5` after adding the positive carry. Write positive and negative flow masses P,N. The inherited exact signed total gives

`P-N=F2 in (0,1/2)`,

while

`P+N>354.5`.

Thus

`N>177` and `P>177`.

Since K drift is `f_i/3`, both directions of total K variation exceed 59.

Again, these are variation floors, not a monotone displacement or a prefix-excursion theorem.

## 7. What this changes and what remains

RL186 proves that the RL185 worst-case picture—most clean corridors hiding a first defect at the highest end of the window—is too generous. The last tail is arithmetically thin, and the maximal 39-zero configuration physically excludes additional shallow starts behind it.

Quantitatively, the ordinary absolute-flow floor improves from `>150` to `>354`, and each signed K-variation floor from `>25` to `>59`.

This remains far below the inherited K-corridor width of about `1.87e10`. It would be incorrect to infer a corridor escape or closure. The next useful step is therefore multiscale: bound `N_n=#{clean starts: tau>=n}` at several n, including the middle of the 40-edge window, and integrate that whole survival distribution into the weighted charging.

## 8. Red-team scope

- **Physical starts:** every counted start is an RL184 clean physical shallow-start corridor.
- **First defect:** selection is canonical; no corridor chooses a later defect to improve the bound.
- **Parity:** oddness is used only at the first nonzero ordinary defect.
- **Strict intervals:** both start and terminal numerator tests preserve the strict RL181 normalized-gap inequalities.
- **Enumeration:** all shallow multiples are included; retained candidates remain necessary, not asserted realized.
- **Tail packing:** the `2/39` argument is a cyclic zero-block density bound, not an independence assumption.
- **Charging:** low/high classes partition selected defects before summation.
- **Carry:** excluded from ordinary charging and added only in the global signed-flow calculation.
- **Variation/excursion:** no total variation is promoted as net K displacement.
- **Historical barriers:** no generic lattice/rank or unconstrained local-template route is revived.
- **No false closure:** the surviving high type and all global closure targets remain open.

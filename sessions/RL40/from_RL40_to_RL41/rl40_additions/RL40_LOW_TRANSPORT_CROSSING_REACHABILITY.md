# RL40 — crossing-aware low-transport reachability through area 17

Date: 2026-08-21

## Status

**ANALYTIC reduction + EXACT FINITE local certificate.**

This note strengthens the inherited RL37 lower bound

`rho >= 16`

to

> **`rho >= 18`**

in the surviving near-resonant order-2 / `g=2` balanced-return branch.

It does **not** close RL or the full `g=2` branch.  The new mechanism is a finite-state refinement of RL37/RL38: the sign-reversal budget is first restricted to excursions that satisfy the exact integer crossing congruence, and then the small residual cases are propagated using the exact physical-gap map between synchronized boundaries.

## 1. Inherited setup

Retain

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`, `z=X/Y>1`,

with `z^2<16/15`, least cycle state `R`, balanced half-state `R+G`, and total transport area

`rho=sum_j |d_j|`.

In the audited near-minimum `g=2` branch:

- `R` and `R+G` are odd;
- `4|G`;
- RL37 gives the strict sign-reversal budget

  `sum_E S(E) > G(1+1/z)`;

- RL38 gives the exact distortion product

  `prod_E J_E=z>1`;

- a positive canonical excursion with local data `(D,h,p)` crosses an incoming positive odd physical gap `g` to negative magnitude `g_out` exactly when

  `D-3^p g = 2^h g_out >0`;

- no integer physical sign-changing excursion exists for transport area `<=6`.

For an area-`r` canonical excursion, let `E(r)` be the inherited RL37 strong envelope.  Define the **crossing-aware envelope** `C(r)` as the maximum strong contribution among area-`r` positive canonical excursions that admit at least one positive odd integer crossing input `g`.

The bundled verifier enumerates all canonical positive excursions through area 17 exactly.

## 2. Exact synchronized-gap reachability lemma

Suppose an excursion ends at a synchronized prefix-count boundary with nonzero integer physical gap `Delta`.

If `Delta` is odd, the two states have opposite parity, so the next column must immediately open another excursion.

If

`|Delta| = 2^s m`, with `m` odd,

then while the trajectories remain synchronized their parity bits agree.  A common even step maps the gap to `Delta/2`, while a common odd step maps it to `3Delta/2`.  Either way, the `2`-adic valuation of the gap drops by exactly one.  Therefore the synchronized run lasts exactly `s` columns before the gap becomes odd again.

If `c` of those `s` common columns are odd, the next excursion begins with physical gap

> `sign(Delta) * m * 3^c`, with `0<=c<=s`.                 (R40.1)

For reachability it is safe to allow every `c` in that range; this is an over-approximation of the actual parity dynamics.

At the terminal synchronized suffix, RL36 gives common suffix odd weight at most `v3(G)`.  Once `G=4`, this is zero.  Hence the terminal suffix contains only even common steps.  Therefore if `Delta_last` is the gap immediately after the final excursion, a necessary endpoint condition is

> `Delta_last = -4*2^s` for some `s>=0`.                  (R40.2)

## 3. Area 16 elimination

The exact area-16 envelope is

`E(16)=22300/2187 < 31/2`.

Thus a hypothetical `rho=16` return cannot have `G>=8`, because `z<16/15` gives

`G(1+1/z)>31/2` for `G>=8`.

Since `4|G`, necessarily `G=4`.

The inherited exact common-prefix theorem then gives prefix length `v2(G)=2`; leastness excludes prefix `10`, so the common prefix is exactly `11`.  Consequently the physical gap at the first excursion is fixed:

> **`g_first=9`.**                                        (R40.3)

Requiring one part of the transport partition to be a genuine crossing excursion leaves only

`(16)`, `(14,2)`, `(14,1,1)`

as crossing-aware budget-viable partitions of 16.

### `(16)`

A single area-16 crossing must itself exceed the `31/4` budget.  Exact enumeration leaves three crossing-capable candidates:

- `(D,h,p,g,g_out)=(27875,11,7,9,4)`,
- `(9199,10,6,7,4)`,
- `(44815,12,7,13,4)`.

Only the first is compatible with the fixed first gap `9`.  Its distortion is

`J=8192/19683<1`.

With one excursion, RL38 would require `J=z>1`, contradiction.

### `(14,2)` and `(14,1,1)`

Area 2 cannot cross, so the area-14 part must be the crossing.  After subtracting the maximal small-part envelopes from the `31/4` budget, exact enumeration leaves the same unique area-14 crossing candidate in both partitions:

`(D,h,p,g,g_out)=(17669,11,6,13,4)`.

Thus the crossing would require incoming gap `13`.

Starting from `g_first=9`, the complete integral area-2 transition set contains only

`9 -> 3`,

and the area-1 transitions are forced

`9 -> 7 -> 5`.

All of `3,5,7` are odd, so by (R40.1) no nonempty synchronized run can alter them before the next excursion.  Hence an area-14 crossing can only begin at `9,7,5`, or `3`, never `13`.

Therefore `rho=16` is impossible.

## 4. Area 17 crossing-aware partition reduction

The exact unrestricted area-17 envelope is

`E(17)=28361/2430 <31/2`,

so the same argument again forces

> **`G=4` and `g_first=9`.**

Requiring a genuine crossing part reduces all integer partitions of 17 to exactly these budget-viable possibilities:

`(17)`,
`(16,1)`,
`(15,2)`,
`(15,1,1)`,
`(14,3)`,
`(14,2,1)`,
`(14,1,1,1)`,
`(12,5)`,
`(12,4,1)`.

In each case the crossing part is the unique largest part displayed.

For each partition, the verifier enumerates only crossing candidates whose strong contribution is large enough that the remaining parts could possibly complete the strict `31/4` budget.  It then propagates the exact local gap map

`Delta_out=(3^p Delta_in - sigma D)/2^h`,

where `sigma=+1` for a positive prefix-count excursion and `sigma=-1` for a negative one, with:

- positive physical gap before the designated crossing;
- negative physical gap after it;
- no sign change in the small area-`<=5` excursions, since RL38 excludes crossings through area 6;
- synchronized-boundary propagation by the safe reachability rule (R40.1);
- terminal condition (R40.2);
- total strong envelope strictly exceeding `31/4`.

This exact/superset search leaves only three distinct physical configurations (one canonical numerator occurs in two word shapes in the first case).

## 5. The three surviving area-17 configurations all have distortion product `<1`

### Case A: one area-17 excursion

The only endpoint-compatible crossing type has

`g: 9 -> -4`,

`D=91817`, `h=13`, `p=8`.

Its distortion is

`J = 32768/59049 <1`.

Since it is the only excursion, `prod J_E=J<1`, contradicting `prod J_E=z>1`.

### Case B: `(1,16)`

The only endpoint-compatible order is an area-1 excursion followed by the crossing area-16 excursion:

`9 -> 7 -> -4`.

The first excursion is the negative-prefix-count orientation of the unique area-1 type, so

`J_1 = 28/27`.

The crossing area-16 type has

`D=9199`, `h=10`, `p=6`, `g:7->-4`,

hence

`J_16 = 4096/5103`.

Therefore

> `J_1 J_16 = 16384/19683 <1`,

again contradicting `prod J_E=z>1`.

### Case C: `(15,2)`

The only endpoint-compatible order is

`9 -> -4`,

then a synchronized run reaching `-3`, then

`-3 -> -4`

through the area-2 type `D=5,h=3,p=2`.

The distortions are

`J_15=16384/19683`,

`J_2=32/27`,

so

> `J_15 J_2 = 524288/531441 <1`.

Again this contradicts `prod J_E=z>1`.

Thus every `rho=17` possibility is impossible.

## 6. Conclusion

Combining Sections 3--5 gives the new certified low-transport floor

> **`rho >= 18`.**                                        (R40.4)

This strictly strengthens RL37/RL39's inherited `rho>=16` statement.

## 7. Strategic meaning

The successful ingredient is not a larger blind enumeration.  It is the state compression:

1. crossing-aware strong-envelope pruning;
2. exact physical gap at the first excursion (`9` when `G=4`);
3. synchronized-gap reachability determined by `v2(Delta)` and the number of common odd steps;
4. exact endpoint gap `-4` with zero terminal odd weight;
5. RL38's global product identity `prod J_E=z>1`.

This suggests a finite-state dynamic program for the next phase.  Rather than enumerate all canonical words up to a large total area, one can propagate only excursion summaries

`(r,D,h,p,strong,crossing-input/output)`

through a small gap state space, pruning by the remaining sign-reversal budget and the distortion-product requirement.

That is likely more scalable than the original raw canonical-excursion enumeration and can be combined later with RL39's odd/valuation charge once low transport is pushed far enough.

Verifier: `verify_rl40_low_transport_reachability.py`.

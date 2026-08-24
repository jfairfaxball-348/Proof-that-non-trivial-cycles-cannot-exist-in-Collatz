# RL40 — crossing-aware elimination of total transport area 16

Date: 2026-08-21

## Status

**ANALYTIC reduction + EXACT FINITE local certificate.**

This note strengthens the inherited RL37 conclusion `rho >= 16` to

> **`rho >= 17`**

in the surviving near-resonant order-2 / `g=2` balanced-return branch.

It does **not** close RL or the full `g=2` branch.  The gain comes from combining the RL37 sign-reversal budget with the RL38 *integer* crossing condition and the already-established `G=4`, common-prefix `11` geometry.  The key point is that a crossing excursion is not an arbitrary canonical excursion: its incoming physical gap is constrained by exact divisibility.

## 1. Inherited setup

Retain

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`, `z=X/Y>1`,

with `z^2<16/15`, least odd cycle state `R`, balanced half-state `R+G`, and transport area

`rho = sum_j |d_j|`.

In the near-minimum `g=2` branch:

- `R` and `R+G` are odd;
- `4|G`;
- RL37 gives the strict sign-reversal budget

  `sum_E S(E) > G(1+1/z)`,

  where each excursion has the certified strong envelope `S(E) <= E(r_E)`;
- RL38 shows the first physical sign change must occur in a positive excursion satisfying the exact integer crossing congruence

  `3^p g-D = -2^h g_out`,

  with positive odd incoming gap `g` and positive integer outgoing magnitude `g_out`;
- every integer crossing has area at least `7`.

The RL37 strong envelopes through area 15 are retained.  The new exact enumeration at area 16 gives

`E(16)=22300/2187`.

## 2. Crossing-aware envelopes

For each area `r`, define `C(r)` to be the maximum RL37 strong contribution among canonical positive area-`r` excursions that admit at least one positive odd integer incoming gap satisfying the RL38 crossing congruence.

The exact verifier enumerates all canonical positive excursions through area 16.  It confirms there are no crossing excursions for `r<=6`, and computes the crossing-aware maxima for `7<=r<=16`.

The only fact needed for the new global step is the crossing-aware partition test at total area 16.

A total-area partition can support the sign-reversal budget only if at least one part is a genuine crossing part.  With this requirement, the exact verifier proves that the only partitions of 16 whose maximum possible strong sum exceeds `31/4` are

> `(16)`, `(14,2)`, `(14,1,1)`.

All other partitions are eliminated before any word-level case analysis.

## 3. Area 16 still forces `G=4`

The unrestricted area-16 envelope is

`E(16)=22300/2187 < 31/2`.

Because `z<16/15`, if `G>=8` then

`G(1+1/z) > 8(1+15/16)=31/2`,

which is already larger than the maximum total area-16 envelope.  Since `4|G`, every hypothetical `rho=16` return therefore has

> **`G=4`.**

The inherited integer-gap synchronization theorem says the common prefix length is exactly `v2(G)=2`.  RL37's least-state argument excludes prefix `10`, so the common prefix is exactly

> **`11`.**

Thus at the first divergence the physical gap is fixed:

`g_first = 3^2*4/2^2 = 9`.                                 (R40.1)

This fixed incoming gap is the decisive extra datum.

## 4. Eliminate the one-excursion partition `(16)`

For a single area-16 excursion, the crossing excursion is the only excursion.  Since its strong contribution must by itself exceed `31/4`, exact enumeration leaves exactly three crossing-capable canonical candidates:

1. `D=27875, h=11, p=7`, crossing `g=9 -> g_out=4`,
2. `D=9199, h=10, p=6`, crossing `g=7 -> g_out=4`,
3. `D=44815, h=12, p=7`, crossing `g=13 -> g_out=4`.

By (R40.1), only the first candidate can occur as the first excursion.

Its distortion is

`J = 2^11*4/(3^7*9) = 8192/19683 < 1`.

But RL38 gives the exact excursion product identity

`prod_E J_E = z > 1`.

With only one excursion this would force `J=z>1`, contradiction.

Hence `(16)` is impossible.

## 5. Eliminate `(14,2)`

Area 2 cannot cross, so the area-14 excursion must be the physical crossing.

To exceed the strict `31/4` budget, its strong contribution must exceed

`31/4 - E(2) = 773/108`.

Exact enumeration leaves a unique crossing-capable area-14 candidate above this threshold:

`D=17669, h=11, p=6`,

with the unique integer crossing

> **`g=13 -> g_out=4`.**                                  (R40.2)

If the area-14 crossing is first, its incoming gap is `9`, contradicting (R40.2).

Otherwise the area-2 excursion occurs first.  Starting from gap `9`, the complete canonical area-2 list consists of

- `D=3,h=3,p=1`,
- `D=5,h=3,p=2`.

Using the two orientation signs in the local gap map

`Delta_out=(3^p Delta_in +/- D)/2^h`,

only one integral transition exists from `Delta_in=9`:

`(3*9-3)/8 = 3`.

So an area-2 first excursion can only send the positive gap `9 -> 3`.

The resulting gap is odd.  Two synchronized integer states with odd difference have opposite parity, so no nonempty synchronized run can intervene before the next excursion.  Therefore the area-14 crossing would have incoming gap `3`, not `13`.

Thus `(14,2)` is impossible.

## 6. Eliminate `(14,1,1)`

Again the area-14 excursion must be the crossing.  To exceed the budget it must contribute more than

`31/4 - 2E(1) = 29/4`.

The exact crossing enumeration again leaves the same unique area-14 candidate (R40.2), requiring incoming gap `13`.

The unique area-1 canonical type has `D=1,h=2,p=1`.  From incoming gap `9`, the two orientation maps are

`(27-1)/4` and `(27+1)/4`.

Only the second is integral, giving

`9 -> 7`.

The gap `7` is odd, so there is no nonempty synchronized run before a second excursion.  From gap `7`, the two area-1 orientation maps are

`(21-1)/4=5`,

`(21+1)/4`,

and only the first is integral.  Hence two area-1 excursions before the crossing can only give

`9 -> 7 -> 5`.

Accordingly, depending on whether zero, one, or two area-1 excursions precede the crossing, its incoming gap can only be `9`, `7`, or `5`.  None equals the required `13`.

Thus `(14,1,1)` is impossible.

## 7. Conclusion

Every total-area-16 partition is impossible.  Therefore any genuine surviving near-resonant order-2 / `g=2` balanced return satisfies

> **`rho >= 17`.**                                        (R40.3)

This is a strict strengthening of RL37's `rho>=16` floor.

## 8. Strategic consequence

The result also clarifies the useful role of RL38: imposing the *integer crossing congruence* before taking the sign-reversal envelope is materially stronger than treating the crossing as an arbitrary high-contribution excursion.

For the next step, the same method can be pushed to `rho=17`, but the crossing-aware viable partition list grows.  The more scalable target is to combine this fixed first-gap geometry with RL39's odd/valuation charge or with a finite-state reachability DP that tracks only:

- transport spent,
- current physical gap at synchronized boundaries,
- whether the physical sign crossing has occurred,
- the strong-envelope budget still required.

Such a DP would avoid enumerating irrelevant canonical words and may extend the low-transport closure substantially farther than 17.

Verifier: `verify_rl40_crossing_aware_area16.py`.

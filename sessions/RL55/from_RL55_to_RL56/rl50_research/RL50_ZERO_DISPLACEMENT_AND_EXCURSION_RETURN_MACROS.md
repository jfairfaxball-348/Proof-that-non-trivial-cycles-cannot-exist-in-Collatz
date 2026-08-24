# RL50 — zero-displacement coupling and height-one excursion-return macros

Date: 2026-08-22

## Status

**ANALYTIC IDENTITIES + DENOMINATOR-INDEPENDENT EXACT FINITE CAP CERTIFICATES.**

This note does not prove Gate A.  It sharpens the coupling in two directions that were still separate in the earlier RL50 notes:

1. the rank defect `E` is rewritten as a positive weighted version of the **zero displacement vector whose unweighted sum is exactly the area `H`**;
2. every complete return excursion from height one back to height one is compressed to two nonnegative macro masses, giving an exact monotone return coordinate and a small total excursion-growth budget on the sole safe continued-fraction survivor.

A third consequence replaces the old independent per-zero cap by the actual sequential `x`-prefix dynamics.  This raises the uniform full-phase zero count from `z>=17` to `z>=20`, and raises the sole safe continued-fraction survivor from `z>=20` to `z>=27`.

## 1. Zero positions carry the same area as the moved-one ranks

Let the internal words `x,y` have the same length and the same number of ones.  Write their zero positions (zero-indexed) as

`u_1<...<u_s`, `v_1<...<v_s`,

where `s=z-1` is the number of internal x-zeros (and also internal y-zeros).

The retained one-excursion condition is

`d_i = 1 + p_y(i)-p_x(i) >= 1`

at every internal prefix.  Equivalently, every prefix of `x` contains at least as many zeros as the corresponding prefix of `y`.  Therefore

`u_j <= v_j`

for every `j`.  Put

`r_j := v_j-u_j >= 0`.

Since the two words have the same length and weight, complementing the one-position identity

`H = sum_j (a_j-b_j)`

gives the exact zero-position identity

`boxed: H = sum_{j=1}^s r_j}`.

Thus the area is literally the total rightward displacement of the y-zeros relative to the x-zeros.

## 2. The phase/rank defect is the weighted zero displacement

Before the `j`-th x-zero at position `u_j`, exactly `u_j-j+1` x-ones have occurred.  Its x-prefix weight is therefore

`w_j = 2^(u_j) / 3^(u_j-j+1)`.

Before the matching y-zero at `v_j=u_j+r_j`, the number of y-ones is larger by exactly `r_j`.  Hence its y-prefix zero weight is

`w_j * (2/3)^(r_j)`.

Summing the exact zero masses gives

`Zx = sum_j w_j`,

`Zy = sum_j w_j (2/3)^(r_j)`.

Since RL49/RL50 proved `E=Zx-Zy`, we obtain the exact positive decomposition

`boxed: E = sum_j w_j [1-(2/3)^(r_j)]}`.

Together with the previous section,

`boxed: H=sum r_j,   E=sum w_j[1-(2/3)^(r_j)]}`.

This is the cleanest direct interface yet between Gate A's unweighted area and the phase-forced rank defect.  It also shows immediately that every displaced zero (`r_j>=1`) contributes at least `w_j/3` to `E`.

A zero with `r_j=0` is an aligned `00` column at height one: the two prefixes have the same zero count and therefore the same one count at that position.

## 3. Exact return coordinate for complete height-one excursions

At height one put

`L := g(J-1)/2 = gT/2`.

For any segment whose two endpoints are both at height one, define

`X_seg = sum x_i g_i/3`,

`S_seg = sum y_i g_i/3^(d_i)`,

`E_seg = X_seg-S_seg`.

The all-height `R` increment from RL50 is

`Delta R = (g/3)(x-y/3^d)`.

Since `L=(3/2)R` at height one, telescoping any height-one-to-height-one segment gives

`boxed: Delta L = S_seg + (3/2)E_seg}`.

Now take a **complete excursion macro**: it starts with a height-one `01`, has no intermediate height-one state, and ends on the first `10` return to height one.  Using

`Delta g = Zx_seg-X_seg`

and `W=(2L+g)/3` at height-one endpoints, the local defect-energy definition telescopes exactly to

`boxed: sum_exc epsilon = 2 E_exc}`.

Every excursion column with `y=1` satisfies `epsilon >= 2 Delta S`; the remaining excursion columns have `Delta S=0`.  Therefore

`boxed: 0 <= S_exc <= E_exc}`,

and hence

`boxed: (3/2)E_exc <= Delta L_exc <= (5/2)E_exc}`.

So successive height-one return values of `L` are monotone across every genuine excursion.  Height-one synchronized `00/11` pieces have `E=0`; consequently the global defect is the sum of the nonnegative excursion defects.

### Safe-survivor endpoint consequence

On the sole safe sub-Legendre survivor RL50 proved

`E<5/3`.

Therefore all complete excursions combined can increase `L` by less than

`(5/2)E < 25/6`.

Before the first positive height-one return, the synchronized negative grammar cannot make `L` positive.  Thus the first positive height-one return satisfies

`boxed: L_+ < 25/6}`.

The safe prefix cap gives `g<17/15` at every prefix, so at that return

`W=(2L+g)/3 < 142/45`.

This is a denominator-independent first-positive-return window.  It does not yet force the terminal valuation, but it is the intended compressed state for the next return-to-terminal attack.

## 4. Sequential prefix cap: zeros cannot all sit independently at the cap

The earlier zero-budget theorem used only the pointwise fact that an x-zero has weight `<17/30`.  The exact x-prefix scalar has more structure:

- start `g=1`;
- an x-one sends `g -> (2/3)g`;
- an x-zero sends `g -> 2g`;
- every prefix has `g<17/15` under the safe phase squeeze;
- therefore an x-zero is legal only when its pre-zero weight is `<17/30`.

So a zero near the cap forces subsequent x-ones before another near-cap zero can occur.  The companion exact verifier treats the relaxed non-strict cap `g<=17/30`, which can only enlarge the admissible class.

For `r` future zeros from a current scalar `g`, two rigorous future-mass bounds are

`future Zx <= r*(17/30)`

and, even if all future x-one contractions and the cap are discarded,

`future Zx <= (2^r-1)g`.

These give a finite exact branch-and-bound search despite allowing arbitrarily many x-ones between zeros.

The exact rational certificate proves:

- with at most **18** x-zeros, `Zx <= 17/2` in the relaxed sequential-cap process;
- with at most **25** x-zeros, `Zx <= 143/12` in the relaxed sequential-cap process.

No denominator, continued-fraction length, or area cutoff enters this finite control problem.

## 5. New uniform zero-count theorem: `z>=20`

Every genuine full-phase object satisfies the exact identity

`3Zx-Zy = 12 + (27/2)zeta(1+2^-k)`.

Since `Zy>=0` and `zeta>1`,

`Zx>17/2`.

But the sequential-cap certificate proves that 18 x-zeros cannot exceed `17/2`.  Hence every retained genuine full-phase object above the safe `2^71` floor has at least **19 internal x-zero columns**:

`boxed: # internal x-zero >=19}`,

so

`boxed: z>=20}`,

`boxed: t<=q-20}`.

This supersedes the earlier RL50 uniform bound `z>=17`.

## 6. Sole safe continued-fraction survivor: `z>=27`

For the unique safe sub-Legendre survivor, RL50 proved

`E<5/3`.

Using `E=Zx-Zy`, the same exact zero identity becomes

`2Zx+E = 12 + (27/2)zeta(1+2^-k) > 51/2`.

Therefore

`2Zx > 51/2 - 5/3 = 143/6`,

so

`boxed: Zx>143/12}`.

The sequential-cap certificate proves that 25 x-zeros cannot exceed `143/12`.  Thus this explicit survivor requires at least **26 internal x-zero columns**:

`boxed: # internal x-zero >=26}`,

and hence

`boxed: z>=27}`,

`boxed: t<=q-27}`.

This supersedes the earlier candidate-specific `z>=20` bound.

## 7. Additional free-grammar localization

Because every displaced zero contributes at least `w_j/3` to `E`, the total x-zero mass on displaced zeros is at most `3E<5` on the safe survivor.  Since `Zx>143/12`, aligned height-one `00` columns carry mass

`Z00_free > 143/12-5 = 83/12`.

With the per-zero cap `<17/30`, this forces at least **13** aligned height-one `00` columns globally.

The inherited energy localization also gives

`S_11,free >115/12`.

Each height-one `11` contributes `<17/45`, hence there are at least **26** height-one `11` columns globally.

These counts do not by themselves close Gate A because the initial negative Collatz-conjugate grammar can contain arbitrarily many zero-energy columns.  Their value is as endpoint/macro constraints when combined with the first-positive-return window above.

## 8. What remains open

The new identity

`H=sum r_j`, `E=sum w_j[1-(2/3)^r_j]`

shows exactly why a scalar `E` bound alone cannot prove Gate A: a very late x-zero can have tiny `w_j`, allowing a large displacement `r_j` at little defect cost.  The missing ingredient must therefore use the terminal power condition `J=2^k` (or an equivalent macro-endpoint arithmetic constraint) to prevent all of the required area from being hidden on tiny late weights.

The next attack should start from the first positive height-one return with

`L<25/6`, `W<142/45`,

compress every subsequent excursion by `(E_exc,S_exc,Delta L_exc)`, and run the terminal power-of-two condition backwards through the intervening height-one synchronized blocks.

## Verification

Run

`python3 rl50_research/verify_rl50_zero_displacement_excursion_macros.py`.

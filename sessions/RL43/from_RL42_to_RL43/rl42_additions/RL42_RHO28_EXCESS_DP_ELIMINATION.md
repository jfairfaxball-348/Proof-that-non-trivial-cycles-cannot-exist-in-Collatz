# RL42 — excess-DP elimination of `rho=28`

Date: 2026-08-22

## Status

**ANALYTIC reduction + EXACT FINITE / SAFE-SUPERSET certificate.**

Together with `RL42_LIGHTWEIGHT_RHO28_RECONSTRUCTION.md`, this proves

> # **`rho >= 29`**

in the surviving near-resonant order-2 / `g=2` balanced-return branch.

RL itself remains open.

Companion verifier:

`verify_rl42_rho28_excess_dp.py`.

## 1. Why area 28 collapses in excess coordinates

Retain

`rho = P + E`,

where

`P=sum_E p_E`

is the displaced-rank / excursion-owned odd mass and

`E=sum_E e_E`, `e_E=r_E-p_E>=0`.

The analytic prefix-cap theorem gives

`P_+ > (45/8)G`,

with `4|G`.  At `rho=28`, a hypothetical return therefore has `G=4` and

`P_+>=23`.

The bounded local certificate in `RL42_LIGHTWEIGHT_RHO28_RECONSTRUCTION.md` shows that every physical crossing occurring in a `rho<=28` candidate has excess at least four.  Hence

`P<=24`.

Since `P>=P_+>=23`, there are only two mass/excess cases:

> **Case I:** `P=24`, `E=4`;
>
> **Case II:** `P=23`, `E=5`.

No raw area-28 excursion table is needed.

## 2. Local crossing data through excess five

The verifier streams every canonical positive excursion with

`e<=5`, `p<=24`.

Total word counts are

- `e=0`: 24;
- `e=1`: 300;
- `e=2`: 2,876;
- `e=3`: 22,403;
- `e=4`: 149,709;
- `e=5`: 886,240.

Only the local data needed by the two global cases are retained.

There are exactly 20 crossing-capable `e=4` local types.  Every one requires

`g=1 -> -4`,

and satisfies

`h=p+3`,

`D=3^p+4*2^h`.

There are 42 crossing-capable `e=5` local types.  Again,

> **every one requires incoming physical gap `g=1`.**     (R42A28.1)

The `e=0` and `e=1` noncrossing types are propagated exactly at excursion boundaries.

## 3. Safe synchronized-run propagation and exponent recovery

For `G=4`, the inherited exact prefix theorem forces common prefix `11`, hence

`g_first=9`.

If an excursion ends at integer gap

`Delta=sign*2^s m`, `m` odd,

then before the next excursion the synchronized run has exactly `s` columns.  If `c` of them are common odd columns, the next excursion begins at

`sign*m*3^c`.

The verifier deliberately allows **every** `c` in `0,...,s`.  This is the inherited safe over-approximation: it may add false paths but cannot delete a genuine one.

This propagation also recovers the half-exponents.  An excursion contributes `(h,p)`.  A synchronized run contributes `(s,c)`.  The initial common prefix contributes `(2,2)`.

At the terminal end, `v3(G)=0`, so the common suffix contains only even steps.  Thus if the final excursion ends at

`Delta_last=-4*2^t`,

the terminal suffix contributes `(t,0)`.

Therefore every endpoint-compatible abstract path determines exactly

`a = 2 + sum h_E + sum s_sync + t`,

`ell = 2 + sum p_E + sum c_sync`.                         (R42A28.2)

The near-resonant branch requires

`1 < 2^a/3^ell`,

`(2^a/3^ell)^2 < 16/15`.                                  (R42A28.3)

Both inequalities are tested with exact integer arithmetic.

## 4. Case I: `P=24`, `E=4`

The mandatory crossing consumes all excess, so:

- exactly one `e=4` excursion is the physical crossing;
- every other excursion has `e=0`.

Since `P_+>=23`, the total negative-prefix odd mass is at most one.  Thus either every excursion is positive, or there is exactly one negative-prefix `e=0,p=1` excursion.

The safe-superset DP explores 6,613 synchronized-boundary states.  It finds 134 distinct endpoint exponent/tag records before imposing the near-resonant window.

Inside (R42A28.3), only

> `(a,ell)=(46,29)` and `(65,41)`                        (R42A28.4)

survive.

Crucially, **every** surviving path used the unique negative `p=1` excursion.  Hence every Case-I survivor has

`P_+=23`.                                                  (R42A28.5)

## 5. Case II: `P=23`, `E=5`

Here `P=P_+=23`, so every prefix-count excursion is positive.

There are only two excess partitions compatible with a physical crossing.

### IIa. One `e=5` crossing

All remaining excursions have `e=0`.

The safe DP explores 46 states and finds

> **zero terminal-compatible endpoints.**                 (R42A28.6)

### IIb. One `e=4` crossing plus one `e=1` excursion

All remaining excursions have `e=0`.

The safe DP explores 5,445 states and finds 123 distinct endpoint exponent/tag records.  After the near-resonant window, only

> `(a,ell)=(46,29)`                                       (R42A28.7)

remains.

But every Case-II path has

`P_+=23`.                                                  (R42A28.8)

## 6. The exact moved-mass bound kills every resonance survivor

For `G=4`, the analytic z-dependent inequality is

> `P_+ > 12(z+1)/z^2`.                                    (R42A28.9)

At both surviving exact ratios

`z=2^46/3^29`,

`z=2^65/3^41`,

exact integer arithmetic gives

`12(z+1)/z^2 > 23`.

Therefore

> **`P_+>=24`**                                            (R42A28.10)

at either resonance.

This contradicts (R42A28.5) for every Case-I survivor and (R42A28.8) for every Case-IIb survivor.  Case IIa already has no endpoint.

Hence `rho=28` is impossible.

## 7. Conclusion

The independently reconstructed RL42 floor `rho>=28` plus the present elimination gives

> # **`rho >= 29`.**                                      (R42A28.11)

This is stronger than the RL41 checkpoint and is reproducible without the missing area-26/27 transient search artifacts.

## 8. Strategic consequence

The excess coordinate is now demonstrably the right low-transport parameter.  Instead of hundreds of millions of raw area words, the global search sees only a few mass/excess partitions and a few thousand safe boundary states.

At `rho=29`, the only top-level possibilities are

- `(P,E)=(25,4)`;
- `(24,5)`;
- `(23,6)`.

Thus the next layer can again be attacked by bounded excess families (`e<=6`) and exact physical-gap / exponent propagation, reserving absolute numerator congruences only for any genuine near-resonant survivors.

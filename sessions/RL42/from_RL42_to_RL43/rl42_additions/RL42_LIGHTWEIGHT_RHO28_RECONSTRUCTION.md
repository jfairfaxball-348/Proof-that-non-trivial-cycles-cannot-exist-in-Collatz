# RL42 — lightweight reconstruction of the `rho >= 28` checkpoint

Date: 2026-08-22

## Status

**ANALYTIC reduction + EXACT FINITE local certificate.**

This note reconstructs the RL41 working checkpoint

> **`rho >= 28`**

without the transient billion-scale area-26/27 excursion tables that were not retained in the RL41 handover.

The proof uses the analytic RL42 moved-rank and prefix-cap theorems, plus a new exact enumeration parameterized by **excess transport** rather than raw area.  The finite certificate is `verify_rl42_lightweight_rho28.py`.

RL remains open.  The near-resonant order-2 / `g=2` branch remains open.

## 1. Excess transport

For a maximal prefix-count excursion `E`, write

- `r_E` for its transport area;
- `p_E` for its common odd weight;
- `e_E = r_E-p_E` for its **excess transport**.

From `RL42_MOVED_RANK_SPARSE_BRIDGE.md`,

`P = sum_E p_E`

is exactly the number of displaced ordered odd ranks.  Therefore

> `rho = P + sum_E e_E`.                                  (R42R.1)

For a canonical positive excursion, after the initial divergence and before the final closing pair, the current prefix-count gap is an integer `d>=1`.  Appending an interior pair `(x,y)` changes `e` by

`d-x >= 0`.

The only zero-cost interior move is common `11` while `d=1`.  Hence

> **`e_E>=0` for every maximal excursion.**                (R42R.2)

This is the key compression: very long excursions can have small `e` only by inserting zero-cost `11` loops at height one.

## 2. Low-excess crossing certificate

The first physical sign reversal is mandatory.  For a positive canonical excursion with local data `(D,h,p)`, an integer crossing requires a positive odd incoming gap `g` such that

`D-3^p g = 2^h g_out > 0`.                                (R42R.3)

To reconstruct the floor `rho>=28`, it is enough to control crossings inside any hypothetical `rho<=27` return.  Such an excursion has `p<=27`; the verifier checks the slightly larger range `p<=28`.

The exact excess recurrence enumerates every canonical excursion with `e<=3`, `p<=28`.  Counts are

- `e=0`: 28;
- `e=1`: 406;
- `e=2`: 4,438;
- `e=3`: 39,124.

There are **zero** integer sign-changing excursions among all 43,996 words.

Deleting the only zero-cost loop (`11` at height one) reduces these infinite low-excess languages to exactly **eight** skeletons:

- `e=0`: `01 / 10`;
- `e=1`: `001 / 100`;
- `e=2`: `0001 / 1000`, `0011 / 1100`;
- `e=3`: `00001 / 10000`, `00011 / 10100`, `00101 / 11000`, `00111 / 11100`.

The earlier session summary said “seven”; that was a counting slip.  The verifier and the corrected list contain eight.

For the bounded range relevant to `rho<=28`, the exact consequence is

> **every physical sign-changing excursion has `e_cross>=4`.** (R42R.4)

This statement is used only in the bounded range just certified; no unproved infinite-parameter strengthening is needed for the theorem below.

## 3. Immediate floor `rho>=27`

`RL42_PREFIX_CAP_GAP_VS_MOVED_MASS.md` proved analytically

`P_+ > (45/8)G`,

and the inherited endpoint ownership gives `4|G`.  Hence

> `P>=P_+>=23`.                                           (R42R.5)

Every genuine half return must physically change sign at least once.  Combining (R42R.1), (R42R.2), (R42R.4), and (R42R.5), any candidate with `rho<=27` satisfies

`rho >= P+e_cross >= 23+4=27`.

Thus

> **`rho>=27`.**                                          (R42R.6)

The only remaining case below 28 is equality.

## 4. Rigidity of `rho=27`

Assume `rho=27`.  Equality in the preceding integer bounds forces

`P=23`,

`sum_E e_E=4`,

and because `P_+>=23` while `P>=P_+`,

`P=P_+=23`.                                               (R42R.7)

Therefore:

1. every moved odd rank is positive, so every maximal prefix-count excursion is positive;
2. exactly one excursion has excess `4` and it is the mandatory physical crossing;
3. every other excursion has excess `0`.

Also the analytic area-gap bound

`rho > (45/8)G`

with `rho=27` and `4|G` forces

> `G=4`.                                                   (R42R.8)

The inherited exact common-prefix theorem then gives common prefix `11`, so the physical gap entering the first excursion is

> `g_first=9`.                                            (R42R.9)

## 5. Exact `e=4` crossing classification at `P=23`

The verifier enumerates every canonical positive excursion with

`e=4`, `p<=23`.

There are

- 124,456 word pairs;
- 124,225 distinct local triples `(p,D,h)`.

Only **19** are integer-crossing capable.  They occur for exactly

`p=5,6,...,23`,

one type at each `p`, and every one satisfies

> `g=1 -> -4`,

with

`h=p+3`,

`D=3^p+4*2^h`.                                            (R42R.10)

Thus an equality candidate can cross only if its pre-crossing physical gap can become `1` using excess-zero excursions.

## 6. Excess-zero pre-crossing reachability

The `e=0` family is explicit:

`alpha = 0 1^p`,

`beta = 1^p 0`,

`D=3^p-2^p`,

`h=p+1`,

`r=p`.                                                     (R42R.11)

Starting at gap `9`, the verifier propagates every integral positive transition of these excursions under the full `P=23` budget.

Between excursions it uses the inherited safe synchronized-run over-approximation: if an excursion ends at

`Delta = 2^s m`, `m` odd,

then the next excursion is allowed to start at every

`m 3^c`, `0<=c<=s`.

This permits more paths than the true parity dynamics and is therefore safe for exclusion.

Across the full pre-crossing budget the computation obtains only 19 distinct positive odd incoming gaps.  Crucially,

> **gap `1` is never reachable.**                          (R42R.12)

A redundant direct scan tests every reachable gap against all 124,225 distinct `e=4` local types under the remaining odd-mass budget and finds zero crossing transitions.

Therefore `rho=27` is impossible.

## 7. Conclusion

Combining the analytic moved-rank lower bound with the bounded low-excess crossing certificate and the exact equality-case reachability computation gives

> # **`rho >= 28`.**                                      (R42R.13)

This is now independently reproducible from retained RL40/RL42 facts and a small RL42 verifier.  It no longer depends on reconstructing the missing RL41 area-26 and area-27 massive search tables.

The previous RL41 searches remain useful corroborating evidence and expose the `(46,29)` and `(65,41)` arithmetic resonances, but they are no longer needed to audit the floor `rho>=28`.

## 8. Next target: `rho=28`

The excess decomposition makes the next layer much smaller than a raw area-28 search.

Since `P>=23` and a crossing costs at least four excess units, `rho=28` has only two top-level possibilities:

1. `P=24`, total excess `4`;
2. `P=23`, total excess `5`.

Hence the next search should enumerate only `e=0,1,4,5` families under these rigid mass budgets, propagate exact physical gaps from `9`, impose the terminal `-4*2^s` condition, and only then apply the exact distortion/product and proper-factor arithmetic.  No all-area-28 excursion table is required.

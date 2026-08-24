# RL42 — crossing-excess transport floor

Date: 2026-08-22

## Status

**ANALYTIC + SMALL EXACT CERTIFICATE** in the inherited near-resonant order-2 / `g=2` balanced-return branch.

This combines the cutoff-free RL42 transport-efficiency bridge with a bounded local crossing certificate to prove

> # **`rho >= 48`.**

The exact certificate checks only positive excursions of excess `e<=3` and odd weight `p<=47`; it does **not** reconstruct the lost RL41 area-26/27 tables.

Companion verifier:

`verify_rl42_crossing_excess_transport_floor.py`.

RL remains open.

## 1. Transport efficiency

Retain the RL42 ordered-rank notation.  For every positive moved rank let

`delta_m=i_m-j_m>=1`.

The exact numerator equation and the prefix cap give

`M_eff := sum_(positive m) (1-2^(-delta_m))`

`>= 3(z+1)G/z^2`.                                           (R42X.1)

Here `z=2^a/3^ell>1`, `z^2<16/15`, and the inherited endpoint ownership gives `4|G`, `G>0`.  Therefore

`M_eff > (45/8)G >= 45/2`.                                  (R42X.2)

The previous RL42 transport theorem used only

`1-2^-delta <= delta/2`

to obtain `rho>=46`.  The crossing structure supplies two more units.

## 2. Excursion excess is rank-displacement excess

For a canonical positive excursion `E`, let

- `p_E` be its number of moved odd ranks;
- `r_E` be its transport area;
- `e_E=r_E-p_E`.

The local ordered-rank identity gives

`r_E = sum_(m in E) delta_m`,

while `p_E` is the number of summands.  Hence

> `e_E = sum_(m in E) (delta_m-1)`.                         (R42X.3)

Thus excursion excess is exactly the amount by which its positive-rank displacement exceeds the unit-displacement baseline.

## 3. A mandatory crossing cannot have excess 0,1,2,3 below rho 48

A nontrivial balanced return has a physical positive-to-negative sign-changing excursion.  Under a hypothetical `rho<=47`, any such excursion has `p<=47`.

The verifier streams **all** canonical positive excursions with

`p<=47`, `e<=3`.

It checks 286,607 words:

| excess | count |
|---:|---:|
| 0 | 47 |
| 1 | 1,128 |
| 2 | 19,505 |
| 3 | 265,927 |

For each local type `(D,h,p)`, the exact crossing congruence is tested:

`D-3^p g = 2^h g_out >0`,

with positive odd incoming gap `g`.

There are **zero** physical sign-changing excursions in the entire `e<=3`, `p<=47` set.  Therefore, in any hypothetical return with `rho<=47`, its mandatory crossing satisfies

> `e_cross >= 4`.                                           (R42X.4)

This is a bounded statement tailored to the contradiction range; no infinite low-excess classification is assumed.

## 4. Price the four crossing-excess units

For every integer `delta>=1`,

> `1-2^-delta <= delta/2 - (delta-1)/4`.                   (R42X.5)

Indeed this is equivalent to

`4(1-2^-delta) <= delta+1`.

Let

`S_+ = sum_(positive m) delta_m <= rho`,

and

`E_+ = sum_(positive m)(delta_m-1)`.

The crossing alone contributes at least four units to `E_+` by (R42X.3)–(R42X.4), so `E_+>=4`.  Summing (R42X.5),

`M_eff <= S_+/2 - E_+/4`

`<= rho/2 - 1`.                                             (R42X.6)

Combine (R42X.2) and (R42X.6):

`rho/2 - 1 > 45/2`.

Therefore

`rho > 47`,

and, since `rho` is integral,

> # **`rho >= 48`.**                                       (R42X.7)

## 5. Why this matters

The improvement from `rho>=46` to `rho>=48` is not another broad area enumeration.  It couples two genuinely different constraints:

1. the exact numerator equation says positive rank displacement has limited arithmetic efficiency;
2. a physical sign change necessarily wastes at least four units of displacement above the unit-move baseline in the entire contradiction range.

This is the first place in the RL42 line where the mandatory crossing is charged directly inside the scalable transport-efficiency inequality.

## 6. Verifier output

The retained verifier run reports:

```text
RL42 crossing-excess transport floor verifier: PASS
e<=3 words checked through p<=47 = 286607
counts by excess = {0: 47, 1: 1128, 2: 19505, 3: 265927}
physical sign-changing excursions among them = 0
therefore any mandatory crossing under rho<=47 has excess >=4
transport efficiency then gives M_eff <= rho/2 - 1
exact numerator bridge gives M_eff > 45/2
certified consequence: rho > 47, hence rho >= 48
```

## 7. Immediate continuation

At `rho=48`, the same efficiency bound forces `P_+>=44`, while (R42X.4) forces `P<=44`.  Hence

`P=P_+=44`, `sum e_E=4`,

so all excursions are positive, exactly one excursion is the physical `e=4` crossing, and every other excursion has excess zero.  That rigid boundary case is handled by the companion RL42 `rho=48` elimination certificate.

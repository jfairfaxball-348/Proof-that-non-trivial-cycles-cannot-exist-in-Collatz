# RL56 session increment and audit targets

Date: 2026-08-23

## Status

This file records the *increment after* `RL56_AGGREGATE_POTENTIAL_AND_TERMINAL_COMPATIBLE_PREFIX.md`.

Some claims below have fresh exact reruns but have not yet received an independent reimplementation. They are therefore marked **finite certificate — independent audit pending** rather than silently promoted.

## 1. Small terminal exponent regime: candidate reduction to `K>=25`

The retained terminal state has

`d=1`, `J_end=2^K`.

Under a hypothetical Gate-A counterexample one has the inherited strict inequality

`H<K`.

The inherited RL45 quotient theorem/certificate proves, for every reachable state through `H<=23`, that no positive state has

`v2(J)>H`

at terminal height one. The fresh rerun is in

`session_runs/RL56_RL45_H23_FRESH_RUN.txt`.

Hence, if the current terminal exponent satisfies `K<=23`, then at terminal height one

`v2(J_end)=K>H`,

contradicting the RL45 certificate. The inherited parity regime treats the live `K` as odd, so the surviving branch is reduced to

`K>=25`.

**Audit requirement:** independently check the notation match between the RL45 terminal-height `H` and the current survivor's `H<K`, and re-check the inherited oddness of `K`. Do not rely only on the shared letter `K`, because RL45 also uses an internal quotient quantity named `K` away from terminal height.

Classification: **analytic consequence of an inherited exact finite certificate, audit pending at the interface.**

## 2. Sharper terminal caps from the inherited phase squeeze

The inherited safe-CF phase squeeze gives

`zeta - 1 < (398/45)/2^71`.

Thus the coarse `zeta<136/135` used in the first RL56 pass can be replaced by a rational overcap arbitrarily close to `1`. The supplied exact scripts use the safe rational surrogate

`A = 27*zeta/2 < 27/2 + 10^-18`.

For `K>=25`, this gives

`Psi_end < 27/4*(1+2^-25) + 10^-18`

`= 6.750000201165676...`.

The corresponding `Xi` cap is essentially `13.5` rather than `13.6`.

Classification: **analytic arithmetic consequence, easy audit target.**

## 3. Tightened terminal-compatible first-26 certificate: `10.3`

The script

`verification/verify_tight_prefix_fast.py`

run as

`python3 verification/verify_tight_prefix_fast.py 25 103/10`

returns no prefix above `103/10` under the legal sequential-cap automaton plus the sharpened `Xi/Psi` caps.

Fresh run:

`session_runs/RL56_TIGHT_PREFIX_K25_10_3_FRESH_RUN.txt`.

Result:

`Zx_26 <= 103/10 = 10.3`.

This would imply

`Zx_late > 97/60`.

Classification: **exact finite certificate — independent audit pending.**

## 4. Coupled-K viable-prefix certificate: `33/4`

The stronger script

`verification/verify_viable_kselector_fast.py`

uses a single odd `K>=25` for both terminal-potential inequalities and additionally prunes prefixes that no longer have enough remaining `Psi` room to reach the inherited total requirement

`Zx>143/12`.

Fresh decision run:

`python3 verification/verify_viable_kselector_fast.py 33/4`

returns

`hit False`,

with `3,676,571` search nodes and `542,063` memo states in the fresh run.

Therefore the session-generated certificate is

`Zx_26 <= 33/4 = 8.25`

for every prefix that still passes those necessary viability conditions.

A separate run at target `8` returns a witness:

`Zx_26 = 8.1728520265...`,

with cut data `(i,p,d,J)=(71,45,2,21)`, minimal compatible `K=25`,

`Psi_cut = 2.9971225238...`,

`Xi_cut = 4.3957797017...`,

and relaxed total upper room `11.9257297038... > 143/12`.

So the `33/4` decision is not vacuous.

Fresh logs:

- `session_runs/RL56_VIABLE_PREFIX_33_4_FRESH_RUN.txt`
- `session_runs/RL56_VIABLE_PREFIX_8_WITNESS_FRESH_RUN.txt`

Classification: **exact finite certificate — high-priority independent audit target.**

## 5. Consequences if the `33/4` certificate survives audit

From

`Zx > 143/12`

and

`Zx_26 <= 33/4`,

one gets

`Zx_late > 143/12 - 33/4 = 11/3`.

Using

`Zx_late <= Psi_end-Psi_cut`

and the `K>=25` terminal cap yields

`Psi_cut < 3.083333535...`.

A convenient safe statement is

`Psi_cut < 3.084`.

Classification: **exact analytic consequences conditional on the certificate.**

## 6. Defect localization to displacement `<=1`

Retain the inherited exact defect identity

`E = sum_j w_j [1-(2/3)^r_j]`,

where here `r_j` denotes the matching displacement of the `j`-th x-zero. This `r_j` is **not** the same symbol as the backward remaining-zero budget used in some terminal coordinates.

The inherited survivor has

`E<5/3`.

For any term with `r_j>=2`,

`1-(2/3)^r_j >= 5/9`.

Hence, writing

`M_ge2 = sum_{late, r_j>=2} w_j`,

we get

`(5/9) M_ge2 < 5/3`,

so

`M_ge2 < 3`.

If the new `Zx_late>11/3` bound is valid, then

`M_le1 = sum_{late, r_j<=1} w_j > 11/3-3 = 2/3`.

The inherited sequential cap gives each x-zero

`w_j<17/30<2/3`.

Therefore a survivor must contain **at least two** late x-zeros with displacement `r_j<=1`.

Classification: **analytic consequence of inherited defect identity + audit-pending `33/4` certificate.**

## 7. Exact suffix event-count relation

Suppose the legal cut immediately after the 26th x-zero has height `d_c`. With `R=z-27` late x-zeros, the suffix has exactly

`#x0 = R`,

`#y0 = R+d_c-1`,

because `d=1+p_y-p_x` and the full endpoint returns to height one.

For compressed event counts

`a=#11`, `b=#10`, `c=#00`, `e=#01`,

one has

`c+e=R`,

`b+c=R+d_c-1`,

hence

`b=e+d_c-1`.

Classification: **elementary exact bookkeeping; audit the convention/order once.**

## 8. Terminal grammar to use next

The inherited backward coordinate is

`Q_d = J + 2^d - 1`.

The exact backward maps are already recorded in inherited RL52:

- `11: Q -> 2Q/3`, requiring `3|Q`;
- `10: Q -> 2Q+1`, height increases by one and consumes one y-zero;
- `00: Q -> 2Q-(3^d-1)`, consuming one x-zero and one y-zero;
- `01: Q -> 2Q/3-3^(d-1)`, requiring `d>1` and `3|Q`, height decreases by one and consumes one x-zero.

A run of backward `11` edges is exactly limited by `v3(Q)`.

The next high-leverage task is to combine this exact divisibility grammar with the forced `>2/3` mass at displacement `<=1`.

## 9. Near-aligned macro claim: reconstruct before promotion

The RL56 session identified the likely tiny local grammar for `r_j<=1` as living at heights `d<=2`, with displacement-zero corresponding to aligned height-one behavior and displacement-one arising from one-column mismatches around `01/00` transitions.

This is intentionally **not promoted here as a theorem**. RL57 should reconstruct the rank-matching convention directly from the inherited RL47/RL50 displacement formalism and then list all allowed `r_j=0` and `r_j=1` local macros without relying on prose memory.

This reconstruction is the first focused proof task after audit.

## 10. Primary closure target for RL57

After audit, aim to prove

`sum_{late, r_j<=1} w_j <= 2/3`

under terminal `J_end=2^K`, odd `K>=25`, exact backward `Q` divisibility, the legal cut constraints, and the suffix count relation.

That would contradict the forced strict lower bound `>2/3` and eliminate the sole safe-CF survivor.

If the local grammar does not support such an upper bound, identify exactly which repeatable macro defeats it and whether its repetition is compatible with `v3(Q)`, terminal power, and the exact event-count relation.

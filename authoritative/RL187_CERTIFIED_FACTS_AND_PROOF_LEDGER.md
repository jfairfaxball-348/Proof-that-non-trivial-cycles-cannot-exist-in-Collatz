# RL187 certified facts and proof ledger

Date: 2026-08-30

Scope: every new statement remains internal to the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)` and to first defects selected by RL184 clean shallow-start corridors.

## Inherited frozen facts

- RL181: `128,081,997,553 < K_i < 146,795,909,391`, every normalized ordinary p-gap is strictly in `(128,081,997,553,293,591,818,782)`, and `K_(i+1)-K_i=f_i/3`.
- RL184: at least `10,075,174,499` clean 40-edge shallow-start corridors exist; a zero-defect transition satisfies `2^d C'=3C` with `d>=1`.
- RL185: ordinary corrected flow is `f_i=rho_i(2^-b-2^-a)`, `rho_i>1/2`, and the exact full-period total obeys `0<F2<1/2`; the carry flow is positive and exceeds `1/2`.
- RL186: at a first nonzero defect offset `tau>0`, `C_tau=3^tau odd(C_0)` and `2^tau|C_0`; the exact late height vocabulary for `tau=28,...,39` is frozen; `N_37<=7,052,720,272`; ordinary absolute corrected-flow variation exceeds `354`.

## RL187.1 — exact joint terminal ownership law

**Class:** proved analytic mathematics.

For a clean shallow zero-prefix start with common starting height `h_0 in {0,1}`, first nonzero defect at offset `tau>0`, and actual chronological mechanical bits `c_j in {1,2}`, let

`ell = #{0<=j<tau : c_j=2}`

and let `H` be the endpoint maximum at the first defect. Since on every zero transition

`d_j=c_j+M_j-M_(j+1)`, 

telescoping gives

`sum_(j<tau)d_j = tau+ell+h_0-H`.

RL186 identifies the left side with `v_2(C_0)`. Hence

`H = h_0 + tau + ell - v_2(C_0)`

and simultaneously

`C_tau = 3^tau odd(C_0)`.

If `r` is the terminal mechanical residue and `B=A-L=80,448,749,305`, then a fixed `ell` is possible only on the exact terminal-rank interval

`tau B-ell L <= r < tau B-(ell-1)L`,

clipped to `0<=r<L`.

Thus every shallow start selecting the same physical first-defect phase must share the same terminal numerator, endpoint maximum, and terminal mechanical residue. Offsets cannot be charged independently.

## RL187.2 — exact high-tail joint offset families

**Class:** proved analytic combinatorics + exact finite integer certificate.

Exhaustive exact enumeration of all admissible shallow `C_0`, the RL187.1 terminal invariant, the strict normalized-gap corridor, and the exact terminal-rank intervals reproduces the entire RL186 late-height vocabulary and yields these maximal simultaneously compatible offset families for one fixed first defect:

- `H=18`: `{28,29,30,31,32,33,34,35}`;
- `H=19`: `{30,31,32,33,34}` or `{31,32,33,34,35,36}`;
- `H=20`: `{31,32,33,34,35,36}`;
- `H=21`: `{33,34,35}` or `{34,35,36,37}`;
- `H=22`: `{35,36}`;
- `H=23`: `{37,38}`;
- `H=24`: `{39}`.

These are necessary co-ownership families, not existence claims.

## RL187.3 — multiscale zero-prefix survival staircase

**Class:** proved analytic combinatorics + exact finite integer certificate.

Let `N_n=#{clean starts: tau>=n}`. Partition the cyclic defect sequence into zero blocks ending at one nonzero defect. A start with first-defect offset `tau` occupies a block span of at least `tau+1` physical phase positions. Combining this span with the exact joint families gives the sharp certified density/cap staircase:

| n | density cap | `N_n` cap |
|---:|:---:|---:|
|28|`2/9`|30,561,787,847|
|29|`7/36`|26,741,564,366|
|30|`1/6`|22,921,340,885|
|31|`6/37`|22,301,845,185|
|32|`5/37`|18,584,870,988|
|33|`4/37`|14,867,896,790|
|34|`2/19`|14,476,636,348|
|35|`3/38`|10,857,477,261|
|36|`1/19`|7,238,318,174|
|37|`2/39`|7,052,720,272|
|38|`1/39`|3,526,360,136|
|39|`1/40`|3,438,201,132|

The `n=37` row independently recovers RL186. The new useful thresholds are `n=36,38,39`. The `n=35` bound remains `782,302,762` above the clean-start floor and therefore does not yet force a contradiction.

## RL187.4 — joint weighted-flow escalation

**Class:** proved analytic mathematics + exact rational/integer certificate.

Assign each clean start the charge

- `1/(3*2^22)` if `tau<=35`;
- `1/(3*2^23)` if `tau=36`;
- `1/2^25` if `tau>=37`.

For endpoint heights `H<=17`, the sum over all individually admissible offsets is at most `2^-(H+1)`. For `H=18,...,24`, the exact RL187.2 joint co-ownership families give the same bound. Since a nonzero ordinary defect of maximum endpoint height H has `|f_i|>2^-(H+1)`, all charges are globally supportable without multiplicity leakage.

Using `N_36<=7,238,318,174` and `N_37<=7,052,720,272`,

`sum_(ordinary i)|f_i|`

`> CLEAN/(3*2^22) - N_36/(3*2^23) - N_37/(3*2^25)`

`= 2,787,212,689 / 6,291,456`

`> 443`.

## RL187.5 — amplified signed flow and directional K variation

**Class:** proved analytic mathematics + exact rational certificate.

Adding the positive carry gives full absolute flow greater than the RL187.4 ordinary floor plus `1/2`, while the exact signed total remains in `(0,1/2)`. Therefore each sign carries corrected-flow mass strictly greater than

`2,787,212,689 / 12,582,912 > 221.5`,

and each sign of total K variation is strictly greater than

`2,787,212,689 / 37,748,736 > 73.8`.

These are total/directional variation statements, not chronological prefix excursion.

## Finite certificate status

`verification/verify_rl187_joint_terminal_multiscale_capacity.py` checks the RL186 tail vocabulary, exact joint terminal families, the full `N_28,...,N_39` staircase, the off-by-one block span `tau+1`, all joint charging inequalities, the exact `>443` ordinary-flow bound, and the inherited rational enclosure `0<F2<1/2`.

## Closure status

No high branch or global gate is closed. RL187 raises the ordinary absolute-flow floor from `>354` to `>443` and each directional K-variation floor from `>59` to `>73.8`, but the inherited K corridor remains vastly wider and total variation can still be chronologically compensated.

The nearest quantitative crossover is `N_35`: its sole density-`3/38` witness is the joint terminal family `tau={35,36,37}` with terminal invariant `(C_tau,H)=(3^37,21)`. That family is **not** ruled out in RL187 and becomes the focused RL188 target.

# RL187 — joint terminal ownership and multiscale zero-prefix capacity

Date: 2026-08-30

## 0. Outcome and classification

RL187 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

RL186 converted a long zero prefix into exact first-defect numerator arithmetic and obtained a single useful tail cutoff `N_37`. RL187 adds the missing joint consumer: multiple clean shallow starts that terminate at the same physical first defect do not merely share a defect height. They share the terminal numerator and the actual mechanical terminal rank. That forces different offsets to satisfy one common terminal invariant and sharply limits which offsets can coexist on one defect.

The resulting co-ownership theorem yields a genuine multiscale survival staircase. In particular, `N_36` is forced below `7.239e9`, while `N_38` and `N_39` fall below `3.527e9` and `3.439e9`. Feeding the joint distribution into a three-level charging scheme raises ordinary absolute corrected flow above 443 and each directional K-variation mass above 73.8.

Promoted results:

1. **RL187.1 — exact joint terminal numerator/height/rank ownership** (analytic).
2. **RL187.2 — exact high-tail joint offset families** (analytic combinatorics + exact finite integer certificate).
3. **RL187.3 — multiscale zero-prefix survival staircase** (analytic combinatorics + exact finite integer certificate).
4. **RL187.4 — joint weighted-flow escalation above 443** (analytic + exact rational/integer certificate).
5. **RL187.5 — signed-flow and directional K-variation escalation** (analytic + exact rational certificate).

No correction/demotion event occurred.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `B=A-L=80448749305`.

Retain RL181:

- `128,081,997,553<K_i<146,795,909,391`;
- every normalized ordinary p-gap lies strictly in `(128,081,997,553,293,591,818,782)`;
- `K_(i+1)-K_i=f_i/3`;
- `1/2<rho_i<=1`.

Retain RL182/RL183:

- exact ternary suffix numerator ownership and reset sensors;
- `2|C_i` iff `G_i=0` on ordinary p-edges;
- common-mechanical successor law `2^d C'=3C+D`, with `d=c+M-M'>=1`;
- chronological mechanical bit `c_i in {1,2}` and exact mechanical residue rotation by `B mod L`.

Retain RL184-RL186:

- `CLEAN=10,075,174,499` clean 40-edge shallow-start corridors;
- along a zero transition `2^d C'=3C`;
- first defect `tau<=39`;
- `C_tau=3^tau odd(C_0)` and `v_2(C_0)=sum_(j<tau)d_j`;
- exact first-defect late height vocabulary for `tau=28,...,39`;
- `N_37<=7,052,720,272`;
- ordinary corrected flow `f_i=rho_i(2^-b-2^-a)`;
- `0<F2<1/2`, carry flow `>1/2`.

All statements below remain internal to `(37,0,23,-1)`.

## 2. Exact terminal height and mechanical rank

Fix a clean corridor and let `tau>0` be the first offset with `G_tau!=0`. The start is zero-defect and shallow, so its two p-shift endpoint heights are equal to some `h_0 in {0,1}`.

For each zero transition `j<tau`, write `M_j` for the common endpoint height and `c_j in {1,2}` for the actual chronological mechanical bit. RL183 gives

`d_j=c_j+M_j-M_(j+1)`.

Let

`ell=#{j<tau:c_j=2}`.

Because `sum c_j=tau+ell`, telescoping gives

`D:=sum_(j<tau)d_j=tau+ell+h_0-H`,

where H is the endpoint maximum at the first defect.

RL186.1 says `D=v_2(C_0)` and `C_tau=3^tau odd(C_0)`. Consequently

`H=h_0+tau+ell-v_2(C_0)`.

This is exact, not merely an upper envelope.

Now encode the actual mechanical word by the mechanical residue `r_0`. Advancing one chronological phase rotates the residue by

`B=A-L=80,448,749,305 (mod L)`.

If the terminal residue is r, then

`r = r_0+tau B-ell L`,

so a fixed ell is possible exactly when

`tau B-ell L <= r < tau B-(ell-1)L`,

clipped to the base interval `0<=r<L`.

Thus a physical first-defect phase simultaneously owns:

- one physical terminal numerator `T=C_tau`;
- one endpoint maximum H;
- one terminal mechanical residue r.

Any clean shallow start that selects that defect must satisfy all three terminal coordinates. This is the co-ownership restriction missing from RL186's offset-by-offset charging.

## 3. Exact high-tail co-ownership families

For `tau=28,...,39`, enumerate every shallow starting numerator

`C_0=2^tau k`

strictly inside the two inherited starting intervals. For each candidate compute

- `v_2(C_0)` and `T=3^tau odd(C_0)`;
- both exact possible mechanical late-bit counts `ell`;
- `H=h_0+tau+ell-v_2(C_0)`;
- the terminal-rank interval;
- the strict terminal normalized-gap test.

The enumeration reproduces the RL186 height vocabulary exactly, providing an internal consistency check. Grouping candidates by common `(T,H)` and intersecting terminal-rank intervals yields the maximal sets of offsets that one physical first defect can co-own:

| terminal H | maximal offset family/families |
|---:|:---|
|18|`{28,29,30,31,32,33,34,35}`|
|19|`{30,31,32,33,34}`; `{31,32,33,34,35,36}`|
|20|`{31,32,33,34,35,36}`|
|21|`{33,34,35}`; `{34,35,36,37}`|
|22|`{35,36}`|
|23|`{37,38}`|
|24|`{39}`|

No family in this table is asserted to occur physically. The table is an exact necessary capacity theorem.

## 4. Multiscale survival distribution

Let

`N_n=#{clean starts: tau>=n}`.

Partition the cyclic defect sequence into blocks ending at a nonzero defect. If a clean start has first-defect offset tau, then from that start through the terminating nonzero defect there are at least `tau+1` physical phase positions in the block. The denominator is therefore `tau+1`, not tau.

For each threshold n, restrict every exact co-ownership family to offsets `>=n`. A block owning k such starts with largest offset t has density at most

`k/(t+1)`.

Taking the exact maximum gives:

| n | worst joint density | exact integer cap `floor(density*L)` |
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

The `n=37` row exactly recovers RL186's earlier `2/39` theorem from the stronger joint framework. The `n=36`, `n=38`, and `n=39` rows are new quantitative cuts.

At n=35 the current bound is

`N_35<=10,857,477,261`,

which exceeds `CLEAN` by only

`782,302,762`.

The exact density witness is the three-offset family `{35,36,37}`. All three offsets can share the terminal invariant

`(T,H)=(3^37,21)`

under the current necessary constraints. RL187 does not rule this family out.

## 5. Joint charging theorem

A nonzero ordinary defect with maximum endpoint height H has

`|f_i|=rho_i |2^-b-2^-a| > 2^-(H+1)`.

Assign a charge to every clean start according to first-defect offset:

`w(tau)=1/(3*2^22)` for `tau<=35`,

`w(36)=1/(3*2^23)`,

`w(tau)=1/2^25` for `tau>=37`.

For `H<=17`, even summing these charges over every individually admissible offset stays within `2^-(H+1)`. For `H>=18`, use the exact joint families from Section 3. Every maximal family also remains within the physical defect budget.

The tight high-tail checks include

- H=21, `{33,34,35}`: `3/(3*2^22)=1/2^22`;
- H=22, `{35,36}`: `1/(3*2^22)+1/(3*2^23)=1/2^23`;
- H=23, `{37,38}`: `2/2^25=1/2^24`;
- H=24, `{39}`: `1/2^25`.

Therefore no physical selected defect is overcharged, even if it serves several starts at different offsets.

Let `N36=N_36`, `N37=N_37`. The three offset classes contain

- `CLEAN-N36` starts with `tau<=35`;
- `N36-N37` starts with `tau=36`;
- `N37` starts with `tau>=37`.

Hence

`sum_(ordinary i)|f_i|`

`> (CLEAN-N36)/(3*2^22) + (N36-N37)/(3*2^23) + N37/2^25`

`= CLEAN/(3*2^22) - N36/(3*2^23) - N37/(3*2^25)`.

Substituting the worst certified survival caps gives

`sum_(ordinary i)|f_i|`

`> 2,787,212,689 / 6,291,456`

`= 443.0155... >443`.

This improves RL186's `>354` ordinary variation floor without assuming any chronological sign ordering.

## 6. Signed consumer

The carry is positive and exceeds `1/2`. Thus full absolute corrected flow is greater than

`2,787,212,689/6,291,456 + 1/2`.

The exact total remains `0<F2<1/2`. If P and N denote positive and negative corrected-flow masses, then

`P+N > ordinary_floor+1/2`,

`P-N = F2 <1/2`.

Therefore both signs satisfy

`P,N > ordinary_floor/2`

`= 2,787,212,689 / 12,582,912`

`=221.5077...`.

Since K drift is `f_i/3`, each direction of total K variation exceeds

`2,787,212,689 / 37,748,736`

`=73.8359...`.

This is still total directional variation, not a chronological prefix excursion. The inherited K corridor remains roughly `1.87e10` wide, so a sign-reversal attack is not yet competitive.

## 7. Nearest crossover and RL188 target

The staircase identifies a uniquely focused next obstruction. At threshold 35, the only density-`3/38` witness is the co-owned terminal family

`tau={35,36,37}`, `T=3^37`, `H=21`.

If that family can be excluded or forced to consume enough extra physical span, the next density ceiling is `2/37`, giving

`N_35<=floor(2L/37)=7,433,948,395`,

which would move more than 2.6 billion additional clean starts into the `tau<=34` class.

RL188 should therefore attack that single physical family using the inherited ternary reset/ownership sensors, exact mechanical terminal-rank segments, and predecessor/successor boundary compatibility. No impossibility claim is made here.

## 8. Verification and scope

The exact verifier

`verification/verify_rl187_joint_terminal_multiscale_capacity.py`

reconstructs the late-tail enumeration from integer arithmetic, verifies the joint-family table and full survival staircase, checks every low/high joint charging inequality, and re-certifies the inherited exact rational enclosure `0<F2<1/2`.

No arbitrary residue word, necessary affine map, or enumerated candidate is promoted as physically realized. No generic rank/lattice route is revived. No branch or global closure claim is made.

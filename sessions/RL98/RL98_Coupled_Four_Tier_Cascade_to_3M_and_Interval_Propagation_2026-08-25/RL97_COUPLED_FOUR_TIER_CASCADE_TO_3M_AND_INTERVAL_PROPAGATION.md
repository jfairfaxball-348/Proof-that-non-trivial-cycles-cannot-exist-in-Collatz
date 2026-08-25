# RL97 — sustained coupled four-tier cascade to deep radius 3,000,000

Date: 2026-08-25

## 0. Executive outcome

RL97 continued from the frozen RL96 first-Farey/full-phase Gate-A state and executed a sustained coupled cascade through **24 adjacent 25,000-step deep checkpoints**, from deep radius `2,400,000` to `3,000,000`.

Final certified frontier:

- wide: `d<=5,000,030`, `r<=7,000,000` => successor `<=5,000,053`;
- middle: `d<=7,500,032`, `r<=4,350,000` => successor `<=7,500,053`;
- deep: `d<=10,000,032`, `r<=3,000,000` => successor `<=10,000,053`;
- ultra: `d<=15,000,035`, `r<=1,680,000` => successor `<=15,000,053`.

No global depth floor was lost anywhere in RL97.

New-band minima over the entire RL97 extension were:

- ultra: `15,000,037 at r=905,728`, tying but not beating the inherited global minimum `15,000,037 at r=575,974`; a second tie occurs at `r=1,368,912`;
- middle: `7,500,036 at r=4,084,218`, above the inherited global minimum `7,500,034 at r=1,635,300`;
- deep: `10,000,036 at r=2,955,163`, above the inherited global minimum `10,000,034 at r=378,722`.

Thus the effective depth floors remain

`D_m=7,500,032`, `D_d=10,000,032`, `D_u=15,000,035`.

The final exact feasible support edges remain `A-C`, `C-D`, `D-E`. `A-C` remains optimal in the live terminal direction over the full promoted RL97 interval.

The branch-specific odd exclusion advances from the incoming first survivor

`k7=2,921,774,731`

through

`k=2,921,801,521`.

This eliminates **13,396 additional consecutive odd values**. The new first surviving odd candidate on this branch is

`k8=2,921,801,523`.

At the last eliminated odd, the exact contradiction margin is `+10,473`. At `k8`, it is `-3,549`.

No Gate A global closure, Gate B closure, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.

## 1. Incoming verification and provenance

The incoming RL97 handover bundle had already passed its outer SHA-256, 38-entry internal manifest, fresh-unpack fast verifier suite, and GitHub provenance gate. Under the verification-economy rule, RL97 accepted the frozen RL96 ledger as authoritative and did not recursively rerun historical expensive certificates.

Incoming frozen state:

- middle `r<=3,950,000`, `D_m=7,500,032`;
- deep `r<=2,400,000`, `D_d=10,000,032`;
- ultra `r<=870,000`, `D_u=15,000,035`;
- active support `A-C` with `lambda=4,600,000/52,500,238,500,033`, `mu=1/7,000,001`;
- first live odd `k7=2,921,774,731`, margin `-3,972`.

## 2. Exact RL97 scan extension

### Ultra

Completed exact gap-free GMP scans modulo `2^15,000,056` over

`870,001 <= r <= 1,680,000`.

Total new ultra-radius values: `810,000`.

New-band minimum:

`15,000,037 at r=905,728`.

A second occurrence of the same minimum appears at

`r=1,368,912`.

Neither is below the inherited global minimum `15,000,037 at r=575,974`, so

`D_u=15,000,035`

remains valid.

### Middle

Completed exact gap-free scans modulo `2^7,500,056` over

`3,950,001 <= r <= 4,350,000`.

Total new middle-radius values: `400,000`.

New-band minimum:

`7,500,036 at r=4,084,218`.

This remains above the inherited global minimum `7,500,034 at r=1,635,300`, so

`D_m=7,500,032`.

### Deep

Completed exact gap-free scans modulo `2^10,000,056` over

`2,400,001 <= r <= 3,000,000`.

Total new deep-radius values: `600,000`.

New-band minimum:

`10,000,036 at r=2,955,163`.

This remains above the inherited global minimum `10,000,034 at r=378,722`, so

`D_d=10,000,032`.

Classification: **new exact finite certificates + inherited minimal-reset interface consequence**.

## 3. Sustained coupled progression

Every listed checkpoint was promoted only after the necessary exact scan coverage was complete and the live global floor comparison had passed.

| deep radius | middle radius | ultra radius | `floor(lambda*C)` | final excluded odd |
| ---: | ---: | ---: | ---: | ---: |
| 2,425,000 | 3,950,000 | 905,000 | 3,673 | 2,921,775,777 |
| 2,450,000 | 3,975,000 | 935,000 | 3,653 | 2,921,776,829 |
| 2,475,000 | 4,000,000 | 970,000 | 3,632 | 2,921,777,889 |
| 2,500,000 | 4,000,000 | 1,005,000 | 3,612 | 2,921,778,953 |
| 2,525,000 | 4,025,000 | 1,040,000 | 3,592 | 2,921,780,023 |
| 2,550,000 | 4,050,000 | 1,075,000 | 3,572 | 2,921,781,099 |
| 2,575,000 | 4,050,000 | 1,110,000 | 3,552 | 2,921,782,181 |
| 2,600,000 | 4,075,000 | 1,145,000 | 3,532 | 2,921,783,269 |
| 2,625,000 | 4,100,000 | 1,180,000 | 3,512 | 2,921,784,363 |
| 2,650,000 | 4,100,000 | 1,215,000 | 3,492 | 2,921,785,463 |
| 2,675,000 | 4,125,000 | 1,250,000 | 3,472 | 2,921,786,569 |
| 2,700,000 | 4,150,000 | 1,270,000 | 3,452 | 2,921,787,681 |
| 2,725,000 | 4,150,000 | 1,305,000 | 3,432 | 2,921,788,799 |
| 2,750,000 | 4,175,000 | 1,340,000 | 3,412 | 2,921,789,923 |
| 2,775,000 | 4,200,000 | 1,375,000 | 3,392 | 2,921,791,053 |
| 2,800,000 | 4,200,000 | 1,410,000 | 3,372 | 2,921,792,191 |
| 2,825,000 | 4,225,000 | 1,445,000 | 3,351 | 2,921,793,335 |
| 2,850,000 | 4,250,000 | 1,480,000 | 3,331 | 2,921,794,485 |
| 2,875,000 | 4,250,000 | 1,515,000 | 3,311 | 2,921,795,641 |
| 2,900,000 | 4,275,000 | 1,550,000 | 3,291 | 2,921,796,803 |
| 2,925,000 | 4,300,000 | 1,585,000 | 3,271 | 2,921,797,973 |
| 2,950,000 | 4,300,000 | 1,620,000 | 3,251 | 2,921,799,149 |
| 2,975,000 | 4,325,000 | 1,655,000 | 3,231 | 2,921,800,331 |
| 3,000,000 | 4,350,000 | 1,680,000 | 3,211 | 2,921,801,521 |

The cascade did not stall after restoring the incoming endpoint. Each successive frontier replenished an approximately eight-million-unit contradiction margin at the then-current first survivor and bought roughly 500–600 further odd exclusions.

## 4. Final exact four-tier geometry

Final staircase-complement corners:

`A=(0,7,000,001)`

`B=(5,000,031,4,350,001)`

`C=(7,500,033,3,000,001)`

`D=(10,000,033,1,680,001)`

`E=(15,000,036,0)`.

The final active `A-C` support is

`mu=1/7,000,001`

and

`lambda=4,000,000/52,500,238,500,033`.

Exact corner values under `lambda*d+mu*r` are

- `A = 1`;
- `B = 5,847,252,783,337 / 5,833,359,833,337 > 1`;
- `C = 1`;
- `D = 52,600,194,940,033 / 52,500,238,500,033 > 1`;
- `E = 20,000,048,000,000 / 17,500,079,500,011 > 1`.

Thus every integer point outside the certified four-tier union satisfies the final weighted support inequality.

Exact feasible nonnegative two-corner supports remain precisely

- `A-C`;
- `C-D`;
- `D-E`.

At the incoming RL97 first survivor `k7`, their exact contradiction margins under the final frontier are respectively

- `A-C`: `+187,826,246`;
- `C-D`: `+184,711,488`;
- `D-E`: `-231,729,553`.

At the new first failure `k8`, the corresponding margins are

- `A-C`: `-3,549`;
- `C-D`: `-3,332,329`;
- `D-E`: `-448,388,026`.

The exact interval verifier checks that `A-C` is optimal at every promoted odd in the full RL97 exclusion interval.

Classification: **updated exact four-tier supporting-line theorem + exact convex-envelope audit**.

## 5. Top-stratum monotonicity

At the final support,

`floor(lambda*C)=3,211`.

This remains vastly larger than the explicit `2`-unit improvement available from increasing the block-count stratum. The inherited top-stratum monotonicity argument therefore remains valid and `b=k-1` is still the worst stratum.

Classification: **updated analytic monotonicity check**.

## 6. Exact RL97 interval propagation

Retain the conservative common successor ceiling

`L_common=15,000,053`.

The final verifier evaluates every odd

`2,921,774,731 <= k <= 2,921,801,521`

at `b=k-1` using exact rational arithmetic and the final `A-C` support.

All **13,396** values violate the necessary condition.

At `k=2,921,801,521`:

- `Q_min=123,139,091,657,857,127,643`;
- `D_b=17,564,442,249,346,917`;
- `R_b^max=11,081,960,984,517,759`;
- weighted bad-block bound `2,921,374,196`;
- forced multiscale-good blocks `427,324`;
- short-successor capacity `416,851`;
- contradiction margin `+10,473`.

At the next odd `k8=2,921,801,523`:

- `Q_min=123,139,091,657,857,127,496`;
- `D_b=17,564,526,551,210,320`;
- `R_b^max=11,082,014,173,071,665`;
- weighted bad-block bound `2,921,388,218`;
- forced multiscale-good blocks `413,304`;
- short-successor capacity `416,853`;
- contradiction margin `-3,549`.

### Theorem 6.1 — RL97 branch-specific odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`2,921,774,731 <= k <= 2,921,801,521`.

The updated branch-specific surviving odd window is

`2,921,801,523 <= k <= 42,150,931,559`, `k` odd.

Classification: **new analytic theorem + exact finite 2-adic certificates + exact rational interval audit**.

## 7. Geometry reserve and next coupling thresholds

At the final state, the final `A-C` support requires only

- middle radius at least `4,333,329` for `R_d=3,000,000`; actual `4,350,000`;
- ultra radius at least `1,666,673`; actual `1,680,000`.

For the next deep step `R_d=3,025,000`, unchanged depth floors require

- `R_m>=4,349,996`;
- `R_u>=1,700,006`.

Thus current middle radius exceeds the geometric threshold by four units for that single step; no middle extension is needed if floors hold. A natural immediate batch is ultra to at least `1,705,000`, then deep to `3,025,000`.

For `R_d=3,050,000`, unchanged floors require

- `R_m>=4,366,662`;
- `R_u>=1,733,340`.

A natural second checkpoint is middle `4,375,000`, ultra `1,740,000`, deep `3,050,000`, subject to live floor updates.

The ultra depth-axis remains nonbinding through deep radius floor `3,499,992` while the current depth floors remain unchanged.

At the final `A-C` support, the `E`-axis minimum ultra depth is

`D_u>=13,125,059`.

Current reserve:

`1,874,976`.

The reserve is smaller than at RL96 but remains substantial. Both the approaching `3.5M` depth-axis event and the `A-C`/`C-D` edge competition should be tracked exactly.

## 8. Red-team audit

The promoted RL97 result passes the inherited load-bearing checks:

1. RL81 common-mode freedom: no forbidden independence assumption is introduced.
2. RL79 generalized-increment homogeneity: the support argument remains homogeneous in the required variables.
3. RL20 physical representative/packing separation: quotient addresses are not counted as physical blocks.
4. Primitivity: no relaxation manufactures extra representatives.
5. First-Farey scope: the theorem is explicitly branch-specific.
6. RL88 arbitrary-reset family: no reset rigidity beyond the inherited minimal-reset interface is assumed.
7. Verification economy: inherited global minima are accepted only after the incoming verification gate.
8. Successor charge: `L_common=15,000,053` remains conservative and unchanged.
9. Exact support re-optimization: every promoted frontier was checked against all feasible pair supports; the final full interval is checked exactly.
10. Live floor update: every completed scan band was compared with the inherited global minimum before geometry was promoted.
11. Ultra-floor ties: equality with the inherited global minimum at `r=905,728` and `r=1,368,912` does not lower `D_u`; no false repair is introduced.
12. Deep near-floor event: the RL97 deep minimum `10,000,036 at r=2,955,163` is still two bits above the inherited global minimum and does not change `D_d`.

## 9. Proof-state ledger additions

### New proved analytic mathematics

- final four-tier support theorem at deep radius `3,000,000`;
- exact support-edge feasibility/optimality result for `A-C`, `C-D`, `D-E` over the promoted interval;
- maintained top-stratum monotonicity with `floor(lambda*C)=3,211`;
- branch-specific odd exclusion through `2,921,801,521`.

### New exact finite certificates

- ultra gap-free scan `870,001..1,680,000`;
- middle gap-free scan `3,950,001..4,350,000`;
- deep gap-free scan `2,400,001..3,000,000`;
- exact final interval audit over `13,396` odd values.

### No promotion from incomplete work

No incomplete scan or estimated endpoint is included in the frozen RL97 state.

## 10. Frozen global status

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open globally;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

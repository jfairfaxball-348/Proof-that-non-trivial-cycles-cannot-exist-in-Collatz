# RL96 — corrected coupled four-tier cascade to deep radius 2,400,000

Date: 2026-08-25

## 0. Executive outcome

RL96 continued from the corrected RL95 four-tier state and carried the exact coupled frontier through eight adjacent 25,000-step deep checkpoints rather than stopping after the first restored endpoint.

Final certified frontier:

- wide: `d<=5,000,030`, `r<=7,000,000` => successor `<=5,000,053`;
- middle: `d<=7,500,032`, `r<=3,950,000` => successor `<=7,500,053`;
- deep: `d<=10,000,032`, `r<=2,400,000` => successor `<=10,000,053`;
- ultra: `d<=15,000,035`, `r<=870,000` => successor `<=15,000,053`.

No new global depth-floor loss occurred. The RL96 new-band minima were:

- ultra: `15,000,038 at r=868,107`, above the inherited global minimum `15,000,037 at r=575,974`;
- middle: `7,500,036 at r=3,871,407`, above the inherited global minimum `7,500,034 at r=1,635,300`;
- deep: `10,000,037 at r=2,216,053`, above the inherited global minimum `10,000,034 at r=378,722`.

The final exact feasible support edges remain `A-C`, `C-D`, `D-E`. `A-C` remains optimal in the promoted terminal direction throughout the new exact interval.

The branch-specific odd exclusion advances from the incoming first survivor

`k6=2,921,766,551`

through

`k=2,921,774,729`.

This eliminates `4,090` additional consecutive odd values. The new first surviving odd candidate on this branch is

`k7=2,921,774,731`.

At the last eliminated odd, the exact contradiction margin is `+11,013`. At `k7`, it is `-3,972`.

No Gate A global closure, Gate B closure, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.

## 1. Incoming verification and provenance

The incoming RL96 outer SHA-256 matched the supplied sidecar. All `69` entries in the incoming internal manifest passed, and the inherited RL95 fast verifier suite passed under the verification-economy rule.

GitHub provenance was checked against repository `jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`. The latest repository commit at session start was

`34cac3e8a47435a6b0014bc57e46a4e8e3ab3626`

with message

`RL96_Coupled_Four_Tier_Cascade_to_2_2M_and_Ultra_Floor_Repair_2026-08-25`.

No historical expensive certificate was recursively rerun.

## 2. Exact RL96 scan extension

### Ultra

Completed exact GMP scans modulo `2^15,000,056` over the gap-free range

`605,001 <= r <= 870,000`.

Total new ultra-radius values: `265,000`.

New-band minimum:

`15,000,038 at r=868,107`.

The inherited global minimum remains

`15,000,037 at r=575,974`,

so the safe ultra depth remains

`D_u=15,000,035`.

### Middle

Completed exact scans modulo `2^7,500,056` over

`3,800,001 <= r <= 3,950,000`.

Total new middle-radius values: `150,000`.

New-band minimum:

`7,500,036 at r=3,871,407`.

The inherited global minimum remains

`7,500,034 at r=1,635,300`,

so

`D_m=7,500,032`.

### Deep

Completed exact scans modulo `2^10,000,056` over

`2,200,001 <= r <= 2,400,000`.

Total new deep-radius values: `200,000`.

New-band minimum:

`10,000,037 at r=2,216,053`.

The inherited global minimum remains

`10,000,034 at r=378,722`,

so

`D_d=10,000,032`.

Classification: **new exact finite certificates + inherited minimal-reset interface consequence**.

## 3. Sustained coupled progression

The completed promoted checkpoints were:

| deep radius | middle radius | ultra radius | `floor(lambda*C)` | final excluded odd |
| ---: | ---: | ---: | ---: | ---: |
| 2,225,000 | 3,825,000 | 635,000 | 3,833 | 2,921,767,553 |
| 2,250,000 | 3,850,000 | 670,000 | 3,813 | 2,921,768,561 |
| 2,275,000 | 3,850,000 | 705,000 | 3,793 | 2,921,769,575 |
| 2,300,000 | 3,875,000 | 735,000 | 3,773 | 2,921,770,595 |
| 2,325,000 | 3,900,000 | 770,000 | 3,753 | 2,921,771,621 |
| 2,350,000 | 3,900,000 | 805,000 | 3,733 | 2,921,772,651 |
| 2,375,000 | 3,925,000 | 835,000 | 3,713 | 2,921,773,687 |
| 2,400,000 | 3,950,000 | 870,000 | 3,693 | 2,921,774,729 |

Each row is based only on completed gap-free scans and exact rational recomputation. The final row is the frozen load-bearing RL96 state.

A larger attempted jump toward deep radius `2,500,000` exceeded the execution window before producing completed scan records. It is not evidence and is not included in the certificate set.

## 4. Final exact four-tier geometry

Final staircase-complement corners:

`A=(0,7,000,001)`

`B=(5,000,031,3,950,001)`

`C=(7,500,033,2,400,001)`

`D=(10,000,033,870,001)`

`E=(15,000,036,0)`.

The final active `A-C` support is

`mu=1/7,000,001`

and

`lambda=4,600,000/52,500,238,500,033`.

Exact corner values under `lambda*d+mu*r` are

- `A = 1`;
- `B = 5,847,253,383,337 / 5,833,359,833,337 > 1`;
- `C = 1`;
- `D = 52,525,188,010,033 / 52,500,238,500,033 > 1`;
- `E = 23,000,055,200,000 / 17,500,079,500,011 > 1`.

Thus every integer point outside the certified four-tier union satisfies the final weighted support inequality.

Exact feasible nonnegative two-corner supports are still precisely

- `A-C`;
- `C-D`;
- `D-E`.

At the incoming `k6`, their contradiction margins are respectively

- `A-C`: `+61,283,778`;
- `C-D`: `+60,263,356`;
- `D-E`: negative by more than two billion.

`A-C` remains optimal throughout the promoted interval and at the first failure.

Classification: **updated exact four-tier supporting-line theorem + exact convex-envelope audit**.

## 5. Top-stratum monotonicity

At the final support,

`floor(lambda*C)=3,693`.

This is still far above the explicit `2`-unit improvement available from increasing the block-count stratum. The inherited top-stratum monotonicity argument therefore remains valid: it suffices to test

`b=k-1`.

Classification: **updated analytic monotonicity check**.

## 6. Exact RL96 interval propagation

Retain the conservative common successor ceiling

`L_common=15,000,053`.

The final verifier evaluates every odd

`2,921,766,551 <= k <= 2,921,774,729`

at `b=k-1` using exact rational arithmetic and the final `A-C` support.

All `4,090` values violate the necessary condition.

At `k=2,921,774,729`:

- `Q_min=123,139,091,657,859,100,054`;
- `D_b=16,435,134,487,197,130`;
- `R_b^max=10,369,447,116,390,851`;
- weighted bad-block bound `2,921,373,665`;
- forced multiscale-good blocks `401,063`;
- short-successor capacity `390,050`;
- contradiction margin `+11,013`.

At the next odd `k7=2,921,774,731`:

- `Q_min=123,139,091,657,859,099,906`;
- `D_b=16,435,218,789,060,534`;
- `R_b^max=10,369,500,304,944,757`;
- weighted bad-block bound `2,921,388,650`;
- forced multiscale-good blocks `386,080`;
- short-successor capacity `390,052`;
- contradiction margin `-3,972`.

### Theorem 6.1 — RL96 branch-specific odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`2,921,766,551 <= k <= 2,921,774,729`.

The updated branch-specific surviving odd window is

`2,921,774,731 <= k <= 42,150,931,559`, `k` odd.

Classification: **new analytic theorem + exact finite 2-adic certificates + exact rational interval audit**.

## 7. Geometry reserve and next coupling thresholds

At the final state, the current `A-C` support requires only

- middle radius at least `3,933,328` for `R_d=2,400,000`; actual `3,950,000`;
- ultra radius at least `866,674`; actual `870,000`.

For the next deep step `R_d=2,425,000`, the same depth floors and active support require

- `R_m>=3,949,995`;
- `R_u>=900,007`.

Thus the existing middle radius has five units of slack and no middle scan is needed for that single step, while ultra should be extended to at least `905,000` before promoting the next deep batch.

For `R_d=2,450,000`, requirements are

- `R_m>=3,966,662`;
- `R_u>=933,341`.

A natural second RL97 checkpoint is therefore middle `3,975,000`, ultra `935,000`, deep `2,450,000`, subject to live floor updates.

The ultra depth-axis nonbinding floor remains `3,499,992` because `D_u` did not change.

At the final `A-C` support, the `E`-axis minimum is now

`D_u>=11,413,095`.

Current reserve:

`3,586,940`.

## 8. Red-team audit

The promoted RL96 result preserves the inherited limitations and passes the same load-bearing checks:

1. RL81 common-mode freedom: no forbidden independence assumption introduced.
2. RL79 generalized-increment homogeneity: the support argument remains homogeneous in the required variables.
3. RL20 physical representative/packing separation: quotient addresses are not counted as physical blocks.
4. Primitivity: no relaxation is used to manufacture extra representatives.
5. First-Farey scope: the theorem is explicitly branch-specific.
6. RL88 arbitrary-reset family: no reset rigidity is assumed beyond the inherited minimal-reset interface used by the exact tier certificates.
7. Verification economy: inherited frozen minima are accepted after the incoming gate passes.
8. Successor charge: `L_common=15,000,053` is retained conservatively.
9. Support re-optimization: all feasible pair supports are enumerated exactly at the final state.
10. Live floor update: every completed new scan band is checked against the inherited global minimum before geometry is promoted.

## 9. Proof-state ledger additions

### New proved analytic mathematics

- final four-tier support theorem at deep radius `2,400,000`;
- exact support-edge feasibility/optimality result for `A-C`, `C-D`, `D-E`;
- maintained top-stratum monotonicity with `floor(lambda*C)=3,693`;
- branch-specific odd exclusion through `2,921,774,729`.

### New exact finite certificates

- ultra gap-free scan `605,001..870,000`;
- middle gap-free scan `3,800,001..3,950,000`;
- deep gap-free scan `2,200,001..2,400,000`;
- exact final interval audit over `4,090` odd values.

### No promotion from incomplete work

The timed-out large jump toward `R_d=2,500,000` produced no completed records and is excluded from the proof state.

## 10. Frozen global status

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open globally;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

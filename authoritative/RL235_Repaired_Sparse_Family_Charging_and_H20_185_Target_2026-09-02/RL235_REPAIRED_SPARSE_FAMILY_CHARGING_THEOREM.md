# RL235 — exhaustive sparse-family charging repair and H20 rebase

## 1. Incoming correction state

RL234 exposed a retained H20 necessary-state cell with

- `T=5*3^35=250157725494998535`,
- `H=20`,
- simultaneous owners `{32,33,34,35}`,
- full-prefix core `[96166487668,98855162143]`,

that was charged above RL231's generic H20 budget and was not covered by RL231's penalty for the distinct H20 invariant `3^36`, owners `{31,...,36}`.

Therefore RL231's promoted `>665` proof and its derived H17 quantitative target were demoted in RL234.

## 2. Exhaustive repaired state space

RL235 reconstructs the inherited first-defect arithmetic and full-prefix physical-gap filter for `tau=26..39`, then partitions every retained `(T,H)` terminal invariant at every endpoint where the simultaneous full-prefix owner set changes.

The exact reconstruction contains **7,531 atomic cells**. This is a retained necessary-state superset; no claim is made that every cell is physically realized.

For a cell with terminal numerator `T`, height `H`, and terminal-rank upper endpoint `r_hi`, the repaired local physical budget uses the maximum of three independently valid lower bounds on physical `|f|`:

1. generic defect floor `2^-(H+1)`;
2. RL234 corridor K-pricing `K_LO/T`, with `K_LO=128081997553`;
3. rank-endpoint K-pricing `K(r_hi)/T`.

For the third item, inherited exact log/exp bounds prove the rank coordinate has positive coefficients `s,d`, so `K(r)` decreases with rank. Every physical point in the cell has `r<=r_hi`, hence `K(r)>=K(r_hi)`. Exact rational exponential upper bounds give a rigorous lower bound for `K(r_hi)/T`.

## 3. Repaired monotone three-band schedule

Let `U=2^-25`. Define three charge levels in U-units:

- `a` for `tau<=34`;
- `b` for `tau=35,36`;
- `c` for `tau>=37`.

Let `B20` be the exact certified local K-priced budget of the RL234 H20 four-owner cell and `B24` the exact certified local K-priced budget of the binding H24 `tau=39` cell with `r_hi=111884226030`.

Set

- `c=B24`,
- `b=c`,
- `a=(B20-b)/3`.

Numerically this is approximately

- `a = 6.10177120865 U`,
- `b=c = 1.13796995829 U`.

The exact rational interval verifier is authoritative; decimals are orientation only.

## 4. Exhaustive local coverage and exact H21 penalty

Under this schedule, exactly **13** of the 7,531 atomic cells exceed their generic height budget.

Twelve are covered by their rigorous local K-priced budget.

The sole remaining excess is the exact inherited H21 terminal invariant

- `T=350220815692997949`,
- `H=21`,
- owners `{33,34,35}`,
- full-prefix core `[23369453298,41775866136]`.

RL231 independently certified chronological spacing `>=1001` for exactly this invariant, and RL234 explicitly preserved that recurrence theorem. Therefore its period occurrence cap is

`floor(L/1001)=137390654`, with `L=137528045312`.

No recurrence cap for one invariant is applied to another invariant or owner subset.

Subtracting the exact worst local excess at that exact cap yields

`ordinary absolute corrected flow > 712.303259566878... > 712`.

Hence, by the preserved signed-total/carry conversion,

- each signed corrected-flow mass is `>356`;
- each directional K variation is `>118`.

These are total-variation statements only.

## 5. Status of the old RL231 theorem

RL235 does **not** retroactively validate RL231's flawed proof. The historical RL231 charging argument remains demoted as written.

Instead RL235 supplies a new exhaustive proof which is stronger numerically (`>712` versus the former `>665`).

The former derived claims

- combined H17 incidence `<=1,615`,
- spacing-only H17 scale `85,103,989`,
- RL233's corresponding standalone 3-adic scale consequence,

remain demoted. They are not consequences of the repaired schedule.

## 6. Rebased successor bottleneck

Increase only the early charge by `dU` while preserving the present middle/late levels.

The inherited H21 penalty grows by `2dU` per capped H21 occurrence. Before any H20 penalty the exact net coefficient is

`2,515,773,745 - 2*137,390,654 = 2,240,992,437`.

The exact H20 `{32,33,34,35}` blocker contains three early owners and one middle owner, so each of its occurrences costs an additional `3dU` once its local budget is crossed.

Strict positive improvement therefore requires

`2,240,992,437 - 3 N20 > 0`,

hence

`N20 <= 746,997,478`.

At `N20=746,997,479` the first-order gain is exactly zero.

A direct combined-event spacing theorem gives:

- spacing `184`: `floor(L/184)=747,435,028`, insufficient;
- spacing `185`: `floor(L/185)=743,394,839`, sufficient.

Thus RL236 should attack chronological recurrence/return of this exact H20 invariant through separation 184, with spacing `>=185` as the first clean success threshold.

## 7. Preserved open state

Unchanged:

- sole high branch `(37,0,23,-1)`;
- K corridor `128081997553 < K < 146795909391`;
- necessary frontier `13415865870`;
- live e=4 rank `31435476727`;
- e=4 survivors through transition 43: `3856660232`;
- RL232 combined H17 spacing `>=1001` remains valid;
- RL233 finite-modulus decomposition remains valid;
- Gate A open;
- Gate B open;
- global non-trivial-cycle exclusion open.

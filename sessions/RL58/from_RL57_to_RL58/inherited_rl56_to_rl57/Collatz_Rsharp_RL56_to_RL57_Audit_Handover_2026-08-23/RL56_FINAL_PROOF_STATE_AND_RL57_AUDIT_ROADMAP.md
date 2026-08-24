# RL56 final proof state and RL57 audit roadmap

Date: 2026-08-23

## Executive status

RL56 did **not** close the safe-CF survivor, Gate A, Gate B, RL, or Collatz.

It did produce a genuine aggregate potential mechanism and a much sharper candidate interface to the terminal suffix. The strongest new finite claim is that every first-26 prefix still capable of satisfying the full total-mass requirement has

`Zx_26 <= 33/4`,

which would force

`Zx_late > 11/3`.

Together with the inherited defect budget this would force more than `2/3` late x-zero mass into displacement `<=1`, localizing the next proof problem to very small-height terminal grammar.

The `33/4` result is reproducible in the supplied script but remains **independent-audit pending**.

## A. Inherited/audited baseline that should remain fixed unless a verifier fails

From the RL55 audit handover and its verifier suite:

- exact legal first-26 maximum under the sequential cap:

  `34057930625026471931596 / 2954312706550833698643`

  `= 11.528207745072855...`;

- inherited total requirement `Zx>143/12`;
- inherited defect budget `E<5/3`;
- sequential x-zero cap `w_j<17/30`;
- exact defect identity `E=sum_j w_j[1-(2/3)^r_j]`;
- z=37 and z=39 closures remain intact;
- for the sole safe continued-fraction survivor, remaining odd `z>=41`;
- exact backward `Q_d=J+2^d-1` terminal grammar;
- radius-3 branch remains inherited/certified;
- global Gate A remains open;
- no valid global Gate-B/RL-to-radius-3 bridge has yet been proved.

The full inherited RL55->RL56 bundle is preserved under

`inherited_rl55_to_rl56/`.

## B. RL56 analytic results already documented

`RL56_AGGREGATE_POTENTIAL_AND_TERMINAL_COMPATIBLE_PREFIX.md` derives

`Xi = g[(T-1)/3^(d-1)+1/2^(d-1)]`

and

`Psi = g+Xi/2`.

The four legal forward maps give monotonicity of `Xi`, monotonicity of `Psi`, and the one-for-one zero-mass majorization

`Delta Psi >= w`

on every x-zero edge. Therefore for any legal segment

`Zx(segment) <= Psi(end)-Psi(start)`.

That document also proves that the old legal first-26 mass maximizer is terminal-incompatible and supplies an exact `10.7` terminal-compatible prefix certificate.

These are the first items RL57 should independently rederive.

## C. New session results requiring audit before promotion

### C1. `K>=25` interface

Using the inherited RL45 `H<=23` valuation certificate together with terminal `J=2^K`, `H<K`, and the inherited oddness of `K`, the current session reduces the live branch to

`K>=25`.

Audit the notation interface carefully.

### C2. Sharper `10.3` finite certificate

With `K>=25` and the sharp phase squeeze, the supplied exact search returns no terminal-compatible legal first-26 prefix above

`103/10`.

### C3. Coupled-K viable-prefix `33/4` certificate

A stronger search enforces a single compatible odd `K>=25` for both `Xi` and `Psi` terminal bounds and prunes any prefix that cannot possibly reach `Zx>143/12` with its remaining `Psi` room.

Fresh output:

`TARGET 33 4 8.25 hit False`.

A target-8 run has a witness with mass `8.172852...`, demonstrating nonvacuity.

If audited, conclude

`Zx_late>11/3`

and

`Psi_cut<3.084`.

### C4. Defect localization

If `Zx_late>11/3`, then the inherited defect formula gives

`sum_{late, r_j>=2} w_j <3`,

so

`sum_{late, r_j<=1} w_j >2/3`.

Since each `w_j<17/30`, at least two such near-aligned late zeros are forced.

## D. Exact obstruction still open

The scalar `Psi` potential cannot by itself close the suffix because the height-one `00/11` subsystem contains neutral Collatz-conjugate pumping. A successful proof must use terminal arithmetic/divisibility, not merely monotonicity.

The next candidate mechanism is the inherited backward `Q` grammar, where backward `11` runs are controlled exactly by `v3(Q)`, coupled with:

- odd terminal `K>=25`;
- terminal `J_end=2^K`;
- legal cut `Psi_cut<3.084` if the new certificate survives audit;
- exact suffix event counts;
- forced `>2/3` mass in displacement `<=1`.

## E. RL57 audit sequence

### Gate 1 — integrity

Verify all checksums and run `verification/run_all_rl56_to_rl57_audit_verifiers.sh`. Stop on any failure.

### Gate 2 — analytic rederivation

Recompute all four increments of `Xi` and `Psi` from the exact forward maps. Check signs, height-one equalities, start/end values, and strict-vs-nonstrict inequalities.

### Gate 3 — independent certificate audit

Do not merely rerun the same Python files. Reimplement at least the `33/4` decision in a structurally independent way if feasible (different DP state representation, rational arithmetic organization, or a compact C++ implementation). Confirm that every prune is in the survivor-favoring direction.

In particular audit:

- legal sequential-cap enforcement;
- forced-y transition rule;
- same-`K` selector;
- `W` interval pruning;
- `Xi/Psi` cut pruning;
- total-viability prune;
- memo dominance condition;
- target strictness at `33/4`.

### Gate 4 — reconstruct displacement-0/1 local grammar

Starting from the inherited rank-matching definition, enumerate exactly all local configurations realizing `r_j=0` and `r_j=1`. Confirm whether they indeed live only at `d<=2` and state the precise edge macros.

### Gate 5 — focused divisibility attack

Use the exact backward maps

`11: Q->2Q/3`,

`10: Q->2Q+1`,

`00: Q->2Q-(3^d-1)`,

`01: Q->2Q/3-3^(d-1)`

together with `v3(Q)` to bound the total weight of the audited displacement-`<=1` macros.

Primary theorem target:

`M_le1 <= 2/3`.

A strict/weak endpoint should be handled carefully because the inherited lower bound is strict `M_le1>2/3`.

## F. Fallback hierarchy

If the `M_le1<=2/3` target fails:

1. identify the exact repeatable local macro and its weight evolution;
2. prove or disprove its compatibility with terminal `J=2^K` via `Q mod 3^n` or `v3(Q)`;
3. if only finitely many `K` remain, certify that bounded window exactly;
4. if the obstruction is inherently an unrestricted Collatz-conjugate subsystem, stop extending survivor-local z thresholds and pivot back to the global Gate-A/Gate-B bridge problem.

## G. Success classifications for RL57

**Strong:** audit survives and `M_le1<=2/3` eliminates the safe-CF survivor.

**Significant:** audit survives and a terminal divisibility theorem reduces the near-aligned grammar to a bounded explicit remainder.

**Useful:** independent verification of the `33/4` certificate and a complete exact classification of displacement-0/1 macros.

**Failure/repair:** any new RL56 theorem or finite certificate is invalidated; repair the first broken interface before further extension.

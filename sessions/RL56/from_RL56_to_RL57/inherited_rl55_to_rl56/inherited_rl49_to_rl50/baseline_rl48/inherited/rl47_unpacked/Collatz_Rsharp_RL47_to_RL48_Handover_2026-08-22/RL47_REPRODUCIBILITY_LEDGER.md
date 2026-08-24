# RL47 Reproducibility Ledger

Date: 2026-08-22

Run commands from the bundle root.

## 1. Integrity

```bash
sha256sum -c SHA256SUMS.txt
```

The inherited RL46->RL47 bundle and its sidecar are retained under `inherited/`.

## 2. Core RL47 verifier

```bash
bash verification/run_rl47_core_verifiers.sh
```

This runner:

1. runs the exact `Phi` identity regression;
2. runs the rational rank-transport bound verifier;
3. compiles the arbitrary-precision fixed-t future-hull verifier;
4. reruns q=17, q=24, q=55, and q=79;
5. asserts `any_violation 0` for all four pairs.

Expected key q=79 conclusion:

`PAIR (214,135,79) any_violation 0`

The exact state counts/timings may vary only if the implementation or compiler changes; the logical conclusion must not.

## 3. q134 stress verifier

```bash
bash verification/run_rl47_q134_stress_verifier.sh
```

This compiles `verify_fixed_t_hull_budgetres64.cpp` and reruns

`t=2,4,6,8,10,12,14,16`

for `(a,ell)=(363,229)`. Every run must print `hit 0`. On some GCC/Boost combinations compilation emits an aggressive-loop-optimization warning inside Boost `cpp_int`; the rerun in this environment still compiles and reproduces all expected exact outputs. Treat any change in logical output as a failure.

The q134 result is only a finite low-t certificate. Combined with the independent analytic rank bound, the unresolved strip remains even `t=18..114`.

## 4. Core sources

- `rl47_additions/verify_fixed_pair_violation_by_t_hull.cpp`
  - arbitrary-precision exact fixed-t forward DP;
  - exact prefix cap at every live state, justified by cap-death monotonicity;
  - conservative backward interval hull in `J`;
  - exact area/descent reserve;
  - minimum-`H` dominance at exact future-relevant states.

- `rl47_additions/verify_rl47_phase_coordinate.py`
  - exact transition identity for `Phi`;
  - exact neutral `11` cancellation;
  - audited `(65,41)` witness regression.

- `rl47_additions/verify_rl47_rank_transport_bound.py`
  - exact `(65,41)` rank-position identity regression;
  - rational relaxed upper bound under hypothetical strict violation;
  - high-t analytic exclusions.

- `rl47_additions/verify_fixed_t_hull_budgetres64.cpp`
  - exact height-one macro traversal;
  - conservative future interval hull;
  - conservative modulo-64 future residue sieve with area budget;
  - q134 low-t stress certificate.

## 5. Recorded outputs

- `RL47_PHASE_COORDINATE_RUN.txt`
- `RL47_RANK_TRANSPORT_BOUND_RUN.txt`
- `RL47_Q17_HULL_REGRESSION.txt`
- `RL47_Q24_HULL_REGRESSION.txt`
- `RL47_Q55_HULL_REGRESSION.txt`
- `RL47_Q79_FIXED_T_HULL_RUN.txt`
- `RL47_Q134_SMALL_T_EXACT_RUN.txt`
- `RL47_Q134_t16_budgetres64.txt`

These are reference outputs only. The bundled runners are the authoritative reproduction path.

## 6. Inherited verification

To reconstruct RL46/RL45 provenance:

```bash
cd inherited
sha256sum -c Collatz_Rsharp_RL46_to_RL47_Handover_2026-08-22.zip.sha256
```

Then unpack that bundle and follow its `README_START_HERE.md`.

Do not silently replace inherited exact certificates with RL47 regression tests: the inherited `(65,41)` minimum-excess `125` witness, for example, proves more than the RL47 no-strict-violation regression.

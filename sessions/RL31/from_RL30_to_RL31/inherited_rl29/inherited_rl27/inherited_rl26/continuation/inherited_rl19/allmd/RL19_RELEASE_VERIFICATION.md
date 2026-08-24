# RL19 release verification

Date: 2026-08-20 (Europe/London)

## Baseline five-verifier gate

At the start of the RL19 work, all five verifiers required by the RL18 kickoff were run successfully:

- `verify_rl18_repairs.py` — **PASS**
- `verify_rl18_global_orbit_identity.py` — **PASS**
- `verify_rl18_cubic_norm_reduction.py` — **PASS**
- `inherited/verify_rl12_same_direction_canonical.py` — **PASS**
- `inherited/verify_rl13_p3_j0_interior.py` — **PASS**

The completed inherited RL12 and RL13 outputs are preserved in `logs/RL12_FRESH_RECHECK_LOG.txt` and `logs/RL13_FRESH_RECHECK_LOG.txt`.

During final housekeeping, another attempt to run the slow inherited RL12 checker inside one hosted command hit the host wall-clock limit before completion. It produced no assertion failure. This is recorded as a runtime limitation, **not** as a mathematical failure; the earlier completed fresh PASS is retained.

## Affected/new release checks

Fresh on the release copy:

- `verify_rl19_cubic_skew_closure.py` — **PASS**
- `verify_rl19_global_weighted_population.py` — **PASS**
- `verify_rl19_global_odd_step_product.py` — **PASS**
- `inherited/verify_rl13_p3_j0_interior.py` — **PASS**

Release logs are in `logs/RL19_RELEASE_*.txt`.

`verify_rl18_repairs.py` and `verify_rl18_global_orbit_identity.py` also passed again during final-session checking. The cubic-norm baseline checker had already passed earlier in the same session; a later batched rerun was interrupted by the shared command timeout before that checker emitted output.

## Failure/repair history that must remain visible

The first strengthened RL19 cubic checker found a genuine omitted one-gap-`a` boundary. Work stopped, the analytic proof was repaired with the short-order lemma, and only the repaired version was promoted. The final RL19 cubic verifier passes the repaired branch classification.

No computational cutoff was promoted to a theorem.

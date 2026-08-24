# Collatz R-sharp / RL18 repair and strategy handover

This bundle repairs the defects identified by the RL17 audit and adds two strategic analytic tools:

- an exact unbounded-radius orbit-sum identity;
- an Eisenstein-norm reduction for the last open radius-3 cubic leaf.

It **does not claim a proof of RL or Collatz**.

## Main files

- `START_HERE.md` — concise orientation and run order.
- `RL18_PROOF_STATUS_AND_BRANCH_LEDGER.md` — authoritative current proof state.
- `RL18_REPAIRED_RADIUS3_PROOF_REPORT.md` — reconstructed RL12/RL13 proofs and newly closed omitted branches.
- `RL18_CUBIC_NORM_REDUCTION.md` — sharpened reduction for the final radius-3 leaf.
- `RL18_GLOBAL_ORBIT_SUM_IDENTITY.md` — exact arbitrary-radius invariant.
- `RL18_EXTERNAL_DEPENDENCY_AUDIT.md` — LMN/Jacobi/Jacobian dependency check.
- `RL18_STRATEGIC_WORKPLAN.md` — research priorities.
- `NEXT_SESSION_KICKOFF_PROMPT.md` — ready-to-paste kickoff.
- `verify_rl18_repairs.py` — finite tails/constants for the repaired branches.
- `verify_rl18_global_orbit_identity.py` — exhaustive small sanity check of the global identity.
- `verify_rl18_cubic_norm_reduction.py` — exhaustive small sanity check of the phase/norm reduction.
- `inherited/` — original RL17 baseline and the two inherited RL12/RL13 verifiers.
- `logs/` — fresh verifier outputs.

See `SHA256_CONTENTS.txt` for the integrity manifest.

## Release verification

Final housekeeping rerun on 2026-08-20 (Europe/London) completed successfully:

- `verify_rl18_repairs.py` — PASS
- `verify_rl18_global_orbit_identity.py` — PASS
- `verify_rl18_cubic_norm_reduction.py` — PASS
- `inherited/verify_rl12_same_direction_canonical.py` — PASS
- `inherited/verify_rl13_p3_j0_interior.py` — PASS

Fresh outputs are in `logs/`.  `SHA256_CONTENTS.txt` is the release integrity manifest and excludes itself by design.

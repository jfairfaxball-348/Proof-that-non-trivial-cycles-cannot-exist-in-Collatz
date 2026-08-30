# RL190 verification

Run:

```bash
bash verification/run_fast_rl190_verifiers.sh
```

The verifier uses exact Python integer/Fraction arithmetic only.

It certifies the phase-43 affine exclusion, rank-empty separations 44/45, spacing `>=46`, the two-point separation-46 exceptional seam, the exact `1/15` `N_35` density and crossover, the phase-resolved dangerous H21 `{33,34,35}` core, and persistence of the two-level charging plateau.

It does not certify physical realization of any rank and does not claim separation-46, branch, or global closure.

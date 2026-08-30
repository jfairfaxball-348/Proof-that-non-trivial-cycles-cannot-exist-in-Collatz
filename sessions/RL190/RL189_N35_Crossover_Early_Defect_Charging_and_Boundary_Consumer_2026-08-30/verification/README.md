# RL189 verification

Run:

```bash
bash verification/run_fast_rl189_verifiers.sh
```

The verifier uses exact Python integer/Fraction arithmetic only. It certifies the separation-41 affine exclusion, separation-42 rank exclusion, spacing `>=43`, the `3/43` `N_35` cap, and the height-21 two-level charging obstruction.

It does not certify physical realization of the terminal-rank core and does not claim branch or global closure.

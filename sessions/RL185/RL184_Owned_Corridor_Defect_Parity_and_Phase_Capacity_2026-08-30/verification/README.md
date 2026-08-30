# RL184 verification

Portable fast suite:

```bash
bash verification/run_fast_rl184_verifiers.sh
```

The exact verifier uses Python integer/Fraction arithmetic. It checks the global one-state phase-overlap refinement, exact three-step mechanical-factor vocabulary, restricted height/template/map counts, zero-intercept rigidity, repeated-map floors, 39-zero extremal arithmetic, clean 40-edge corridor floor, and distinct nonzero-defect incidence.

The signed affine-intercept identity and zero-run recurrence are analytic identities recorded in the RL184 report; the verifier certifies the finite and numerical comparisons consumed by them.

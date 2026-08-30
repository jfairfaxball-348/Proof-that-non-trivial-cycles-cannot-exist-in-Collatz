# RL182 verification

Portable fast suite:

```sh
bash verification/run_fast_rl182_verifiers.sh
```

The exact verifier uses Python integer/Fraction arithmetic and rigorous rational logarithm/exponential enclosures. It checks the refined high-branch mass band, universal p-window q-mass/tail floor, ternary ownership-depth size thresholds, fixed-defect repetition floors, and strengthened shallow-width occupancy.

The chronological transport and ternary suffix formulas are analytic identities recorded in the RL182 report; the verifier certifies all numerical comparisons consumed by them.

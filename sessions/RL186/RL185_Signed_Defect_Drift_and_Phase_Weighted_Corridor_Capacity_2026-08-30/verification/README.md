# RL185 verification

Run:

```bash
bash verification/run_fast_rl185_verifiers.sh
```

The verifier checks the exact mechanical late-bit height envelope through offset 39, the height-dependent corridor multiplicity table, the `2^26` weighted-capacity inequality, the signed threshold-count arithmetic, and a rational enclosure proving `0<F2<1/2`.

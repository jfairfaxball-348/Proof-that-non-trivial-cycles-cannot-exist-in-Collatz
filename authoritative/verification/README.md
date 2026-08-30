# RL180 verification

Run:

```sh
bash verification/run_fast_rl180_verifiers.sh
```

The phase-support certificate reconstructs the RL179 high-branch necessary automaton and certifies the phase-31 budget and delayed-support ladder with exact `Fraction` arithmetic.

The global-height certificate uses rational atanh logarithm enclosures and rational Taylor exponential enclosures. It certifies the RL180 support band, mechanical-loss splice, internal least-state band, and shallow-population floors without external computational minima.

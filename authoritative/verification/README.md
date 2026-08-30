# RL193 portable fast verification

From the package root run:

```sh
sh verification/run_fast_rl193_verifiers.sh
```

The wrapper runs both complete portable verifiers:

1. `verify_rl178_inherited_early_window.py`: byte-for-byte inherited RL178
   necessary-transition certificate for the canonical early-defect window;
2. `verify_rl193_physical_debt.py`: exact integer/Fraction checks for the
   atom mappings, all carry/early-window deletions and boundaries, buffers,
   valuation constants, logarithm enclosure and cancellation fractions.

Analytic telescoping and the all-offset valuation inequalities are proved in
the main report.  The finite verifier checks their constants; it is not a
substitute for those proofs.  No astronomically large `2^A` or `3^L` is built;
the endpoint congruence is checked with modular exponentiation.

Neither surviving necessary states nor remaining ranks are physical cycles.
The internal manifest covers every payload file other than itself.  The ZIP
and outer sidecar are envelope files and are not included in the payload.

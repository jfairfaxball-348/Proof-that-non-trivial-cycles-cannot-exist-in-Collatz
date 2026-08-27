# RL135 verification

Run:

```bash
bash verification/run_fast_rl135_verifiers.sh
```

The verifier uses exact `fractions.Fraction` arithmetic and rigorous
atanh-series logarithm enclosures. It checks the finite/rational constants
used by RL135:

- survivor/continued-fraction neighborhood and determinant bases;
- the `g Delta<log(2)` endpoint;
- `m<2^76` on the one-defect range;
- the refined `m<2^75` bound at 28 billion;
- determinant `±2` discrepancy windows and the `g=16/17` shell threshold;
- the canonical-contact absolute gap;
- low-multiplicity exceptional counts, conditional population floors, and
  absolute state-window inequalities.

The analytic physical arguments are in the RL135 report. Any line using
`R0=2^71` remains explicitly conditional on that inherited external input.

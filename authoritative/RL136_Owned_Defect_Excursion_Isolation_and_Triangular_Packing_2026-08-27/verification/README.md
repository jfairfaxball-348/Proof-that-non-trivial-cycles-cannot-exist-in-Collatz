# RL136 verification

Run:

```bash
bash verification/run_fast_rl136_verifiers.sh
```

The verifier uses exact `fractions.Fraction` arithmetic and rigorous logarithm enclosures. It checks:

- the `exp(g Delta)<4/3` isolation endpoint `g=320,125,202,432`;
- the determinant/mechanical margin used by the isolation theorem;
- the inherited one-period mechanical-weight envelope;
- the triangular exceptional-population relaxation;
- the monotone `m<2^75` endpoint `g=56,336,298,016` and failure of that same envelope at the next integer;
- the low-shell and last-translate absolute gap constants.

The owned physical proofs and red-team scope are in the RL136 report. No line in the RL136 verifier uses the inherited external `R#>=2^71`.

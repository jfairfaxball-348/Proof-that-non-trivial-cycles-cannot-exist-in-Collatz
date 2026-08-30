# RL192 fast verification

Run from the package root:

```bash
python3 verification/verify_rl192_full_period_phase_lock.py
```

or:

```bash
sh verification/run_fast_rl192_verifiers.sh
```

The verifier uses exact integer/Fraction arithmetic and rigorous logarithm-series tails.  It checks the full-period overlap, gap-free two-atom rank split, phase-lock exponents, `0<Delta<2^-40`, target-miss bounds, relaxed-ball radius floor, and explicit single-final-error relaxed witness.

The witness certifies a method limitation only.  It does not certify a physical epsilon sequence or realized Collatz state.

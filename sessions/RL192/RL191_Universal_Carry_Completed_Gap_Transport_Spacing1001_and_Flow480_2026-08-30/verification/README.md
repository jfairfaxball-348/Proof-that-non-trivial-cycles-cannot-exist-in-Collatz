# RL191 fast verification

Run:

```bash
python3 verification/verify_rl191_universal_gap_spacing_and_charging.py
```

or:

```bash
sh verification/run_fast_rl191_verifiers.sh
```

The verifier uses exact integer/Fraction arithmetic and checks:

- universal-gap exclusion of the two RL190 phase-46 exceptional ranks;
- all necessary separations 46..1000 on exact constant-mechanical-word atoms;
- spacing-1001 `N35` density arithmetic;
- inherited RL187 low/high charging-family safety under the RL191 weights;
- exact >480 ordinary-flow and >80 directional-`K` consequences.

The finite separation certificate is deliberately bounded at 1000.  It does not claim an unbounded resonance theorem.

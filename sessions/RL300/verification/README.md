# RL300 verification

`verify_rl300_fast.py` is the portable closeout verifier.

It uses exact rational atanh bounds for `ln 2` and `ln 3` to:

- certify the 34-term common continued-fraction prefix;
- reconstruct the 51 one-sided resonance records from U5 through the direct-start boundary;
- compute exact relaxed quotient ceilings;
- compute exact A/B physical maxima;
- verify the final safe physical envelope lies below the frozen external delay threshold;
- verify the next direct-start record crosses that threshold;
- independently replay ordinary Collatz delays 2334 and 2337 for the two load-bearing external record values;
- verify the selector excess lower bound dominates `J+2`.

The verifier does not and cannot replace the external exhaustive computation proving the delay-record pair is consecutive/confirmed. That dependency is frozen and classified in `../RL300_EXTERNAL_DELAY_CERTIFICATE.md`.

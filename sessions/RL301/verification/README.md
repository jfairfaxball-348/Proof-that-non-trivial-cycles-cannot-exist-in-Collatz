# RL301 verification

Run:

`python3 verify_rl301_fast.py`

The portable verifier uses only Python's standard library and exact rational/integer arithmetic. It certifies:

- the 44-term continued-fraction prefix used by RL301;
- the exact one-sided resonance records and relaxed quotient ceilings needed for the promoted frontier;
- the exact B-ancestor maxima and finite-certificate boundary;
- the four-odd-step affine B-ancestry identity;
- replay of the load-bearing external record holder's ordinary delay 2456;
- the `J_B<=2452` conversion and selector-margin inequality;
- the first uncovered record and later finite-ladder diagnostic values.

It does not reproduce the historical external exhaustive class-record computation. That dependency is explicitly documented in `../RL301_EXTERNAL_CLASS_RECORD_CERTIFICATE.md`.

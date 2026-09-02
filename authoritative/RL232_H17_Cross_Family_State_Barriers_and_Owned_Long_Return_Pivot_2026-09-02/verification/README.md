# RL232 verification

Portable standard-library verification suite.

Run:

`bash verification/run_fast_rl232_verifiers.sh`

The suite checks:
- exact four-direction H17 return exclusion through separation 1000;
- relaxed B-return method barrier;
- exact H17 K-core and scalar full-period stress tests;
- H17 owned-prefix graph and zero-interface theorems;
- positive moving-window saturation barrier;
- proof-state/successor consistency.

All mathematical inequality decisions in the Python verifiers use exact integer/Fraction arithmetic or rigorous rational enclosures.

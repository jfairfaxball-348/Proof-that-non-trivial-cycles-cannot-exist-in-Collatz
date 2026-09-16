# RL336 independent red team

Status: GREEN after candidate execution.

The independent `verification/red_team_rl336.py` reconstructs all p=5 and p=6 excluded prefix families, computes their required residues by three-way Hensel lifting rather than the main verifier's modular inverse, and verifies the exact minima. It then recomputes the q=32 edge potential with reversed edge order and checks all 2,242 inequalities and the range `0..43`. Finally it independently continues the two maximum-escape witness starts for 229 and 234 odd steps respectively.

The zero-run counts and per-factor maxima are also cross-checked by a separate C++ implementation against the portable Python suite. No contradiction or scope strengthening was found. The q=33 diagnostic remains unpromoted.

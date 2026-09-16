# RL335 closeout verification

Date: 2026-09-16
Status: GREEN FOR ATOMIC PROMOTION
BASE_HEAD: `a22d083d82bce4e09657c4e5a39bb941d7230a11`
Transport: committed flat Git-tree authority.

Candidate checks executed from the frozen candidate directory:

- `python3 -I verification/verify_rl335_physical_and_q28.py` — GREEN; singleton T 9,836 / 31 pairs / max escape 185; singleton L 4,764 / 141 / 184; p2 11,682 / 176 / 151; p3 7,030 / 165 / 133; p4 79,820 templates, 4,986 physical / 141 / max escape 81; `(37,37)` 213 p4 templates and zero physical; graph 37 states / 2,242 edges; density potential 0..31; q=28 potential 0..28.
- `python3 -I verification/verify_rl335_consumer.py` — GREEN; rho60 RHS floor 32,546,289,526; uniform rho2895 bridge floor 32,546,289,530; rho22,000,000 ordinary upper 32,546,008,794; promoted cap 32,546,289,530.
- `python3 -I verification/red_team_rl335_q28.py` — GREEN using reversed edge order; independently confirms 2,242 edges, potential ranges, exact self-loop slack 141, q28 charge -1, q29 charge +4, and all-length monotonicity for q<43.

No mathematical defect was found. Scratch-only count/arithmetic corrections are recorded in `RL335_CORRECTION_AND_DEMOTION_LEDGER.md`.

Knowledge catalogues are stale/deferred.

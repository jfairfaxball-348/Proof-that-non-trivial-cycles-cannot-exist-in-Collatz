# RL268 closeout

Date: 2026-09-06

Incoming base HEAD: `785c9eaf1db327937783cb4358fb5d263cb48110`.

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

Closed in this generation:
- determinant-one `[2,1,1,1]`.

Previously closed and inherited unchanged:
- `[3,2]` (RL266);
- `[3,1,1]` (RL267);
- `[2,2,1]` (RL267).

Remaining determinant-one leaf:
- `[1,1,1,1,1]`.

Radius 5 remains open. Completing `[1,1,1,1,1]` would complete the determinant-one sector only; `|kappa|=3` and `|kappa|=5` would still remain unless eliminated by a new uniform argument.

Verifier suite:
- `verification/verify_rl268_analytic.py`;
- `verification/verify_rl268_2111.cpp`;
- `verification/redteam_rl268_2111.cpp`;
- `verification/rl268_2111_pairs.csv`.

Corrections made before promotion are recorded in `RL268_CORRECTION_DEMOTION_LEDGER.md`; no inherited result is demoted.

Successor: RL269, prepared but NOT STARTED, targeting determinant-one `[1,1,1,1,1]` only.

Knowledge catalogues: stale/deferred; do not hand-edit generated catalogues during closeout.

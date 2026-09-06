# RL267 closeout

Date: 2026-09-06

Incoming base HEAD: `2c247c6e25c1427739224e8a0308356dac067be2`.
Incoming authoritative tree: `2005969090dc36b9b32fa1a0ac8181183632131b`.

Classification: **RADIUS5_KAPPA1_311_221_CLOSED**.

Closed in this generation:
- determinant-one `[3,1,1]`;
- determinant-one `[2,2,1]`.

Previously closed and inherited unchanged:
- determinant-one `[3,2]` (RL266).

Remaining determinant-one leaves:
- `[2,1,1,1]`;
- `[1,1,1,1,1]`.

Radius 5 remains open. `|kappa|=3` and `|kappa|=5` remain frozen until determinant one is complete. Gate A, the fifth selector, selector enumeration and the general Radius-n programme remain frozen. Gate B remains open.

Corrections made before promotion are recorded in `RL267_CORRECTION_DEMOTION_LEDGER.md`; no inherited result is demoted.

Verifier suite:
- `verification/verify_rl267_analytic.py`;
- `verification/verify_rl267_311.cpp`;
- `verification/redteam_rl267_311.cpp`;
- `verification/verify_rl267_221.cpp`;
- `verification/redteam_rl267_221.cpp`;
- `verification/redteam_rl267_small.py`.

Successor: RL268, prepared but NOT STARTED, targeting `[2,1,1,1]` first.

Knowledge catalogues: stale/deferred; connector closeout does not hand-edit generated catalogues.

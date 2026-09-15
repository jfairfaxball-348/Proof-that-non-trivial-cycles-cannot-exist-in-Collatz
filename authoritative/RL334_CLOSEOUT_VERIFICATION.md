# RL334 closeout verification

Date: 2026-09-15
Status: GREEN FOR ATOMIC PROMOTION
BASE_HEAD: `31352b47ae6e27fbf019ea8270faf73f894510bc`
Transport: connector-produced committed flat Git-tree authority.

Candidate checks executed from a clean candidate directory:

- `python3 -I verification/verify_rl334_zero38.py` — GREEN; 38 factors, 1,825,797 candidates, maximum escape 213 odd steps.
- `python3 -I verification/verify_rl334_refined_charge.py` — GREEN; 385 states, 15,835 edges, density potential 0..31, q=22 potential 0..44.
- `python3 -I verification/verify_rl334_consumer.py` — GREEN; cap `32546313237`, lower bootstrap `32546313238`, exact finite range and handoff checks pass.
- `python3 -I verification/red_team_rl334_refined_charge.py` — GREEN; independent reverse-order max-plus reconstruction reproduces charge range 0..44.

The final lower-bootstrap reconstruction is GREEN: total-44 rows 13,559, large rows 7,189, inherited 323-state base projection unchanged; the only new RL333-relative total-44 realization `(38,6)` is removed by the proved 38-zero exclusion.

A closeout bookkeeping correction changes the final refined graph cardinality from an intermediate reported 17,348 edges to the verified 15,835 edges. The q=22 theorem is unchanged and passes both primary and reverse-order checks.

Remote `main` was reconfirmed at BASE_HEAD before candidate promotion. The successor is exactly RL335 and START_HERE names exactly one live RL335 target. Knowledge catalogues are stale/deferred by connector policy and are not part of the proof-state gate.

Post-commit readback must confirm the new remote ref, frozen `sessions/RL334/`, successor `authoritative/START_HERE.md`, and the committed verifier paths.

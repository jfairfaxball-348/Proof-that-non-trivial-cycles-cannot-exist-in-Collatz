# RL286 post-closeout mechanical startup repair

Date: 2026-09-09

Classification: `MECHANICAL_HANDOVER_REPAIR_ONLY`

This repair was triggered by the RL287 start gate. It does not alter any RL286 mathematical result or proof-state classification.

## Defects found

1. `sessions/RL286/RL286_CLOSEOUT.md` and `README.md` referenced `verification/RL286_RED_TEAM.md`, but that file was absent.
2. `sessions/RL286/RL286_TRANSPORT.md` claimed a `SHA256SUMS.txt` sidecar that was never committed.
3. `authoritative/START_HERE.md` identified RL287 as incoming, but `authoritative/` still contained the stale RL286 target while the verified RL287 target existed only in the frozen RL286 handover.

## Repair actions

- reran the committed RL286 portable verifier independently and reproduced the recorded PASS counts exactly;
- restored `verification/RL286_RED_TEAM.md` with an explicit proof-state/overclaim audit;
- corrected the transport note to the actual connector-worker integrity scheme based on Git object identities, verifier output, red team, and readback;
- copied the already-frozen RL287 target into `authoritative/` using the identical blob identity;
- removed the stale RL286 target from `authoritative/`;
- updated `authoritative/START_HERE.md` to point to the authoritative RL287 target.

## Proof-state effect

None.

RL286 remains classified

`EXCURSION_CARRY_COUPON_DEFECT_BRIDGE_AND_STATE_RESERVE_BARRIER_PROVED`.

Gate A remains open at odd `k>=25`, `H_can<k`. Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

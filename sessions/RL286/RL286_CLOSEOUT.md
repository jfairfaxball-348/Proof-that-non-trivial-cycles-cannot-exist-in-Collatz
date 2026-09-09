# RL286 closeout

Date: 2026-09-09

## Frozen classification

Primary:

`EXCURSION_CARRY_COUPON_DEFECT_BRIDGE_AND_STATE_RESERVE_BARRIER_PROVED`

Promoted analytic subordinate results:

- `EXCURSION_CARRY_EQUALS_NORMALIZED_COUPON_DEFECT_PROVED`;
- `EXCURSION_HEIGHT_SUPPORTED_CELL_DECOMPOSITION_PROVED`;
- `STATE_FREE_COMPONENT_HEIGHT_CARRY_BUDGET_BARRIER_PROVED`.

## Gate-A proof state

Gate A remains open:

`H_can>=k`

at terminal `d=1,J=2^k`.

Exact residual remains:

`k>=25`, `k` odd, `H_can<k`.

The preferred checkpoint theorem remains open:

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

No global post-column valuation theorem is claimed.

## Main advance

For every genuine first-return excursion,

`C_E=W_x-W_y=3^r D_E/Q_in`

and equivalently

`C_E/2^L=D_E/Q_out`.

The carry component is therefore exactly the return-normalized coupon defect.

The component contains exactly `h` carry/coupon cells, all with binary exponent at most `h-1`.

The one-zero family proves that this support theorem is insufficient for a state-free carry budget:

`C_E/2^h=(3/2)^h-1`.

The successor must add a state-dependent reserve closed under arbitrary positive zero-height boundary retention.

## Verification

Portable regression verifier:

`verification/verify_rl286_component_carry.py`

Recorded stdout:

`verification/RL286_FAST_VERIFIER_OUTPUT.txt`

Red team:

`verification/RL286_RED_TEAM.md`

Result: PASS.

## Successor

RL287 should attack a **return-normalized defect reserve**. It should combine:

- the exact component identity `C_E/2^L=D_E/Q_out`;
- one-zero rigidity `h=nu_2(J_in+4)`;
- multi-zero `F`/mass pricing;
- an exact treatment of zero-height positive boundary retention.

It must not revive local `nu_2` monotonicity or assume a height-only carry cap.

Gate B, fifth selector and Radius 6+ remain frozen.

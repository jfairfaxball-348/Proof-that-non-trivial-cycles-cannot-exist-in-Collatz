# RL326 closeout — mechanical-excess density and global carry contraction

Date: 2026-09-15
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `82d9102e013fcf5d239e3cfee4a9b4c69b82fa00`
Successor: RL327

## Executive conclusion

RL326 does not close R1, Gate A, Gate B, or global positive non-trivial-cycle exclusion.

It converts the finite maximal-carry endgame into a support-uniform theorem. A complete exact audit of all 50 length-49 factors of the least-root mechanical gap word proves that a high-carry genuine trajectory cannot contain 49 consecutive ideal backward gaps. Consequently the normalized displacement excess is positive at least once per 50 ranks across the full crossing-to-canonical interval.

The resulting mandatory coefficient loss feeds through the genuine RL325 ownership telescope and contracts

`n<=33068504812`

to

`n<=32839291403`.

This removes 229,213,409 carry values at once and consumes the full incoming maximal-carry endgame.

## Verification

`verification/verify_rl326_mechanical_density.py` uses exact integer and `Fraction` arithmetic to check the logarithmic bounds, all 50 mechanical factors, every forced residue/backward reconstruction, the high-carry threshold, the density count, and the final rational carry bound.

Red-team result: GREEN.

## Scope

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.
External `2^71` least-state floor remains conditional.

R1 Parent Bridge: OPEN.
Gate A: OPEN.
Gate B: OPEN.
`g=1`: separate.
Global positive non-trivial-cycle exclusion: OPEN.

## GLOBAL PROOF ROADMAP STATUS

`CURRENT_STAGE = R1`

`CURRENT_STAGE_NAME = Parent Bridge`

`CURRENT_STAGE_PROGRESS = 68%`

`THIS_SESSION_ADVANCE = Complete 50-factor mechanical certificate, positive-excess density at least one rank per 50 in the high-carry regime, elimination of the RL325 maximal endgame, and carry contraction to n<=32839291403.`

`CURRENT_STAGE_BLOCKER = Extend the mechanical-excess consumer below the new cap, strengthen the density/weight loss, or convert positive excess into a genuinely owned descent closing the remaining K<0 branch.`

`ADVANCE_CRITERION = Close the full remaining K<0 parent bridge at required scope before moving to R2.`

`REMAINING_STAGES = R2 g=2 Closure; R3 g>1 Lift; R4 Scale Closure; R5 g=1 Closure; R6 Gate Reconciliation; R7 End-to-End Proof.`

`ROADMAP_DELTA = ADVANCE`

`GLOBAL_PROOF_STATUS = OPEN`

# RL325 closeout — global ownership telescope and finite maximal-carry endgame

Date: 2026-09-15
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `e12cbd171fd9b4920c32ba10f1066faea77ad1b1`
Successor: RL326

## Executive conclusion

RL325 does not prove Gate A, Gate B, the full R1 parent bridge, global positive non-trivial-cycle exclusion, or the Collatz conjecture.

It does achieve the requested global change of attack in the remaining ordered `g=2`, `Z0>0`, `K<0` branch.

The local matched-rank displacement route was left barred. Instead RL325 derives an exact full-`D0/H` ownership telescope across the entire linear crossing-to-canonical interval, couples it to the frozen least-root mechanical word, and obtains an all-depth Beatty contraction.

This yields the certified carry bound

`n<=33068504812`.

A second global theorem controls the zero phases at both outer ends of the parent bridge:

`(L-h)+z<=floor(d rho/ell)`.

At the maximal surviving carry this combines with the exact omitted Beatty mass to force

`rho in {60,61,62}`,
`d_j<=36`,
`L<=62`,

with at most one zero in the entire canonical-to-boundary suffix. For `rho=60,61` that suffix is all ones.

The main remaining obligation is to consume these bounded endgames and turn the resulting contraction into a support-uniform elimination/descent for every lower carry.

`PARENT_DIFFICULTY_DELTA = EASIER`.

## Promoted theorem-grade results

See `RL325_PROOF_LEDGER.md`. In brief:

- exact linear full-ownership telescope for normalized matched defect;
- exact normalized recurrence and all-depth unrolling;
- least-root mechanical lower bound on matched phase separation;
- Beatty/permutation contraction and omitted-mass refinement;
- exact full-row gap partition at the canonical rank;
- valid live-branch inequality `n-5/6<(X/Y)G`;
- crossing-prefix gap bound `G<2^z`;
- two-ended zero-budget theorem;
- exact rational certificate giving `n<=33068504812`;
- finite maximal-carry physical endgame.

## Correction frozen before promotion

A scratch-only step incorrectly transferred RL319's root-aligned theorem `G<2^35` into the live late-row-root branch and attempted to infer `n<=G`.

That transfer is rejected and was never authoritative. The correction is recorded in `RL325_CORRECTION_AND_DEMOTION_LEDGER.md`. No promoted RL325 theorem relies on it.

## Binding barriers

RL324.6 remains binding. The exact local family with arbitrarily large next displacement and tiny positive defect forbids local rank-by-rank displacement propagation as a closing method.

RL325 also preserves the no-cyclic-wrap discipline: its telescope is linear only.

## Verification

`verification/verify_rl325_global_ownership.py` checks with exact rational arithmetic:

- the 280-term lower enclosure for `log 2`;
- the frozen `lambda<1+2^-40` consumer bounds;
- the initial Beatty carry cap;
- the `rho=60` and `rho=63` decisive omitted-mass thresholds;
- the `rho<=59` carry threshold;
- the exact floor values at `rho=59,...,63`;
- the arithmetic consequences for the maximal-carry endgame.

The verifier is a certificate consumer for the finite constants. The analytic telescope, least-root mechanical derivation, and ownership identities are proved in the ledger, not established by finite search.

The clean connector reconstruction and manifest checks are recorded in `RL325_FRESH_RECONSTRUCTION_VERIFICATION.md`.

## Scope

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.
External `2^71` least-state floor remains conditional.

Gate A: OPEN.
Gate B: OPEN.
R1 Parent Bridge: OPEN.
`g=1`: separate.
Global positive non-trivial-cycle exclusion: OPEN.

## GLOBAL PROOF ROADMAP STATUS

`CURRENT_STAGE = R1`

`CURRENT_STAGE_NAME = Parent Bridge`

`CURRENT_STAGE_PROGRESS = 60%`

`THIS_SESSION_ADVANCE = Exact global ownership telescope, Beatty carry contraction to n<=33068504812, two-ended zero budget, and <=62-phase maximal-carry endgame.`

`CURRENT_STAGE_BLOCKER = Consume the maximal-carry endgames and extend the global mechanism to all remaining lower carries, or obtain an equivalent support-independent parent closure.`

`ADVANCE_CRITERION = Close the full remaining K<0 parent bridge at required scope before moving to R2.`

`REMAINING_STAGES = R2 g=2 Closure; R3 g>1 Lift; R4 Scale Closure; R5 g=1 Closure; R6 Gate Reconciliation; R7 End-to-End Proof.`

`ROADMAP_DELTA = ADVANCE`

`GLOBAL_PROOF_STATUS = OPEN`

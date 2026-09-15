# RL327 closeout — owned-bridge density and fixed-point bootstrap

Date: 2026-09-15
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `f37a2984065548440a8ae0973060f97a40a44a2b`
Successor: RL328

## Executive conclusion

RL327 does not prove Gate A, Gate B, the full R1 parent bridge, global positive non-trivial-cycle exclusion, or the Collatz conjecture.

It materially strengthens the remaining ordered `g=2`, `Z0>0`, `K<0` parent attack. Instead of treating long mechanical zero plateaux independently, RL327 enumerates and links the genuinely owned bridges between them, then converts those exact ownership restrictions into a finite-state density theorem and a residue-weighted telescope loss.

The first automaton proves

`Z<=24K+72`,

so at `rho=60` at least `5501121808` positive excess ranks occur. Residue weighting contracts the carry to

`n<=32603663706`.

A self-consistent parity-aware total-46 bootstrap then proves

`19Z<=449K+1347`,

forcing at least `5583403544` positive excess ranks and yielding the final contradiction above threshold `32596612663`. Therefore

`n<=32596612662`.

The RL326 cap improves by exactly `242678741`.

`PARENT_DIFFICULTY_DELTA = EASIER`.

## Promoted theorem-grade results

See `RL327_PROOF_LEDGER.md`. In brief:

- exact parity-aware singleton owned-bridge certificate through totals 47--98;
- exact shared-plateau state linkage, leaving 5 physical links / 4 conservative pair-type links;
- exhaustive two-positive bridge certificate, with no high-carry survivor above total 51;
- 224-state / 21,805-edge potential proof of `Z<=24K+72`;
- distinct-residue weighted telescope loss and intermediate cap `32603663706`;
- corrected threshold bootstrap including total 46, with 2,414 endpoints, 187 pair types, 9 links and `19Z<=449K+1347`;
- exact rational fixed-point contraction `n<=32596612662`.

## Correction frozen before promotion

A scratch enumerator omitted initial endpoint odd parity. Red team detected this before promotion. All affected scratch counts, including pre-repair total-46 counts, were discarded and every promoted range was rerun with explicit parity. See `RL327_CORRECTION_AND_DEMOTION_LEDGER.md`. No prior authoritative theorem is altered.

## Binding barriers

RL324's local propagation counterfamily remains binding. RL327 succeeds by adding global shared-state ownership and finite automaton structure; it does not resurrect rank-by-rank displacement propagation. The telescope remains linear only.

## Verification

`verification/verify_rl327_owned_excess_density.py` reproduces the exact singleton/two-positive counts, all 21,805 base potential edges, weighted loss, bootstrap certificate, and final cap.

`verification/red_team_rl327_owned_excess_density.py` independently cross-checks factor cells, endpoint parity/band coverage, the exhaustive two-positive shapes, every potential inequality, residue power sums, and both cap derivations.

Both pass from the clean reconstructed handover.

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

`CURRENT_STAGE_PROGRESS = 72%`

`THIS_SESSION_ADVANCE = Exact owned-bridge automata, Z<=24K+72 density, residue-weighted telescope, and total-46 fixed-point bootstrap contracting n to 32596612662.`

`CURRENT_STAGE_BLOCKER = Iterate or uniformize the threshold-dependent owned-bridge bootstrap to eliminate the remaining high-carry interval, or obtain an equivalent genuinely owned contradiction/descent.`

`ADVANCE_CRITERION = Close the full remaining K<0 parent bridge at required scope before moving to R2.`

`REMAINING_STAGES = R2 g=2 Closure; R3 g>1 Lift; R4 Scale Closure; R5 g=1 Closure; R6 Gate Reconciliation; R7 End-to-End Proof.`

`ROADMAP_DELTA = ADVANCE`

`GLOBAL_PROOF_STATUS = OPEN`

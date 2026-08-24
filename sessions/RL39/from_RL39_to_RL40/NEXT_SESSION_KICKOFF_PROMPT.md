# RL36 next-session kickoff

Continue the Collatz R# / RL research from the attached `Collatz_Rsharp_RL35_to_RL36_Handover_2026-08-21.zip` as a skeptical research mathematician.

Start by reading:

1. `START_HERE.md`;
2. `RL35_PROOF_STATUS_AND_NEXT_ATTACK.md`;
3. `RL31_TO_RL35_PROGRESS_LEDGER.md`;
4. `RL35_FRESH_VERIFIER_RERUN.txt`;
5. `rl31_to_rl35_additions/RL35_ANCHOR_RUN_CHARGING_AND_CF_GATE.md`.

Then rerun at least the RL34 and RL35 verifiers. Any verifier failure is a stop-and-repair event.

Treat the nested `inherited/Collatz_Rsharp_RL30_to_RL31_Handover_2026-08-21.zip` as the authoritative audited pre-RL31 dependency tree. In particular, preserve the RL30 correction that `(G,H)=(12,4)` is only an exceptional order-3 subbranch and that radius-3 closure is not yet a global RL closure.

## Primary objective — export RL35 to an actually open branch

Do **not** spend the session merely optimizing the coefficient `0.2457975378...` unless an improvement provably crosses a meaningful continued-fraction or branch threshold.

Preferred target: the order-2 / `g=2` simultaneous-factor branch.

Use the ingredients already present in the inherited RL21-RL29 work:

- exact integer-gap synchronization;
- common `v2(G)` prefix and first-divergence blow-up;
- the proper-factor decompositions of the simultaneous `X-Y` and `X+Y` equations;
- RL27 adjacent-block ownership / synchronization experiments;
- RL29 transport information;
- RL35's itemization, deterministic-successor maps, and finite slack charging.

Seek a theorem of the following general shape:

> repeated resynchronization or repeated ownership of near-extremal blocks forces a **linear** arithmetic charge: either positive-density high correction, a positive-density valuation excess, or a proper-factor quotient cost that is visible simultaneously in both factor equations.

The desired output is a branch-closing lemma, a strictly stronger quotient/divisibility obstruction, or a precise no-go showing which missing invariant is necessary.

Avoid the already-refuted local heuristic that a long synchronized future run must have a proportionally long immediately preceding unsynchronized excursion; 2-adic gap dynamics permits deep future synchronization after short excursions.

## Secondary target — strict excursion branch

If the order-2 route stalls for a structural reason, transfer the RL35 method to the strict-excursion/no-balanced-return branch. Define canonical induced items using block imbalance or low-state height, identify the true zero-slack extremizers, compute their successor maps, and prove that long extremal runs incur a finite positive charge.

A fixed global gain is valuable only if it feeds a real branch threshold or a new sparse bridge.

## Tertiary target — sparse algebraic bridge

Only pursue order-3/higher cyclotomic algebra if the new relation is genuinely sparse in the rotation phase or yields a proper-factor resultant. Dense exact factor recovery is not enough.

## Evidence discipline

Maintain four statuses explicitly:

- analytic theorem;
- theorem conditional on a named external result/input;
- exact finite certificate;
- computational/session evidence only.

Keep `R>=2^71` explicitly external. Keep Laurent-Mignotte-Nesterenko dependencies explicit. Do not call RL closed unless every branch in the audited global DAG is discharged.

## End-of-session deliverable

Freeze any new theorem with an exact verifier, update the proof/branch ledger, state exactly what changed in the distance-to-RL picture, and prepare an RL36->RL37 handover if the session becomes long.

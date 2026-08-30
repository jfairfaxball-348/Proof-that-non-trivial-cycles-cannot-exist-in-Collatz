# RL185 red-team report

Date: 2026-08-30

Result: **PASS with no closure claim**.

## Checks

1. **Incoming authority / verification economy — PASS.** Current `main` was `5562e24...`; the frozen RL184 package records fast-verifier, manifest, and red-team PASS. Only RL181/RL183 targeted dependencies were expanded.
2. **Mechanical late-bit count — PASS.** The bound is the exact floor-difference identity for `B=A-L`, not a frequency heuristic.
3. **Height propagation — PASS.** It uses only `h_(i+1)<=h_i+c_i-1` and clean common-mechanical p-pair transitions.
4. **Coverage multiplicity — PASS.** A physical defect can be assigned at most one corridor start per chronological offset, and impossible low offsets are removed by the height envelope.
5. **Flow lower bound — PASS.** For unequal endpoint heights with maximum H, the dyadic potential gap is at least `2^-H`; inherited `rho>1/2` gives strict `|f|>2^-(H+1)`.
6. **Carry handling — PASS.** Carry is excluded from the ordinary corridor charging. It is added separately and is positive `>1/2`.
7. **Global signed total — PASS.** The exact inherited flow sum is used, and a rational enclosure independently checks `0<F2<1/2`.
8. **Threshold sign count — PASS.** The p-rank height cycle has equal up/down crossings at each threshold. The carry can affect only the positive/downward side, so the ordinary positive floor is reduced by one.
9. **Variation versus excursion — PASS.** The report explicitly refuses to convert total variation into K-corridor escape without a sign-reversal/late-defect capacity theorem.
10. **Physical versus formal — PASS.** All charged starts and selected defects come from RL184 physical corridors; no necessary automaton state is promoted as realized.
11. **No false closure — PASS.** High type, preferred branch, Gate A/B, non-trivial cycle exclusion, and Collatz all remain open.

## Main remaining risk / route barrier

The lower bound is minimized by late, high defects. A future session must control the distribution of first-defect offsets; simply increasing the raw nonzero count will not bridge the K-corridor scale.

# RL326 red-team report

Date: 2026-09-15
Status: PASS FOR CLOSEOUT CANDIDATE

## RT1 — complete factor coverage

**PASS.** The length-49 rational-mechanical word has exactly 50 factors. The verifier constructs every factor by partitioning the full intercept range at every discontinuity; it does not sample trajectory supports.

## RT2 — physical ownership of the state band

**PASS.** Every state used in the block contradiction is an actual odd state `P_i` in the genuine late row. The lower bound is global minimality; the upper bound follows only at a rank with `q_t=0` from the genuine odd-to-odd segment equation.

## RT3 — residue uniqueness and reconstruction

**PASS.** `3^49` exceeds the entire certified state band. Each factor therefore has at most one candidate endpoint. All backward divisions and oddness checks are exact integers.

## RT4 — density combinatorics

**PASS.** A forbidden 49-gap block is exactly a forbidden run of 50 zero `q` values. Counting zero runs gives `K>=ceil((T-48)/50)` with no uncovered endpoints.

## RT5 — coefficient-loss direction

**PASS.** Positive `q_t` halves or further reduces its ideal coefficient. Since `c_t>1/(2lambda)>1/(2Lambda)`, the loss is strictly greater than `1/(12Lambda)`. All replacements are in the upper-bound direction required for exclusion.

## RT6 — all-rho coverage

**PASS.** `rho<=59` is covered by the independent RL325 carry inequality. From `rho=60` onward, the omitted-mass decrease dominates the worst one-rank relaxation of the rounded density bound, so the new right side is strictly decreasing.

## RT7 — scope and barred routes

**PASS.** The result is conditional where the inherited `2^71<=m<2^75` window is conditional. It uses no root-aligned `G` cap, no cyclic wrap, no affine ownership relabelling, and no local displacement propagation.

## RT8 — stage discipline

**PASS.** The carry contracts to `n<=32839291403`, but the parent branch and R1 remain open.

Overall red-team result: **GREEN**.

# RL328 route viability barrier — singleton density cannot close R1 alone

Date: 2026-09-15
Status: VERIFIED METHOD BARRIER

Within the RL327 conservative owned-bridge graph and its current residue-min linear telescope consumer, continuing to certify shorter singleton bridges cannot by itself eliminate the full high-carry interval.

The graph admits every positive-excess run of length at least three and zero plateaux through length 49. Therefore it contains a repeatable `N(49)->N(49)` cycle with `Z=49`, `K=3`. Any fixed-boundary potential `Z<=R K+B` on this unchanged graph must have `R>=49/3` asymptotically, regardless of singleton ownership.

At `rho=60`, even granting the optimistic ratio `Z/K=49/3` with zero boundary gives `K>=7934310304`; the inherited exact residue-min telescope yields `n<32393913987.784203...`, still far above the high-carry floor `20390252058`.

Solving the current consumer for the first `K` that reaches that floor gives `K>=112933933538`, about 82.117% of ranks, equivalently `Z/K<0.217775`.

Sending every positive `q_t` height to infinity can at most double its loss in the same linear coefficient family. Even granting that impossible best case uniformly still requires `K>=64392480586`, about 46.821% of ranks, equivalently `Z/K<1.135779`, again far below `49/3`.

Consequence: shorter-singleton descent is frozen as a legitimate local mechanism but loses automatic priority. A successor must constrain long positive runs / force owned descent, or replace the current linear consumer with a genuinely stronger global relation.

This is a method barrier, not a claim that no stronger Collatz theorem exists. It does not change RL327's promoted cap `n<=32596612662`.

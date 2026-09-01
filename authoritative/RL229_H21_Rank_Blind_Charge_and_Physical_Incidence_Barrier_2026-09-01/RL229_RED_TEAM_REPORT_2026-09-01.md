# RL229 red-team report

Date: 2026-09-01.

## Checks

1. Recomputed the dangerous H21 interval `D` and verified both the excluded e=16 rank and
   the currently live e=4 rank lie inside it.
2. Recomputed `a=906,638,145`, `b=1,930,218,180`, and
   `2b-a=2,953,798,215>0`.
3. Re-derived the two-level optimum `x=y=1/(3*2^22)` from the active budget and `x>=y`.
4. Checked the rank-blind theorem as a duplicate-half-space statement: removing any proper
   subset of identical rank rows cannot relax the intersection.
5. Kept necessary-rank nonemptiness strictly distinct from physical realization.
6. Confirmed RL184's incidence theorem forces nonzero defects, not H21-height-21 defects.
7. Confirmed RL187 joint H21 families and RL190 `D` are necessary classifications, not
   existence populations.
8. Confirmed no e=4 transition-44 deletion or new rank deletion is introduced.
9. Confirmed no improvement of the `>443` flow floor is claimed.
10. Confirmed no branch, Gate A, Gate B or global conclusion is promoted.

## Verdict

**PASS — RL229 meets success class C.**

The current binding H21 charge interface is exactly rank-blind, so isolated H21 rank deletion
is not a route to improved physical charge. The precise missing invariant is rank-sensitive
physical incidence/multiplicity, family-wide dangerous-H21 exclusion, or an owned-macro bypass.

# RL127 — canonical `L=11` ownership and the `L>=12` frontier

## Outcome and classification

RL127 excludes the complete remaining `L=11`, `7<=Z<=33` strip and advances the inherited primitive ordinary frontier:

> Every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L>=12`.

This is a mixed analytic/exact-finite result.  It is not a Gate A or Gate B closure, a global nontrivial-cycle exclusion, or a proof of Collatz.

## Exact capacity and ownership certificate

For each `L=11` run profile, the verifier applies only the inherited valid floors: one-fibre odd/zero bounds, the `6(t-1)` CRT boundary floor, and nonempty depth-sensitive CRT fibre bounds.  Empty depth fibres are explicitly ignored, implementing the RL126 repair.

The recursive generator tries every positive run composition; it prunes a branch only after a partial zero-window or nonempty CRT fibre count exceeds its exact width-capacity limit.  Counts are monotone as further runs are appended, so the retained leaves are exactly the capacity-feasible profiles.

The completed certificate records:

- capacity-feasible transition-root profiles: `68,792,297`;
- periodic profiles: `1`;
- canonical primitive run-pair representatives: `8,081,463`;
- orbit-weight total: `68,792,296`, exactly equal to the primitive transition-root profile total;
- cyclic roots tested for `D|Q`: `255,028,004`;
- divisibility hits: `0`.

The orbit-weight identity is load-bearing: each primitive profile orbit has one lexicographically least pair rotation, and its weight is the run count.  The verifier aborts unless summed weights equal the primitive capacity-profile count.  Every binary cyclic root of that representative is then tested, so no root is lost to the run-profile compression.

RL125 had already analytically excluded `Z>=34`; hence the certificate covers every `L=11` candidate.  Its zero-hit result proves the stated `L>=12` corollary within the inherited ordinary physical-ownership framework.

## Corrections and red teams

RL126's empty-fibre correction remains in force.  RL20 ownership, RL79 scaling, RL81 physical-state ownership, primitivity/periodicity separation, Raw/Farey scope, and finite-certificate scope are preserved.  No quotient representative is called a physical cycle, and a divisibility hit would only be a necessary-condition event.

## RL128 kickoff

For `L=12`, first derive an analytic high-`Z` tail cut using the inherited `H` floor and width ceiling, then build a corrected constrained profile generator only for the finite residual strip.

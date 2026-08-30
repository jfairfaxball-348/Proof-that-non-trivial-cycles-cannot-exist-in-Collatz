# RL185 target — signed defect drift and phase-weighted corridor capacity

Continue from the surviving high branch `(v,H,J,d)=(37,0,23,-1)` and RL184's forced nonzero-defect incidence.

## Primary target

Convert the certified floor of at least `251,879,363` distinct physical nonzero-defect phases into a **signed corrected-flow / phase-capacity obstruction**.

The preferred route is to couple at least two of:

- RL184's `10,075,174,499` clean 40-edge corridors;
- the distinct nonzero-defect floor `251,879,363`;
- the exact signed identity
  `q_i(2^G_i-1)=rho_i 2^-M D`;
- the three-step zero-intercept rigidity and reduced `270` affine-map vocabulary;
- the repeated-map floor `37,315,462`;
- the global one-state overlap at `4m/3`, with every late rank after R strictly above `4m/3`;
- RL181's K corridor and exact drift
  `K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`;
- RL182/RL183 ternary ownership and parity/divisibility sensors;
- shallow width occupancy and affine-tail lower bounds.

Seek a theorem that forces too much positive or negative corrected-flow mass, too many sign changes, or too much phase-localized width for the inherited K corridor / shallow quotas to absorb.

## Preferred consumers

1. A lower bound on one sign of the forced nonzero-defect population after partitioning by early/late mechanical phase.
2. A compensation theorem: many positive defects force enough negative defects (or conversely) that the total variation of K exceeds its certified corridor.
3. A signed repeated-map theorem: once a physical affine map, mechanical word, and phase compartment are fixed, repeated nonzero intercepts cannot all be absorbed without violating width or K drift.
4. A ternary/parity refinement that converts the nonzero-incidence floor into a minimum population of odd versus nonzero-even defects and then into signed flow.

## Do not spend the session on

- longer unconstrained local template enumeration;
- arbitrary ternary residue or lattice capacity;
- a broad BFS with no signed global consumer;
- generic rank/monotone-chain/inverse-rank routes blocked by RL168-RL171;
- blind higher odd-modulus lifting;
- RL173's demoted `3^-G` physical interpretation;
- treating necessary templates/maps as physically realized;
- recursive historical verification absent a current failure, unresolved dependency, or contradiction.

## Scope discipline

All RL180-RL184 refined floors, m bounds, pair-gap, suffix/corridor ownership, map multiplicities, defect-incidence and phase-location statements remain internal to `(37,0,23,-1)`. Excluding that branch would require proof-state reconciliation before selecting the next branch and would not by itself prove global Collatz closure.

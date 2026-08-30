# RL183 target — shallow ternary suffix capacity and successor correlation

Continue from the surviving high branch `(v,H,J,d)=(37,0,23,-1)` and RL182's exact shallow-numerator ownership theorem.

## Primary target

Convert RL182's **25/26/27-step ternary ownership** into a physical count or width obstruction.

Every ordinary shallow p-shift numerator is now uniquely determined by its short chronological transition suffix modulo a power of three. Seek an independent theorem that bounds the number of physically admissible suffixes which can own shallow edges, or correlates those suffixes strongly enough with chronological successor incidence to conflict with the inherited shallow populations/width.

Principal certified inputs:

- `2^k_i U_(i+1)=3U_i+2^G_i-1`;
- `C_i (mod 3^n)` is exactly determined by the preceding n chronological `(k,G)` suffix;
- ownership depths:
  - `h<=1`: 25,
  - `h<=2`: 26,
  - `h<=3`: 26,
  - `h<=4`: 27;
- `3|C_i` iff `G_(i-1)` is even;
- 25 zero predecessor defects cannot feed an ordinary `h<=1` edge, and 27 cannot feed an ordinary `h<=4` edge;
- ordinary shallow p-shift edge floors:
  `10,075,174,577`, `25,683,594,699`, `32,081,399,275`, `35,000,224,335`;
- fixed-defect repetition floors:
  `3,358,391,526`, `5,136,718,940`, `4,583,057,040`, `3,888,913,815`;
- universal p-window q-mass `>10,711,830,952` and affine tail `>3,570,610,317`;
- strengthened normalized-width occupancy
  `>25m/512, >33m/256, >167m/1024, >23m/128`;
- refined internal high-branch state band
  `26,385,000,000,000,000,000,000 < m < 28,084,000,000,000,000,000,000`;
- RL180 delayed positive-support requirements and all inherited correction/scope locks.

Preferred consumers:

1. a finite-state or analytic upper bound on **physically admissible** 25/26/27-step suffixes ending at a shallow p-shift edge;
2. a lower bound on chronological overlap between shallow-owning suffixes and their successors/predecessors strong enough to activate the ternary reset rule repeatedly;
3. a repeated-suffix incompatibility theorem using the fact that a fixed suffix uniquely owns the small physical numerator;
4. a phase-location/affine-tail correlation that further restricts which suffixes can own the required width.

A successful result should cap the possible shallow count or width below the certified quota, or otherwise exclude the surviving high type.

## Do not spend the session on

- counting all formal ternary residues or all arbitrary `(k,G)` strings as though they were physical;
- a broad local phase BFS without a global shallow-incidence consumer;
- generic dyadic/ternary lattice capacity;
- rank-only, monotone-chain, universal permutation, or inverse-rank routes blocked by RL168-RL171;
- blind higher odd-modulus lifting;
- RL173's demoted `3^-G` physical interpretation;
- treating necessary automaton states as physically realized;
- recursive historical verification absent a live failure, unresolved dependency, or contradiction.

## Scope discipline

All RL180-RL182 floors, refined m bounds, suffix ownership depths, and width statements remain internal to the surviving `(37,0,23,-1)` high branch. Excluding that branch would require proof-state reconciliation before selecting the next branch and would not by itself prove global Collatz closure.

# RL181 certified facts and proof ledger

## New proved analytic mathematics

- **RL181.1 — carry-completed normalized pair-gap chain.** With periodic extension and `x_i=y_i/2^h_i`, each noncarry p-shift pair satisfies `K_i=rho_i(x_(i+p)-x_i)`; the unique carry pair satisfies `K_t=rho_t(2m-x_t)`. The full-period drift remains `K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`, with `K_0=2^37`, `K_L=lambda K_0`, and `m=sum_i K_i/rho_i` in p-shift order.
- **RL181.2 charging theorem.** If `N^-=sum max(-q_i(2^G_i-1),0)`, then `N^-<=exp(s+Delta)W`; hence all K-prefixes are uniformly trapped by the resulting two-sided flow budget.
- **RL181.3 shallow adjacency theorem.** A shallow set of size `N_k` on the directed p-shift cycle owns at least `2N_k-L` shallow-shallow directed edges.
- **RL181.4 reciprocal-weight width theorem.** Any `E` p-shift sources satisfy `sum 1/omega_r > exp(-Delta)(2^(E/L)-1)/(2^(1/L)-1)` after minimizing over residue positions.

## Analytic results with exact rational / finite certificates

- Uniform physical pair-gap potential corridor:
  `128,081,997,553 < K_i < 146,795,909,391` for every `0<=i<=L`.
- Every normalized p-shift gap is positive and lies strictly between `128,081,997,553` and `293,591,818,782`.
- Shallow-shallow p-shift edge floors:
  - `h<=1`: `10,075,174,578`;
  - `h<=2`: `25,683,594,700`;
  - `h<=3`: `32,081,399,276`;
  - `h<=4`: `35,000,224,336`.
- At least `10,075,174,577` noncarry shallow gaps have normalized denominator dividing `2`; at least `35,000,224,335` have denominator dividing `16`.
- Some ordered `h<=1` endpoint-height type occurs on at least `2,518,793,645` noncarry gaps; some ordered `h<=4` type occurs on at least `1,400,008,974` noncarry gaps.
- Mandatory normalized-width occupancy:
  - `h<=1`: `>11m/256`;
  - `h<=2`: `>15m/128`;
  - `h<=3`: `>5m/32`;
  - `h<=4`: `>11m/64`.

## Exact verifier output

`verification/verify_rl181_pair_gap_occupancy.py`: PASS.

## New method barrier

- Denominator-only shallow-gap packing is not closure-grade without a further physical numerator ownership/divisibility or phase-location correlation.

## Inherited correction / scope state

- Corrected `G_i=S_(p+i)-S_p-S_i` remains authoritative.
- The physical functional remains `sum q_i(2^G_i-1)`; RL173's `3^-G` quantity remains auxiliary only.
- Necessary automata remain one-way filters, not physical existence certificates.
- RL175's sparse ownership resultant is not revived as a generic independent gap obstruction.
- RL168-RL171 rank/chain/inverse-rank barriers remain in force.
- RL180's `m` band and shallow populations remain internal only to the surviving high branch.

## Global status

The sole zero-height `v=37` negative-sign high type survives. The preferred `h_p=0` branch, the positive-height branch, Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.

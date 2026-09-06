# RL268 certified facts

Date: 2026-09-06

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

Promoted:
- complete four-order classification for determinant-one `[2,1,1,1]` after anchoring the length-two component;
- exact four-component support cut `U4=floor((3A+1)/4)`;
- shorter determinant-window parameter `r=q` or `L-q` and uniform `r<=floor(A/3)`;
- normalized full-`D` edge bound `0<|E|<=5*3^(7+r)*2^(U4-r)`;
- non-bracketing exclusion for `A>=430`;
- exact reuse of the audited RL238 LMN dependency with a safe bracketing cutoff `A<=195421` and no reduced-denominator multiplicity because `gcd(A,L)=1`;
- exact 35-row Stern-Brocot upper-neighbour certificate, with only six size survivors `(5,3;3,2),(8,5;3,2),(27,17;19,12),(46,29;19,12),(65,41;19,12),(149,94;84,53)`;
- complete determinant-pair cover through `A<=429`: 34,931 determinant pairs, 967 size survivors, maximum size-survivor `A=174`;
- `[2,1,1,1]` certificate over all four cyclic orders: 179,403,060 gap configurations, 9,510,691 structural candidates, maximum structural `A=174`, zero full-`D` hits;
- independent brute-force `A<=18` red team: 21,596 raw positive-domain `|kappa|=1` `[2,1,1,1]` instances, exact 10,798/10,798 orientation symmetry, zero full-`D` hits, zero determinant mismatches and zero edge-identity mismatches after legal zero-flow cutting;
- 1,608 proper-factor-only small-range numerator-difference instances are explicitly not promoted as full-`D` hits;
- permanent negative-domain sentinel remains `D=-139,Q=18904` and is outside scope.

Together with RL266/RL267, determinant-one leaves `[3,2]`, `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]` are closed.

Still open in determinant one: `[1,1,1,1,1]`.

Radius 5 remains open. After determinant one is complete, `|kappa|=3` and `|kappa|=5` remain active research sectors unless a later argument eliminates them uniformly. Gate A, Gate B and global exclusion remain open.

# RL268 certified facts

Date: 2026-09-06

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

Promoted:
- exact four-case cyclic sign/order classification for determinant-one `[2,1,1,1]`;
- new four-component support cut `U4=floor((3A+1)/4)`;
- exact shorter-window count `r=q` or `L-q` tied to `h=min(m,A-m)`;
- mixed full-`D` edge bound `0<|E|<=5*3^(7+r)*2^(U4-r)`;
- non-bracketing exclusion for `A>=375`;
- audited-RL238 LMN bracketing cutoff `A<=163052`;
- exact 35-row Stern-Brocot bracketing traversal through that cutoff;
- six bracketing coarse size survivors, all with `A<=149`;
- exact complete mixed-bound determinant cover: 967 pairs, maximum `A=174`;
- 179,403,060 positive four-gap configurations;
- 9,510,691 structural binary candidates, maximum structural `A=174`;
- per-order structural counts 2,405,606 / 2,410,327 / 2,405,606 / 2,289,152;
- zero full-`D` hits in every cyclic sign/order case;
- independent `A<=18` earth-mover replay: 21,596 raw positive-domain `[2,1,1,1]`, `|kappa|=1` instances, split 10,798 / 10,798 by orientation, with zero full-`D` hits;
- zero determinant and edge-identity mismatches in the independent small-range replay;
- nonprimitive candidates are not filtered;
- the permanent negative-domain sentinel remains `D=-139,Q=18904` and is outside scope.

Together with RL266 and RL267, determinant-one leaves now closed are:
- `[3,2]`;
- `[3,1,1]`;
- `[2,2,1]`;
- `[2,1,1,1]`.

Still open in determinant one:
- `[1,1,1,1,1]`.

Radius 5 remains open. After determinant one, `|kappa|=3` and `|kappa|=5` remain to be treated unless eliminated by a new uniform argument. Gate A, Gate B, and global exclusion remain open.

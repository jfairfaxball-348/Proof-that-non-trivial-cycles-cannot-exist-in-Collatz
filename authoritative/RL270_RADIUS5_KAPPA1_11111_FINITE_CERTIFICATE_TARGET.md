# RL270 — Radius-5 `[1,1,1,1,1]` finite certificate

Date prepared: 2026-09-06
Status: **PREPARED, NOT STARTED**

Incoming classification: `RADIUS5_KAPPA1_11111_REDUCED_TO_FINITE_CERTIFICATE`.

## Inherited exact reduction

RL269 has already proved the infinite reduction. Do not redo it unless auditing a specific dependency.

Inherited finite domain:
- exactly 2,234 determinant-one tuples `(A,L;m,q)`;
- maximum `A=690`;
- all satisfy positive `D=2^A-3^L>1` and `qA-mL=1`;
- exact zero-flow-cut five-edge identity and full-`D` divisibility remain the theorem test;
- the naive five-positive-gap expansion would be 618,391,058,390 configurations and is not an acceptable default enumeration strategy.

## Primary target

Close the remaining determinant-one topology `[1,1,1,1,1]` by a complete finite certificate over the RL269 pair list.

Priority compression:
1. exploit `x_i-x_(i+m)=g_i-g_(i-1)` around the single `m`-cycle;
2. exploit that singleton components give ten boundary events whose signs/order are strongly constrained by binary reconstruction;
3. translate physical adjacency using `qA-mL=1` / the determinant-window relation;
4. enumerate the resulting compressed exact state space, not all raw five-gap compositions;
5. test the entire positive `D`, never a proper factor;
6. preserve both `kappa` orientations by exact source/target reversal or explicit replay;
7. do not filter by primitivity.

Required red teams:
- independent direct-word replay on a tractable small range;
- cyclic-cut / wrap convention;
- numerator-index convention;
- proper-factor versus full-`D` separation;
- negative-`D` sentinel;
- nonprimitive candidates;
- proof that every cyclic singleton sign/order case is covered.

Preferred outcome: `RADIUS5_KAPPA1_11111_CLOSED`.

Only if that closure is obtained does the complete determinant-one `|kappa|=1` sector close. At that point a successor may activate the inherited `|kappa|=3` sector. Do not begin `|kappa|=3` or `5` before closure.

Frozen:
- Gate A;
- fifth retained selector;
- selector enumeration;
- general Radius-n programme.

Radius 4 remains promoted locally. Gate B, Radius 5 and global exclusion remain open.

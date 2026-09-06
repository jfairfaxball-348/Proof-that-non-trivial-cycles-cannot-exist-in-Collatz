# RL268 closeout

Date: 2026-09-06

Incoming base HEAD: `785c9eaf1db327937783cb4358fb5d263cb48110`.

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

Closed in this generation:
- determinant-one `[2,1,1,1]`.

Previously closed and inherited unchanged:
- `[3,2]` (RL266);
- `[3,1,1]` and `[2,2,1]` (RL267).

Remaining determinant-one leaf:
- `[1,1,1,1,1]`.

The new four-component proof does not reuse the RL267 three-component support bound. It combines a longest-zero-gap support cut with the exact determinant-window count, reduces the infinite domain to an exact 967-pair certificate with maximum `A=174`, and checks 9,510,691 structural candidates with zero full-`D` hits.

Independent `A<=18` earth-mover replay gives 21,596 raw `|kappa|=1` `[2,1,1,1]` instances, exact orientation symmetry, and zero full-`D` hits.

Successor: RL269, targeting only `[1,1,1,1,1]` first.

Important: closing `[1,1,1,1,1]` will complete the determinant-one (`|kappa|=1`) flat sector, **not automatically the entire Radius-5 theorem**. The inherited Radius-5 classification still contains `|kappa|=3` and `|kappa|=5` sectors. Those remain frozen until determinant one is complete.

Gate A, the fifth selector, selector enumeration and the general Radius-n programme remain frozen. Gate B and global exclusion remain open.

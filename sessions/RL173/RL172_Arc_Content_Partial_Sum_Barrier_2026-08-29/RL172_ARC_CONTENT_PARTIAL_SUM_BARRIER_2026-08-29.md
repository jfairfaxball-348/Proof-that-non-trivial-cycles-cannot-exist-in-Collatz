# RL172 — arc-content partial-sum barrier

An inverse-phase arc's positive ordinary affine content is exactly the
chronological partial increment of `z_j=q_jy_j`; it is not an additional
transported-height constraint.

For an ordinary arc of width `w`, exponent total `B`, and affine content `C`,
let `q'=q 2^B/3^w`. From `2^B y'=3^w y+C`,

`q'y'-qy=qC/3^w`.

Iterating `z_(i+1)-z_i=q_i/3` over that same arc gives

`q'y'-qy=(1/3)sum_(t=0)^(w-1)q_(j+t)`.

Thus `qC/3^w` is exactly the partial sum. In particular, RL163's positive
p-arc numerator adds no independent physical quantity beyond the
chronological owned `z` increments used in RL169–RL170.

This is an analytic ordinary-`+1` barrier, not a cycle construction or
exclusion. It does not claim all arc data are physically realizable.

`RL172_CERTIFICATES/verify_arc_partial_sum.py` checks the identity on 30,340
bounded cyclic ordinary arcs. The next target is a physical constraint not
reducible to a partial `z` sum.

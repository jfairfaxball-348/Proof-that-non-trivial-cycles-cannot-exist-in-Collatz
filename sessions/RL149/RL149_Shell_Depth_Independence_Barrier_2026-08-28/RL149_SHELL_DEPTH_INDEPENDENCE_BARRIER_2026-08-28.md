# RL149 — Shell/depth independence barrier

## Status

**Proved analytic method barrier** for the inherited local defect recurrence,
determinant shell, and physical prefix-squeeze resources.  No cycle branch is
excluded.

At an isolated negative phase `h_j=-1`, write predecessor height
`H=h_(j-1)>=0` and `c=b_j-b_(j-1)`.  Then

`a_(j-1)=H+c+1`, `z=2^(H+c)y_j`,
`y_(j-1)=(2^(H+c+1)y_j-1)/3`.                              (1)

Since `S_j=b_j+1`, its positive determinant shell is

`r_j=S_jL-jA=L-(jA mod L)`,                                (2)

which is independent of `H`, whereas exact entry depth is `H+c`.  The local
recurrence admits every nonnegative `H` at the same shell by selecting the
exponent in (1).  Further, substituting (1) into the inherited physical prefix
quantity gives

`q_(j-1)y_(j-1)=rho_(j-1)(2^(c+1)y_j-2^(-H))/3`.            (3)

Thus the existing prefix squeeze cancels the height apart from a bounded
`2^(-H)` correction.  These resources cannot yield a shell-to-depth injection,
monotonicity, or exact-depth population lower bound.

This does not say a new global ownership or ordering theorem cannot do so.  It
does not promote a mechanically admissible local transition to a cycle.

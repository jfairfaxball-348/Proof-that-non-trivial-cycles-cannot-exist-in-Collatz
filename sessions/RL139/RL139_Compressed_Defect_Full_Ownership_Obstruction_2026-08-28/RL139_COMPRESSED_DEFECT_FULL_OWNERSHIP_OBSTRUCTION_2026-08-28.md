# RL139 — compressed-defect full-ownership obstruction

Let `N=gL` and consider the exact compressed no-negative defect path
`h=(0,0,1,...,1,0)`. Its exponents are `a_j=c_j+h_j-h_(j+1)`, with
`c_j=floor(A(j+1)/L)-floor(Aj/L)`.

Let `B_j=3^(N-1-j)2^(floor(Aj/L))`, `Q_c=sum B_j`, and `Q_a` be the affine
numerator of the compressed path. Directly,

`2Q_a=Q_c+B_0+B_1=Q_c+5*3^(N-2)`.

For repeated mechanical blocks, `Q_c=Q_0F_g` and
`D_g=(2^A-3^L)F_g`, where
`F_g=sum_{t=0}^{g-1}2^((g-1-t)A)3^(tL)`.

If this path were an actual cycle, `D_g|Q_a`, hence
`F_g|5*3^(N-2)`. But `F_g` is coprime to 3 and exceeds 5 for `g>1`, a
contradiction.

Thus no actual full-count cycle with `g>1` realizes this exact compressed
no-negative path. This is an analytic ordinary-owned obstruction with exact
factorization checks. It does not force a general defect path into this form,
so it excludes no multiplicity and leaves all frontiers and global gates open.

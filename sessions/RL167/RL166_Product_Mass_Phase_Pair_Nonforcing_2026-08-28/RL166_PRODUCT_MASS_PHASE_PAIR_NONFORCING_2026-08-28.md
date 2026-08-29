# RL166 — product-mass phase-pair non-forcing barrier

RL166 strengthens RL165.  The conditional product-mass lower inequality,
local nonnegative defect grammar, and absence of shallow inverse-phase pairs
can hold together.  This is an exact local-inequality compatibility result,
not a cycle construction or exclusion.

Let `R=30,000,000,000`.  Set `h=0` on an initial physical interval of length
at least `R`; rise five times only at successive available mechanical `c=2`
edges; stay at height five; make the terminal drop to `h_L=0`.  All exponents
`a=c+h-h_next` are positive.  The resulting shallow interval has exact size
`30,000,000,008`, below both

`p=65,470,613,321` and `L-p=72,057,431,991`.

It is therefore disjoint from its inverse-phase successor translate.

On the initial proper interval `h=0`, hence `q=rho>1/2`; so formal mass is
strictly greater than `R/2`.  RL134 certifies `5 theta<1` for
`theta=L Delta/log(2)`, hence `Delta<1/(5L)`.  The exact integer inequality
`5LR>6*2^71` proves

`R/2>3*2^71 Delta`.

Thus this grammar also meets the conditional lower product force used to
derive the inherited shallow population.  It does not meet or assert the
full cycle-closing affine equality, physical state ownership, or a cycle.
Accordingly it only blocks a route that combines the one-sided product mass
with local grammar to force a two-shallow-arc phase premise.

Run `python3 verify_rl166_report.py .` for the exact audit.

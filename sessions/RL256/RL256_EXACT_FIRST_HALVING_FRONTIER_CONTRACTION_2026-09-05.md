# RL256 — exact first-halving terminal contraction

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

## Incoming exact selector

RL255 leaves the unique first halving selector

`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`

with

- `q=317`;
- half-window parameter `K=7`;
- `260<=beta(P)<=354`;
- odd terminal exponent `k>=31`;
- terminal physical word shape `u=110 x 1 0^(k-3)`.

Write `tau=k-3` for the terminal zero-run length. This avoids collision with
RL254's unrelated half-window variable `t=n/2=2`.

## Seven physical q-layers

For the 33 exact length-19 window starts `s=-39,...,-7`, the seven q-sites
per window are pairwise disjoint. Their union is the following seven physical
length-33 intervals:

- `[129,161]`;
- `[278,310]`;
- `[446,478]`;
- `[595,627]`;
- `[763,795]`;
- `[912,944]`;
- `[1061,1093]`.

The cyclic complementary gap lengths are

`116,135,116,135,116,116,135`.

Because every Branch-C negative root is exactly `-1` and successive negative
roots have cyclic distance at least three, the complement contains at most

`4*ceil(116/3)+3*ceil(135/3)=291`

negative roots.

## Terminal zero mass and the k contraction

Let `R(tau)` denote the guaranteed raw P-sum on the seven-layer union produced
by the 33 exact 19-window identities and the known terminal zero block.

Exact values needed here are

- `R(28)=262`;
- `R(30)=283`;
- `R(32)=300`.

The quantity is nondecreasing with `tau`.

Since `sum_i P_i=2`, if `tau>=32` the complement has raw P-sum at most

`2-300=-298`.

All negative P-values are isolated `-1`s and all remaining values are
nonnegative, so complement sum `<=-298` requires at least `298` complement
negative roots. This contradicts the exact complement packing capacity `291`.

Hence `tau<32`. Inherited full-phase ownership gives odd `k`, so `tau=k-3`
is even. Together with `k>=31`, hence `tau>=28`, this leaves only

`tau in {28,30}`,

equivalently

`boxed: k in {31,33}`.

## k=33: tail exclusion and flank budget

For `k=33`, `tau=30` and the terminal zero block is at physical positions
`[-30,-1]`.

From the exact derivative

`P_(i+1)-P_i = u_i-u_(i+q)`,

a forced zero `u_i=0` makes `P_(i+1)<=P_i`; therefore a negative root at `i`
would force an adjacent negative root at `i+1`, impossible. Similarly,
`u_(i+q)=0` excludes a negative root at `i+1`.

Thus the terminal zero block excludes negative P-roots on two exact length-30
intervals. Their intersections with two 135-site complement gaps remove 6
and 9 usable sites respectively, reducing the exact complement packing
capacity from `291` to

`ceil(129/3)+4*ceil(116/3)+ceil(135/3)+ceil(126/3)=286`.

The 17 unknown physical flank sites are

left:  `-39,...,-32`,
right: `3,...,11`.

Their zero weights in the 33-window raw sum are respectively

left:  `1,2,3,4,5,6,7,8`,
right: `9,8,7,6,5,4,3,2,1`.

Let `E_33` be their weighted zero total. Then

`sum_U P = 283+E_33`

and the complement requires at least `281+E_33` negative roots. Hence

`281+E_33 <= 286`,

so

`boxed: E_33<=5`.

Consequences:

- every flank site of weight at least 6 is a one;
- therefore
  `u_-34 u_-33 u_-32 u_-31 = 1111`;
- and
  `u_3 u_4 u_5 u_6 = 1111`;
- if both outer triples `[-37,-35]` and `[7,9]` contained a zero, the cheapest
  possible weighted cost would be `3+3=6`, impossible.

Therefore at least one side extends by three further ones:

`boxed: k=33 forces a physical run 1^7 adjacent to the terminal structure}`.

Also the complement already requires at least `281` negative roots, giving

`boxed: k=33 => beta(P)>=281`.

## k=31: sharpened flank budget

For `k=31`, `tau=28`. The analogous tail-root exclusion reduces the seven-gap
complement capacity to `287`.

The 33-window base raw sum is `262`. If `E_31` is the weighted flank excess,
the complement needs at least `260+E_31` negative roots. Hence

`260+E_31<=287`,

so

`boxed: E_31<=27`.

The 19 unknown flank weights are

`1,2,...,10,9,8,...,1`.

The ten cheapest weights sum to `30>27`, so at most nine of the 19 unknown
flank sites can be zero; at least ten are ones.

## Scope

These are analytic necessary conditions for the exact first halving selector.

They do **not** eliminate the selector, close Gate A, close Gate B, or invoke
Radius 4. The physical `1^7` block must not be promoted to a canonical rank
event without correct absolute full-phase indexing.

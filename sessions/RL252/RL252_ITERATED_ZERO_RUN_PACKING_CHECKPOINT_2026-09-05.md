# RL252 — iterated zero-run packing checkpoint

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**
Scope: Branch C, `beta(P)=6`
Proof status: exact local contraction at the first RL250 frontier; no Gate closure

## Inherited first frontier

RL250 leaves the first unexcluded arithmetic scale

`(a,ell,z,q,r)=(783,494,289,317,200)`

with canonical word `u=110 x 1 0^t`, `t=k-3`, and `31<=k<=59`. Hence `28<=t<=56`.

Every `q=317` window contains at least `D_q=q-r-1=116` zeros, and `783=2*317+149`.

## Exact endpoint form of the inherited zero-run propagation lemma

For an ordinary zero run

`u_s ... u_{s+L-1}=0^L`,  `L>=10`,

the RL249 proof gives `P_{s+8}=0` and then, for
`i=s+8,...,s+L-2`, forces `u_{i+q}=0`. Therefore the forced shifted
zero block is exactly

`[s+q+8, s+q+L-2]`

(modulo `a`), of length `L-9`.

This is only an exact endpoint unpacking of the already-promoted RL249
zero-run propagation argument; it does not alter its hypotheses.

## Fivefold propagation of the terminal run

At the first frontier the terminal run is

`B_0=[783-t,782]`, length `t`.

Iterating the endpoint formula gives, whenever the previous block has
length at least 10,

`s_j=(783-t+325j) mod 783`,
`|B_j|=t-9j`.

For `j=5` (available for `t>=46`),

`s_5=(783-t+5*325) mod 783=59-t`,
`|B_5|=t-45`,

and its endpoint is

`(59-t)+(t-45)-1=13`.

Thus

`B_5=[59-t,13]`.

## Packing contradiction for t>=51

For `51<=t<=56`, `B_5` starts at an index from 8 down to 3, so it is
disjoint from both the fixed prefix zero at index 2 in `110` and the
terminal block `B_0`.

The cyclic arc from the terminal block through the prefix to index 13
has length at most `t+14<=70`, so a 149-site gap may be chosen to
contain all of:

- the `t` terminal zeros in `B_0`;
- the fixed prefix zero at index 2;
- the `t-45` zeros in `B_5`.

Its complement consists of two disjoint 317-windows. Each contains at
least 116 zeros, so the total zero count obeys

`289 >= 2*116 + t + 1 + (t-45) = 2t+188`.

Hence `2t<=101`, so integer `t<=50`. Therefore all `t>=51` are
excluded.

## Promoted contraction

At `(783,494,289,317,200)`:

- `t<=50`;
- `k=t+3<=53`;
- the canonical range contracts from `31<=k<=59` to **`31<=k<=53`**;
- with `m=z-k+2=291-k`, one has **`m>=238`**.

The packing threshold is sharp for this exact mechanism:
`t=50` yields lower bound 288, while `t=51` yields 290>289.

## Boundary

This checkpoint does **not** close Gate A or Gate B, invoke Radius 4,
activate Radius 5, exclude all Branch-C candidates, or revive any
demoted q-identification / quadratic zero-desert / q-ordered B=13/14
formula.

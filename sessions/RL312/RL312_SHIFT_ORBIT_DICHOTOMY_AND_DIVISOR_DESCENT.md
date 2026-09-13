# RL312 — balanced shift-orbit dichotomy and divisor-aligned descent

Date: 2026-09-13
Status: ANALYTIC + EXACT FINITE REGRESSION CHECK
Session: RL312

## 0. Scope

This note records the final RL312 theorem. It is a purely cyclic-combinatorial consequence of an exact balanced self-rotation and therefore applies in particular to the owned balanced return extracted by RL311.

It does **not** prove Gate A, Gate B, or global non-trivial-cycle exclusion.

The theorem concerns the canonical zero-sum balanced flow. It does **not** identify its L1 mass with the optimally normalized cyclic transport radius; RL312's earlier normalization repair remains binding.

## 1. Setup

Let `w=(w_i)_(i mod A)` be a binary cyclic word of length `A` and total weight

`L=sum_i w_i`.

Let `1<=s<A` be a balanced shift, meaning

`p=sL/A`

is an integer. Put

`W_i(s)=sum_(t=0)^(s-1) w_(i+t)`

and define the canonical balanced flow

`G_i=p-W_i(s)`.

Then

`sum_i G_i=Ap-sL=0`.

Set

`d=gcd(A,s)`, `n=A/d`, `t=s/d`.

Because `gcd(t,n)=1`, addition by `s` partitions the `A` phase positions into exactly `d` shift-orbits, each of length `n`.

## 2. Orbitwise zero-sum theorem

Fix one shift-orbit `O`.

As the start point runs once around `O`, every physical word position is covered by exactly `t=s/d` of the length-`s` cyclic windows. Therefore

`sum_(i in O) W_i(s)=tL`.

But

`n p=(A/d)(sL/A)=sL/d=tL`.

Hence

`boxed: sum_(i in O) G_i=0`

for every shift-orbit separately.

This is stronger than the global identity `sum_i G_i=0`.

## 3. Active-orbit alternative

Call a shift-orbit active if `G_i` is not identically zero on that orbit.

Since the `G_i` are integers and each orbit has total zero, every active orbit contains at least one positive and one negative value. Consequently its canonical L1 contribution is at least `2`.

Therefore, if all `d` shift-orbits are active,

`boxed: sum_i |G_i| >= 2d`.

Again, this is a statement about the canonical zero-sum flow, not automatically the optimally normalized transport distance.

## 4. Inactive orbit forces an exact balanced block partition

Suppose some shift-orbit `O` is inactive, so

`W_i(s)=p`

for every `i in O`.

Choose `r in O` and cut the cyclic word into `n=A/d` consecutive blocks of length `d` beginning at

`r, r+d, r+2d, ..., r+(n-1)d`.

Let their weights be

`b_0,...,b_(n-1)`.

Since `s=td`, every length-`s` window beginning at one of these block boundaries is a cyclic sum of `t` consecutive block weights.

The shift-orbit `O` visits all block boundaries in the order `k -> k+t mod n`, because `gcd(t,n)=1`. Inactivity therefore says every cyclic `t`-window sum of the sequence `(b_k)` is equal.

Subtract two consecutive such equalities:

`b_(k+t)=b_k`

for every `k` modulo `n`.

Because `gcd(t,n)=1`, this forces

`b_0=b_1=...=b_(n-1)`.

Their total is `L`, so each block has exact weight

`Ld/A`.

Thus:

> **RL312 shift-orbit dichotomy.** For every balanced shift `s`, with `d=gcd(A,s)`, either
>
> 1. every one of the `d` shift-orbits is active and the canonical zero-sum flow satisfies `sum |G_i|>=2d`; or
> 2. after a genuine cyclic rotation, the word decomposes into `A/d` consecutive length-`d` blocks, every one having exactly `Ld/A` ones.

No Collatz ownership assumption is needed for this combinatorial dichotomy.

## 5. Specialization to the RL311 balanced return

RL311 supplies a balanced owned shift

`s=ma`, `p=m ell`

inside a primitive positive full-`D` cycle, where

`A=ga`, `L=g ell`, `1<=m<g`.

Put

`c=gcd(g,m)`.

Then

`d=gcd(A,s)=a c`,

and in the inactive-orbit alternative every divisor-aligned block has exact counts

`(length, ones)=(ca,c ell)`.

Hence the RL311 balanced return satisfies the exact dichotomy

`boxed: all ac shift-orbits active with canonical mass >=2ac`

or

`boxed: there is a genuine full-D-owned balanced segment of counts (ca,c ell)`.

If `c<m`, the second alternative is a **strict balanced-return descent** from gap `m` to gap `c`.

In particular, if `gcd(g,m)=1`, then either all `a` shift-orbits are active or a genuine owned reduced-block balanced segment `(a,ell)` exists after rotation.

The descended endpoints are genuine rotations of the same full cycle and therefore retain global full-`D` ownership. No local-denominator ownership is asserted.

The RL311 near-endpoint ratio bound for the originally selected pair is **not automatically inherited** by the descended pair; successor work must not assume it.

## 6. Relation to the earlier RL312 results

RL312 already proved:

1. exact owned balanced Radius 2 is impossible, with the zero-skew/optimal-normalization correction made explicit;
2. a full-`D` owned balanced flow cannot be supported on only one shift-orbit, by exact row factorization.

The present theorem is different. It applies before any support-count classification and gives a divisor-aligned descent whenever even one shift-orbit is inactive.

It therefore reframes the surviving balanced-return branch as:

- a fully active canonical flow at the gcd scale; or
- a shorter divisor-aligned balanced owned segment.

This is the correct all-scale frontier for the successor session.

## 7. Regression check

`verify_rl312_shift_orbit_dichotomy.py` exhaustively checks all balanced binary word/shift instances through length `A<=13`.

It verifies:

- orbitwise zero sums;
- the `>=2d` canonical-mass bound when all orbits are active;
- exact equal-weight `d`-block decomposition from every inactive orbit.

The finite check is regression evidence only; the proof above is analytic.

## 8. Classification

`PARENT_DIFFICULTY_DELTA = EASIER`

Reason: the selected RL311 balanced pair is no longer merely an arbitrary equal-level return. It either descends to a strictly shorter divisor-aligned owned balance (unless the gcd is already the terminal divisor), or its canonical defect is forced to occupy every shift-orbit. This is an exhaustive all-scale contraction and does not introduce a fixed-radius grammar.

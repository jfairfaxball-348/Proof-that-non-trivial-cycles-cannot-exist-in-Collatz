# RL196 — global p-shift seam and exact zero-edge placement

Date: 2026-08-31. Incoming authority: RL195 at `a6d0c0b0821723b0d8338f4ffab83b841e79c038`.

All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`. This note does not construct or exclude a nontrivial cycle.

## Frozen definitions

Let `A=217976794617`, `L=137528045312`, `B=A-L=80448749305`, `R=L-B=57079296007`, `p=65470613321`, `u0=103768467013`, `t=L-p=72057431991`, `r_i=iB (mod L)`, `b_i=floor(Ai/L)`, `c_i=b_(i+1)-b_i in {1,2}`, with `c_i=1` exactly for `0<=r_i<R`, and `h_(i+1)=h_i+c_i-a_i`, `a_i>=1`, `G_i=h_i-h_(i+p)`.

The exact Bezout identity is `A p-u0 L=1`, equivalently `pB=1 (mod L)`.

## Theorem 1 — global mechanical p-shift seam

For every phase `i (mod L)`, `r_(i+p)=r_i+1 (mod L)`.

Consequently the mechanical digit is p-shift invariant except at exactly two consecutive chronological phases:

- at `i=t-1=72057431990`, `c_(i+p)-c_i=+1`;
- at `i=t=72057431991`, `c_(i+p)-c_i=-1`;
- at every other `i`, `c_(i+p)=c_i`.

Proof. The rank partition defining c changes under `r -> r+1 mod L` only at `r=R-1` and `r=L-1`. Since `I(r)=pr mod L`, exact arithmetic gives `I(R-1)=t-1` and `I(L-1)=t`. The signs follow from crossing `1->2` at `R-1` and `2->1` at the wrap.

Equivalently, `b_(i+p)-b_i=u0` except at `i=t`, where it equals `u0+1`. Taking a first difference gives the two-phase digit seam.

## Theorem 2 — defect transport and common-prefix edge copy

For every phase, `G_(i+1)-G_i = c_i-c_(i+p)+a_(i+p)-a_i`. Hence away from the two seam phases, `G_(i+1)-G_i=a_(i+p)-a_i`.

The frozen interface gives `G_0=G_1=...=G_23=0`. Since phases `0,...,22` are off the seam, for every `0<=i<=22`: `(h_(i+p),h_(i+p+1))=(h_i,h_(i+1))`; `a_(i+p)=a_i`; and any zero-zero edge at `i->i+1` has an exact p-shifted zero-zero copy.

## Corollary — an owned p-shifted zero-edge pair exists

The canonical normalization has `h_0=0`. Since `c_0=1`, `a_0>=1`, and heights are nonnegative, the recurrence forces `a_0=1` and `h_1=0`. Using `G_0=G_1=0` gives `h_p=h_(p+1)=0`. Thus both `0 -> 1` and `p -> p+1` are chronological zero-zero edges. Their source ranks are exactly `0` and `1`, because `r_p=pB=1 (mod L)`.

This promotes one explicit p-shift-compatible physical zero-edge placement. It does not promote an H21 terminal, H21 budget unit, or second p-shift pair.

## Theorem 3 — sharp placement barrier for the RL195 bulk floors

Let `Z_base={r: r mod 5 in {0,2}}` on `Z/LZ`, then replace rank 2 by rank 1: `Z=(Z_base union {1}) minus {2}`.

Because `B` is divisible by 5 and `L mod 5=2`, exact residue counting gives `|Z|=55011218125`, greater than `N0>=43742681439`; the number of chronological B-adjacencies is `38921468263`, greater than `J00>=9719139553`; and the only rank adjacency `r,r+1` contained in Z is the anchored pair `0,1`.

Since p-shift adjacency is rank adjacency, this relaxation meets both bulk floors and retains the mandatory anchor while having no second p-shift pair. It is not a height word and not a physical counterexample. Its sole role is a method barrier: N0, J00 and the anchor cannot release H21 without a genuinely additional physical constraint.

## H21 status and scope

H21 remains core `[23369453298,41775866136]` minus 14 inherited deletions, canonical floor 67, and binding `{33,34,35}` budget/ownership obligations. No multiplicity map from the anchored pair to those owned objects is proved here.

Newly proved: exact global two-phase mechanical seam; exact defect transport specialization; exact first-23-edge p-shift copy; one explicit p-shifted zero-edge pair; exact bulk-count-plus-anchor placement barrier.

Not proved: a second p-shifted zero pair; H21 ownership or budget release; either atom's realization/exclusion; sole-branch, Gate A/Gate B, nontrivial-cycle or global Collatz closure.

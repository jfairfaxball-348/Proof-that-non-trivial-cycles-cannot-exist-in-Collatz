# RL290 scratch freeze — preserved derivations, regression notes, and open leads

Date frozen: 2026-09-09
Status: SCRATCH / SUPPORTING MATERIAL. This file is intentionally broader than the promoted report.

This file preserves the main exploratory derivations from RL290 so the next audit session can recover the route without relying on conversation history.

## A. Seam normal form derivation

After synchronized first departure from `(101)^infinity`:

`q=n-s`,
`R_x=U_x/2^s`,
`R_y=U_y/2^s`,
`X=R_x+2^q`,
`Y=R_y+2^q`.

RL289 gives

`3^d X-Y=2^q K`.

Define for `q>=2`

`C=(Y-3^(d-1)X)/2`,
`B=3^(d-1)X-2^(q-1)`.

Then

`B-C=[3^d X-Y-2^q]/2`
`    =2^(q-1)(K-1)`.

At balanced `d=1` this is

`B-C=2^(q-1)J`.

At the three forced post-departure `01` roots, `C=-3` in every phase. The corresponding `B` values are:

- `(d,J)=(2,-6)`: `B=-11`;
- `(2,-39)`: `B=-77`;
- `(2,-3)`: `B=-5`.

The neutral seed prefix changes neither `q` nor `(B,C)`.

## B. Exact B,C transition table

With `P=2^(q-1)`:

`00`:
`C'=C-(3^(d-1)-1)P`
`B'=B+(2*3^(d-1)-1)P`

`11`:
`C'=3C`
`B'=3B+P`

`01`:
`C'=3C-3^d P`
`B'=3B+(2*3^d+1)P`

`10`:
`C'=C+P`
`B'=B-P`

All have `P'=2P`.

Private regression against the reconstructed RL289 depth-16 canonical tree:
- RL289 canonical edges: 39,165;
- post-departure transition checks: 39,118;
- recurrence failures: 0;
- oddness failures for B,C at q>=2: 0;
- `B-C=2^(q-1)(K-1)` failures: 0.

This was discovery/regression support; the promoted formulas are analytic.

## C. Positive boundary loop masking family

At `J=3`, pair columns `11,00` return to `J=3` with zero height and act as

`(B,C,P)->(3B+3P,3C,4P)`.

Starting from the globally reached seam state

`(d,J,H)=(1,3,3)`,
`P=128`,
`B=295`,
`C=-89`,

insert this loop `N` times and then follow the common suffix

`11,11,01,11,10`.

For every `N>=0` the physical endpoint is

`(d,J,H)=(1,12,5)`.

Writing `R` for the count of postdeparture boundary `11` columns and normalizing `I=C/3^R`, the exact family obtained in scratch work was

`I_N=-801-(2560/9)(4/3)^N`

and

`nu_2(I_N+801)=9+2N`.

Checked for `N=0,...,80` with exact arithmetic and canonical replay.

Interpretation: even after dividing the obvious power-of-three boundary phase, free positive boundary loops can push the next paid seam contribution arbitrarily far out 2-adically.

## D. Loop erasure and its failure to fix history

Zero-area chronological loop erasure is valid because all edge costs are nonnegative and only d=1 starts cost zero.

But exact physical mergers remain.

One-step merger family:

`K_d=(3^d-1)/2`,
`J_d=(3^d-2^(d+1)+1)/2`,
even `d>=2`.

At this state, `00` and `11` have identical physical children.

Concrete fixed-seed instance:

`x=0001` reaches `(2,1,3)`;
both `00010` and `00011` reach `(2,3,4)`.

Frozen seam before the choice:

`(B,C,P)=(1,-23,8)`.

After `00`:

`(B,C,P)=(41,-39,16)`.

After `11`:

`(B,C,P)=(11,-69,16)`.

The physical invariant `B-C=80` agrees; individual seam coordinates differ by common translation `-30`.

Acyclic equal-area diamond:

from `(d,J,H)=(2,3,1)`,

- `01` -> `(1,2,3)`;
- `110` -> `(1,2,3)`.

Frozen full paired words:

route A:
`x=00100001`
`y=01000100`

route B:
`x=001000110`
`y=010001100`

seam endpoints:

A: `(q,P,B,C)=(8,128,205,-51)`
B: `(q,P,B,C)=(9,256,423,-89)`.

For `t=C/P`:

`t_B+1/2=(3/2)(t_A+1/2)`.

This is the cleanest preserved witness that loop reduction alone cannot make seam history canonical.

## E. Bellman threat definition

Physical-state future threat:

`Bcal(s)=sup_sigma [nu_2(J_end)-Delta H_sigma]`

over legal future segments ending at a positive even balanced checkpoint.

Equivalent fixed-segment affine form:

`Bcal(d,J)=sup_sigma [nu_2(c_sigma J+b_sigma)-L_sigma-Delta H_sigma]`

because

`2^L J_end=c_sigma J+b_sigma`,
`c_sigma` odd.

Bellman equation:

`Bcal(s)=max(current checkpoint hazard, max_(s->s') [Bcal(s')-(d(s)-1)])`.

A dual potential `Phi` satisfying edge increments bounded by area and dominating endpoint valuation must dominate `Bcal`.

Gate A is equivalent to

`Bcal(1,-13)<=0`.

## F. Minimal-height terminal launchpad family

For odd `k>=3`, odd `q>=1`:

`J0=1+2^q(2^k-1)`,

`Jin=(2^(q+2)(2^k-1)-2)/3`.

Then

`3(Jin+4)=2(2J0+3)`,

so `01` is a genuine one-zero excursion of exact height one, followed by `q` boundary zeros to `2^k`.

Shell condition:

`nu_3(J0)=1 <=> q != k+2 (mod 6)`.

Every survivor has:

`nu_2(Jin)=1`.

Affine ray:

`Jin(k,q+2)=4Jin(k,q)+2`.

Useful small instances:

- `k=3,q=1`: `Jin=18`, `J0=15`, terminal `8`;
- `k=7,q=1`: `Jin=338`, `J0=255`, terminal `128`;
- `k=13,q=1`: `Jin=21842`, `J0=16383`, terminal `8192`;
- `k=25,q=1`: `Jin=89478482`, terminal `33554432`.

For `q=1`, the complete x-word is `010`.

## G. Stripped-unit hazard

For positive even `J`:

`t=nu_2(3J+2)`,
`u=(3J+2)/2^t`.

If `t>=3`,

`J --01 0^(t-2)--> u+1`

with exact added height one.

Thus

`nested(J)=nu_2(u+1)`

is the valuation of a specific cost-one future checkpoint.

With `J=2n`:

`3n+1=2^(t-1)u`.

So the same operation is RL284's labelled accelerated odd Collatz step on `n`, with exact removal label `t-1`.

Inverse ray for a desired successor `M=u+1`:

`J_t(M)=(2^t(M-1)-2)/3`,
`J_(t+2)(M)=4J_t(M)+2`.

## H. Fixed-seed shadow action of stripping

At balanced endpoint:

`J=3a-b+1`.

Under the stripping suffix:

`a'=(3a+2)/2^t`,
`b'=(3b+1)/2^t`.

Then

`3a'-b'+1=u+1`.

Inverse:

`a=(2^t a'-2)/3`,
`b=(2^t b'-1)/3`.

Open lead: this is the cleanest exact bridge from RL289's ballot-selected root to RL284's labelled accelerated ray.

## I. Positive checkpoint Bellman kernel

Macro-edge construction:

even checkpoint
-> forced excursion launch
-> first return
-> arbitrary retained odd-boundary motion
-> complementary even exit.

Cost = excursion height, always >=1.

Exact height-one kernel:

If `J==6 mod 8`:
`Gamma_1(J)={3(J+2)/4}`.

If `J==2 mod 8`:
`n0=(3J+2)/8`,
`Gamma_1(J)={E(C^s(n0)):s>=0}`.

Here `C` and `E` are exactly RL283's retained boundary map and complementary even exit.

Thus RL283's

`Beta(n)=sup_s nu_2(E(C^s(n)))`

is the one-generation valuation projection of the cost-one Bellman kernel.

## J. Genuine extremal chain showing recursive threat

Preserved exact chain from the RL282 H<=22 certified state space:

`(2514,15) -> (5378,16) -> (21842,17) -> (8192,18)`,

each edge cost one.

Macro x-words:

- `2514 -> 5378`: `0111110101`;
- `5378 -> 21842`: `01101011110110111`;
- `21842 -> 8192`: `010`.

At `21842`:
- `nu_2(J)=1`;
- `3J+2=8*8191`;
- stripped successor `8192`;
- therefore `V(21842)>=12`.

At `5378`:
- stripped nested depth is only `1`;
- after the mandatory `01` excursion, `n0=2017`;
- exhaustive one-generation boundary hazard `Beta(2017)=5`;
- nevertheless one exit is `21842`, whose future threat contains `2^13`;
- therefore `V(5378)>=11`.

This is the cleanest witness that one-generation Beta is not the full Bellman threat.

## K. Nested valuation jump witness

Globally reachable checkpoint:

`J=1074`.

Nested hazard:

`t=nu_2(3J+2)=3`,
`u=403`,
`nu_2(u+1)=2`.

Legal cost-one macro:

`1074 --011101--> 1364`.

At `1364`:

`nu_2(3J+2)=1`,
stripped odd unit `2047`,
`nu_2(2048)=11`.

So this nested coordinate jumps from 2 to 11 at cost one.

## L. Finite evidence to preserve but not promote

On the exact RL282 H<=22 checkpoint set, 146,341 positive even checkpoints were tested against

`nested(J)<=H-2`.

Observed:
- violations: 0;
- equality only at `(2,3)` and `(8,3)`.

A separate ordinary fixed-length canonical-tree regression through depth 33 also found no violation.

This is not promoted.

Reasons not to make it the next principal route:
- the coordinate can jump by nine bits across a cost-one macro;
- it is one Bellman successor selector, not an inductive reserve;
- older finite shifted-valuation programmes already warned against finite closure.

## M. Open leads frozen, not authorized as successor work

1. Study the positive-even Bellman operator by excursion height `h=1,2,...`.
2. Seek a fixed-seed Bellman subsolution or backward danger-set contraction.
3. Use the synchronized labelled accelerated map on ballot shadow endpoints.
4. Study minimum historical area required to enter a state with `V(J)>=k`.
5. Investigate whether the exact height-one kernel admits a contraction only after fixed-seed ancestry is imposed.
6. Reassess whether older RL47/RL48 ordered-rank and RL279/RL282 terminal-backward objects can be interpreted as dual relaxations of the new Bellman operator.
7. Preserve all seam formulas as bridge identities, but do not revert to chosen-history seam charges without defeating the merger/diamond barriers.

The user explicitly requested a broad programme audit next. These are therefore frozen open leads only.

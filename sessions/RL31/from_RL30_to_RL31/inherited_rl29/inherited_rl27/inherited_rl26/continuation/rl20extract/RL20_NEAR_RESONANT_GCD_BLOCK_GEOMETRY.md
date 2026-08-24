# RL20 — near-resonant gcd-block imbalance is one-sided and controls phase height

Date: 2026-08-20

## Status

**ANALYTIC**, with one small **EXACT FINITE CERTIFICATE conditional on the inherited external input** `R#>=2^71`.

This does not prove RL.  It adds the one-sided least-state information that the RL20 block-coboundary note identified as missing from the raw proper-factor identity.

## 1. Setup

Let a hypothetical primitive positive cycle be rotated to its least phase `R#`.  Write

`A=g a`, `L=g ell`, `g=gcd(A,L)>1`, `gcd(a,ell)=1`,

`X=2^a`, `Y=3^ell`, `z=X/Y`,

so

`lambda=2^A/3^L=z^g>1`.

At the canonical block cuts `j a`, let

`K_j=P_(j a)`

be the number of ones in the first `j a` full-parity positions, and define

`E_j=K_j-j ell`,

with `E_0=E_g=0`.

Let `x_j` be the actual phase state at the block cut `j a`.

Put

`alpha=log_3(2)`,

`delta=alpha A-L=log_3(lambda)>0`.

## 2. RL20-G1 — least-state suffix domination bounds every block imbalance

The suffix from phase `x_j` back to the least state has length `(g-j)a` and weight `L-K_j`.  RL-L54 gives

`L-K_j < alpha (g-j)a`.

Since

`alpha a = ell + delta/g`,

this rearranges exactly to

`E_j > -(g-j) delta/g`.                                  (R20G.1)

Hence whenever

`lambda<3`,

we have `delta<1`, so for every proper block cut

`E_j>=0`.                                                  (R20G.2)

In particular this holds throughout the RL19/RL20 near-resonant branch

`lambda<16/15`.

Thus the canonical gcd-block imbalance walk is not an arbitrary zero-sum walk.  At the least-state rotation it is a **nonnegative excursion from `0` back to `0`**.

This is the extra one-sided hypothesis absent from the raw RL-L55/coboundary identity.

## 3. RL20-G2 — exact block-cut height sandwich

At cut `j a`, define the usual prefix weight

`q_j=2^(j a)/3^(K_j)=z^j/3^(E_j)`.

The prefix affine equation from `R#` to `x_j` gives

`q_j x_j = R# + B_j/3^(K_j)`.

For `j>0`, the prefix contains the root odd bit, so `B_j>0`; therefore

`q_j x_j > R#`.                                           (R20G.3)

The complementary suffix equation back to the minimum gives

`q_j x_j <= lambda R#`.                                   (R20G.4)

Consequently

`R# < z^j x_j / 3^(E_j) <= lambda R#`,                    (R20G.5)

or equivalently

`3^(E_j) R#/z^j < x_j <= 3^(E_j) lambda R#/z^j`.          (R20G.6)

So the integer imbalance `E_j` is an actual phase-height address: up to the narrow global factor `lambda`, a block-cut phase lives at height `3^(E_j) R#`.

A coarse rotation-independent version is

`3^(E_j) R#/lambda < x_j < 3^(E_j) lambda R#`             (R20G.7)

for every proper block cut.

## 4. Near resonance creates disjoint height bands

Assume now

`lambda<16/15`.

By (R20G.2), `E_j` is a nonnegative integer.

### Balanced cut

If

`E_j=0`,

then (R20G.6) gives

`R# < x_j < (16/15)R#`.                                   (R20G.8)

So every balanced proper gcd-block cut produces a distinct phase in a very narrow interval immediately above the least state. Moreover this phase is necessarily **odd**. Indeed `(16/15)R#<2R#`; if `x_j` were even, the next full-parity phase would be `x_j/2<R#`, contradicting leastness of `R#`. Thus a balanced cut gives a second odd cycle rotation in the near-minimum strip.

### Positive imbalance

If

`E_j>=1`,

then (R20G.7) gives

`x_j > 3R#/lambda > (45/16)R#`.                           (R20G.9)

More generally

`E_j>=h  =>  x_j > (15/16) 3^h R#`.                       (R20G.10)

Hence no canonical gcd-block phase lies in the large multiplicative gap

`[(16/15)R#, (45/16)R#]`.                                 (R20G.11)

At block cuts the near-resonant orbit has a discrete two-scale geometry:

- balance level `E=0` means **near-minimum**;
- the first positive imbalance level already means **above `2.8125 R#`**;
- higher imbalance levels force geometric height growth by powers of `3`.

This is genuine orbit information, not a restatement of the block polynomial congruence.

## 5. The coboundary becomes a monotone narrow-strip lift

The RL20 coboundary note used normalized states

`y_j=3^(-E_j)x_j`

and proved

`3^(-E_(j+1)) Q(B_j)=X y_(j+1)-Y y_j`.

Define

`H_j=z^j y_j=q_j x_j`.

Then

`H_(j+1)-H_j = z^j Q(B_j)/Y >=0`,                         (R20G.12)

with strict inequality for every nonempty block.

Moreover

`H_0=R#`, `H_g=lambda R#`,

and (R20G.3)-(R20G.4) place every proper `H_j` in the same narrow global strip

`R# < H_j <= lambda R#`.                                  (R20G.13)

Thus the canonical block coboundary is best viewed as a monotone lift through a strip of total width `(lambda-1)R#`, while the *actual* phase heights are obtained by multiplying back by the discrete factors `3^(E_j)/z^j`.

This is the useful non-tautological content supplied by least-state ownership.

## 6. Balanced cuts cannot occur in the old short prefix window

If `E_j=0`, then the block-cut prefix has

`m=j a`, `p=j ell`,

and

`1 < 2^m/3^p = z^j < lambda <16/15`.

RL-L54's exact rescue bound therefore applies.

Conditional on the inherited external floor

`R#>=2^71`,

the verifier checks exactly that no pair `(m,p)` with

`m<195`, `1<2^m/3^p<16/15`

has a rescue bound reaching `2^71`.  The first such pair is

`(m,p)=(195,123)`.

Therefore every balanced proper gcd-block cut in the near-resonant external-floor branch satisfies

`j a >=195`.                                                (R20G.14)

This finite threshold is mostly superseded numerically by the stronger RL20 continued-fraction gate: conditional on the same external floor,

`ell=L/g >=49,547,666,544`.

Since `a/ell= A/L > log_2 3 >19/12`, this gives

`a >=78,450,472,029`.                                      (R20G.15)

So the canonical reduced blocks are themselves enormous.

## 7. Strategic consequence

The raw canonical block polynomial remains a telescoping closure identity; RL20 has not revived bare factor descent.

What is new is the geometric information available at its block cuts:

1. near resonance forces `E_j>=0` at every proper cut;
2. `E_j=0` creates a second near-minimum phase;
3. `E_j>0` forces the phase immediately into a separated height band near `3^(E_j)R#`;
4. the normalized coboundary lift `H_j` is monotone inside the narrow strip `(R#,lambda R#]`.

A viable next factor/rotation argument should therefore branch on

- **balanced return:** exploit two `D`-divisible rotations whose physical states both lie below `(16/15)R#`;
- **strict excursion:** exploit the forced geometric height jump `x_j>(45/16)R#` at every proper canonical block cut.

Verifier: `verify_rl20_near_gcd_block_geometry.py`.

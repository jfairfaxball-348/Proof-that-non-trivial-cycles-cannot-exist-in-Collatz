# RL254 — general 38-window mass escalation

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

## Promoted result

Every simultaneous surviving Branch-C object satisfies

`beta(P) >= 260`.

Moreover, with

`H = 19z - 7a`, `n = 19B - 7q`,

the stronger alternative holds:

- if `H` and `n` are both even, `beta(P) >= 260`;
- otherwise, `beta(P) >= 355`.

This strictly strengthens the RL253 exploratory candidate `beta(P)>=118`.

## 1. General-beta bookkeeping

The inherited determinant flow is

`P_i = r - W_i(q)`, `a r - q ell = 2`.

Summing all cyclic q-window counts gives

`sum_i W_i(q) = q ell`,

hence

`sum_i P_i = a r - q ell = 2`.

With the inherited convention

`beta(P) = sum_i max(-P_i,0)`,

the total positive P-mass is therefore exactly

`sum_i max(P_i,0) = beta(P) + 2`.

No beta=6 assumption is used.

## 2. The 65/41 corridor is general on the current Branch-C survivor

RL248 already promotes, for every simultaneous Branch-C survivor,

- `beta(P)>=6`;
- `z=a-ell>=46`;
- `19/12 < a/ell < 8/5`;
- `1 < 2^a/3^ell`;
- `(2^a/3^ell)^2 < 16/15`.

From `z>=46` and `a/ell<8/5`, one gets `ell>=77`.

Repeating the RL249 rational comparison without the beta=6 restriction: if
`a/ell>65/41`, integrality gives `41a-65ell>=1`, hence

`a-log_2(3) ell >= ell(65/41-log_2(3))+1/41`.

At `ell=77` the right side already exceeds
`(1/2)log_2(16/15)`, contradicting the scale window. Therefore every current
Branch-C survivor satisfies

`a/ell <= 65/41`,

equivalently

`7/19 < z/a <= 24/65`.

Thus, setting

`H=19z-7a`, `n=19B-7q`,

one has

`0 < H <= a/65`.

## 3. General 38-window identity

From `qz-aB=2`,

`Hq = na + 38`,
`HB = nz + 14`.

For every cyclic start `s`, summing the H q-windows beginning at

`s, s+q, ..., s+(H-1)q`

gives exactly n full word-cycles plus one length-38 cyclic window. Therefore

`Z_38(s) = 14 + sum_{j=0}^{H-1} P_{s+jq}`.

This is valid for arbitrary beta on the retained Branch-C domain.

## 4. Nineteen disjoint 38-window segments: beta >= 256

Use coordinates in which the guaranteed terminal zeros are

`u_{-28}=...=u_{-1}=0`

and the canonical prefix is

`u_0 u_1 u_2 = 110`.

Consider the 19 length-38 windows starting at

`-42,-41,...,-24`.

Their guaranteed zero counts are

`24,25,26,27,28,28,28,29,29,29,29,29,29,29,29,28,27,26,25`.

Subtracting the identity baseline 14, the guaranteed P-segment sums total

`258`.

These 19 q-orbit P-segments are pairwise disjoint. Indeed, if starts differ by
`1<=d<=18` and two segments meet, then for some nonzero `m` with `|m|<H`,

`m q ≡ d (mod a)`.

Combining this with `Hq-na=38` gives

`a | (38m-Hd)`.

But

`|38m-Hd| <= 38(H-1)+18H = 56H-38 < a`,

so `38m=Hd`. Since `d<19`, this forces `19|H`. The same cross-multiplication
with `mq-ca=d` gives `38c=nd`, hence `19|n`. From

`H=19z-7a`, `n=19B-7q`

one obtains `19|a` and `19|q`, contradicting `gcd(a,q)|2`, itself inherited
from `qz-aB=2`.

Therefore total positive P-mass is at least 258, so

`beta(P)+2 >= 258`,
`beta(P) >= 256`.

## 5. Bootstrap to the 149/94 corridor

RL248 promotes the zero-budget inequality

`beta(P) <= z-k+4`

and the simultaneous-survivor floor `k>=31`. Hence the new `beta(P)>=256`
gives

`z >= 256+31-4 = 283`.

Together with `a/ell<=65/41`, this implies `ell>=484`.

If `a/ell>149/94`, integrality gives `94a-149ell>=1`, so

`a-log_2(3) ell >= ell(149/94-log_2(3))+1/94`.

Already at `ell=484` this exceeds `(1/2)log_2(16/15)`. Thus

`a/ell <= 149/94`,
`z/a <= 55/149`,
`H/a <= 2/149`.

## 6. Parity split and the uniform beta >= 260 theorem

### 6a. Halving case: H and n both even

Write

`K=H/2`, `t=n/2`.

Then

`Kq = ta + 19`,
`KB = tz + 7`,

so the exact half-window identity is

`Z_19(s) = 7 + sum_{j=0}^{K-1} P_{s+jq}`.

Since `H/a<=2/149`, one has `K<=a/149`.

Take the 33 length-19 windows with starts `-39,-38,...,-7`. Their guaranteed
zero counts, from the same terminal `0^28` and prefix zero, give total excess
over the baseline 7 equal to

`262`.

Their K-site q-orbit segments are pairwise disjoint. If two starts differ by
`1<=d<=32`, an overlap gives `mq-ca=d` with `0<|m|<K`; combining with
`Kq-ta=19` gives

`a | (19m-Kd)`.

The bound

`|19m-Kd| <= 19(K-1)+32K = 51K-19 < a`

forces `19m=Kd`.

If `d>=19`, then `|m|>=K`, impossible. If `d<=18`, then `19|K`; the second
cross-relation gives `19|t`, hence `19|H,n`, and therefore `19|a,q`,
again contradicting `gcd(a,q)|2`.

Thus positive P-mass is at least 262:

`beta(P) >= 260`.

### 6b. Non-halving case: H,n not both even

Use the 37 useful length-38 windows with starts `-51,-50,...,-15`. Their total
guaranteed excess over the baseline 14 is

`357`.

Any two starts differ by at most 36. If two H-site q-segments overlap, the same
determinant argument gives

`a | (38m-Hd)`,

while

`|38m-Hd| <= 38(H-1)+36H = 74H-38 < a`

because `H<=2a/149`. Hence `38m=Hd`.

For `d != 19`, this again forces `19|H,n`, impossible. For `d=19`, the equality
forces `H=2m`, and the companion cross-relation forces `n` even, contradicting
the present non-halving case.

So all 37 segments are disjoint and

`beta(P)+2 >= 357`,
`beta(P) >= 355`.

Combining the two cases proves the uniform promoted theorem

`boxed: beta(P) >= 260`.

## 7. Immediate inherited consequences

Feeding the certified floor into RL248:

- zero budget:
  `z >= beta(P)+k-4 >= 287`;
- physical companion-envelope amplification:
  `beta(E) >= 4(beta(P)-2)+H_I >= 1032`.

These are consequences of already-promoted RL248 inequalities; no Radius-4
application is made here.

## Scope

RL254 is a strict global-bridge contraction only.

- Branch-C beta below 260 is eliminated.
- In the non-halving 38-window branch, beta below 355 is eliminated.
- Gate A remains open.
- Gate B remains open.
- Radius 4 is not invoked.
- Radius 5 remains inactive.
- No global non-trivial-cycle exclusion is claimed.

All RL249/RL250 demotions remain binding. RL251's Gabriel-horn equivalence
remains frozen.

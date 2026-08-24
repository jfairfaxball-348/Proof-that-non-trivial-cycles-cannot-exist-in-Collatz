# RL38 — scaled-gap telescoping, synchronized-run elimination, and crossing charge

Date: 2026-08-21

## Status

Sections 1--7 are **ANALYTIC** in the inherited near-resonant `g=2` balanced-return branch. Section 8 contains an **EXACT FINITE local certificate** through transport area 7 (with broader sanity checks through area 15 in the verifier).

This note does **not** close RL or the full order-2 branch. Its main advance is structural: the synchronized-anchor population that remained explicit in RL36--RL37 cancels exactly after passing to the scaled physical gap. The order-2 half-return becomes a jump process supported only on maximal prefix-count excursions. In addition, a synchronized run immediately before a physical sign-changing excursion is charged linearly to that excursion's transport area, with no `log R` loss.

## 1. Setup

Retain

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`, `z=X/Y>1`,

with aligned half trajectories

`u_j=T^j(R)`, `v_j=T^j(x)`, `x=R+G`,

and prefix counts / scalings

`p_u(j)`, `p_v(j)`, `d_j=p_v(j)-p_u(j)`,

`q_u(j)=2^j/3^(p_u(j))`, `q_v(j)=2^j/3^(p_v(j))`.

At every synchronized prefix-count column `d_j=0`, put

`q_j=q_u(j)=q_v(j)`,

`Delta_j=v_j-u_j`,

and define the **scaled physical gap**

> `W_j=q_j Delta_j`.                                      (R38.1)

At the endpoints,

`W_0=G`,

`W_a=z(R-x)=-zG`.                                         (R38.2)

Thus the scaled gap must reverse sign and change magnitude by the fixed factor `z` over the half return.

## 2. Synchronized runs leave `W` exactly invariant

Suppose `[s,t]` is a synchronized run: `d_j=0` throughout and the two parity bits agree at every local column. Let its common word have length `h` and odd weight `c`. The physical gap evolves homogeneously,

`Delta_t=(3^c/2^h) Delta_s`,

while

`q_t=(2^h/3^c) q_s`.

Therefore

> **`W_t=W_s`.**                                          (R38.3)

So an arbitrarily long synchronized run, with arbitrarily many common odd anchors, contributes **zero** to the scaled-gap motion. All changes in `W` are concentrated on maximal excursions.

This is the exact replacement for trying to estimate synchronized anchors one by one.

## 3. Exact excursion jump formula

Let `E=[s,t]` be a positive maximal excursion (`d_j>0` inside). Write its two local equal-weight words as

`alpha` on the `u` trajectory and `beta` on the `v` trajectory,

with common length `h`, common weight `p`, and

`D_E=Q(alpha)-Q(beta)>0`.

The local gap map is

`Delta_t=(3^p Delta_s-D_E)/2^h`.                           (R38.4)

Since `q_t=q_s 2^h/3^p`, multiplying by `q_t` gives

> **`W_t-W_s=-q_s D_E/3^p`.**                              (R38.5)

For a negative excursion the sign is reversed:

> **`W_t-W_s=+q_s D_E/3^p`.**                              (R38.6)

Consequently the entire half-return sign reversal is the exact sum of excursion jumps,

> **`sum_E (W_t-W_s)=-(1+z)G`.**                           (R38.7)

No synchronized-run term remains.

## 4. Correction-product telescoping on synchronized runs

Let a synchronized run carry the common affine multiplier

`m=3^c/2^h`.

For either trajectory `y`, the odd correction product on the run is

`P_y=product_(odd run phases)(1+1/(3y))`

and the exact segment identity gives

`y_t=m y_s P_y`.

Because `|Delta_t|=m|Delta_s|`,

> **`P_y=(y_t/|Delta_t|)/(y_s/|Delta_s|)`.**               (R38.8)

For the pair,

> **`P_u P_v = [u_t v_t/Delta_t^2]/[u_s v_s/Delta_s^2]`.** (R38.9)

Thus the complete correction product of a synchronized run is a pure boundary ratio. It is not intrinsically proportional to the number of synchronized odd anchors.

This explains why the RL37 statewise estimate acquired a `log R` loss: it bounded individual synchronized states before using the exact affine cancellation available to the pair.

## 5. Excursion distortion product

For an excursion `E=[s,t]`, put

`m_E=3^(p_E)/2^(h_E)`

and define its positive distortion

`J_E=|Delta_t|/(m_E |Delta_s|)`.                           (R38.10)

At synchronized endpoints,

`J_E=|W_t/W_s|`.                                           (R38.11)

Since synchronized runs leave `W` unchanged, multiplying over all maximal excursions telescopes:

> **`product_E J_E = |W_a/W_0|=z`.**                       (R38.12)

Equivalently, using `lambda=z^2`,

> **`lambda = product_E J_E^2`.**                          (R38.13)

The same identity follows by multiplying (R38.9) over synchronized runs and the paired correction products over excursions; the endpoint ratio `Rx/G^2` is identical at the two half endpoints and cancels.

R38.12--R38.13 are algebraically exact. They do not by themselves bound `lambda`; their value is that the residual order-2 problem is now supported only on excursions.

## 6. Universal transport bound on a local excursion kick

Let `r=rho_E` be the transport area of a positive excursion. Put

`K(r)=((3/2)^r-1)/2`.                                     (R38.14)

The raw envelope needed below has a short direct proof. For fixed length `h` and weight `p`, adjacent `10 -> 01` moves strictly increase `Q`. Therefore among positive-excursion endpoint words,

`Q(alpha) <= Q(0^(h-p)1^p)=2^(h-p)(3^p-2^p)`,

while

`Q(beta) >= Q(1^p0^(h-p))=3^p-2^p`.

Hence

`D_E/2^h <= ((3/2)^p-1)(1-2^(p-h))`.                      (R38.14a)

For every nonempty maximal excursion,

`r=sum_(s<j<t) |d_j| >= h-1`,

so, writing `n=h-1`,

`r>=n>=p` and `h<=r+1`.                                   (R38.15)

If `d=n-p>=0` and `a=(3/2)^p`, then twice the difference between `K(n)` and the right side of (R38.14a) is

`a((3/2)^d-2)+1+(a-1)2^(-d)`,

which is `0` for `d=0`, `1/2` for `d=1`, and positive for `d>=2`. Thus

> **`D_E/2^h <= K(h-1) <= K(r)`.**                         (R38.14b)

Also `p>=1`. Hence

`D_E/3^p`
` = (D_E/2^h)(2^h/3^p)`
` <= K(r) 2^h/3`
` <= K(r) 2^(r+1)/3`
` = (3^r-2^r)/3`
` < 3^(r-1)`.                                             (R38.16)

Thus the unscaled relative kick of an area-`r` excursion is universally bounded by a power of `3` depending only on transport area.

## 7. Synchronized-anchor charge before an inward / crossing excursion

Consider a positive excursion while the incoming physical/scaled gap is positive. Let

`g=Delta_s>0`

and define its relative inward kick

`t_E = D_E/(3^p g)`.                                      (R38.17)

Then

`W_t/W_s = 1-t_E`.                                        (R38.18)

Suppose the immediately preceding synchronized run contains `c` common odd columns. During that run the physical gap is multiplied by `3^c` and divided only by powers of `2`. Therefore

`v3(g) >= c`,

hence

`g>=3^c`.                                                  (R38.19)

Combining (R38.16)--(R38.19) gives

> **`t_E < 3^(r-1-c)`.**                                  (R38.20)

This is the new no-`log R` anchor-to-transport charge.

Consequences:

1. If `r<=c`, then `t_E<1/3`: the excursion can remove less than one third of the incoming scaled gap.
2. If `t_E>=1/2`, then necessarily `r>=c+1`.
3. If the excursion changes the physical gap sign, then `t_E>1`, so necessarily

> **`r>=c+2`.**                                           (R38.21)

Thus a long synchronized common-odd run can certainly be followed by a short excursion -- the false local claim retired in RL36 is still false -- but such a short excursion is exponentially ineffective at changing the scaled gap. The mandatory sign-changing excursion must linearly pay for the synchronized odd mass immediately before it.

For a sign-changing positive excursion, (R38.4) also gives

`D_E > 3^p g`,

so (R38.16) implies

> **`g < 3^(r-1)`.**                                      (R38.22)

In particular `v3(g)<=r-2`, another form of (R38.21).

## 8. Exact local crossing floor: area at least 7

At the start of any maximal excursion the parity bits differ immediately, so the incoming integer gap is odd. For a positive excursion, a physical sign change requires an odd integer `g>=1` such that

`3^p g-D_E < 0`

and

`2^h | (3^p g-D_E)`.                                      (R38.23)

The bundled exact verifier enumerates **all canonical positive excursions of transport area at most 7** and all possible positive incoming gaps satisfying (R38.23).

It proves:

- no sign-changing integer excursion exists for `r=1,...,6`;
- at `r=7` there is exactly one canonical local crossing triple,

`alpha=000011`,

`beta =101000`,

`p=2`, `h=6`, `D_E=73`,

with

`g=1 -> Delta_t=-1`,

and distortion

`J_E=64/9`.

Therefore every genuine order-2 half return contains at least one physical sign-changing excursion and hence

> **`r_cross >= 7`.**                                     (R38.24)

Combining with (R38.21), if `c_cross` is the common odd mass of the synchronized run immediately preceding a chosen positive sign-changing excursion,

> **`r_cross >= max(7,c_cross+2)`.**                       (R38.25)

RL37's stronger global theorem `rho>=16` remains in force. R38.24 is not intended to replace it; it identifies where the compulsory physical crossing first becomes locally possible and adds the linear predecessor-run charge R38.25.

## 9. Strategic meaning and next target

RL36 ended with a packing-or-synchronized-anchor dichotomy. RL37 bounded the synchronized population statewise, but the resulting estimate retained a `K~log R` term.

R38 changes the structure:

- synchronized runs are **exactly inert** for the scaled gap;
- their paired correction products are exact boundary ratios;
- all half-return motion and all excursion distortion are carried by maximal excursions;
- a synchronized run immediately before a meaningful inward excursion cannot be long compared with that excursion's transport area;
- the mandatory crossing excursion has area at least 7, and its immediate predecessor common-odd mass is at most `r_cross-2`.

The next branch-closing target should therefore be phrased on the scaled-gap jump process, not as an independent synchronized-anchor population estimate:

> **Effective-excursion charging target.** Partition inward excursions by relative kick size `t_E`. Use (R38.20) to charge the synchronized mass before every effective inward excursion to transport area, while excursions with exponentially small `t_E` are shown incapable of supplying the total decrement `(1+z)G` unless they occur in sufficiently large number. Couple that large-number alternative to the RL35 valuation/packing budget.

A successful aggregate version would remove the `log R` term from RL37's overlap inequality and would be a genuine route to closing the `g=2` branch.


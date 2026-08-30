# RL181 — shallow pair-gap corridor and normalized width occupancy

Date: 2026-08-30

## 0. Outcome and classification

RL181 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`, with `g_p=2^37`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

The new advance is a simultaneous physical-normalized spacing theorem. RL180 supplied a global height profile, an internal state floor, and the physical pair-gap potential. RL181 couples them: every normalized p-shift gap is forced into a uniform corridor, billions of those gaps must have shallow endpoints, and the shallow gaps must occupy a positive certified fraction of the complete normalized width.

Promoted results:

1. **RL181.1 — carry-completed normalized pair-gap chain** (analytic). Extend the physical orbit periodically and put `x_i=y_i/2^h_i`. In p-shift order `i_r=pr (mod L)`, every ordinary edge satisfies
   `K_i=rho_i(x_(i+p)-x_i)`, while the unique carry edge `i=t=L-p` satisfies
   `K_t=rho_t(2m-x_t)`. Moreover the RL180 drift law holds for the full period and `K_L=lambda K_0`.
2. **RL181.2 — uniform pair-gap corridor** (analytic + exact rational interval certificate). Every `K_i`, `0<=i<=L`, obeys
   `128,081,997,553 < K_i < 146,795,909,391`.
   Hence all normalized p-shift gaps are positive and the p-shift chain runs strictly from `m=x_0` to the terminal copy `2m`. Since `1/2<rho_i<=1`, every normalized gap lies strictly between
   `128,081,997,553` and `293,591,818,782`.
3. **RL181.3 — shallow p-shift adjacency floors** (analytic combinatorics + inherited exact shallow-population certificates). The number of directed p-shift gaps whose two endpoint heights are at most `k` is at least
   - `10,075,174,578` for `k=1`,
   - `25,683,594,700` for `k=2`,
   - `32,081,399,276` for `k=3`,
   - `35,000,224,336` for `k=4`.
   At most one in each family is the carry edge. Thus at least `35,000,224,335` ordinary physical pair gaps have denominator dividing `16` in the normalized coordinate, and at least `10,075,174,577` have denominator dividing `2`. Among the `h<=1` ordinary gaps some ordered endpoint-height type occurs at least `2,518,793,645` times; among `h<=4` gaps some ordered type occurs at least `1,400,008,974` times.
4. **RL181.4 — shallow normalized-width occupancy ladder** (analytic + exact rational interval certificate). The total normalized width occupied by shallow-shallow p-shift gaps is forced to exceed
   - `11m/256` for `h<=1`,
   - `15m/128` for `h<=2`,
   - `5m/32` for `h<=3`,
   - `11m/64` for `h<=4`.
   In particular, more than `17.1875%` of the entire normalized width from `m` to `2m` is carried by at least `35,000,224,336` p-adjacent gaps with both endpoint heights at most four.

The high branch remains open. Denominator-only lattice capacity is still far too large; the next useful consumer must control the pair-state numerators, ownership, divisibility, or phase-location correlation.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `t=L-p=72057431991`.

Let

`Delta=A log 2-L log 3 >0`, `lambda=exp(Delta)`,
`s=p log 3-u log 2 >0`,
`b_i=floor(Ai/L)`, `h_i=b_i-S_i>=0`,
`q_i=2^S_i/3^i`, `rho_i=2^b_i/3^i`, and `z_i=q_i y_i`.

RL180 supplies in this high branch:

- `g_p=2^37` and `h_p=0`;
- `23,493,381,795 < W=R-Q < 28,070,867,755`;
- `2^74 < m < 3*2^73`;
- shallow population floors
  `N_1=73,801,609,945`,
  `N_2=81,605,820,006`,
  `N_3=84,804,722,294`,
  `N_4=86,264,134,824`;
- `F2=sum_i q_i(2^G_i-1)=3(lambda-1)2^37`;
- `K_i=exp(s)z_(p+i)-z_i` and the corrected physical flow convention.

All necessary automata remain one-way filters only. RL173's `3^-G` functional remains auxiliary and is not used here.

## 2. RL181.1 — full-period normalized pair-gap chain

Periodically extend the orbit by

`y_(i+L)=y_i`, `S_(i+L)=S_i+A`, `h_(i+L)=h_i`,
`q_(i+L)=lambda q_i`, `rho_(i+L)=lambda rho_i`, and `z_(i+L)=lambda z_i`.

Because `S_p=b_p=u`,

`exp(s) q_(p+i)/q_i = 2^(S_(p+i)-S_p-S_i)=2^G_i`.

Therefore the RL180 difference identity is valid over the full period:

`K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`,

with `K_0=2^37` and `K_L=lambda K_0`.

For the p-shift pair `j=(i+p) mod L`, the mechanical carry

`c_i=b_(p+i)-b_p-b_i`

is zero except at `i=t`, where it equals one. Put `x_i=y_i/2^h_i`. For every noncarry source,

`G_i=h_i-h_j`,

so

`K_i=rho_i(x_j-x_i)`.

At the carry source `t`, `j=0` and

`K_t=rho_t(2m-x_t)`.

Since `Ap=1 (mod L)`, the sources `i_r=pr (mod L)` traverse every phase exactly once. Consequently, once positivity of `K` is established, the normalized p-shift pairs form one strict chain from `x_0=m` to the terminal copy `2m`, and exactly

`m = sum_(r=0)^(L-1) K_(i_r)/rho_(i_r)`.

This is an identity for normalized coordinates of actual physical phase states. It is not an assertion that the ordinary states `y_i` themselves occur in this order.

## 3. RL181.2 — charging negative flow to mechanical loss

Write

`f_i=q_i(2^G_i-1)`.

At a noncarry source `i` with target `j=i+p (mod L)`, set `v_i=2^-h_i`. Then

`f_i=rho_i(v_j-v_i)`.

At the carry source,

`f_t=rho_t(2-v_t)>0`.

Thus every negative flow term is noncarry. If `f_i<0`, then

`-f_i=rho_i(v_i-v_j) <= rho_i(1-v_j)`.

In residue/p-shift order the source-to-target mechanical ratio is one of `exp(s)` or `exp(s+Delta)`. Hence

`rho_i <= exp(s+Delta)rho_j`.

The p-shift is a permutation, so the negative edges have distinct targets. Summing and charging each negative term to its target mechanical loss gives

`N^-:=sum_i max(-f_i,0) <= exp(s+Delta) W`.

Because `sum_i f_i=F2`, the total positive flow is

`N^+=N^-+F2 <= exp(s+Delta)W+F2`.

Every prefix of the exact K-drift is therefore trapped by

`2^37-exp(s+Delta)W/3 <= K_i <= 2^37+[exp(s+Delta)W+F2]/3`.

The bundled rational interval verifier combines this with the inherited RL180 bound `W<28,070,867,755` and certifies

`128,081,997,553 < K_i < 146,795,909,391`.

RL180's residue envelope gives `1/2<rho_i<=1` over one period. It follows that every normalized p-shift gap is positive and lies in

`128,081,997,553 < K_i/rho_i < 293,591,818,782`.

## 4. RL181.3 — shallow adjacency and dyadic pair numerators

For any subset `A` of the vertices of a directed cycle of length `L`, at most `L-|A|` edges can leave `A`; hence at least

`2|A|-L`

directed edges have both endpoints in `A`.

Apply this to the p-shift cycle and

`A_k={i:h_i<=k}`.

Substituting the four RL180 shallow floors gives the four promoted adjacency counts.

At most one shallow-shallow edge is the unique carry edge. On every ordinary noncarry edge with endpoint heights `(a,b)`, positivity of the normalized gap gives an exact integer numerator `C`:

- if `a>b`, `delta=(2^(a-b)y_j-y_i)/2^a` and the numerator is odd;
- if `a<b`, `delta=(y_j-2^(b-a)y_i)/2^b` and the numerator is odd;
- if `a=b`, `delta=(y_j-y_i)/2^a` and the numerator is positive even.

Thus the denominator divides `2^max(a,b)`. This yields the denominator-2 and denominator-16 populations stated above. Pigeonhole over the four ordered height types for `k=1`, and the 25 ordered height types for `k=4`, gives the promoted repeated-type multiplicities.

These are physical pair numerators because they are formed from actual orbit states. The result does not assert that an arbitrary dyadic gap is physically owned.

## 5. RL181.4 — mandatory shallow width

Let `omega_r=rho_(i_r)` in p-shift/residue order. RL180's exact mechanical envelope gives

`omega_r < exp(Delta) 2^(-r/L)`.

Therefore

`1/omega_r > exp(-Delta) 2^(r/L)`.

The right side increases with `r`. For any set of `E` p-shift gap sources, the smallest possible sum of these reciprocal lower bounds is attained by the first `E` residues, so

`sum_(r in S) 1/omega_r
 > exp(-Delta) [2^(E/L)-1]/[2^(1/L)-1]`.

Every selected shallow-shallow gap has width `K_(i_r)/omega_r` and RL181.2 gives `K_(i_r)>128,081,997,553`. The exact verifier evaluates the geometric lower bound with rigorous rational logarithm/exponential enclosures. Combining it with the conservative inherited ceiling `m<3*2^73` proves the occupancy ladder

`11/256, 15/128, 5/32, 11/64`

for heights one through four respectively.

This is genuinely simultaneous information: the RL180 population floors identify a large set of physical p-shift edges, the RL181 corridor gives every such edge a physical-normalized width, and the mechanical residue profile prevents all those widths from being hidden at arbitrarily favorable weights.

## 6. Barrier and next consumer

The result does not close the high branch. Even tens of billions of denominator-16 gaps fit comfortably in an interval of the inherited scale if their numerators are unconstrained. RL168-RL170 already block generic rank/chain capacity arguments, and RL181 does not revive them.

Freeze the following route limitation:

> Denominator-only shallow-gap packing, without a numerator ownership/divisibility or phase-location correlation, is not closure-grade.

RL182 should attack the now-large physical family of shallow pair numerators. The preferred next theorem would show that the numerators cannot realize the required count or the required `>11m/64` width while respecting the actual accelerated transitions, divisibility, ownership, or congruence structure.

## 7. Red-team scope

- **Physical versus normalized:** PASS. `x_i=y_i/2^h_i` is a normalized coordinate of a physical state, not itself promoted as an odd cycle state.
- **Carry:** PASS. The unique `t=L-p` edge is treated separately; the full-period K identity uses the periodic extension.
- **Negative-flow charging:** PASS. Negative terms are noncarry and are injected into distinct target mechanical-loss terms.
- **Inherited floors:** PASS. Only frozen RL180 certified facts are consumed; no external least-cycle minimum is introduced.
- **Dyadic ownership:** PASS. Denominator statements are made only for actual noncarry physical pairs; arbitrary dyadic points are not promoted to realizable states.
- **Historical barriers:** PASS. No monotone-chain, universal rank, inverse-rank, blind higher-modulus, or RL173 route is revived.
- **No false closure:** PASS. The high branch and all global gates remain open.

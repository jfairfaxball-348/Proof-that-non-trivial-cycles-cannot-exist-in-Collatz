# RL133 — physical prefix-defect restrictions at the first CF survivor

Date: 2026-08-27

## 0. Outcome and classification

RL133 advances the RL132 physical-divisibility target on the **coprime `g=1` realization** of the first reduced continued-fraction survivor

`(A,L)=(217,976,794,617,137,528,045,312)`.

It does **not** exclude that whole reduced scale, because an actual cycle may realize the same reduced pair with multiplicity `g>1`. It does not advance either the internal or externally conditional `L` frontier. Gate A, Gate B, global nontrivial-cycle exclusion, and Collatz all remain open.

New promoted mathematics:

1. **RL133.1 — least-state physical prefix squeeze** (analytic, `g=1` first-survivor branch).
2. **RL133.2 — continued-fraction prefix-sign and exact floor-lock theorem** (analytic + exact rational interval arithmetic).
3. **RL133.3 — nonnegative prefix-defect excursion and physical height bands** (analytic).
4. **RL133.4 — shallow-defect population force** (analytic consequence + exact arithmetic, conditional on inherited external `R#>=2^71`).
5. **RL133.5 — zero-defect mechanical extremal has rotation radius one and is excluded by the inherited closed radius-three engine** (analytic/combinatorial, branch-specific).

The principal strategic change is that the first survivor is no longer merely a pair of counts. In the coprime realization, an actual cycle rooted at its least odd state would have to keep **every proper accelerated prefix strictly below the global logarithmic slope**, creating a nonnegative defect path whose values control actual physical state heights.

## 1. Incoming authority

RL132 freezes:

- internally certified primitive ordinary frontier `L>=190,537`;
- conditional on inherited external `R#>=2^71`, reduced denominator and hence ordinary odd-count frontier `L>=49,547,666,544`;
- first above-side reduced CF survivor
  `(A,L)=(217,976,794,617,137,528,045,312)`;
- `gcd(A,L)=1` for this reduced pair;
- bare product/CF, single fixed-depth complete residue-prefix descent, and count-only gcd-block extensions are method barriers at this scale.

RL133 preserves the provenance of the external floor. No stronger demoted floor and no Hercher/corrigendum-dependent consequence is used.

Put

`beta=log(3)/log(2)`,

`Delta=A log(2)-L log(3)>0`,

`lambda=2^A/3^L=exp(Delta)`.

The exact verifier reconstructs the inherited rational log intervals and CF prefix and proves that this pair is the convergent immediately after

`U=103,768,467,013 / 65,470,613,321`,

with the preceding convergent

`V=10,439,860,591 / 6,586,818,670`.

It also proves rigorously that the survivor still satisfies the inherited external product inequality, so RL132's method-barrier status is retained.

## 2. Scope precision: reduced pair versus full counts

This distinction is load-bearing.

RL131 constrains the **reduced** pair

`p=A_full/g`, `q=L_full/g`, `g=gcd(A_full,L_full)`.

The first survivor is the coprime reduced pair above. RL133's prefix theorem in Sections 3–8 assumes the full cycle counts are exactly this pair, i.e. **`g=1`**.

For `g>1`, the full discrepancy is `g Delta`, and a proper prefix may have denominator above the reduced `L`. The best-approximation argument below no longer forces every proper prefix to have negative discrepancy. Therefore no `g>1` exclusion or implicit multiplicity-one theorem is claimed.

This is not a demotion of RL132. It is an explicit scope boundary on the new RL133 argument.

## 3. RL133.1 — least-state physical prefix squeeze

Assume for this section a hypothetical primitive positive ordinary cycle whose full counts equal the first survivor `(A,L)`, so `g=1`.

Rotate to its least odd state `m=R#`. Write the accelerated odd orbit

`y_0=m, y_1, ..., y_(L-1)`

with positive exponents `a_i>=1` satisfying

`3 y_i + 1 = 2^(a_i) y_(i+1)`

cyclically. Then

`sum_i a_i=A`.

For `1<=j<L`, put

`S_j=a_0+...+a_(j-1)`

and

`q_j=2^(S_j)/3^j`.

Iterating the first `j` accelerated odd steps gives

`2^(S_j) y_j = 3^j m + C_j`

with `C_j>0`. Hence

`q_j y_j > m`.                                             (3.1)

Iterating the complementary `L-j` odd steps back from `y_j` to `m` gives

`2^(A-S_j) m = 3^(L-j) y_j + C'_j`

with `C'_j>0`. Since

`lambda/q_j=2^(A-S_j)/3^(L-j)`,

we obtain

`q_j y_j < lambda m`.                                      (3.2)

Because `m` is the least state, `y_j>=m`. Combining with (3.2),

`q_j < lambda`,

or equivalently

`S_j log2 - j log3 < Delta`.                               (3.3)

This is an actual physical-state restriction: it uses the positive affine numerators on both complementary pieces of a real cycle and least-state ownership. It is not a generic count-only CF statement.

Classification: **analytic**.

## 4. RL133.2 — every proper coprime-survivor prefix lies below `beta`

The first-survivor pair `A/L` is a continued-fraction convergent of `beta`.

A classical best-approximation-of-the-second-kind property of convergents says that for every pair of integers `(p,q)` with `0<q<L`,

`|p log2-q log3| > Delta`,                                 (4.1)

unless `(p,q)` is the survivor itself, which is impossible because `q<L`.

Suppose a proper accelerated prefix had

`S_j log2-j log3 > 0`.

Reduce `(S_j,j)` by their gcd `d`. The reduced denominator `j/d` is strictly less than `L`, while by (3.3)

`0 < (S_j/d)log2-(j/d)log3 < Delta`.

This contradicts (4.1). Equality with zero is impossible because no positive powers of `2` and `3` coincide. Therefore every proper prefix satisfies

`S_j log2-j log3 < 0`,                                     (4.2)

hence

`S_j <= floor(j beta)`.                                    (4.3)

### Exact floor lock

The verifier proves with rigorous rational log intervals that

`L Delta < log2`.                                          (4.4)

Since

`A/L-beta=Delta/(L log2)`,

(4.4) gives

`0 < A/L-beta < 1/L^2`.

Because `gcd(A,L)=1`, for every `1<=j<L` the fractional part of `Aj/L` is at least `1/L`. Thus shifting `Aj/L` downward by `j(A/L-beta)<1/L` cannot cross an integer. Consequently

`floor(j beta)=floor(Aj/L)`                                (4.5)

for every proper `j`.

Combining (4.3)–(4.5):

### Theorem RL133.2

For every proper accelerated prefix of a hypothetical `g=1` cycle at the first survivor,

`S_j <= floor(Aj/L)`,  `1<=j<L`.                           (4.6)

Classification: **analytic theorem + exact finite rational-interval arithmetic**.

## 5. RL133.3 — defect excursion and physical height bands

Define

`b_j=floor(Aj/L)`,

`h_j=b_j-S_j`,

for `0<=j<=L`, with `b_L=A` and `S_L=A`.

By RL133.2,

`h_j>=0`, `h_0=h_L=0`.                                     (5.1)

Because `1<A/L<2`, the mechanical increments

`c_j=b_(j+1)-b_j`

belong to `{1,2}`. Since every accelerated exponent `a_j>=1`,

`h_(j+1)-h_j=c_j-a_j <= c_j-1`.                            (5.2)

Thus:

- the defect path is a nonnegative excursion from `0` back to `0`;
- it can rise by at most one in a step;
- it can rise only at a mechanical `c_j=2` position;
- at a `c_j=1` position it cannot increase.

Now define

`rho_j=2^(b_j)/3^j`.

By the floor lock, `b_j=floor(j beta)`, so `rho_j<=1` (strictly `<1` for `0<j<L`). Also

`q_j=rho_j 2^(-h_j)`.

Combining (3.1) and (3.2) yields the physical band

`2^(h_j) m/rho_j < y_j < lambda 2^(h_j) m/rho_j`.          (5.3)

Therefore each unit of prefix defect multiplies the corresponding physical-state scale by a factor of `2`, up to the narrow factors `rho_j` and `lambda`.

Classification: **analytic physical-state geometry**.

## 6. RL133.4 — external-floor shallow-defect population force

This section is explicitly conditional on the inherited external input

`m=R#>=R0:=2^71`.

The inherited exact odd-step product identity is

`Delta = sum_j log(1+1/(3y_j))`.                           (6.1)

Using `log(1+t)<t` and (3.1),

`Delta < (1/3) sum_j 1/y_j < (1/(3m)) sum_j q_j`.

Hence

`sum_j q_j > 3m Delta >= 3R0 Delta`.                       (6.2)

The verifier then bounds the available mechanical mass `sum rho_j` exactly. For proper `j`, the residues `Aj mod L` permute `1,...,L-1`, and

`log rho_j=(j/L)Delta-((Aj mod L)/L)log2`.

Using rigorous rational log intervals, the elementary bounds

`exp(Delta)<=1/(1-Delta)`

and

`1-exp(-x)>=x-x^2/2`, `x=log2/L`,

it certifies

`sum_j rho_j < 99,205,514,478`.                            (6.3)

Let

`N_k=#{j in {0,...,L-1}: h_j<=k}`.

For `M=2^(k+1)`, `rho_j<=1` gives

`sum_j q_j
 <= (sum_j rho_j)/M + (1-1/M) N_k`.                     (6.4)

Combining (6.2)–(6.4) with exact rational arithmetic gives:

### Theorem RL133.4

Conditional on inherited external `R#>=2^71`, any `g=1` physical realization of the first survivor must contain at least

- `176,343,262` odd phases with `h_j<=3`;
- `3,370,832,656` odd phases with `h_j<=4`.

Classification: **analytic consequence + exact finite arithmetic certificate + inherited external computational input**.

These counts do not by themselves imply a cycle or a contradiction. They force a substantial population of prefixes to remain physically close to the zero-defect mechanical envelope.

## 7. RL133.5 — zero-defect extremal falls into the closed radius-one branch

Suppose the defect path were identically zero:

`h_j=0` for all `j`.

Then

`S_j=floor(Aj/L)`,

so the full parity word is the rational mechanical/Christoffel word of slope `L/A` rooted at its first odd symbol.

Let

`s=114,208,327,604`,

`t=72,057,431,991`.

The exact verifier proves

`sL-tA=1`.                                                 (7.1)

For the rational mechanical word, every cyclic length-`s` window contains either `t` or `t+1` ones. The total of all `A` window counts is `sL=tA+1`, so **exactly one** window has `t+1` ones and all other windows have `t`.

RL123's inherited exact sliding-window rotation formula therefore gives

`dist_cyc(w,rot_s(w))=1`.                                  (7.2)

Because `gcd(A,L)=1`, this mechanical word is primitive. Hence an actual ordinary-owned cycle with `h identically 0` would lie in the inherited primitive radius-one branch, which is contained in the already-closed radius-three local engine.

Therefore:

### Corollary RL133.5

A hypothetical `g=1` physical realization of the first CF survivor must have

`h_j>0`

for at least one proper prefix.

Classification: **analytic/combinatorial corollary using the inherited closed radius-three theorem**.

This does not imply that every nonzero defect excursion has small radius.

## 8. Red teams and barriers

### Multiplicity / gcd scope — PASS, load-bearing limitation

The new prefix-sign theorem is **not** promoted for `g>1`. The first reduced survivor may occur as `(gA,gL)`. RL134 must treat multiplicity using physical prefixes/canonical cuts, not count-only gcd data.

### RL20 ownership discriminator — PASS

The prefix squeeze is assumed only for an actual physical cycle rooted at its least state. No arbitrary word satisfying count data is called physical.

### RL79 generalized-increment scaling — PASS

RL133 uses the ordinary `+1` accelerated identity `3y+1=2^a y'` and the ordinary product identity. No generalized-increment invariance is claimed.

### RL81 physical-versus-quotient — PASS

All `y_j` and `m` are actual assumed cycle states. No quotient representative is silently identified with a physical state.

### Fixed-depth residue barrier — respected

RL133 does not attempt to cover all odd residue classes at one depth. Its prefix constraint is conditional on full cycle closure and least-state ownership.

### Bare-CF barrier — respected

Continued fractions enter only after the physical prefix squeeze (3.3) supplies a cycle-specific sub-discrepancy. No new frontier is inferred from the bare survivor inequality.

### Radius scope — PASS

Only the exact zero-defect mechanical extremal is sent to radius one. No radius bound is inferred for arbitrary nonzero defect excursions.

## 9. Correction/demotion ledger

No inherited theorem is demoted.

One scope correction is frozen explicitly: exploratory scratch reasoning initially treated the first reduced survivor as though it necessarily gave the full counts. RL133 does **not** promote that inference. All new prefix-defect conclusions are labeled `g=1`; the multiplicity branch remains open.

The conditional external frontier is unchanged:

`L>=49,547,666,544` under inherited `R#>=2^71`.

The internal frontier is unchanged:

`L>=190,537`.

Gate A, Gate B, global nontrivial-cycle exclusion, and Collatz remain open.

## 10. RL134 direction

RL134 should attack the surviving structure rather than restart retired methods.

1. **Coprime branch (`g=1`)**: combine the nonnegative defect excursion, its one-step rise restriction, the billions of `h<=4` phases, and RL123's sliding-window/rotation formula or direct `D|Q` ownership. The goal is to force an inherited radius-three entry or a direct physical contradiction.
2. **Multiplicity branch (`g>1`)**: extend the physical prefix-strip idea to full counts `(gA,gL)`. Classify which positive prefix discrepancies below `g Delta` can occur at reduced/canonical cuts, using physical-state ownership and exact Farey/CF arithmetic. Do not replace this with count-only gcd blocks.
3. Preserve the external-floor label. Do not infer a frontier advance or Gate closure unless the corresponding full branch is discharged.


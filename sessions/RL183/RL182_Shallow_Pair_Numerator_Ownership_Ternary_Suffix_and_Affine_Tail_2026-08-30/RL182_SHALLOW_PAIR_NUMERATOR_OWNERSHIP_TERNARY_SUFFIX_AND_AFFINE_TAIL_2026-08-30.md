# RL182 — shallow pair numerator ownership, ternary suffixes, and affine-tail occupancy

Date: 2026-08-30

## 0. Outcome and classification

RL182 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`, with `g_p=2^37`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

The main advance is that RL181's shallow physical p-shift gaps are no longer merely dyadic lattice points. Their physical numerators obey an exact chronological transport recurrence, and a shallow numerator is owned by a short ternary suffix of the actual accelerated transition data. Independently, the full p-step affine law supplies a positive physical tail on every normalized p-shift gap and strengthens the mandatory shallow-width occupancy.

Promoted results:

1. **RL182.1 — chronological numerator transport law** (analytic). With the periodic extension, let `k_i=S_(i+1)-S_i`, `G_i=S_(i+p)-S_p-S_i`, and
   `U_i=2^G_i y_(i+p)-y_i` in the dyadic ring `Z[1/2]`. Then
   `2^k_i U_(i+1)=3U_i+2^G_i-1`.
   For an ordinary noncarry p-shift edge with endpoint heights `(a,b)`, the physical numerator of RL181 is
   `C_i=2^e_i U_i`, where `e_i=max(0,-G_i)` and `G_i=a-b`.

2. **RL182.2 — ternary suffix ownership and divisibility reset** (analytic + exact size certificate). Iterating RL182.1 gives, for every `n>=1`,
   `C_i = 3^n 2^(e_i-K_n) U_(i-n) + R_(i,n)`,
   where `K_n=sum_(t=i-n)^(i-1) k_t` and
   `R_(i,n)=sum_(r=1)^n 3^(r-1) 2^(e_i-sum_(t=i-r)^(i-1)k_t)(2^G_(i-r)-1)`.
   Modulo `3^n`, powers of two, including negative powers, are interpreted as units. Hence the current physical numerator is congruent to `R_(i,n)` modulo `3^n`, determined entirely by the current dyadic scaling and the preceding chronological `(k,G)` suffix.

   RL181's uniform normalized-gap ceiling implies the following exact ownership depths for ordinary shallow edges:
   - `h<=1`: `0<C_i<587,183,637,564<3^25`;
   - `h<=2`: `0<C_i<1,174,367,275,128<3^26`;
   - `h<=3`: `0<C_i<2,348,734,550,256<3^26`;
   - `h<=4`: `0<C_i<4,697,469,100,512<3^27`.

   Therefore the corresponding residue modulo `3^25`, `3^26`, `3^26`, or `3^27` determines `C_i` **uniquely**, not merely up to a congruence class.

   The first ternary digit is especially simple:
   `3 | C_i` if and only if `G_(i-1)` is even.
   Thus an odd predecessor defect resets the next physical numerator to ternary valuation zero. Also, a shallow `h<=1` ordinary edge cannot be preceded by 25 consecutive zero defects, and a shallow `h<=4` ordinary edge cannot be preceded by 27 consecutive zero defects: such a suffix would force `C_i=0 (mod 3^n)` while `0<C_i<3^n`.

3. **RL182.3 — internal mass refinement and universal p-window tail** (analytic inequalities + exact rational certificate). Re-evaluating the frozen RL180 mass identities with the same rigorous rational logarithm/exponential enclosures gives, inside this high branch only,
   `26,385,000,000,000,000,000,000 < m < 28,084,000,000,000,000,000,000`
   and `Q>71,134,646,723`.

   Let
   `P_i=sum_(r=0)^(p-1) q_(i+r)`
   in the periodic extension. Any cyclic complement has `t=L-p` base-period phases. Since `q_j<=rho_j`, the mechanical envelope bounds the mass of any such complement by less than `60,422,815,771`. Wrapped periodic q-terms are multiplied by `lambda>1`, so replacing them by their base-period values can only decrease `P_i`. Consequently
   `P_i>10,711,830,952`
   for every phase.

   Summing the exact affine z-increments over p steps and using RL181's normalized p-gap `delta_i` gives
   `delta_i=(exp(s)-1)x_i + exp(s)P_i/(3rho_i)`.
   As `rho_i<=1`, every p-shift gap therefore has the independent physical tail
   `exp(s)P_i/(3rho_i)>3,570,610,317`.

4. **RL182.4 — strengthened shallow normalized-width occupancy** (analytic + exact rational certificate). In p-shift order let `X_r` be the source normalized coordinate. RL182.3 gives
   `X_(r+1)>exp(s)X_r+T`, with `T=3,570,610,317`.
   Therefore the gap at rank r is larger than
   `exp(sr)((exp(s)-1)m+T)`.
   For any set of `E` p-shift gap sources, the minimum sum of these increasing lower bounds is attained at the first E ranks. Combining this with the inherited shallow-edge populations and the refined upper bound on m proves:
   - `h<=1`: shallow width `>25m/512`;
   - `h<=2`: shallow width `>33m/256`;
   - `h<=3`: shallow width `>167m/1024`;
   - `h<=4`: shallow width `>23m/128`.

   These strictly strengthen RL181's `11/256, 15/128, 5/32, 11/64` ladder. In particular, the height-four shallow family occupies more than `17.96875%` of the complete normalized width.

5. **RL182.5 — repeated defect classes feed uniform ternary predictions** (analytic combinatorics). Removing the possible carry edge and grouping ordinary shallow p-shift edges by `G=a-b` gives a fixed defect value repeated at least
   - `3,358,391,526` times for `h<=1`;
   - `5,136,718,940` times for `h<=2`;
   - `4,583,057,040` times for `h<=3`;
   - `3,888,913,815` times for `h<=4`.
   For each such fixed-G class, the chronological successor numerator has a common mod-3 divisibility prediction from RL182.2, apart from the possible unique successor which is the carry edge.

The high branch remains open. The new suffix theorem converts physical numerator ownership into a finite-modulus chronological condition, but no certified upper bound is yet available for how many physically admissible 25/26/27-step suffixes can land on the required shallow family.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `t=L-p=72057431991`.

Let

`Delta=A log 2-L log 3 >0`, `lambda=exp(Delta)`,
`s=p log 3-u log 2 >0`,
`b_i=floor(Ai/L)`, `h_i=b_i-S_i>=0`,
`q_i=2^S_i/3^i`, `rho_i=2^b_i/3^i`, `z_i=q_i y_i`,
and extend periodically by
`y_(i+L)=y_i`, `S_(i+L)=S_i+A`, `q_(i+L)=lambda q_i`.

RL181 supplies:

- the full normalized p-shift chain from `m` to `2m`;
- `128,081,997,553 < K_i < 146,795,909,391`;
- every normalized p-shift gap satisfies
  `128,081,997,553 < delta_i < 293,591,818,782`;
- shallow p-shift edge floors
  `10,075,174,578`, `25,683,594,700`, `32,081,399,276`, `35,000,224,336`
  for heights one through four;
- at most one edge in each family is the carry edge;
- for an ordinary edge, the physical numerator `C_i` is the exact positive integer from the RL181 height-dependent formula.

RL180 supplies the mass identities, mechanical residue envelope, and high-branch scope. All inherited correction/demotion locks remain in force.

## 2. Chronological transport of the physical pair difference

Put

`k_i=S_(i+1)-S_i`

and, in the periodic extension,

`U_i=2^G_i y_(i+p)-y_i`.

The two accelerated transitions are

`2^k_i y_(i+1)=3y_i+1`,
`2^k_(i+p) y_(i+p+1)=3y_(i+p)+1`.

Also

`G_(i+1)=G_i+k_(i+p)-k_i`.

Multiplying `U_(i+1)` by `2^k_i` and substituting these identities gives exactly

`2^k_i U_(i+1)=3U_i+2^G_i-1`.

No physical-existence inference is made from an arbitrary solution of this recurrence. It is an identity satisfied by the assumed physical cycle.

For an ordinary noncarry p-shift edge with heights `(a,b)`,
`G_i=a-b`. If `G_i>=0`, the RL181 physical numerator is `U_i`; if `G_i<0`, it is `2^(-G_i)U_i`. Hence in all cases

`C_i=2^e_i U_i`, `e_i=max(0,-G_i)`.

This is the bridge between RL181's large physical shallow family and chronological accelerated-transition arithmetic.

## 3. Ternary suffix ownership

Iterate the transport recurrence backwards n times in `Z[1/2]`. One obtains

`U_i =
  3^n 2^(-K_n) U_(i-n)
  + sum_(r=1)^n 3^(r-1) 2^(-sum_(t=i-r)^(i-1)k_t)(2^G_(i-r)-1)`,

where `K_n=sum_(t=i-n)^(i-1)k_t`.

After multiplying by `2^e_i`, reduction modulo `3^n` kills the inherited first term. Since every power of two is invertible modulo `3^n`, this reduction is legitimate even when an exponent is negative. This proves RL182.2.

For an ordinary shallow edge with endpoint heights at most k, RL181 gives

`C_i=2^max(a,b) delta_i < 2^k * 293,591,818,782`.

The exact integer comparisons with powers of three give the 25/26/26/27 ownership-depth ladder.

For `n=1`,

`C_i = unit * (2^G_(i-1)-1) (mod 3)`,

so `3|C_i` exactly when `G_(i-1)` is even. If the preceding n defects all vanish then every term in the suffix residue vanishes; the shallow size bounds therefore forbid the stated 25- and 27-zero suffixes.

This is a physical numerator restriction. It does not certify that an arbitrary transition suffix is realizable.

## 4. Universal p-window q-mass

RL180's exact mass calculation gives

`Q=R-W=3(lambda-1)m`.

The RL182 verifier retains the full rational interval rather than rounding immediately to the older coarse `2^74<m<3*2^73` band. It certifies the displayed refined m interval and

`Q>71,134,646,723`.

For a base-period subset of t phases, `q_j<=rho_j`. The mechanical weights, in residue order, obey

`rho_r < exp(Delta) 2^(-r/L)`.

Therefore the maximum q-mass of any t-element complement is bounded by the first t terms of that mechanical envelope, and the exact verifier gives

`mass(complement)<60,422,815,771`.

If a p-step window wraps the period, its wrapped q-terms are multiplied by `lambda>1`; replacing them by base-period q-values lowers the window mass. Hence every periodic p-window satisfies

`P_i>71,134,646,723-60,422,815,771
     =10,711,830,952`.

## 5. Affine p-step law and strengthened occupancy

The normalized affine increment is

`z_(i+1)-z_i=q_i/3`.

Summing p steps gives

`z_(i+p)-z_i=P_i/3`.

Since

`K_i=exp(s)z_(i+p)-z_i`
and
`q_i y_i=rho_i x_i`,

RL181's identity `K_i=rho_i delta_i` becomes

`delta_i=(exp(s)-1)x_i + exp(s)P_i/(3rho_i)`.

The universal p-window lower bound and `rho_i<=1` yield the strict tail `>T=3,570,610,317`.

Now order sources by `i_r=pr (mod L)` and write `X_r=x_(i_r)`, using the terminal copy `X_L=2m`. Then

`X_(r+1)>exp(s)X_r+T`.

Induction gives

`delta_r > exp(sr)((exp(s)-1)m+T)`.

For any E selected ranks the right-hand side is increasing, so the minimum selected sum is the first E terms:

`sum_selected delta_r
 > m(exp(sE)-1)
   + T (exp(sE)-1)/(exp(s)-1)`.

The bundled exact verifier inserts the four inherited shallow-edge floors, rigorous rational enclosures for s and exp, and the refined upper bound on m. It proves the promoted `25/512, 33/256, 167/1024, 23/128` occupancy ladder.

## 6. Repeated defect classes and the remaining barrier

For height cutoff k, an ordinary shallow edge has

`G=a-b in {-k,...,k}`,

only `2k+1` possibilities. Pigeonholing the inherited ordinary-edge floors gives RL182.5.

This is useful because a repeated defect class produces the same binary parity of `G`, and therefore the same mod-3 divisibility prediction for the next chronological physical numerator. But it is not yet a contradiction: the next numerator need not itself be shallow, and the set of physically admissible 25/26/27-step suffixes has not yet been capped below the required population.

Freeze the successor barrier:

> Ternary suffix ownership is now exact for every shallow physical numerator, but closure requires a **physical suffix-capacity or successor-correlation theorem**. Counting arbitrary residue strings, arbitrary automaton states, or arbitrary dyadic/ternary lattice points is not sufficient.

## 7. Red-team scope

- **Dyadic versus integer:** PASS. `U_i` is allowed to lie in `Z[1/2]`; only the rescaled ordinary-edge `C_i` is promoted as the physical integer numerator.
- **Negative powers modulo 3:** PASS. Powers of two are units modulo every `3^n`, so the ternary suffix congruence is well-defined.
- **Carry:** PASS. Physical-numerator size/ownership statements are for ordinary noncarry edges. The periodic recurrence may cross the unique carry algebraically; no carry edge is silently classified as ordinary.
- **Necessary versus physical:** PASS. The suffix formula constrains actual physical edges. It does not promote arbitrary transition words or necessary automaton states to existence.
- **Periodic p-window wrap:** PASS. Wrapped q-terms are multiplied by `lambda>1`, so the base-period cyclic replacement is a safe lower bound.
- **Mass provenance:** PASS. The refined m/Q bounds are derived from the frozen RL180 high-branch identities and rigorous rational enclosures; they remain internal to `(37,0,23,-1)`.
- **Occupancy minimization:** PASS. The increasing affine lower envelope is minimized over arbitrary selected ranks before the shallow population floors are inserted.
- **Historical barriers:** PASS. No generic rank/chain capacity, inverse-rank identity, blind higher odd-modulus lift, or RL173 physical interpretation is revived.
- **No false closure:** PASS. The high branch and all global gates remain open.

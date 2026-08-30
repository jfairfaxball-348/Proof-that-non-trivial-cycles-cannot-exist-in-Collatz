# RL193 — Physical Debt Telescope, Valuation, and Phase Incidence

Date: 2026-08-31
Authoritative branch: sole high branch `(v,H,J,d)=(37,0,23,-1)`.
Incoming authority: RL192 at `706dae8a25fc7b494ee2d97eab0e2d69181aa82f`.

Every assertion about an extremal triple below is conditional on a
hypothetical physical triple.  No necessary terminal rank is asserted to be
realized.  No branch or global gate is closed.

## 0. Portable inherited definitions and scope

The integer constants are

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`R=2L-A=57079296007`, `p=65470613321`, `u0=103768467013`,
`Ap-u0 L=1`, `z=L-p=72057431991`, `Q=37B mod L=88514772733`.

Canonical phases are `0<=i<L`; rank is `r_i=iB mod L`.  The mechanical
exponent is `c_i=floor(A(i+1)/L)-floor(Ai/L)`, equal to 1 below rank R and
2 otherwise.  For a block of length n beginning at rank r, its exponent sum
is `floor((r+nA)/L)`.

The physical nonnegative integer height is `h_i`, with `h_0=0`, periodic
modulo L, and `h_(i+1)<=h_i+1`.  At an ordinary source, put
`j=(i+p) mod L`, `G_i=h_i-h_j`; at the unique carry source z, use
`G_z=1+h_z`.  Define

`rho_i=2^floor(Ai/L)/3^i`, `q_i=rho_i 2^(-h_i)`,
`epsilon_i=2^(-h_i)(2^(G_i)-1)`, `f_i=rho_i epsilon_i`.

The physical normalized gap is `Delta_i=K_i/rho_i`, where the inherited
corrected-gap coordinate K satisfies

`K_0=2^37`, `f_i=3(K_(i+1)-K_i)`,
`2^(c_i)Delta_(i+1)=3Delta_i+epsilon_i`.

The lifts obey `K_(i+L)=lambda K_i`, `rho_(i+L)=lambda rho_i`, with
`lambda=2^A/3^L`; Delta, heights, errors and mechanical bits are periodic.
For canonical i, `1/2<rho_i<=1` and
`128081997553<K_i<146795909391`.  Only rho_0 equals 1.  RL192 certifies
`0<delta=A ln2-L ln3<2^-40`.

An extremal `{35,36,37}` terminal has a tau=37 zero-defect prefix and
ordinary terminal endpoint maximum 21; its terminal normalized gap is
`3^37/2^21`, its prefix-start gap is `2^37` or `2^38`, and its necessary
rank belongs to `E=[72797034370,103818202602]`.  The binding H21
`{33,34,35}` family has a tau=35 zero prefix and necessary core
`D_H21=[23369453298,41775866136]`.

The inherited high-branch signature is `G_0=...=G_23=0`,
`G_24,...,G_28<0`, `G_29!=0`.  The latter exact necessary-state certificate
is included verbatim as `verification/verify_rl178_inherited_early_window.py`.

RL191 retains distinct-extremal spacing at least 1001,
`N35<=7559400754`, ordinary absolute corrected flow `>480`, and
directional K variation `>80`.  These are not excursion bounds.  The H21
charging equality remains binding.  No physical population or ownership
bound follows merely by deleting necessary ranks.

## 1. Exact indexing and the common tail numerator

Choose the canonical phase `0<=a<L` of a physical extremal triple's `tau=37`
start and put `u=a+37` in the periodic lift.  Write

`lambda=2^A/3^L=exp(delta)`,

where `delta=A ln(2)-L ln(3)>0`.  The inherited zero prefix and endpoint gaps
are

`Delta_a=T=2^k`, `k in {37,38}`,

`Delta_u=3^37/2^21`.

All 37 errors on `[a,u)` vanish.  If their mechanical exponent sum is `H`,
zero-error propagation gives `H=k+21`.  Hence the complementary interval
`[u,a+L)` has length `n=L-37` and exponent sum

`S=A-k-21`.

For `0<=j<=n`, put

`P_j=sum_(ell<j)c_(u+ell)`.

Exact iteration of

`2^(c_i) Delta_(i+1)=3 Delta_i+epsilon_i`

gives

`2^S Delta_(a+L)=3^n Delta_u+D`,

where

`D=sum_(j<n)3^(n-1-j)2^(P_j)epsilon_(u+j)`.

Since `Delta_(a+L)=Delta_a=T`, substitution yields the atom-independent
identity

`D=(2^A-3^L)/2^21`.                                      (1)

After final normalization,

`D/2^S=T(1-3^L/2^A)=T(1-exp(-delta))`.                   (2)

The atom table is exact:

| terminal-rank atom | `T` | zero-prefix sum | complement sum |
| --- | ---: | ---: | ---: |
| `[72797034370,88514772732]` | `2^38` | 59 | `A-59` |
| `[88514772733,103818202602]` | `2^37` | 58 | `A-58` |

## 2. Physical substitution telescopes term by term

Use the inherited physical identities

`rho_(i+1)=2^(c_i)rho_i/3`,

`rho_i epsilon_i=q_i(2^(G_i)-1)=3(K_(i+1)-K_i)`.

The second identity contains the ordinary formula
`epsilon_i=2^(-h_j)-2^(-h_i)` and the unique carry formula
`epsilon_i=2-2^(-h_i)` without relaxation.  Since

`rho_(u+j)/rho_u=2^(P_j)/3^j`,

every summand in (1) is the same constant multiple of a physical `K`
increment.  Therefore

`D=(3^n/rho_u)(K_(a+L)-K_u)`.                            (3)

The zero prefix has no `K` drift, so `K_u=K_a`.  Periodic monodromy gives
`K_(a+L)=lambda K_a`.  Equation (3) then reproduces (1) identically.

Equivalently, in final-gap units each recurrence correction term is

`3^(n-1-j)epsilon_(u+j)/2^(S-P_j)
 =(K_(u+j+1)-K_(u+j))/rho_(a+L)`,

so the apparent nonuniform affine weights are precisely the physical flow
weights divided by one common endpoint factor.

This proves conditional compatibility, not physical existence.  The total
weighted-debt equation contains no information beyond the inherited endpoint
monodromy once the 37-zero prefix is assumed.

## 3. Exact 2-adic valuation is locally automatic

Because `2^A-3^L` is odd, (1) requires `v_2(D)=-21` on both atoms.  The
terminal source lies in

`E=[72797034370,103818202602]`,

strictly above `R=57079296007` and below the unique carry rank `L-1`.
It is therefore ordinary, has `c_0=2`, is a nonzero defect, and has endpoint
maximum 21.  Hence

`v_2(epsilon_u)=-21`.

For tail offset `j>=1`, the height-rise law gives endpoint maximum
`H_j<=21+j`, while the initial `c_0=2` and all later `c_i>=1` give
`P_j>=j+1`.  Thus every later term of `D` has valuation at least

`P_j-H_j>=-20`.

The first term is the unique term of valuation `-21`, so the required total
valuation follows without cancellation.  Total-valuation or denominator
tests therefore cannot exclude either atom.

The stronger endpoint congruence is

`2^21 D == -3^L (mod 2^m)` for `1<=m<=A`.

Since `v_2(L)=8`, LTE gives `v_2(3^L-1)=10` and hence
`v_2(2^21 D+1)=10`.  These higher congruences are exact, but at the level of
the total sum they remain endpoint identities.  A future consumer must retain
owned local numerators and locations rather than only the total valuation.

## 4. Unweighted physical telescope and carry incidence

Put `v_i=2^(-h_i)`.  Ordinary physical errors are `v_(i+p)-v_i`.
At the unique carry source `z=L-p`, the target is phase zero with `v_0=1`
and the physical error is

`2-v_z=(v_0-v_z)+1`.

The p-shift targets permute the phases, so the ordinary differences together
with the noncarry part of the carry telescope to zero.  Therefore the exact
base-period identity is

`sum_(i mod L) epsilon_i=1`.                              (4)

The 37-zero block contains no carry and contributes zero.  On its complement,

`sum_(ordinary)epsilon_i=v_z-1<=0`,

while the carry supplies `2-v_z`.  This fixes the exact ordinary unweighted
aggregate; the weighted identity below additionally forces a strictly
negative ordinary net.

The carry source has mechanical rank `L-1`.  If a zero-prefix terminal has
rank `r` and the carry lies `d` sources before it, then

`r=(L-1+dB) mod L`.

Intersecting `d=1,...,37` with the extremal core removes exactly these nine
necessary ranks:

`75485708845, 80448749304, 83137423780, 85826098256,`

`88514772732, 93477813191, 96166487667, 98855162143,`

`103818202602`.

This is a finite necessary-rank refinement, not a realization or atom
exclusion.  Both RL192 atoms retain large nonempty sets.  On the complement,
the first possible carry is at least 11 sources after the terminal and at
least 5 sources before the next start on the `2^38` atom; the corresponding
buffers on the `2^37` atom are 4 and 7.

The same exact incidence test applies to the binding H21 `{33,34,35}` joint
family through its 35-zero member.  It removes five isolated ranks from
`D=[23369453298,41775866136]`:

`26058127773, 28746802249, 36398517184, 39087191660, 41775866136`.

These deleted necessary ranks do not provide a physical count or multiplicity
bound, so the binding H21 charging budget is unchanged.

## 5. The canonical early-defect window and strict prefix signs

The defining high branch has `G_0=...=G_23=0`.  The frozen RL178 exact
second-transition certificate proves `G_24,...,G_28<0` and `G_29!=0`.
That live dependency was replayed successfully for this use.

A first-defect terminal with zero-prefix length `tau` has nonzero `G_t` and
zero sources `G_(t-tau),...,G_(t-1)`.  It therefore cannot have canonical
terminal phase `t in [0,23]`, and its zero prefix cannot meet phases 24..29.
The latter excludes exactly `t in [25,29+tau]` in the early canonical window.

For `tau=37`, intersecting those phase ranks `tB mod L` with E removes ten
prefix-contaminated ranks

`75485708846, 78174383322, 80863057798, 83551732274, 85826098257,`

`88514772733, 91203447209, 93892121685, 98855162144, 101543836620`,

and five ranks whose terminal itself is known zero:

`72797034370, 80448749305, 83137423781, 93477813192, 96166487668`.

Together with the nine carry deletions, this refines the extremal necessary
core to `E` minus 24 distinct ranks.  It contains 31,021,168,209 certificate
ranks, not a claimed number of physical terminals.  In the canonical phase
numbering there is no physical extremal terminal before phase 71: the known
window excludes phases through 66 except 24, whose rank is outside E; phases
67..70 are also rank-forbidden.

For the H21 joint family, its `tau=35` member gives five additional
prefix-contaminated ranks

`23783761791, 28746802250, 31435476726, 34124151202, 36812825678`,

and four known-zero terminal ranks

`23369453298, 26058127774, 36398517185, 39087191661`.

Together with the five carry deletions, the H21 core is `D` minus 14 distinct
ranks.  There is no such canonical terminal before phase 67.  The H21 binding
budget still does not change.

The triple start rank is `(r_terminal-Q) mod L`.  The lower/`2^38` atom has
start ranks `[121810306949,L-1]`; the upper/`2^37` atom has start ranks
`[0,15303429869]`.  Since `K_start=rho_start T`, `K_0=2^37`, and
`1/2<rho_i<1` for `0<i<L`, these force opposite actual chronological prefix
signs:

- lower atom: `sum_(0<=i<start)f_i=3(K_start-K_0)>0`;
- upper atom: the same prefix sum is strictly negative.

The only possible equality case on the upper atom would be start phase zero,
equivalently terminal rank `Q`; the early-defect window has just excluded it.
Here the start is always its canonical representative in `[0,L)`.  Strict
`rho_i<1` for nonzero canonical phases follows from the inherited `rho_i<=1`
and `rho_i=2^(floor(Ai/L))/3^i`: equality is impossible for `i>0`.
This is a genuine signed displacement theorem, not an inference from total
variation.  Both signs still fit inside the inherited K corridor.

## 6. The carry oversupplies the signed debt

The 37-zero suffix cannot contain the carry, whose physical error is at least
one.  Thus the complementary interval contains the unique carry.  Put
`f_i=rho_i epsilon_i`.  Summing its `K` increments gives the exact signed flow

`F_tail=sum_[u,a+L) f_i=3(lambda-1)K_u>0`.               (5)

The inherited corridor has `K_u<146795909391`.  From
`0<delta<2^-40` and `exp(x)-1<x/(1-x)` for `0<x<1`,

`lambda-1<1/(2^40-1)`.

The exact small-integer comparison

`6*146795909391 < 2^40-1`

therefore proves

`0<F_tail<1/2`.                                          (6)

At the carry, `rho>1/2`, `h>=0`, and
`epsilon_carry=2-2^(-h)>=1`, so its flow is strictly greater than `1/2`.
Combining this with (6) shows that the carry contribution strictly
oversupplies the positive debt and the sum of all ordinary physical flow
terms on the complement is strictly negative.  The same sign statement
holds after division by the common positive factor `3 rho_(a+L)` in the
normalized affine debt.

Thus the physical mechanism is not a freely chosen small positive final
error: the forced positive carry is offset by negative ordinary flow, leaving
the tiny positive monodromy net.

More precisely, the inherited bounds give atom-specific strict cancellation
floors:

- on the `2^38` atom,
  `sum ordinary f_i < -72912057143/733007751850`;
- on the `2^37` atom,
  `sum ordinary f_i < -91625968981/733007751850`.

The first uses `K_start=K_terminal<146795909391`; the second uses the sharper
`K_start=rho_start*2^37<=2^37`.  If the carry height is at least one, each
floor strengthens by `1/4`.

## 7. Classification and remaining obligation

- Equations (1)--(6), the valuation theorem, and the carry/ordinary sign
  decomposition are **proved analytic mathematics**, conditional
  on a physical extremal triple.
- The fact that they do not exclude either atom is a **method barrier** for
  the displayed total weighted-debt and total-valuation identities alone.
  Separately, unsigned variation cannot be converted to excursion without
  an ordering theorem.
- No rank is realized, no extremal triple is constructed, and no branch or
  global gate is closed.
- The 24 extremal and 14 H21 rank deletions are exact finite necessary-state
  refinements; the opposite prefix signs are conditional analytic results.
- A live successor must preserve information erased by summation: prefix
  congruences coupled to owned pair numerators, carry phase versus terminal
  rank, partial `K` order, or a genuine chronological/H21 incidence theorem.

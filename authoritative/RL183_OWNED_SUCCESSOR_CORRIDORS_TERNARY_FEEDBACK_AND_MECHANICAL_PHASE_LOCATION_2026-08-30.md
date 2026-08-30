# RL183 — owned successor corridors, ternary feedback, and mechanical phase location

Date: 2026-08-30

## 0. Outcome and classification

RL183 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

The session converts RL182's isolated shallow-numerator ownership into a genuinely chronological physical structure. A very large `h<=1` p-shift family forces long runs of ordinary successor pair gaps; every numerator along those runs remains uniquely owned by a short ternary suffix. The first successor also turns the current physical numerator parity and next ternary divisibility into an exact coarse defect sensor. Away from two mechanically exceptional p-ranks, consecutive pair numerators obey a finite height/mechanical affine template, yielding a small three-transition map vocabulary. Independently, the chronological mechanical bit `c_i=b_(i+1)-b_i` physically localizes normalized states on opposite sides of a narrow interval around `4m/3`.

Promoted results:

1. **RL183.1 — successor height-rise and 25-edge owned corridors** (analytic + exact combinatorics). Put
   `c_i=b_(i+1)-b_i in {1,2}`. Since the accelerated exponent `k_i>=1`,
   `h_(i+1)=h_i+c_i-k_i<=h_i+1`.
   Hence if an ordinary p-shift edge at phase i has both endpoint heights at most k, then its j-th chronological successor has both endpoint heights at most `k+j`.

   RL181/RL182 give `10,075,174,578` p-shift edges with endpoint heights at most one, at most one of them the unique carry edge. Thus there are at least `10,075,174,577` ordinary `h<=1` starts. Excluding the at most 24 starts whose next 24 p-shift edges cross the unique carry source leaves at least

   `10,075,174,553`

   physical starts for which the 25 edges `i,i+1,...,i+24` are all ordinary and have endpoint-height cutoffs at most `1,2,...,25`.

   RL182.2 is valid modulo `3^n` for every n, while RL181 supplies the uniform gap ceiling
   `delta<293,591,818,782`. For endpoint-height cutoff k,
   `0<C<2^k*293,591,818,782`.
   The least ownership depths for `k=1,...,25` are

   `25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,35,35,36,37,37,38,38,39,40,40`.

   Therefore every one of those more than ten billion 25-edge corridors consists entirely of physical numerators uniquely owned by actual chronological ternary suffixes, with required depth never exceeding 40.

2. **RL183.2 — binary/ternary defect sensor** (analytic). On an ordinary p-shift edge with endpoint heights `(a,b)`, RL181's exact numerator formula gives
   `2|C_i` if and only if `a=b`, equivalently `G_i=0`.
   RL182 gives
   `3|C_(i+1)` if and only if `G_i` is even.
   Consequently, whenever both i and i+1 are ordinary, the pair

   `(C_i mod 2, C_(i+1) mod 3)`

   determines the coarse physical defect class:
   - `C_i` even  iff `G_i=0`;
   - `C_i` odd and `3|C_(i+1)` iff `G_i` is nonzero even;
   - `C_i` odd and `3∤C_(i+1)` iff `G_i` is odd.

   In particular, for an ordinary `h<=1` edge, `G_i in {-1,0,1}`, so

   `2|C_i` if and only if `3|C_(i+1)`.

   This activates RL182's ternary reset on the physical successor family rather than on arbitrary words or automaton states.

3. **RL183.3 — common-mechanical successor law and finite three-transition map vocabulary** (analytic + exact finite certificate). Let the p-shift/residue rank be
   `r_i=A i (mod L)`. Since `A/L in (1,2)`,
   `c_i=1` for `r_i<R:=2L-A=57,079,296,007`
   and `c_i=2` for the remaining
   `A-L=80,448,749,305` ranks.
   The p-shift target has rank `r_i+1 (mod L)`. Therefore `c_(i+p)=c_i` except at exactly two p-ranks: the ordinary mechanical-switch source `r=R-1` and the unique carry source `r=L-1`.

   On any ordinary pair transition avoiding those exceptions, write current endpoint heights `(a,b)`, successor heights `(a',b')`, `M=max(a,b)`, `M'=max(a',b')`, and physical pair numerators `C,C'`. The normalized chronological recurrences have the same c, so

   `2^d C' = 3C + 2^(M-b) - 2^(M-a)`,
   where `d=c+M-M' >=1`.

   Starting from `(a,b) in {0,1}^2`, the necessary height-rise constraints give at most 34 one-transition templates, 342 two-transition templates, and 3,884 three-transition templates. Those 3,884 templates collapse to only 357 distinct composite affine maps from `C_i` to `C_(i+3)`.

   From the ordinary `h<=1` start floor, exclude at most three starts whose next three p-edges cross the carry and at most three starts whose first three pair transitions hit the ordinary mechanical-switch source. At least

   `10,075,174,571`

   clean four-edge corridors remain. Hence some necessary three-transition height/mechanical template is physically used at least

   `2,594,021`

   times, and some composite three-transition affine numerator map is physically used at least

   `28,221,778`

   times.

   The 3,884 templates and 357 maps are a certified necessary vocabulary, not a claim that every listed template or map is physically realizable.

4. **RL183.4 — mechanical-bit phase-location split** (analytic + exact combinatorics). For every chronological phase,
   `2^c_i x_(i+1)=3x_i+2^(-h_i)`,
   where the p-shift chain places every normalized physical state in `[m,2m)`.
   Thus:
   - if `c_i=1`, then `x_i<4m/3`;
   - if `c_i=2`, then `x_i>=(4m-2^(-h_i))/3>=(4m-1)/3`.

   Hence the two mechanical classes can overlap only in the interval
   `[(4m-1)/3,4m/3)`, of width `1/3`. Among states with `h<=k`, normalized coordinates lie on the `2^-k` grid, so that overlap contains at most `ceil(2^k/3)` such physical states.

   Combining this with RL180's shallow-population floors and the exact mechanical-rank capacities forces the following counts:

   | cutoff | forced `c=1` shallow states | forced `c=2` shallow states | overlap cap | forced `c=2` shallow states with `x>=4m/3` |
   | --- | ---: | ---: | ---: | ---: |
   | `h<=1` | 0 | 16,722,313,938 | 1 | 16,722,313,937 |
   | `h<=2` | 1,157,070,701 | 24,526,523,999 | 2 | 24,526,523,997 |
   | `h<=3` | 4,355,972,989 | 27,725,426,287 | 3 | 27,725,426,284 |
   | `h<=4` | 5,815,385,519 | 29,184,838,817 | 6 | 29,184,838,811 |

   This is a physical phase-location correlation: tens of billions of certified shallow states are forced into the late mechanical class, and almost all of those forced late states lie at or above `4m/3`.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `t=L-p=72057431991`.

Let

`b_i=floor(Ai/L)`, `h_i=b_i-S_i>=0`,
`k_i=S_(i+1)-S_i`,
`c_i=b_(i+1)-b_i`,
`x_i=y_i/2^h_i`.

Retain all RL182 certified facts, especially:

- the corrected defect `G_i=S_(i+p)-S_p-S_i`;
- the physical transport
  `2^k_i U_(i+1)=3U_i+2^G_i-1`;
- ordinary physical numerator `C_i=2^max(0,-G_i)U_i`;
- ternary suffix ownership modulo `3^n` for every n;
- `3|C_i` iff `G_(i-1)` is even;
- the uniform normalized p-gap ceiling `293,591,818,782`;
- shallow p-edge floors and width occupancies;
- the refined high-branch m band and affine-tail lower bound.

Retain RL180 shallow phase floors

`N_1=73,801,609,945`,
`N_2=81,605,820,006`,
`N_3=84,804,722,294`,
`N_4=86,264,134,824`.

All of these remain internal to `(37,0,23,-1)`.

## 2. Successor height rise

Since `S_(i+1)=S_i+k_i` and `b_(i+1)=b_i+c_i`,

`h_(i+1)=b_(i+1)-S_(i+1)=h_i+c_i-k_i`.

Here `c_i in {1,2}` and every accelerated odd step has `k_i>=1`, so

`h_(i+1)<=h_i+1`.

Apply this simultaneously to the source i and ordinary p-shift target `i+p`. The p-shift target of the next chronological edge is `i+p+1`, so a shallow pair propagates forward with cutoff increasing by at most one per chronological step.

The p-shift graph has one carry source. Among the `10,075,174,577` ordinary `h<=1` starts, each future offset `j=1,...,24` can place the carry at at most one starting phase. Removing those at most 24 starts proves the 25-edge ordinary-corridor floor.

For an ordinary edge with endpoint heights at most k,

`delta=C/2^M` with `M<=k`.

The inherited strict upper gap bound gives

`0<C<2^k*293,591,818,782`.

RL182's suffix congruence is valid for arbitrary n, so taking the least n for which the right side is below `3^n` yields the displayed ownership-depth ladder through height 25.

This is not formal residue counting: every corridor is cut out of the assumed physical cycle.

## 3. Parity and the next ternary digit

RL181's ordinary numerator formula shows:

- if endpoint heights are unequal, C is odd;
- if endpoint heights are equal, C is positive even.

On an ordinary p-edge `G_i=a-b`, so this is exactly

`2|C_i <=> G_i=0`.

RL182.2a applied to the chronological successor gives

`3|C_(i+1) <=> G_i even`.

The three coarse defect classes follow immediately. At height one, the only possible defects are `-1,0,1`, giving the sharper parity/divisibility equivalence.

The point is temporal: the current physical pair numerator and the next physical pair numerator jointly read a property of the current p-shift defect.

## 4. Common mechanical bit and the affine numerator map

Let

`r_i=A i mod L`.

Writing `Ai=L b_i+r_i` gives

`c_i=floor((r_i+A)/L)`.

Because `L<A<2L`, put

`R=2L-A=57,079,296,007`.

Then `c_i=1` for `0<=r_i<R` and `c_i=2` otherwise.

Also `Ap-uL=1`, hence the p-shift target has residue rank

`r_(i+p)=r_i+1 mod L`.

The mechanical bits therefore differ only when that increment crosses R or wraps L: at `r=R-1` and `r=L-1`. The latter is precisely the unique p-shift carry source.

The ordinary normalized chronological transition follows directly from the accelerated odd map:

`2^c_i x_(i+1)=3x_i+2^(-h_i)`.

On a clean p-pair transition, source and target share c. Subtract the two normalized recurrences. If `delta=C/2^M` and `delta'=C'/2^M'`, then

`2^c C'/2^M' = 3C/2^M + 2^-b - 2^-a`.

Multiplying by `2^M` gives RL183.3. Since each successor height is at most its current height plus `c-1`, `M'<=M+c-1`, so `d=c+M-M'>=1`.

The bundled verifier enumerates only the necessary local height ranges
`0<=a'<=a+c-1`, `0<=b'<=b+c-1`.
It records the exact template counts 34, 342, 3,884 and the 357 distinct three-step affine maps. This enumeration is intentionally local and small; no surviving template is promoted as a physical state.

## 5. Mechanical phase location

The same normalized chronological law has a global geometric consequence.

Every `x_i` is one vertex of RL181's strict p-shift chain from m to the terminal copy 2m, so

`m<=x_i<2m`.

If `c_i=1`,

`2x_(i+1)=3x_i+2^-h_i <4m`,

hence `x_i<4m/3`.

If `c_i=2`,

`4x_(i+1)=3x_i+2^-h_i >=4m`,

hence
`x_i>=(4m-2^-h_i)/3>=(4m-1)/3`.

There are exactly R early mechanical ranks and `L-R=A-L` late ranks. For a shallow cutoff k, a population `N_k` therefore forces at least

`max(0,N_k-(A-L))`

shallow states into c=1 and at least

`max(0,N_k-R)`

into c=2.

A state with `h<=k` has `x=y/2^h` on the `2^-k` grid. The possible c-class overlap interval has width `1/3`, so it contains at most `ceil(2^k/3)` distinct shallow normalized states. Subtracting this cap from the forced c=2 count proves the last column of RL183.4.

## 6. Barrier and next consumer

RL183 makes the suffix problem substantially more physical, but it does not yet supply a quota-breaking capacity theorem.

Three limitations are now explicit:

1. A 25-edge owned successor corridor constrains future numerators, but RL182 ownership is by the **preceding** ternary suffix. Backward heights can drop by more than one in a single step, so the forward height-rise theorem does not by itself bound the full predecessor vocabulary.
2. The three-transition necessary vocabulary is small enough to force millions of repeated physical map uses, but repeated use of the same affine map is not itself impossible. Extending the unconstrained necessary-template enumeration to long windows grows rapidly and is not a closure-grade substitute for a global consumer.
3. The mechanical phase split localizes tens of billions of shallow states, but each mechanical compartment still has enough raw capacity. The missing theorem must couple phase location or map repetition to defect sign/parity, corrected-flow drift, ternary reset, or shallow width.

Freeze the route limitation:

> The next step should not merely enumerate longer local successor templates. It should exploit the owned 25-edge physical corridors together with the defect sensor and mechanical phase location to cap repeated defect/map patterns or force a corrected-flow/width contradiction.

## 7. Red-team scope

- **Physical versus formal suffixes:** PASS. Corridor counts begin with inherited physical shallow p-edges; no arbitrary suffix is promoted as realizable.
- **Carry:** PASS. The unique p-shift carry is removed explicitly from ordinary starts and from the future offsets used by each corridor claim.
- **Mechanical-switch exception:** PASS. The finite common-c map theorem separately removes the unique ordinary p-rank where source and target mechanical bits differ.
- **Ownership extension:** PASS. RL182 proves the suffix congruence for every n; RL183 only adds the inherited physical numerator ceiling to choose sufficient n through height 25.
- **Parity:** PASS. Even/odd statements use RL181's physical ordinary numerator formula, not a normalized-coordinate parity fiction.
- **Necessary versus physical:** PASS. The 3,884 templates and 357 affine maps are an upper vocabulary for actual clean corridors; their individual realizability is not asserted.
- **Phase location:** PASS. The normalized x coordinates are physical normalized states from the inherited strict p-shift chain; grid counting uses only actual shallow states.
- **Historical barriers:** PASS. No rank-only, inverse-rank, generic lattice, blind odd-modulus, or RL173 physical route is revived.
- **No false closure:** PASS. The surviving high type and all global gates remain open.

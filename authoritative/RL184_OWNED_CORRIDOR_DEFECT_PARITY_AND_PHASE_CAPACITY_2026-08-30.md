# RL184 — owned-corridor defect parity, mechanical vocabulary, and phase capacity

Date: 2026-08-30

## 0. Outcome and classification

RL184 continues the sole surviving zero-height high type

`(v,H,J,d)=(37,0,23,-1)`.

It does **not** exclude that type, close the preferred `h_p=0` branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

The session turns RL183's physical successor corridors into three stronger global restrictions.

First, the chronological mechanical word is not an arbitrary binary word: its exact Sturmian factor structure sharply reduces the physically relevant three-transition height/map vocabulary. Second, the affine-map intercept is identified with the physical corrected-flow defect term, and exact finite enumeration shows that three-step intercept cancellation cannot hide a nonzero defect. Third, the homogeneous zero-defect recurrence has a finite dyadic lifetime from every `h<=1` start. This forces a certified global incidence of nonzero defects inside the physical 40-edge successor corridors.

Independently, RL181's strict p-rank gap chain upgrades RL183's width-`1/3` mechanical overlap from a shallow-grid bound to a **one-state global overlap**.

Promoted results:

1. **RL184.1 — one-state mechanical overlap and strict late compartment** (analytic). In p-shift rank order the normalized physical states are strictly increasing, and every adjacent normalized p-gap is greater than `128,081,997,553`. RL183 places every `c=1` state below `4m/3` and every `c=2` state at or above `(4m-1)/3`. The possible class-overlap interval therefore has width only `1/3`, so it contains at most one physical state in the entire cycle. Since the exact mechanical rank threshold is `R=57,079,296,007`, only the first late rank `r=R` can possibly lie below `4m/3`; every late rank `r>R` lies strictly above `4m/3`.

   Consequently the RL183 shallow late-state floors sharpen to at least

   - `16,722,313,937` states with `h<=1` at or above `4m/3`;
   - `24,526,523,998` states with `h<=2` at or above `4m/3`;
   - `27,725,426,286` states with `h<=3` at or above `4m/3`;
   - `29,184,838,816` states with `h<=4` at or above `4m/3`.

2. **RL184.2 — exact chronological mechanical factor restriction** (analytic + exact finite certificate). Put `B=A-L=80,448,749,305`. The chronological mechanical bit is
   `c_i=1` or `2` according as the mechanical residue lies below or above the threshold `R=L-B`. Advancing one chronological phase rotates the residue by `B (mod L)`. The only length-three mechanical words are

   `121, 122, 212, 221`.

   Restricting RL183's necessary local height enumeration to those actual words reduces the three-transition vocabulary from `3,884` templates to `1,818`, and the composite affine-map vocabulary from `357` maps to `270`.

   The inherited clean-corridor floor `10,075,174,571` is unchanged. Hence some necessary three-transition template is physically used at least

   `5,541,901`

   times, and some composite three-transition affine numerator map is physically used at least

   `37,315,462`

   times.

3. **RL184.3 — affine intercept equals the physical defect-flow sensor** (analytic). On a clean common-mechanical p-pair transition with endpoint heights `(a,b)`, let `M=max(a,b)`, `G=a-b`, and

   `D=2^(M-b)-2^(M-a)`.

   RL183 gives
   `2^d C' = 3C + D`.

   Since `q_i=rho_i 2^-a`,

   `q_i(2^G-1) = rho_i(2^-b-2^-a) = rho_i 2^-M D`.

   Thus `D` has exactly the sign of the corrected physical defect flow and vanishes exactly when `G=0`. The finite three-transition enumeration over the four actual mechanical words contains `210` zero-intercept templates and only `4` distinct zero-intercept composite maps; in every such template all three one-step defects are zero. No nonzero signed defect pattern cancels to a zero three-step affine intercept inside this necessary vocabulary.

4. **RL184.4 — finite zero-defect lifetime from shallow starts** (analytic + exact integer certificate). Along a clean run with `G_j=0`, the affine law is homogeneous:
   `2^d_j C_(j+1)=3C_j`, with `d_j>=1`.
   Therefore an n-step zero-defect run satisfies

   `2^(d_0+...+d_(n-1)) C_(i+n)=3^n C_i`.

   An ordinary `h<=1` start satisfies
   `0<C_i<2*293,591,818,782=587,183,637,564<2^40`.
   Since every `d_j>=1`, forty consecutive zero-defect transitions are impossible.

   The extremal 39-zero case is rigid. Divisibility forces
   `C_i=2^39`, every `d_j=1`, and the start cannot have endpoint heights `(0,0)` because `2^39` already exceeds the universal normalized-gap ceiling. Hence the initial endpoint type is `(1,1)`.

   In any actual 39-transition mechanical factor the number of late bits is either `22` or `23`. If it were `22`, the terminal normalized gap would be
   `3^39/2^23 > 293,591,818,782`,
   contradicting RL181's universal gap ceiling. Thus there are exactly `23` late bits, the terminal common height is `24`, and

   `C_(i+39)=3^39`.

   This terminal numerator is odd, so RL183's parity sensor forces `G_(i+39) != 0`.

5. **RL184.5 — global nonzero-defect incidence inside owned physical corridors** (analytic combinatorics + exact integer certificate). Start from the inherited `10,075,174,577` ordinary `h<=1` p-edges. To obtain 40 ordinary consecutive edges, remove at most 39 starts for future carry crossings. To make all first 39 pair transitions common-mechanical, remove at most 39 starts for the unique ordinary mechanical-switch p-rank. Therefore at least

   `10,075,174,499`

   clean 40-edge physical corridors remain.

   By RL184.4 every such corridor contains a nonzero defect among its 40 p-edges. Any fixed physical p-edge can belong to at most 40 such length-40 windows, so there are at least

   `251,879,363`

   **distinct physical nonzero-defect phases** in the surviving high branch.

This is the requested global consumer: the large successor family can no longer be filled by arbitrarily long zero-defect/homogeneous-map behavior. The result still does not quantify the positive-versus-negative compensation strongly enough to violate the inherited K-corridor or shallow width quotas.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`,
`Ap-uL=1`, `t=L-p=72057431991`.

Retain RL183 in full, especially:

- at least `10,075,174,577` ordinary `h<=1` p-shift starts;
- the universal normalized gap corridor
  `128,081,997,553 < delta < 293,591,818,782`;
- the common-mechanical successor law
  `2^d C'=3C+D`, `d>=1`;
- the binary/ternary sensor `2|C <=> G=0`;
- the clean three-transition floor `10,075,174,571`;
- the mechanical threshold
  `R=57,079,296,007`;
- the p-rank chain order and RL183 phase-location split;
- all ternary ownership and scope restrictions.

All statements remain internal to `(37,0,23,-1)`.

## 2. One-state phase overlap

RL181 proves that p-shift rank order is the strict normalized chain from `m` to `2m`, and every adjacent normalized gap exceeds `128,081,997,553`.

RL183 proves

- `c=1 => x<4m/3`;
- `c=2 => x>=(4m-1)/3`.

The only possible overlap has width `1/3`. Two physical p-rank states cannot both lie in such an interval because their normalized separation exceeds `128,081,997,553`.

The exact mechanical split is contiguous in p-rank:
`c=1` for `0<=r<R`, `c=2` for `R<=r<L`.
Since x increases strictly with r, if any late state lies below `4m/3` it must be the first late state at rank R. This proves RL184.1 and replaces RL183's cutoff-dependent overlap caps by one global exceptional state.

## 3. Actual three-step mechanical vocabulary

Write `A=L+B` with
`B=80,448,749,305`.
The chronological mechanical sequence is the binary rotation word generated by residue advance `r -> r+B (mod L)`, with bit 2 on `[R,L)` and bit 1 on `[0,R)`.

Partitioning the residue circle by the three preimages of the threshold R gives exactly the four length-three words

`121, 122, 212, 221`.

The bundled verifier applies RL183's necessary height-rise ranges
`0<=a'<=a+c-1`, `0<=b'<=b+c-1`
only along those four words. It obtains exactly `1,818` necessary three-transition templates and `270` composite affine maps.

This remains a one-way necessary vocabulary. It is not a claim that every listed template or map is physically realized.

## 4. Signed intercept and three-step cancellation

For a clean ordinary p-edge, `G=a-b` and `M=max(a,b)`. Therefore

`2^-M D = 2^-b-2^-a`.

Multiplying by rho gives the exact corrected-flow identity in RL184.3. In particular:

- `D>0 <=> G>0`;
- `D=0 <=> G=0`;
- `D<0 <=> G<0`.

The exact four-word enumeration composes the affine transitions with rational arithmetic. Among the zero composite-intercept templates, every one-step D is zero. Thus short map cancellation cannot conceal a nonzero signed defect over three clean transitions.

## 5. Zero-run rigidity

If every defect in n consecutive clean transitions vanishes, then every D vanishes and repeated substitution gives

`C_(i+n)=3^n C_i / 2^Dsum`,
where `Dsum=sum d_j>=n`.

At an `h<=1` start, `C_i<587,183,637,564<2^40`; since C is a positive integer, its 2-adic valuation is at most 39. Hence n cannot reach 40.

For n=39, integrality and positivity force equality throughout:

- `v_2(C_i)=39`;
- `C_i=2^39`;
- every `d_j=1`.

The `(0,0)` height type is impossible because its normalized gap would equal C and exceed the inherited gap ceiling. Thus the start is `(1,1)`.

With `d_j=1` and zero defect, the common height obeys
`M_(j+1)=M_j+c_j-1`.
The number of c=2 bits in a length-39 mechanical factor is either
`floor(39B/L)=22` or `ceil(39B/L)=23`.
The 22 case would give terminal height 23 and normalized gap `3^39/2^23`, which is too large. Therefore the terminal height is 24 and the numerator is `3^39`, which is odd. The terminal edge is ordinary, so `G=0` would require an even numerator. Hence the 40th edge has nonzero defect.

## 6. Incidence consequence and remaining barrier

The carry and ordinary common-mechanical switch each have one source. Removing their possible locations across the 39 transitions of a 40-edge window costs at most 78 starts in total, giving the promoted `10,075,174,499` clean corridors.

Each corridor must contain at least one nonzero defect. A single defect phase can cover at most 40 corridor starts, proving the global distinct-incidence floor `251,879,363`.

This is a genuine physical restriction, but it is not yet a quota-breaking signed-flow theorem. The next consumer should separate those forced nonzero defects by sign and mechanical phase, then use

`K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`

and/or the shallow-width requirements to show that the necessary compensation cannot fit inside the inherited K corridor.

## 7. Red-team scope

- **Incoming authority:** no historical replay beyond current dependencies.
- **Actual versus arbitrary c-words:** only factors of the exact mechanical rotation are used.
- **Necessary versus physical:** template/map enumeration remains an upper vocabulary only; physical repetition follows solely by pigeonhole from clean physical corridors.
- **Signed intercept:** the corrected physical `2^G` flow is used; RL173's auxiliary `3^-G` quantity is not revived.
- **Zero-run divisibility:** only clean ordinary common-mechanical transitions are multiplied; carry/switch starts are removed before incidence counting.
- **39-run rigidity:** the universal normalized-gap ceiling is used to exclude the 22-late-bit case; no unproved backward height bound is used.
- **Incidence:** overlapping windows are handled by the conservative multiplicity cap 40.
- **Phase overlap:** the global one-state cap uses the inherited strict p-rank gap lower bound, not lattice counting.
- **Scope:** every new numerical floor remains internal to `(37,0,23,-1)`.
- **No false closure:** the surviving high type, preferred branch, Gate A/B, non-trivial-cycle exclusion, and Collatz remain open.

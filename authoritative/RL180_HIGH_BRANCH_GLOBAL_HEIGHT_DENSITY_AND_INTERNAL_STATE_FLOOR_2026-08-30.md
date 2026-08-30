# RL180 — high-branch global height density and internal state floor

Date: 2026-08-30

## 0. Outcome and classification

RL180 continues the sole zero-height `v=37` high type inherited from RL179,

`(v,H,J,d)=(37,0,23,-1)`, with `g_p=2^37`.

It does **not** close that type, the preferred `h_p=0` branch, Gate A, Gate B, global non-trivial-cycle exclusion, or Collatz.

The main advance is that RL178's residue-localized corrected-flow deficit can be spliced to the older mechanical mass loss. This turns the high branch from a local multi-support problem into a global height-profile problem and, in this branch only, supplies an internal least-state floor stronger than the previously inherited external computational floor.

Promoted results:

1. **RL180.1 — delayed positive-flow support** (analytic + exact finite certificate). The ten RL179 phase-29 histories remain globally below `1/3` through phase 31. The exact maximum is
   `64458869178368/205891132094649 < 1/3`.
   Hence every physical high continuation needs a positive corrected-flow phase at index at least 32. Six phase-29 roots require at least three such positive phases at indices at least 32; the root `(0,3,2144699292643)` requires at least four. For that root, exact necessary propagation forces at least four positive phases from 34 onward, three from 36 onward, two from 38 onward, and one from 40 onward.
2. **RL180.2 — deficit / mechanical-loss splice** (analytic). With RL178 residue notation,
   `D=rho_t-F2` and `W:=R-Q=sum_r omega_r(1-2^-H_r)`. Each adjacent residue gap is either `s` or `s+Delta`, so
   `D/(exp(s+Delta)-1) < W < D/(exp(s)-1)`.
   The exact interval certificate gives the safe numerical window
   `23,493,381,795 < W < 28,070,867,755`.
3. **RL180.3 — global support band** (analytic inequalities + exact rational certificate). If
   `N_+=#{r:H_r>0}`, then
   `26,724,850,253 <= N_+ <= 88,981,261,496`.
   Therefore at least `48,546,783,816` residues have height zero.
4. **RL180.4 — internal least-state band for the high branch** (analytic inequalities + exact rational certificate):
   `2^74 < m < 3*2^73`.
   No external least-cycle computation is used.
5. **RL180.5 — internal shallow-population floors** (analytic capacity inequality + exact rational certificate):
   `#{h<=1} >= 73,801,609,945`,
   `#{h<=2} >= 81,605,820,006`,
   `#{h<=3} >= 84,804,722,294`,
   `#{h<=4} >= 86,264,134,824`.
   These reuse the RL135 mechanical top-weight method, but their premise is now internal to this high branch.
6. **RL180.6 — normalized physical pair-gap potential** (analytic). Put `z_i=q_i y_i` and, for the carry-free p-shift window, `K_i=e^s z_(p+i)-z_i`. Then
   `K_0=g_p` and
   `K_(i+1)-K_i=(1/3) q_i(2^G_i-1)`.
   Thus the local corrected-flow budget is exactly the drift of a normalized physical pair gap.

The mod-16/mod-32 odd-part continuation was also inspected. It refines valuation depth after the RL179 mod-8 sieve but did not produce a second immediate forbidden residue class. No stronger odd-part exclusion is promoted from that lift.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`,
`t=L-p=72057431991`.

Let

`Delta=A log 2-L log 3 >0`, `lambda=exp(Delta)`,
`s=p log 3-u log 2 >0`,
`b_i=floor(Ai/L)`, `h_i=b_i-S_i>=0`,
`q_i=2^S_i/3^i`, `rho_i=2^b_i/3^i`.

RL179 supplies the sole high zero-height type `(37,0,23,-1)`, `g_p=2^37`, and
`F2=3(lambda-1)2^37 >1/3`.

RL178 supplies the exact necessary pair-state transition law and, in residue order `r=A i (mod L)`,

`F2=rho_t-D`,
`D=sum_(r=1)^(L-1) (omega_(r-1)-omega_r)(1-2^-H_r)`.

The weights satisfy `1=omega_0>...>omega_(L-1)=rho_t`.

## 2. Exact phase-31 budget and delayed support

The RL179 exact high start at phase 24 is `(h,hp,C)=(0,1,3^24)`. Reapplying the RL178 valuation transition law gives the inherited ten distinct necessary states at phase 29.

RL180 propagates only those ten histories through phase 31, adding the exact corrected-flow term at each phase. There are 62 necessary histories through the phase-31 budget. Their largest cumulative value is

`64458869178368/205891132094649`,

which is strictly below `1/3`.

Since every physical continuation is contained in the necessary automaton and the high branch has `F2>1/3`, a positive term is mandatory at phase 32 or later.

Root-by-root, six histories still need more than two units of later net positive compensation after phase 31. Because RL178's residue ordering gives every individual positive corrected-flow term `<1`, each of those roots needs at least three positive phases at index at least 32. The root

`(0,3,2144699292643)`

still needs more than three units and therefore needs at least four.

The same exact filter, applied only to that worst root, gives:

- through phase 33, the remaining deficit is greater than 3: at least four positive phases at index `>=34`;
- through phase 35, greater than 2: at least three at `>=36`;
- through phase 37, greater than 1: at least two at `>=38`;
- through phase 39, still positive: at least one at `>=40`.

These are necessary-interface statements. Surviving automaton states are **not** promoted as physically realizable cycle states.

## 3. Global deficit / mass-loss splice

Let `i_r=pr mod L`, `H_r=h_(i_r)`, and `omega_r=rho_(i_r)`. For `r<L-1`, increasing the residue by one advances phase by `p` modulo `L`. The ratio `omega_(r-1)/omega_r` is exactly one of

`exp(s)` or `exp(s+Delta)`.

Put `u_r=1-2^-H_r`. Then

`W:=R-Q=sum_r omega_r u_r`,

whereas RL178 gives

`D=sum_(r=1)^(L-1) omega_r (exp(alpha_r)-1) u_r`,

with `alpha_r in {s,s+Delta}`. Positivity gives

`D/(exp(s+Delta)-1) < W < D/(exp(s)-1)`.

In the high branch,

`D=rho_t-3*2^37*(lambda-1)`,
`rho_t=exp(Delta+s)/2`.

The bundled rational interval verifier certifies the displayed integer window for `W`.

## 4. Positive-height support band

For a positive height, `1/2 <= u_r <1`.

For the upper support bound, the smallest possible mechanical mass carried by `N` positive residues is obtained by placing them at the smallest residue weights and taking the factor `1/2`. The exact base envelope

`2^(-r/L) <= omega_r`

then excludes `N=88,981,261,497` against the certified upper bound on `W`.

For the lower support bound, split adjacent residue gaps into their two exact species. There are decreasing large-gap and small-gap coefficient sequences. The certificate majorizes each by a decreasing geometric sequence, proves the discrete maximizing split for `N=26,724,850,252`, and shows even that maximal deficit is below the certified `D`. Hence one more positive-height residue is necessary.

This is a theorem about the transported height profile, not an assertion that an arbitrary profile is physically owned.

## 5. Internal least-state band

The mechanical residue weights have the exact envelope

`2^(-r/L) <= omega_r < exp(Delta) 2^(-r/L)`.

Therefore their total mass `R` is trapped by a geometric series. Since

`Q=R-W=3(lambda-1)m`,

the certified `W` interval immediately yields

`2^74 < m < 3*2^73`.

This internalizes the old external `m>=2^71` premise only **inside this surviving high branch**. It is not a new unconditional computational minimum for all Collatz cycles.

## 6. Shallow populations

For `M=2^(k+1)`, if only `N` phases have `h<=k`, then the q-mass satisfies

`Q <= R/M + (1-1/M) * (sum of the N largest mechanical weights)`.

RL135 used the same capacity mechanism with the inherited external lower floor. RL180 inserts the new internal high-branch lower bound for `Q=3(lambda-1)m` and the exact mechanical geometric envelope. The bundled verifier certifies the four displayed lower populations.

The old RL168/RL169/RL170 rank and chain barriers were selectively checked. The stronger `m` floor does not revive them: RL169's direct chain comparison scales by `m` on both sides, and the RL170 universal rank slack becomes no tighter as `m` increases.

## 7. Normalized physical pair-gap potential

The ordinary accelerated affine increment is

`z_(i+1)-z_i=q_i/3`, where `z_i=q_i y_i`.

Before the mechanical p-shift wrap,

`q_(p+i)/q_p=q_i 2^G_i`, and `q_p=exp(-s)`.

Define

`K_i=exp(s) z_(p+i)-z_i`.

Then

`K_0=y_p-y_0=g_p`,

and direct subtraction of the two affine increments gives

`K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`.

Thus three times the drift of `K` over an interval is exactly the corrected-flow budget on that interval. This is a physical pair-gap coordinate, not the demoted RL173 `3^-G` auxiliary functional.

## 8. Odd-part higher lift and barrier

The RL179 mod-8 sieve remains authoritative. Inspecting the next mod-16/mod-32 valuation depth separates zero-return classes more finely, but does not remove a second odd residue class uniformly at the tested depth. The four `c=2` zero-height indices were also checked at the same local-transition level. No new closure-grade sieve is promoted.

Status: retain the RL179 sieve; freeze “blindly raise the odd modulus without another global consumer” as a low-priority subroute.

## 9. Red-team scope

- **Exact arithmetic:** PASS. The two fast certificates use integer/Fraction arithmetic and rigorous rational transcendental enclosures.
- **Necessary versus physical:** PASS. The phase automaton is only a one-way necessary filter.
- **Residue versus physical ownership:** PASS. The support theorem constrains the height profile of an assumed physical cycle; it does not promote residue classes to states.
- **External provenance:** PASS. The new high-branch `m` band and shallow populations use no external least-cycle computation.
- **Coordinate correction:** PASS. Only the corrected `2^G` physical functional is used; RL173's `3^-G` quantity remains auxiliary.
- **Historical barriers:** PASS. RL168-RL171 are not reopened merely because the state floor increased.
- **No false closure:** PASS. The high branch remains open.

## 10. Strategic handover

RL181 should not expand the bounded phase BFS merely because it is available. The strongest simultaneous data are now global:

- a two-sided positive-height support band;
- a very large internally certified shallow population;
- a tight internal least-state band; and
- an exact physical pair-gap potential whose drift is the corrected flow.

The next attack should seek an independent packing, spacing, divisibility, or ownership theorem that couples at least two of those structures and conflicts with the surviving `(37,0,23,-1)` branch. Preserve all correction, provenance, and one-way-filter qualifications.

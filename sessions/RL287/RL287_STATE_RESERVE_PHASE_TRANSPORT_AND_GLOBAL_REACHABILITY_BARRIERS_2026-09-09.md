# RL287 — state reserve, 2-adic phase transport, and local closure barriers

Date: 2026-09-09

Primary classification:

`STATE_RESERVE_PHASE_TRANSPORT_AND_GLOBAL_REACHABILITY_BARRIERS_PROVED`

Gate A is **not closed**. The exact inherited residual remains

`k>=25`, `k` odd, `H_can<k`.

The preferred sufficient theorem remains

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`,

or equivalently RL285's all-depth candidate

`nu_2(K-1)<=H+d-1`

with `K=J+2^d-1`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and outcome

RL287 inherited RL286's theorem

`C_E/2^L = D_E/Q_out`

for every genuine positive first-return excursion and the one-zero obstruction

`C_E/2^h=(3/2)^h-1`.

The mission was to find a state-dependent reserve transported through positive boundary/checkpoint dynamics.

RL287 succeeds in identifying the available scalar reserve structures exactly, but also proves that none of the local scalar or local phase mechanisms can close Gate A. The unresolved information is the globally selected 2-adic lift determined by the complete canonical history from the fixed seed.

## 2. Boundary quotient for one-zero output

Let a one-zero first-return excursion of height `h` take positive even checkpoint `J_in` to positive output `J_0`. The inherited exact law is

`3^h(J_in+4)=2^h(2J_0+3)`.

Let an arbitrary legal positive zero-height boundary suffix `w` of length `L`, weight `r`, and affine constant `C_w` carry `J_0` to `J`. Then

`2^L J = 3^r J_0 + C_w`.

Define

`N_w(J)=2^(L+1)J-2C_w+3^(r+1)`.

Then exactly

`N_w(J)=3^r(2J_0+3)`.

Hence the normalized quotient

`G_w(J)=N_w(J)/3^r`

is invariant through the entire boundary suffix and equals

`G_w(J)=2J_0+3=(J_in+4)(3/2)^h`.

Also

`nu_3(N_w(J))-r = h+nu_3(J_in+4)`.

For a one-zero excursion,

`D_E/Q_out = (1/2)((3/2)^h-1)`,

so

`1+2D_E/Q_out = G_w(J)/(J_in+4)`.

This identifies the unbounded normalized one-zero defect as relative growth of an exactly boundary-transported arithmetic quotient.

Classification:

`ONE_ZERO_BOUNDARY_QUOTIENT_DEFECT_RESERVE_IDENTITY_PROVED`.

This is not a Gate-A closure because the next component can reset the relevant 2-adic phase.

## 3. Unique affine positive reserve and exact ledger

Define

`Pcal(J,Q)=Q(2J+3)/5`.

Among affine potentials `Q(J+c)`, one-zero height dependence disappears uniquely at `c=3/2`; the above normalization gives the exact one-zero law

`Pcal_out-Pcal_in=Q_in`.

For an arbitrary genuine first-return excursion,

`5 Delta Pcal = 4S_E+2D_E+Q_out-Q_in`.

Using the inherited nested-zero inequality gives

`Delta Pcal >= S_E`,

with equality exactly for one-zero excursions, and

`Delta Pcal >= D_E+Q_out/2`,

again with equality exactly for one-zero excursions.

The exact surplus is

`Delta Pcal-D_E-Q_out/2
 = (1/5) sum_(j=2)^z c_j
   +(3/5) sum_(j<z) c_j(2/3)^(h_j)`.

On a positive odd zero-height boundary state:

- `x=0`: `Delta Pcal=Q`;
- `x=1`: `Delta Pcal=-Q/15`.

Thus for an arbitrary positive boundary segment,

`Delta Pcal_bdry = S_bdry - T_1/15`

where `T_1` is the sum of incoming scales over boundary `x=1` columns.

Therefore a full positive checkpoint block obeys

`Delta Pcal_block + T_1/15 >= S_block`.

Classification:

`STATE_DEPENDENT_AFFINE_DEFECT_RESERVE_LEDGER_PROVED`.

Integrity note: `Pcal=(4/5)B+(1/5)Q`; it is not an independent global scalar constraint.

## 4. Global Ferrers reserve is exactly the inherited coupon defect

At an equal-weight `d=1` paired prefix of length `n`, let

`Delta = W_x-W_y`

be RL285's global shifted-shadow/Ferrers difference and let the current physical scale be `Q=2^n/3^r`.

Define

`R_F = Q Delta / 2^n`.

A diagonal zero-height boundary column transports `R_F` exactly:

- `00`: `Delta` is unchanged while `Q` and `2^n` both double;
- `11`: `Delta` is multiplied by `3`, while `Q` is multiplied by `2/3` and `2^n` doubles.

For a genuine first-return excursion `E`, shifted-shadow concatenation and RL286's component bridge give

`R_F,out-R_F,in = D_E`.

Termwise Ferrers/zero-rank expansion yields the stronger identity

`R_F = D`

for the accumulated global coupon defect.

Classification:

`GLOBAL_FERRERS_DEFECT_RESERVE_IDENTITY_PROVED`.

This prevents double-counting: the natural boundary-invariant Ferrers reserve is not independent of the inherited defect.

## 5. Hybrid reserve ledger and scalar phase barrier

Let `Phi(w)=-Q_w/3^|w|_1`, so the accumulated defect is

`D=Phi(y)-Phi(x)`.

Put

`A_x=Phi(x)+7`,
`Lres=A_x+2D`.

For a genuine first-return excursion with zero weights `c_j` and local heights `h_j`,

`Delta Lres
 = sum_(j=1)^(z-1)
   [c_(j+1)-2c_j(2/3)^(h_j)]`.

Hence:

- one-zero excursion: `Delta Lres=0`;
- multi-zero excursion: `0<Delta Lres<S_E`.

On the zero-height positive boundary:

- `x=0`: `Delta Lres=0`;
- `x=1`: `Delta Lres=-Q/3`.

Thus one-zero components and boundary zeros transport the reserve exactly; boundary ones only spend it; multi-zero excursions are the only replenishment mechanism and that replenishment is strictly zero-mass priced.

However a fixed height-two, two-zero excursion can expose arbitrarily deep 2-adic hazard while all absolute scalar costs tend to zero at large phase depth. Therefore no local theorem bounding phase depth by height plus an absolute scalar debit of `F`, mass, defect, `Pcal`, or `Lres` can close Gate A.

Classification:

`HYBRID_PHASE_RESERVE_LEDGER_AND_VANISHING_COST_RESET_BARRIER_PROVED`.

## 6. General 2-adic cylinder-isometry theorem

The decisive structural theorem is not limited to first-return excursions.

Take any fixed legal canonical segment of length `L`. Every canonical column has the form

`J_(i+1)=(c_i J_i+q_i)/2`

with `c_i` odd. Composition gives

`2^L J_out = c J_in + b`

with odd `c` and segment-dependent integer `b`.

If one input `J_*` realizes this segment, then every

`J_*+2^L t`

realizes exactly the same depth/parity itinerary. At prefix `i<L`, the perturbed trajectory differs by an even multiple

`c_i^* 2^(L-i)t`,

so all required parity choices are unchanged.

At the endpoint,

`J_out(J_*+2^L t)=J_out(J_*)+c t`.

Since `c` is odd, the higher lift is transported by a 2-adic affine isometry.

For a first-return excursion with common weight `r`, `c=3^r`.

Consequences:

1. a fixed segment fixes exactly its low legality cylinder modulo `2^L`;
2. imposing `v` further output phase bits selects exactly `v` further input-lift bits;
3. arbitrarily deep output phase is transported from higher input bits, not created by local component height or cost.

Classification:

`GENERAL_2ADIC_SEGMENT_CYLINDER_ISOMETRY_PROVED`.

This theorem explains the repeated local reset families and identifies the missing variable as the globally selected cylinder lift.

## 7. Height-bounded non-boundary skeleton

Decompose a canonical path into zero-height `d=1` boundary segments and genuine first-return excursions `E_i` of heights `h_i` and lengths `L_i`.

All accumulated height is carried by the excursions:

`H=sum_i h_i`.

Every excursion has `h_i>=1`, so the number of excursion components `m` satisfies

`m<=H`.

For a first-return excursion, after the zero-cost launch every pre-return column begins at depth at least two, hence

`L_i-1<=h_i`.

Therefore

`sum_i L_i <= H+m <= 2H`.

Thus a height-`H` trajectory has:

- at most `H` first-return excursions;
- at most `2H` non-boundary columns;
- at most `H+1` intervening zero-height boundary macros.

Classification:

`GLOBAL_HEIGHT_BOUNDED_NONBOUNDARY_SKELETON_PROVED`.

The remaining unbounded combinatorics are entirely in the boundary macros.

## 8. Universal low-height direct-terminal local predecessors

The height-bounded skeleton does not control terminal exponent.

For the depth-two normal form

`x=0^z 1`,
`y=1 0^z`,
`h=z`,

the exact endpoint equation is

`2^(z+1)J_out = 3J_in + 5*2^z - 4`.

Setting `J_out=2^k` gives

`J_in(k,z)=(2^(k+z+1)-5*2^z+4)/3`.

For every odd `k>=3`, choose:

- `z=2` when `k mod 6` is `1` or `5`;
- `z=4` when `k mod 6` is `3`.

Then `J_in` is positive, even, locally legal, and lies in the inherited admissible `d=1` mod-3 class `{0,2}`. The genuine excursion returns directly to `2^k` with height at most four.

Its entry scale, zero mass, defect, and `F` increment all tend exponentially to zero as `k` grows.

Therefore every residual odd terminal exponent admits a locally legal, mod-3-admissible height-`<=4` direct predecessor. Such inputs are not claimed globally reachable.

Classification:

`UNIVERSAL_LOW_HEIGHT_DIRECT_TERMINAL_LOCAL_PREDECESSOR_BARRIER_PROVED`.

## 9. Residual boundary-one contraction

Let `m0=n-r` denote the global number of `x` zeros. RL279 gives

`X=2^(n+k+1)/3^r`,
`27<X<160/3`,

and the inherited residual has `m0>=8`.

Put `beta=log_2(3/2)`.

Then exactly

`beta r = m0+k+1-log_2 X`.

Inside all first-return excursions, the total number of `x=1` columns is at most `H`. Hence a Gate-A violator with `H<=k-1` must have zero-height boundary-one count

`r_bdry > (1/beta-1) k + 6.578...`

i.e.

`r_bdry > 0.709511 k + 6.578`.

Also

`r_bdry-z_bdry > 0.709511 k - 1.422`.

This is a genuine global contraction, but it does not close Gate A.

Classification:

`RESIDUAL_BOUNDARY_ONE_SURPLUS_LINEAR_LOWER_BOUND_PROVED`.

## 10. Arbitrary boundary surplus with globally bounded hazard

Write the positive boundary conjugate state as `n=(J-1)/2`, with retained map

`C(n)=n/2` for even `n`,
`C(n)=(3n+1)/2` for odd `n`,

and complementary exit

`E(n)=3n+2` for even `n`,
`E(n)=n+1` for odd `n`.

For every `N>=1` and positive odd `u`, put

`n_0=2^(3N)u-5`.

The first `3N` retained boundary bits are exactly

`(110)^N`.

Thus this zero-height transient contains `2N` boundary ones and `N` boundary zeros, with scale multiplier `(8/9)^N`.

Every complementary exit along the transient has 2-adic valuation at most two.

Moreover, because `2` generates the units modulo every power of `3`, choose `s` with

`2^s == -5 (mod 9^N)`

and put

`u=(2^s+5)/9^N`.

Then after the `(110)^N` transient the retained state is exactly `2^s`, after which the orbit falls into the trivial positive boundary cycle. The entire future boundary hazard satisfies

`Beta(n_0)=3`.

Therefore arbitrarily large zero-height boundary-one surplus, arbitrarily strong `(8/9)^N` scale contraction, and deletion of neutral cycles do not force a deep boundary hazard.

Classification:

`ARBITRARY_BOUNDARY_SURPLUS_WITH_GLOBAL_BETA_THREE_BARRIER_PROVED`.

These boundary origins are local positive-boundary examples; they are not claimed globally reachable from the canonical seed.

## 11. Unpromoted finite evidence

During RL287 scratch work, the inherited exact `H<=22` positive-checkpoint set was used as a falsification oracle. A proposed odd-quotient phase inequality survived that finite set, but no global proof was obtained and the result is not needed by any promoted RL287 theorem.

It remains:

`UNPROMOTED_FINITE_EVIDENCE_ONLY`.

No residual bound is narrowed by it.

## 12. Strategic conclusion

RL287 identifies and exhausts the natural local reserve architecture:

- boundary quotient `G`: exact but component-reset sensitive;
- affine reserve `Pcal`: exact ledger but algebraically dependent;
- normalized Ferrers reserve: exactly the existing defect `D`;
- hybrid reserve `Lres`: locally sign-definite but defeated by vanishing-cost phase resets;
- local phase itself: transported isometrically through every fixed legal segment.

The decisive conclusion is:

**the remaining Gate-A obstruction is not a missing local reserve. It is the global selection of the high 2-adic cylinder lift by the complete canonical history from the fixed seed.**

The successor must return directly to RL285's fixed-seed global high-divisibility/sign theorem rather than extend the local reserve programme.

## 13. Verification

Portable verifier:

`sessions/RL287/verification/verify_rl287_phase_reserve.py`

checks on the same bounded first-return regression family used by RL281/RL286:

- 13,909 genuine first-return excursions;
- 199 one-zero excursions;
- exact affine `Pcal` excursion identities and inequalities;
- exact RL286 Ferrers/coupon bridge;
- fixed-excursion cylinder-isometry perturbation by `2^L`;
- direct-terminal height-2/4 families for odd `k` through 79;
- `(110)^N` low-hazard boundary families for `1<=N<=5`.

The verifier output is recorded in

`sessions/RL287/verification/RL287_FAST_VERIFIER_OUTPUT.txt`.

The proof-state/scope audit is

`sessions/RL287/verification/RL287_RED_TEAM.md`

and records PASS.

The verifier is regression support. The promoted results above are analytic.

## 14. Proof-state summary

Promoted analytic results:

- `ONE_ZERO_BOUNDARY_QUOTIENT_DEFECT_RESERVE_IDENTITY_PROVED`;
- `STATE_DEPENDENT_AFFINE_DEFECT_RESERVE_LEDGER_PROVED`;
- `GLOBAL_FERRERS_DEFECT_RESERVE_IDENTITY_PROVED`;
- `HYBRID_PHASE_RESERVE_LEDGER_AND_VANISHING_COST_RESET_BARRIER_PROVED`;
- `GENERAL_2ADIC_SEGMENT_CYLINDER_ISOMETRY_PROVED`;
- `GLOBAL_HEIGHT_BOUNDED_NONBOUNDARY_SKELETON_PROVED`;
- `UNIVERSAL_LOW_HEIGHT_DIRECT_TERMINAL_LOCAL_PREDECESSOR_BARRIER_PROVED`;
- `RESIDUAL_BOUNDARY_ONE_SURPLUS_LINEAR_LOWER_BOUND_PROVED`;
- `ARBITRARY_BOUNDARY_SURPLUS_WITH_GLOBAL_BETA_THREE_BARRIER_PROVED`.

Not promoted:

- the scratch `H<=22` odd-quotient phase inequality;
- any global boundary-hazard theorem;
- any new global checkpoint valuation theorem.

Open:

- global `nu_2(K-1)<=H+d-1`;
- equivalent fixed-seed positive high-divisibility sign theorem;
- checkpoint `nu_2(J)<=H`;
- Gate A exact residual `k>=25`, odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

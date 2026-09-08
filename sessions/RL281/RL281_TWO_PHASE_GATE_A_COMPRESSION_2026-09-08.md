# RL281 — two-phase Gate-A compression, gateway rigidity, and odd-k contraction

Date: 2026-09-08

## Classification

Primary:

`TWO_PHASE_GATE_A_COMPRESSION_PROVED`

Promoted subordinate results:

- `SHARP_EXCURSION_ZERO_MASS_ENVELOPE_PROVED`
- `POSITIVE_BLOCK_FULL_MASS_PRICING_PROVED`
- `DEPTH_TWO_EQUALITY_ENTRY_SCALE_SUPPRESSION_PROVED`
- `ONE_ZERO_2ADIC_HEIGHT_RIGIDITY_PROVED`
- `POSITIVE_BOUNDARY_ZERO_MASS_TELESCOPE_PROVED`
- `POSITIVE_PHASE_ZERO_MASS_CEILING_PROVED`
- `NEGATIVE_PHASE_DUAL_POTENTIAL_BUDGET_PROVED`
- `NEGATIVE_TO_POSITIVE_GATEWAY_DICHOTOMY_PROVED`
- `MOD3_REACHABILITY_INVARIANT_PROVED`
- `MINIMUM_POSITIVE_HEIGHT_THREE_PROVED`
- `K3_GATE_A_CASE_CLOSED_PROVED`

All items above are **proved analytic mathematics**. The portable verifier supplies regression checks and one exact finite closure certificate for the `H<=2` reachable state set.

Gate A remains open, but every hypothetical violator is now restricted to

`k>=5`, `k` odd, `H_can<k`.

Gate B is unchanged/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming state

RL281 inherits RL280's exact normalized state

`K=J+2^d-1`

with its four affine transitions, the zero weights

`c_t=2^(t-1)(2/3)^(u_t)`,

the exact endpoint identity

`Q_out K_out-Q_in K_in=2S_E+D_E`

for first-return excursions, the sharp defect envelope

`D_E >= q[1+((2^z-4)/3)(2/3)^(h-z)]`,

the unique depth-two equality family, the equality arithmetic relation, and the positive-checkpoint Lyapunov quantity

`F=Q(J+3)`,

with retained-terminal ceiling

`F_T<110/3`.

Also inherited are the global zero-mass corridor

`17/2<S<21`,

the exact terminal scale, the positive/negative boundary cycle scale-sign theorem, `J>0` forward invariance, and the dangerous-region contraction

`H_can<k => m0>=8 => z>=k+6`.

## 2. Sharp excursion zero-mass envelope

Consider a first-return excursion beginning at `d=1`, with entry scale

`q=Q_in=c_1`.

Let its zero-count be `z`, total height be `h`, local height increments be `h_j>=1`, and put

`s=h-z`.

RL280 gives the nested-zero inequality

`c_(j+1)>=3c_j(2/3)^(h_j)`.

Iterating and minimizing the resulting lower bound at fixed `(z,h)` gives

`boxed:
 S_E >=
 q[1+(2^z-2)(2/3)^(h-z)]`.

Equality is attained exactly when

`h_1=h-z+1`,
`h_2=...=h_z=1`

and all nested inequalities saturate, hence exactly in RL280's depth-two normal form

`x=0 1^(h-z) 0^(z-1) 1`,
`y=1^(h-z+1) 0^z`.

Thus the same depth-two family simultaneously minimizes the excursion zero mass and coupon defect.

## 3. Positive block full-mass pricing

At `d=1` put

`B=QK/2=Q(J+1)/2`.

Across a first-return excursion,

`B_out-B_in=S_E+D_E/2`.

On the zero-height positive boundary:

- an `x=0` column has zero weight `Q` and satisfies exactly
  `B'-B=Q`;
- an `x=1` column satisfies exactly
  `B'-B=0`.

Therefore every positive boundary zero is priced exactly by increase in `B`.

For a positive checkpoint block, let `F=Q(J+3)=QK+2Q`. If the first return is followed by any number of positive zero-height retaining columns and then the complementary exit to the next even-`J` checkpoint, monotonicity of `QK` on the boundary gives

`F_next-F_in > 2S_E+D_E-2q`.

Combining the mass and defect envelopes yields the explicit uniform cost

`boxed:
 F_next-F_in
 >
 q[1+((7*2^z-16)/3)(2/3)^(h-z)]`.

For `z>=2`, `D_E>=q` and `S_E>q`, so

`boxed:
 F_next-F_in > 2S_E-q > S_E`.

Hence every multi-zero positive excursion costs more `F` than its entire excursion zero mass, even after arbitrary positive neutral boundary transients are quotiented away.

For `z=1`, the guaranteed cost is exactly the one-zero coupon defect

`F_next-F_in > q(1-(2/3)^h)`,

whose weakest value is the inherited `q/3` limit at `h=1`.

## 4. Depth-two equality entry-scale suppression

For a positive depth-two equality excursion, put

`s=h-z`,
`w=2K_out-7`.

RL280 gives

`3^(s+1)(J_in+4)=2^(s+1)(8+2^(z-1)w)`.

For `z>=5`, positivity of the left side implies `w>=1`: if odd `w<=-1`, then

`8+2^(z-1)w <= 8-16 < 0`.

Also

`8+2^(z-1)w == 8 (mod 16)`,

so its exact 2-adic valuation is `3`. Therefore

`boxed:
 nu_2(J_in+4)=s+4`.

Consequently

`J_in+4 >= 2^(s+4)`

and, since `w>=1`,

`J_in+4 >= (2/3)^(s+1)(8+2^(z-1))`.

Balancing these opposite monotone bounds eliminates `s`. With

`beta=log_3(2)`,

`boxed:
 J_in+4 >= 8*2^(beta(z-4))`.

Using `Q_in(J_in+3)<110/3` at every positive checkpoint gives exponential suppression of the entry weight of the locally cheapest high-zero equality family.

## 5. One-zero rigidity

For `z=1`, RL280's equality relation specializes exactly to

`boxed:
 3^h(J_in+4)=2^h(2J_out+3)`.

Since `2J_out+3` is odd, whenever `J_in!=-4`,

`boxed:
 h=nu_2(J_in+4)`.

Thus the cheap one-zero channel has no independent height freedom.

Its exact word and scale are

`x=0 1^h`,
`Q_out=2(2/3)^h Q_in`.

At a positive checkpoint, the terminal `F` ceiling also gives

`Q_in < 110/[3(2^h-1)]`

for `h>=3`, with the small cases handled separately. Hence high-height one-zero excursions enter at exponentially small absolute scale.

## 6. Positive-phase zero-mass telescope

Let the first positive checkpoint occur at some positive even `J`.

Across every positive first-return excursion,

`Delta B=S_E+D_E/2`.

Across every intervening zero-height positive boundary segment, the total increase in `B` is exactly the sum of all `x=0` zero weights on that segment.

Therefore from the first positive checkpoint to the retained terminal,

`B_T-B_first
 =
 S_positive + (1/2)D_positive_excursions`,

where `S_positive` includes every zero weight in the positive phase, both off-boundary and on the zero-height boundary.

In particular,

`S_positive < B_T`.

At the terminal,

`B_T=X(1/4+2^(-k-2))`.

With `k>=3` and `X<160/3`,

`boxed:
 S_positive < B_T < 15`.

Thus positive neutral boundary cycles cannot hide unpriced zero mass.

## 7. Negative-phase dual potential budget

Use the inherited endpoint-potential family at `c=-2`. At `d=1`, define

`C=Q(J-1)=Q(K-2)=3 Phi_-2`.

Initially,

`C_0=-14`.

The quantity is globally nondecreasing. As long as a first return remains nonpositive, `J<=0`, hence `C<0`.

For any first-return excursion with entry scale `q`, the mandatory entry ascent at `d=1` contributes exactly

`Delta Phi_-2 = 5q/9`,

while every later contribution is nonnegative. Therefore

`boxed:
 C_out-C_in >= 5q/3`.

If `q_i` are the entry scales of all complete excursions which still return to nonpositive `J`, then

`boxed:
 sum q_i < 42/5`.

A complementary global identity follows from `B_0=-6`:

`B+6=S+D/2`.

Hence at any nonpositive even checkpoint:

- if `J<=-2`, then `B<0` and `S<6`;
- if `J=0`, monotonicity of `C` gives `Q<14`, hence `S<13`.

## 8. Exact negative-to-positive gateway dichotomy

For a one-zero excursion,

`3^h(J_in+4)=2^h(2J_out+3)`.

If `J_in<=-4`, the left side is nonpositive while a positive `J_out` makes the right side positive. Thus such a one-zero crossing is impossible.

If `J_in=-2`, then `h=1` and the equation forces

`J_out=0`.

Therefore

`boxed:
 J_in<0, J_out>0
 =>
 z>=2`.

Every direct strictly-negative-to-positive crossing is therefore in the multi-zero, fully mass-priced regime.

The unique cheap gateway is `J_in=0`. Then

`h=nu_2(4)=2`

and the exact equation forces

`J_out=3`.

Thus

`boxed:
 J=0 --x=011,h=2--> J=3`

with

`Q_out=(8/9)Q_in`.

This is the only positive one-zero first return from `J=0`.

## 9. Mod-3 reachability invariant and odd terminal exponent

The exact `J` transitions derived from the normalized recurrence are:

- fixed-depth even-`K`, `x=1`:
  `J'=(3J+2^d-1)/2`;
- fixed-depth even-`K`, `x=0`:
  `J'=(J+3^d-2^d)/2`;
- descending odd-`K`, `x=1`:
  `J'=J/2`;
- ascending odd-`K`, `x=0`:
  `J'=(3J+3^(d+1)-2^d-1)/2`.

Let `epsilon_d=(-1)^d == 2^d (mod 3)`. Direct substitution in the four cases proves the invariant

`boxed:
 J (mod 3) in {0,epsilon_d}`

for every reachable state. It holds at the initial state `(d,J)=(1,-13)`.

At a terminal `d=1,J=2^k`, the residue is nonzero, so it must equal `2 mod 3`. Therefore

`boxed:
 k is odd`.

No even terminal exponent is reachable.

## 10. Minimum positive height and closure of k=3

The exact height-zero boundary dynamics from the initial state contain the neutral cycle

`-13 -> -19 -> -9 -> -13`

with word `101`.

Its three alternative zero-height exits are

`-13 -> -6`,
`-19 -> -28`,
`-9 -> -4`.

A first-return excursion has `h>=z>=1`. The complete excursion word forms with total height at most two are:

- `h=1`: `x=01`;
- `h=2,z=1`: `x=011`;
- `h=2,z=2`: `x=001`.

Exact replay from the three height-zero exits shows that the only legal first return with `h<=2` is

`-6 --01--> -3`

with height `1`.

From `J=-3`, zero-height boundary motion may reach

`-3 -> -1 -> 0`

or exit again through `-4`, but cannot become positive. At `J=0`, the unique cheap gateway of Section 8 costs two further height units and reaches `J=3`.

Therefore

`boxed:
 d=1,J>0 => H_can>=3`.

A minimum-height sign-change core is

`(101)^p 00100 011`, `p>=0`,

which reaches `J=3` at exact height `3`; the leading negative neutral loops change scale but not height.

The portable verifier independently closes the entire reachable state set with `H<=2`: it contains exactly `28` states and no positive `d=1` state.

Since every retained terminal has `k>=3`, Section 9 forces odd `k`, and the present theorem gives `H_can>=3`, the entire lowest case closes:

`boxed:
 k=3 => H_can>=3=k`.

Thus any Gate-A violator must satisfy

`boxed:
 k>=5, k odd, H_can<k`.

## 11. Verification

Portable verifier:

`verification/verify_rl281_two_phase.py`

checks:

- preservation of the mod-3 reachability invariant on `7,017` exact legal transition regressions;
- exact closure of all reachable states with `H<=2`: `28` states, `31` retained edges, zero positive `d=1` states;
- `13,909` first-return excursions;
- `399` exact depth-two equality excursions;
- the new sharp zero-mass envelope and equality class;
- endpoint/B identities;
- the normalized negative `C` excursion increment floor `5/3`;
- `199` one-zero excursion regressions and exact valuation/return law;
- `1,889` negative-to-positive first-return excursions, all with `z>=2`;
- uniqueness of the `J=0 -> 3`, `x=011`, `Q`-factor `8/9` one-zero gateway;
- `45,170` positive-checkpoint block regressions;
- `44,158` multi-zero checkpoint block regressions satisfying the full-mass pricing theorem;
- terminal `F<110/3` and positive-phase `S<15` ceiling algebra.

The verifier passes cleanly.

## 12. Remaining obstruction

Gate A is not closed.

The live dangerous region has been contracted from arbitrary retained terminals to

`k>=5`, `k` odd, `H_can<k`.

The remaining task is no longer unrestricted positive/negative excursion classification. A successor should quotient the mandatory height-3 sign-change core and prove a scalable **height escalation law** for odd terminal exponents `k>=5`, preferably by coupling:

- the exact mod-3 state invariant;
- one-zero `nu_2(J+4)` rigidity;
- multi-zero positive full-mass pricing;
- the rigid `J=0 -> 3` cheap gateway;
- the terminal power-of-two condition `J_T=2^k`;
- the inherited zero-mass/coupon/terminal-scale constraints.

Further flat fixed-zero enumeration should remain secondary only.

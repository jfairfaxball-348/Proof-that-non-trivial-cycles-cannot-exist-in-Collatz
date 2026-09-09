# RL289 — fixed-seed ballot geometry, rejected tubes, mixed-coordinate barriers, and seam obstruction

Date: 2026-09-09

Closed classification:

`FIXED_SEED_BALLOT_BIJECTION_REJECTED_TUBE_AND_SEAM_BARRIERS_PROVED`

## 1. Scope and inherited target

RL289 worked only on the research-front Gate-A problem.

The incoming authority was:

`RL289_NORMALIZED_COMMON_SEED_SHADOW_PAIR_GATE_A_TARGET.md`

The inherited preferred sufficient theorem is:

for a genuine canonical state with

`K = J + 2^d - 1`,
`A = H + d - 1`,

prove

`J > 0  =>  nu_2(K-1) <= A`.

At `d=1` this becomes

`J > 0 even  =>  nu_2(J) <= H`.

The exact unresolved residual remains:

`k>=25`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

The inherited RL285 exhaustive certificate through `H<=22` is not duplicated or enlarged in this session.

## 2. Normalized joint pair after synchronized departure

Let the common first-deviation position from the seed itinerary `(101)^infinity` be `s`, let the current common word length be `n>s`, and put

`q=n-s`,
`R_x=U_x/2^s`,
`R_y=U_y/2^s`.

Both normalized shadow numerators are odd.

Define shifted normalized variables

`X=R_x+2^q`,
`Y=R_y+2^q`.

They satisfy the exact joint state identity

`3^d X - Y = 2^q K`.

Equivalently,

`2^q(K-1)=3^d X-(Y+2^q)`.

Appending one bit to a normalized shadow has the simple rule

- bit `0`: `Z' = Z + 2^q`;
- bit `1`: `Z' = 3Z`.

After the synchronized departure the three RL288 roots all have the same natural root-cancelling coordinate

`E = 3^(d-1) X - Y`.

At the forced first post-departure `01` column,

`E=6`.

Thereafter the four column recurrences are:

- `00`: `E' = E + (3^(d-1)-1)2^q`;
- `11`: `E' = 3E`;
- `01`: `E' = 3E + 3^d 2^q`;
- `10`: `E' = E - 2^q`.

For every post-departure prefix with `q>=2`,

`E == 2 (mod 4)`,

so

`nu_2(E)=1`.

Classification:

`ROOT_CANCELLING_NORMALIZED_JOINT_COORDINATE_HAS_FIXED_VALUATION_ONE_PROVED`

This is a route barrier: the unique natural linear coordinate that erases the three departure phases also erases the higher 2-adic information needed by Gate A.

## 3. Rational common-phase invariants collapse to the inherited defect

For a parity word `w`, write the shifted affine map

`F_w(z)=C_w(z)+1=a_w z+b_w`.

For a pair `(x,y)` define

`rho=a_y/a_x`,
`tau=(b_y-b_x)/a_x`.

Under simultaneous affine postcomposition these are complete rational orbit invariants.

More strongly, any rational function of the two affine-map coefficient pairs which is invariant under both actual common generators

`f_0(z)=(z+1)/2`,
`f_1(z)=3z/2`

is invariant under the full affine group and therefore factors through `(rho,tau)`.

At a balanced `d=1` equal-weight checkpoint,

`rho=1`

and

`tau=(Q_y-Q_x)/3^r`.

The inherited RL287 defect is

`D=(Q_x-Q_y)/3^r`,

so

`tau=-D`.

Classification:

`RATIONAL_FINAL_PAIR_COMMON_PHASE_INVARIANTS_COLLAPSE_TO_INHERITED_DEFECT_PROVED`

This rules out rational ratios/cross-products of final two-shadow affine coefficients as a new global selector.

## 4. Boundary phase-vector isometry and finite-suffix transparency

At a positive `d=1` boundary state use the RL287 conjugate

`n=(J-1)/2`.

The retained boundary map is

`C(n)=n/2` if `n` is even,

`C(n)=(3n+1)/2` if `n` is odd.

Its retained control bit is exactly `n mod 2`.

### Boundary phase-vector isometry

If `nu_2(n-m)=s`, then the retained parity sequences of `n` and `m` agree for exactly the first `s` bits and differ at bit `s`.

While their bits agree:

- even/even divides the difference by `2`;
- odd/odd multiplies the difference by `3/2`.

Hence the valuation drops by exactly one per retained step.

Therefore

`n mod 2^L  <->  first L retained boundary bits`

is a bijective 2-adic isometry.

### Periodic boundary cylinders

For a retained boundary word `w` of length `L` and weight `r`,

`C_w(n)=(3^r n+a_w)/2^L`.

It has unique 2-adic fixed point

`n_w=-a_w/(3^r-2^L)`.

For every `N>=1`,

the first `NL` retained bits are `w^N`

iff

`n == n_w (mod 2^(NL))`.

Also

`C_w^N(n)-n_w=(3^r/2^L)^N(n-n_w)`.

For `w=110`,

`C_110(n)=(9n+5)/8`,
`n_w=-5`.

Thus `(110)^N` is exactly the cylinder

`n == -5 (mod 2^(3N))`.

### Finite-suffix transparency theorem

Let `S` be any fixed legal canonical segment of length `L` ending at a positive odd `d=1` boundary state. RL287's cylinder-isometry gives

`2^L J_out = c J_in + b`

with `c` odd.

Writing a cylinder lift as

`J_in=J_*+2^L t`

gives

`J_out=J_out,*+c t`.

Restricting to odd output uses `t=2u`; then

`n_out=n_out,*+c u`.

Since `c` is odd, for every prescribed `N`-bit future boundary word there is exactly one `u mod 2^N`.

Therefore any fixed finite recent suffix is transparent to arbitrarily deep future boundary phase.

Classifications:

`BOUNDARY_PHASE_VECTOR_2ADIC_ISOMETRY_PROVED`

`PERIODIC_BOUNDARY_CYLINDER_NORMAL_FORM_PROVED`

`ANY_FIXED_RECENT_SUFFIX_IS_TRANSPARENT_TO_ARBITRARY_FUTURE_BOUNDARY_PHASE_PROVED`

The last statement is a decisive barrier to any proof using only a bounded recent-history window.

## 5. Fixed-seed parity-cylinder affine ballot bijection

For a word `w` of length `n` and weight `r`,

`C_w(z)=(3^r z+Q_w)/2^n`.

Let `zeta_w mod 2^n` be the unique residue whose first `n` ordinary half-step Collatz parity bits are exactly `w`:

`zeta_w == -Q_w 3^(-r) (mod 2^n)`.

Since

`U_w=-7*3^r+Q_w`,

we have

`U_w == -3^r(zeta_w+7) (mod 2^n)`.

For a genuine canonical pair `(x,y)` at common length `n`, with depth `d`, the exact paired-shadow integrality is

`3^d U_x-U_y == 0 (mod 2^n)`.

The weight relation is

`r_y-r_x=d-1`.

Substitution cancels the word-dependent powers of `3` and gives the fixed affine relation

`zeta_y == 3 zeta_x + 14 (mod 2^n)`.

Define

`A(z)=3z+14`.

It fixes `-7`:

`A(-7)=-7`

and

`A(z)+7=3(z+7)`.

Thus if

`z=-7+2^s u`

with `u` odd, then

`A(z)=-7+3*2^s u`.

This rederives the synchronized first-deviation theorem and shows that the normalized higher lift is one odd 2-adic unit `u`, paired with `3u`.

### Exact converse

Choose any residue `z mod 2^n`.

Let `x` be the first `n` parity bits of `z`, and let `y` be the first `n` parity bits of `A(z)`.

If every prefix satisfies

`#1(y_prefix)-#1(x_prefix) >= 0`,

then `(x,y)` is a genuine canonical prefix from the fixed seed `J=-13`.

Reason:

1. the cylinder relation gives full endpoint denominator divisibility;
2. reduction modulo every `2^i` gives the same divisibility for all prefixes;
3. the inherited RL283 backward reconstruction theorem converts those divisibility conditions into exact prefix integrality;
4. prefix dominance gives `d_i>=1`;
5. integrality is exactly canonical parity compatibility.

Hence canonical prefixes from `J=-13` are in exact bijection with residues `z` whose parity-count difference for `A(z)` versus `z` never goes negative.

Regression counts through depths `1..12` are exactly

`2,3,5,9,16,30,56,105,199,379,721,1377`.

### Section interpretation

If the current endpoint values are `a=C^n(z)` and `b=C^n(A(z))`, then the current section on suffix coordinate `u` is

`g_(d,J)(u)=3^d u-(J-3^d+2^d)`.

At `d=1`,

`g_J(u)=3u+1-J`.

For the reference

`h(u)=3u+1`,

`g_J-h=-J`.

Thus

`nu_2(J)=k`

is exactly level-`k` agreement of the current balanced section `g_J` with the reference section `h`.

Classification:

`FIXED_SEED_PARITY_CYLINDER_AFFINE_BALLOT_BIJECTION_PROVED`

This is the main positive RL289 reparameterization. It replaces the vague phrase "globally selected higher lift" by an exact ballot-selected subtree of the fixed affine map `A(z)=3z+14`.

## 6. Boundary valuation equals complete rejected-tube depth

Take a genuine positive even balanced checkpoint

`d=1`, `J>0`, `k=nu_2(J)>=1`.

Because `J` is even, `K=J+1` is odd. At the ballot wall:

- the legal child is column `01`, raising `d` from `1` to `2`;
- the sibling `10` is rejected by the ballot condition and formally lowers `d` from `1` to `0`.

Follow that rejected sibling algebraically in the full paired parity tree.

After the initial `10`,

`d=0`,
`J_1=J/2`.

At `d=0`, if `J_i` is even, both diagonal columns are possible:

- `00`: `J_(i+1)=J_i/2`;
- `11`: `J_(i+1)=3J_i/2`.

Either way,

`nu_2(J_(i+1))=nu_2(J_i)-1`.

Therefore `nu_2(J)=k` iff the rejected sibling supports a complete `d=0` binary tube for exactly `k-1` additional diagonal levels after the initial rejected edge.

At the bottom there are `2^(k-1)` `d=0` nodes and every bottom `J` is odd.

For a general even state

`J=2^k q`, `q` odd,

a tube word of length `k-1` containing `r` `11` columns gives

`J_bottom=3^r q`.

Taking the returning `01` edge gives

`J_return=(3^(r+1)q+1)/2`.

For a terminal power `J=2^k`, this becomes

`J_return=(3^(r+1)+1)/2`.

The old RL283 formal terminal extension is exactly the all-`00` tube branch (`r=0`), which returns to `J=2`.

### Gate-A geometric equivalence

At a balanced checkpoint, `H` is the accumulated ballot/Ferrers area.

Hence Gate A is exactly:

`depth of the complete rejected d=0 tube adjacent to a positive boundary node <= accumulated legal-path area`.

This is a genuine isoperimetric reformulation, but the rejected tube itself is not a legal canonical subtree and cannot be used as though it were reachable.

Classifications:

`BOUNDARY_VALUATION_EQUALS_COMPLETE_REJECTED_TUBE_DEPTH_PROVED`

`TERMINAL_EXTENSION_IS_ONE_BRANCH_OF_FULL_REJECTED_TUBE_PROVED`

## 7. Dual endpoint codes and the mixed finite carry

For a word `w`, choose its least nonnegative cylinder representative

`0 <= zeta_w < 2^n`

and define the endpoint code

`e_w=C^n(zeta_w)`.

If the word has weight `r`, then analytically

`0 <= e_w < 3^r`.

Also

`2^n e_w == Q_w (mod 3^r)`.

For a canonical pair set

`xi=zeta_x`, `eta=zeta_y`,
`a=e_x`, `b=e_y`.

The fixed affine cylinder relation gives an ordinary integer carry

`c=(3xi+14-eta)/2^n`.

For `n>=4`,

`c in {0,1,2,3}`.

The physical state has the exact representation

`J=3^d a-b-c 3^(r_y)+3^d-2^d`.

At a balanced checkpoint,

`J=3a-b-c3^r+1`.

If `J>0`, then `c!=3`, so positive states have

`c in {0,1,2}`.

The carry evolves finitely. If a child cylinder lift uses bits `t_x,t_y in {0,1}`, then

`c'=(c+3t_x-t_y)/2`.

The endpoint codes also have exact closed transitions.

### Genuine mixed-state diamonds

The mixed state does not determine accumulated area.

At length `6`, both genuine histories

`(x,y)=(001000,010001)`

and

`(x,y)=(100000,100100)`

reach the same

`(d,J)=(2,3)`

and the same mixed values

`r_x=1`, `r_y=2`, `a=1`, `b=2`, `c=1`,

but have different accumulated areas:

`H=1` and `H=2`.

Thus `H` is a path cost, not an endpoint coordinate.

Define

`mu(Q)=min H`

over all fixed-seed histories reaching a mixed state `Q`.

Then the exact Bellman recurrence is

`mu(Q')=min_(Q->Q') [mu(Q)+d(Q)-1]`.

Gate A at a balanced state is equivalently

`nu_2(J(Q)) <= mu(Q)`.

Classifications:

`BOUNDED_3ADIC_ENDPOINT_CODES_AND_FINITE_BINARY_CARRY_REPRESENTATION_PROVED`

`MIXED_STATE_HISTORY_MERGING_DIAMONDS_PROVED`

`GATE_A_EQUIVALENT_TO_MINIMUM_AREA_BELLMAN_BOUND_ON_EXACT_MIXED_QUOTIENT_PROVED`

This is a structural reformulation only; it does not itself contract the residual.

## 8. Pure 3-adic suffix information is insufficient

At a balanced checkpoint, reverse one-rank positions give endpoint-code congruences of the form

`a == sum 3^(j-1) 2^(-A_j) (mod 3^r)`,
`b == sum 3^(j-1) 2^(-B_j) (mod 3^r)`,

with ordered reverse ranks and total displacement equal to `H`.

For a terminal `J=2^k`, the necessary endpoint congruence is

`3a-b == 2^k-1 (mod 3^r)`.

This condition is far too weak.

For every odd `k` and every `r>=1`, let `a_(k,r)` be the least residue satisfying

`2a_(k,r) == 2^k-1 (mod 3^r)`.

There exist weight-`r` words having endpoint code `a_(k,r)`.

Taking `x=y` then gives

`H=0`

while satisfying the full terminal 3-adic endpoint congruence.

The fake family persists through the formal terminal extension modulo the next power of `3`.

Classification:

`PURE_3ADIC_ENDPOINT_CONGRUENCE_ADMITS_ARBITRARILY_DEEP_ZERO_AREA_FAKE_TERMINALS_PROVED`

Hence endpoint-code congruence, rank order, and area without the fixed-seed 2-adic coupling cannot prove Gate A.

## 9. Signed defects and the absolute-rank gauge correction

Define signed cylinder defects

`alpha=3^(r_x)-a`,
`beta=3^(r_y)-b`.

They are the terminal magnitudes obtained by starting the parity words from the least negative representatives of their cylinders.

They yield a length-free finite transition system and initially appeared to provide a useful high-rank reverse Bellman/discrete-log rigidity.

That apparent Gate-A leverage is **demoted**.

The exact identity is

`2^n(alpha + C_x(-7)) = 3^(r_x)(2^n-xi-7)`.

Therefore

`2^n alpha == -U_x (mod 3^(r_x))`,

equivalently

`alpha == -C_x(-7) (mod 3^(r_x))`

in the 3-adic sense.

Likewise

`beta == -C_y(-7) (mod 3^(r_y))`.

Prepending another neutral `(101)` seed cycle raises both one-ranks by `2` while leaving the complete physical post-departure trajectory `(d,J,H)` unchanged.

Thus increasing the absolute signed rank merely reveals more 3-adic digits of the same inherited fixed-seed shadows.

The previously explored discrete-log period

`2*3^(m-1)`

and its apparent "high-rank rigidity" are algebraically correct at a chosen gauge, but **absolute rank is not a gauge-invariant complexity parameter** and can be inflated for free.

Classifications:

`SIGNED_DEFECTS_ARE_FINITE_3ADIC_TRUNCATIONS_OF_FIXED_SEED_SHADOWS_PROVED`

`ABSOLUTE_SIGNED_RANK_AS_GATE_A_COMPLEXITY_PARAMETER_DEMOTED_AS_NEUTRAL_PREFIX_GAUGE_ARTIFACT`

The derived affine source rays and common-phase carry identities remain correct algebraic descriptions, but they are not promoted as a Gate-A contraction.

## 10. Cycle-lemma ballot repair has an exact fixed-seed seam obstruction

At a terminal

`d=1`, `J=2^k`,

let `(x,y)` be the genuine equal-weight prefix of common length `m`, weight `r`.

RL283 gives

`3Q_x-Q_y = 14*3^r + 2^m(2^k-1)`.

Extend formally:

`X=x 1 0^k`,
`Y=y 0^k 1`.

The extension has one negative-height plateau of length `k`.

There are exactly `k` minimum-height cyclic rotations which restore prefix dominance.

For `e=0,...,k-1`, write those rotations as

`X_e=0^(e+1) x 1 0^(k-1-e)`,
`Y_e=0^e 1 y 0^(k-e)`.

Their numerators satisfy

`3Q_(X_e)-Q_(Y_e)=2^e B`

where

`B=18Q_x+6*2^m-3^r-2Q_y`.

`B` is odd.

The fixed-seed endpoint seam defect is

`D_e=3Q_(X_e)-Q_(Y_e)-14*3^(r+1)`.

Exactly,

`nu_2(D_e)=0` for `e=0`,
`nu_2(D_e)=2` for `e=1`,
`nu_2(D_e)=1` for `e>=2`.

Hence every ballot-restoring cyclic rotation has

`nu_2(D_e)<=2`.

But a genuine fixed-seed reconstruction at extended length

`L=m+k+1`

would require full `2^L` divisibility.

Classification:

`ALL_BALLOT_RESTORING_CYCLE_LEMMA_ROTATIONS_HAVE_FIXED_SEED_SEAM_VALUATION_AT_MOST_TWO_PROVED`

This decisively kills the natural reflection/cyclic-rotation strategy: pure ballot geometry can repair order, but the seam destroys essentially all fixed-seed divisibility.

## 11. Verification and falsification notes

Portable verifier:

`verification/verify_rl289_normalized_pair.py`

Recorded clean output:

`verification/RL289_FAST_VERIFIER_OUTPUT.txt`

The fast verifier checks:

- all canonical edges through depth `16`;
- exact two-shadow identity;
- exact fixed-seed cylinder relation;
- mixed endpoint/carry and signed-defect identities;
- positive-state exclusion of carry `3`;
- exact ballot-bijection counts through depth `12`;
- rejected-tube branches;
- terminal cycle-lemma seam valuations.

Recorded PASS counts:

- canonical edges: `39165`;
- ballot counts depth `1..12`:
  `2,3,5,9,16,30,56,105,199,379,721,1377`;
- rejected-tube branch checks: `5446`;
- genuine terminal occurrences checked: `1688`;
- cycle-seam checks: `3290`.

The inherited RL285 `H<=22` exhaustive certificate remains the finite falsification oracle and is not duplicated.

During exploration, the tempting real-magnitude bound

`0<J<2^(H+1)`

was falsified by a genuine reachable state, e.g.

`(d,J,H)=(1,10934,12)`.

It is not promoted.

## 12. Closed proof state

Promoted RL289 advances:

1. normalized root-cancelling joint coordinate and its fixed valuation-one barrier;
2. rational common-phase invariant collapse to the inherited defect;
3. exact boundary phase-vector 2-adic isometry and periodic-cylinder normal form;
4. arbitrary-future-phase transparency of any fixed recent suffix;
5. exact fixed-seed parity-cylinder affine ballot bijection for `A(z)=3z+14`;
6. balanced section interpretation `g_J(u)=3u+1-J`;
7. boundary valuation equals complete adjacent rejected-tube depth;
8. full rejected-tube generalization of the old terminal extension;
9. bounded endpoint-code / finite carry exact representation and Bellman quotient;
10. pure 3-adic endpoint fake-family barrier;
11. signed defects identified as finite 3-adic truncations of the inherited shadows;
12. absolute-rank/discrete-log leverage explicitly demoted as neutral-prefix gauge artefact;
13. exact cycle-lemma fixed-seed seam valuation barrier.

No RL289 result proves Gate A.

Exact live residual remains:

`k>=25`, `k` odd, `H_can<k`.

## 13. Successor direction

RL290 should keep the fixed affine ballot model and rejected-tube geometry, but it must work in **gauge-invariant post-departure variables**.

The surviving conceptual target is the fixed-seed seam/history coupling:

- high terminal valuation is a deep complete rejected sibling tube / deep agreement with the reference section `h(u)=3u+1`;
- bounded recent history cannot control that depth;
- pure endpoint `3`-adic data cannot control it;
- absolute signed rank is gauge;
- ballot reflection repairs order but loses fixed-seed divisibility at the cut seam.

Therefore a successful successor needs a genuinely history-sensitive, gauge-invariant constraint tying the fixed seed `-7` / affine map `A(z)=3z+14` to the seam between the legal ancestry and the adjacent rejected tube.

Do not restart the demoted absolute-rank/discrete-log programme, pure endpoint-code programme, cycle-rotation programme, bounded recent-suffix programme, or raw height-cap enumeration as principal routes.

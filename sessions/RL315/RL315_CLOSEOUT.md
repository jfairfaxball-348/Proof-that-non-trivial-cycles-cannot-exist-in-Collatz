# RL315 closeout — universal reduced-window extraction, reduced-shadow interface, and ownership frontier

Date: 2026-09-14
Status: CLOSED AND FROZEN
Session type: MATHEMATICAL EXECUTION AFTER RL314 WHOLE-PROGRAM AUDIT
Incoming authoritative HEAD: `3bad9e4df6f70472fdf1230b2ac951434391f3d2`
Successor: RL316

## 0. Executive conclusion

RL315 does not prove Gate A, Gate B, global positive non-trivial-cycle exclusion,
or the Collatz conjecture.

It does, however, materially change the top-level architecture selected by RL314.

The incoming target asked whether, in the RL311 controlled branch `g<=h+1`,
full-D ownership forces a repeated canonical gcd-block level.  RL315 found a
stronger route: for every multiplicity `g>1`, independently of the canonical
minimum-root block levels, there is always a genuine cyclic length-`a` window
with exactly `ell` odd bits.  Thus every `g>1` candidate already has a proper
owned reduced balanced return of counts `(a,ell)`.

RL315 then develops a canonical reduced-shadow/interface normal form for the
entire `g>1` word, proves strict physical domination by the reduced rational
shadow, derives an exact positive full-cofactor ownership identity, and isolates
a support-independent successor target.

The original literal repeated-level target is therefore superseded for `g>1`.
The `g=1` coprime branch remains separate and does not admit a proper reduced
balanced return.

## 1. Universal reduced-window theorem

Write

`A=ga`, `L=g ell`, `gcd(a,ell)=1`, `g>1`.

For each cyclic phase `r`, let `N_r` be the number of ones in the cyclic
length-`a` window beginning at `r`.

Every full-word one contributes to exactly `a` such windows, hence

`sum_r N_r = aL`

and therefore the average value is exactly

`aL/A = ell`.

Also

`N_(r+1)-N_r in {-1,0,1}`.

An integer-valued cyclic 1-Lipschitz sequence with average exactly the integer
`ell` must attain `ell`.  Therefore some genuine rotation has a proper segment
with exact counts

`(a,ell)`.

This is a genuine owned balanced return between two rotations of the full
integer cycle.  No local denominator ownership is inferred.

Using the RL311 `U=q(4x+1)` coordinate from that rotation, the endpoint pair
obeys

`1/lambda < (4x_(r+a)+1)/(4x_r+1) < lambda < 3`

in the active `lambda<3` sector.

Consequences:

- the RL311 controlled/non-controlled branch distinction is no longer needed to
  *existentially* obtain a reduced balanced return for `g>1`;
- RL312/RL313 balanced-shift consumers may be applied at the universal shift
  `s=a`;
- `g=1` is the unique branch with no proper reduced balanced window.

## 2. Canonical multi-layer reduced-shadow normal form

Cut the full binary parity word into `g` rows of length `a`.
Let `P_k(j)` be the number of ones in the first `j` positions of row `k`, and
let

`E_k = (# ones in rows 0,...,k-1) - k ell`.

Put

`H_(k,j)=E_k+P_k(j)`,
`m_j=min_k H_(k,j)`,
`f_(k,j)=H_(k,j)-m_j`.

Then `f_(k,j)>=0` and each column has a zero.

Since `H_(k,j+1)-H_(k,j)` is a parity bit, define

`tau_j=m_(j+1)-m_j in {0,1}`.

The twisted row boundary gives `m_a=m_0+ell`, hence

`sum_(j<a) tau_j = ell`.

The original parity word satisfies the exact identity

`d_(k,j)=tau_j + f_(k,j+1)-f_(k,j)`

with twisted boundary

`f_(k,a)=f_(k+1,0)`.

Thus every multiplicity-`g` word is canonically a nonnegative integer interface
over the repeated reduced word

`v=tau^g`

of counts `(a,ell)`.

The universal block-shift flow is exactly

`G_(k,j)=ell-W_(k,j)(a)=f_(k,j)-f_(k+1,j)`.

So RL312 full activity means exactly that every interface column is nonconstant.
The equality case `sum|G|=2a` is the height-one/binary-interface special case.

## 3. Strict reduced-shadow domination

Let `x_i` be the genuine integer cycle and flatten the canonical interface to
`f_i`.  Put

`Z_i=3^(-f_i)(4x_i+1)`.

From the ordinary half-step recurrence and
`d_i=v_i+f_(i+1)-f_i`,

`2Z_(i+1)=3^(v_i)(Z_i+3^(-f_i))`.

Let `r_i` be the positive rational cyclic orbit of the repeated reduced word
`v=tau^g`, and set `Y_i=4r_i+1`.  Then

`2Y_(i+1)=3^(v_i)(Y_i+1)`.

Hence

`2(Y_(i+1)-Z_(i+1))
 =3^(v_i)((Y_i-Z_i)+(1-3^(-f_i)))`.

The homogeneous full-period multiplier is `3^L/2^A=1/lambda<1`.
For a primitive `g>1` word, `f` is not identically zero.  Therefore the unique
cyclic solution has

`Y_i-Z_i>0`

at every phase.

Because each column contains some row with `f=0`, every reduced shadow phase
strictly dominates at least one genuine physical phase:

`for every j<a, there exists k with x_(k,j)<r_j`.

If `tau_j=1` and `f_(k,j)=0`, then binary legality forces
`f_(k,j+1)=0` and `d_(k,j)=1`.  Thus every odd shadow phase dominates a distinct
genuine odd cycle state.  The inherited physical odd-state packing bounds can
therefore be transferred to the reduced shadow.

## 4. Internal reduced-denominator upgrade

RL130 supplies an internal least-state floor and a minimum-element/product
ceiling whose exact arithmetic scan yields the primitive ordinary frontier
`L>=190537`.

The minimum-element ceiling is positivity/product based, so it applies to the
positive reduced rational shadow as well as to an integer cycle.

Since the shadow minimum is strictly above the genuine cycle minimum, the same
RL130 certificate applies directly at reduced counts `(a,ell)`.

Therefore RL315 upgrades the internal frontier to

`boxed: ell = L/gcd(A,L) >= 190537`.

This is stronger than a bound on the unreduced `L` alone.

The conditional external RL131 frontier remains stronger when its inherited
external `R>=2^71` input is allowed:

`ell>=49,547,666,544`.

No external floor is internalized.

## 5. Exact positive full-cofactor ownership identity

Choose a phase with `f_0=0`.  Put

`X=2^a`, `Y=3^ell`, `D0=X-Y`,
`H=(X^g-Y^g)/(X-Y)`.

Let `q=Q(tau)` and let `r_0=q/D0` be the corresponding reduced-shadow state.
Strict domination gives `r_0>x_0`, so

`n=q-x_0 D0`

is a positive integer.

Iterating the transformed difference equation around the complete full word
gives

`sum_(i=0)^(A-1) 2^i 3^(L-C_i^v) (1-3^(-f_i)) = 4 n H`.

Since `f_0=0` implies

`C_i^d=C_i^v+f_i`,

every summand is an integer:

`2^i 3^(L-C_i^v-f_i)(3^(f_i)-1)`.

Thus

`boxed:
 sum_i 2^i 3^(L-C_i^v-f_i)(3^(f_i)-1)
 in 4H Z_(>0)`.

Equivalently, decomposing the interface into superlevel layers gives a positive
layer sum equal to `2nH`.

This is not claimed to evade RL206's additive compatibility classification.
Algebraically it is a nonlinear/order-aware rewriting of full numerator
ownership.  Its new content is the canonical min-normalized interface,
positivity, layer structure, and exact positive `H`-multiple target.

## 6. Height-one interface and `g=2`

If `sum|G|=2a`, every nonconstant interface column has cyclic variation exactly
two, hence is binary with one cyclic interval of ones.  This recovers the
RL313 rational countermodel geometry as the complete height-one class, rather
than merely one example.

For `g=2`, the universal balanced length-`a` window has a complementary
length-`a` window with the same count `ell`.  Hence one entire `a`-shift orbit
is inactive.

Therefore

`boxed: g=2 => the RL312 fully-active alternative is impossible`.

Every `g=2` survivor lies in the equal-row terminal branch.

If the two balanced row numerators are `q_0,q_1` and boundary states are
`x_0,x_1`, then

`X x_1=Y x_0+q_0`,
`X x_0=Y x_1+q_1`.

Hence

`q_0-q_1=(X+Y)(x_1-x_0)`

and primitivity forces

`|q_0-q_1|>=X+Y`.

This is an exact two-row ownership/spacing condition.

## 7. Physical-order theorem for canonical block levels

In the RL311 minimum-root `lambda<3` normalization, for proper canonical block
cuts `0<=j<k<g`, put `m=k-j`.

The exact `U` identity gives

`(4x_k+1)/(4x_j+1)
 =(U_(ka)/U_(ja)) z^(-m) 3^(E_k-E_j)`

with

`1<U_(ka)/U_(ja)<lambda`,
`1<z^m<lambda<3`.

Therefore

`E_k>E_j iff x_k>x_j`,
`E_k<E_j iff x_k<x_j`.

If levels differ by `r>=1`, the higher-level physical state satisfies the
quantitative bound

`(4x_high+1)/(4x_low+1) > 3^r/lambda`.

Under distinct levels,

`n_j>ell iff x_(j+1)>x_j`,
`n_j<ell iff x_(j+1)<x_j`.

This theorem did not itself force a collision, but it remains a useful
order-sensitive physical invariant.

## 8. Front-loaded block product lemma

For any length-`a` block with `n` odd bits and positive starting state `x`, its
exact block numerator is minimized by placing all odd bits first:

`b_min(n)=3^n-2^n`.

The odd-step product over the block therefore satisfies

`P >= 1 + [1-(2/3)^n]/x`.

In the injective canonical-level branch, `E_1>=1` gives
`n_0>=ell+1`, yielding the least-state lower bound

`R > [1-(2/3)^(ell+1)]/(lambda-1)`.

This is exact but did not remove the unbounded controlled parameter by itself.

## 9. Constant-coefficient block compression barrier

For canonical blocks, with `X=2^a`, `Y=3^ell`,
`n_j=ell+E_(j+1)-E_j`, and exact block numerator `b_j`, define for
`H=max E_j`

`s_j=3^(H-E_j)x_j`,
`f_j=3^(H-E_(j+1))b_j`.

Then

`X s_(j+1)-Y s_j=f_j`

is a constant-coefficient cyclic recurrence.

Its compatibility module has determinant
`D=X^g-Y^g` and cyclic cokernel `Z/DZ`, with weights
`X^jY^(g-1-j)`.

Thus the first natural attempt to obtain a repeated-level theorem from bare
additive full-D compatibility collapses to a generalized RL206 recurrence/gauge
description.  This is a barrier, not a closure.

## 10. Final attack: dyadic row decoding

For fixed row length `a` and fixed weight `ell`, the numerator map

`w -> Q(w) mod 2^a`

is injective.

Proof is recursive.  Modulo two, the numerator parity reveals the first bit.
If it is zero, divide by two and recurse with the same remaining weight.  If it
is one, subtract `3^(ell-1)`, divide by two, and recurse with remaining weight
`ell-1`.

In the `g=2` terminal branch this gives

`Q(w_0) == -3^ell R (mod 2^a)`,

so the least boundary state determines the complete outgoing balanced row
uniquely.

This did not close `g=2`, but it is an exact order-sensitive reconstruction
interface for future work.

## 11. Corrections, failed routes, and preserved barriers

Binding corrections from this session:

1. `H | Q(d)-Q(tau^g)` alone does **not** force `d=tau^g`; small nonrepeated
   binary counterexamples exist.  Do not promote a bare cofactor-injectivity
   claim.
2. The `g=1` Bezout/determinant-one selected-flow route is historically mature
   (RL240-RL242 and later work).  RL315's simple `<3` endpoint observation is a
   splice, not a new closure.
3. Bare finite modulus remains subject to RL233; additive full-D compatibility
   remains subject to RL206.
4. The universal reduced-window theorem does not create local denominator
   ownership.
5. The reduced rational shadow is not an integer cycle.  Only positivity/product
   arguments and explicitly justified inherited consumers may be transferred.
6. Support-by-support `3,4,5,...` grammar remains frozen.
7. Fixed-96 P/Q, Radius 6+, H21, and raw Gate-A routes remain frozen unless a
   future authoritative target explicitly reactivates them.

## 12. Unpromoted numerical/computational scratch preserved for replay

The following were obtained during the long conversational session and are
preserved because they may be valuable, but they are **not promoted as
authoritative certificates by this closeout** without an independent portable
replay:

- first internal reduced fibre `(a,ell)=(301994,190537)`;
- exploratory RL310 multiplicity cap first estimated as `g<=10,199,842`, later
  tightened in scratch to `g<=9,728,182` after a claimed extension of the
  internal descent floor;
- scratch determinant threshold `56 theta<1<57 theta` on that first fibre;
- scratch low-multiplicity least-state ceiling
  `R<=710,220,447,737`;
- scratch full-first-fibre state ceiling near `1.365e12`;
- claimed deterministic stopping-to-smaller extension of the internal descent
  checkpoint from `15,671,092,983` to `19,671,092,983`, covering two billion
  additional odd starts;
- associated claimed maximum stopping times/intermediate values.

These numbers must be independently regenerated by a portable verifier before
future promotion.  The analytic formulas and attack logic are preserved here
so no work is lost.

## 13. Exact successor frontier

The highest-leverage successor is no longer the literal repeated-level theorem.

For `g>1`, the canonical state is:

`full word d`
=
`repeated reduced shadow tau^g`
+
`nonnegative integer interface f`

with

`d_i=tau_(i mod a)+f_(i+1)-f_i`

and exact positive ownership energy

`sum_i 2^i 3^(L-C_i^v-f_i)(3^(f_i)-1)=4nH`.

RL316 should ask:

> Can genuine full `D0 H` ownership, positivity, and binary path legality force
> the canonical interface to vanish, or otherwise reduce every nonzero
> interface to a finite exact certificate?

Primary subtargets:

- consume the row-energy / layer-energy equation with a support-independent
  small-coefficient or no-carry theorem;
- exploit the fact that interface rises occur only on shadow-zero bits and falls
  only on shadow-one bits, so the full word is an order-preserving transport of
  ones relative to `tau^g`;
- attack `g=2` first using exact row spacing plus dyadic row decoding;
- independently replay the promising first-fibre numerical certificates and
  promote only reproducible finite arithmetic;
- keep `g=1` as a separate mature Bezout/ordinary-`+1` branch.

## 14. Final proof status

RL315: CLOSED AND FROZEN.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.
Lean formalisation remains a separate project.
Knowledge catalogues remain stale/deferred.

`PARENT_DIFFICULTY_DELTA = EASIER`

Reason: RL315 replaced the controlled-branch collision target for all `g>1`
with an unconditional reduced balanced return, then exposed a canonical
support-independent reduced-shadow/interface object carrying exact positive
full-cofactor ownership.

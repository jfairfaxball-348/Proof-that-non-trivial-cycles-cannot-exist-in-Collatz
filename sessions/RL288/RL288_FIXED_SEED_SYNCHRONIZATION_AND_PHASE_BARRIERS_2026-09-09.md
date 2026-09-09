# RL288 — fixed-seed synchronization and phase-selection barriers

Date: 2026-09-09

## Classification

Primary:

`FIXED_SEED_FIRST_DEVIATION_SYNCHRONIZATION_AND_LOCAL_PHASE_BARRIERS_PROVED`

Promoted analytic subordinate results:

- `FIRST_POSITIVE_ENTRY_2ADIC_AREA_BOUND_PROVED`;
- `M_MAGNITUDE_ESCAPE_LOCALIZED_TO_BOUNDARY_11_PROVED`;
- `ARBITRARILY_DEEP_VALUATION_SAFE_REVERSE_00_RAY_BARRIER_PROVED`;
- `SHIFTED_T_MAGNITUDE_ESCAPE_LOCALIZED_TO_BOUNDARY_11_PROVED`;
- `PAIRED_M_T_PHASE_CLOSURE_COLLAPSES_TO_TWO_TEMPLATE_BOUNDARY_HAZARD_BARRIER_PROVED`;
- `COMMON_SEED_FIRST_DEVIATION_SYNCHRONIZATION_PROVED`;
- `THREE_FIXED_SEED_ESCAPE_ROOTS_REDUCTION_PROVED`;
- `FIXED_SHIFTED_SHADOW_PHASE_DEGENERACY_PROVED`.

Gate A remains open with exact residual

`k>=25`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming state and mission

RL288 inherited RL287's conclusion that local reserves, local component-height inequalities, boundary-density arguments, finite shifted-valuation tables, and fixed-suffix 2-adic restrictions cannot by themselves select the globally reachable lift. The mission was therefore to attack the fixed-seed global selection problem directly.

Use

`K=J+2^d-1`,
`M=K-1=J+2^d-2`,
`A=H+d-1`.

The preferred all-depth Gate-A sufficient theorem remains

`J>0 => nu_2(M)<=A`.

RL288 does not prove it.

## 2. First positive entry is 2-adically area-safe

Consider a canonical path from the fixed seed `(d,J,H)=(1,-13,0)` and its first state with `J>0`.

### Theorem

At that first-positive state,

`0<M<3^d`

and

`nu_2(M)<=A`.

Equality occurs only at

`(d,J,H)=(3,2,1)`,

where `M=8`, `A=3`.

This equality state is genuinely reached by `x=000`.

### Proof sketch

A sign crossing cannot occur through the `10` descent because that sends even `J<=0` to `J/2<=0`. The other three crossing branches give directly:

- `11`: `M'=(3J+3*2^d-5)/2 < 3^d`;
- `00`: `M'=(J+3^d+2^d-4)/2 < 3^d`;
- `01`: at child depth `e=d+1`, `M'=(3J+3^e+3*2^(e-1)-5)/2 < 3^e`.

Any path starting at depth one and first reaching depth `d` has

`A>=d(d-1)/2`.

For `d>=4`,

`2^(A+1)>3^d>M`,

so `nu_2(M)<=A`. The small depths `d=1,2,3` reduce to explicit crossing cases; only `d=3,A=3,J=2` gives equality.

This theorem uses the complete sign history from the fixed seed and is not a local predecessor statement.

## 3. Elementary M-magnitude safety and its unique escape column

Call a positive state `M`-safe when

`M<2^(A+1)`.

The exact `M` recurrences are

- `11`: `M'=(3M+1)/2`;
- `00`: `M'=(M+3^d-2)/2`;
- `10`: `M'=(M-2)/2`;
- `01`: `M'=(3M+3^(d+1)+1)/2`.

### Theorem

Every positive `M`-safe canonical transition remains `M`-safe except possibly the zero-height boundary `11` transition at `d=1`.

Thus the first loss of the elementary magnitude barrier can occur only on that boundary amplification.

If such a first magnitude escape is already a 2-adic failure, then with `T0=2^(A+1)` the child must be exactly

`M'=T0`,

because the first escaped value lies in `[T0,3T0/2)`. Hence its boundary parent is uniquely

`M=(2T0-1)/3`.

The conditional reverse congruence refinements explored from this special case are not promoted in RL288; see Section 9.

## 4. Arbitrarily deep safe reverse-00 rays defeat a naive ancestor sieve

Earlier harmless magnitude escapes cannot simply be ignored.

### Theorem

For every odd terminal exponent `k` and every `L>=1`, set

`J_0=1+2^L(2^k-1)`.

Then `L` consecutive legal boundary `00` columns give

`J_i=1+2^(L-i)(2^k-1)`

and terminate exactly at

`J_L=2^k`.

Every proper predecessor is positive and odd, hence has valuation zero, and the whole ray costs zero height.

For odd `k`, these proper predecessors also remain in the inherited necessary nonzero mod-3 classes.

### Consequence

A reverse proof using only positivity, local legality, the basic mod-3 filter, and the already desired `nu_2(J)<=H` inequality can have arbitrarily deep valuation-safe predecessor tails. Therefore the conditional first-magnitude-escape congruence sieve cannot globalize without an additional fixed-seed selector.

## 5. Shifted coordinate T and the same boundary escape architecture

Define

`T=J+2^d-3^d`.

Bookkeeping correction made during RL288 closeout:

`T=K+1-3^d`,

not `K-3^d`. The transition formulas used during the session were already the correct formulas, so no mathematical conclusion below is changed.

The exact recurrences are

- even `K`, `x=0`: `T'=T/2`;
- even `K`, `x=1`: `T'=(3T+3^d-1)/2`;
- odd `K`, `x=1`: `T'=(T+3^(d-1))/2`;
- odd `K`, `x=0`: `T'=(3T-1)/2`.

Call a state `T`-safe when

`0<T<2^A`.

### Theorem

A first transition from `T<=0` into `T>0` is `T`-safe. Once `T`-safe, every canonical transition preserves `T`-safety except possibly the zero-height boundary `11` column.

At `d=1`, if a first `T`-magnitude escape is immediately a violation of the shifted bound `nu_2(T)<=H-1`, the child must be

`T'=2^H`,

with unique parent

`T=(2^(H+1)-2)/3`,
`J=(2^(H+1)+1)/3`.

Integrality forces `H` even.

This does not prove the shifted inequality globally; arbitrary locally legal high-phase lifts still exist.

## 6. Pairing M and T does not create a new finite phase invariant

At the boundary `d=1`,

`M=J`,
`T=J-1`.

Thus one of the two is odd at every boundary state. Along an odd boundary `11` run, `M` is 2-adically blind while `T` predicts a future zero cylinder.

For `r` consecutive boundary `11` columns,

`J_r+1=(3/2)^r(J+1)`.

A subsequent zero-run of length at least `s` requires

`2^(r+s) | 3^r(J+1)-2^(r+1)`,

or

`J == 2^(r+1)3^(-r)-1 (mod 2^(r+s))`.

As `r` varies these form an infinite hierarchy of 2-adic cylinders approaching the already inherited boundary template `-1`. The complementary exits give the second inherited template.

### Classification

The paired `(M,T)` architecture collapses to RL283's two-template boundary hazard rather than supplying a new finite closed shifted-valuation table.

This is a route barrier, not a Gate-A theorem.

## 7. Common-seed shadow first-deviation synchronization

RL283's formal Collatz shadow for a binary word `w` is

`C_w(z)=(3^r z+Q_w)/2^n`.

Define the common-seed cleared numerator

`U_w=-7*3^r+Q_w=2^n C_w(-7)`.

Its recurrence is

`U_empty=-7`,
`U_(w0)=U_w`,
`U_(w1)=3U_w+2^n`.

The genuine half-step parity itinerary of the seed `-7` is the periodic word

`p=(101)^infinity`,

because

`-7 -> -10 -> -5 -> -7`.

### First-deviation valuation lemma

Let `w` have length `n` and first differ from `p` at position `s<n`. Then

`nu_2(U_w)=s`.

Up to `s` the prescribed word follows the genuine integer orbit, hence the cleared numerator has the required powers of two. At the first wrong parity choice the remaining quotient is odd. Every later update either multiplies by odd `3` or adds a term divisible by a strictly higher power of two, so the valuation remains exactly `s`.

### Synchronization theorem

For a genuine canonical paired prefix `(x,y)` of common length `n` and current depth `d`, RL283's exact two-shadow representation gives

`3^d U_x-U_y = 2^n T`.

The right side is divisible by `2^n`.

If `x` and `y` first deviated from `p` at distinct positions below `n`, the valuation of the left side would be the smaller first-deviation position, because `3^d` is odd. That would be `<n`, contradiction.

Therefore:

`x` and `y` have exactly the same first-deviation position from `(101)^infinity`, or neither has deviated yet.

At the common first deviation they also choose the same opposite bit.

This is a genuinely fixed-seed theorem: it depends on complete shadow divisibility from the common seed and is unavailable for arbitrary local cylinder inputs.

## 8. Three fixed seed escape roots and fixed-shift degeneracy

Before and through the common first deviation, `x=y`, so the canonical trajectory stays on the zero-height `d=1` boundary.

According to the deviation phase modulo three, the departure boundary state is exactly one of

`J=-6`, `J=-28`, `J=-4`.

At each, the next canonical column is forced to be `01`, producing exactly three zero-height off-boundary roots:

`(d,J,H)=(2,-6,0)`,
`(2,-39,0)`,
`(2,-3,0)`.

Thus after quotienting arbitrary initial repetitions of the neutral `(101)` history, every nontrivial canonical trajectory is rooted in one of three explicit fixed states.

Moreover, after the first deviation at `s`,

`nu_2(U_x)=nu_2(U_y)=s`

persists for the rest of the prefix. For every fixed integer shift `c` and every later length `n>s`,

`nu_2(U_w+c*2^n)=s`.

Hence all fixed shifted valuations of either individual common-seed shadow collapse to the same conserved departure label. Any successful successor invariant must therefore be genuinely joint in the normalized shadow pair, not another finite table of individual shifted valuations.

A natural normalization after departure is

`R_x=U_x/2^s`,
`R_y=U_y/2^s`,

with both odd and mandatory congruence

`R_y == 3^d R_x (mod 2^(n-s))`.

RL288 does not prove any stronger joint congruence or Gate-A consequence from this normalization.

## 9. Unpromoted finite and conditional evidence

The inherited exact `H<=22` raw-state certificate remains a falsification oracle only. RL288 observed within it:

- zero positive violations of the inherited `nu_2(M)<=A` candidate, as already certified by RL285;
- all first-positive states satisfy the theorem in Section 2, with unique equality `(3,2,1)`;
- the shifted candidate `T>0 => nu_2(T)<=A-1` has no violation in the inherited closure and unique equality `(1,5,3)`.

These finite observations are not promoted as global theorems.

A conditional reverse analysis of the special case where the first `M`-magnitude escape is already a valuation failure produced a mod-54 restriction on the terminal exponent. Because arbitrary earlier harmless magnitude escapes admit the exact reverse-00 rays of Section 4, that sieve does not globalize by itself. RL288 therefore leaves the mod-54 refinement as `UNPROMOTED_CONDITIONAL_SCRATCH` rather than promoting it.

Likewise, particular first magnitude-escape examples and finite escape counts are regression diagnostics only.

## 10. Verification

Portable targeted verifier:

`sessions/RL288/verification/verify_rl288_fixed_seed.py`

checks:

- exact `M` and corrected `T` transition recurrences on every legal canonical prefix through length 16;
- the two-shadow identity on those prefixes;
- first-deviation synchronization and exact common-shadow valuations;
- the three boundary departure states and three forced off-boundary roots;
- the genuine first-positive equality witness `(3,2,1)` and the exceptional small-depth arithmetic used in its proof;
- 224 explicit valuation-safe reverse-00 rays;
- representative fixed-shift shadow-degeneracy cases.

The verifier intentionally does not duplicate RL285's multi-million-state `H<=22` certificate.

Recorded output:

`sessions/RL288/verification/RL288_FAST_VERIFIER_OUTPUT.txt`.

Proof-state/scope red team:

`sessions/RL288/verification/RL288_RED_TEAM.md`.

## 11. Proof-state summary

RL288 makes a real fixed-seed advance but does not close Gate A.

The key surviving information is:

1. first-positive entry is 2-adically area-safe;
2. simple magnitude/shifted phase controls localize their first escape to zero-height boundary amplification but cannot survive arbitrary harmless predecessor rays;
3. paired local phases collapse to the already known two-template boundary hazard;
4. the common seed `-7` forces exact first-deviation synchronization of the two shadows;
5. after neutral-cycle quotienting, every nontrivial path begins from one of three fixed zero-height off-boundary roots;
6. all individual fixed shifted-shadow valuations become degenerate after departure.

The successor should therefore work with the normalized odd **joint** shadow pair after the synchronized common-seed departure and seek a genuinely nonlocal constraint coupling its selected higher lift to prefix area. It must not restart the exhausted local phase/reserve routes.

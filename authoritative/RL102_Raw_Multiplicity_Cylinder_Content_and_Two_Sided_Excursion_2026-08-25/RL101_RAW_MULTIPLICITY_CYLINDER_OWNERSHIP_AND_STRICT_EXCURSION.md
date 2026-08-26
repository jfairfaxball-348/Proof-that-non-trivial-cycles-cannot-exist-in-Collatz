# RL101 — raw multiplicity cylinder compression, owned primitive-block excursion, and remaining ownership barrier

Date: 2026-08-25

## 0. Executive outcome

RL101 attacked the authoritative raw first-surplus multiplicity target at the frozen first Farey reduced slope

`(p*,q*)=(114,208,327,604,72,057,431,991)`.

The session produced two reusable structural advances.

1. **Normalized raw-multiplicity cylinder compression.** Although the RL82 absolute maximum envelope increases with raw multiplicity `g`, the same envelope divided by the full cylinder modulus `2*3^(gq*)` decreases exponentially with `g`. Every genuine raw-`g` first-Farey survivor must occupy an exponentially tiny fraction of its full maximum cylinder. The physical maximum must in fact be the least positive even representative of that cylinder.
2. **Owned primitive-block excursion.** If `g>=2`, every internal primitive boundary `hp*`, `1<=h<g`, has at least one excess odd step above `h q*`. In particular the first primitive block reaches an actual physical state below `(sqrt(2)/3)M < M/2`, while the final primitive block must compensate.

These advances do **not** satisfy RL101 Forms A–D. No proof that `g=1`, no universal exclusion of `g>=2`, no feasible finite multiplicity complement, and no multiplicity-aware domination of the existing raw-`g=1` cascade was obtained.

The remaining obstruction is now narrower:

> the missing theorem is a **global ordinary-`+1`, `D|Q`-sensitive lower-content / ownership obstruction** showing that a primitive full cycle cannot extend a first-surplus cylinder whose least representative is as tiny as RL101 forces it to be.

The existing numerical cascade remains frozen at the repaired RL100 checkpoint.

---

## 1. Incoming authority and scope

RL101 accepted the verified RL100 ledger under the verification-economy rule.

Frozen global proof status remains:

- primitive/full-`D` radius-3 obstruction: **closed local theorem**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd terminal `k>=27`: **open globally**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

Mandatory scope repair retained:

- RL83 raw first-surplus counts are `(j,o)=(g p,g q)`;
- the RL85–RL100 physical/cascade machinery is load-bearing at raw `(p*,q*)`, i.e. `g=1`;
- the existing cascade therefore applies only to the **exact first-Farey reduced slope + raw `g=1` + full-phase Gate-A branch** unless a separate multiplicity bridge is proved.

At the frozen first Farey pair the inherited Beatty first-crossing certificate allows

`1 <= g <= 125,777,718,029`.

This is an arithmetic admissibility range only. It does not construct a legal word or cycle.

---

## 2. Setup

Write

`p = 114,208,327,604`,

`q = 72,057,431,991`,

`Delta = p log 2 - q log 3 > 0`,

and

`rho = 2^p / 3^q = exp(Delta)`.

Let raw multiplicity be `g>=1`. For raw counts

`j=gp`, `o=gq`,

define

`D_g = 2^(gp)-3^(gq)`.

RL100 inherits the exact RL82 safe maximum envelope

`U_g = 2^(g(p-q)) (3^(gq)-2^(gq)) / D_g`.

For a full maximum-word cylinder modulo

`2*3^(gq)`,

let `m_(w,g)` be its least positive even representative and define

`theta_(w,g)=m_(w,g)/(2*3^(gq))`.

For a genuine physical survivor,

`M <= U_g`.

The inherited RL84 exact logarithm certificate gives

`Delta > 1/200,000,000,000`.

The first-crossing Beatty condition gives

`0 < g Delta < log 2 < 1`

for every admissible raw multiplicity at this reduced slope.

---

## 3. The normalized multiplicity envelope decreases exponentially

Define

`N_g = U_g/(2*3^(gq))`.

Put

`c=(2/3)^q`.

Direct algebra gives

`N_g = (1/2) (rho/2^q)^g (1-c^g)/(rho^g-1)`.

Therefore

`N_(g+1)/N_g`

`= (rho/2^q) * (1-c^(g+1))/(1-c^g) * (rho^g-1)/(rho^(g+1)-1)`.

Because `0<c<1`,

`(1-c^(g+1))/(1-c^g) < 2`.

Because `rho>1`,

`(rho^g-1)/(rho^(g+1)-1) < 1/rho`.

Hence

`boxed: N_(g+1)/N_g < 2^(1-q) < 1.`

### Theorem RL101.1 — normalized raw-multiplicity compression

For the fixed first Farey reduced pair `(p,q)`, the safe maximum envelope as a fraction of the full raw-`g` cylinder modulus is strictly decreasing in `g`, with the uniform ratio bound

`boxed: N_(g+1) < 2^(1-q) N_g.`

Classification: **analytic theorem**.

This is the opposite monotonicity from the absolute envelope `U_g`, which RL100 proved is strictly increasing.

---

## 4. Explicit exponentially tiny cylinder-height theorem

From

`3^(gq)-2^(gq) < 3^(gq)`

we get

`N_g < 2^(g(p-q)-1)/D_g`.

Also

`D_g / 2^(g(p-q))`

`= 2^(gq) (1-exp(-g Delta))`.

Since `0<g Delta<1`,

`1-exp(-g Delta) > g Delta/2`.

Therefore

`N_g < 1/(g Delta 2^(gq))`.

Using the inherited RL84 certificate

`Delta > 1/200,000,000,000`

gives

`boxed: N_g < 200,000,000,000 / (g 2^(gq)).`

Since a genuine survivor has `m_(w,g)<=M<=U_g`, we obtain:

### Theorem RL101.2 — raw-`g` cylinder-height compression

Every genuine first-surplus survivor at the first Farey reduced slope satisfies

`boxed: theta_(w,g) < 200,000,000,000 / (g 2^(gq)).}`

Classification: **analytic theorem + inherited exact finite logarithm certificate**.

---

## 5. Physical maximum equals the least cylinder representative

Theorem RL101.2 implies

`M < 2*3^(gq)`.

But the full word fixes the maximum cylinder modulo exactly

`2*3^(gq)`,

and `m_(w,g)` is the least positive even representative of that residue class.

Since the physical `M` is itself a positive representative below one full modulus:

### Corollary RL101.3 — representative collapse

`boxed: M = m_(w,g).`

Thus, for every genuine raw multiplicity at this fixed reduced slope, the actual cycle maximum is not an arbitrary lift of its cylinder. It is the cylinder's least positive even representative.

Classification: **analytic consequence of RL101.2 plus the inherited exact word-cylinder statement**.

### Ownership red-team status

This is stronger than cylinder uniqueness alone and consumes the inherited ordinary-`+1` physical maximum envelope. However it still does **not** use the full-cycle divisibility `D|Q(w_full)` or an equivalent primitive ownership condition. It therefore does not yet pass the RL20 `D∤Q` fake test as a multiplicity-exclusion theorem.

---

## 6. Absolute scale still grows with multiplicity

Multiplying the normalized estimate by the modulus gives

`U_g < [2/(g Delta)] (3/2)^(gq)`,

hence

`boxed: M < [400,000,000,000/g] (3/2)^(gq).`

Classification: **analytic theorem + inherited exact logarithm certificate**.

This explains why the existing raw-`g=1` RL85 physical-scale engine does not automatically dominate every `g>=2`.

The normalized cylinder becomes vastly tighter, but the absolute physical cap still grows exponentially with `gq`.

Therefore RL101 Form D is **not** obtained from cylinder compression alone.

---

## 7. Raw multiplicity forces an owned primitive-block excursion

Let `o_i` be the odd-count function of the maximum-rooted backward first-surplus prefix.

At first surplus,

`(j,o_j)=(gp,gq)`.

By definition of the **first** surplus, every proper prefix `i<gp` satisfies

`2^i <= 3^(o_i)`.

Take an internal primitive boundary

`i=hp`, `1<=h<g`.

If `o_(hp) <= hq`, then

`2^(hp)/3^(o_(hp)) >= 2^(hp)/3^(hq) = rho^h > 1`,

which would be an earlier surplus.

Therefore:

### Theorem RL101.4 — internal primitive-boundary excess

For every `g>=2` and every `1<=h<g`,

`boxed: o_(hp) >= hq+1.`

Define

`d_h=o_(hp)-hq`.

Then

`d_0=d_g=0`

and

`boxed: d_h>=1 for 1<=h<g.`

Classification: **analytic theorem from first-surplus minimality**.

Consequences:

- the first primitive block contains at least `q+1` odd steps;
- the last primitive block contains at most `q-1` odd steps;
- the aligned primitive-block count walk makes a strict positive excursion and returns to zero.

---

## 8. A balanced sliding primitive window is forced

Let `b_r` be the odd count in the `r`-th aligned block of length `p`.

Then

`b_1>=q+1`

and

`b_g<=q-1`.

Now slide a length-`p` window one parity position at a time from the first aligned block to the last. Its odd count changes by at most one per slide.

Therefore a discrete intermediate-value argument gives:

### Corollary RL101.5 — owned balanced sliding window

Every raw `g>=2` first-surplus word contains at least one proper physical length-`p` window with exactly `q` odd positions.

Classification: **analytic combinatorial consequence**.

This is an actual window inside the first-surplus word. It is not an auxiliary quotient construction.

No claim is made that this window alone satisfies the full hypotheses of the closed radius-3 theorem.

---

## 9. Multiplicity produces an actual state below half the maximum

Let `x_i` be the physical predecessor state at backward depth `i` from the actual cycle maximum `M`.

For a legal prefix with `o_i` odd steps, the ordinary `+1` affine numerator is positive, so

`3^(o_i) x_i < 2^i M`.

Thus

`x_i/M < 2^i/3^(o_i)`.

At `i=hp`,

`x_(hp)/M < rho^h/3^(d_h)`.

Using `d_h>=1` gives

`x_(hp)/M < rho^h/3`.

At `h=1`,

`x_p/M < rho/3`.

The Beatty first-crossing condition gives

`rho^g<2`.

For `g>=2`,

`rho < 2^(1/g) <= sqrt(2)`.

Hence:

### Theorem RL101.6 — canonical owned low state

For every raw `g>=2` first-surplus survivor,

`boxed: x_p < (sqrt(2)/3) M < M/2.`

Classification: **analytic physical-state theorem using ordinary `+1` positivity and first-surplus arithmetic**.

This is a genuine cycle state, not a normalized quotient coordinate.

---

## 10. Why this does not splice directly into the closed radius-3 theorem

The inherited radius-3 theorem is a finished local contradiction engine with a specific input contract, including exact cyclic adjacent-transposition distance `3` and primitive/full-`D` self-rotation hypotheses.

RL101.6 supplies a physical low state. It does **not** manufacture the exact radius-3 word-distance and full-`D` hypotheses.

Therefore:

- radius-3 remains closed and unchanged;
- RL101 makes no new radius-3 global bridge claim;
- generic radius-4/5 exploration is not justified by this result.

The relevant older programme is instead RL20's still-open **strict-excursion packing** route.

---

## 11. Equal local/global slope: two-sided owned excursion in the near-resonant branch

Assume the local first-surplus reduced slope equals the global reduced cycle slope.

Write global counts as

`(A,L)=(G p,G q)`

with `G>g` when the first-surplus prefix is proper.

Then the complementary physical segment has the same reduced slope and multiplicity `G-g`.

Let the local first-surplus endpoint be `x_(gp)`.

On the complementary forward segment from `M` to `x_(gp)`, positivity of the ordinary `+1` numerator gives

`x_(gp)/M > 3^((G-g)q)/2^((G-g)p)`

`= rho^(-(G-g)).`

In the inherited near-resonant branch

`lambda=rho^G < 16/15`,

we have

`rho^(G-g)<lambda`,

hence

`boxed: x_(gp) > M/lambda > 15M/16.`

Combining with RL101.6:

### Theorem RL101.7 — conditional two-sided excursion

In the proper equal-slope branch with inherited `lambda<16/15`, the actual first-surplus arc contains

- an endpoint `x_(gp) > 15M/16`, and
- an internal primitive-cut state `x_p < M/2`.

Classification: **conditional analytic theorem in the inherited near-resonant branch**.

This is a genuine owned deep-excursion / near-return geometry and is the most natural interface to RL20 strict-excursion packing.

It is not yet a contradiction.

---

## 12. Exact barriers found in RL101

### Barrier A — normalized versus absolute scale

The normalized cylinder fraction is stronger at larger `g`, but the absolute maximum ceiling still grows like

`(3/2)^(gq)/g`.

Existing RL85/RL87–RL100 physical-span constants therefore do not automatically become no weaker with `g`.

### Barrier B — the excursion need not grow with `g`

The proved aligned constraints are only

`d_h>=1`.

They permit, at the level of the current inequalities, the extremal pattern

`d_1=d_2=...=d_(g-1)=1`.

Thus raw multiplicity does not by itself force a block-count excursion whose cost grows with `g`.

### Barrier C — block-count algebra alone remains vulnerable to the RL20 coboundary

The new excursion uses genuine physical endpoints, but if the next argument discards those endpoints and keeps only canonical block count algebra, it falls back toward the inherited RL20 proper-factor/coboundary barrier.

Any RL102 promotion must preserve at least one of:

- exact full-cycle `D|Q(w_full)` content;
- a non-homogeneous ordinary-`+1` numerator;
- primitive owned rotations/states;
- a physical strip/packing quantity not reproduced by the `D∤Q` fake.

### Barrier D — no feasible finite multiplicity complement

RL101 does not reduce the unresolved multiplicities to an explicit computationally feasible set with certified eliminators. The inherited Beatty upper range is finite arithmetically, but no branch-by-branch elimination mechanism is available. RL101 Form C is therefore not satisfied.

---

## 13. RL101 red-team ledger

1. **RL79 ordinary-`+1` discriminator:** RL101.6 and RL101.7 use positivity of actual affine `+1` numerators; RL101.2–RL101.3 use the inherited physical envelope. No final theorem yet isolates denominator/content information impossible under generalized increment scaling.
2. **RL20 `D∤Q` fake:** normalized cylinder and low-state theorems do not yet consume global `D|Q(w_full)`. They are insufficient for multiplicity exclusion.
3. **RL81 common-mode warning:** RL101.6 and RL101.7 are explicitly physical states; no normalized quotient is treated as a bounded physical state.
4. **Raw multiplicity:** RL101.1–RL101.6 quantify over every admissible raw `g` at the fixed reduced first-Farey slope.
5. **Scope:** reduced slope `p/q` and raw pair `(gp,gq)` remain distinct throughout.
6. **External floor:** inherited `R#>=2^71` remains external computational input and is not upgraded.
7. **Cascade scope:** no raw-`g=1` interval exclusion is promoted to `g>=2` or global Gate A.

---

## 14. Frozen cascade checkpoint

No numerical cascade scan was run in RL101.

Retain exactly:

- wide `(D_w,R_w,L_w)=(5,000,030,7,000,000,5,000,053)`;
- middle `(D_m,R_m,L_m)=(7,500,031,4,500,000,7,500,053)`;
- deep `(D_d,R_d,L_d)=(10,000,032,3,250,000,10,000,053)`;
- ultra `(D_u,R_u,L_u)=(15,000,035,2,005,000,15,000,053)`.

The repaired middle depth

`D_m=7,500,031`

is mandatory.

Feasible supports remain exactly

- `A-C`;
- `C-D`;
- `D-E`.

Active support:

`lambda=234375/3281264468752`

`mu=1/7000001`

`floor(lambda*C)=3010`

`L_common=15,000,053`.

First live odd on the exact first-Farey/raw-`g=1`/full-phase branch:

`boxed: k=2,921,813,805`

with margin `-3,297`.

Previous odd

`2,921,813,803`

is excluded with margin `+10,323`.

Branch upper endpoint:

`42,150,931,559`.

---

## 15. Outgoing strategic recommendation

RL102 should **not** return immediately to bulk cascade scans.

Primary theorem target:

> Combine RL101's exponentially tiny physical first-surplus cylinder with full primitive cycle ownership to prove a nontrivial lower bound on the least cylinder representative, or an equivalent denominator-content contradiction.

The desired consumer must use at least one load-bearing feature absent from the current fake/coboundary models:

- `D|Q(w_full)`;
- ordinary-`+1` numerator content before normalization;
- primitive full-cycle rotation ownership;
- a two-sided physical excursion packing quantity.

Secondary target:

> In the proper equal-slope branch, feed RL101.7 into RL20 strict-excursion packing and determine whether the near-return `>15M/16` plus internal low state `<M/2` forces an impossible population/strip-width budget.

If both routes collapse to scale-free or coboundary identities, record the exact barrier and rerank direct Gate-B denominator-content architectures before resuming the numerical cascade.

# RL310 closeout — universal ownership/coercivity audit and canonical extremal route

Date: 2026-09-13
Status: CLOSED AND FROZEN
Session type: mathematical execution under RL309 redesigned roadmap

## 0. Executive conclusion

RL310 did not prove global non-trivial-cycle exclusion. Gate A and Gate B remain open.

It did, however, produce a coherent new global route and several theorem-sized advances which materially improve the parent problem. The most important late-session result is that every hypothetical primitive positive cycle has a **canonical physical minimum-to-maximum low arc** and, in the near-resonant branch, that arc induces a **canonical nonnegative transport flow** whose total mass is an exact extremal cross-determinant and whose height is forced by the physical aspect ratio.

The successor must continue from this extremal route. Do not automatically return to fixed-96 P/Q, H21, Radius 6+, or the older local Gate-A attack.

No result below should be treated as globally closing Collatz or even the non-trivial-cycle theorem unless the remaining upper-budget/compression implication is proved.

---

## 1. Incoming authoritative objective

RL310 started from:

`authoritative/RL310_UNIVERSAL_FULL_D_OWNERSHIP_COERCIVITY_GLOBAL_EXTRACTION_TARGET.md`

The target was a universal all-scale theorem extracting either:

- a direct contradiction;
- a universally bounded owned witness already excluded;
- a scale-growing owned discrepancy exceeding an independent resource budget;
- or an equivalent global closure.

The session obeyed the RL309 reset: local mature programmes were treated as tools/fallbacks, not as automatic priorities.

---

## 2. Early route A — accelerated odd-step population: proved, then frozen

Let the accelerated odd states be `u_j` and

`a_j = v_2(3u_j+1)`,

so `a_j>=1` and `sum_j a_j=A`.

The exact cycle product is

`2^A = product_j (3 + 1/u_j)`.

If `m=min u_j`, then

`A <= L log_2(3+1/m) <= L log_2(10/3)`.

Let

`N1 = #{j : a_j=1}`.

Since every `a_j>=1`,

`N1 >= 2L-A`, hence

`N1 >= [2-log_2(10/3)] L`,

with density approximately `0.263034`.

For a maximal run of consecutive `a=1` steps beginning at odd `u`, the run length is

`r = v_2(u+1)-1`,

because along the run

`u_{j+1}+1 = 3(u_j+1)/2`.

Thus

`N1 = sum_over_runs (v_2(u_start+1)-1)`.

### Barrier

The multiplicative `+1` defect decays with state size, while long contraction episodes remain unbounded. No all-scale coercive budget emerged.

Classification at checkpoint:

`PARENT_DIFFICULTY_DELTA = LATERAL`.

This mechanism is frozen.

---

## 3. Early route B — shifted forcing and moment hierarchy: exact but RL206-linear

With `y=u-1`, the ordinary shortcut recurrence becomes

`2y_{i+1}-3^{d_i}y_i = 3d_i-1`.

This was checked against RL206 and is only a constant translation of the existing recurrence-linear/coboundary family; it does not supply an independent obstruction.

A cyclic power-moment identity was also derived. Put

`E_p = sum_{d_i=0} R_i^p`,
`O_p = sum_{d_i=1} R_i^p`.

Then for every integer `p>=1`,

`(2^p-1)E_p-(3^p-2^p)O_p`
`= sum_{k=0}^{p-1} binom(p,k) 3^k O_k`.

In particular,

`E_1-O_1=L`,

and

`3E_2-5O_2 = 6O_1+L`.

### Barrier

The hierarchy is cyclic power invariance for rational cyclic solutions of the parity recurrence; it is ownership-blind and lies inside the RL206 killed family.

Classification:

`PARENT_DIFFICULTY_DELTA = LATERAL`.

Two consecutive lateral checkpoints froze this mechanism.

---

## 4. Early route C — quotient/content exactness: theorem, but no scale-growing budget

For the cyclic parity numerators `Q_i`, one obtains

`gcd(Q_0,...,Q_{A-1}) = gcd(D,Q_0)`.

The proof uses the one-step relation

`2Q_{i+1}-3^{d_i}Q_i = D d_i`

to propagate common divisors around the cycle and then back to `Q_0`.

Under genuine full-`D` ownership, `D|Q_0`, hence

`gcd(Q_0,...,Q_{A-1})=D`.

Writing `R_i=Q_i/D`,

`gcd(R_0,...,R_{A-1})=1`.

### Barrier

This does not produce a scale-growing content obstruction: every owned odd edge already satisfies

`2R_{i+1}-3R_i=1`,

so adjacent quotient states are automatically coprime. Together with the historical RL104 and RL119 barriers, quotient/content/residue was frozen.

Classification:

`PARENT_DIFFICULTY_DELTA = LATERAL`.

---

## 5. Whole-cycle/Farey pivot — new physical segment packing theorem

The session then pivoted to the RL83 maximum-ending surplus-segment/Farey programme, but with one new physical input: apply coprime-6 distinct-state packing **inside the segment**, not merely globally.

Suppose a maximum-ending surplus segment has raw counts

`(i,o)=(gp,gq)`, `gcd(p,q)=1`,

and put

`epsilon = p ln 2 - q ln 3 > 0`.

RL83 gives

`g epsilon <= S`,

where `S` is the sum of `ln(1+1/(3y))` over the segment's odd physical states.

The `o=gq` odd states are distinct and nonzero modulo 3, hence lie in residues `+-1 mod 6`. If sorted as

`y_0<...<y_{o-1}`,

then uniformly

`y_0>=R`,

`y_j>=R+3j-1` for `j>=1`,

where `R` is the genuine cycle minimum.

Using `ln(1+t)<=t` and a decreasing integral,

`S <= 1/(3R) + (1/9) ln((R+3o-4)/(R-1))`.

Therefore

`boxed:`

`g epsilon <= 1/(3R)`
`             + (1/9) ln(1 + 3(gq-1)/(R-1)).`

This is the RL310 segment-packing theorem.

The decisive change is the dependence on `g`: the left side is linear in `g`, while the physical packing envelope grows only logarithmically.

A parameter-free consequence follows from `R>=5` and `ln(1+x)<=sqrt(x)`:

`g <= max(2/(15 epsilon), q/(27 epsilon^2)).`

Classification:

`PARENT_DIFFICULTY_DELTA = EASIER`.

---

## 6. Exact first-Farey multiplicity contraction

Under the inherited external floor

`R>=R0=2^71`,

RL83's first admissible reduced surplus slope is

`p*=114208327604`,

`q*=72057431991`.

Put

`epsilon*=p* ln2-q* ln3`.

The exact rational-interval verifier in

`sessions/RL310/verify_rl310_extremal_and_farey.py`

certifies

`epsilon* > 0`,

and for

`B(g)=1/(3R0)+(1/9)ln(1+3(gq*-1)/(R0-1))`,

it certifies:

- `G=22,623,517,356` has `G epsilon* - B(G) < 0`;
- `G+1` has `(G+1) epsilon* - B(G+1) > 0`;
- `epsilon* > B'(G+1)`;
- `B'(g)` decreases thereafter.

Hence every `g>=22,623,517,357` is excluded by the segment-packing inequality:

`boxed: g <= 22,623,517,356.`

RL100's first-crossing arithmetic alone had allowed

`g <= 125,777,718,029`.

Thus the first Farey raw-multiplicity fibre contracts by a factor about `5.56`.

This is an exact finite arithmetic certificate plus the inherited floor, not a global closure.

---

## 7. Global multiplicity-fibre theorem

The same packing theorem applies to the full cycle. If the reduced global slope is

`A/L=P/Q`,

and

`A=GP`, `L=GQ`,

then with

`epsilon=P ln2-Q ln3>0`,

`G epsilon <= 1/(3R)`
`             + (1/9)ln(1+3(GQ-1)/(R-1)).`

Therefore every fixed reduced global slope has only finitely many possible raw multiplicities `G`.

The same parameter-free estimate yields

`G <= max(2/(15 epsilon), Q/(27 epsilon^2)).`

### Structural consequence

The old arithmetic freedom

`(reduced slope, raw multiplicity)`

is reduced to

`one unbounded reduced slope + a finite multiplicity fibre over each slope`.

This materially repairs the historical RL100 raw-multiplicity obstruction.

### Exact remaining barrier

The Farey tail itself remains infinite. The `G=1` branch survives arbitrarily large reduced denominators as the rational slope approaches `log_2 3`.

Thus physical packing alone cannot turn the entire Farey family into a finite list.

Classification:

`PARENT_DIFFICULTY_DELTA = EASIER`.

---

## 8. Explicitly rejected false bridge: proper-prefix ownership

In the equal local/global slope case, RL83 gives

`D_g=2^(gp)-3^(gq)`,

`D_G=2^(Gp)-3^(Gq)`.

If `g|G`, then `D_g|D_G`.

RL310 tested whether full ownership modulo `D_G` implied that the proper prefix itself was owned modulo `D_g`.

It does **not**.

`D_g|D_G` only couples the complementary arc algebraically. It does not imply that the first arc numerator is divisible by `D_g`.

Do not resurrect this as a valid local-ownership theorem. It would be the exact sort of silent strengthening warned against by RL104.

---

## 9. Universal extremal aspect-ratio theorem

This is the first major late-session global theorem.

Let

`R=min C`, `M=max C`,

for a hypothetical primitive positive cycle. Let `L` be the number of odd phase states.

Sort those odd states:

`R=y_0<y_1<...<y_{L-1}`.

Because every odd cycle state is nonzero modulo 3,

`y_j>=R+3j-1` for `j>=1`.

Hence

`M>=R+3L-4`.

The exact whole-cycle product is

`lambda := 2^A/3^L`
`        = product_j (1+1/(3y_j)).`

The same packing estimate gives

`ln lambda <= 1/(3R)`
`            +(1/9)ln((R+3L-4)/(R-1)).`

Set

`X=(R+3L-4)/R`.

For `R>=5`, `L>=2`,

`8 ln X > 3/R + ln(R/(R-1))`.

A sufficient elementary chain is

`8 ln(1+2/R) >= 16/(R+2)`

and

`3/R + ln(R/(R-1)) <= 3/R + 1/(R-1)`,

with exact difference

`16/(R+2)-3/R-1/(R-1)`
`=3(4R^2-7R+2)/(R(R-1)(R+2)) > 0`.

Therefore

`boxed: lambda < M/R.`

Equivalently,

`boxed: 2^A/3^L < M/R.`

The elementary inequality is also sanity-checked by the RL310 verifier.

---

## 10. Universal canonical low/high extremal split

Use RL84's exact minimum/maximum arc factorization.

Let the forward physical arc

`R -> ... -> M`

have length `d` and odd count `o`, and define

`u=2^d/3^o`.

For the complementary arc

`M -> ... -> R`,

put

`v=2^(A-d)/3^(L-o)`.

Then

`lambda=uv`.

RL84 proves

`v > M/R`.

RL310 now proves

`lambda < M/R < v`.

Hence

`boxed: u<1`,

that is,

`boxed: 2^d < 3^o.`

So **every** hypothetical primitive positive cycle has a canonical owned low/high decomposition whose endpoints are the actual physical extrema.

The former RL84 high-branch alternative is eliminated completely.

This yields the canonical two-sided slope bracket

`boxed:`

`d/o < log_2 3 < A/L < (A-d)/(L-o).`

Define the extremal cross-determinant

`kappa_ext := A o - d L > 0`.

Then the same integer measures both rational gaps:

`A/L - d/o = kappa_ext/(Lo)`,

`(A-d)/(L-o) - A/L = kappa_ext/[L(L-o)].`

Classification:

`PARENT_DIFFICULTY_DELTA = EASIER`.

This is a universal owned global object, not a selected local witness.

---

## 11. Exact physical-extremum to transport-coercivity bridge

Root the parity word at the physical minimum `R`, and rotate it by the canonical extremal distance `d`, so the new root is `M`.

Let `G_i` be RL19's prefix-flow difference between the rotated and unrotated words, and let `q_i>0` be RL19's positive prefix weights.

RL19's exact weighted rotation identity gives

`sum_i q_i(3^(-G_i)-1)`
`=4(lambda-1)(M-R)`.

Since

`sum_i q_i=(lambda-1)(4R+1)`,

RL310 obtains

`boxed:`

`[sum_i q_i 3^(-G_i)]/[sum_i q_i]`
`= (4M+1)/(4R+1).`

Therefore some index satisfies

`-G_i >= h`,

where

`h = ceil(log_3((4M+1)/(4R+1))).`

For the rotation by `d`,

`G_i=W_i(d)-o`,

where `W_i(d)` is the odd count in the cyclic length-`d` window starting at `i`.

Thus `G` is a cyclic integer 1-Lipschitz walk and has range at least `h`.

For the cyclic earth-mover distance of this rotation,

`R_ext = min_c sum_i |G_i-c|`.

Any cyclic integer 1-Lipschitz walk of range `H` has

`min_c sum_i |G_i-c| >= ceil(H^2/2)`.

Hence

`boxed:`

`R_ext >= ceil( (ceil(log_3((4M+1)/(4R+1))))^2 / 2 ).`

Using `M>=R+3L-4` gives an explicit lower bound in `R,L`.

### Interpretation and barrier

This is a genuine physical-ownership -> combinatorial-discrepancy theorem.

But its direction is toward **large** transport radius. RL274 already diagnosed that large counterflow by itself does not feed the Radius-3/4/5 obstruction library.

Classification:

`PARENT_DIFFICULTY_DELTA = LATERAL`.

---

## 12. Near-resonant canonical one-sided extremal transport

This is the live frontier at closeout.

Assume the near-resonant branch

`lambda=2^A/3^L < 3`.

For every cyclic start `i`, let `x_i` be the physical phase state and `W_i(d)` the number of odd inputs in the length-`d` segment from `x_i` to `x_{i+d}`.

Write the segment `+1` log mass as `S_i>=0`. Then

`ln(x_{i+d}/x_i)`
`=W_i(d) ln3 - d ln2 + S_i`.

For the true extremal arc from `R` to `M`,

`ln(M/R)=o ln3-d ln2+S_0`.

Because every phase lies in `[R,M]`,

`x_{i+d}/x_i <= M/R`.

Subtracting,

`(W_i(d)-o)ln3 <= S_0-S_i <= S_0`.

Since

`S_0 <= ln lambda < ln3`,

and `W_i(d)-o` is integral,

`boxed: W_i(d) <= o for every cyclic i.`

Thus the true `R->M` arc has the **maximum odd count among all cyclic length-d windows**.

Define

`P_i := o-W_i(d)`.

Then

`boxed: P_i>=0`,

`P_0=0`,

`P_{i+1}-P_i in {-1,0,1}`.

Every odd bit lies in exactly `d` length-`d` windows, so

`sum_i W_i(d)=dL`.

Therefore

`boxed:`

`sum_i P_i = A o-dL = kappa_ext.`

So `P` is a canonical **nonnegative owned transport flow** for the extremal self-rotation, with exact flow cost `kappa_ext`.

The weighted extremal identity becomes

`[sum_i q_i 3^(P_i)]/[sum_i q_i]`
`=(4M+1)/(4R+1)`.

Hence `max_i P_i>=h`, with

`h=ceil(log_3((4M+1)/(4R+1))).`

A cyclic nonnegative integer 1-Lipschitz walk having a zero and reaching height `h` has total mass at least `h^2`. Therefore

`boxed:`

`kappa_ext = A o-dL`
`>= ceil(log_3((4M+1)/(4R+1)))^2.`

Using state packing,

`boxed:`

`kappa_ext`
`>= ceil(log_3((4R+12L-15)/(4R+1)))^2.`

This is the strongest live theorem at closeout.

Classification:

`PARENT_DIFFICULTY_DELTA = EASIER`.

A previously arbitrary signed canonical self-rotation flow has collapsed, in the principal near-resonant branch, to a one-sided nonnegative flow with exact total mass and a physical quadratic coercivity law.

---

## 13. Exact live obstruction

The global proof is not closed because no theorem yet supplies an independent incompatible **upper** bound on

`kappa_ext = Ao-dL`,

nor an owned compression theorem converting this large one-sided extremal flow into a bounded-radius primitive/full-D witness.

The next proof must attack that precise point.

The most promising formulations are:

1. **Extend one-sidedness beyond the sufficient `lambda<3` hypothesis.**
   The exact condition used is only `S_0<ln3`, where `S_0` is the `+1` log mass of the actual `R->M` arc. Either prove this universally, or handle the complementary branch `S_0>=ln3` by a separate global contradiction.

2. **Upper-budget theorem for the same extremal determinant.**
   Find a genuinely independent physical/full-D/phase resource forcing an upper bound on `Ao-dL` that is incompatible with the quadratic lower bound above.

3. **Owned compression from one-sided extremal flow.**
   Use `P_i>=0`, `P_0=0`, `sum P=kappa_ext`, full-D ownership and primitivity to force a bounded-radius owned self-rotation already excluded by Radius 3/4/5.

4. **Owned replication.**
   Show that the extremal one-sided profile forces repeated independently owned zero-rich or phase-rich features whose cumulative cost exceeds a global budget.

5. **Gate-A/B splice only if exact.**
   RL274's determinant-discrepancy identities can be used, but the extremal determinant is not automatically the historical determinant-2 sector. Do not silently identify them.

---

## 14. Frozen negative controls

Do not automatically resume or rediscover:

- shifted/coboundary recurrence forcing (RL206 family);
- quotient gcd/content/residue as a scale-growing obstruction;
- direct prime/order/cylinder-residue ownership after division by `D` (RL104 barrier);
- p-adic variable-prime families without a new global mechanism (RL119 barrier);
- finite Farey enumeration as though it covers the infinite tail;
- proper-prefix ownership from `D_g|D_G`;
- fixed local pattern escalation without a growing ownership theorem;
- Radius 6+ enumeration without an encounter/extractor theorem;
- the claim that large extremal discrepancy alone is a contradiction.

The exact first-Farey packing theorem and extremal theorems are preserved as tools even if the successor later pivots.

---

## 15. Verification material

New exact verifier:

`sessions/RL310/verify_rl310_extremal_and_farey.py`

It certifies:

- positivity of the first-Farey logarithmic error by exact rational intervals;
- the exact cap `g<=22,623,517,356` under `R>=2^71`;
- the sign change at `g+1`;
- monotonic exclusion thereafter;
- the elementary rational inequality used in the universal extremal split.

The structural theorems themselves are analytic and do not depend on floating-point computation.

---

## 16. Proof-state classification at closeout

Promoted by this closeout as RL310 research results, subject to the ordinary project convention that theorem statements retain their explicit hypotheses:

- accelerated `a=1` population/run lemma;
- moment hierarchy and its RL206 barrier classification;
- cyclic numerator gcd/content theorem;
- segment coprime-6 multiplicity-compression theorem;
- exact first-Farey multiplicity cap under inherited `R>=2^71`;
- finite raw-multiplicity fibre over every fixed reduced slope;
- universal aspect-ratio theorem `lambda<M/R`;
- universal canonical extremal low/high split;
- canonical two-sided slope bracket and positive extremal cross-determinant;
- physical-extremum -> transport-coercivity theorem;
- near-resonant (`lambda<3`) canonical one-sided extremal transport theorem;
- exact barrier statements listed above.

Still open:

- upper budget/compression for `kappa_ext`;
- exhaustive handling beyond the current sufficient near-resonant one-sidedness condition;
- Gate A;
- Gate B;
- global non-trivial-cycle exclusion.

No Collatz conjecture claim is made.

---

## 17. Successor direction

The next authoritative research session should **continue this route**, because the late RL310 checkpoints materially changed the proof architecture.

Primary successor target:

> Convert the canonical extremal low/high split and, where available, the one-sided flow `P_i=o-W_i(d)>=0` with `sum P=Ao-dL` into an incompatible upper resource bound or into a bounded owned full-D witness already excluded by the local obstruction library.

The first task is to make the one-sided entrance exhaustive: sharpen `lambda<3` to the exact segment condition `S_0<ln3` and attack the complementary branch directly.

Only if this route fails under a precise barrier should the successor fall back to Gate A/B.

---

## 18. Repository state

RL310 is closed and frozen.

The exact verifier and this closeout are now repository-resident.

The successor authoritative target is prepared separately and `authoritative/START_HERE.md` should point to it.

Lean formalisation remains a separate project and is not part of this closeout.

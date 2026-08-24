# Collatz R# RL-6 — Good Rotations, Exact Boundary Cancellation, and Denominator Defect

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-5  
**Verdict:** RL remains open. RL-6 resolves the *structural form* of the exact saturation-boundary exception to RL-L41: every admissible cyclic word has a rotation with automatic exact 3-adic numerator signature, and from that rotation all remaining 3-adic work is confined to explicit finite-depth boundary cancellation gates. This yields a necessary-and-sufficient generalized realization criterion for arbitrary admissible words. A separate minimum-anchor argument gives a direct upper/lower budget for the common denominator defect `D/2^A`.

## 1. Inherited notation

For a cyclic compressed anchor word, transition `j` carries

`(n_j, t_j, mu_(j+1))`.

Put

`mu_j = mu_next of transition j-1`,

`s_j = n_j-mu_j >= 1`,

`M = sum_j mu_j`,

`L = sum_j s_j`,

`A = L + sum_j t_j`,

`D = 2^A-3^L > 0`,

`K = 6^M D`.

The integer affine transition is

`d_j W_(j+1) = ell_j W_j + c_j`,

with

`ell_j = 2^(mu_(j+1)) 3^(n_j)`,

`c_j = 2^(n_j+mu_(j+1)) (2^(t_j)-1)`,

`d_j = 2^(n_j+t_j) 3^(mu_(j+1))`.

For every rotation `r`, composition gives

`W_r = C_r/K`

as the unique rational candidate, and the rotation numerators obey

`d_j C_(j+1) = ell_j C_j + c_j K`.      (R42.1)

RL-L40 already proves

`v2(C_r)=M+n_r`      (R42.2)

for every valid word and every rotation.

For one transition put

`r_j = v3(2^(t_j)-1)`,

`a_j = r_j-mu_(j+1)`,

`h_j = n_j-mu_(j+1)`.      (R42.3)

The local valuation law gives exactly:

- `r_j<n_j`: `(a_j,h_j)=(0, positive)`;
- `r_j>n_j`: `(a_j,h_j)=(positive,0)`;
- `r_j=n_j`, `mu_(j+1)=n_j+c_j^*`: `(a_j,h_j)=(-c_j^*,-c_j^*)`, where `c_j^*>=0` is the declared cancellation depth.

Cyclically,

`sum_j h_j = sum_j n_j - sum_j mu_(j+1) = L > 0`.      (R42.4)

The symbol `c_j^*` below is a cancellation depth and is distinct from the affine constant `c_j`.

## 2. RL-L42 — every admissible word has a 3-adically good rotation

Expand one rotation numerator as in RL-L40:

`C = sum_i T_i`,

`T_i = c_i (product_(k<i) d_k) (product_(k>i) ell_k)`.

Writing

`H_i = sum_(k=i)^(P-1) h_k`,

RL-L40 gives

`v3(T_i)-M = a_i + H_(i+1)`.      (R42.5)

Here `H_P=0`.

### Cycle-lemma choice of rotation

Because the cyclic integer word `(h_j)` has positive total `L`, apply the elementary cycle lemma to the reversed height word. There exists a rotation for which **every nonempty suffix sum is strictly positive**:

`H_i > 0` for every `0<=i<P`.      (R42.6)

Call any such rotation a **3-adically good rotation**.

In particular the final step satisfies

`h_(P-1)=H_(P-1)>0`,

so it is necessarily an unsaturated step `r_(P-1)<n_(P-1)` with `a_(P-1)=0`.

Now inspect (R42.5).

- For the final step,
  `v3(T_(P-1))-M = 0`.
- For any earlier unsaturated step, `a_i=0` and `H_(i+1)>0`.
- For any oversaturated non-boundary step `r_i>n_i`, both `a_i>0` and `H_(i+1)>0`.
- For an exact boundary with cancellation depth `c_i^*`, `a_i=h_i=-c_i^*`, hence

  `a_i+H_(i+1)=H_i>0`.

Therefore the final term is the **unique** 3-adically minimal term and

`v3(C_good)=M`.      (R42.7)

This holds whether or not the word contains exact saturation boundaries, and regardless of their declared cancellation depths.

**Status: PROVED ANALYTIC THEOREM.**

### Consequence

RL-L40's generic result is strengthened in a different direction. Boundary words need not have automatic `v3(C_r)=M` at every rotation, but they always have at least one canonically selectable rotation where the signature is automatic.

## 3. RL-L43 — exact boundary transport gate

Assume at some rotation `j` that

`v3(C_j)=M`.      (R43.1)

### Non-boundary edge

If `r_j != n_j`, the two terms on the right of (R42.1) have 3-adic valuations

`M+n_j`

and

`M+r_j`.

They are unequal. Therefore there is no cancellation, and subtracting

`mu_(j+1)=min(n_j,r_j)`

from the valuation of the left coefficient gives

`v3(C_(j+1))=M`.      (R43.2)

Thus **every non-boundary edge propagates the exact numerator unit signature automatically**.

### Exact boundary edge

Now let

`r_j=n_j`,

`mu_(j+1)=n_j+c_j^*`,

`H_j^* = (2^(t_j)-1)/3^(n_j)`,      (R43.3)

where `H_j^*` is a 3-adic unit.

Because `v3(C_j)=M`, put

`C_hat_j = C_j/3^M`,

which is a 3-adic unit. Factoring `3^(M+n_j)` from the right side of (R42.1) gives a cancellation depth

`kappa_j = v3(C_hat_j + 2^(M+n_j) D H_j^*)`.      (R43.4)

(The omitted factor is a power of 2 and hence a 3-adic unit.)

Since the left coefficient contributes `n_j+c_j^*` powers of 3,

`v3(C_(j+1))-M = kappa_j-c_j^*`.      (R43.5)

Hence

`v3(C_(j+1))=M  <=>  kappa_j=c_j^*`.      (R43.6)

This is the exact **boundary cancellation gate**.

It is finite-depth: checking `kappa_j=c_j^*` requires only the residue modulo `3^(c_j^*+1)`.

If additionally `D|C_j`, then

`W_j=C_j/(6^M D)=2^(n_j) q_j`

is an integer 3-adic unit, and (R43.4) reduces to the familiar local cancellation law

`kappa_j = v3(q_j+H_j^*)`.      (R43.7)

Thus the local RL-L32 cancellation depth is now coupled exactly to the unique global rotation numerator candidate.

**Status: PROVED ANALYTIC THEOREM.**

## 4. RL-L44 — generalized one-rotation criterion, including exact boundaries

Call a cyclic word **admissible** if the local `mu_(j+1)` values satisfy RL-L32, including arbitrary declared exact-boundary depths `c_j^*>=0`, and if every cyclic physical suffix length satisfies

`s_j=n_j-mu_j>=1`.

Assume `D>0`.

Choose a good rotation `g` from RL-L42. Then

`v2(C_g)=M+n_g`,

`v3(C_g)=M`      (R44.1)

are automatic.

The divisibility transport identity from RL-L41 did not use genericity, so

`D|C_j <=> D|C_(j+1)`      (R44.2)

still holds across every edge.

Suppose first that

`D|C_g`.      (R44.3)

Then `K|C_g`, so the good-rotation anchor candidate is a positive integer 6-adic unit with the declared `n_g`.

Move forward around the word.

- At every non-boundary edge, RL-L43 preserves `v3(C)=M` automatically.
- At every exact boundary, require the finite gate

  `kappa_j=c_j^*`.      (R44.4)

If all boundary gates pass, then every rotation has

`v2(C_r)=M+n_r`,

`v3(C_r)=M`,

and `D|C_r`.

Therefore every

`W_r=C_r/(6^M D)`

is a positive integer with

`v2(W_r)=n_r`, `v3(W_r)=0`.      (R44.5)

The exact affine identity then repeats the sufficiency argument of RL-L41 without any genericity assumption. Writing `W_j=2^(n_j)q_j`, it forces

`v2(3^(n_j)q_j-1)=t_j`,

and, for

`z_j=(3^(n_j)q_j-1)/2^(t_j)`,

it forces

`v3(z_j+1)=mu_(j+1)`

and

`xi(z_j)=W_(j+1)`.

So the declared word is the exact Collatz anchor orbit.

Conversely any realized periodic anchor orbit necessarily satisfies `D|C_g` and every boundary cancellation gate.

Therefore:

> **For every admissible cyclic compressed word, a positive periodic integer anchor orbit exists if and only if `D` divides the numerator at one 3-adically good rotation and every exact-boundary edge passes its declared cancellation-depth gate.**      (R44.6)

For generic words there are no boundary gates, so RL-L44 reduces exactly to RL-L41.

**Status: PROVED ANALYTIC THEOREM.**

### Strategic consequence

The exact-boundary exception to RL-L41 is no longer an unresolved all-rotation integrality problem. It is a finite list of explicit 3-adic residue gates. The only genuinely global arithmetic obstruction left is still `D|C_good`.

## 5. RL-L45 — minimum-anchor denominator-defect budget

Return to the exact multiplicative-ceiling form

`W_(j+1)=a_j W_j+e_j`,

where

`a_j=3^(h_j)/2^(h_j+t_j)`,

`e_j=(2/3)^(mu_(j+1)) (1-2^(-t_j))`,

`0<e_j<1`.      (R45.1)

For any admissible word with `D>0`, the unique rational periodic candidates are positive. Rotate them so that

`W_0=W_* = min_j W_j`.      (R45.2)

Put

`rho = product_j a_j = 3^L/2^A`,

so

`1-rho = D/2^A`.      (R45.3)

Composing from the minimum gives

`W_* = rho W_* + sum_i e_i B_i`,      (R45.4)

where

`B_i = product_(k=i+1)^(P-1) a_k`

is the multiplicative coefficient of the suffix after transition `i`.

For `i<P-1`, the suffix recurrence back to the minimum has positive additive error, hence

`W_* > B_i W_(i+1)`.

Since `W_(i+1)>=W_*`,

`0<B_i<1`.      (R45.5)

For the closing transition, `B_(P-1)=1`.

Define the explicit local error budget

`E_mu = sum_i e_i`

`= sum_i (2/3)^(mu_(i+1)) (1-2^(-t_i))`.      (R45.6)

If `P>1`, (R45.4)-(R45.5) give the strict bracket

`e_close/W_* < D/2^A < E_mu/W_* < P/W_*`.      (R45.7)

Equivalently,

`e_close 2^A/D < W_* < E_mu 2^A/D`.      (R45.8)

This is a direct denominator-defect restriction derived from the ceiling orbit itself.

### k=0 RL specialization

For the least-red cycle root,

`W_*=R#+1`,

and the closing transition has `mu_next=0`, so

`e_close = 1-2^(-t_close)`.      (R45.9)

Hence any nontrivial k=0 RL word must satisfy

`(1-2^(-t_close))/(R#+1) < D/2^A < E_mu/(R#+1)`.      (R45.10)

Using the accepted computational guardrail that all starting values below `2^71` converge, any least-red counterexample satisfies `R#>=2^71`; therefore

`D/2^A < E_mu/(2^71+1) < P/(2^71+1)`.      (R45.11)

This is not a proof of nonexistence, but it makes the denominator target explicitly near-resonant before any numerator divisibility is tested.

**Status: PROVED ANALYTIC THEOREM + EXTERNAL LOWER-BOUND COROLLARY.**

## 6. RL-X10 — exact verifier

The new verifier is

`tools/verify_rl6_boundary_good_rotation.py`.

It performs:

- 6,370 symbolic good-rotation existence/unique-minimum audits on admissible words with boundaries included;
- 6,370 symbolic checks that the boundary-gate scan is equivalent to the direct all-rotation `v3(C_r)=M` signature;
- an exhaustive generalized-criterion audit in the RL-5 diagnostic domain `P<=3`, `n,t<=6`, cancellation depth `<=2`;
- 4,062 exact rational-orbit audits of the minimum-anchor denominator-defect bracket.

In the exhaustive diagnostic domain:

- admissible positive-slope words: `37,057`;
- words containing exact boundaries: `11,278`;
- boundary words passing all 3-adic gates: `3,593`;
- words with `D` dividing the good-rotation numerator: `3`;
- generalized criterion survivors: `3`;
- nontrivial survivors: `0`.

The three survivors are repetitions of the trivial `W=2` anchor.

This is an exact finite certificate only on the declared domain.

**Status: EXACT FINITE CERTIFICATE.**

## 7. What is now closed, and what is not

### Closed structurally

The RL-5 Rank-2 task—classifying the exact saturation-boundary exception—has been completed at the level needed for the global integrality argument:

1. a good rotation always supplies the initial exact 3-adic numerator unit;
2. generic edges propagate it automatically;
3. boundary edges are exact finite-depth congruence gates;
4. `D|C_good` plus those gates is necessary and sufficient for full realization.

There is no longer a separate mysterious all-rotation 3-adic cancellation problem.

### Still open

The hard global condition remains

`D | C_good`,      (R46.1)

or equivalently at any rotation, since `D`-divisibility propagates.

For the k=0 RL branch this must be attacked together with:

- the forced-low departure from the least root;
- strict minimum of all non-root anchors;
- the final odd high return;
- the exact final-return discrete-log class `t_close mod 2*3^(n_close-1)`;
- the new denominator-defect budget (R45.10).

The next theorem should make one of those endpoint gates visible modulo a divisor of `D`, or force a denominator descent/lift contradiction.

## 8. External guardrails rechecked

A targeted literature recheck on 2026-08-19 found the published Barina 2025 verification result through `2^71`, together with the reported nontrivial-cycle length consequence `355,504,839,929`. Hercher's `m>=92` theorem remains the accepted local-minimum exclusion used by RL-L35. A 2026 paper by Angeltveit gives a faster verification algorithm but does not, in the source checked here, replace the published `2^71` verified bound with a higher completed range.

No external source is being used as proof of RL itself.

## 9. Verdict

RL is **not solved**.

The main advance is nevertheless exact: the boundary case has been compressed to a good-rotation scalar denominator test plus finite local cancellation gates. This means the next phase can stop treating boundary numerators as a separate global obstacle and return full attention to the one global arithmetic question that survives both generic and boundary words:

`D | C_good`.

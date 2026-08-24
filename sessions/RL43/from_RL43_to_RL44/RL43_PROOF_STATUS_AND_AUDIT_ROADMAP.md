# RL43 proof status and RL44 audit road map

Date: 2026-08-22

## 1. Retained branch only

All RL43 claims live inside the inherited surviving near-resonant order-2 / `g=2` balanced-return branch unless a note explicitly says otherwise. None of RL43 proves the Collatz conjecture or closes all RL.

## 2. Status ledger

### A. Analytic statements introduced in RL43

1. Excursion excess/gap inequality:
   `D_E / 3^p < 2^(e+1)` and therefore physical crossing gap `g < 2^(e+1)`.
2. Synchronization cost:
   if `c` common odd columns immediately precede a crossing, `e >= floor(c log_2 3)`.
3. Defect-support compression:
   with total excursion excess `E` and excursion count `N`, the proper-factor numerator has a signed `2^r 3^s` representation with at most `4(E+N)` terms before collection.
4. One-excursion full-denominator phase relation:
   `P(rho)=0 mod (X-Y)` with `P(T)=4+3 sum(T^b-T^c)` and at most `2e+3` terms.
5. Short phase binomial:
   `3 rho^q = 2 mod (X-Y)`, `q=a-ell`.
6. Nonzero resultant gateway:
   `0 != Res(3T^q-2,P(T))` and `X-Y` divides it.
7. Exact binomial resultant identity used as a bridge marker:
   `|Res(3T^q-2,2T^ell-1)| = 2^a-3^ell = X-Y` when `q=a-ell` and the retained coprimality assumptions hold.

### B. Analytic + exact finite certificate

1. `rho=49` is eliminated, hence inherited `rho>=49` becomes **`rho>=50`**.
2. Gap-9 cutoff-free automaton theorem: any canonical positive excursion entering with physical gap 9 and crossing negative has **`e>=8`**. The proof idea is finite-state at fixed excess after quotienting a single neutral pump; the verifier is a certificate/sanity implementation of that exact reduction.

### C. Exact computation awaiting independent audit

The one-excursion phase DP finds no full-denominator residue solution for all admissible normalized geometries with `26<=e<=40`. If the geometry exhaustion and DP are independently confirmed, the one-excursion computational frontier is `e>=41`.

This result is intentionally **not promoted here to an analytic theorem**.

### D. Conjectural / proof target

The sharp pattern

`e >= q+2`, `q=a-ell`,

or equivalently in the one-excursion branch

`rho_E >= a`

is not proved.

A proposed normalization is recorded in `RL43_JK_INVARIANT_CANDIDATE.md`.

## 3. Why the bridge is closer than before

The important change is not the numerical frontiers `rho>=50` or computational `e>=41`. Arbitrary-radius one-excursion transport is now compressed to a defect-controlled sparse phase polynomial against the **same short binomial `3T^q-2` that occurs in the inherited radius-3 closure**.

The missing bridge is therefore quantitative and structural:

- either show defect cannot grow in a manner compatible with near resonance/full denominator divisibility;
- or transplant the RL19 resultant-size/uniqueness mechanism from uniformly tiny radius-3 support to defect-controlled support;
- or prove a transport theorem such as `rho_E>=a` that couples defect to the Diophantine scale strongly enough to force the sparse resultant contradiction.

## 4. Ranked RL44 road map

### Priority 1 — audit before extension

Reconstruct all RL43 analytic identities and rerun every verifier. Verify every imported RL19/RL21/RL38/RL42 premise. Produce a dependency graph that distinguishes proved, externally dependent, finite-certified, and heuristic statements.

### Priority 2 — attack the `J_d/K` invariant

Try to prove or falsify the proposed invariant. Descent already has an exact normalization; the unresolved transitions are `00`, `11`, and upward `01`. Search for a stronger local statement preserved under all transitions or a minimal-counterexample argument.

If the stated invariant is false, determine the sharp replacement: e.g. a valuation inequality with an additive constant or a signed/ordered quotient condition sufficient to imply `H>=t+3` at the terminal state.

### Priority 3 — transplant the RL19 short-binomial argument

Locate the exact RL19 radius-3 lemma using `3T^q-2`. Rewrite it in terms of the RL43 `P(T)`. Determine which bound depended on radius exactly 3 and whether `R<=e+1`, positivity `0<b<c`, or run pairing can replace it.

The goal is a theorem of the form:

`X-Y | Res(3T^q-2,P)` + near resonance + defect constraints => contradiction,

uniformly in `e`.

### Priority 4 — generalize beyond one excursion

The global defect-support theorem already handles many excursions for `U-V`. Work out the corresponding full-`D` phase relation modulo `X-Y` with support controlled by `E+N`, and identify whether inter-excursion synchronized blocks introduce only phase shifts or genuinely new algebra.

A genuine RL closure needs this step unless a separate argument forces `N=1`.

### Priority 5 — finite computation only as reconnaissance

Do not spend the session merely extending `e=40`. Extend it only if needed to test a proposed invariant, locate a minimal counterexample, or reveal a new skeleton family relevant to a uniform proof.

## 5. Stop conditions

- Any inherited or RL43 verifier failure: stop, repair, and downgrade affected claims.
- Any counterexample to the `J_d/K` invariant: record it immediately and salvage the weakest true replacement.
- Any hidden finite cutoff in a purported cutoff-free claim: downgrade it.
- Any use of an unresolved external conjecture: isolate it explicitly; do not treat it as a theorem.

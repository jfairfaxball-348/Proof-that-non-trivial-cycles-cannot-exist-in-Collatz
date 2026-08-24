# RL21 — half-high odd-state packing and a stronger continued-fraction gate

Date: 2026-08-20

## Status

Sections 1--3 are **ANALYTIC**.  Section 4 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R#>=2^71`.

This note strengthens the RL20 global state-packing/continued-fraction gate using a simple cycle-injectivity observation that was exposed by the integer-gap synchronization work.

## 1. Low odd states inject into high odd states

Let `R` be the least state of a nontrivial positive full-parity Collatz cycle, and let `x` be any odd phase state.

Put

`H=(4R-1)/3`.

Suppose

`x < H`.

Then its immediate odd-step image is

`T(x)=(3x+1)/2 < 2R`.                                      (R21P.1)

If `T(x)` were even, the next full-parity step would be

`T^2(x)=T(x)/2 < R`,

contradicting leastness.  Therefore `T(x)` is itself odd.

Moreover

`T(x) >= (3R+1)/2 > (4R-1)/3 = H`.                        (R21P.2)

Thus every odd state below `H` maps in one cycle step to an odd state above `H`.  In fact the image satisfies the stronger bound

`T(x) >= (3R+1)/2`.                                      (R21P.2a)

Because the states on a primitive cycle form a directed cycle, the successor map is injective on phase states.  Distinct low odd states therefore have distinct high odd successors, and these low/high pairs are disjoint.

Hence, writing `L_low` and `L_high` for the numbers of odd states below and at/above `H`,

`L_low <= L_high`.                                         (R21P.3)

Since `L_low+L_high=L`,

> **At least half of all odd cycle states satisfy**
>
> `x >= (4R-1)/3`.                                         (R21P.4)

This statement is independent of the balanced-return branch.

A useful local corollary is that every odd phase below `(4R-1)/3` must be `3 mod 4`: otherwise its odd-step image would be even and would force the forbidden descent below `R` on the next step.

## 2. Strengthened global odd-step product bound

RL19 proved the exact product identity

`lambda = 2^A/3^L = product_(odd phases x) (1+1/(3x))`.

At most half of the `L` odd states can lie below `H`; at least half lie at or above `H`.

Pair each low odd state `x` with its distinct odd successor `T(x)`.  A low member is at least `R`, while its paired successor is at least `(3R+1)/2`.  Every unpaired odd state is not low, hence is at least `H=(4R-1)/3`.

For `R>=5`, the single-state factor at `H` is no larger than the geometric mean of the worst low/high pair factors; exactly,

`(1+1/(4R-1))^2`
` <= (1+1/(3R)) (1+2/(9R+3))`,                            (R21P.5)

because the difference of the two sides has numerator `8R^2-31R+5>0`.  (Every nontrivial cycle has `R>=5`; RL20 already proves no phase is divisible by `3`.)

Therefore the whole odd-state product satisfies the matched-pair bound

`log lambda / L`
` <= (1/2) [ log(1+1/(3R)) + log(1+2/(9R+3)) ]`.          (R21P.6)

Using `log(1+t)<=t`,

`log lambda / L`
` <= 1/(6R) + 1/(9R+3)`.                                  (R21P.7)

Asymptotically the coefficient improves from the old crude `1/(3R)` to

`5/(18R)`,

a `16.7%` reduction.

## 3. Improved continued-fraction gate

Let

`g=gcd(A,L)`, `p=A/g`, `q=L/g`,

and

`beta=log 3/log 2`.

Since

`log lambda = g(p log2-q log3)`

and `L=gq`, (R21P.6) gives

`0 < p/q-beta`
` <= [1/(6R)+1/(9R+3)]/log2`.                               (R21P.8)

Thus Legendre's criterion applies whenever

`2 q^2 [1/(6R)+1/(9R+3)] < log 2`.                          (R21P.9)

Under this inequality the reduced slope `p/q` must again be an above-`beta` continued-fraction convergent.

This strictly enlarges the RL20 Legendre window.

## 4. Exact external-floor consequence

Use the inherited external floor

`R>=R0=2^71`.

The exact verifier `verify_rl21_half_high_cf_gate.py` uses rigorous rational intervals for `log2` and `log3` and proves that

`q <= 54,276,749,274`                                      (R21P.10)

lies inside the strengthened Legendre window.

It then reconstructs the same above-`beta` convergents occurring below that range and checks that each violates the sharper product bound exactly.

Therefore, conditional on `R>=2^71`,

> **`L/gcd(A,L) >= 54,276,749,275`.**                       (R21P.11)

This improves the RL20 floor

`49,547,666,544`

by about `9.5%`.

The first continued-fraction denominator beyond the new Legendre window is still

`65,470,613,321`,

so no additional convergent is crossed; the gain comes from enlarging the interval on which every admissible reduced slope is forced onto the already-excluded convergent spine.

## 5. Strategic consequence

This does not close RL, but it demonstrates that **integer transition ownership can strengthen the global packing theorem without any radius assumption**.

The natural next extension is to classify more short parity patterns that would force descent below `R` for states in successively larger low intervals.  Such pattern exclusions turn into density restrictions on low odd states and can in principle sharpen the product/CF gate beyond the one-step half-high argument above.

Evidence discipline:

- R21P.1--R21P.9: **ANALYTIC**;
- R21P.11: **EXACT FINITE CERTIFICATE + inherited EXTERNAL COMPUTATIONAL INPUT `R>=2^71`**.

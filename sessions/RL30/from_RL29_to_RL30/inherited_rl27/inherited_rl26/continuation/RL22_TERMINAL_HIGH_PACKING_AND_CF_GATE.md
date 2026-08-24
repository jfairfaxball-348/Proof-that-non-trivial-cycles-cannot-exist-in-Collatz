# RL22 — terminal-high refinement of odd-state packing

Date: 2026-08-21

## Status

Sections 1--4 are **ANALYTIC**. Section 5 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This supersedes the weaker RL22 low-chain coefficient `29/108` in the external-floor branch.  The key extra observation is that the second high odd state terminating a maximal low chain is dynamically owned; it cannot be replaced by an arbitrary state merely bounded below by the threshold `H=(4R-1)/3`.

## 1. Low chains and the exact terminal state

Let `R` be the least state of a nontrivial positive cycle and

`H=(4R-1)/3`.

As in RL21/RL22, every low odd state `x<H` has odd successor

`y=(3x+1)/2`,

and if the next odd state is again low then necessarily

`x_next=f(x):=(9x+5)/8`.                                   (R22T.1)

Thus maximal short-linked low chains have lengths `k=1,2,3`.

Let `x_0,...,x_(k-1)` be such a maximal chain, with

`x_i=f^i(x_0)` for `i<k`.

After the last low `x_(k-1)`, write

`y=(3x_(k-1)+1)/2`.

Because `x_(k-1)<H`, we have `y<2R`.  Let

`nu=v2(3y+1)`

and let `z=(3y+1)/2^nu` be the following odd state.

The case `nu>=3` would give

`z<(6R+1)/8<R`,

impossible.  Hence only two terminal types exist:

- **type I:** `nu=1`, so

  `z=(9x_(k-1)+5)/4 = 2 f^k(x_0)`;                       (R22T.2)

- **type II:** `nu=2`, so

  `z=f^k(x_0)`, and maximality of the low chain forces

  `z>=H`.                                                   (R22T.3)

This exact terminal alternative is the extra information omitted by the earlier coarse chain bound.

## 2. Exact block products

For an odd state `s`, put

`F(s)=1+1/(3s)`.

For every low/high-successor pair,

`F(x)F((3x+1)/2)=(9x+5)/(9x)=(8/9)f(x)/x`.                (R22T.4)

Therefore the product over the `k` low/high-successor pairs telescopes:

`prod_(i=0)^(k-1) F(x_i)F(y_i)`
` = (8/9)^k f^k(x_0)/x_0`.                                (R22T.5)

Attach the owned terminal high state `z`.  Each maximal-chain block therefore contains `2k+1` odd states.

### Type I

Both factors in (R22T.5) and `F(2f^k(x_0))` decrease with `x_0`, so the maximum occurs at `x_0=R`.  Exact simplification gives

`P_I,1 = (27R+19)/(27R)`,

`P_I,2 = (243R+287)/(243R)`,

`P_I,3 = (2187R+3511)/(2187R)`.                            (R22T.6)

### Type II

Now `f^k(x_0)>=H`.  The product again decreases with `x_0`, so the worst case is the smallest allowed starting point.

For `R>=160`, the thresholds are:

- `k=1`: `x_0=f^(-1)(H)=(32R-23)/27 >R`;
- `k=2`: `x_0=f^(-2)(H)=(256R-319)/243 >R`;
- `k=3`: `f^(-3)(H)<R`, so `x_0=R`.

This yields

`P_II,1 = 32R/(32R-23)`,

`P_II,2 = 256R/(256R-319)`,

`P_II,3 = (2187R+3767)/(2187R)`.                           (R22T.7)

## 3. Every maximal-chain block is no worse than one threshold-high state per phase

Let

`F_H=F(H)=4R/(4R-1)=1+1/(4R-1)`.                          (R22T.8)

For every `R>=160`, exact rational comparison gives

`P_I,k <= F_H^(2k+1)`,

`P_II,k <= F_H^(2k+1)`,

for `k=1,2,3`.                                             (R22T.9)

The bundled verifier proves all six inequalities by expanding the positive-denominator differences and checking that their numerator polynomials have strictly positive coefficients after the shift `R=t+160`.

Now partition the odd cycle into the disjoint maximal-chain blocks above.  Any odd states not used by these blocks lie in additional high portions of the gaps between low chains, so each such leftover state is at least `H` and individually has factor at most `F_H`.

Therefore, for every positive cycle with `R>=160`, multiplying all block and leftover estimates gives

> **`lambda <= F_H^L`.**                                   (R22T.10)

Using the exact RL19 odd-step product identity, this is equivalently

> **`log(lambda)/L <= log(1+1/(4R-1))`.**                  (R22T.11)

Finally,

> **`log(lambda)/L <= 1/(4R-1)`.**                         (R22T.12)

The asymptotic coefficient is now exactly `1/4`, improving both

- RL21: `5/18`, and
- the first RL22 chain bound: `29/108`.

No radius assumption is used.

## 4. Continued-fraction gate

With

`g=gcd(A,L)`, `p=A/g`, `q=L/g`, `beta=log(3)/log(2)`,

we have

`0 < p/q-beta <= [1/(4R-1)]/log(2)`.                       (R22T.13)

Legendre applies whenever

`2q^2/(4R-1) < log(2)`.                                    (R22T.14)

## 5. Exact consequence under the inherited external floor

Under the inherited external computational input

`R>=R0=2^71`,

the exact verifier `verify_rl22_terminal_high_cf_gate.py` proves that

`q <= 57,212,717,232`

lies inside the new Legendre window.  It reconstructs the above-`beta` convergents in this range and verifies that every one violates the sharper bound (R22T.13).

Therefore, conditional on `R>=2^71`,

> **`L/gcd(A,L) >= 57,212,717,233`.**                      (R22T.15)

The next continued-fraction denominator is still

`65,470,613,321`,

so the stronger packing theorem does not yet cross that qualitative threshold.

## 6. Evidence discipline

- R22T.1--R22T.14: **ANALYTIC** for `R>=160` where stated.
- R22T.15: **EXACT FINITE CERTIFICATE + inherited EXTERNAL COMPUTATIONAL INPUT `R>=2^71`**.

The earlier `29/108` theorem remains correct, but (R22T.12) is stronger throughout the inherited external-floor branch.

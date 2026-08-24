# RL22 — low-chain packing and a further continued-fraction gate

Date: 2026-08-21

## Status

Sections 1--4 are **ANALYTIC**. Section 5 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This sharpens RL21's half-high odd-state packing theorem by exploiting the dynamics of a low odd state that returns to the low interval after exactly one intervening high odd state.

## 1. Odd-to-odd low returns

Use the shortcut map

`T(n)=n/2` for even `n`,

`T(n)=(3n+1)/2` for odd `n`.

Let `R` be the least state of a nontrivial positive cycle, and write

`H=(4R-1)/3`.

RL21 proved that if an odd state `x<H`, then

`y=T(x)=(3x+1)/2`

is odd and satisfies

`y >= (3R+1)/2 > H`.                                      (R22P.1)

Now ask when the next odd cycle state after `y` can again lie below `H`.
Let

`nu=v2(3y+1)`

so that the next odd state is

`z=(3y+1)/2^nu`.

If `nu=1`, then

`z=(3y+1)/2 >= (9R+5)/4 > H`,

so the next odd state is not low.

If `nu>=3`, then `y<2R` from `x<H`, hence

`z <= (3y+1)/8 < (6R+1)/8 < R`,

contradicting leastness.

Therefore a low-to-low return across exactly one intervening high odd state is possible only for

`nu=2`,

and then exactly

`z=(3y+1)/4=(9x+5)/8`.                                    (R22P.2)

Thus every such short low return grows the low state by more than the factor `9/8`.

## 2. Low chains have length at most three

Call two consecutive low odd states in the induced odd-state cycle **short-linked** if exactly one high odd state lies between them.
By (R22P.2), along a short-linked low chain

`x_(i+1)=(9x_i+5)/8 > (9/8)x_i`.                           (R22P.3)

Since `x_0>=R`, after three short links,

`x_3 > (9/8)^3 R = (729/512)R > (4/3)R > H`.

Hence no four low states can be connected by three successive short links.

> **Every maximal short-linked low chain contains exactly `k=1,2`, or `3` low states.** (R22P.4)

At the end of each maximal chain, the gap to the next low state contains at least two high odd states. Therefore one may attach to each chain:

- its `k` low states;
- the immediate high successor of each low state;
- one additional high state from the terminal long gap.

These chain blocks are disjoint. Any remaining unassigned odd states are high.

## 3. Exact chain-product telescoping

For any odd state `s`, let

`F(s)=1+1/(3s)`.

If `x` is low and `y=(3x+1)/2`, then algebraically

`F(x)F(y)=(9x+5)/(9x)`.                                    (R22P.5)

Define the affine map

`f(x)=(9x+5)/8`.

When the next low state is short-linked, it is exactly `f(x)`; even for the terminal low of a chain, (R22P.5) remains the same algebraic pair factor.
Thus for a chain beginning at `x_0`, the product of the `k` low/high-successor pairs is

`prod_(i=0)^(k-1) F(x_i)F(y_i)`
` = (8/9)^k f^k(x_0)/x_0`.                                 (R22P.6)

The ratio `f^k(x)/x` decreases with `x`, so the worst case is `x_0=R`.
The attached extra high state is at least `H`, with

`F(H)=4R/(4R-1)`.                                          (R22P.7)

Therefore every chain block of length `2k+1`, for `k=1,2,3`, has product at most

`P_1 = 4(9R+5) / [9(4R-1)]`,

`P_2 = 4(81R+85) / [81(4R-1)]`,

`P_3 = 4(729R+1085) / [729(4R-1)]`.                        (R22P.8)

The first expression simplifies to

`P_1 = 1 + 29/(36R-9)`.                                    (R22P.9)

For every `R>=5`, direct rational comparison gives

`P_2^(1/5) <= P_1^(1/3)`,

`P_3^(1/7) <= P_1^(1/3)`,

and

`F(H) <= P_1^(1/3)`.                                       (R22P.10)

The verifier checks these comparisons by reducing them to integer polynomials whose coefficients are nonnegative after the shift `R=t+5`.

Consequently every chain block, and every leftover high state, has geometric-mean factor at most `P_1^(1/3)`.

## 4. Global product bound

Using the exact RL19 identity

`lambda = prod_(odd cycle states x) F(x)`,

and multiplying the disjoint chain-block estimates,

> **`log(lambda)/L <= (1/3) log(1+29/(36R-9))`.**           (R22P.11)

Using `log(1+t)<=t`,

> **`log(lambda)/L <= 29/(108R-27)`.**                     (R22P.12)

The asymptotic coefficient is therefore

`29/108 = 0.268518...`,

improving RL21's coefficient

`5/18 = 0.277777...`.

This is a radius-independent analytic strengthening.

## 5. Continued-fraction consequence under the inherited floor

Let

`g=gcd(A,L)`, `p=A/g`, `q=L/g`, `beta=log(3)/log(2)`.

As before,

`0 < p/q-beta <= [29/(108R-27)]/log(2)`.                   (R22P.13)

Legendre's criterion therefore applies whenever

`2 q^2 * 29/(108R-27) < log(2)`.                           (R22P.14)

Under the inherited external computational floor

`R>=R0=2^71`,

the exact verifier proves that every

`q <= 55,204,624,167`

lies inside this Legendre window, reconstructs all above-`beta` convergents below that range, and excludes each one with the sharper product bound.

Therefore, conditional on `R>=2^71`,

> **`L/gcd(A,L) >= 55,204,624,168`.**                      (R22P.15)

The first continued-fraction denominator beyond the new window remains

`65,470,613,321`,

so this does not yet cross a new convergent threshold.

## 6. Evidence discipline

- R22P.1--R22P.14: **ANALYTIC**.
- R22P.15: **EXACT FINITE CERTIFICATE + inherited EXTERNAL COMPUTATIONAL INPUT `R>=2^71`**.

Verifier: `verify_rl22_low_chain_cf_gate.py`.

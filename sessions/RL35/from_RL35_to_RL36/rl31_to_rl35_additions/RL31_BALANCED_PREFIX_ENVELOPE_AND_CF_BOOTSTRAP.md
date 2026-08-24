# RL31 — balanced-prefix envelope and continued-fraction bootstrap

Date: 2026-08-21

## Status

Sections 1–6 are **ANALYTIC** inside the exact exceptional three-way-balanced branch, with the same inherited external input `R>=2^71` used by RL24/RL30. The finite `N=300` envelope and continued-fraction arithmetic are checked by `verify_rl31_balanced_prefix_envelope.py` as an **exact finite certificate**.

This is a local improvement in the exceptional order-3 branch. It does **not** close RL and does not repair the other open branches in the RL30 dependency DAG.

## 1. Setup

Retain the audited RL30 exceptional branch

`R==667 mod4608`, `R>=5275`, `(G,H)=(12,4)`,

with three balanced blocks of common full-parity length `b` and common odd count `e`. Put

`B=2^b`, `Y=3^e`, `z=B/Y`, `1<z<46/45`.

The full cycle has

`A=3b`, `L=3e`.

For one balanced block let `X_j` be its phase state, let `p(j)` count odd bits before phase `j`, and define

`q_j=2^j/3^{p(j)}`.

If `P_j` is the odd-correction product accumulated before phase `j`, then the standard prefix identity is

> `q_j X_j = X_0 P_j`.                                      (RL31.1)

Since every cycle state is at least `R`, `X_0>=R`, and `P_j>=1`,

> `q_j X_j >= R`.                                          (RL31.2)

## 2. Uniform cap on every balanced prefix scale

The prefix correction product is increasing and is bounded by the complete block product. For a balanced block from `X_0` to `X_b`,

`P_b=z X_b/X_0`.

Therefore

`q_j X_j=X_0P_j <= X_0P_b=zX_b <= z(R+12)`.

Using `X_j>=R`, every phase in every one of the three balanced blocks satisfies

> `q_j < Q(R):=(46/45)(R+12)/R`.                           (RL31.3)

Under the inherited external floor `R>=R0=2^71`, put

> `Q0=(46/45)(R0+12)/R0`.

Then `q_j<Q0` uniformly.

This cap is stronger than the raw fact `q_j=2^j/3^{p(j)}`: it forces a lower envelope on every prefix odd count.

## 3. Odd-weighted scale sum reduces to the unweighted scale sum

The scale recurrence is

- even phase: `q_{j+1}=2q_j`;
- odd phase: `q_{j+1}=2q_j/3`.

Hence, with `epsilon_j` the parity bit,

`epsilon_j q_j=(3/4)(2q_j-q_{j+1})`.

Summing a complete balanced block gives

> `sum_(j odd) q_j = (3/4)(sum_(j=0)^(b-1)q_j + 1-z)`.     (RL31.4)

Because `z>1`,

> `sum_(j odd)q_j < (3/4) sum_j q_j`.                      (RL31.5)

For an odd phase,

`log(1+1/(3X_j)) <= 1/(3X_j) <= q_j/(3R)`

by (RL31.2). Thus the complete block correction product `P` satisfies

> `log P < (1/(4R)) sum_j q_j`.                            (RL31.6)

So it is enough to control the ordinary prefix-scale sum.

## 4. Greedy cap envelope

Normalize `x_j=q_j/Q` for any cap `Q`. Then `0<x_j<=1` and

`x_{j+1}=2x_j/3^{epsilon_j}`.

For a fixed starting `x_0`, admissibility of the cap implies

`p(j) >= ceil(log_3(x_0 2^j))`.

The minimal admissible prefix count is realizable because `log_3 2<1`, so the ceiling rises by only `0` or `1` each step. Equivalently, the pointwise largest admissible scale path is the greedy map

> `T(x)=2x` for `x<=1/2`, and `T(x)=2x/3` for `x>1/2`.      (RL31.7)

Every other cap-admissible parity path from the same `x_0` has `x_j` no larger at every phase.

For `N=300`, the interval `(0,1]` can be split exactly at the preimages of `1/2`. On each resulting interval every `T^j(x_0)` is a rational multiple of `x_0`, so the `N`-step sum is linear in `x_0`. Exact interval recursion gives

> `sum_(j=0)^299 x_j <= 300 M_300`,                        (RL31.8)

where

`M_300 =`

`289661025475730124348366187773731846212314723592236134059063480299134845890983137619226395753`

`/ 473884046723725653464253538204405286537042604564020039780668940186229359983539922912333900800`

and

> `M_300 ~= 0.6112487379103574`.                           (RL31.9)

The verifier reconstructs all `28,637` terminal envelope intervals and checks this exact maximum.

Partitioning an arbitrary balanced block into full 300-step chunks plus one remainder gives

> `sum_j q_j <= b Q0 M_300 + 300 Q0`.                      (RL31.10)

## 5. New finite product coefficient

Multiplying (RL31.6) over the three balanced blocks and using `L=3e`,

`R log(lambda)/L`
` <= (b/e) Q0 M_300/4 + 300 Q0/(4e)`.                     (RL31.11)

The inherited RL24H continued-fraction result gives

`L/gcd(A,L) >= 57,397,300,723`.

Since `L=3e`, this implies

> `e>=19,132,433,575`.                                     (RL31.12)

Also `b/e<317/200` in this range. An exact elementary check is enough: if `b/e>=317/200`, then

`z^200 >= (2^317/3^200)^e`,

and the right side already exceeds `(46/45)^200` at `e=846`, contradicting `z<46/45`.

Substituting (RL31.12) into (RL31.11) yields the first certified coefficient

> `R log(lambda)/L < 0.2475897011240691`.                  (RL31.13)

This improves the inherited RL24H rational asymptotic coefficient

`457841/1843200 ~= 0.2483946397569444`

by about

> `0.00080493863` in normalized `R log(lambda)/L` units.

This improvement does not use RL29's `Omega(e/log e)` high-column theorem; it comes directly from the balanced-prefix scale cap.

## 6. Continued-fraction bootstrap

Under `R>=R0=2^71`, (RL31.13) can be inserted into the same rigorous Legendre/convergent check used by RL24H.

First pass:

> `L/gcd(A,L) >= 57,490,527,166`.

This raises the inherited `e` floor. Reinsert the larger `e` into the finite 300-step remainder term in (RL31.11). One more pass gives

> **`L/gcd(A,L) >= 57,490,527,167`.**                       (RL31.14)

Now `ceil(57,490,527,167/3)=19,163,509,056`, the same `e` floor as the preceding pass, so the bootstrap is fixed.

The resulting coefficient is

> **`R log(lambda)/L < 0.2475897011175711`.**               (RL31.15)

The next relevant continued-fraction denominator remains

`65,470,613,321`,

so this is a genuine quantitative advance but not a qualitative CF-gate crossing.

## 7. Asymptotic envelope

The greedy map has a useful analytic limit. Writing `y=log(Q/q)`, after the finite transient its dynamics is the irrational rotation by `log(3/2)` modulo `log 3`. Hence the normalized greedy scales are equidistributed in logarithmic coordinate. Their mean is

`integral_0^1 3^(t-1) dt = 2/(3 log 3)`.

Consequently the ideal long-block limit of the same argument is

> `limsup R log(lambda)/L <= Q0/(6 log 2)`
> `~= 0.2457924884477493`.                                 (RL31.16)

RL31.15 is deliberately weaker because it is a completely explicit finite certificate with no discrepancy-rate input.

## 8. What happened to the weighted-synchronization attack?

The audit kickoff suggested charging long synchronized runs to high odd corrections or 2-adic valuation. Two clarifications emerged.

First, the RL24H supporting line can be rewritten exactly as a phase pressure. If

`J=T^3/C^5`, `tau=(1/4)log J`,

then

`lambda^12 <= C^(4L)J^(3A-4L)`

is equivalent to

> `log(lambda)-A tau <= (L/3)log(C/J)`.                    (RL31.17)

Thus every full-parity even phase contributes the fixed negative pressure `-tau`, while an odd phase contributes `log F(x)-tau`. This makes the odd-or-valuation intuition precise, but it also shows that raw valuation excess has the wrong sign if inserted naively into the old supporting line.

Second, a short unsynchronized excursion can manufacture a deep later synchronization. For example, if a synchronized pair/triple has one-vs-two parity pattern `(0,1,1)` followed by the complementary `(1,0,0)`, a pair gap `D` transforms as

> `D -> (3D-1)/4`.                                         (RL31.18)

The opposite orientation gives `(3D+1)/4`. Choosing `D` in a suitable 2-adic class can therefore make the new gap divisible by an arbitrarily high power of two after only this short excursion. So no theorem of the form

`next synchronization length <= C * preceding unsynchronized length`

can follow from the local gap recurrence alone.

This is why the prefix-envelope route is useful: it extracts a fixed gain without needing such a synchronization-production lemma.

## 9. Proof-state consequence

RL31 advances only the exact exceptional three-way-balanced branch:

- the audited RL29 ownership and transport theorems remain valid;
- the branch now has a stronger finite product coefficient and CF denominator floor;
- the global RL30 DAG remains open in the non-near-resonant/huge-length, strict-excursion, order-2/general cyclotomic, and non-extremal order-3 branches.

The next useful question is whether the **balanced-prefix cap envelope generalizes beyond the exact `(12,4)` branch**. If a comparable uniform cap can be obtained for order-2 or general balanced returns, this method may have wider bridge value than the synchronization-specific attack.

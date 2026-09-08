# RL279 — scalable zero-rank/run compression, boundary quotient, and seven-zero Gate-A contraction

Date: 2026-09-08

## Classification

Primary:

`SCALABLE_ZERO_RANK_RUN_COMPRESSION_PROVED`

Promoted subordinate results:

- `HEIGHT_BUDGET_ZERO_RANK_IDENTITY_PROVED`
- `UNIFORM_ZERO_MASS_CORRIDOR_PROVED`
- `BOUNDARY_CYCLE_SCALE_SIGN_THEOREM_PROVED`
- `ZERO_BUDGET_ONLY_HEIGHT_GROWTH_BARRIER_PROVED`
- `EXACT_SEVEN_ZERO_GATE_A_CONTRACTION_PROVED`

Gate A remains open uniformly. Gate B is unchanged/open and frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming exact state

RL279 starts from RL278:

- the global zero-rank threshold
  `S_m0=sum 2^(t-1)(2/3)^(u_t)>17/2`;
- exact Gate-A safety for `m0=4,5,6`;
- `H_can<k => m0>=7 => z>=k+5`;
- the fixed-zero finite-reduction engine;
- the canonical recurrence beginning at `(d,J,H)=(1,-13,0)`;
- terminal `d=1,J=2^k`, `k>=3`;
- full-phase box `3^ell<2^a<(160/81)3^ell`;
- `m=a-k-1`, `r=ell-3`, `m0=m-r=z-k+2`.

Write

`K=J+2^d-1`.

## 2. Exact normalized recurrence

From the promoted recurrence, every legal column has height increment

`H' = H+d-1`.

The `(d,K)` transition is exactly:

- `K` even, `x=1`:
  `(d,K) -> (d,3K/2)`;
- `K` even, `x=0`:
  `(d,K) -> (d,(K+3^d-1)/2)`;
- `K` odd, `x=1`, necessarily `d>1`:
  `(d,K) -> (d-1,(K-1)/2)`;
- `K` odd, `x=0`:
  `(d,K) -> (d+1,3(K+3^d)/2)`.

Classification: **exact analytic recurrence normalization**.

### All-one macro

For `K != 0`, let `s=nu_2(K)`.

An all-`1` run consumes the `s` powers of two at fixed `d`:

`K -> 3^s K/2^s`.

If `d>1`, the next all-`1` column descends:

`(d,K) -> (d-1,(3^s(K/2^s)-1)/2)`.

The macro has exact length `s+1` and exact height charge

`Delta H=(s+1)(d-1)`.

At `d=1`, the descending all-`1` step is illegal, so the boundary all-one run has length exactly `nu_2(K)` and zero height. The special state `K=0` is treated separately.

Classification: **exact run-compression theorem**.

## 3. Multiplicative Gate-A potential

For a prefix of length `n`, weight `r_n`, and height `H_n`, define

`P_n = 2^(H_n+n)/3^(r_n)`.

A legal column satisfies exactly

`P_(n+1)/P_n = 2^d/3^x`.

Thus:

- a zero multiplies `P` by `2^d`;
- a one at `d>=2` multiplies it by at least `4/3`;
- the only column which decreases `P` is a one at `d=1`, with factor `2/3`.

At a terminal, put

`X=2^a/3^r`.

Since `n=m=a-k-1`,

`P/X = 2^(H_can-k-1)`.

Using the full-phase box `27<X<160/3` gives the strict separation:

- if `H_can<k`, then `P<40/3`;
- if `H_can>=k`, then `P>27/2`.

Because `40/3<27/2`, retained phase-box terminals satisfy

`H_can>=k  <=>  P>=40/3`.

Classification: **exact analytic Gate-A potential reformulation**.

## 4. Exact height budget in zero coordinates

Let the zero ranks of the canonical words be

`u_t = # x-ones before the t-th x-zero`,
`v_t = # y-ones before the t-th y-zero`.

Canonical order gives `u_t<=v_t`. Put

`h_t=v_t-u_t>=0`.

Because `x` and `y` have equal length and equal weight, complementary ordered positions give

`H_can = sum_t (v_t-u_t) = sum_t h_t`.

This is an exact identity.

Now let

`rho=2/3`,
`c_t=2^(t-1) rho^(u_t)`,
`S=sum_t c_t`.

The inherited zero-rank identity becomes

`2S + D(u,h) = 12 + X(1/2+2^(-k-1))`

where

`D(u,h)=sum_t c_t(1-rho^(h_t))`.

Also

`D(u,h)=(1/3) sum_t sum_(q=0)^(h_t-1) c_t rho^q`.

Therefore a height unit is an exact diminishing coupon, and for fixed zero ranks and total height `H`, the maximum possible defect is the sum of the `H` largest coupons from

`{ c_t rho^q / 3 : t>=1, q>=0 }`.

In particular,

`D <= (1-rho^H)S`

and every terminal of height `H` satisfies

`S > 51 / (2(3-(2/3)^H))`.

The older `S>17/2` is the `H->infinity` limit of this sharper finite-height envelope.

Classification: **exact analytic height-budget theorem**.

## 5. Uniform zero-mass corridor

The same exact identity also supplies a uniform upper bound.

Since `S_v=sum 2^(t-1)rho^(v_t)<=S`,

`3S-S_v >= 2S`.

The phase box and `k>=3` give

`12 + X(1/2+2^(-k-1)) < 42`.

Hence

`boxed: 17/2 < S < 21`.

This is independent of `m0`.

Let

`lambda=log_(3/2)(2)`

and

`sigma_t=u_t-lambda(t-1)`.

Then

`c_t=(2/3)^(sigma_t)`

and every retained terminal satisfies

`17/2 < sum_t (2/3)^(sigma_t) < 21`.

Thus the zero ranks have a bounded exponential moment about the critical slope `lambda`.

For every `j`,

`(2^j-1)(2/3)^(u_j) < 21`.

Examples:

- `u5>=1`;
- `u6>=3`;
- `u7>=5`;
- `u8>=7`;
- `u10>=10`;
- `u20>=27`.

Also the number of ranks with `sigma_t<=-h` is strictly less than

`21(2/3)^h`.

Classification: **uniform scalable analytic theorem**.

## 6. Exact zero-to-zero scalar multiplier and terminal reduction

Let

`g_t=u_t-u_(t-1)`.

Then

`c_t/c_(t-1) = 2(2/3)^(g_t)`.

Thus each zero-to-zero run is represented by one scalar multiplier. In particular:

- `g=0`: factor `2`;
- `g=1`: factor `4/3`;
- `g=2`: factor `8/9`;
- `g=3`: factor `16/27`.

Let

`tau=r-u_(m0)`

be the all-one tail length after the final zero. Then the full-phase terminal scale depends on the prior zero history only through the final weight:

`X = 2^(k+2) c_(m0) (2/3)^tau`.

Likewise

`P_terminal = 2^(H_can+1) c_(m0) (2/3)^tau`.

This is the promoted finite-dimensional zero-history compression.

## 7. Exact boundary accelerated-Collatz conjugacy

At `d=1`, write an even boundary `K` as

`K=2(n+1)`,

equivalently `n=(J-1)/2`.

The unique choice which keeps the next state on the even-`K`, `d=1` zero-height boundary gives

- `n` even:
  `n -> n/2`, with `x=0`;
- `n` odd:
  `n -> (3n+1)/2`, with `x=1`.

Thus the retained boundary subsystem is exactly the accelerated `3n+1` map.

The initial state has `n=-7`, and

`-7 -> -10 -> -5 -> -7`

is the exact neutral word `101`.

The positive trivial cycle

`1 -> 2 -> 1`

is the exact neutral word `10`.

Classification: **exact analytic conjugacy**.

## 8. Boundary monotonicity and cycle scale sign

On the zero-height boundary, retain the prefix potential `P` and define

`A=Pn`,
`B=P(n+1)`.

For an even step,

`n'=n/2`, `P'=2P`,

so

`A'=A`,
`B'=B+P`.

For an odd step,

`n'=(3n+1)/2`, `P'=(2/3)P`,

so

`A'=A+P/3`,
`B'=B`.

Hence `A` and `B` are both nondecreasing; exactly one increases at each nontrivial step.

If a boundary orbit returns to the same `n` after length `L` with `r` one-bits, its scale multiplier is

`mu=2^L/3^r`.

For any nonzero positive boundary cycle, at least one odd step occurs, so `A` increases and

`mu>1`.

For any negative boundary cycle with `n<-1`, at least one even step occurs, so `B` increases; since `B<0`, this forces

`mu<1`.

The special fixed states satisfy:

- `n=0`: `mu=2>1`;
- `n=-1`: `mu=2/3<1`.

Therefore every positive neutral boundary cycle is scale-expanding and every negative neutral boundary cycle is scale-contracting. No classification of possible Collatz cycles is needed.

Also, `J>0` is forward invariant under every legal canonical transition.

Classification: **exact analytic boundary quotient theorem**.

## 9. Infinite Gate-safe neutral family: barrier to zero-budget-only height growth

The exact canonical word

`00101001111`

terminates at

`d=1,J=8=2^3,H_can=3`

with

`m0=5`

and phase scale

`X0=2^15/3^6`.

The initial neutral loop `101` returns `(d,J,H)=(1,-13,0)` to itself and has scale factor `8/9`.

After the prefix `001010011`, the state is `(d,J,H)=(1,3,3)`; the positive neutral loop `10` returns this state to itself and has scale factor `4/3`.

Therefore for all integers `p,q>=0`,

`x_(p,q)=(101)^p 001010011 (10)^q 11`

is an exact canonical terminal with

`k=H_can=3`,
`m0=5+p+q`,

and

`X_(p,q)=X0(8/9)^p(4/3)^q`.

Since `log(9/8)/log(4/3)` is irrational, integer approximation gives infinitely many positive `(p,q)` with the multiplier arbitrarily close to `1`. Because `X0` lies strictly inside the full-phase box, infinitely many family members are retained full-phase terminals.

Exact verifier examples include:

- `(p,q)=(127,52)`, `m0=184`, `X≈44.9952`;
- `(p,q)=(276,113)`, `m0=394`, `X≈44.9473`.

Hence there is no valid theorem of the form

`H_can >= f(m0)` with `f(m0)->infinity`

on the retained phase-box canonical terminal class.

This is a barrier to zero-budget-only height growth, not a Gate-A counterexample: every member has exact equality `H_can=k`.

Classification: **exact analytic recurrent-family barrier**.

## 10. Supporting exact seven-zero contraction

This section uses the inherited fixed-zero finite-reduction engine only as supporting contraction, not as the main scalable programme.

Define

`S6=sum_(t=1)^6 2^(t-1)(2/3)^(u_t)`.

Exact monotone upper-envelope branch-and-bound gives

`M6=max{S6:S6<17/2}`
`=583353885633550/68630377364883`

with witness

`(1,1,1,2,10,29)`.

Thus

`gamma6=17/2-M6`
`=8643935911/137260754729766`.

If the first six zeros are below threshold but seven zeros cross it, the seventh term must bridge the gap. Exact comparison gives

`64(2/3)^34 > gamma6`,
`64(2/3)^35 < gamma6`,

hence

`u7<=34`.

If the first six have already crossed threshold, the promoted six-zero exact family has 458 legal prefixes and actual maximum `u6=14`; exact all-one replay gives at most 11 further columns before terminal/stop, hence `u7<=25`.

Therefore globally

`u7<=34`.

Exact enumeration of

`0<=u1<=...<=u7<=34`,
`S7>17/2`

gives:

- `140185` relaxed tuples;
- `2662` legal canonical prefixes;
- actual maximum legal `u7=19`;
- `691` terminal closures;
- `286` full-phase scale-box terminals;
- `0` Gate-A violators.

Thus seven internal zeros are Gate-A safe, and the promoted dangerous-region contraction is

`boxed: H_can<k => m0>=8 => z>=k+6`.

Classification: **exact finite canonical certificate built on a non-arbitrary finite reduction**.

## 11. What remains open

Gate A remains the exact target

`H_can>=k`

at terminal `d=1,J=2^k`.

RL279 has removed several false scalable targets:

- zero budget alone cannot force unbounded height;
- neutral boundary dynamics cannot be treated as uniformly height-positive;
- the embedded accelerated-Collatz subsystem should not be attacked by classifying all its cycles.

The compressed remaining target is a positive excursion theorem.

A trajectory can be viewed as:

`negative neutral boundary dynamics`
`-> height-positive excursions`
`-> positive neutral boundary dynamics`
`-> terminal`.

Negative neutral cycles are scalar contractions; positive neutral cycles are scalar expansions; all positive height is paid in the off-boundary macros.

The successor should prove a sharp scale/state-versus-height inequality for a positive excursion

`d=1 -> d>1 -> d=1`

and combine it with the terminal scale formulas and height-coupon budget. This is the principal route. Further fixed-zero enumeration is secondary only.

## 12. Verification

Portable verifier:

`verification/verify_rl279_structural.py`

independently checks:

- the normalized `(d,K)` transition law on 1,851 legal sample transitions;
- the exact multiplicative potential law on 74,040 legal sample states;
- the zero-lag height identity on 590 reachable equal-weight prefixes;
- the exact six-zero sub-threshold maximum `M6` and witness;
- the exact gap `gamma6`;
- `u7<=34`;
- all seven-zero counts and zero Gate-A violators;
- the exact neutral-loop family and phase-box examples;
- boundary endpoint monotonicity on 401 integer states;
- positive-`J` forward invariance on 1,150 legal sample transitions.

The exact finite seven-zero certificate is exhaustive over its rigorously derived range. The analytic results above are proved algebraically from the promoted recurrence and inherited full-phase identities.

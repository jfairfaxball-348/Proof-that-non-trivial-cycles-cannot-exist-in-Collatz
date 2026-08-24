# RL20 — coprime-6 state packing and a continued-fraction gate

Date: 2026-08-20

## Status

The structural statements below are **ANALYTIC**.  The numerical lower bound in Section 5 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R# >= 2^71`.

This does **not** prove RL or Collatz.

## 1. Every phase state of a nontrivial positive cycle is nonzero modulo 3

Use the full-parity shortcut map

- `T(x)=x/2` for even `x`;
- `T(x)=(3x+1)/2` for odd `x`.

Immediately after any odd step,

`T(x) = (3x+1)/2 != 0 (mod 3)`.

Every following even division preserves nonzero residue modulo 3.  A nontrivial positive cycle contains an odd step and every phase lies after some odd step around the cycle.  Hence

`3 \nmid x_i`

for every phase state `x_i`.

In particular every odd phase state is congruent to `1` or `5 (mod 6)`.

## 2. Sharpened odd-state packing in the k=0 RL least-root branch

The inherited k=0 least-root branch has `R# = 1 (mod 3)`.  Since the least state is odd, in fact

`R# = 1 (mod 6)`.

Let the `L` distinct odd phase states be sorted as

`R# = y_0 < y_1 < ... < y_(L-1)`.

The admissible odd integers not divisible by 3, starting from a number `1 mod 6`, have offsets

`0,4,6,10,12,16,18,...`.

Therefore exactly

`y_j >= R# + 3j + (j mod 2) >= R# + 3j`.                 (R20.1)

This improves the RL19 parity-only estimate `y_j >= R# + 2j`.

## 3. Strengthened logarithmic packing

RL19 proved the exact odd-step product identity

`lambda = 2^A/3^L = prod_(odd phases) (1+1/(3x_i))`.

Put

`Lambda = log lambda = A log 2 - L log 3 > 0`.

Using (R20.1) and `log(1+t)<=t`,

`Lambda <= sum_(j=0)^(L-1) log(1+1/(3(R#+3j+(j mod2))))`

and hence

`Lambda <= (1/3) sum_(j=0)^(L-1) 1/(R#+3j)`.             (R20.2)

The elementary integral bound gives

`Lambda <= 1/(3R#) + (1/9) log(1+3(L-1)/R#)`.            (R20.3)

This is strictly stronger in the k=0 branch than the RL19 bound

`1/(3R#) + (1/6) log(1+2(L-1)/R#)`.

For the arithmetic argument below we also retain the cruder but uniform consequence

`Lambda <= L/(3R#)`.                                      (R20.4)

## 4. Continued-fraction gate at arbitrary least state

Let

`g = gcd(A,L)`, `p=A/g`, `q=L/g`,

so `p/q=A/L` is reduced, and put

`beta = log 3 / log 2`.

Because `Lambda>0`,

`p/q - beta = Lambda/(L log2)`.

By (R20.4),

`0 < p/q-beta <= 1/(3R# log2)`.                            (R20.5)

Therefore, whenever

`2 q^2 < 3 R# log 2`,                                     (R20.6)

we have

`0 < p/q-beta < 1/(2q^2)`.

Legendre's theorem implies:

> **RL20-CF gate.** Under (R20.6), the reduced ratio `p/q` must be a continued-fraction convergent of `beta=log 3/log 2`, and specifically one lying above `beta`.

There is a second useful form.  If `p_n/q_n=p/q` and `q_(n+1)` is the next convergent denominator, the standard convergent lower bound

`|beta-p_n/q_n| > 1/[q_n(q_n+q_(n+1))]`

combined with (R20.5) yields

`q_(n+1) > 3R# log2/q - q`.                                (R20.7)

Thus a reduced odd-count denominator much smaller than `sqrt(R#)` would require an anomalously large next partial quotient of the fixed number `log_2 3`.

This is a radius-independent arithmetic coupling between the RL19 state packing and the two-logarithm resonance.

## 5. Exact finite consequence from the inherited `R#>=2^71` floor

Now use the inherited external cycle-minimum floor

`R# >= R0 := 2^71`.

Let

`Q0 = 49,547,666,543`.

The verifier `verify_rl20_global_cf_gate.py` proves with rational interval arithmetic for `log 2` and `log 3` that

`2 Q0^2 < 3 R0 log 2`.

Hence any reduced denominator `q<=Q0` must be an above-`beta` convergent by the RL20-CF gate.

The same verifier rigorously reconstructs the continued-fraction prefix of `beta` and finds the above-`beta` convergents through this range:

`2/1, 8/5, 65/41, 485/306, 24727/15601, 125743/79335,`

`301994/190537, 17087915/10781274, 272500658/171928773,`

`630138897/397573379, 10439860591/6586818670`.

For an actual cycle with `(A,L)=g(p,q)`, (R20.4) is equivalent to

`p log2 - q log3 <= q/(3R#) <= q/(3R0)`.                  (R20.8)

Using rigorous rational lower/upper bounds for the logarithms, the verifier checks that every listed above-`beta` convergent instead satisfies

`p log2 - q log3 > q/(3R0)`.

Therefore all are excluded.

So, conditional only on the inherited external floor,

> **`L/gcd(A,L) >= 49,547,666,544`.**                     (R20.9)

In particular `L >= 49,547,666,544`.

Evidence label: **EXACT FINITE CERTIFICATE + EXTERNAL COMPUTATIONAL INPUT**, on top of the analytic RL19 product identity and classical Legendre/continued-fraction theory.

No LMN theorem is used in this new bound.

## 6. Strategic consequence

The near-resonant branch is no longer merely “`A/L` is close to `log_2 3`.”  Below the square-root scale of the least state it is forced onto the discrete continued-fraction spine of `log_2 3`; the inherited `2^71` floor then removes that entire spine through reduced denominator `4.95e10`.

This still leaves an enormous unbounded branch.  The next useful target is to combine (R20.7) with one of:

1. an RL-specific restriction on `g=gcd(A,L)` or on admissible convergent indices;
2. the final-return 3-adic address, which may constrain `A,L` modulo powers of 3;
3. a weighted-difference/proper-factor obstruction;
4. an explicit two-logarithm lower bound only after preserving the `R#` dependence.

# RL19 — exact odd-step product identity and strengthened least-state packing

## Status

**ANALYTIC.** This note uses only the standard shortcut Collatz step equations and the least-state/primitive-cycle hypotheses. No external theorem and no finite cutoff is used in the derivation.

It does **not** prove RL or Collatz.

## 1. Exact product identity

Let a positive primitive cycle be written in full-parity phases `x_i`, with parity bits `d_i in {0,1}`, length `A`, weight `L`, and

`lambda = 2^A / 3^L > 1`.

For an even phase,

`x_(i+1)/x_i = 1/2`.

For an odd phase,

`x_(i+1)/x_i = (3x_i+1)/(2x_i) = (3/2)(1+1/(3x_i))`.

Multiplying around the whole cycle and using `prod_i x_(i+1)/x_i = 1` gives

`1 = (3^L/2^A) prod_(d_i=1) (1+1/(3x_i))`.

Hence

`lambda = prod_(d_i=1) (1+1/(3x_i))`.                 (R19P.1)

Equivalently,

`log lambda = sum_(d_i=1) log(1+1/(3x_i))`.           (R19P.2)

## 2. Least-state odd packing

Let `R#` be the least cycle state. It is odd. In a primitive cycle the `L` odd phase states are distinct odd integers, all at least `R#`. After sorting them as `y_0<...<y_(L-1)`, therefore

`y_j >= R# + 2j`.                                      (R19P.3)

Since `x -> log(1+1/(3x))` is decreasing on positive reals, (R19P.2) yields

`log lambda <= sum_(j=0)^(L-1) log(1+1/(3(R#+2j)))`.   (R19P.4)

Using `log(1+t)<=t`,

`log lambda <= (1/3) sum_(j=0)^(L-1) 1/(R#+2j)`.       (R19P.5)

The elementary integral estimate

`sum_(j=0)^(L-1) 1/(R#+2j)
 <= 1/R# + (1/2) log(1+2(L-1)/R#)`

gives

`log lambda
 <= 1/(3R#) + (1/6) log(1+2(L-1)/R#)`.                (R19P.6)

Rearranging,

`L >= 1 + (R#/2)(lambda^6 exp(-2/R#)-1)`.               (R19P.7)

This is a radius-independent necessary condition for any primitive positive cycle.

## 3. Relation to the RL19 weighted-population bound

The earlier weighted-population argument proved

`D/2^A <= 1/(3R#) + (1/6)log(1+2(L-1)/R#)`.

Since

`D/2^A = 1-1/lambda < log lambda`

for `lambda>1`, (R19P.6) is strictly stronger whenever it is applicable. Thus the preferred global least-state dichotomy should now be stated using `log lambda`, not merely `D/2^A`.

For any chosen `eta>0`, either

`0 < log lambda < eta`,

or

`L >= 1 + (R#/2)(exp(6eta-2/R#)-1)`.                    (R19P.8)

Conditional on any inherited external lower bound for `R#`, this turns a non-near-resonant branch into an enormous lower bound on `L`. The lower bound on `R#` remains an **EXTERNAL COMPUTATIONAL INPUT** wherever it is used numerically.

## 4. Strategic consequence

The global problem is now concentrated into two branches:

1. **Near resonance:** `A log 2 - L log 3 = log lambda` is very small. A two-logarithm lower bound may be useful here, but any use of Laurent–Mignotte–Nesterenko must remain explicitly labelled **EXTERNAL: LMN**.
2. **Huge length:** if the logarithmic gap is not tiny, then `L` must be comparable to the least state `R#` by (R19P.7).

Neither branch is presently contradictory. A useful next theorem must couple one of them to additional RL-specific root/final-return, ownership, congruence, or arbitrary-radius weighted-difference structure.

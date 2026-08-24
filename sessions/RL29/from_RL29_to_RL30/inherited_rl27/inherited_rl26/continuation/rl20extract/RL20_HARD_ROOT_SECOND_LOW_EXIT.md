# RL20 — hard-root / exceptional weak-close resonance forces a second low plateau or enormous length

Date: 2026-08-20

## Status

**ANALYTIC**, with the numerical `R#>=2^71` consequence conditional on the inherited **EXTERNAL COMPUTATIONAL INPUT**.

This does not prove RL. It is the first RL20 result in which the hard least-root departure and the owned final return interact with the global near-resonant slope rather than merely coexisting as endpoint residues.

## 1. Plateau factorization of the global slope

For the compressed cycle write each plateau as `(s_j,t_j)`. The inherited bookkeeping gives

`L=sum_j s_j`,

`A=L+sum_j t_j`.

Therefore

`lambda=2^A/3^L`

factors exactly as

`lambda = product_j [ 2^(s_j+t_j) / 3^(s_j) ]`.             (R20E.1)

Call a plateau **low-excess** if

`2^(s_j+t_j) < 3^(s_j)`,                                    (R20E.2)

or equivalently `t_j < s_j log_2(3/2)`.

## 2. Hard least-root factor

In the hard root branch

`s_root=2`, `t_exit=1`.

When the weak close `(n_close,t_close)=(1,1)` is also imposed, RL20 final-return phase compatibility further restricts this theorem to `R#==91 (mod 144)`.

Its factor in (R20E.1) is exactly

`2^3/3^2 = 8/9`.                                             (R20E.3)

This is the forced low departure from the least root.

## 3. Exceptional n_close=t_close=1 factor

For the final return, `n_close=s_close+mu_close`.

If

`n_close=1`, `t_close=1`,

then necessarily

`s_close=1`, `mu_close=0`.

Its factor is therefore

`2^2/3 = 4/3`.                                               (R20E.4)

Multiplying the owned root and final factors gives

`(8/9)(4/3)=32/27`.                                         (R20E.5)

## 4. Second-low-or-large-lambda dichotomy

Suppose every plateau other than the hard root is non-low, except of course the final close which is already strictly high. Then every remaining factor in (R20E.1) is at least 1. Hence

`lambda >= 32/27`.                                          (R20E.6)

Contrapositively:

> **If `lambda<32/27`, then a hard-root RL cycle with the exceptional `(n,t)=(1,1)` close must contain at least one additional low-excess plateau distinct from the root.**      (R20E.7)

In particular the older near-resonant branch `lambda<16/15` lies strictly inside this regime because

`16/15 < 32/27`.

So in that branch the endpoint ownership forces a second dense/low block somewhere else on the cycle.

## 5. The alternative branch is quantitatively enormous

RL20 strengthened the packing inequality to

`log lambda <= 1/(3R#) + (1/9) log(1+3(L-1)/R#)`.

Rearranging gives

`L >= 1 + (R#/3) [ lambda^9 exp(-3/R#) - 1 ]`.              (R20E.8)

If `lambda>=32/27` and `R#>=2^71`, then `exp(-x)>1-x` gives

`lambda^9 exp(-3/R#)`

`> (32/27)^9 (1-3/2^71)`

`> 23/5`.

The last inequality is checked exactly by rational arithmetic. Therefore

`L > 1 + 6R#/5`.                                           (R20E.9)

Conditional on the external floor `R#>=2^71`, this is an odd-count lower bound above `2.83e21`.

Thus the unique hard weak-close branch (`R#==91 mod144`, `n=t=1`) now has the structural dichotomy

> **either an additional low-excess plateau exists, or the cycle has `L>1+6R#/5`.**

## 6. Why this is more useful than the direct CF/address coupling

The final-return discrete-log address alone did not select `(A,L)` classes because `t_close` is only one free summand of `A-L`.

Here, by contrast, the least-root and final-return plateaus are **owned positions in the same multiplicative factorization of the global slope**. Their product already overshoots the near-resonant target by the fixed factor `32/27`, so the rest of the cycle must either provide a compensating low plateau or accept a large global slope and hence an enormous state-packing cost.

The next useful question is therefore no longer “which CF convergent does the final address permit?” It is:

> **Can the additional low plateau forced by (R20E.7) be made canonical/owned strongly enough to create a forbidden weighted rotation difference or a repeatable descent?**

Verifier: `verify_rl20_hard_root_second_low.py`.

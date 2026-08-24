# RL20 — the exceptional hard weak close gives a global numerator lower bound

Date: 2026-08-20

## Status

**ANALYTIC.**  The clean numerical simplification using `L>=92` is conditional on the inherited accepted external input RL-E3 (a nontrivial cycle has at least 92 local minima, hence at least 92 odd steps).

This does not prove RL.  It is a genuine `D|Q`/ownership coupling in the unique hard-root branch where the final local address itself is weakest.

## 1. Unique weak endpoint package

By `RL20_FINAL_RETURN_PHASE_COMPATIBILITY.md`, the only hard-root branch with

`t_close=1`

is

`R# == 91 (mod 144)`, `n_close=1`, `t_close=1`.

The hard root departure is

`s_root=2`, `t_exit=1`,

so the least-state full parity word begins with

`110`.

The `n_close=t_close=1` physical close is the block

`10`.

Thus the whole least-state word has the exact decomposition

`d = 110  e  10`,                                           (R20N.1)

where the middle word `e` has

`M=A-5`, `N=L-3`.

Because every plateau has `t>=1`, this branch has `A-L>=2`, so `M>=N`.

## 2. Exact concatenation identity for Q

For binary words `u,v`, the standard Collatz word numerator satisfies

`Q(uv)=3^(|v|_1) Q(u)+2^(|u|) Q(v)`.

The endpoint blocks have

`Q(110)=5`, `Q(10)=1`.

Applying concatenation twice to (R20N.1) gives

`Q(d)=5*3^(L-2) + 24 Q(e) + 2^(A-2)`.                     (R20N.2)

For a binary word of weight `N`, its numerator is minimized by placing all ones first.  Hence

`Q(e) >= 3^N-2^N`.                                         (R20N.3)

Substituting `N=L-3` into (R20N.2),

`Q(d) >= (13/9) 3^L + 2^(A-2) - 3*2^L`.                  (R20N.4)

## 3. Use the genuinely global condition D|Q

For an actual least-state cycle,

`Q(d)=D R#`,

`D=2^A-3^L`,

and put

`lambda=2^A/3^L`.

Divide (R20N.4) by `3^L`:

`R# (lambda-1) >= 13/9 + lambda/4 - 3(2/3)^L`.             (R20N.5)

Rearranging the `lambda/4` term yields the exact endpoint-owned lower bound

`(R#-1/4)(lambda-1)`

`>= 61/36 - 3(2/3)^L`.                                     (R20N.6)

This is not an endpoint congruence.  It uses the whole-word divisibility identity `Q=D R#` and a global lower bound on the middle numerator.

## 4. Clean consequence from the inherited local-minimum floor

The inherited accepted result RL-E3 gives at least `92` local minima in a nontrivial cycle.  In particular

`L>=92`.

Already for `L>=12`,

`61/36 - 3(2/3)^L > 5/3`.

Therefore the exceptional hard weak-close branch satisfies

`lambda-1 > 5/[3(R#-1/4)]`.                                (R20N.7)

In the near-resonant branch

`lambda<16/15`,

put

`delta_D=D/2^A=1-1/lambda=(lambda-1)/lambda`.

Then (R20N.7) gives

`D/2^A > 25/[16(R#-1/4)]`.                                 (R20N.8)

Asymptotically this is a lower defect of more than

`1.5625/R#`,

substantially stronger than the old closing-edge-only lower bound `1/[2(R#+1)]` for this branch.

## 5. A two-sided logarithmic-form window

Because

`log lambda > D/2^A`,

(R20N.8) and the RL20 coprime-6 state-packing upper bound combine to give

`25/[16(R#-1/4)]`

`< A log2-L log3`

`<= 1/(3R#) + (1/9) log(1+3(L-1)/R#)`.                    (R20N.9)

For the reduced pair

`p=A/g`, `q=L/g`,

this becomes a genuine global ownership constraint on the two-logarithm error

`p log2-q log3`

rather than the failed local statement about `t_close`.

If the reduced ratio is a continued-fraction convergent and `q_next` denotes the next convergent denominator, the standard convergent upper error bound also gives

`q_next < [16 g (R#-1/4) log2]/25`.                         (R20N.10)

Together with RL20's existing lower bound

`q_next > 3R# log2/q - q`,

this sandwiches the next denominator from both sides.  The present constants do not yet contradict the large surviving convergent classes, but this is an actual `D|Q`-based CF coupling, unlike the retired address-only route.

## 6. Strategic consequence

The unique `t_close=1` branch is no longer merely a local endpoint nuisance.  Its fixed endpoint bits force a global positive amount of normalized numerator mass.

The next useful strengthening would be to improve (R20N.3) using any additional mandatory structure of the middle word—especially a globally owned second low plateau, multiple local minima at controlled positions, or a proper rotation/factor constraint.  Any improvement of the constant in (R20N.6) feeds immediately into the lower side of the two-logarithm window (R20N.9).

Verifier: `verify_rl20_hard_universal_global_numerator.py`.

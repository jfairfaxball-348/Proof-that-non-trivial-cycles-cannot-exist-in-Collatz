# Collatz R# RL-4 — Crossing/Slack Compression and the First Cycle-Coupled Xi Exit Filter

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-3 seed  
**Verdict:** RL remains open. The `k>0` relative-height state can be compressed substantially before the first order crossing, and the `k=0` branch now has a genuine cycle-coupled xi restriction at the exit from the exact neutral spine. Neither mechanism closes its branch by itself.

## 1. Reproduction

The inherited RL-3 verifier passes. The new verifier

`tools/verify_rl4_crossing_exit.py`

also passes. It audits exact finite consequences of the analytic statements below; it is not a proof that nontrivial Collatz cycles do not exist.

## 2. Notation for the strict-preperiod comparison

Assume `k>0`. Unwrap the cycle backwards from the entry `c0` and compare it to the true preperiod backwards:

- `x_0=y_0=c0`;
- `x_h=r_(k-h)` for `0<=h<=k`;
- `y_h=c_(-h mod L)` for the periodically unwrapped cycle;
- `d_i=b_(k-i-1)` and `e_i=a_(-i-1 mod L)` are the reverse exponents used from depth `i` to `i+1`;
- `D_h=sum_(i=0)^(h-1) d_i`, `E_h=sum_(i=0)^(h-1) e_i`.

Thus

`x_i=(3 x_(i+1)+1)/2^(d_i)`

and similarly for `y`.

RL-L14 says `d_0!=e_0` and `d_0=e_0 (mod 2)`. Hence the entry exponent gap is `|d_0-e_0|=2m`, `m>=1`.

## 3. RL-L23 — exact relative product and first-crossing exponent catch-up

For every `h>=1`,

`2^(D_h) = (x_h/c0) * product_(i=1)^h (3+1/x_i)`

and

`2^(E_h) = (y_h/c0) * product_(i=1)^h (3+1/y_i)`.

Therefore the exact relative ratio is

`x_h/y_h = 2^(D_h-E_h) * product_(i=1)^h [(3+1/y_i)/(3+1/x_i)]`.      (R23.1)

Moreover `x_h!=y_h` for every `h>=1`: equality at equal depth would give the same deterministic forward accelerated orbit from that physical state to `c0`, forcing the two length-`h` exponent words to be equal, contradicting `d_0!=e_0`.

### Down-crossing

Suppose `x_1>y_1`, and let `H` be the first depth with `x_H<y_H`. Then

`D_H <= E_H`.      (R23.2)

Indeed, all factors in (R23.1) before the crossing are `>1`. At the crossing factor,

`(3+1/y_H)/(3+1/x_H) > 3/4`

because `1<=x_H<y_H`. If `D_H-E_H>=1`, then (R23.1) would give

`x_H/y_H > 2*(3/4)>1`,

a contradiction.

Since `D_1-E_1=2m`, the later reverse phases must erase the entire entry exponent advantage:

`sum_(i=1)^(H-1) (e_i-d_i) >= 2m`.      (R23.3)

### Up-crossing

Symmetrically, suppose `x_1<y_1`, and let `H` be the first depth with `x_H>y_H`. Then

`D_H >= E_H`.      (R23.4)

Before the crossing all correction factors in (R23.1) are `<1`; at the crossing factor it is `<4/3`. If `D_H-E_H<=-1`, then

`x_H/y_H < (1/2)*(4/3)<1`,

again impossible.

Thus every first order reversal forces the cumulative exponent-sum order to reverse as well.

**Status: PROVED ANALYTIC THEOREM.**

### Strategic consequence

For the tail-larger entry orientation, a continuous ratio interval is not needed to certify the first crossing. The discrete state

`(cycle phase, sign(x_h-y_h), D_h-E_h)`

already contains an exact necessary crossing condition. Ratio information may still be useful after multiple crossings, but it is not required for the first one.

## 4. RL-L24 — least-red prefix slack dominates physical height

Let

`R#=r_0 -> r_1 -> ... -> r_n`

be any forward odd prefix of the true preperiod, with exponent sum

`S_n=b_0+...+b_(n-1)`.

Set

`beta_R = log2(3+1/R#)`

and define the prefix slack

`sigma_n = n beta_R - S_n`.

The exact product identity gives

`2^(S_n) = (R#/r_n) * product_(i=0)^(n-1) (3+1/r_i)`.

Since every `r_i>=R#`,

`r_n/R# <= 2^(sigma_n)`,

or equivalently

`log2(r_n/R#) <= sigma_n`.      (R24.1)

So prefix slack is not merely an exponent budget: it is an exact upper budget for logarithmic physical height above the least-red floor.

### Entry-gap slack debt

Now take the entry orientation

`d_0-e_0=2m>0`.

Let `n=k-1`; then `r_n=x_1` is the tail predecessor of `c0`. RL-L20 gives

`x_1 = 4^m y_1 + (4^m-1)/3`,

with the cycle predecessor `y_1>R#`. Hence

`x_1/R# > 4^m`.

Applying (R24.1),

`sigma_(k-1) > 2m`.      (R24.2)

Thus the factor-of-`4^m` entry amplification consumes more than `2m` bits of the prefix slack available before the entry predecessor.

Let `N_1` be the number of exponent-1 moves among `b_0,...,b_(k-2)`. Since every other exponent is at least 2,

`S_(k-1) >= 2(k-1)-N_1`.

Combining with (R24.2) gives the length-sensitive density bound

`N_1 > (k-1)(2-beta_R) + 2m`.      (R24.3)

This is complementary to RL-L22. RL-L22 gives a gap-only contraction bound; (R24.3) adds the ordinary least-red one-density cost over the full prefix before the entry predecessor.

**Status: PROVED ANALYTIC THEOREM.**

## 5. RL-L25 — first-crossing phase/slack certificate

Let the total preperiod exponent sum be `B`, and let

`s = beta_R*k - B >= 0`

be the total preperiod slack.

Suppose the tail-larger orientation has its first down-crossing at depth `H`. Let `D_H` be the tail suffix exponent sum over those `H` reverse steps. The complementary forward prefix has length `k-H`, so RL-L5 gives

`B-D_H <= beta_R (k-H)`.

Hence

`D_H >= beta_R H - s`.      (R25.1)

By RL-L23, first crossing also requires `D_H<=E_H`. Therefore

`s >= beta_R H - E_H`.      (R25.2)

Now write

`H=qL+r`, `0<=r<L`,

and let `E_r^-` be the sum of the last `r` exponents of the entry rotation of the cycle, with `E_0^-=0`. Periodic unwrapping gives

`E_H=qA+E_r^-`.

So (R25.2) becomes

`s >= q(beta_R L-A) + (beta_R r-E_r^-)`.      (R25.3)

In the `k>0` branch every cycle state is `>R#`, so the cycle product identity gives the strict inequality

`A < beta_R L`.

Consequently, for a fixed candidate cycle and fixed total preperiod slack, the first down-crossing can occur only within finitely many full reverse turns of the cycle at any fixed phase `r`.

This does not close `k>0`, because `s`, `k`, and the candidate cycle are themselves unbounded. It does, however, replace an unbounded ratio state before first crossing by a phase plus a scalar slack threshold.

**Status: PROVED ANALYTIC THEOREM.**

## 6. Rank-3 verdict — contraction debt is not just a duplicate variable

RL-L22 and RL-L24 are related but not identical:

- RL-L22 is a pure height-contraction theorem. It says the larger-entry branch needs enough exact reverse exponent-1 contractions to erase `4^m`, regardless of preperiod length.
- RL-L24 says the same entry amplification must be paid out of the prefix slack and yields the length-sensitive one-density bound (R24.3).
- Near the shortest possible preperiod for a given gap, RL-L22 can be the sharper numerical statement; for longer preperiods, (R24.3) adds a growing baseline density term.

Therefore the automaton should not keep a separate arbitrary “height debt” coordinate, but it should retain both:

1. the integer count/gap consequence from RL-L22; and
2. the scalar prefix slack, which now has the direct physical interpretation (R24.1).

## 7. k=0 notation — exact neutral spine at the cycle minimum

Now assume `k=0`, so

`R#=c_0=C_min`.

Write

`R#+1 = 2^s q`,

where `s=v2(R#+1)>=2` and `q` is odd. Since `R#=1 (mod 3)`, `q` is a 3-adic unit.

RL-L17 gives exactly `s-1` initial exponent-1 steps. For `0<=j<=s-1`,

`c_j+1 = 2^(s-j) 3^j q`,

and

`xi(c_j)=R#+1`.

Call these phases the **neutral spine**. Since a full period cannot consist entirely of exponent-1 steps, `s<=L`. The boundary case `s=L` means the neutral spine occupies every cycle state and the unique non-1 exit is the closing exponent back to `R#`.

## 8. RL-L26 — equality in the xi barrier occurs only on the neutral spine

For any red odd state `y`, put `m=v3(y+1)`. RL-N1 gives

`xi(y)-1 = B^m(y)`,

where each `B` is a legal inverse exponent-1 step. By inverse closure, `B^m(y)` is red, so

`xi(y)-1 >= R#`.

If equality holds, then

`B^m(y)=R#`.

Forward determinism forces the next `m` accelerated exponents from `R#` all to be 1 and reaches `y`. In the `k=0` branch RL-L17 says this can happen only inside the exact initial neutral spine.

Therefore, for cycle phases in one period,

`xi(c_j)=R#+1  <=>  0<=j<=s-1`.      (R26.1)

Every other cycle phase satisfies the strict gap

`xi(c_j) >= R#+3`.      (R26.2)

The `+3` rather than `+2` comes from parity: `xi(c_j)-1` and `R#` are odd, so a strict inequality between them is at least 2.

**Status: PROVED ANALYTIC THEOREM.**

## 9. RL-L27 — cycle-coupled restriction on the exponent that exits the neutral spine

Assume first that `s<L`, so the state after the neutral-spine exit is a distinct cycle state above the minimum. At the last neutral phase,

`c_(s-1)+1 = 2*3^(s-1) q`.

Hence

`3 c_(s-1)+1 = 2(3^s q-1)`.

Define

`t = v2(3^s q-1) >= 1`.

Then the first non-1 cycle exponent is exactly

`a_(s-1)=t+1`,      (R27.1)

and the first post-neutral cycle state is

`c_s = (3^s q-1)/2^t`.      (R27.2)

Because `c_s` is a distinct odd cycle state above the minimum,

`c_s >= R#+2 = 2^s q+1`.

Using (R27.2), this implies

`2^(t+s) < 3^s`,

or

`t < s log2(3/2)`.      (R27.3)

In particular `t<s`.

Now put

`r = v3(2^t-1)`.

Since `t<s`, the two terms in

`c_s+1 = (3^s q + 2^t-1)/2^t`

have unequal 3-adic valuations `s` and `r<s`. Thus

`v3(c_s+1)=r`.      (R27.4)

Explicitly,

- if `t` is odd, `r=0`;
- if `t` is even, `r=1+v3(t/2)` by LTE.

The phase `c_s` lies outside the neutral spine, so RL-L26 gives

`xi(c_s) >= R#+3`.

Substituting (R27.2) and (R27.4) and rearranging forces the sharper necessary inequality

`2^(t+s-r) < 3^(s-r)`,      (R27.5)

or equivalently

`t < (s-r) log2(3/2)`.      (R27.6)

The boundary case `s=L` is different: the exit returns directly to `R#`, so the strict off-spine xi gap is unavailable. Then `t` is odd (the closing exponent into `R#=1 mod3` is even) and exact closure reduces to

`(2^(s+t)-3^s) q = 2^t-1`.      (R27.7)

This exceptional one-plateau Diophantine subbranch is **not** closed here.

For `s<L`, (R27.5) is the first xi restriction in the project that is simultaneously tied to:

- the actual minimum rotation of the hypothetical cycle;
- the exact forward exponent word leaving that minimum;
- a 2-adic valuation `t`; and
- the resulting 3-adic cycle-state valuation `r`.

**Status: PROVED ANALYTIC THEOREM.**

### Immediate low-`s` consequences

In the ordinary post-neutral case `s<L`, the sharpened condition (R27.5) leaves only `t=1` for

`s=2,3,4`.

Therefore in all three cases the first exponent after the neutral spine is exactly

`a_(s-1)=2`.

For `s=3`, `t=1` gives `q=1 (mod 4)`, hence

`R#=7 (mod 32)`.

So the inherited `R#=7 (mod 16)` k=0 branch loses its `R#=23 (mod 32)` half.

For exact `s=4`, `t=1` gives `q=3 (mod 4)`, hence

`R#=47 (mod 64)`.

Thus the exact-`s=4` cylinder `R#=15 (mod 64)` is excluded; the `s>=5` cylinders are not affected by that particular consequence.

## 10. RL-L28 — exact compression of every exponent-1 plateau

The neutral-spine calculation has a cycle-wide form.

Let `y` be any odd cycle state and write

`y+1 = 2^s 3^mu q`,

where `s=v2(y+1)>=1`, `mu=v3(y+1)>=0`, and `gcd(q,6)=1`. Define

`n=s+mu`

and the plateau xi level

`W=xi(y)=2^n q`.

If `s>=2`, the forward accelerated orbit has exactly `s-1` consecutive exponent-1 steps. On each such step,

`(s,mu,q) -> (s-1,mu+1,q)`.

Therefore both

`n=s+mu`

and

`W=2^n q`

are invariant across the whole exponent-1 run.

At the last state of the plateau,

`y_*+1 = 2*3^(n-1) q`.

Set

`t=v2(3^n q-1)`.

Then the first non-1 exit exponent is exactly

`a_*=t+1`,

and its successor is

`z=(3^n q-1)/2^t`.      (R28.1)

For the next 3-adic level, put

`r=v3(2^t-1)`.

Since

`z+1=(3^n q+2^t-1)/2^t`,

the valuation is classified exactly by the comparison of `r` with `n`:

- if `r<n`, then `v3(z+1)=r`;
- if `r>n`, then `v3(z+1)=n`;
- if `r=n`, cancellation may raise the valuation above `n`.

Thus an arbitrarily long exponent-1 block can be compressed to one plateau state `(n,q,W)` plus one exit parameter `t`.

**Status: PROVED ANALYTIC THEOREM.**

## 11. RL-L29 — regular plateau exits have an exact xi-rise/xi-descent threshold

Continue with RL-L28 and assume the exit is **regular**, meaning

`t<n`.

Then `r<t<n`, so the next 3-adic valuation is exactly `r`. Let

`W'=xi(z)`.

A direct subtraction gives

`3^r 2^t (W'-W)`

`= 2^r ( [3^n-3^r 2^(n+t-r)] q + 2^t-1 )`.      (R29.1)

Hence, if

`2^(n+t-r) < 3^(n-r)`,      (R29.2)

then the coefficient of `q` on the right of (R29.1) is positive and therefore

`W'>W`.      (R29.3)

Equivalently, any regular exit with

`W'<=W`

must satisfy the opposite strict threshold

`2^(n+t-r) > 3^(n-r)`,      (R29.4)

or

`t > (n-r) log2(3/2)`.      (R29.5)

There is no equality case because a positive power of 2 cannot equal a positive power of 3.

### Cycle-wide consequence in `k=0`

Assume the root neutral spine has `s<L`. Compress the cycle into maximal exponent-1 plateaus. The root plateau has the unique minimum xi level

`W_0=R#+1`

by RL-L26. Its exit lands off the neutral spine, so the next plateau has xi level `>W_0`.

Because the compressed plateau sequence is periodic and eventually returns to `W_0`, at least one later plateau exit must strictly decrease the xi level. Therefore every such hypothetical cycle contains a later exit of one of two types:

1. a **deep exit** with `t>=n`; or
2. a **regular-high exit** with `t<n` and `2^(n+t-r)>3^(n-r)`.

The root exit is a low-threshold event by RL-L27, while a later xi descent must be high/deep. This is the first cycle-wide alternation rule for the plateau grammar.

**Status: PROVED ANALYTIC THEOREM.**

## 12. RL-L30 — plateau xi telescoping reproduces the scalar cycle-slope identity exactly

The plateau compression also identifies a redundancy that should not be mistaken for new cycle information.

For plateau `j`, use the RL-L28 variables

`(s_j, mu_j, n_j, q_j, t_j, W_j)`

and let `mu_(j+1)=v3(y_(j+1)+1)` be the 3-adic valuation at the next plateau start. Define

`eps_j = log2(1 + (2^(t_j)-1)/(3^(n_j) q_j)) > 0`.

The exact transition (R28.1) gives

`W_(j+1)/W_j`

`= (3/2)^(n_j-mu_(j+1)) * 2^(-t_j)`

`  * (1 + (2^(t_j)-1)/(3^(n_j) q_j))`.      (R30.1)

Therefore

`log2(W_(j+1)/W_j)`

`= (n_j-mu_(j+1)) log2(3/2) - t_j + eps_j`.      (R30.2)

Now compress a whole cycle into `P` plateaus. Each plateau contains `s_j-1` exponent-1 moves followed by one exit exponent `t_j+1`, so

`L = sum_j s_j`

and

`A = sum_j (s_j+t_j) = L + sum_j t_j`.      (R30.3)

Also `n_j=s_j+mu_j`, and the `mu` terms telescope cyclically:

`sum_j (n_j-mu_(j+1)) = sum_j s_j = L`.      (R30.4)

Finally `W_P=W_0`, so summing (R30.2) yields

`A - L log2(3) = sum_j eps_j`.      (R30.5)

Thus the **scalar** sum of plateau xi changes is exactly another form of the classical positive cycle-slope defect. It is not, by itself, an independent strengthening of RL-L7.

The new information in the plateau grammar is therefore discrete, not scalar: which valuations `mu_(j+1)` are permitted by a given exit `t_j`, where deep/cancellation exits occur, and where the xi-level order must rise or fall.

**Status: PROVED ANALYTIC THEOREM / STRUCTURAL REINTERPRETATION.**

## 13. RL-G8 — the one-exit cycle-coupled filter still has positive 2-adic measure

The new exit condition prunes substantially more than the old root-only xi ceilings, but a single neutral-spine exit is still not enough to close `k=0`.

To measure the strength of the **ordinary post-neutral** filter, normalize Haar measure inside the 2-adic cylinder

`R#=3 (mod 4)`.

Then

`P(s=n)=2^(1-n)`, `n>=2`.

For fixed `s`, the odd unit `3^s q` is Haar-uniform among odd 2-adic units, so

`P(t=n | s)=2^(-n)`, `n>=1`.

Let

`r(t)=v3(2^t-1)`

and define `s_min(t)` as the least `s>=2` satisfying the exact exit inequality

`2^(t+s-r(t)) < 3^(s-r(t))`.

Ignoring the single boundary valuation `s=L` for a moment, the inverse-limit conditional survivor measure of the one-exit filter is therefore

`mu_exit = sum_(t>=1) 2^(2-t-s_min(t))`.      (G8.1)

The `t=1` term alone contributes `1/2`, so the filter has positive measure immediately. Summing the first 30 terms gives

`2612725980859984691467425 / 4835703278458516698824704`

`= 0.5402990693202431...`

and the omitted tail is `<2^-30`. Thus

`0.5402990693202431 < mu_exit < 0.5402990702515657`.

So the ordinary post-neutral condition removes about 46% of the 2-adic root cylinder but still leaves about 54%. For a fixed candidate cycle length `L`, the exceptional boundary cylinder `s=L` has conditional 2-adic mass `2^(1-L)` and must be handled by (R27.7), while `s>L` is impossible. Thus the fixed-`L` survivor mass differs from the displayed inverse-limit value only by the finite truncation/boundary terms. By CRT the same 2-adic analysis applies inside any fixed compatible mod-9 root cylinder.

**Status: FAILED / REFUTED ROUTE for “the first neutral-spine exit condition alone closes k=0”.**

This is nevertheless qualitatively different from RL-G7: the filter is no longer root-only. It uses an actual cycle rotation and an actual adjacent cycle exponent.

## 14. New finite audit

`tools/verify_rl4_crossing_exit.py` checks:

- 3,840 exact inverse-product identities;
- 46,080 equal-depth noncollision instances;
- 2,199 first down-crossing exponent catch-up instances;
- 2,199 first up-crossing exponent catch-up instances;
- 385 least-red height/slack prefixes;
- 20 explicit entry slack-debt instances;
- 2,474,832 suffix/phase/slack algebra instances;
- 45,925 exact neutral-spine identities;
- 3,304 neutral-exit implications;
- 40,000 general plateau normal-form checks;
- 40,000 plateau xi-ratio checks;
- 21,329 regular plateau-exit checks;
- 4,535 regular xi-descent checks;
- 18,671 deep-exit diagnostics;
- the 30-term exact rational partial sum for `mu_exit` and its geometric tail bound.

**Status: EXACT FINITE CERTIFICATE for the stated audit domain.**

## 15. Current endpoint

RL is still open, but both branches have moved to a more compressed state space.

### `k>0`

Before the first relative-order crossing, keep

`(entry orientation, cycle phase, sign, cumulative exponent difference, total/prefix slack, exponent-1 count)`.

Do **not** carry a free continuous ratio variable unless a later multi-crossing argument proves it necessary. RL-L23 and RL-L25 already turn the first crossing into discrete exponent catch-up plus a phase/slack threshold.

### `k=0`

Do **not** return to root-only xi probes. RL-L28 now gives the exact plateau compression, so the next state can be reduced to

`(cycle phase, plateau n, unit q or a quotient code, xi level W, exit t, next valuation class)`

rather than tracking every exponent-1 step individually. RL-L29 forces at least one later high/deep xi-descent after the low root exit.

The most promising next theorem is a **plateau/exit density grammar**: prove that repeated applications of the exact neutral-run and xi-exit rules force either a forbidden return to the minimum or a cycle-wide exponent/valuation density incompatible with the product slope.

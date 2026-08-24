# RL54 — Uniform late-zero defect reduction

Date: 2026-08-23

## Status

**Analytic reduction + exact rational verifier.** This is not a terminal theorem and does not by itself close z=41, Gate A, RL, or Collatz.

Work inside the sole inherited safe continued-fraction survivor, with

- `Zx > 143/12`,
- `E < 5/3`,
- sequential x-zero cap `w_j < 17/30`,
- exact defect formula `E=sum_j w_j[1-(2/3)^r_j]`,
- `z=q-t` odd.

Let `R=z-27` be the number of x-zero indices after the first 26.

## 1. Uniform self-seeding recurrence

Assume the last `t` late x-zero weights have already been forced below `2^-1000`, and put

`n=(z-1)-t`.

For every `n>=30`, suppose `h=n-22` matching y-zeroes among the first `n` x-zero indices were delayed beyond the current cut. The exact defect lower bound has the form

`E >= 143/12 - M_22 - C_n - t*2^-1000`,

where `M_22` is the exact greedy mass of the first 22 x-zero weights and

`C_n = w_n * (2^(n-21)-2)/3^(n-22)`.

Because `w_n<17/30` and the ratio `(2^(m+1)-2)/3^m` is strictly decreasing for `m>=2`, every `n>=30` is bounded below by the `n=30` cap case. Exact rational arithmetic gives

`E > 1.681870022295953 > 5/3`,

a contradiction. Therefore at most `n-23` such y-zeroes are delayed.

At `n=29`, the crude `17/30` cap is just too weak, but the exact greedy exponent `p_29=50` gives

`E > 1.677023477400696 > 5/3`.

Thus the same `n-23` delayed-y conclusion holds through `n=29`.

Since `t=(z-1)-n`, the total terminal y-zero budget at every stage `n>=29` is

`(n-23)+t = z-24 = R+3`.

## 2. Two fixed cleanup stages

At `n=28`, seven delayed matching y-zeroes give

`E > 2.09765037322183 > 5/3`,

so at most six are delayed. Including the later tiny indices gives total terminal y-budget

`6 + ((z-1)-28) = z-23 = R+4`.

At `n=27`, six delayed matching y-zeroes give

`E > 2.060564266359511 > 5/3`,

so at most five are delayed, again giving total terminal y-budget `R+4`.

Hence the whole late-zero induction has a z-independent shape:

- stages through `n=29`: terminal caps `(x<=t, y<=R+3)`;
- last two stages: terminal caps `(x<=t, y<=R+4)`.

## 3. Single-cap domination

All of those classes are contained in the single largest relaxed class

`(x<=R, y<=R+4)`.

Therefore **one terminal-negligibility certificate for `(R,R+4)` dominates the entire late-zero cascade**. It can be reused at every stage to force all `R` late x-zero weights tiny.

Once all `R` late weights are tiny, the exact best non-greedy first-26 x-zero schedule remains below `143/12` even after allowing the total `q*2^-1000` error. Thus the first 26 x-zero schedule is uniquely greedy and

`u_26=70`.

Five delayed first-26 matching y-zeroes after column 70 contribute exact defect

`2.059051471067492... > 5/3`,

so at most four are delayed. The genuine final suffix therefore has exactly the same largest cap

`(x<=R, y<=R+4)`.

Thus, for any fixed odd `z>=41`, a sufficiently strong terminal-small certificate for `(R,R+4)`, `R=z-27`, both bootstraps all late weights and supplies the final terminal contradiction.

## 4. z=41 specialization

For `z=41`, `R=14`, so a single terminal certificate for

`(14,18)`

is sufficient to replace all remaining individual classes `(8,17),...,(14,18)`.

The companion verifier is

`rl54_research/verify_rl54_uniform_defect_recurrence.py`.

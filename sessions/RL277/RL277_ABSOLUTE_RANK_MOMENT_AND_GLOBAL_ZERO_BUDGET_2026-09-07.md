# RL277 — absolute rank moment and global dangerous zero-budget contraction

Date: 2026-09-07

## Classification

Primary:

`ONE_SIDED_COMMON_MODE_CONSUMER_PROVED`

Promoted subordinate results:

- `ABSOLUTE_ORDERED_RANK_MOMENT_BUDGET_PROVED`
- `GLOBAL_DANGEROUS_ZERO_BUDGET_Z_GE_K_PLUS_4`

Gate A remains open uniformly. Gate B is unchanged/open. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming target and notation

RL277 starts from the checksum-clean RL276 state and targets the common-mode absolute ownership scale that survives paired determinant subtraction.

Retain the canonical internal words `x,y` of common length

`m = a-k-1`

and common weight

`r = ell-3`.

Let the one-positions be

`a_1 < ... < a_r`,
`b_1 < ... < b_r`,

with canonical prefix order

`b_j <= a_j`.

Write

`delta_j = a_j-b_j >= 0`,
`H_can = sum_j delta_j`.

The exact inherited terminal rank identity is

`3 Qx - Qy = 14*3^r + 2^(a-1) - 2^(a-k-1)`,          (1.1)

where

`Qx = sum_j 2^(a_j) 3^(r-j)`,
`Qy = sum_j 2^(b_j) 3^(r-j)`.

RL276 supplies the full-phase scale box

`3^ell < 2^a < (160/81) 3^ell`,                       (1.2)

with `ell=r+3`, and terminal `k` is inherited odd with `k>=3`.

Define the internal zero count

`m0 = m-r = z-k+2`.                                    (1.3)

The objective is to obtain a genuinely one-sided/global restriction on `m0` from (1.1), canonical order, and the absolute scale (1.2), without importing Branch-C-only counterflow theorems.

---

## 2. Absolute ordered-rank moment budget

Since `b_j<=a_j`, termwise `Qy<=Qx`, while `Qy>0`.

Put

`X = 2^a / 3^r`.

From `ell=r+3` and (1.2),

`27 < X < 160/3`.

Divide (1.1) by `3^r`:

`3 Qx/3^r - Qy/3^r
 = 14 + X(1/2 - 2^(-k-1))`.                            (2.1)

Because `k>=3`,

`1/2 - 2^(-k-1) >= 7/16`.

Using `Qy>0` in (2.1),

`Qx/3^r > (1/3)(14 + 27*7/16) = 413/48`.

Using `Qy<=Qx` and the strict upper scale bound,

`2 Qx/3^r
 < 14 + (160/3)(1/2)
 = 122/3`,

hence

`Qx/3^r < 61/3`.

Therefore

`boxed: 413/48 < Qx/3^r < 61/3`.                       (2.2)

Equivalently, with

`eta_j = a_j - (j-1) log_2 3`,

one has

`3 Qx/3^r = sum_j 2^(eta_j)`,

so

`boxed: 413/16 < sum_j 2^(eta_j) < 61`.                (2.3)

This is an absolute common-mode statement: synchronized ranks contribute positively and are not annihilated by the defect difference `Qx-Qy`.

Immediate rank-frontier consequences include

`a_j < (j-1) log_2 3 + log_2 61`,                      (2.4)

and, for every integer `h>=0`,

`#{j : eta_j >= h} < 61 / 2^h`.                        (2.5)

Thus at most 60 ranks have `eta_j>=0`, at most 30 have `eta_j>=1`, at most 15 have `eta_j>=2`, at most 7 have `eta_j>=3`, at most 3 have `eta_j>=4`, at most 1 has `eta_j>=5`, and none has `eta_j>=6`.

Classification: **analytic theorem**.

---

## 3. Zero-rank normal form

Let the zero positions of `x` be

`p_1 < ... < p_(m0)`

and those of `y` be

`q_1 < ... < q_(m0)`.

Because the one-positions satisfy `b_j<=a_j`, complementary order gives

`p_t <= q_t`.

Define

`u_t = p_t-(t-1)`,
`v_t = q_t-(t-1)`,

so `u_t` and `v_t` are the numbers of ones preceding the `t`-th zero in `x` and `y`, respectively. They are nondecreasing and

`u_t <= v_t`.

Let `rho=2/3`.

For any binary word of weight `r` and `m0` zeros, direct telescoping over its one-runs gives

`Q/3^r = 1 + sum_(t=1)^m0 2^(t-1) rho^(h_t) - 2^m0 rho^r`,   (3.1)

where `h_t` is the number of preceding ones at its `t`-th zero.

Applying (3.1) to `x` and `y`, substituting into (1.1), and using

`a = r+m0+k+1`

gives the exact global zero-rank identity

`boxed:
 sum_(t=1)^m0 2^(t-1) [3 rho^(u_t) - rho^(v_t)]
 = 12 + 2^m0 (2^k+1) rho^r`.                          (3.2)

This is not the Branch-C determinant profile. It is a direct rewrite of the canonical terminal rank identity in absolute zero coordinates.

From the lower half of the phase box,

`2^a > 3^(r+3)`,

hence

`2^m0 2^k rho^r > 27/2`.

Therefore the right side of (3.2) is strictly larger than

`12 + 27/2 = 51/2`.                                    (3.3)

Dropping the negative terms on the left gives the necessary inequality

`boxed:
 sum_(t=1)^m0 2^(t-1) rho^(u_t) > 17/2`.               (3.4)

Classification: **analytic theorem**.

---

## 4. First global zero-budget consequence: `m0>=4`

If `m0<=3`, the left side of (3.4) is at most

`sum_(t=1)^m0 2^(t-1) <= 7`,

contradicting `>17/2`.

Thus every retained full-phase terminal object satisfies

`boxed: m0>=4`,                                         (4.1)

equivalently

`boxed: z>=k+2`.                                        (4.2)

Unlike the older RL248 `z>=k+3` result, (4.2) is global full-phase scope and does not use Branch C.

---

## 5. Exact four-zero contraction

Assume `m0=4`. Put

`S4 = rho^(u_1)+2 rho^(u_2)+4 rho^(u_3)+8 rho^(u_4)`.

Then (3.4) requires `S4>17/2`.

A complete elementary monotone case split gives exactly ten possibilities:

`(u_1,u_2,u_3,u_4)` in

- `(0,0,0,0)`,
- `(0,0,0,1)`,
- `(0,0,0,2)`,
- `(0,0,0,3)`,
- `(0,0,0,4)`,
- `(0,0,1,1)`,
- `(0,0,1,2)`,
- `(0,1,1,1)`,
- `(0,1,1,2)`,
- `(1,1,1,1)`.

The case split is finite because:

- `u_1>=2` gives `S4<=15(2/3)^2<17/2`;
- `u_4>=5` gives `S4<=7+8(2/3)^5<17/2`;
- the remaining small cases give exactly the ten tuples above.

Each tuple fixes the internal `x` prefix through the fourth zero. Canonical parity legality then fixes `y` deterministically. Exact replay gives:

| `u` | `x` through fourth zero | state after fourth zero `(d,J,H)` | all-`1` closure |
|---|---|---|---|
| 0000 | `0000` | `(4,39,3)` | terminal `k=5,H=18`; violates upper phase box |
| 0001 | `00010` | `(2,3,4)` | terminal `k=3,H=6`; phase-box compatible |
| 0002 | `000110` | `(2,4,5)` | stops at `d=1,J=2` |
| 0003 | `0001110` | `(3,20,6)` | terminal `k=3,H=9`; violates lower phase box |
| 0004 | `00011110` | `(1,2,6)` | no terminal |
| 0011 | `00100` | `(1,0,1)` | no terminal |
| 0012 | `001010` | `(1,0,1)` | no terminal |
| 0111 | `01000` | illegal | — |
| 0112 | `010010` | illegal | — |
| 1111 | `10000` | `(2,1,1)` | terminal `k=3,H=4`; violates lower phase box |

After the fourth zero, `x` contains only ones, so this closure is exhaustive.

The sole four-zero terminal compatible with (1.2) has

`(k,H_can)=(3,6)`,

hence is Gate-A safe.

Therefore a hypothetical Gate-A violator cannot have `m0=4`.

Classification: **exact finite canonical certificate built on the analytic zero-rank contraction**.

---

## 6. Exact five-zero contraction

Assume `m0=5` and write

`S5 = S4 + 16 rho^(u_5)`.

Again `S5>17/2`.

The four-zero case split has a useful exact gap:

among all nondecreasing four-tuples not satisfying `S4>17/2`,

`boxed: S4 <= 25/3`.                                   (6.1)

Hence, if `S4<=17/2`, then

`16 rho^(u_5) > 17/2 - 25/3 = 1/6`.

Since

`16(2/3)^11 > 1/6`,
`16(2/3)^12 < 1/6`,

one gets

`u_5<=11`.                                              (6.2)

If instead `S4>17/2`, the first four zero-ranks are one of the ten tuples in Section 5. Exact canonical all-one replay after the fourth zero becomes terminal or makes another `x=1` illegal after at most seven one-columns. A fifth zero must therefore occur by then. Since the ten tuples have `u_4<=4`, again

`u_5<=11`.

Thus every five-zero candidate is contained in the finite family

`0<=u_1<=...<=u_5<=11`,
`S5>17/2`.

There are exactly

`206`

such monotone tuples.

Canonical deterministic replay leaves exactly

`72`

legal prefixes through the fifth zero.

After the fifth zero all remaining `x` bits are `1`. Exact all-one closure gives:

- `36` terminal canonical paths;
- `19` terminals satisfying the full phase scale box (1.2);
- terminal `(k,H_can)` pairs among those 19:
  `(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(5,18),(5,20)`;
- **zero** cases with `H_can<k`.

Therefore a hypothetical Gate-A violator cannot have `m0=5`.

Classification: **exact finite canonical certificate built on an analytic finite reduction**.

---

## 7. Promoted global dangerous zero budget

Sections 4--6 prove:

if a retained genuine full-phase terminal object violates Gate A,

`H_can < k`,

then

`m0 >= 6`.

Using `m0=z-k+2`,

`boxed: H_can<k  =>  z>=k+4`.                          (7.1)

Equivalently, Gate A is now globally reduced to the region

`z>=k+4`.

This is stronger in scope than the historical Branch-C zero-budget contraction: it is a theorem about every hypothetical Gate-A-violating full-phase object satisfying the inherited canonical rank identity and scale box.

It does **not** prove Gate A. Objects with six or more internal zeros remain possible at this stage.

Classification:

`GLOBAL_DANGEROUS_ZERO_BUDGET_Z_GE_K_PLUS_4`.

---

## 8. Independent bounded red team

The portable RL277 verifier independently:

1. checks the zero-rank `Q` formula on every binary word of length at most 10 (`2,046` checks);
2. reproduces the ten four-zero rank patterns and their finite canonical closures;
3. reproduces the five-zero finite reduction:
   - 206 admissible monotone tuples,
   - 72 legal canonical prefixes,
   - 36 terminal closures,
   - 19 phase-box terminals,
   - zero Gate-A violators;
4. replays the RL66 bounded canonical terminal search through internal length 17:
   - 1,421 terminal paths,
   - 250 satisfying the RL276 phase ratio box,
   - zero bounded phase-box Gate-A violators;
5. checks the absolute moment inequalities on all 250 phase-box paths.

The bounded RL66 replay is falsification support only. The promoted `z>=k+4` theorem rests on the analytic zero-rank reduction plus the explicitly finite four-/five-zero canonical certificates.

---

## 9. Scope and barriers

Promoted:

- absolute ordered-rank moment budget (2.2)--(2.5);
- exact zero-rank identity (3.2);
- global `m0>=4`;
- exact four-zero Gate-A safety;
- exact five-zero Gate-A safety;
- global dangerous-object consequence `z>=k+4`.

Not promoted:

- any Branch-C theorem outside its inherited scope;
- any statement that `z>=k+4` closes Gate A;
- exploratory six-zero computations performed during RL277;
- any fifth-selector elimination;
- any Radius-6+ work;
- any reuse of RL231--RL237 total variation as a one-sided excursion theorem.

The six-zero exploratory replay found no counterexample, but RL277 does not promote it because the clean analytic finite-reduction proof was frozen at five zeros.

---

## 10. Successor target

RL278 should continue the same exact global zero-rank programme, not restart selector enumeration.

Primary target:

extend the finite zero-rank/canonical closure from `m0<=5` to `m0=6` and beyond, ideally obtaining either

1. a scalable induction/automaton proving a uniform lower bound on `m0=z-k+2` under `H_can<k`; or
2. a direct contradiction when the zero-rank family is combined with `H_can=sum delta_j`.

The first six-zero exploratory data are favorable but unpromoted; they must be regenerated from the frozen RL277 verifier logic and given an exact finite-reduction proof before use.

Gate B remains frozen unless a new theorem explicitly couples it to this Gate-A route.

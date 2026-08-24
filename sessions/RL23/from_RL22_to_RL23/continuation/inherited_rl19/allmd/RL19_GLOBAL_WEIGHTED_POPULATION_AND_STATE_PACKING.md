# RL19 — global weighted-flow population identities and least-state packing

## Status

All identities and inequalities in Sections 1--5 are **ANALYTIC** consequences of the standard full-parity cycle equations plus the least-state hypothesis. No finite scan or non-elementary theorem is used.

These results do **not** prove RL. They sharpen the arbitrary-radius programme by identifying what the full orbit polynomial can and cannot do, and by producing a radius-independent necessary dichotomy between near-resonance and enormous cycle length.

---

## 1. Exact positive lift of the RL18 orbit sum

Let `d=(d_0,...,d_(A-1))` be the full parity word of a positive cycle, with weight `L`,

`D=2^A-3^L>0`,

and standard word numerator `Q(d)`. Rotate to a cycle phase `R` so

`Q(d)=D R`.

Let

`P_i=sum_(j<i) d_j`,

`q_i=2^i 3^(-P_i)`,

`lambda=2^A/3^L`,

and

`Z=sum_(i=0)^(A-1) q_i`.

The exact telescoping identity behind RL18 is

`4Q(d)=2*3^L + sum_(i=1)^(A-1) 2^i 3^(L-P_i) - 2^A`.

Therefore, without reducing modulo `D`,

`3^L Z = 4Q(d)+D`,

so

`Z=(lambda-1)(4R+1)`.                                      (R19G.1)

This is important strategically: the raw RL18 orbit polynomial has a positive exact lift. Its vanishing modulo `D` is not in tension with positivity; the quotient is exactly `4R+1`. Hence a proof based only on the sign of the entire `Z` polynomial cannot be the missing global contradiction.

---

## 2. Arbitrary-radius weighted prefix-flow difference

Rotate by `m`. Let `R_m` be the resulting cycle phase and let

`G_i=P_i(rot_m d)-P_i(d)`.

The rotated prefix weight is

`q_i^(m)=q_i 3^(-G_i)`.

Apply (R19G.1) to both rotations. Then

`sum_i q_i(3^(-G_i)-1)
 = 4(lambda-1)(R_m-R)`.                                     (R19G.2)

This is an exact arbitrary-radius weighted-flow identity.

If `R=R#` is the least cycle state and the word is primitive, then every nonzero phase has `R_m>R#`, so the left side of (R19G.2) is strictly positive. Thus the negative-flow contribution must dominate the positive-flow contribution after the exact `q_i` weighting. This is a necessary sign-balance law, not by itself a contradiction.

Radius-1/2/3 coefficient arguments are small-support specializations of the same difference identity. At unbounded support, the right side shows why a naked positivity proof cannot work: the weighted numerator is exactly measuring the positive state height `R_m-R#`.

---

## 3. Exact weighted populations of odd and even phases

The positive rational weights satisfy

`q_(i+1)=2 q_i` if `d_i=0`,

`q_(i+1)=(2/3) q_i` if `d_i=1`,

with `q_A=lambda` and `q_0=1`.

Put

`E=sum_(d_i=0) q_i`,

`O=sum_(d_i=1) q_i`.

Summing `q_(i+1)-q_i` gives

`E - O/3 = lambda-1`.                                       (R19G.3)

Together with

`E+O=Z=(lambda-1)(4R+1)`,

this gives the exact population split

`O=3R(lambda-1)`,                                            (R19G.4)

`E=(R+1)(lambda-1)`.                                        (R19G.5)

This is a radius-independent orbit-population identity.

---

## 4. Least-state suffix domination

Now take `R=R#`, the least positive cycle state, and let `x_i` be the phase reached after the first `i` full-parity steps.

The complementary suffix from `x_i` back to `R#` has the affine form

`2^(A-i) R# = 3^(L-P_i) x_i + B_i`,

with `B_i>=0`. Therefore

`lambda/q_i = 2^(A-i)/3^(L-P_i) >= x_i/R#`,

or

`q_i <= lambda R#/x_i`.                                     (R19G.6)

This refines the RL-L54 suffix contraction: it weights each prefix by the actual height of its phase state.

For a primitive cycle the `A` phase states are distinct positive integers. Since `R#` is minimal,

`sum_i 1/x_i <= sum_(j=0)^(A-1) 1/(R#+j)`.                 (R19G.7)

Combining (R19G.1), (R19G.6), and (R19G.7) yields

`(D/2^A)(4R#+1)
 <= R# sum_(j=0)^(A-1) 1/(R#+j)`.                           (R19G.8)

Using the elementary integral bound,

`sum_(j=0)^(A-1) 1/(R#+j)
 <= 1/R# + log(1+(A-1)/R#)`,

we get

`D/2^A
 <= [1+R# log(1+(A-1)/R#)]/(4R#+1)`.                      (R19G.9)

---

## 5. Parity-separated state packing: the stronger bound

A least state in a positive full-parity cycle is odd: an even least state would immediately map to the smaller positive state `R#/2`.

At positions with `d_i=1`, the phase state `x_i` is odd. There are `L` distinct odd phase states, all at least `R#`. Hence, after sorting,

`x_i >= R#+2j`, `j=0,...,L-1`.

Apply (R19G.6) to the exact odd population (R19G.4):

`3R#(lambda-1)
 = O
 <= lambda R# sum_(j=0)^(L-1) 1/(R#+2j)`.

Cancel `lambda R#` and use

`1-1/lambda = D/2^A`.

Therefore

`3 D/2^A
 <= sum_(j=0)^(L-1) 1/(R#+2j)`.                           (R19G.10)

Likewise, the `A-L` even states are distinct even integers at least `R#+1`, giving

`((R#+1)/R#) D/2^A
 <= sum_(j=0)^(A-L-1) 1/(R#+1+2j)`.                         (R19G.11)

The odd-state inequality is usually the sharper one. Since

`sum_(j=0)^(L-1) 1/(R#+2j)
 <= 1/R# + (1/2) log(1+2(L-1)/R#)`,

we obtain

`D/2^A
 <= 1/(3R#) + (1/6) log(1+2(L-1)/R#)`.                    (R19G.12)

Equivalently, for any `epsilon>0`, if

`D/2^A >= epsilon`,

then

`L >= 1 + (R#/2) [ exp(6epsilon-2/R#) - 1 ]`.               (R19G.13)

This is an exact near-resonance/huge-length dichotomy.

For example, conditional on the inherited external cycle-minimum floor `R#>=2^71`:

- if `D/2^A >= 1/16`, then `L > 0.22749 R#`, hence `L > 2^68.86`;
- if `D/2^A < 1/16`, then `lambda<16/15`, equivalently
  `0 < A log 2-L log 3 < log(16/15)`.

The numerical floor is an inherited **EXTERNAL COMPUTATIONAL INPUT**; the dichotomy (R19G.13) itself is analytic.

---

## 6. Strategic consequence

The RL18 raw-orbit-polynomial route should be narrowed as follows.

**Retire:** attempts to prove `Z` nonzero modulo `D` merely from positivity, one-sided coefficient signs, or monotonicity of its positive rational lift. Equation (R19G.1) shows that the exact lift is designed to be the positive multiple `(lambda-1)(4R#+1)`.

**Keep:**

1. proper-factor/resultant obstructions for the orbit polynomial;
2. weighted *difference* identities (R19G.2), where the quotient is a phase-height difference;
3. population/state-packing constraints (R19G.10)--(R19G.13);
4. a two-logarithm or continued-fraction attack on the near-resonant branch, but only if combined with the new `R#`-dependent upper bound rather than used as an isolated cutoff engine.

No implication from radius 3 to RL is asserted here.

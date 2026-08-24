# RL42 — transport-efficiency bridge from ordered-rank displacement

Date: 2026-08-22

## Status

**ANALYTIC** in the inherited near-resonant order-2 / `g=2` balanced-return branch.

This strengthens the RL42 moved-rank/prefix-cap theorem from

`rho > (45/8)G`

to

> # **`rho > (45/4)G`.**

Since the inherited endpoint ownership gives `4|G`, every surviving return satisfies

> # **`rho >= 46`.**

This supersedes the low-area floors `rho>=28` and `rho>=29`.  Those finite certificates remain useful audits of the local excursion machinery, but are no longer needed for the transport floor itself.

Companion verifier:

`verify_rl42_transport_efficiency_bridge.py`.

RL remains open.

## 1. Exact ordered-rank equation

Retain

`X=2^a`, `Y=3^ell`, `z=X/Y>1`, `z^2<16/15`,

and ordered odd positions

`i_1<...<i_ell`, `j_1<...<j_ell`.

The exact proper-factor relation is

`(X+Y)G = sum_m 3^(ell-m)(2^(i_m)-2^(j_m))`.              (R42T.1)

For a positive moved rank `m`, put

`delta_m=i_m-j_m>=1`.

The total transport is exactly the total ordered-rank displacement,

`rho=sum_m |i_m-j_m|`.                                    (R42T.2)

In particular

`sum_(positive m) delta_m <= rho`.                        (R42T.3)

## 2. Keep the displacement factor instead of discarding it

For a positive moved rank,

`2^(i_m)-2^(j_m)=2^(i_m)(1-2^(-delta_m))`.                (R42T.4)

The RL42 prefix-cap argument already proved

`2^(i_m)/3^(m-1) <= z^2`.                                 (R42T.5)

Therefore

`3^(ell-m)(2^(i_m)-2^(j_m))`
` <= (z^2 Y/3)(1-2^(-delta_m))`.                          (R42T.6)

Negative moved ranks contribute negatively to (R42T.1), so omitting them only increases the right side.  Hence

`(z+1)YG`
` <= (z^2 Y/3) sum_(positive m)(1-2^(-delta_m))`.

Cancel `Y`:

> `sum_(positive m)(1-2^(-delta_m))`
> ` >= 3(z+1)G/z^2`.                                      (R42T.7)

This is the refined moved-rank transport inequality.

It is strictly stronger than the old count bound

`P_+ > 3(z+1)G/z^2`,

because each moved rank is weighted by the actual displacement efficiency `1-2^-delta` rather than by the coarse upper bound `1`.

## 3. One unit of displacement carries at most one half-unit of effective rank mass

For every integer `delta>=1`,

> `1-2^(-delta) <= delta/2`.                              (R42T.8)

Equality occurs only at `delta=1`; for `delta>=2` it is strict.

Summing and using (R42T.3),

`sum_(positive m)(1-2^(-delta_m))`
` <= (1/2) sum_(positive m) delta_m`
` <= rho/2`.                                               (R42T.9)

Combine (R42T.7) and (R42T.9):

> `rho >= 6(z+1)G/z^2`.                                  (R42T.10)

Now use only

`z+1>2`,

`z^2<16/15`.

Then

`6(z+1)/z^2 > 6*2/(16/15)=45/4`.

Therefore

> # **`rho > (45/4)G`.**                                 (R42T.11)

Since `4|G` and `G>0`,

`G>=4`,

so

`rho>45`.

As `rho` is an integer,

> # **`rho>=46`.**                                       (R42T.12)

## 4. Why this is structurally different from the RL39 concentration barrier

RL39's obstruction came from allowing arbitrarily large transport charge to concentrate on one sacrificial high state.  R42T.7 does not price a rank merely by whether it moved.  A displacement of length `delta` contributes only

`1-2^-delta < 1`

to the normalized proper-factor budget, while consuming `delta` units of transport.

Thus long concentrated displacements are intrinsically inefficient, and short displacements have efficiency at most `1/2` per unit of transport.  The exact numerator geometry itself therefore enforces a linear transport cost.

This is a genuine scalable bridge between rank displacement and the proper-factor equation.

## 5. A sharper concentration tradeoff

Equation (R42T.7) is more informative than the coarse floor (R42T.11).  If `P_+` positive ranks have displacements `delta_1,...,delta_(P_+)`, then

`P_+ - sum 2^(-delta_i) >= 3(z+1)G/z^2`.                  (R42T.13)

For `G=4`, the uniform right side is strictly larger than `45/2=22.5`.  Hence

`sum 2^(-delta_i) < P_+ - 22.5`.                          (R42T.14)

This quantitatively separates sparse and dense transport:

- if `P_+=23`, the binary-deficit sum must be below `1/2`, forcing the 23 displacements collectively to be very large;
- if `P_+` is large, there are many genuinely distinct positive moved ranks;
- either way, the dangerous “huge rho on a few ranks at no arithmetic cost” scenario is eliminated.

This is the natural quantity to feed back into the RL35/RL39 packing side.

## 6. Verifier sanity

The companion verifier checks every equal-weight ordered word pair through length 10 and confirms

`sum_pos(1-2^-delta) <= rho/2`

for 250,952 pairs.

On the retained RL21 proper-factor countermodel

`(a,ell,G,P_+,rho)=(65,41,4,39,170)`,

the effective positive-rank mass is exactly

`4571/128 = 35.7109375`,

which exceeds the exact required threshold

`3(z+1)G/z^2 ≈ 23.59125`,

while remaining far below `rho/2=85`, as predicted.

## 7. Next target

The highest-value continuation is no longer another raw low-area enumeration.  Use (R42T.13) as the sparse/dense bridge:

1. optimize the minimum possible transport `rho` for fixed `P_+` under the binary-deficit constraint;
2. combine that tradeoff with the endpoint-loss theorem `P+C >= ell-O(log P)`;
3. reinsert the resulting forced population of moved/high states into the RL39 correction-product support line;
4. test whether the sparse and dense regimes now overlap across the next continued-fraction gate.

The immediate finite corollary can also be strengthened slightly by combining the new `rho>=46` floor with the bounded low-excess crossing certificate, but the main strategic value is the scalable inequality (R42T.7), not the numerical floor alone.

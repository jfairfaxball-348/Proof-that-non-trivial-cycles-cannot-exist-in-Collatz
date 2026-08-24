# RL42 proof status and RL43 attack

Date: 2026-08-22

## Executive status

The current independently rerun frontier in the surviving near-resonant order-2 / `g=2` balanced-return branch is

> **`rho >= 49`.**

This does **not** close RL. It does not close the `g=2` branch. It is a strengthened transport lower bound inside that branch.

The major qualitative advance is that the frontier no longer depends on the lost RL41 area-26/27 transient tables. RL42 replaces them with a much smaller ordered-rank/excursion argument whose retained verifiers rerun from source.

---

## A. Retained analytic structure

### A1. Ordered-rank identity

With `X=2^a`, `Y=3^ell`, `z=X/Y>1`, `z^2<16/15`, common proper factor `G`, and ordered odd positions

`i_1<...<i_ell`, `j_1<...<j_ell`,

the inherited exact relation is

`(X+Y)G = sum_m 3^(ell-m)(2^(i_m)-2^(j_m))`.

For a positive moved rank put `delta_m=i_m-j_m>=1`. Total transport is exactly

`rho = sum_m |i_m-j_m|`.

### A2. Prefix cap and effective moved-rank mass

The RL42 prefix cap gives

`2^(i_m)/3^(m-1) <= z^2`.

Consequently the exact numerator relation yields

`M_eff := sum_(m positive) (1-2^(-delta_m))`

`>= 3(z+1)G/z^2`.

Negative moved ranks can be omitted on the upper side because their terms have the opposite sign.

### A3. Scalable transport-efficiency floor

For every integer `delta>=1`,

`1-2^(-delta) <= delta/2`.

Therefore

`M_eff <= rho/2`,

so

`rho >= 6(z+1)G/z^2 > (45/4)G`.

The inherited endpoint ownership gives `4|G`, hence `G>=4` and

> **`rho >= 46`.**

This part is analytic; the companion verifier is a sanity check, not the proof itself.

### A4. Binary-deficit form

Equivalently,

`P_+ - sum_(m positive) 2^(-delta_m) >= 3(z+1)G/z^2`.

This is the main object to export back into the global packing/concentration argument.

---

## B. Bounded crossing-excess certificate

For a positive excursion `E`, let

- `p_E` = number of moved odd ranks owned by the excursion;
- `r_E` = excursion transport area;
- `e_E=r_E-p_E`.

Then exactly

`e_E = sum_(m in E)(delta_m-1)`.

A nontrivial balanced return has a mandatory physical positive-to-negative sign-changing excursion.

The retained verifier exhausts all canonical positive excursions with `p<=47` and `e<=3` and finds zero physical sign-changing excursions. Therefore, under a hypothetical `rho<=47`, the mandatory crossing must satisfy

`e_cross>=4`.

This is a **bounded exact certificate**, not an asserted infinite classification of all low-excess excursions.

Using

`1-2^-delta <= delta/2 - (delta-1)/4`,

the four mandatory excess units imply

`M_eff <= rho/2 - 1`.

But the numerator bridge and `G>=4` imply

`M_eff > 45/2`.

Hence `rho>47`, so

> **`rho >= 48`.**

---

## C. Exact elimination of rho=48

Assume `rho=48`.

The refined effective-mass inequality forces `P_+>=44`, while the mandatory `e_cross>=4` gives `P<=44`. Thus

`P=P_+=44`, `E:=rho-P=4`.

So:

- every excursion is positive;
- exactly one excursion has excess four and is the physical crossing;
- every other excursion has excess zero;
- the transport theorem forces `G=4`;
- the inherited common-prefix theorem gives initial excursion gap `Delta_0=9`.

The complete retained `e=4`, `p<=44` local scan finds exactly 40 physical crossing types, one for each `p=5,...,44`, all of the form

`1 -> -4`, with `h=p+3` and `D=3^p+4*2^h`.

A safe-superset boundary DP propagating arbitrary `e=0` excursions, exactly one such crossing, and all synchronized-run choices produces 7,791 states and 130 terminal endpoint records. None lies in the required near-resonant window.

Therefore

`rho != 48`,

and together with `rho>=48`,

> **`rho >= 49`.**

This is an exact finite certificate over a rigorously reduced equality case.

---

## D. What is superseded but still retained

RL42 also contains independent smaller certificates establishing `rho>=28` and `rho>=29`. These were valuable during development and still audit local excursion machinery, but the analytic `rho>=46` bridge supersedes them as transport floors.

Do not use the old RL41 missing area-26/27 transient searches as a dependency of `rho>=49`.

---

## E. RL43 immediate attack: rho=49

At `rho=49`, the same excess bookkeeping leaves only

`(P,E)=(45,4), (44,5), (43,6)`.

The refined efficiency threshold gives `P_+>=43`, so there are at most two units of negative moved mass.

Recommended route:

1. classify crossing-capable positive excursions of excess `e=4,5,6` in a representation whose size grows polynomially/parametrically with `p`;
2. isolate exact incoming/outgoing gap families and 2-adic constraints;
3. combine with the explicit excess-zero family;
4. represent the at-most-two negative moved ranks separately rather than exploding the positive catalogue;
5. run a safe-superset boundary DP for each of the three `(P,E)` layers;
6. impose the exact terminal ownership and near-resonant endpoint test;
7. freeze a `rho=49` certificate only after an independent rerun from source.

A previous in-session exploratory observation was that crossing-capable `e=5,6` data appeared sparse. That observation is **not frozen and is not a theorem**; reproduce it before relying on it.

---

## F. Main strategic track: global distortion versus concentration

Avoid allowing the research to degrade into one-area-at-a-time enumeration.

The strongest RL42 scalable bridge is

`P_+ - sum 2^(-delta_m) >= 3(z+1)G/z^2`.

Long displacements consume large transport but asymptotically contribute less than one effective unit; short displacements are numerous. This is the exact arithmetic obstruction to concentrating arbitrary transport on very few ordered ranks for free.

Feed this into the inherited global machinery:

1. optimize minimum transport/excess for fixed `P_+` under the binary-deficit constraint;
2. combine with endpoint-loss `P+C >= ell-O(log P)` (using the exact inherited formulation, not this shorthand, when proving anything);
3. force a population of genuinely distinct moved/high states;
4. reinsert that population into the RL39 correction-product support line;
5. compare against continued-fraction near-resonance gates;
6. seek an overlap of sparse and dense regimes that removes the surviving concentration loophole.

The strategic goal remains a bridge capable of closing the surviving RL branch, not merely a larger numerical lower bound for `rho`.

# RL29 skeptical audit ledger

Date: 2026-08-21

This file deliberately separates inherited proof, newly machine-checked algebra, proposed analytic arguments, and exploratory evidence.

## A. Inherited proof state — retain unless audit finds a dependency failure

From RL21--RL27, with all 20 inherited verifiers freshly reproduced:

- radius 3 is closed under the inherited audited hypotheses/dependencies;
- global supporting-line coefficient:
  `lim R*C_H(R) = 457841/1843200 ~= 0.248394639756944`;
- exact deficit from `1/4`:
  `1/4 - 457841/1843200 = 2959/1843200 ~= 0.00160536024305556`;
- near-resonant cubic numerator upper:
  `Delta < Y[(4/5)e - 3 + 3(2/3)^e]`;
- weak cubic geometry is localized to
  `R == 91 mod288, (G,H)=(12,4)`;
- repaired exact full spread there is
  `Delta = 4(2B+3Y)`;
- forced five-bit block prefixes are
  `11011 / 11101 / 11111`;
- inherited adjacent-block argument gives `e>=37`.

The external computational input `R>=2^71` remains external. Do not relabel it as proved.

## B. New RL29 claims with exact/symbolic machine checks

The script `rl29_additions/verify_rl29_exact_ownership_and_lifts.py` checks:

1. Large-root least-state lifting through the relevant depth forces
   `R == 667 mod4608` after discarding the bounded `R=91` branch.
2. `R=667` itself drops below its starting value, so a genuine survivor in that class has `R>=5275`.
3. The nine-bit prefixes are
   - `u: 110111101`,
   - `v: 111011011`,
   - `w: 111110111`.
4. At synchronized shift `s=6`, the gaps are `(45,14)` and the Eisenstein norm is `1591=37*43`.
5. Root gaps `(12,4)` have norm `112`, coprime to `1591`.
6. The synchronized state sums satisfy a Bezout relation yielding
   `B-Y = 200 A_2 - 207 A_0 - 64 A_6`.
7. The relative Eisenstein gap factors satisfy
   `(-19-11w) alpha_0 + (5+3w) alpha_6 = 1`,
   giving exact bounded extraction of `B w^2 - Y` from `F_0,F_6`.
8. The polynomial comparison used in the proposed `e>=67` argument is positive for all `R>=5275`.

These checks validate arithmetic and finite lifting, not the surrounding analytic implications by themselves.

## C. Proposed analytic statements that RL30 must referee

### C1. Exact absolute and relative ownership

At equal-odd-count synchronized rotation `s`, define rotated balanced numerators

`U_s = B v_s - Y u_s`,
`V_s = B w_s - Y v_s`,
`W_s = B u_s - Y w_s`.

Then

`A_s=U_s+V_s+W_s=(B-Y)(u_s+v_s+w_s)`.

Using `s=0,2,6`, the state-sum gcd is 1, hence proposed theorem:

`gcd(A_0,A_2,A_6)=B-Y`.

For `F_s=U_s+w V_s+w^2 W_s`, one has

`F_s=(B w^2-Y) alpha_s`,
`alpha_s=u_s+w v_s+w^2 w_s`.

The coprime norms at `s=0,6` imply proposed theorem:

`gcd_{Z[w]}(F_0,F_6)=B w^2-Y` up to a unit.

Audit points:
- confirm rotation definitions really preserve the same balanced `(b,e)` block;
- confirm no orientation/indexing mismatch;
- confirm all gcd statements are in the intended ring/ideal sense;
- assess whether this ownership is genuinely useful or merely an exact reformulation with dense numerators.

### C2. Strengthened odd-count floor `e>=67`

At pair synchronization `s=9`, the remaining `u` and `v` tails each have `e-7` odd steps and the correction-product ratio is proposed to be

`K_9(R)=((R+12)(2187R+29143))/((R+4)(2187R+3031))`.

Leastness gives

`K_9(R) < (1+1/(3R))^(e-7)`.

If `e-7<=59`, use

`(1+1/(3R))^59 <= 3R/(3R-59)`

and the exact positive polynomial comparison for `R>=5275` to contradict the displayed `K_9`.

Proposed conclusion: `e>=67`.

Audit points:
- rederive the correction product from first principles;
- verify the direction of the ratio inequality;
- prove the elementary exponential bound with no hidden range issue;
- check whether `R>=5275` is unconditional in the current branch.

### C3. Exact unsynchronized-support identity

For a length-`b`, weight-`e` parity block with prefix odd count `p(j)`, define

`Z = sum_{j=0}^{b-1} 2^j / 3^{p(j)}`.

The proposed universal identity is

`Z = 4Q/Y + B/Y - 1`.

For the three exceptional blocks, put

`q_j=2^j/3^{p_u(j)}`,
`a_j=p_v(j)-p_u(j)`,
`c_j=p_w(j)-p_u(j)`.

Then the proposed relative-mode identity is

`sum_j q_j(1+w 3^{-a_j}+w^2 3^{-c_j})`
` = 4(z w^2-1)(-4+8w)`.

Every triple-synchronized time `(a_j,c_j)=(0,0)` contributes zero exactly.

This is the conceptual statement:

> the relative cubic mode is supported entirely on unsynchronized aligned times.

Audit points:
- prove the universal `Z` identity cleanly;
- check all exponents when `a_j` or `c_j` are negative;
- ensure “supported” is not being overstated: cancellation among unsynchronized terms remains possible.

### C4. Pairwise transport threshold

At a `u/v` pair synchronization `s` with common odd count `p`, let

`r_s=2^s/3^p`, `G_s=v_s-u_s`.

Proposed identity:

`sum_{j<s} q_j(1-3^{-a_j}) = 48 - 4 r_s G_s`.

Thus the first synchronized sign reversal `G_s<0` requires the left side to exceed 48. Since only indices with `a_j>0` contribute positively and

`q_j <= z(R+12)/R`,

46 positive-imbalance indices cannot reach 48 for `R>=5275`, `z<46/45`.

Proposed consequence: at least 47 positive-imbalance aligned times precede the first synchronized `u/v` reversal.

Audit points:
- independently derive the partial identity from prefix numerators;
- verify that negative contributions cannot invalidate the counting direction (they should only make more positive indices necessary);
- check strict versus non-strict inequalities.

### C5. High-state transport and `Omega(e/log e)` theorem

For each trajectory `i`, proposed scaled-state bounds are

`R <= q_i(j) x_i(j) < z(R+12)`.

At an unsynchronized aligned time, the `q_i` differ by a factor at least 3, giving some phase

`> 3R^2/[z(R+12)] > 2.928R`.

At a triple synchronization, if the next `r` parity bits are common, the three distinct states are congruent modulo `2^r`; hence their physical span is at least `2^(r+1)`. The common scaled factor `q` then obeys

`q 2^(r+1) < W`,
where
`W=z(R+12)-R < 23e/90 + 552/45`.

A synchronized run therefore contains at most

`C(e)=ceil(log_2(2.9*(23e/90+552/45)))`

columns at which all three phases can remain below `2.9R`.

If `U` is the number of unsynchronized aligned columns and `H` the number of aligned columns containing a phase above `2.9R`, proposed inequalities are

`H>=U`,
`H>=b-C(e)(U+1)`.

Hence

`H >= (b-C(e))/(C(e)+1) = Omega(e/log e)`
using `b>log_2(3)e`.

Audit points:
- verify the parity-vector/residue-mod-`2^r` implication and the factor `2^(r+1)` for three distinct states;
- verify the synchronized-run indexing carefully (off-by-one risk);
- verify the scaled-state upper bound is valid for every aligned rotation;
- verify the three aligned blocks partition the cycle phases so the high phases are distinct;
- determine whether high **even** phases can be converted into a useful odd-state packing/product gain;
- determine whether `Omega(e/log e)` is quantitatively sufficient anywhere in the current CF/packing chain.

## D. Exploratory evidence only

`rl29_experiments/reproduce_rl29_lift_density_to35.py` reproduces, under the inherited `R>=2^71` floor:

- depth 20: 109 survivors, min unsynchronized count 13;
- depth 25: 794 survivors, min unsynchronized count 14;
- depth 30: 6458 survivors, min unsynchronized count 18;
- depth 35: 43996 survivors, min unsynchronized count 20;
- maximum observed `v2(gcd(G,H))` reaches 5 by depth 35;
- maximum consecutive triple-synchronized run reaches 4 time levels by depth 35.

This supports, but does not prove, positive-density unsynchronization. It also falsifies any naive claim that synchronized gap divisibility stays uniformly tiny.

Earlier session remarks about depths above 35 are intentionally **not** promoted into this release because they were not cleanly reproduced during packaging.

## E. Explicit non-results

Not proved:

- RL;
- exclusion of `R==91 mod288,(G,H)=(12,4)`;
- `Omega(e)` unsynchronized or high phases;
- a positive-density odd-state packing gain;
- applicability of the radius-3 sparse uniqueness theorem to the dense rotated numerators `F_s`;
- that eliminating this one geometry automatically closes the whole global RL theorem (RL30 must audit that implication);
- replacement of the external `R>=2^71` computational input by the new unconditional `R>=5275` local floor.

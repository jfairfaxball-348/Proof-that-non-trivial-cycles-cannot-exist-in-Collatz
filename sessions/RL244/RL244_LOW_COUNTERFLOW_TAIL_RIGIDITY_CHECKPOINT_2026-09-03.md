# RL244 checkpoint — low-counterflow determinant-2 tail rigidity

Date: 2026-09-03

Classification: **`R4_BRIDGE_REDUCED`**.

This continues RL244 from checkpoint commit
`c4553b989f91430647f6bdb5054e24ece3aa308b`.
It is a research checkpoint, not a full authoritative promotion.
`authoritative/START_HERE.md` remains the checksum-clean RL243 -> RL244 kickoff.
Gate A remains open uniformly, Gate B remains open, global non-trivial-cycle
exclusion remains open, and Radius 5 remains inactive.

## 1. Frozen incoming facts and scope

Use the exact RL243/RL244 notation

`P_i = r-W_i^u(q)`, `Q_i=r-W_i^v(q)`, `ar-qell=2`,

with

`Q_i-P_i=h_i-h_(i+q)`.

The full physical half-word is

`u=110 x 1 0^t`, `t=k-3`,

and inherited full-phase ownership gives odd `k>=3`.

Put

`R=2^a/3^ell`, `z=a-ell`.

The exact retained resonance/provenance is

`1<R`, `R^2<16/15`,

and RL243 sharpened its rational consequence to

`19/12<a/ell<8/5`,

hence

`7a/19<z<3a/8`, `ell>=17`.

Also

`gcd(a,q) | ar-qell = 2`,

so

`gcd(a,q) in {1,2}`.

The auxiliary flows `P,Q` are **not** Radius-4 theorem inputs. This checkpoint
uses `P` only to constrain the q-rotation geometry of the genuine physical
half-word `u`.

The previous RL244 checkpoint already removes `beta(P)=0` from the
simultaneously unresolved branch. Here write

`b=beta(P)`

and treat `b in {1,2,3}`.

## 2. Counterflow mass controls q-ordered zero components

Because

`sum_i P_i=2`,

negative mass `b=beta(P)` implies positive mass `b+2`, hence

`||P||_1 = 2b+2`.

For every cyclic real sequence,

`sum_i |P_(i+1)-P_i| <= 2||P||_1`,

so

`TV(P)<=4b+4`.                                           (2.1)

The exact cyclic q-window derivative is

`P_(i+1)-P_i=u_i-u_(i+q)`.                              (2.2)

Therefore `TV(P)` is exactly the number of bit mismatches between `u` and
its q-shift, equivalently the total number of transition edges when `u` is
read around all q-orbits.

A nonconstant cyclic orbit with `c` zero blocks has exactly `2c` transition
edges. In the cases below every q-orbit carrying a terminal tail zero is
nonconstant; an all-zero orbit is impossible because it would already use at
least an entire orbit's worth of zeroes, exceeding the exact zero budget in
the two-orbit case.

Thus the total number `C_q(u)` of q-ordered zero blocks obeys

`2 C_q(u) <= TV(P) <= 4b+4`,

hence

`boxed: C_q(u) <= 2b+2`.                                (2.3)

For `b=1,2,3` this gives respectively

`C_q(u)<=4,6,8`.

This is the structural input for the tail-cover argument.

## 3. Exact cyclic-cover lemma

For marked sites on a cyclic integer circle of length `N`, if their cyclic
successive gap distances are `d_1,...,d_m`, the minimum cardinality of a
union of at most `C<m` cyclic integer intervals covering all marked sites is

`N - (sum of the C largest d_j) + C`.                   (3.1)

Indeed cutting the `C` selected inter-point gaps removes exactly `d_j-1`
empty integer sites from the full circle.

The companion verifier performs the following gap-order calculations with
exact `Fraction` arithmetic. They are finite symbolic audits of the analytic
formulas below, not bounded evidence for the theorem.

## 4. Coprime determinant case: `gcd(a,q)=1`

Let

`s=q^(-1) mod a`.

From `q ell == -2 (mod a)` and `z=a-ell`,

`2s == z (mod a)`.

Since `0<z<a`, exactly one of

`s=z/2`,

`s=(a+z)/2`                                               (4.1)

holds.

Put

`x=z/a`, so `7/19<x<3/8`.

A run of `n` consecutive ordinary terminal zeroes becomes the marked q-order
set

`{0,s,2s,...,(n-1)s}`

up to cyclic translation.

For the three counterflow levels use

| `b` | zero-block cap `C=2b+2` | forced tail zeroes `n` |
|---:|---:|---:|
| 1 | 4 | 11 |
| 2 | 6 | 13 |
| 3 | 8 | 16 |

Applying (3.1), the continuous `a`-coefficient of the minimum cover is the
following affine function of `x`. The table lists both orientations in
(4.1):

| `(n,C)` | `s=z/2` | `s=(a+z)/2` |
|---|---|---|
| `(11,4)` | `5-12x` | `-7/2+(21/2)x` |
| `(13,6)` | `1-(3/2)x` | `-7/2+(21/2)x` |
| `(16,8)` | `-7+20x` | `-4+12x` |

On the whole open corridor `7/19<x<3/8`, every listed affine function is at
least `x`:

- `5-12x-x = 5-13x >= 1/8` at the upper endpoint;
- `-7/2+(21/2)x-x = (-7+19x)/2 >= 0` at the lower endpoint;
- `1-(3/2)x-x = 1-(5/2)x >= 1/16` at the upper endpoint;
- `-7+20x-x = -7+19x >= 0` at the lower endpoint;
- `-4+12x-x = -4+11x >= 1/19` at the lower endpoint.

The discrete `+C` term in (3.1) therefore gives

`minimum zero cover >= ax+C = z+C > z`,

contradicting the exact total number `z` of zeroes in `u`.

Consequently:

- `b=1` is impossible whenever `t>=11`, hence for odd `k>=15`;
- `b=2` is impossible whenever `t>=13`, hence for odd `k>=17`;
- `b=3` is impossible whenever `t>=16`, hence for odd `k>=19`.

Thus in the coprime branch any residual `b<=3` case has respectively

`k<=13,15,17`.                                           (4.2)

## 5. Two-orbit determinant case: `gcd(a,q)=2`

Write

`a=2A`, `q=2Q`.

Then

`Ar-Qell=1`, `gcd(A,Q)=1`.

Put

`delta=ell-A`, `x=delta/A`.

The rational corridor gives

`1/4<x<5/19`,                                             (5.1)

and the exact total number of zeroes is

`z=a-ell=A-delta=A(1-x)`.                               (5.2)

If `s=Q^(-1) mod A`, the determinant identity gives

`s == A-delta == -delta (mod A)`.

The q-action consists of the two parity orbits, each of length `A`. A run
of `n` consecutive ordinary tail zeroes splits into

`ceil(n/2)` and `floor(n/2)`

consecutive reduced positions on those two orbits, with q-order step
`-delta mod A`.

For the same three counterflow levels use

| `b` | total zero-block cap `C` | forced tail zeroes `n` |
|---:|---:|---:|
| 1 | 4 | 7 |
| 2 | 6 | 17 |
| 3 | 8 | 24 |

Both parity orbits contain a forced tail zero. Neither can be all zero,
because one all-zero parity orbit would contribute `A>z` zeroes. Hence each
uses at least one zero block. Allowing exactly `C` total blocks can only
make the minimum cover smaller, so it is enough to audit every allocation
`c_1+c_2=C`, `c_1,c_2>=1`.

### 5.1 `b=1`, `C=4`, `n=7`

For all allocations `1+3`, `2+2`, `3+1`, the exact two-orbit cover is at
least

`A(1-x)+4 = A-delta+4 = z+4`,

impossible.

Thus `b=1` is impossible for `t>=7`, hence for odd `k>=11`.

### 5.2 `b=2`, `C=6`, `n=17`

Across the five allocations, the exact continuous cover coefficients are

`-3+15x`, `-4+19x`, `-5+22x`, `-5+22x`, `-6+26x`.

Throughout (5.1), each is at least

`-5+22x`.

Therefore the total zero cover is at least

`-5A+22delta+6`.                                         (5.3)

If this failed to exceed the available zero budget `z=A-delta`, then

`23delta+6 <= 6A`,

hence, using `A=a/2` and `delta=ell-A`,

`29a-46ell >= 12`.                                      (5.4)

But the exact integer comparison

`2^46 > 3^29`

then gives

`R^46 = 2^(46a)/3^(46ell) > 3^(29a-46ell) >= 3^12`,

so

`R^2 > 9^(6/23)`.

The exact comparison

`16^23 < 15^23 * 9^6`

is equivalent to

`16/15 < 9^(6/23)`.

This contradicts the frozen resonance `R^2<16/15`.

Hence (5.3) is strictly larger than `z`, and `b=2` is impossible for
`t>=17`, hence for odd `k>=21`.

### 5.3 `b=3`, `C=8`, `n=24`

Across the seven allocations, the exact continuous cover coefficients are

`-6+27x`, `-9+38x`, `-12+49x`, `-16+64x`,
`-12+49x`, `-9+38x`, `-6+27x`.

Throughout (5.1), each is at least

`-16+64x`.

Thus the total zero cover is at least

`-16A+64delta+8`.                                        (5.5)

If this failed to exceed `z=A-delta`, then

`65delta+8 <= 17A`,

and therefore

`41a-65ell >= 8`.                                       (5.6)

The exact comparison

`2^65 > 3^41`

would imply

`R^65 > 3^8`,

hence

`R^2 > 9^(8/65)`.

But

`16^65 < 15^65 * 9^8`

is exactly

`16/15 < 9^(8/65)`,

again contradicting `R^2<16/15`.

Therefore `b=3` is impossible for `t>=24`, hence for odd `k>=27`.

The two-orbit residual bounds are therefore

- `b=1 => k<=9`;
- `b=2 => k<=19`;
- `b=3 => k<=25`.                                      (5.7)

## 6. Low-counterflow tail-rigidity theorem

Combining (4.2) and (5.7):

### Theorem RL244.LC

For a retained determinant-2 full-phase object satisfying the RL243
resonance:

- if `beta(P)=1`, then `k<=13`;
- if `beta(P)=2`, then `k<=19`;
- if `beta(P)=3`, then `k<=25`.

The branch-sensitive sharper bounds are those in (4.2) and (5.7).

This theorem is analytic. It uses the auxiliary flow only through the exact
q-window derivative and transition count; it does not apply Radius 4 to
`P` or `Q`.

## 7. Routing the finite residual range through frozen Gate-A authority

This section does **not** claim a new uniform Gate-A theorem.

Suppose a `beta(P) in {1,2,3}` object were still a simultaneous Gate-A/Gate-B
survivor. Gate-A failure would require

`H<k`.

Theorem RL244.LC gives `k<=25`, hence

`H<=24`.

The inherited exact RL45 quotient certificate, frozen in RL62/RL64, exhausts
this finite area range with two independent C++ implementations and proves
no violation of

`v2(J)<=H`

for `H<=24`.

At a genuine full-phase terminal state,

`J=2^k`.

Thus a hypothetical `H<k` would give

`v2(J)=k>H`,

which is exactly a forbidden certificate violation.

Therefore none of `beta(P)=1,2,3` can remain a simultaneous unresolved
RL244 branch.

The expensive historical H<=24 computation is **not rerun** here, in
accordance with verification economy; only its checksum-clean frozen result
is used in its exact finite scope.

## 8. Combined RL244 obstruction

The previous checkpoint proves that `beta(P)=0` cannot remain simultaneous
unresolved. The new theorem and finite routing eliminate `beta(P)=1,2,3`.

Hence every simultaneous unresolved RL244 survivor must satisfy

`boxed: beta(P)>=4`.                                    (8.1)

Every negative `P_i` is inherited at the same u-half index by both genuine
determinant-4 physical flows through the exact RL243 envelope

`{A_i,B_i}={P_i,P_i-h_(i+q)}`.

So the live obstruction is no longer merely the existence of a same-index
double physical valley. It carries at least **four units of total intrinsic
negative determinant-2 half-flow mass** before the ownership charge
`Q-P=h-h_shift` is added.

This is a strict reduction of the live bridge target. It is not Gate-B
closure, not global Radius-4 application, and not a proof of non-trivial-cycle
exclusion.

## 9. Verification

The portable verifier

`sessions/RL244/verification/verify_rl244_low_counterflow_tail_rigidity.py`

uses exact `Fraction` arithmetic to audit:

1. the six one-orbit affine cyclic-cover formulas in Section 4;
2. every two-orbit block allocation used in Section 5;
3. the four exact power comparisons used to combine the two-orbit cover
   bounds with the frozen `R^2<16/15` resonance.

Fresh output:

`RL244 low-counterflow tail-rigidity verifier: PASS`

`gcd1_piece_checks= 6`

`gcd2_piece_checks= 15`

`gcd2_formula_counts= [(7, 4, 3), (17, 6, 5), (24, 8, 7)]`

`exact_power_comparisons=4`

`classification=R4_BRIDGE_REDUCED`

The frozen RL243 portable verifier was also rerun before this checkpoint and
passed with its original counts:

- cyclic interval checks: `1495`;
- small-word flow checks: `1711`;
- entry-crossing checks: `5103`.

## 10. Mandatory red-team ledger

Still forbidden:

- treating `P,Q` as Radius-4 theorem inputs;
- inferring an exact-distance-4 encounter merely from large negative mass;
- generic physical-scale anti-concentration;
- generic packing/product/continued-fraction closure;
- a bare radius-shell principle;
- RL43/RL19 parameter transplantation;
- blanket half-prefix determinant positivity;
- relabelling the H<=24 certificate as uniform Gate A;
- Radius 5.

The `(65,41)` missing-full-phase rejection remains preserved.

## 11. Next live target

Classification remains **`R4_BRIDGE_REDUCED`**.

The unique combined survivor is now

`beta(P)>=4`.

The next attack should exploit the fact that this is not four arbitrary units
of abstract counterflow: every negative unit of `P` is inherited by **both**
genuine determinant-4 physical rotations at the same canonical u-half root.
The target is to couple this deeper same-index physical-valley mass to the
actual zero-carry physical states and the ordered RL64-RL69 `d,T,H,J` / rank
recurrence, seeking either:

1. an eligible primitive full-`D` exact-distance-4 self-rotation satisfying
   every RL238/RL239 hypothesis; or
2. an exact contradiction to genuine full phase.

No authoritative closeout is performed at this checkpoint.

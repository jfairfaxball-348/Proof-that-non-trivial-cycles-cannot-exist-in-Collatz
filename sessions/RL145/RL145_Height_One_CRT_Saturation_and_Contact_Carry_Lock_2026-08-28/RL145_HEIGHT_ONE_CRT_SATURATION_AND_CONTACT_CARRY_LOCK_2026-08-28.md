# RL145 — height-one CRT saturation barrier and ordinary-owned contact-carry lock

Date: 2026-08-28

## 0. Outcome and classification

RL145 continues from the repaired RL144 state. It does **not** restore the retracted RL143 interval theorem and does **not** exclude a multiplicity.

The session obtains four promoted results:

1. **RL145.1 — exact height-one exponent/run population identity.**
   If `n_r=#{j:a_j=r}` in a height-one profile, then
   `n_1 = g(2L-A)+n_3`.
   Here `n_1=O_2` is the two-odd-window population and `n_3` is exactly the
   number of two-zero ordinary runs.
2. **RL145.2 — exact parity split of the two-odd endpoints.**
   The `O_2` endpoints split into `C_2` terminal even endpoints in one class
   modulo 18 and `C_3+C_4` continuing odd endpoints in the other class modulo
   18. This repairs the endpoint semantics without merging residue classes.
3. **RL145.3 — mechanical saturation barrier.**
   At multiplicity `g=13` there exists an explicit valid height-one local
   defect construction with no `a=3` edges and
   `(C_2,C_3,C_4)=(9q,3q,q)`, `q=2L-A`.
   For that mechanically admissible population, all inherited one-fibre,
   parity-split, and depth-1 boundary floors have maximum
   `162q-18`, asymptotically the same effective coefficient `162/13`.
   Therefore the missing approximately 11.58% cannot be forced by local
   height-one mechanics plus the existing run-population/CRT floors alone.
   This is a **method barrier**, not a cycle construction.
4. **RL145.4 — ordinary-owned rotated contact-carry and endpoint valuation
   lock.**
   For a hypothetical primitive height-one ordinary cycle, the RL140 contact
   polynomial at every block rotation has an integer quotient `n_t`.
   These quotients satisfy an exact integer carry recurrence. A primitive
   owner can have no equal adjacent reduced-block contact sets. At every
   adjacent block interface the first changed contact residue is at most 22
   and the last changed residue is at least `L-23`. Consecutive interfaces are
   coupled by an exact finite 2-adic/3-adic valuation budget.

The new carry theorem is genuinely ordinary-owned and strengthens the
RL140--RL142 scattered-support route. It does not yet give the positive-density
physical width gain needed to close a multiplicity interval.

No Gate A or Gate B status changes. Global nontrivial-cycle exclusion and
Collatz remain open.

---

## 1. Incoming authority

Use the frozen RL144 repair.

The first reduced above-side survivor remains

`(A,L)=(217,976,794,617,137,528,045,312)`.

Put

`P=A-L=80,448,749,305`,
`K=2L-A=57,079,296,007`.

The inherited one-defect multiplicity range remains

`1 <= g <= 771,316,334,039`.

RL144 supplies:

- height-one ordinary odd runs have length at most four;
- `W >= (162/13)(gK-3)`;
- the corrected floor does not contradict the favorable carried upper-width
  estimate anywhere in the inherited range;
- the RL143 equation `C_(2,1)=O_2` is retracted.

RL122/RL123, RL137, and RL139--RL142 remain authoritative exactly as inherited.

---

## 2. RL145.1 — exact height-one exponent/run population identity

Let the full accelerated exponent profile have length

`N=gL`

and, in the height-one branch,

`a_j=c_j+h_j-h_(j+1)`,
`c_j in {1,2}`,
`h_j in {0,1}`.

Thus every valid accelerated exponent is in `{1,2,3}`.

Let

`n_r=#{j:a_j=r}`, `r=1,2,3`.

Then

`n_1+n_2+n_3=gL`,                                      (2.1)

while the total exponent sum gives

`n_1+2n_2+3n_3=gA`.                                    (2.2)

Subtracting (2.1),

`n_2+2n_3=g(A-L)=gP`.                                  (2.3)

Eliminating `n_2` gives

### Theorem RL145.1

`n_1 = g(2L-A)+n_3 = gK+n_3`.                           (2.4)

In ordinary shortcut language, `a_j=1` means the next shortcut state is odd,
so

`n_1=O_2`.

Also `a_j=3` means that after the odd step there are exactly two ordinary even
steps before the next odd state. Hence `n_3` is exactly the number of ordinary
zero runs of length two in the height-one branch. In particular,

`O_2 >= gK`,                                             (2.5)

with equality exactly when all positive zero runs have length one.

Classification: **analytic structural identity**. It is not an ownership
claim.

---

## 3. RL145.2 — parity split of the two-odd endpoints

Write the ordinary odd-run tail counts, using RL144's run-length bound, as

`C_r=#{odd runs of length at least r}`, `r=2,3,4`.

Then

`O_2=C_2+C_3+C_4`.                                      (3.1)

RL122 places every endpoint of two consecutive odd shortcut steps in the
single residue class

`x == -1 (mod 9)`.

Those endpoints split physically into two disjoint parity classes.

- The terminal endpoint of each odd run of length at least two is followed by
  an even shortcut step. It is even, so it lies in the unique class

  `x == 8 (mod 18)`,

  and there are `C_2` such states.
- Every remaining two-odd endpoint is still inside an odd run. It is odd, so
  it lies in the unique class

  `x == 17 (mod 18)`,

  and there are

  `O_2-C_2=C_3+C_4`

  such states.

Therefore, for a hypothetical primitive ordinary cycle,

### Theorem RL145.2

`W >= 18(C_2-1)`,                                       (3.2)

`W >= 18(C_3+C_4-1)`.                                   (3.3)

The first is the valid depth-2 terminal boundary fibre already used in
RL144. The second is the previously separated continuing-endpoint fibre. It
must **not** be merged with (3.2) into one mod-18 population.

For reference, the inherited deeper odd-window and boundary floors remain

`W >= 27(C_3+C_4-1)`,                                   (3.4)

`W >= 54(C_3-1)`,                                       (3.5)

`W >= 81(C_4-1)`,                                       (3.6)

`W >= 162(C_4-1)`.                                      (3.7)

Classification: **analytic ordinary-owned physical fibre theorem** for a
hypothetical primitive cycle.

---

## 4. RL145.3 — exact mechanical saturation construction

This section proves a method barrier: the local height-one mechanics can
realize the population ratio that saturates the repaired convex-combination
coefficient.

Put

`u_j=c_j-1 in {0,1}`.

Over one reduced period the number of `u=1` positions is `P=A-L`, and the
number of `u=0` positions is `K=2L-A`.

The exact inequalities

`2A>3L`,
`3A<5L`

give

`1/2 < P/L < 2/3`.                                      (4.1)

Hence the cyclic mechanical word `u` has no consecutive zeros, and the runs
of ones between successive zeros have length one or two.

Let

`s = # one-gaps = 5L-3A = 33,709,842,709`,
`d = # two-gaps = 2A-3L = 23,369,453,298`.              (4.2)

Indeed,

`s+d=K`,
`s+2d=P`.                                                (4.3)

### 4.1 Local excursion tiles

Start from `h=0`, so every mechanical zero edge `u=0` is an isolated `a=1`
edge.

Two disjoint local modifications preserve height one, validity, and the total
number of `a=1` edges.

**Length-2 tile.**
Take two consecutive mechanical zero edges. Stay at height zero across the
first zero, rise `0->1` on the first intervening `u=1` edge, stay at height one
through a possible second `u=1`, and fall `1->0` on the second zero edge.
The two baseline isolated `a=1` edges become one run of two consecutive
`a=1` edges.

**Length-3 tile.**
Take three consecutive mechanical zero edges for which the first inter-zero
one-run has length one. Stay at height zero across the first zero, rise on the
unique following `u=1`, stay at height one across the second zero, remain at
height one through the following one-run, and fall on the third zero.
The three baseline isolated `a=1` edges become one run of three consecutive
`a=1` edges.

All falls occur on `u=0`, so these tiles create no `a=3` edge.

### 4.2 Exact packing at `g=13`

Take

`g=13`,
`q=K`.

There are

`13q`

mechanical zero edges and

`13s`

eligible single-one gaps.

A selected length-3 tile occupies three consecutive zero positions. In the
cyclic zero-index, choosing one such tile can invalidate at most five eligible
starts. The exact inequality

`13s = 438,227,955,217 > 5q = 285,396,480,035`           (4.4)

therefore guarantees `q` disjoint length-3 tiles by a greedy packing.

After removing their `3q` zero positions, `10q` zero positions remain in at
most `q` path components. These components contain at least

`(10q-q)/2 > 2q`

pairwise disjoint adjacent zero pairs. Choose `2q` of them as length-2 tiles.

The remaining zero positions number

`13q-3q-4q=6q`.

Thus the consecutive-`a=1` run counts are exactly

- `6q` runs of length 1;
- `2q` runs of length 2;
- `q` runs of length 3.

Equivalently, the ordinary odd-run tail counts are

### Theorem RL145.3

`C_2=9q`,
`C_3=3q`,
`C_4=q`,                                                  (4.5)

with

`O_2=C_2+C_3+C_4=13q=gK`,                               (4.6)

and `n_3=0`.

The number of ordinary odd runs is

`t=g(A-L)=13P`,

and the number of odd runs of length one is

`t-C_2=532,120,076,902>0`.

The total odd population is exactly `gL`.

### 4.3 Fibre-floor saturation

For this mechanically admissible population, the inherited and repaired
run-fibre floors evaluate to

- `3(gL-1) = 5,363,593,767,165` for the depth-1 odd fibre;
- `9(O_2-1) = 6,678,277,632,810`;
- `18(C_2-1) = 9,246,845,953,116`;
- `18(C_3+C_4-1) = 4,109,709,312,486`;
- `27(C_3+C_4-1) = 6,164,563,968,729`;
- `54(C_3-1) = 9,246,845,953,080`;
- `81(C_4-1) = 4,623,422,976,486`;
- `162(C_4-1) = 9,246,845,952,972`;
- `6(t-1) = 6,275,002,445,784`;
- the depth-1 zero fibre is smaller still.

The maximum is

`18(C_2-1)=162q-18`.                                    (4.7)

Dividing by `O_2=13q` gives a coefficient strictly below, and tending to,

`162/13 = 12.461538...`.                                (4.8)

Therefore the requested approximately 11.58% increase to about `13.9043`
cannot be obtained from the existing run/window/CRT population floors plus
local height-one mechanical restrictions alone.

The construction is **not** asserted to satisfy the ordinary affine ownership
condition `D|Q`, and is not a cycle. Its role is precisely to show which
additional ingredient is missing: a genuinely global ordinary-owned
discriminator.

Classification: **analytic mechanical method barrier**.

---

## 5. RL145.4 — ordinary-owned rotated contact-carry theorem

Retain the RL140 notation

`X=2^A`,
`Y=3^L`,
`F_g=sum_(i=0)^(g-1) X^i Y^(g-1-i)`,

`W_r=3^(L-1-r)2^(floor(Ar/L))`,

`Q_0=sum_(r=0)^(L-1) W_r`.

For reduced block `t`, let

`C_t={r:h_(tL+r)=0}`,
`c_t=C(C_t)=sum_(r in C_t) W_r`.

RL140 proves the necessary ownership divisibility for one anchor. RL142's
block-boundary re-anchoring proves the same `F_g` divisibility at every cyclic
block rotation, including the shifted `{-1,0}` normalization when the cut is
made at height one.

Define

`S_t=sum_(i=0)^(g-1) X^i Y^(g-1-i) c_(t+i)`              (5.1)

with block indices modulo `g`.

For a hypothetical actual height-one owner,

`F_g | S_t`

for every `t`. Define the integer quotient

`n_t=S_t/F_g`.                                           (5.2)

Because every coefficient in (5.1) is positive,

`min_i c_i <= n_t <= max_i c_i`,                         (5.3)

and in particular

`0 <= n_t <= Q_0`.                                       (5.4)

A direct shift computation gives

`X S_(t+1)-Y S_t=(X^g-Y^g)c_t=(X-Y)F_g c_t`.             (5.5)

Dividing by `F_g`,

`X n_(t+1)-Y n_t=(X-Y)c_t`.                              (5.6)

Since `gcd(X,Y)=1`, there is an integer `d_t` such that

### Theorem RL145.4a — contact carry

`n_t-c_t = X d_t`,                                       (5.7)

`n_(t+1)-c_t = Y d_t`.                                   (5.8)

Consequently,

`n_(t+1)-n_t = -(X-Y)d_t`,                               (5.9)

`c_(t+1)-c_t = Y d_t-X d_(t+1)`,                         (5.10)

and cyclic summation gives

`sum_t d_t=0`.                                           (5.11)

RL140's inherited bound

`Q_0 < LX/3`

and (5.4) imply the small-carry bound

`|d_t| < L/3 = 45,842,681,770.666...`.                   (5.12)

This recurrence is a new ordinary-owned global constraint. It is not a
restatement of a local defect recurrence.

### 5.1 No equal adjacent contact blocks in a primitive owner

Suppose `c_(t+1)=c_t`. Then (5.10) gives

`Y d_t=X d_(t+1)`.

Because `gcd(X,Y)=1` and (5.12) is far smaller than either `X` or `Y`, this
forces

`d_t=d_(t+1)=0`.

Now (5.10) at the next interface says that a nonzero
`c_(t+2)-c_(t+1)` would be divisible by `X`. But any nonzero difference of two
contact subset weights has 2-adic valuation

`floor(Ar/L) <= A-2 < A`

at its least changed residue, so it cannot be divisible by `X=2^A`.
Therefore the equality propagates around the cycle.

Hence an equal adjacent pair forces

`C_0=C_1=...=C_(g-1)`.                                   (5.13)

Distinct contact subsets have distinct weights by RL140. A block-periodic
height-one exponent profile cannot represent a primitive full-count cycle with
`g>1`: the repeated reduced affine block is a contraction and a fixed point of
its `g`-th iterate is already its one-block fixed point.

### Corollary RL145.4b

For every hypothetical primitive height-one owner with `g>1`,

`C_(t+1) != C_t`

for every cyclic block interface.                        (5.14)

This strictly extends the RL140--RL142 bounded-interface exclusions: arbitrary
scattered support is still possible, but it must change at **every** adjacent
reduced-block boundary.

---

## 6. Endpoint valuation lock

Fix an interface and put

`delta_t=c_(t+1)-c_t != 0`.

Let

`r_t=min(C_t triangle C_(t+1))`,
`s_t=max(C_t triangle C_(t+1))`.

Because the weights have strictly increasing 2-adic valuations,

`v_2(delta_t)=floor(A r_t/L)`.                            (6.1)

Because they have strictly decreasing 3-adic valuations,

`v_3(delta_t)=L-1-s_t`.                                  (6.2)

Equation (5.10) and the small-carry bound separate the endpoint valuations.

For the 2-adic side, `Y d_t` has valuation `v_2(d_t)<36`, whereas
`X d_(t+1)` is divisible by `2^A`. Hence

`v_2(d_t)=floor(A r_t/L)`.                               (6.3)

The exact checks

`2^35 < L/3 < 2^36`,
`floor(22A/L)=34`,
`floor(23A/L)=36`

give

### Theorem RL145.4c — first-change lock

`r_t <= 22`.                                             (6.4)

For the 3-adic side, `Y d_t` is divisible by `3^L`, whereas
`v_3(d_(t+1))<=22` because

`3^22 < L/3 < 3^23`.

Therefore

`v_3(d_(t+1))=L-1-s_t <=22`,                             (6.5)

so

### Theorem RL145.4d — last-change lock

`s_t >= L-23 = 137,528,045,289`.                         (6.6)

Thus every adjacent pair of reduced blocks in a primitive height-one owner
must differ both inside the first 23 contact residues and inside the last 23
contact residues.

There is also a cross-interface coupling. The same carry `d_t` satisfies

`v_2(d_t)=floor(A r_t/L)`

from the outgoing interface and

`v_3(d_t)=L-1-s_(t-1)`

from the incoming interface. Hence

### Theorem RL145.4e — cross-interface valuation budget

`2^(floor(A r_t/L)) 3^(L-1-s_(t-1)) < L/3`.             (6.7)

The exact finite frontier is:

| `r_t` | `floor(A r_t/L)` | max `L-1-s_(t-1)` |
|---:|---:|---:|
|0|0|22|
|1|1|21|
|2|3|20|
|3|4|19|
|4|6|18|
|5|7|17|
|6|9|16|
|7|11|15|
|8|12|14|
|9|14|13|
|10|15|12|
|11|17|11|
|12|19|10|
|13|20|9|
|14|22|8|
|15|23|7|
|16|25|6|
|17|26|5|
|18|28|4|
|19|30|3|
|20|31|2|
|21|33|1|
|22|34|0|

Classification: **analytic ordinary-owned theorem + exact finite arithmetic
frontier**.

---

## 7. Red teams

### Population semantics — PASS

`O_2`, `C_2`, `C_3`, and `C_4` remain distinct. The mod-18 parity split is
applied to two separate physical residue classes and is never merged into the
retracted RL143 identity.

### RL20 / full ownership — PASS

The mechanical saturation construction is explicitly classified as a method
barrier and not as a cycle. The contact-carry theorem is invoked only under
actual ordinary full ownership and uses the inherited RL140/RL142
divisibility.

### RL79 generalized increment — PASS

No generalized-increment normalization is used to cancel the ordinary affine
increment. The carry theorem descends from the ordinary affine numerator.

### RL81 physical versus quotient — PASS

Physical CRT spacing is applied only to actual hypothetical cycle states.
The quotient variables `n_t,d_t` are not called physical states.

### Verification economy — PASS

No historical expensive certificate is rerun. Only the live RL144/RL140--142
dependencies and exact small arithmetic consequences are checked.

---

## 8. Correction/demotion ledger

No new inherited theorem is demoted in RL145.

The RL144 correction remains authoritative:

- RL143 height-one interval exclusion:
  **DEMOTED / RETRACTED**;
- do not use `C_(2,1)=O_2`;
- use the repaired lower floor
  `W >= (162/13)(gK-3)` unless a stronger valid ordinary-owned theorem is
  separately proved.

RL145 adds a method barrier showing why the repaired coefficient cannot be
raised by local mechanical/run-population refinement alone.

---

## 9. Open frontier and next target

Still open:

- arbitrary primitive height-one owners;
- turning the RL145 contact-carry/endpoint lock into a positive-density
  physical packing or a direct ownership contradiction;
- mixed-height nonnegative profiles;
- negative-defect profiles outside the already isolated ranges;
- lower multiplicities and full multiplicity exclusion;
- Gate A and Gate B globally;
- global nontrivial-cycle exclusion;
- Collatz.

RL146 should attack the new integer carry system

`c_(t+1)-c_t = Y d_t-X d_(t+1)`,
`sum d_t=0`,
`0<|d_t|<L/3`

together with the endpoint valuation lock. The preferred goal is either:

1. prove that no cyclic contact sequence arising from a valid height-one path
   can satisfy the carry system under primitive ownership; or
2. prove a positive-density physical consequence strong enough to exceed the
   required width coefficient.

If that global carry route reaches a rigorous barrier without a coefficient
gain, pivot immediately back to the inherited mixed-height and negative-defect
targets rather than spending further sessions on local height-one
run-population refinements.

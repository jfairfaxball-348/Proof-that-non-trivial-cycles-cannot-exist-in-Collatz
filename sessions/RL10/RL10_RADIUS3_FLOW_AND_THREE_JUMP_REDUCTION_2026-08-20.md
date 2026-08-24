# Collatz R# RL-10 — Radius-3 Flow Classification, Connected Closure, and the Three-Jump Reduction

**Date:** 2026-08-20  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-9  
**Verdict:** **RL remains open. Radius 3 is not yet completely closed analytically.** RL-10 proves the exact geometry of every radius-3 cyclic transposition, closes the entire connected three-edge branch, and converts the remaining coprime branches into sparse three-jump congruences for `Q` itself. A constructive exact scan through `A<=40` finds only the nonprimitive threefold repetition of the trivial `10` cycle as a `D`-divisible radius-3 survivor.

---

## 1. Inherited state

RL-9 proved that if a primitive parity word `d` has

`D = 2^A - 3^L > 1`,

and `D | Q(d)`, then no distinct rotation of `d` is at cyclic adjacent-transposition distance `1` or `2` from `d`.

Thus every distinct rotation of a primitive hypothetical cycle word has transposition distance at least `3`.

The next Rank-1 target was radius `3`. The exact position-sum invariant already gives

`S(tau^m d)-S(d)=A P_m-mL`,

so a length-three path has discrepancy

- `+/-3` if all three elementary moves have one direction;
- `+/-1` if two moves have one direction and one has the other.

RL-10 first classifies the geometry before doing any denominator arithmetic.

---

## 2. RL-L62 — every exact radius-3 path has three unit-flow edges

Let `d,d'` be binary words with the same length and number of ones. Choose a cut at an unused cyclic edge of a shortest cyclic transposition path; for an exact distance-three path such an unused edge always exists. Work linearly across that cut.

For prefix length `i`, define

`G_i = #(ones in d'[1..i]) - #(ones in d[1..i])`,

with `G_0=G_A=0`.

The standard one-dimensional transport identity gives

`dist_transp(d,d') = sum_(i=1)^(A-1) |G_i|`.                 (R62.1)

If this distance is exactly `3`, then no `|G_i|` can exceed `1`. Indeed, reaching level `+/-2` from `0` and returning to `0` requires at least the edge-level pattern

`1,2,1`,

whose absolute mass is already `4`.

Therefore:

- every nonzero `G_i` is `+1` or `-1`;
- exactly three internal edges have nonzero flow;
- adjacent nonzero flow edges have the same sign, because `G` cannot jump directly from `+1` to `-1` or conversely.

Hence the support is a union of constant-sign runs whose lengths partition `3`:

`[3]`, `[2,1]`, or `[1,1,1]`.                                (R62.2)

A run of length `r` has the exact local endpoint form

`1 M 0  ->  0 M 1`                                           (R62.3)

or its reverse, where `M` is the unchanged binary middle word of length `r-1`.

Thus a connected run is literally one `1` transported across `r` adjacent edges; disconnected paths are disjoint unions of such transports.

### 2.1 Exact connected coefficients

For a run beginning at position `a`, with `b` ones to the right of the run, its `Q` change is an outside unit `2^a 3^b` times a small local coefficient.

At length three the four right-moving possibilities are

`1000 -> 0001` : coefficient `7`,

`1010 -> 0011` : coefficient `13`,

`1100 -> 0101` : coefficient `9`,

`1110 -> 0111` : coefficient `19`.                            (R62.4)

The reverse moves have the negatives of these values.

At run length two the analogous coefficients are `3` and `5`; at run length one the coefficient is `1`.

**Status: PROVED ANALYTIC THEOREM.**

---

## 3. RL-L63 — the connected radius-3 branch is impossible

Assume now that

`d' = tau^m d`

is a distinct rotation and that both endpoints are `D`-divisible. Rotation invariance from RL-L52 gives this automatically if `D|Q(d)`.

If the radius-three flow is connected, (R62.4) gives

`D | c`,

where

`c in {7,9,13,19}`,

because the outside factor is a `2,3`-unit modulo `D`.

Since `gcd(D,6)=1`, `c=9` is immediately impossible. Three exceptional primes remain.

### 3.1 The coefficient `7`

Here `D=7`.

Since `A>=3`, reduction modulo `8` gives

`3^L == 1 (mod 8)`,

so `L` is even. Reduction modulo `3` gives

`2^A == 1 (mod 3)`,

so `A` is even.

Thus `gcd(A,L)` is even.

But a connected three-edge run has position-sum discrepancy `+/-3`, so

`gcd(A,L) | 3`.                                               (R63.1)

Contradiction.

### 3.2 The coefficient `19`

Here `D=19`. Positivity forces `A>=5`, so modulo `32`,

`3^L == -19 == 13 (mod 32)`.                                 (R63.2)

The powers of `3` modulo `32` are

`1,3,9,27,17,19,25,11`,

and never `13`. Contradiction.

### 3.3 The coefficient `13`

Here the right-moving local factor is

`1010 -> 0011`.                                               (R63.3)

The endpoint difference has only two nonzero vertex defects, separated by three natural positions. Telescoping on the rotation orbits therefore gives

`H = gcd(A,m) | 3`.                                           (R63.4)

We first show `H!=1`.

Assume `H=1` and orient the defects so the negative defect is at natural position `0` and the positive defect at position `3`. Put

`a = m^(-1) mod A`,

and let

`q = 3a mod A`, `1<=q<=A-1`.                                 (R63.5)

Along the single `m`-orbit, the bit drops from `1` to `0` at the first defect and rises from `0` to `1` at the second. Therefore the zero-set in orbit coordinates is exactly

`1,2,...,q`,

so

`q=A-L`.                                                      (R63.6)

The local word `1010` requires

- natural position `1` to be zero, hence `a<=q`;
- natural position `2` to be one, hence `2a mod A` not in `[1,q]`.

Write

`3a = rA+q`, `r in {0,1,2}`.                                 (R63.7)

- If `r=0`, then `q=3a`, so `2a<=q`, forcing position `2` to be zero.
- If `r=1`, the condition `a<=q=3a-A` gives `a>=A/2`; then `2a-A` is the residue of `2a` and satisfies `0<2a-A<q`, again forcing position `2` to be zero.
- If `r=2`, `a<=q=3a-2A` would imply `a>=A`, impossible.

Thus coefficient `13` cannot occur with `H=1`, so

`gcd(A,m)=3`.                                                 (R63.8)

Now `3|A`. Since `D=13`, modulo `3` also forces `A` even, hence `6|A`.

Modulo `13`,

`2^A == 3^L`.                                                 (R63.9)

The order of `2` modulo `13` is `12`, while the order of `3` is `3`. Since `A` is a multiple of `6`, `2^A` is `+/-1`. It cannot be `-1`, because a power of `3` modulo `13` lies in `{1,3,9}`. Therefore

`12|A`, `3|L`.                                                (R63.10)

The position-sum discrepancy still gives `gcd(A,L)|3`, so in fact

`gcd(A,L)=3`.                                                 (R63.11)

Write

`A=3a`, `L=3 ell`,

`X=2^a`, `Y=3^ell`.

Then `X>Y` and

`13 = X^3-Y^3`

`   = (X-Y)(X^2+XY+Y^2)`.                                    (R63.12)

Because `13` is prime and the second factor exceeds `1`, necessarily

`X-Y=1`,

`X^2+XY+Y^2=13`.                                             (R63.13)

Putting `X=Y+1` gives

`3Y^2+3Y+1=13`,

or

`Y(Y+1)=4`,

which has no positive integer solution.

Hence coefficient `13` is also impossible.

Therefore:

> **RL-L63. No `D`-divisible self-rotation can have connected radius-3 transposition flow.**

This statement is analytic and infinite.

**Status: PROVED ANALYTIC THEOREM.**

---

## 4. Arithmetic shapes left by the disconnected cases

RL-L62 leaves only `[2,1]` and `[1,1,1]` support.

### 4.1 A `[2,1]` path is a coefficient-binomial resonance

The length-two component has local coefficient `3` or `5`; the isolated edge has coefficient `1`.

After stripping a common `2,3`-unit, the endpoint difference has the form

`c_L 3^v +/- c_R 2^u`,                                       (R64.1)

where one of `c_L,c_R` is `1` and the other is `3` or `5`.

If the nontrivial coefficient is `3`, the factor `3` can be absorbed into the exponent, leaving an ordinary binomial resonance

`2^u +/- 3^v`.                                                (R64.2)

The genuinely new binomial branch is therefore the coefficient-`5` form

`2^u +/- 5*3^v`,

or equivalently

`5*2^u +/- 3^v`.                                              (R64.3)

### 4.2 A `[1,1,1]` path is a proper trinomial resonance

If the three isolated edges begin at increasing positions with gaps `u,w`, and the corresponding suffix-one drops are `v,z`, the endpoint difference is, up to a unit,

`eps_1 3^(v+z) + eps_2 2^u 3^z + eps_3 2^(u+w)`.             (R64.4)

The signs encode the three move directions.

This is the genuinely new radius-three arithmetic object.

**Status: PROVED ANALYTIC REDUCTION.**

---

## 5. RL-L64 — common-base representation of `2` and `3` in the coprime branch

Assume now

`gcd(A,L)=1`.

Choose integers `r,s` with

`rL+sA=1`,                                                    (R64.5)

and define the unit modulo `D`

`theta = 2^r 3^s`.                                            (R64.6)

Negative exponents mean modular inverses. Since

`2^A == 3^L (mod D)`,

we obtain

`theta^L == 2 (mod D)`,                                      (R64.7)

`theta^A == 3 (mod D)`.                                      (R64.8)

Thus every mixed `2,3` ratio is a single power of `theta`. In particular,

`2^u 3^(-v) == theta^(uL-vA) (mod D)`.                       (R64.9)

So the determinant `uL-vA` is literally the exponent in a common cyclic base, not merely an auxiliary elimination quantity.

**Status: PROVED ANALYTIC THEOREM.**

---

## 6. RL-L65 — a geometric-sum formula for `Q`

For the source word `d`, let

`P_i = d_1+...+d_i`, `P_0=0`,

and define its prefix discrepancy

`H_i = A P_i-iL`, `0<=i<=A`.                                 (R65.1)

Also put

`R_i = 2^i 3^(L-P_i)`.                                       (R65.2)

A one-step check gives, for every bit position, the telescoping identity

`4Q(d) == 2R_0 + sum_(i=1)^(A-1) R_i - R_A`.                (R65.3)

Modulo `D`, `R_A=2^A` and `R_0=3^L` are equal. Hence

`4Q(d) == sum_(i=0)^(A-1) 2^i 3^(L-P_i) (mod D)`.           (R65.4)

Using RL-L64,

`2^i 3^(-P_i) == theta^(iL-A P_i) = theta^(-H_i)`,

so

`4Q(d) == 3^L sum_(i=0)^(A-1) theta^(-H_i) (mod D)`.        (R65.5)

Since `4*3^L` is a unit modulo `D`, we obtain the exact criterion

`D|Q(d)`

`<=>`

`sum_(i=0)^(A-1) theta^(-H_i) == 0 (mod D)`.                 (R65.6)

This is a new representation of the cycle divisibility obstruction as a geometric sum over the prefix-discrepancy lift.

**Status: PROVED ANALYTIC THEOREM.**

---

## 7. RL-L66 — radius 3 becomes a three-jump discrepancy walk

Let

`d' = tau^m d`,

and define

`G_i = P_i(d')-P_i(d)`.                                      (R66.1)

The periodic extension of `H_i` gives the exact identity

`H_(i+m) = H_i + e + A G_i`,                                 (R66.2)

where

`e = H_m = A P_m-mL`.                                        (R66.3)

For exact radius `3`, RL-L62 says

`sum |G_i|=3`,                                                (R66.4)

with exactly three nonzero values, each `+/-1`.

Thus the full `H` sequence, when read in the rotation order `i -> i+m`, is an arithmetic walk of slope `e` with exactly three jumps of size `+/-A`.

This is considerably more rigid than the raw three-unit `Q` sum.

### 7.1 Immediate gcd split

Both `gcd(A,L)` and `gcd(A,m)` divide `e`. Hence:

- mixed direction: `e=+/-1`, so
  `gcd(A,L)=gcd(A,m)=1`;
- same direction: `e=+/-3`, so both gcds divide `3`.

This sharpens the RL-9 roadmap split.

**Status: PROVED ANALYTIC THEOREM.**

---

## 8. RL-L67 — exact sparse normal forms in the coprime one-orbit branches

The combination of RL-L65 and RL-L66 gives a much smaller arithmetic target than (R64.4).

### 8.1 Mixed direction, normalized to `e=+1`

Here `gcd(A,m)=1`. Read indices in the order

`i_t = tm mod A`, `0<=t<A`,

and put

`h_t=H_(i_t)`.

Then

`h_(t+1)=h_t+1+A G_(i_t)`.                                   (R67.1)

Write

`h_t=t+A N_t`.                                                (R67.2)

There are exactly three jump times

`a<b<c`,

and the three nonzero `G` values sum to `-1`. Put

`rho = theta^(-1)`.                                          (R67.3)

Because `theta^A=3`, RL-L65 becomes

`D|Q(d) <=> sum_t rho^t 3^(-N_t) == 0 (mod D)`.             (R67.4)

Also `1-rho` is a unit modulo `D`: if a prime divisor of `D` made `rho=1`, then `theta=1` and (R64.7) would give `2=1` modulo that prime.

Telescoping the three jumps therefore gives exactly one of the following, according to the sign order of the jumps:

`(-1,-1,+1):`

`rho^a + 3 rho^b - 3 rho^c == 0 (mod D)`,                   (R67.5)

`(-1,+1,-1):`

`rho^a - rho^b + rho^c == 0 (mod D)`,                       (R67.6)

`(+1,-1,-1):`

`-rho^a + rho^b + 3 rho^c == 0 (mod D)`.                    (R67.7)

Conversely each corresponding sparse congruence is equivalent to `D|Q(d)` under the radius-three hypotheses.

The `e=-1` case is the reversed orientation of the same three forms.

### 8.2 Same direction, coprime, one rotation orbit

Now normalize to

`e=+3`, `gcd(A,L)=gcd(A,m)=1`.

All three jumps are `G=-1`. Put

`sigma = theta^(-3)`.                                        (R67.8)

The element `1-sigma` is a unit modulo `D`. Indeed, if a prime `p|D` satisfied `theta^3=1`, then

`2^3 = theta^(3L) == 1 (mod p)`,

`3^3 = theta^(3A) == 1 (mod p)`,

so `p` would divide both `7` and `26`, impossible.

If the three jump times are `a<b<c`, the geometric-sum criterion is therefore equivalent to

`sigma^a + 3 sigma^b + 9 sigma^c == 0 (mod D)`.              (R67.9)

Again the negative orientation is obtained by reversal.

Thus two major coprime radius-three branches have been reduced from arbitrary word divisibility to one explicit sparse trinomial at three jump times.

**Status: PROVED ANALYTIC REDUCTION.**

---

## 9. What remains analytically open at radius 3

RL-L63 removes the connected `[3]` geometry completely.

The unresolved infinite cases are now:

1. **mixed, coprime, disconnected** — governed by the three sparse forms (R67.5)-(R67.7);
2. **same direction, coprime, `gcd(A,m)=1`** — governed by (R67.9);
3. **same direction, coprime, `gcd(A,m)=3`** — a three-orbit version not yet collapsed to one sparse sum;
4. **same direction with `gcd(A,L)=3`** — naturally tied to the cubic factor

   `2^(3a)-3^(3ell)`

   `=(2^a-3^ell)(2^(2a)+2^a3^ell+3^(2ell))`.                (R68.1)

The last branch is the exact cubic analogue of RL-9's half-denominator branch. The finite survivor described below is precisely the cubic cofactor itself.

Radius `3` is therefore **not** yet an analytic theorem. The remaining target is much narrower than the generic three-edge path problem.

---

## 10. Exact constructive finite certificate through `A<=40`

The RL-10 verifier does not enumerate all `2^A` words. It enumerates every translation-normalized three-edge flow support, solves

`d_(r+m)-d_r = delta_r`

exactly on the rotation orbits, and retains binary solutions.

Through `A<=40` it checks **140,668** exact radius-three self-rotation solutions with `D>0`:

- connected `[3]`: `940`;
- `[2,1]`: `23,580`;
- `[1,1,1]`: `116,148`.

Among all of them, the necessary condition

`D | Q(tau^m d)-Q(d)`                                       (R68.2)

has exactly six normalized orientation/shift instances, all belonging to the two rotations

`101010`, `010101`,

with

`(A,L,D)=(6,3,37)`.                                          (R68.3)

These are the exact threefold repetition

`(10)^3`,

of the trivial `1 <-> 2` parity cycle. Indeed

`Q(101010)=37=D`,

`Q(010101)=74=2D`.                                           (R68.4)

They are nonprimitive and are already excluded by the inherited repetition theorem RL-L48.

There are **no primitive `D|Delta Q` radius-three survivors through `A<=40`** in this exact constructive domain.

This is strong finite evidence only; it is not used to claim the remaining analytic branches are closed.

The same verifier also certifies:

- 3,200 exact linear distance-three pairs through local length `8`;
- the complete connected coefficient table (R62.4);
- 2,772 constructive connected-orbit checks through `A<80` for the `13`-coefficient orbit claim;
- 4,458 exact checks of the geometric `Q` identity;
- 1,166 mixed `e=+1` sparse-normal-form checks;
- 899 same-direction `e=+3`, one-orbit sparse-normal-form checks.

---

## 11. Strategic consequence

RL-10 changes the radius-three problem in three ways.

First, there is no need to enumerate arbitrary three-swap paths again. Exact radius three is equivalent to three unit-flow edges, with only three support partitions.

Second, the entire connected branch is gone analytically. Any genuine primitive radius-three obstruction must be disconnected.

Third, in the coprime one-orbit cases, the correct object is no longer the raw `Q` numerator but the three-jump discrepancy walk and its sparse geometric congruence.

The best next attack is therefore:

- prove the three mixed sparse forms (R67.5)-(R67.7) cannot vanish modulo `D` under the natural-edge adjacency constraints on the jump times;
- then attack (R67.9) by a cubic/Jacobi or resultant argument;
- in parallel, treat `gcd(A,L)=3` with the cubic cofactor in (R68.1), aiming to show that cofactor divisibility forces the exact repeat `(10)^3` just as RL-9's half-denominator argument forced a square in its zero-determinant case.

If those three tasks close, radius `3` will be completely excluded for primitive `D`-divisible cycle words.

---

## 12. Guardrails

- **RL remains open.**
- **Radius 3 remains analytically open in disconnected branches.**
- RL-L63, the connected radius-three exclusion, is analytic and infinite.
- RL-L64 through RL-L67 are analytic identities/reductions, not nonexistence theorems.
- The `A<=40` scan is finite evidence only.
- The only finite `D`-divisible radius-three survivor found is the nonprimitive repeated trivial cycle `(10)^3`.

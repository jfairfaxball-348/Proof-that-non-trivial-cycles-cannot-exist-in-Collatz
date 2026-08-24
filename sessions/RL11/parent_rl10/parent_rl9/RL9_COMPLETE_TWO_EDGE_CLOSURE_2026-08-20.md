# Collatz R# RL-9 — Complete Closure of the Two-Edge Self-Rotation Route

**Date:** 2026-08-20  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-8  
**Verdict:** **RL remains open.** RL-9 closes, analytically and for all `gcd(A,L)`, the entire route in which two `D`-divisible rotations of one full parity word are connected by two non-cancelling adjacent parity transpositions.

---

## 1. Inherited state

RL-8 proved that for

`D = 2^A - 3^L > 0`,

a disjoint two-edge path between `D`-divisible parity words forces

`D | 2^u +/- 3^v`,

with `2<=u<=A-2`, `1<=v<=L-1`. In the coprime self-rotation case, the two swaps have the same direction, so only

`D | 2^u + 3^v`                                              (R56.1)

survives. RL-8 further introduced

`k = uL-vA`                                                   (R56.2)

and the determinant divisibilities, but did not exclude (R56.1) in general.

RL-9 uses a second invariant that was present but not fully exploited: for

`S(d)=sum_(r=1)^A r d_r`,

a right adjacent transposition `10->01` changes `S` by `+1`, and a left transposition changes it by `-1`.

For a rotation by `m`, with `P_m` ones in the first `m` symbols,

`S(tau^m d)-S(d)=A P_m-mL`.                                  (R56.3)

Thus two same-direction swaps force

`A P_m-mL = +/-2`,                                           (R56.4)

whereas two opposite-direction swaps force

`A P_m-mL = 0`.                                              (R56.5)

These tiny exact discrepancies are the starting point of the closure.

---

## 2. RL-L56 — Jacobi signature of the Collatz cycle denominator

Assume `A>=3` and `D=2^A-3^L>1`. Then `gcd(D,6)=1`. Directly from `D mod 8`, `D mod 4`, and `D mod 12`, the Jacobi symbols are

`(2/D)  = (-1)^L`,                                           (R56.6)

`(-1/D) = (-1)^(L+1)`,                                      (R56.7)

`(3/D)  = (-1)^(A+L+1)`.                                    (R56.8)

Now suppose the plus resonance (R56.1) holds. Since `2` and `3` are units modulo `D`,

`2^u == -3^v (mod D)`.

Taking Jacobi symbols gives

`(2/D)^u = (-1/D) (3/D)^v`.                                 (R56.9)

### 2.1 Coprime consequence when `L` is even

If `gcd(A,L)=1` and `L` is even, then `A` is odd. Equations (R56.6)-(R56.9) become

`1 = -1`,

which is impossible.

Hence:

> **A coprime plus resonance is impossible when `L` is even.**

### 2.2 Coprime consequence when `L` is odd

If `L` is odd, (R56.9) becomes

`(-1)^u = (-1)^(Av)`.

Therefore

`u == Av (mod 2)`.

Since `L` is odd,

`k=uL-vA == u-vA == 0 (mod 2)`.                              (R56.10)

Hence:

> **Every coprime plus resonance has even determinant `k`.**

**Status: PROVED ANALYTIC THEOREM.**

---

## 3. RL-L57 — a coprime two-swap self-rotation has odd determinant

Now assume `gcd(A,L)=1` and a nontrivial self-rotation is reached by two disjoint swaps in the same direction. Reverse the path if necessary so both swaps are right moves `10->01`. Rotate the whole configuration so the swap starts are `0` and `u`, with `2<=u<=A-2`.

Then (R56.4) is

`A P_m-mL=2`.                                                (R57.1)

For the two swap starts, RL-8's exponent `v` is exactly the number of ones in the first `u` symbols:

`v=P_u`.                                                      (R57.2)

Thus

`k=uL-vA=uL-A P_u`.                                          (R57.3)

We prove `k` is odd.

### 3.1 `A` even

Coprimality makes `L` odd. Reducing (R57.1) modulo `2` gives `m` even. Also

`gcd(A,m) | 2`,

so in fact

`gcd(A,m)=2`.                                                (R57.4)

The rotation by `m` has exactly the even and odd position classes as its two orbits. The difference

`delta_r=d_(r+m)-d_r`

has `-1,+1` on each right swap. The sum of `delta` on each rotation orbit must be zero. Consequently the two swap starts have opposite parity, so `u` is odd.

Because `A` is even and `L` odd,

`k=uL-vA == u == 1 (mod 2)`.                                 (R57.5)

### 3.2 `A` odd

Then `L` is also odd in the only branch not already killed by RL-L56. From (R57.1),

`gcd(A,m)=1`.

Let `a` be the inverse of `m` modulo `A`. Multiplying

`mL == -2 (mod A)`

by `a` gives

`2a == A-L (mod A)`.

Both sides are even and lie in the unique compatible range, hence

`a=(A-L)/2`.                                                  (R57.6)

Put

`U = au mod A`.

In the rotation-orbit coordinate `t=ar mod A`, the two negative events are at

`0, U`,

and the two positive events at

`a, U+a`.

A binary cyclic solution requires the signs to alternate. Since `2a=A-L<A`, this forces

`a < U < A-a`.                                               (R57.7)

The zero states in orbit coordinate are exactly the two intervals

`1,...,a`

and

`U+1,...,U+a`.                                               (R57.8)

Let `z=u-v` be the number of zeros in the natural interval from the first swap start up to the second. Write

`au=qA+U`.

A direct crossing count of the multiples of `a` modulo `A` gives

`z=2q+1`.                                                     (R57.9)

For completeness, the count is elementary: the high residues in `[A-a,A)` among the first `u` multiples are exactly the `q` wrap events; the low residues in `(0,a]` contribute the same `q` wraps plus the initial residue `a`. Hence the total is `q+(q+1)`.

Now

`k=uL-vA`

` = u(A-2a)-(u-z)A`

` = Az-2au`

` = A(2q+1)-2(qA+U)`

` = A-2U`.                                                    (R57.10)

Since `A` is odd, `k` is odd.

Therefore:

> **Every coprime disjoint same-direction two-swap self-rotation has odd determinant `k`.**

Combining with RL-L56, which says a plus resonance requires `k` even, yields a contradiction.

**Status: PROVED ANALYTIC THEOREM.**

---

## 4. RL-L58 — overlapping coprime paths cannot use the exceptional factor 5

RL-8 showed that an overlapping two-edge path has only two possible local forms:

`100 <-> 001`,

whose `Q` change is a `2,3`-unit, and

`110 <-> 011`,

whose `Q` change is `5` times a `2,3`-unit.

The unit case is impossible for `D>1`. The only apparent survivor is therefore

`D=5`                                                       (R58.1)

with the `110<->011` shape.

For `D=5`, reduction modulo `8` forces `L` odd, while reduction modulo `3` forces `A` odd. In the coprime branch, orient the move as `110->011`. It moves one `1` two positions to the right, so again

`A P_m-mL=2`.

With

`a=(A-L)/2=m^(-1) mod A`,

the rotation-orbit difference now has only one negative event at `t=0` and one positive event at `t=2a`. Since the word contains exactly `A-L=2a` zeros, the zero interval is exactly

`t=1,...,2a`.

Natural position `1` has orbit coordinate `a`, so it must be zero. Therefore the local factor beginning at the moved `1` is `100`, not `110`.

Thus the only realizable overlap shape is the unit case, already impossible for `D>1`.

**Status: PROVED ANALYTIC THEOREM.**

---

## 5. RL-L59 — opposite-direction two-swap self-rotations are impossible for every gcd

Now let the two disjoint swaps have opposite directions. Orient the path so the left swap is

`10->01`

and the right swap is

`01->10`.

Equation (R56.5) gives

`A P_m=mL`.                                                   (R59.1)

Write

`g=gcd(A,L)`, `A=ga`, `L=g ell`, `gcd(a,ell)=1`.

For a nontrivial rotation,

`m=h a`, `P_m=h ell`,                                        (R59.2)

for some `1<=h<=g-1`. In particular `g>1`.

Let

`H=gcd(A,m)=a gcd(g,h)`.                                     (R59.3)

Since `a>ell>=1`, we have `H>=2`.

Set the left swap start to `0` and the right start to `u`. The difference signs are

- negative at `0` and `u+1`;
- positive at `1` and `u`.

The sum of the difference on every rotation orbit modulo `H` must vanish. Since `0` and `1` lie in distinct orbits, this forces

`u == 0 (mod H)`.                                            (R59.4)

Thus the interval of length `u` between the swap starts is a union of complete `H`-blocks.

Let `v` be its number of ones. Because the left pair is `10` and the right pair `01`, this `v` is exactly RL-8's binomial exponent.

For any start congruent to `0 mod H`, the translated length-`u` interval is again a union of complete `H`-blocks. The four difference contributions cancel blockwise, so all such intervals contain the same number `v` of ones.

There are `A/H` such starts, and each position belongs to exactly `u/H` of their intervals. Averaging therefore gives

`(A/H) v = (u/H) L`,

hence

`vA=uL`,

so

`k=uL-vA=0`.                                                  (R59.5)

Because `gcd(a,ell)=1`,

`u=q a`, `v=q ell`,                                          (R59.6)

with `1<=q<=g-1`.

The opposite-direction path requires the difference resonance

`D | 2^u-3^v`.                                               (R59.7)

But `D>0` implies `2^a>3^ell`, and therefore

`0 < 2^(qa)-3^(q ell) < 2^(ga)-3^(g ell)=D`.                (R59.8)

So (R59.7) is impossible.

Hence:

> **No nontrivial opposite-direction two-swap self-rotation can join two `D`-divisible rotations, for any `gcd(A,L)`.**

**Status: PROVED ANALYTIC THEOREM.**

---

## 6. RL-L60 — the `g=2` same-direction branch is killed by the half denominator

After RL-L57 and RL-L59, the only disjoint same-direction case not yet covered is

`gcd(A,L)=2`.

Write

`A=2a`, `L=2 ell`, `gcd(a,ell)=1`,

and

`c=a-ell>0`.                                                  (R60.1)

Orient both swaps as `10->01`, at starts `0` and `u`. Then

`aP_m-m ell=1`.                                              (R60.2)

Let

`v=P_u`,

and define the half determinant

`k_0=u ell-v a`,                                             (R60.3)

so the RL-8 determinant is `k=2k_0`.

Also factor

`D=(2^a-3^ell)(2^a+3^ell)`.                                 (R60.4)

Put

`D_+ = 2^a+3^ell`.                                           (R60.5)

### 6.1 Exact combinatorial bound on `k_0`

From (R60.2),

`gcd(2a,m)` is either `1` or `2`.

#### Case H=1

Let

`r=m^(-1) mod 2a`,

and

`U=ru mod 2a`.

Equation (R60.2) gives

`r == c (mod a)`,

so `r` is either `c` or `c+a`.

Solving the two-event-pair difference equation around the unique rotation orbit and counting the zeros between the swap starts gives the exact centered-residue formula

`k_0 = a-U`.                                                  (R60.6)

If `r=c`, this follows from the same two-interval crossing count as (R57.9): writing `cu=2aq+U`, the prefix has `2q+1` zeros. If `r=c+a=2a-ell`, apply the identical count to ones with the reversed orbit orientation. Both give (R60.6).

Therefore

`|k_0|<a`, unless `k_0=0` of course still satisfying the same bound. (R60.7)

#### Case H=2

Write

`m=2n`,

so `a` and `u` are odd. Put

`w=(u-1)/2`,

`r=n^(-1) mod a`,

`V=rw mod a`,

`T=r(w+1) mod a`.                                            (R60.8)

The even and odd position classes are the two rotation orbits. Each contains exactly one negative and one positive event. Their zero intervals have lengths `T` and `a-V`; equation (R60.2) is equivalent to

`T+a-V=2c`.                                                   (R60.9)

Counting zeros in the first `u=2w+1` natural positions across the two parity orbits gives

`2k_0 = a-V-T`.                                              (R60.10)

Here is the exact residue count. Write

`rw=qa+V`, `r(w+1)=q'a+T`.

Also write `2c=r+eta a` with `eta in {0,1}`. Equation (R60.9) is equivalent to

`q'-q=1-eta`.

Pair the even position indexed by `x` with the odd position indexed by `w-x`. For `1<=x<=w-1`, the pair contributes a second zero precisely when the residue `R_x=rx mod a`, translated by the terminal residue `V`, lies in the oriented arc from `V` to `T`. Under `x -> w-x` this condition becomes

`R_(w-x) >= a-r`,

which is exactly a wrap event for addition by `r`. The number of such events among the first `w` steps is `q=floor(rw/a)`. If the terminal step wraps (`eta=0`, so `q'=q+1` and `T<V`), the prefix zero count is therefore

`z=q+1`.

If it does not wrap (`eta=1`, so `q'=q` and `T>V`), every paired even/odd position contributes one baseline zero and the same `q` wrap events contribute one extra zero, giving

`z=w+q+1`.

Substituting either formula into `k_0=az-cu`, together with `2c=r+eta a`, yields exactly (R60.10).

Since `1<=V,T<=a-1`,

`|k_0| <= (a-2)/2 < a`.                                      (R60.11)

Thus in every `g=2` same-direction self-rotation,

`|k_0|<a`.                                                    (R60.12)

### 6.2 The half denominator demands the opposite inequality

A surviving disjoint same-direction path would require

`2^u == -3^v (mod D_+)`,                                    (R60.13)

while by definition of `D_+`,

`2^a == -3^ell (mod D_+)`.                                  (R60.14)

Raise (R60.13) to `ell`, raise (R60.14) to `v`, and divide. This gives

`2^(k_0) == (-1)^(ell-v) (mod D_+)`.                         (R60.15)

For `k_0!=0`, inversion if necessary gives

`D_+ | 2^|k_0| - (-1)^(ell-v)`.                             (R60.16)

But `|k_0|<a`, so the nonzero integer on the right has absolute value at most

`2^(a-1)+1`,

whereas

`D_+=2^a+3^ell > 2^a`.                                      (R60.17)

Impossible.

### 6.3 The zero-determinant subcase is a repetition

If `k_0=0`, then

`u ell=v a`.

Coprimality of `(a,ell)` and the proper ranges force

`u=a`, `v=ell`.                                              (R60.18)

The two swap starts are exactly half a word apart. The difference pattern is invariant under the half-turn `r->r+a`. Since the rotation difference equation commutes with this half-turn, the half-difference

`h_r=d_(r+a)-d_r`

is constant on every rotation orbit. At a swap start both half-separated bits are `1`, so the constant is zero. Hence

`d_(r+a)=d_r` for all `r`.                                   (R60.19)

The word is the exact square of its length-`a` half and is nonprimitive. RL-L48 excludes it as a primitive cycle word.

Therefore the `g=2` same-direction branch has no primitive survivor.

**Status: PROVED ANALYTIC THEOREM.**

---

## 7. RL-L61 — complete two-edge self-rotation exclusion

Collect the cases.

### Overlapping edges

- `100<->001`: `Q` changes by a unit, impossible for `D>1`.
- `110<->011`: requires `D=5`.
  - if `gcd(A,L)=2`, then `A,L` are even and `D==7 mod8`, impossible;
  - if `gcd(A,L)=1`, RL-L58 shows the factor-5 local shape is incompatible with the rotation orbit;
  - if `gcd(A,L)>2`, the `S` discrepancy `+/-2` is already impossible because `gcd(A,L)` must divide it.

### Disjoint, same direction

The `S` discrepancy is `+/-2`, so

`gcd(A,L) | 2`.

- `g=1`: RL-L56 + RL-L57 give the even/odd determinant contradiction.
- `g=2`: RL-L60 gives the half-denominator contradiction, with `k_0=0` reducing to an exact repeat.

### Disjoint, opposite direction

RL-L59 excludes this case for every gcd.

Therefore:

> **RL-L61. Let `d` be a primitive full parity word with `D=2^A-3^L>1`. If `D|Q(d)`, then no nontrivial rotation of `d` can be reached from `d` by two non-cancelling adjacent cyclic transpositions.**

Equivalently, after RL-L52 excluded one-edge self-rotations, the transposition distance from any `D`-divisible primitive cycle rotation to every distinct rotation is now at least **3**.

**Status: PROVED ANALYTIC THEOREM.**

This is the main RL-9 result.

---

## 8. Finite verification certificate

New verifier:

`verify_rl9_twoedge_closure.py`

passes exactly and reports:

- 3,072 direct Jacobi-signature checks;
- exact coprime plus-resonance parity checks;
- 48,512 explicit cyclic two-edge self-rotation path instances through `A<=13`;
- 7,508 overlap paths;
- 26,340 disjoint same-direction paths;
- 14,664 disjoint opposite-direction paths;
- 21,260 coprime determinant-parity checks;
- 5,080 `g=2` half-determinant formula checks in the word audit;
- 14,664 opposite-direction `k=0` checks;
- **zero primitive `D`-divisible length-two survivors** in that full path domain;
- 30,602 constructive `g=2` determinant-formula checks through half-length `a<=45`;
- a strengthened exact plus-resonance scan through `A<=2000`.

The only proper plus-resonance parameter pairs through `A<=2000` are still

`(A,L,D)=(4,2,7)`

and

`(A,L,D)=(8,5,13)`.

The first is the repeated trivial word branch; the second is coprime but is now analytically excluded from being a two-edge self-rotation by RL-L56/RL-L57.

This `A<=2000` statement remains **FINITE EVIDENCE**. It is no longer needed for RL-L61.

---

## 9. Strategic consequence

The transposition program has now advanced one full rank:

- distance 1: excluded by RL-L51/RL-L52;
- distance 2: excluded by RL-L61;
- every primitive `D`-divisible cycle word must have cyclic self-rotation transposition distance at least 3.

This does **not** prove RL. A length-three path has a weighted change of three units and introduces genuinely new cancellation geometries. But RL-9 says future work should not enumerate generic length-three paths. The exact `S` discrepancy still severely restricts their direction signatures:

- three equal directions give `A P_m-mL=+/-3`, so `gcd(A,L)|3`;
- two moves one way and one the other give discrepancy `+/-1`, so necessarily `gcd(A,L)=1`;
- there is no zero-discrepancy signature with three moves.

This immediately suggests a **mod-3 gcd split** before any weighted `Q` analysis.

The more promising alternative is to exploit RL-L54's least-state prefix/suffix envelopes to prove that the distinguished root/return rotations cannot be at transposition distance 3 either, without classifying all words.

---

## 10. Highest-priority next attack

### Rank 1 — length-three direction signature before weights

For a three-edge self-rotation path, first use

`A P_m-mL in {+/-1,+/-3}`.

This forces:

- mixed `2+1` direction paths into `gcd(A,L)=1`;
- three-equal-direction paths into `gcd(A,L) in {1,3}`.

Only after this gcd split derive the exact three-unit `Q` change. Seek a Jacobi/cubic-character analogue of RL-L56, or a determinant pair that forces contradictory parity/residue classes.

### Rank 2 — distinguished root/return distance

Use RL-L27 and RL-L36 to show that the root rotation and final-return/first-post-neutral rotations cannot lie within transposition radius 3. Combine:

- root prefix `1^s 0^t 1...`;
- final return block;
- the universal least-state suffix envelope;
- the externally forced first-183 root-prefix supercritical envelope.

The target is a **distinguished-rotation distance theorem**, not a generic word theorem.

### Rank 3 — factor descent through exact-balanced cuts

RL-L59 shows something stronger than the failed bare `D_0` descent: when a zero-`S` path actually comes from an opposite-direction self-rotation, its balanced cut forces exact proportionality and kills the path by size. Revisit RL-L55 looking for boundary grammar that forces one of its block cuts into this exact-balanced regime.

### Rank 4 — positive-density displacement

RL-L61 says every nontrivial rotation is at least three transpositions away, but a constant lower bound is still far from the `Omega(L)` displacement needed for the quantitative Christoffel route. Continue seeking a density theorem rather than iterating constant-radius exclusions indefinitely.

---

## 11. Guardrails

- **RL remains open.**
- RL-L61 is an infinite analytic exclusion of transposition radius 2; it is not merely a finite search result.
- The `A<=2000` resonance scan is only supporting finite evidence.
- The inherited external floor `R#>=2^71` is not used in RL-L61.
- The failed bare `D_0` descent from RL-8 remains failed; RL-L59 only identifies a special exact-balanced situation where descent-like proportionality is forced by a genuine self-rotation path.

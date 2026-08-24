# Collatz R# RL-8 — Two-Edge Resonance, Minimum-Word Slope Barriers, and the Limit of Bare Factor Descent

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-7  
**Verdict:** **RL remains open.** RL-8 advances the two highest-priority RL-7 routes. It reduces every genuinely two-edge parity transposition obstruction to a very small arithmetic target, derives an exact full-parity suffix/prefix barrier at the least cycle state, and shows that the proposed proper-factor denominator descent is false without additional root/boundary structure.

---

## 1. Inherited target

RL-7 reduced the k=0 global obstruction to the odd denominator

`D = 2^A - 3^L > 0`

and proved:

- every rotation of an integer-cycle parity word is `D`-divisible;
- one adjacent parity transposition changes `Q` by a unit modulo `D`;
- a one-edge self-rotation is exactly a primitive Christoffel class;
- primitive Christoffel words are therefore internally excluded;
- every remaining primitive cycle is non-Christoffel, but the one-defect quantitative loss is too small by a factor of order `L`.

The next stated target was a path of length at least two between two `D`-divisible rotations, or a stronger global displacement theorem.

RL-8 attacks exactly the length-two case first.

---

## 2. RL-L53 — every two-edge path collapses to a binomial resonance

For a full parity word `d` of length `A` with `L` ones, recall

`Q(d) = sum_(i=1)^A 2^(i-1) 3^(r_i(d)) d_i`,                 (R53.1)

where `r_i(d)` is the number of ones strictly to the right of position `i`.

For one internal adjacent move `10 -> 01` starting at zero-based position `i`, RL-L49 gives the exact increment

`Delta Q = 2^i 3^b`,                                        (R53.2)

where `b` is the number of ones to the right of the moved pair. The reverse move has the negative of this increment.

Consider a path of exactly two non-cancelling adjacent transpositions between words `d_0` and `d_2` with the same `(A,L)`. For a cyclic path, rotate both endpoints and the whole path jointly so that the at most two used cyclic edges are internal. There are only two structural cases.

### 2.1 Overlapping edges

If the two used edges overlap, the changed length-three factor is necessarily one of

`100 <-> 001`,

or

`110 <-> 011`.                                               (R53.3)

In the first case, the two unit increments add as

`2^a 3^b + 2^(a+1) 3^b = 2^a 3^(b+1)`,                    (R53.4)

so the total change is still a unit modulo every `D` with `gcd(D,6)=1`.

In the second case,

`2^a 3^(b+1) + 2^(a+1) 3^b = 5 * 2^a 3^b`.                (R53.5)

Therefore, if both endpoints are `D`-divisible and `D>1`, an overlapping two-edge path is impossible except for the exceptional denominator

`D = 5`.                                                     (R53.6)

No generic two-edge cancellation survives in the overlap case.

### 2.2 Disjoint edges

Now let the two internal edges begin at positions `i<j`, with

`u = j-i >= 2`.                                              (R53.7)

Let `b_i,b_j` be the numbers of ones to the right of the respective pairs in the original word. Because the left pair sees the one in the right pair while the right pair does not,

`v = b_i-b_j >= 1`.                                          (R53.8)

The two edge magnitudes are

`2^i 3^(b_i)` and `2^j 3^(b_j)`.

Writing `eps_i,eps_j in {+1,-1}` for their directions gives

`Q(d_2)-Q(d_0)`

`= 2^i 3^(b_j) [ eps_i 3^v + eps_j 2^u ]`.                  (R53.9)

Since `D` is coprime to `6`, if both endpoints are `D`-divisible then necessarily

`D | (2^u + 3^v)`                                            (R53.10)

when the two moves have the same direction, and

`D | (2^u - 3^v)`                                            (R53.11)

up to an overall sign when their directions are opposite.

Thus the entire disjoint two-edge problem is reduced to one proper binomial resonance with

`2 <= u <= A-2`, `1 <= v <= L-1`.                            (R53.12)

### 2.3 Coprime self-rotations force the plus sign

Now assume `d_2=tau^m(d_0)` is a nontrivial rotation and `gcd(A,L)=1`.

For the same common cut, put

`S(d)=sum_(k=1)^A k d_k`.

Rotating the first `m` bits to the end gives

`S(tau^m d)-S(d)=A P_m-mL`,                                  (R53.13)

where `P_m` is the number of ones in that prefix.

Two opposite-direction internal swaps would give zero total change in `S`. Equation (R53.13) would then imply

`A P_m=mL`.

Coprimality forces `A|m`, impossible for `0<m<A`. Therefore a disjoint two-edge self-rotation in the coprime case must use two moves in the same direction, so it necessarily satisfies the **plus** resonance

`D | (2^u+3^v)`.                                             (R53.14)

The only overlapping alternative is the exceptional `D=5` case from (R53.6).

### 2.4 Determinant collapse of the binomial resonance

More generally write

`2^u == sigma 3^v (mod D)`,                                  (R53.15)

where `sigma=+1` corresponds to the minus resonance and `sigma=-1` to the plus resonance. Together with

`2^A == 3^L (mod D)`,                                        (R53.16)

put

`k = uL-vA`.                                                  (R53.17)

Raising (R53.15) to the `L`th power and (R53.16) to the `v`th power eliminates the power of `3`; similarly one can eliminate the power of `2`. If `k!=0`, this gives

`D | [2^|k| - sigma^L]`,                                     (R53.18)

and

`D | [3^|k| - sigma^A]`.                                     (R53.19)

Hence a two-edge resonance forces `D` into the common divisor of two much more rigid exponential values at the determinant `|uL-vA|`.

For a coprime self-rotation, `k=0` is impossible because `u/A=v/L` with `0<u<A` would force `A|u`. Thus every coprime two-edge self-rotation that could survive RL-L49 must satisfy the nonzero determinant constraints (R53.18)-(R53.19).

**Status: PROVED ANALYTIC THEOREM.**

### Why this is progress

The Rank-1 problem is no longer “control a weighted sum of two arbitrary units.” At path length two there are only three surviving arithmetic shapes:

1. an overlap exceptional factor `D=5`;
2. a proper plus resonance `D | 2^u+3^v`;
3. in non-coprime/opposite-orientation cases, a proper difference resonance `D | 2^u-3^v`.

For coprime self-rotations only item 1 or item 2 remains.

---

## 3. Finite diagnostic for RL-L53

The new verifier exhausts 29,692 internal non-cancelling two-edge paths through word length 10 and checks the overlap/disjoint formulas exactly.

It also exhausts all admissible binary words through `A<=16` for exact cyclic self-rotation distance two. There are 4,702 such word instances. The only `D`-divisible instances are

`1010` and its rotation `0101`

at

`(A,L,D)=(4,2,7)`.                                           (R53.20)

These are the doubled trivial `10` word and are nonprimitive. Their two-edge change realizes the resonance

`7 = 2^2+3`.                                                  (R53.21)

A separate exact parameter search through `A<=200` for any proper binomial resonance in the ranges (R53.12) finds only

- `(A,L,D)=(4,2,7)`;
- `(A,L,D)=(5,3,5)`;
- `(A,L,D)=(8,5,13)`.

This is **finite evidence only**, not a theorem for unbounded `(A,L)`. It does, however, isolate a concrete next number-theoretic target: rule out proper plus resonances for large coprime cycle parameters, preferably by combining (R53.18)-(R53.19) with the root/return grammar rather than by naked brute force.

---

## 4. RL-L54 — least-state suffix contraction and the exact prefix rescue bound

The transposition route benefits from a second full-parity fact that does not require Christoffel extremality.

Let `d` be the full parity word rotated to the least positive state `R#` of a primitive hypothetical cycle. For a prefix of length `m` containing `p` ones, write its affine numerator as `B_m`. Then the shortcut map over that prefix is

`2^m x_m = 3^p R# + B_m`.                                    (R54.1)

The same identity applies to any suffix ending at `R#`.

### 4.1 Every proper suffix ending at the minimum is multiplicatively contracting

Take a proper suffix of length `m`, with `p` ones, beginning at cycle state `x` and ending at `R#`. Then

`2^m R# = 3^p x + B`,                                        (R54.2)

with `x>=R#` and `B>=0`. If `p>0`, then `B>0`; if `p=0`, positivity of `x` already gives strict contraction. Therefore

`2^m > 3^p`                                                   (R54.3)

for **every proper suffix ending at the least state**.

Equivalently, if `E_m` is the number of ones in the final `m` bits and

`alpha = log_3 2`,

then

`E_m < alpha m`,

hence

`E_m <= floor(alpha m)`.                                     (R54.4)

This is an exact irrational mechanical-word envelope on every proper suffix of the least-state rotation.

### 4.2 Any undercritical prefix must be rescued by its additive numerator

Now take a proper prefix of length `m`, with `p` ones, from `R#` to a later state `x_m>=R#`. From (R54.1), if

`2^m > 3^p`,                                                  (R54.5)

then

`B_m >= (2^m-3^p) R#`,                                       (R54.6)

strictly for a primitive cycle because a proper phase cannot be the least state again.

For fixed `(m,p)`, adjacent right-transpositions increase the prefix numerator, so its maximum occurs when all `p` ones occupy the rightmost `p` positions. The exact maximum is

`B_max(m,p)=2^(m-p)(3^p-2^p)`.                               (R54.7)

Therefore every undercritical proper root prefix obeys the explicit bound

`R# < 2^(m-p)(3^p-2^p)/(2^m-3^p)`.                          (R54.8)

This is the full-parity analogue of the least-anchor prefix/suffix sandwich, but it acts directly on the parity count of a specific prefix.

**Status: PROVED ANALYTIC THEOREM.**

### 4.3 External `2^71` floor gives a 183-step supercritical root window

Using the inherited external computational input that any nontrivial positive cycle minimum must satisfy

`R# >= 2^71`,                                                 (R54.9)

an exact finite scan of (R54.8) gives:

> For every proper root prefix with `1<=m<=183`, one must have
>
> `3^(P_m) > 2^m`,                                           (R54.10)
>
> equivalently `P_m >= ceil(alpha m)`.

At `m=184`, the pair `p=116` is the first generic undercritical rescue bound to reach the external floor:

`B_max(184,116)/(2^184-3^116) ~= 2.8047e21`

which is about `1.18785 * 2^71`.

So `183` is the exact threshold for this particular floor-plus-generic-prefix argument.

**Status: EXACT FINITE COROLLARY CONDITIONAL ON INHERITED EXTERNAL INPUT.**

### Strategic interpretation

The least-state rotation has a sharp directional asymmetry:

- every proper suffix is below the critical multiplicative slope;
- the first 183 proper prefixes are forced above it by the external least-counterexample floor.

This does not produce the required `Omega(L)` Christoffel displacement by itself, but it gives a concrete finite window in which any proposed distinguished-rotation path must respect a one-sided mechanical envelope.

---

## 5. RL-L55 — exact proper-factor block congruence

RL-7 proposed a denominator descent when

`g=gcd(A,L)>1`.

Put

`a=A/g`, `ell=L/g`,

and

`D_0=2^a-3^ell`.                                              (R55.1)

Then

`D_0 | D`                                                     (R55.2)

by the difference-of-powers factorization.

Partition a parity word `d` into `g` consecutive blocks

`B_0,...,B_(g-1)`

of length `a`. Let `r_j` be the number of ones in block `B_j`, let

`K_(j+1)=r_0+...+r_j`,

and define the cumulative block imbalance

`E_(j+1)=K_(j+1)-(j+1)ell`.                                  (R55.3)

The global numerator splits exactly as

`Q(d)=sum_(j=0)^(g-1) 2^(ja) 3^(L-K_(j+1)) Q(B_j)`.          (R55.4)

Modulo `D_0`, use

`2^a == 3^ell`.                                               (R55.5)

Then

`Q(d) == 3^(L-ell) * sum_(j=0)^(g-1) 3^(-E_(j+1)) Q(B_j)`

`       (mod D_0)`.                                          (R55.6)

All inverse powers of `3` are legitimate because `gcd(D_0,3)=1`.

Thus the proper factor sees a **weighted block cancellation law**, not an individual shorter-cycle numerator.

If each block happens to contain exactly `ell` ones, all `E_j=0` and the condition simplifies to

`D_0 | sum_j Q(B_j)`,                                         (R55.7)

which still does not force any one block to be `D_0`-divisible or equal to another block.

**Status: PROVED ANALYTIC THEOREM.**

---

## 6. RL-G9 — bare proper-factor descent is false

The smallest useful counterexample to the naive implication

`D_0 | Q(d)  =>  d is a repetition / shorter block closes`

is

`d = 100001`,

with

`(A,L)=(6,2)`, `g=2`, `(a,ell)=(3,1)`,

`D=2^6-3^2=55`,

`D_0=2^3-3=5`.                                                (R56.1)

The two length-three blocks are

`100`, `001`,

so they are balanced at one `1` each and have local numerators

`Q(100)=1`, `Q(001)=4`.                                      (R56.2)

Hence

`Q(d)=35`,

`5 | 35`, but `55` does not divide `35`.                      (R56.3)

The full word is primitive under rotation; it is not a repeated shorter block. The proper-factor divisibility arises purely from the block cancellation

`1+4 == 0 (mod 5)`.                                          (R56.4)

The finite block audit finds 219 primitive `D_0`-divisible examples in its small declared domain, so this is not an isolated pathology.

Therefore the Rank-3 idea from RL-7 cannot work in the form

“factor `D`, reduce modulo `D_0`, and infer symbolic repetition.”

Any successful descent must add genuinely RL-specific information, such as:

- the least-root prefix/suffix inequalities;
- exact root departure cylinders;
- final-return 3-adic discrete-log classes;
- or compressed boundary-gate information that prevents the weighted block cancellations in (R55.6).

**Status: FAILED / REFUTED ROUTE in its bare form.**

---

## 7. New finite verification certificate

New verifier:

`tools/verify_rl8_twoedge_suffix_descent.py`

It passes exactly and reports:

- 29,692 internal non-cancelling two-edge path checks;
- 3,586 overlapping unit-factor checks;
- 3,586 overlapping factor-5 checks;
- 22,520 disjoint binomial-reduction checks;
- 4,702 exact cyclic two-edge self-rotation instances through `A<=16`;
- only the two rotations of repeated `1010` are `D`-divisible in that domain;
- proper binomial-resonance parameters through `A<=200` occur only at `(4,2,7)`, `(5,3,5)`, `(8,5,13)`;
- 26,419 least-rotation words audited;
- 317,295 proper-suffix slope checks;
- 152,017 undercritical-prefix rescue checks;
- exact confirmation that `m=184,p=116` is the first generic rescue bound reaching `2^71`;
- 1,373 proper-factor block congruence checks;
- 219 primitive `D_0`-divisible examples in the declared block domain;
- the explicit primitive balanced counterexample `100001` is checked exactly.

The inherited RL-7 verifier also passes unchanged.

**Status: EXACT FINITE CERTIFICATE for the stated audit domains.**

---

## 8. Strongest current architecture after RL-8

The k=0 branch now has the following hierarchy.

1. **Global realization:** inherited RL-6/RL-7 still reduces realization to `D|C_good` / `D_res=1` plus finite boundary gates.
2. **One edge:** RL-L49/RL-L51/RL-L52 completely exclude the one-edge self-rotation route except the trivial cycle.
3. **Two edges:** RL-L53 reduces every surviving two-edge route to `D=5` or one proper binomial resonance `D|2^u +/-3^v`; coprime self-rotations require the plus sign, with the determinant constraints (R53.18)-(R53.19).
4. **Least-state geometry:** RL-L54 gives an exact critical-slope envelope on every proper suffix and an explicit rescue bound for every undercritical prefix.
5. **Proper factors:** RL-L55 shows exactly what reduction modulo `D_0` remembers: a weighted block sum. RL-G9 shows this is insufficient for descent without extra RL grammar.
6. **Christoffel gap:** inherited RL-L50 remains valid but still needs linearly many weighted defects to become a global contradiction.

RL remains open.

---

## 9. Highest-priority next attack

### Rank 1 — eliminate the two-edge binomial resonance under RL endpoint grammar

Do not search arbitrary length-two paths anymore. For a candidate distinguished-rotation pair, derive its actual `(u,v)` and attack

`D | 2^u+3^v`                                                  (R57.1)

in the coprime case.

Use the determinant

`k=uL-vA`

together with

`D | 2^|k|-(-1)^L`,

`D | 3^|k|-(-1)^A`.                                          (R57.2)

The most valuable intermediate theorem would be a root/return bound forcing `|k|` into a range too small to support a divisor as large as `D`, or forcing a forbidden sign/parity class.

### Rank 2 — combine the 183-step prefix window with the final-return suffix

For the least-state parity rotation, encode explicitly:

- root prefix `1^s 0^t 1...` from RL-L27;
- closing suffix from the final physical plateau and RL-L36;
- the universal suffix envelope (R54.4);
- the externally forced first-183 prefix envelope (R54.10).

Search for a theorem on the **distance between these two mechanical envelopes**, not arbitrary word distance.

### Rank 3 — salvage factor descent only with weighted-block rigidity

Equation (R55.6) is now the correct proper-factor target. A viable descent theorem must prevent cancellation among the terms

`3^(-E_j) Q(B_j) (mod D_0)`.

Root/return grammar may force one term to have a unique valuation/order signature or may constrain the imbalance path `E_j`. Without such input, descent is false.

### Rank 4 — positive-density Christoffel loss remains the global quantitative target

The prefix/suffix barriers provide new local mechanical constraints, but no `Omega(L)` displacement theorem has yet been proved. Continue to treat `s=2` as the extremal branch and `s>=3` as a potentially easier over-dense branch.

---

## 10. Guardrails

- **RL is not proved.**
- The two-edge reduction is an analytic theorem; the absence of large binomial resonances through `A<=200` is finite evidence only.
- The `2^71` prefix-window corollary depends on the inherited external computational verification floor.
- The proper-factor counterexample refutes only **bare** descent. It does not rule out a stronger descent using the RL root/return/boundary grammar.
- Do not scale brute-force path enumeration. Future computation should target the determinant `k`, the root/suffix mechanical envelopes, or weighted block cancellation in (R55.6).

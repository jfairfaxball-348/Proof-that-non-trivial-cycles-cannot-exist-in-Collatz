# Collatz R# RL-7 — Mixed Divisibility, Reciprocal Defect, and a Quantitative Christoffel Gap

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-6  
**Verdict:** **RL remains open.** RL-7 does not prove nonexistence of a nontrivial Collatz cycle. It adds four exact structural tools aimed directly at the remaining RL-6 obstruction `D | C_good`: a rotation-invariant residual denominator, a repeated-word descent, a unit-edge obstruction in the parity-word transposition graph, and a quantitative gap below the Christoffel extremum. It also sharpens the RL-6 denominator-defect budget to a reciprocal-anchor/physical-state sum.

---

## 1. Inherited state and target

RL-6 reduced every admissible compressed k=0 word, including exact saturation boundaries, to

`D | C_good`

plus explicit finite-depth 3-adic boundary gates. Here

`D = 2^A - 3^L > 0`.

The boundary bookkeeping is therefore no longer the global obstruction. The remaining problem is to prevent the affine-cycle numerator from acquiring the full odd factor `D`.

RL-7 attacks that problem by mixing the denominator with the **combinatorics of the whole word**, rather than applying further local 2-adic or 3-adic tests.

---

## 2. RL-L46 — least-anchor prefix/suffix sandwich and reciprocal defect

Write one RL-6 compressed transition as

`W_(j+1) = a_j W_j + e_j`,

where

`a_j = 3^(h_j) / 2^(h_j+t_j)`,

`e_j = (2/3)^(mu_(j+1)) (1-2^(-t_j))`,

and over one cycle

`rho = prod a_j = 3^L / 2^A < 1`,

`delta = 1-rho = D/2^A`.

Rotate the rational candidate orbit so that

`W_0 = min_j W_j`.

For `1 <= j < P` define the prefix and suffix products

`A_j = prod_(i=0)^(j-1) a_i`,

`B_j = prod_(i=j)^(P-1) a_i`,

so `A_j B_j = rho`.

The prefix composition has a positive additive part:

`W_j = A_j W_0 + E_j`, `E_j>0`,

hence

`A_j < W_j/W_0`.                                            (R46.1)

The closing suffix also has a positive additive part:

`W_0 = B_j W_j + F_j`, `F_j>0`,

hence

`B_j < W_0/W_j`.                                            (R46.2)

Multiplying (R46.2) by `A_j W_j/W_0` and using `A_jB_j=rho` gives the two-sided sandwich

`rho * W_j/W_0 < A_j < W_j/W_0`.                            (R46.3)

Equivalently,

`1 < W_j/(A_j W_0) < 1/rho`.                                (R46.4)

Thus every proper prefix, not just the whole word, is squeezed into the same global multiplicative defect window.

### Reciprocal defect refinement

The exact closing identity is

`delta W_0 = sum_(i=0)^(P-1) e_i B_(i+1)`,                  (R46.5)

where `B_(i+1)=prod_(k=i+1)^(P-1) a_k` and the closing factor for `i=P-1` is `1`.

For `i<P-1`, (R46.2) at `j=i+1` gives

`B_(i+1) < W_0/W_(i+1)`.

Therefore

`delta < e_(P-1)/W_0 + sum_(i=0)^(P-2) e_i/W_(i+1)`         (R46.6)

and, since every `0<e_i<1`,

`delta < sum_(j=0)^(P-1) 1/W_j`.                            (R46.7)

This is strictly sharper than RL-6's uniform `delta<P/W_0` whenever the orbit rises appreciably above its least anchor.

For an actual physical plateau start `y_j`, with

`y_j+1 = 2^(n_j-mu_j) 3^(mu_j) q_j`,

`W_j = 2^(n_j)q_j`,

one has the exact conversion

`e_(j-1)/W_j = (1-2^(-t_(j-1)))/(y_j+1)`.                  (R46.8)

Hence the defect is bounded by a reciprocal sum over actual cycle states:

`delta < sum_j (1-2^(-t_(j-1)))/(y_j+1)`

`      < sum_j 1/(y_j+1)`.                                  (R46.9)

If the `P` plateau starts are sorted increasingly and the least is `R#`, they are distinct odd integers, so

`y_(j)+1 >= R#+1+2j`.

Consequently

`delta < sum_(j=0)^(P-1) 1/(R#+1+2j)`.                     (R46.10)

A convenient analytic relaxation is

`delta < 1/(R#+1) + (1/2) log(1+2(P-1)/(R#+1))`.            (R46.11)

At the closing edge, `t_close` is odd by RL-5, hence `e_close=1-2^(-t_close)>=1/2`. RL-6's lower defect estimate therefore also yields

`delta > 1/(2(R#+1))`.                                      (R46.12)

If the closing anchor exponent satisfies `n_close>=2`, strict-high forces `t_close>=3`, improving this branch to

`delta > 7/(8(R#+1))`.                                      (R46.13)

**Status: PROVED ANALYTIC THEOREM.**

### Limitation

(R46.10) is useful only if the number and heights of plateaus can also be controlled. A lower bound on `P` does not help an upper reciprocal sum. This is a sharpening, not a closure.

---

## 3. RL-L47 — rotation-invariant residual denominator

RL-6 uses cleared affine transitions

`d_j W_(j+1) = ell_j W_j + c_j`

and cyclic numerators `C_j` satisfying

`W_j = C_j/(6^M D)`.

Transport of the composed numerator across one edge has the exact form

`d_j C_(j+1) = ell_j C_j + c_j (6^M D)`.                    (R47.1)

Reduce modulo `D`:

`d_j C_(j+1) == ell_j C_j (mod D)`.                          (R47.2)

Every `d_j` and `ell_j` is a product of powers of `2` and `3`. But

`gcd(D,6)=1`,

because `D` is odd and `D == +/-1 (mod 3)`. Thus `d_j` and `ell_j` are units modulo `D`. It follows that

`gcd(C_(j+1),D)=gcd(C_j,D)`.                                 (R47.3)

So the quantity

`g = gcd(C_j,D)`                                              (R47.4)

is independent of rotation.

When the RL-6 boundary gates pass, each rotation has the exact numerator signature

`v2(C_j)=M+n_j`, `v3(C_j)=M`.

Therefore `6^M | C_j`. Put

`Cbar_j=C_j/6^M`.

Because `6^M` is a unit modulo `D`,

`gcd(Cbar_j,D)=g`.                                           (R47.5)

The rational anchor candidate reduces to

`W_j=Cbar_j/D`,

whose reduced odd denominator is therefore the same at every rotation:

`D_res = D/g`.                                               (R47.6)

Thus the RL-6 scalar obstruction has the equivalent form

`D | C_good  <=>  D_res=1`.                                  (R47.7)

**Status: PROVED ANALYTIC THEOREM.**

### Strategic interpretation

A failed word does not fail at one unlucky rotation. It carries a single global residual odd denominator through the entire cyclic anchor orbit. Any future descent theorem can therefore target `D_res` rather than a particular huge numerator.

---

## 4. RL-L48 — repeated compressed words descend to the primitive block

Let a compressed block `V` induce the positive affine map

`f_V(W)=rho_V W+E_V`, `E_V>0`.

Suppose the cyclic symbolic word is the exact repetition `V^m`, `m>=2`. Since the full cycle has `D>0`,

`rho_V^m<1`, hence `rho_V!=1`.

The fixed point of the repeated map is

`Fix(f_V^m) = E_V(1+rho_V+...+rho_V^(m-1))/(1-rho_V^m)`

`           = E_V/(1-rho_V)`

`           = Fix(f_V)`.                                    (R48.1)

Thus the rational orbit determined by `V^m` already closes after `V`; it cannot have primitive symbolic period `m|V|`.

**Status: PROVED ANALYTIC THEOREM.**

This explains the repeated trivial `W=2` survivors in the inherited small compressed search and lets future finite work quotient exact repetitions before doing expensive arithmetic.

---

## 5. Full-map parity numerator and the mixed transposition invariant

For the shortcut Collatz map

`phi(x)=x/2` for even `x`,

`phi(x)=(3x+1)/2` for odd `x`,

let `d=(d_1,...,d_A)` be a full parity word with exactly `L` ones. Let

`r_i(d)=sum_(j=i+1)^A d_j`.

The standard cycle numerator is

`Q(d)=sum_(i=1)^A 2^(i-1) 3^(r_i(d)) d_i`,                  (R49.1)

and a periodic candidate based at that rotation is

`x=Q(d)/D`, `D=2^A-3^L`.                                    (R49.2)

This is the full-map counterpart of the compressed `D | C_good` obstruction.

---

## 6. RL-L49 — a unit-edge obstruction in the transposition graph

Take two parity words with the same `(A,L)` which differ only by one adjacent transposition

`d  = [u,1,0,v]`,

`d' = [u,0,1,v]`.

Let `|u|=a` and let `b` be the number of ones in `v`. Directly from (R49.1),

`Q(d')-Q(d)=2^a 3^b`.                                       (R49.3)

Because `gcd(D,6)=1`,

`gcd(Q(d')-Q(d),D)=1`.                                      (R49.4)

Therefore, whenever `D>1`, it is impossible that both words are `D`-divisible:

`D|Q(d)` and `D|Q(d')` cannot both hold.                     (R49.5)

Equivalently, the set

`S_(A,L)={d : D|Q(d)}`

is an **independent set** in the graph whose edges are adjacent `10 <-> 01` transpositions.

The only case `D=1` is `(A,L)=(2,1)`: if `L>=2` is even, `3^L+1 ==2 (mod 8)`; if `L>=3` is odd, `3^L+1 ==4 (mod 8)` but exceeds `4`; and `L=1` gives `2^A=4`. Thus the unit-edge obstruction applies to every nontrivial cycle parameter pair.

**Status: PROVED ANALYTIC THEOREM.**

### Why this matters

This is the first RL-7 obstruction that mixes the denominator `D` with a genuinely global word operation. Local 2-adic and 3-adic signatures do not see primes dividing `D`; an adjacent transposition does, because it changes the global numerator by a guaranteed unit modulo every prime divisor of `D`.

### What is still missing

To turn (R49.5) into a contradiction, one must force **two words known independently to be `D`-divisible** into a single transposition edge, or force a short transposition path whose weighted unit sum cannot vanish modulo `D`. Rotations of a genuine cycle are all `D`-divisible, so the most promising version is to use the RL root departure/return grammar to constrain the transposition distance between two distinguished rotations.

---

## 7. RL-L51 — one-edge self-rotations are exactly primitive Christoffel classes

RL-L49 suggested trying to force two distinguished cycle rotations to differ by one adjacent transposition. That case can now be classified completely.

Let `d` be a nonconstant binary word of length `A` with `L` ones, and suppose for some nonzero cyclic shift `m` that `d` and `tau^m(d)` differ only by swapping one cyclically adjacent `10` and `01` pair.

Use indices modulo `A` and put

`z_i=d_i-d_(i+m)`.

All `z_i` vanish except at the two adjacent defect positions, where the values are `+1` and `-1`.

The permutation `i -> i+m` decomposes the indices into `gcd(A,m)` cycles. On each such cycle the telescoping sum of `z_i=d_i-d_(i+m)` is zero. Since the two nonzero defects are at adjacent natural indices, they can lie in the same `m`-orbit only if

`gcd(A,m)=1`.                                                (R51.1)

Hence `i -> i+m` is one cycle through all positions. Along this cyclic `m`-ordering the bit value can change only at the two defects. Therefore the set `S` of one-positions is one contiguous block in the `m`-ordering:

`S={a, a+m, ..., a+(L-1)m} (mod A)`                         (R51.2)

for some `a`.

Rotating the word by `m` shifts this block by one `m`-step. Its symmetric difference consists of the two endpoints

`a+(L-1)m` and `a-m`.

By hypothesis those endpoints are adjacent in the ordinary cyclic order, so

`L m == +/-1 (mod A)`.                                      (R51.3)

In particular

`gcd(A,L)=1`.                                                (R51.4)

Let `u=L^(-1) (mod A)`. After a rotation, (R51.2)-(R51.3) say that the one-set is

`{0, -u, -2u, ..., -(L-1)u}`

or its translate/reflection.

Now consider the standard Christoffel positions, in zero-based indexing,

`p_k=floor(k A/L)`, `0<=k<L`.

Write

`r_k=kA-p_k L`, `0<=r_k<L`.

Because `gcd(A,L)=1`, the `r_k` run through `0,...,L-1`. Modulo `A`,

`p_k L == -r_k`,

so

`{p_k}={-j u (mod A):0<=j<L}`.                              (R51.5)

Thus `d` is a rotation of the primitive Christoffel word.

Conversely, when `gcd(A,L)=1`, (R51.5) writes the Christoffel one-set as one consecutive block in the step `m=-L^(-1) (mod A)`. Shifting by `m` changes only its two endpoints, and `Lm==-1 (mod A)` makes those endpoints naturally adjacent. Hence a primitive Christoffel word has a nontrivial rotation differing by one cyclic adjacent transposition.

Therefore

`one-edge self-rotation  <=>  primitive Christoffel rotation class`.   (R51.6)

**Status: PROVED ANALYTIC THEOREM.**

### Consequence for the Rank-1 strategy

The hoped-for single-edge contradiction is not a new family beyond the Christoffel extremal case: forcing two rotations to be one transposition apart is equivalent to forcing the whole parity word into a primitive Christoffel class. Future transposition work must therefore target paths of length at least two, or a total weighted path obstruction.

---

## 8. RL-L52 — internal exclusion of Christoffel parity words from primitive nontrivial integer cycles

The standard numerator divisibility is itself rotation-invariant. If the first bit of `d` is `0`,

`2 Q(tau d)=Q(d)`.                                          (R52.1)

If the first bit is `1`,

`2 Q(tau d)=3Q(d)+D`.                                       (R52.2)

Since `D` is odd, either relation implies

`D|Q(d)  <=>  D|Q(tau d)`.                                  (R52.3)

Now suppose a primitive Christoffel word with `gcd(A,L)=1` satisfied `D|Q`. By RL-L51 it has a rotation differing by one cyclic adjacent transposition. Rotate both words jointly so the differing pair is an ordinary internal adjacent pair. By (R52.3) both words are `D`-divisible, while RL-L49 says two such adjacent words cannot both be `D`-divisible for `D>1`. Contradiction.

If `g=gcd(A,L)>1`, the Christoffel word is exactly the `g`-fold repetition of the primitive Christoffel word with parameters `(A/g,L/g)`, because its defining ceiling differences are periodic with period `A/g`. Such a parity word cannot represent a primitive cycle: the affine map of the shorter block has the same fixed point as its `g`th iterate, exactly as in RL-L48.

The only `D=1` parameter pair is `(A,L)=(2,1)`, the trivial `1 <-> 2` parity cycle.

Therefore:

> **No primitive nontrivial positive integer Collatz cycle can have a Christoffel parity word (up to rotation).**

This conclusion is now internal to the RL chain; Knight's high-cycle theorem is no longer needed to exclude the extremal class for the purpose of RL-L50.

**Status: PROVED ANALYTIC THEOREM.**

---

## 9. RL-L50 — quantitative gap below the Christoffel extremum

This section derives an explicit gap, rather than merely a strict inequality.

For fixed `(A,L)`, let `d*` denote the Christoffel word with one positions

`i_k* = 1 + floor((k-1)A/L)`, `1<=k<=L`.                    (R50.1)

Let

`Q_min(d)=min_rotation Q(rotation(d))`.

Choose a rotation `d^c` minimizing the position sum

`S(d)=sum_(i=1)^A i d_i`

among all rotations. Let `P_m` be the number of ones in the first `m` positions of `d^c`. Rotating those `m` symbols to the end changes the position sum by

`S(tau^m d^c)-S(d^c)=A P_m-mL`.

Minimality therefore gives

`P_m >= mL/A` for every `m`.

If the kth one of `d^c` occurs at position `i_k^c`, take `m=i_k^c-1`. Then `P_m=k-1`, so

`i_k^c <= 1+floor((k-1)A/L)=i_k*` for every `k`.             (R50.2)

Starting with the last one and working leftward, move each kth one right from `i_k^c` to `i_k*`. The already placed later ones lie strictly to the right, so this is a valid sequence of adjacent `10 -> 01` transpositions taking `d^c` to `d*`.

If the rotation class of `d` is not Christoffel, at least one move is required. The first one already occupies position `1`, so some moved one has index `k>=2`. Consider the **last** unit move of that kth one into its Christoffel position. At that moment it moves from `i_k*-1` to `i_k*`, while the `L-k` later ones are already to its right. By RL-L49 the increase contributed by this single move is

`G_k = 2^(i_k*-2) 3^(L-k)`

`    = 2^(floor((k-1)A/L)-1) 3^(L-k)`.                      (R50.3)

Put `x=(k-1)A/L`. Since `floor(x)>=x-1`,

`2^(floor(x)-1) >= 2^(x-2)`.                                (R50.4)

The cycle-slope condition `2^A>3^L` is equivalent to

`A/L > log_2 3`.

Therefore

`2^x > 3^(k-1)`.                                            (R50.5)

Combining (R50.3)-(R50.5),

`G_k > 3^(L-1)/4`.                                          (R50.6)

All other transpositions also increase `Q`, and

`Q_min(d) <= Q(d^c)`.

Thus every non-Christoffel rotation class obeys the explicit strict gap

`Q_min(d) < Q(d*) - 3^(L-1)/4`.                             (R50.7)

This is stronger than the qualitative statement that Christoffel is the unique maximizer.

### Bounding the Christoffel numerator itself

By (R50.1),

`Q(d*) = sum_(k=1)^L 2^(floor((k-1)A/L)) 3^(L-k)`

`      <= sum_(k=1)^L 2^((k-1)A/L) 3^(L-k)`

`      = (2^A-3^L)/(2^(A/L)-3)`

`      = D/(2^(A/L)-3)`.                                    (R50.8)

If a non-Christoffel integer cycle has least element `R#`, then `Q_min=R# D`, so (R50.7)-(R50.8) give

`R# < 1/(2^(A/L)-3) - 3^(L-1)/(4D)`.                        (R50.9)

Now put

`Lambda = A log 2 - L log 3 >0`.

Since

`2^(A/L)=3 exp(Lambda/L)`,

`D=3^L(exp(Lambda)-1)`,

(R50.9) becomes

`R# < 1/[3(exp(Lambda/L)-1)]`

`     - 1/[12(exp(Lambda)-1)]`.                             (R50.10)

**Status: PROVED ANALYTIC THEOREM for non-Christoffel classes; RL-L52 makes the resulting cycle bound internal for every primitive nontrivial cycle.**

### Internal extension to every hypothetical primitive nontrivial integer cycle

RL-L52 now excludes the Christoffel rotation class internally. Therefore every hypothetical primitive nontrivial positive integer cycle lies in the non-Christoffel branch, and (R50.9)-(R50.10) apply **without any external high-cycle theorem**.

The July 2026 Fernández-Ibáñez preprint independently proves the qualitative Christoffel extremality of `Q_min`, and Knight's 2026 published high-cycle result gives a related non-integrality theorem. These are now literature cross-checks rather than dependencies of the RL-7 proof chain.

### Limitation: the explicit penalty is too small by itself

For small `Lambda`,

`1/[3(exp(Lambda/L)-1)] ~ L/(3 Lambda)`,

while

`1/[12(exp(Lambda)-1)] ~ 1/(12 Lambda)`.

So the new penalty is only about

`1/(4L)`

of the leading Christoffel bound. Since any hypothetical nontrivial cycle has enormous `L`, this correction alone cannot eliminate the first continued-fraction candidates.

As a diagnostic, using the inherited external least-counterexample floor `R#>=2^71`, the first upper convergent to `log_2 3` meeting the classical approximation window is

`A/L = 217,976,794,617 / 137,528,045,312`.

At that pair,

`Lambda ~= 8.9865487086e-13`,

classical Christoffel bound `~=5.1012555828807e22`,

RL-L50 penalty `~=9.2731187506e10`.

The penalty is mathematically real but far too small to exclude the candidate.

---

## 10. Finite verification certificate

New verifier:

`tools/verify_rl7_mixed_invariants.py`

It passed exactly and reported:

- 22,924 prefix/suffix sandwich checks;
- 8,073 reciprocal-defect checks;
- 8,073 rotation-gcd checks;
- 20,481 adjacent-transposition identity checks;
- 16,560 unit-edge obstruction checks;
- all 17 admissible `(A,L)` pairs with `A<=14` in the cycle-slope strip checked for Christoffel maximality;
- 958 non-extremal rotation classes checked against the strict quantitative gap;
- 975 binary rotation classes audited in that strip;
- 1,050 exact repeated-affine fixed-point descent checks;
- 8,166 exhaustive one-edge/primitive-Christoffel classification checks through word length 12;
- 694 primitive Christoffel `D`-divisibility exclusions and 669 nonprimitive Christoffel repetition checks through length 60;
- the only `D=1` pair with `A,L<80` is `(2,1)`.

The finite checks are audits of the algebra, not substitutes for the analytic proofs.

---

## 11. Strongest current proof architecture

After RL-7 the k=0 branch can be organized as follows.

1. **Compressed realization:** RL-L44 says a candidate word needs `D|C_good` plus its finite boundary gates.
2. **Residual denominator:** RL-L47 turns this into `D_res=1`, invariant under rotation.
3. **Primitive reduction:** RL-L48 removes exact symbolic repetitions.
4. **Mixed word arithmetic:** RL-L49 says `D`-divisible words cannot be adjacent under a single parity transposition.
5. **Self-edge classification:** RL-L51 identifies one-edge self-rotations exactly with primitive Christoffel classes.
6. **Internal extremal exclusion:** RL-L52 rules Christoffel parity words out of every primitive nontrivial integer cycle.
7. **Global extremal distance:** RL-L50 then gives every hypothetical nontrivial cycle an explicit loss of more than `3^(L-1)/4` below the Christoffel numerator ceiling.
8. **Root endpoint grammar:** inherited RL-L27 and RL-L36 specify a dense initial root block and an exact 3-adic closing return address.
9. **Near resonance:** RL-L46 and RL-L45 bound the denominator defect from both sides using the least anchor.

The unresolved step is to make items 4-7 collide.

---

## 12. Next theorem targets

### Target A — weighted multi-edge obstruction between distinguished rotations

RL-L51 shows that a **single** self-rotation transposition is exactly the primitive Christoffel case, already eliminated internally by RL-L52. So the next genuinely new target starts at path length two.

For an actual cycle every rotation numerator is divisible by `D`. Use the forced root prefix and exact final-return suffix to connect two distinguished rotations by a short **monotone or sign-controlled** transposition path and prove that its exact weighted numerator change lies strictly between `0` and `D`. That would contradict divisibility without collapsing back to the Christoffel case.

### Target B — quantify **many** forced Christoffel defects

RL-L50 charges only one local correction. To become competitive with the leading term, the number/weight of forced corrections must scale like `L`. Seek a theorem that the RL root/xi grammar forces positive-density displacement from the Christoffel word. A linear number of corrections could turn the `1/(4L)` relative penalty into an order-one penalty.

The hard subbranch is expected to be `s=v2(R#+1)=2`, because the root parity prefix then begins `110...`, exactly matching the critical Christoffel prefix near slope `log_2 3`.

### Target C — residual-denominator descent through a cyclotomic factor

Let `g=gcd(A,L)`. If `g>1`,

`D=(2^(A/g))^g-(3^(L/g))^g`

has the proper factor

`D_0=2^(A/g)-3^(L/g)`.

Since `D|Q` implies `D_0|Q`, test whether the root endpoint grammar forces the parity word to descend modulo `D_0` to a shorter admissible word. RL-L48 would then rule out primitive cycles. No such descent theorem is proved yet.

### Target D — exploit the stronger closing-defect lower bound

Branch on the final anchor exponent. For `n_close>=2`, RL-L46 gives the much stronger

`D/2^A > 7/[8(R#+1)]`.

Combine this with the exact final-return discrete-log class modulo `2*3^(n_close-1)` and continued-fraction residue data. Treat `n_close=1` separately; it contains the universal inverse branch `t=1` and is likely the true hard case.

---

## 13. Guardrails

- **RL is still open.** None of RL-L46--RL-L50 proves the Collatz conjecture or rules out every nontrivial cycle.
- Do not treat the current 2026 Christoffel preprint as a black-box proof inside the canonical chain. RL-L50--RL-L52 are now internally proved; Fernández-Ibáñez and Knight are literature cross-checks only.
- Do not enlarge brute-force compressed searches without testing one of Targets A-D.
- Do not multiply local probabilistic/Haar costs as if plateau events were independent.
- Keep `k>0` separate; RL-7 concerns the k=0 cycle obstruction.

---

## 14. External references consulted

1. Carlos Fernández and Santiago Ibáñez, **Christoffel Words as Extremal Structures in Collatz Dynamics**, arXiv:2607.24844v1, 24 July 2026. The paper defines the parity functional, proves Christoffel extremality, and notes the connection to Knight high cycles.  
   https://arxiv.org/abs/2607.24844
2. Kevin Knight, **Collatz high cycles do not exist**, *Discrete Mathematics* 349 (2026), Article 114812, DOI 10.1016/j.disc.2025.114812.  
   https://www.sciencedirect.com/science/article/abs/pii/S0012365X25004200
3. Christian Hercher, **There are no Collatz m-Cycles with m <= 91**, *Journal of Integer Sequences* 26 (2023), with journal corrigendum dated 2026.  
   https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html
4. David Barina, **Improved verification limit for the convergence of the Collatz conjecture**, *The Journal of Supercomputing* (2025): computational verification through `2^71`.  
   https://link.springer.com/article/10.1007/s11227-025-07337-0

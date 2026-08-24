# Collatz R# RL-5 — Plateau Anchor Return Map, Exit-Direction Grammar, and Root Return Address

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-4 seed  
**Verdict:** RL remains open. The k=0 plateau grammar now has a canonical deterministic anchor map, an almost deterministic next-valuation law, a one-integer-wide xi-direction ambiguity, an exponential local cost for saturated exits, an exact 3-adic discrete-log address for the final return, and—new in this continuation—an exact multiplicative-ceiling recurrence plus a common-denominator/all-rotation integrality formula. The composed numerator is 2-adically triangular, while genuinely nontrivial 3-adic numerator cancellation is confined to exact saturation-boundary exits `v3(2^t-1)=n`. The exceptional one-plateau boundary is closed using the accepted Hercher m>=92 external input. For k>0, repeated relative crossings are rigidly controlled by the integer cumulative exponent difference through reverse depth 2R#.

## 1. Reproduction

The inherited RL-4 verifier passes unchanged.

The new verifier

`tools/verify_rl5_anchor_grammar.py`

also passes. It audits exact finite consequences of the analytic statements below. It does not prove that nontrivial Collatz cycles do not exist.

## 2. RL-L31 — every physical plateau has a canonical red anchor

Let `y` be a cycle state at the start of a compressed exponent-1 plateau and write

`y+1 = 2^s 3^mu q`,

where `s=v2(y+1)>=1`, `mu=v3(y+1)>=0`, and `gcd(q,6)=1`. As in RL-L28 set

`n=s+mu`,

`W=xi(y)=2^n q`.

Define the **anchor**

`u=W-1=xi(y)-1=2^n q-1`.      (R31.1)

By RL-N1,

`u=B^mu(y)`,

so `u` is red and `u>=R#`. Moreover

`v3(u+1)=0`,

and applying exactly `mu` accelerated exponent-1 moves to `u` reaches `y`. In `+1` coordinates,

`u_j+1 = 2^(n-j) 3^j q`, `0<=j<=mu`,

so `u_mu=y`.

The full canonical neutral run from `u` has exactly `n-1` exponent-1 moves. Its exit parameter is

`t=v2(3^n q-1)`,

and its exit state is

`z=(3^n q-1)/2^t`.      (R31.2)

This is exactly the same exit obtained by starting at the physical plateau state `y` and taking its remaining `s-1` exponent-1 moves.

Thus the physical plateau is merely a suffix of a unique canonical neutral run beginning at `u`.

Define

`F(u)=xi(z)-1`.      (R31.3)

The compressed xi-level sequence of a k=0 cycle is therefore a genuine deterministic orbit of the induced anchor map `F`:

`u_j=W_j-1`, `u_(j+1)=F(u_j)`.

In particular the root plateau has anchor

`u_0=R#`.

**Status: PROVED ANALYTIC THEOREM.**

### Strategic consequence

The k=0 state no longer needs both a physical plateau start and a free xi level. The canonical state is an anchor `u` with `v3(u+1)=0`, or equivalently `(n,q)` with `u+1=2^n q`; the physical plateau start is only a position `mu` along that anchor's neutral run.

## 3. RL-L32 — exact next-valuation/reset law

Continue with one anchor transition. Put

`r=v3(2^t-1)`

and

`mu'=v3(z+1)`.

Since

`z+1 = (3^n q + 2^t-1)/2^t`,

the next 3-adic valuation is determined as follows:

- if `r<n`, then `mu'=r`;
- if `r>n`, then `mu'=n`;
- if `r=n`, write
  `h=(2^t-1)/3^n`; then
  `mu'=n+v3(q+h)`.      (R32.1)

For `t` odd, `r=0`. For `t` even, LTE gives

`r=1+v3(t/2)`.      (R32.2)

Therefore

`mu'=0  <=>  t is odd`.      (R32.3)

So the exit parity is an exact 3-adic reset bit: odd `t` resets the next anchor-normalization position to `mu'=0`; even `t` forces `mu'>=1`.

### Saturated exits

Call an exit **3-adically saturated** if `r>=n`. Then `t` must be even and

`2*3^(n-1) | t`,      (R32.4)

hence

`t >= 2*3^(n-1)`.      (R32.5)

This is far stronger than the RL-4 diagnostic category `t>=n`.

The equality/cancellation case `r=n` can raise `mu'` above `n`, but only after this exponential divisibility cost has already been paid.

**Status: PROVED ANALYTIC THEOREM.**

## 4. RL-L33 — the xi direction has only a one-integer critical strip

Let

`W=u+1=2^n q`,

`W'=F(u)+1=xi(z)`,

and define

`h=n-mu'`.

The exact RL-L30 transition ratio can be written

`W'/W = (3/2)^h * 2^(-t) * (1+eta)`,      (R33.1)

where

`eta=(2^t-1)/(3^n q)`.      (R33.2)

Because `3^n q-1` is a positive multiple of `2^t`,

`0<eta<1`.      (R33.3)

Thus the multiplicative error contributes strictly between zero and one bit.

### Case h<=0

If `h<=0`, then

`W'<W`.      (R33.4)

So every saturated/cancellation transition with `mu'>=n` is automatically an xi descent.

### Case h>0

There are exactly three regimes:

1. **low:**
   `2^(h+t)<3^h`  
   implies `W'>W`;

2. **supercritical:**
   `2^(h+t-1)>3^h`  
   implies `W'<W`;

3. **critical strip:**
   `2^(h+t-1)<3^h<2^(h+t)`.      (R33.5)

Because `t` is integral and `log2(3/2)` is irrational, the critical strip contains exactly the single value

`t=ceil(h log2(3/2))`.

In that critical case the sign is decided by the unit `q`. Precisely,

`W'-W`

has the sign of

`(2^t-1) - 3^(mu') (2^(h+t)-3^h) q`.      (R33.6)

So RL-4's coarse split into “regular-high or deep” is no longer the right direction state. The exact direction grammar is:

- saturated (`h<=0`) -> forced descent;
- low -> forced rise;
- supercritical -> forced descent;
- one critical `t` -> one explicit unit inequality.

**Status: PROVED ANALYTIC THEOREM.**

## 5. RL-L34 — exact cylinder cost and a universal half-depth descent cost

For fixed `n` and `t`, exactness of

`t=v2(3^n q-1)`

is equivalent to one 2-adic unit cylinder:

`q = 3^(-n)(1+2^t)  (mod 2^(t+1))`.      (R34.1)

Conditional on odd `q`, this cylinder has normalized 2-adic Haar mass

`2^(-t)`.      (R34.2)

This is a local density statement only; no independence between different cycle plateaus is assumed.

### Exact mass of saturation

From RL-L32, saturation at depth `n` is equivalent to

`M_n=2*3^(n-1) | t`.

Hence the total normalized 2-adic mass of saturated exits at fixed `n` is exactly

`sum_(j>=1) 2^(-j M_n)`

`= 1/(2^(M_n)-1)`

`= 1/(2^(2*3^(n-1))-1)`.      (R34.3)

Thus genuine 3-adic saturation is exponentially sparse in `3^n`.

### Cancellation depth at r=n

When `r=n`, put

`h=(2^t-1)/3^n`,

which is a 3-adic unit, and let

`c=v3(q+h)`.

For `q` Haar-uniform among 3-adic units,

`P(c=0)=1/2`,      (R34.4)

and for every `ell>=1`,

`P(c=ell)=3^(-ell)`.      (R34.5)

Again this is a local cylinder law, not a cycle-wide independence assertion.

### Universal half-depth cost for any non-rise

A stronger deterministic statement holds:

`W'<=W  =>  2t>=n`.      (R34.6)

Proof. Suppose `2t<n`; then `n>=2t+1`. By RL-L32, a saturated exit would satisfy `t>=2*3^(n-1)>=n/2`, so saturation is impossible here. Hence `r<n` and `mu'=r`.

If `t` is odd, `r=0`. If `t` is even, write

`r=1+v`, `v=v3(t/2)`.

For `v>=1`, `t>=2*3^v`, and the elementary inequality

`7v < 4*3^v <= 2t`

holds; it is also trivial for `v=0`. Hence

`7r < 2t+7`.

Using `n>=2t+1`,

`7(n-r) > 12t`,

so

`t < (7/12)(n-r)`.      (R34.7)

Finally

`log2(3/2) > 7/12`

because

`3^12 > 2^19`.

Therefore

`t < (n-r) log2(3/2)`,

which lies in the forced-rise regime of RL-L33. Contradiction.

Consequently the entire local 2-adic mass of exits that can possibly satisfy `W'<=W` is at most

`sum_(t>=ceil(n/2)) 2^(-t)`

`= 2^(1-ceil(n/2))`.      (R34.8)

**Status: PROVED ANALYTIC THEOREM / EXACT LOCAL HAAR LAW.**

## 6. RL-L35 — the one-plateau boundary and anchor fixed points reduce to one-local-minimum cycles

RL-4 left the boundary `s=L` as the equation

`(2^(s+t)-3^s)q=2^t-1`.

There is a cleaner structural interpretation. If `s=L`, the accelerated odd cycle has exactly `s-1` exponent-1 moves and one exponent `t+1>=2`. Every exponent-1 move strictly raises a positive odd state greater than 1, while the unique `>=2` move is the sole descending passage. Therefore this is a Collatz cycle with exactly one local minimum.

The accepted external result RL-E3 states that every nontrivial Collatz cycle has at least 92 local minima. Hence the boundary `s=L` is excluded.

The same reduction removes anchor fixed points. If

`F(u)=u`,

then, writing `mu'=v3(z+1)`, RL-N1 gives

`B^(mu')(z)=u`,

so the forward orbit from `u` reaches `z` through `mu'` exponent-1 moves. But the canonical anchor run reaches the same `z` after `n-1` exponent-1 moves followed by its single exit. The exact initial run length forces `mu'<n`; therefore `z` lies on that neutral run, and the segment from `z` through the remaining 1-run and the single exit back to `z` is again a one-local-minimum cycle.

Thus, under RL-E3,

`F(u)!=u`      (R35.1)

for every anchor belonging to a hypothetical nontrivial RL cycle. Equivalently, consecutive compressed xi levels are never equal:

`W_(j+1)!=W_j`.      (R35.2)

This closes the exceptional one-plateau state left open in RL-4.

**Status: PROVED REDUCTION + EXCLUDED BY CANONICAL EXTERNAL INPUT RL-E3.**

## 7. RL-L36 — the final return to R# is an exact realized root xi probe

Let `u=2^n q-1` be the final anchor before the compressed cycle returns to the root anchor

`R#`.

Because the physical exit lands directly at the root plateau start, its next physical state is exactly `R#`, so

`R#=(3^n q-1)/2^t`.      (R36.1)

Equivalently,

`2^t R#+1 = 3^n q`,      (R36.2)

where `gcd(q,6)=1`. Hence

`n=v3(2^t R#+1)`.      (R36.3)

By RL-L32 the return has `t` odd, and by RL-L35 its anchor is strictly above the root:

`u>R#`.      (R36.4)

Therefore the final return satisfies the strict high condition

`2^(n+t)>3^n`.      (R36.5)

### Identification with the old side probe

Let

`p=(2^(t+1) R#-1)/3`.

Since `t+1` is even and `R#=1 mod3`, this is the legal root side predecessor with probe exponent `d=t+1`. RL-L16 gives

`xi(p)=2^n(2^t R#+1)/3^n`

`=2^n q`

`=u+1`.      (R36.6)

So the final plateau anchor is not merely compatible with one of the old root probes: it is **exactly the xi-normalized value of the particular side probe selected by the closing cycle rotation**.

Because `u>R#`, this actual realized probe obeys the strict barrier

`xi(p)>=R#+3`.      (R36.7)

This is the cycle coupling that the root-only RL-3 sieve lacked.

### Exact 3-adic discrete-log address of t

For `n>=1`, the order of `2` modulo `3^n` is

`M_n=2*3^(n-1)`.

Thus (R36.2) puts `t` in the unique class

`t=lambda_n(R#)  (mod M_n)`      (R36.8)

satisfying

`2^lambda_n R# = -1  (mod 3^n)`.      (R36.9)

At level `n+1`, the class modulo `M_n` has exactly three lifts modulo

`M_(n+1)=3M_n`,

and exactly one of those three lifts solves the congruence modulo `3^(n+1)`. Since (R36.3) is an **exact** valuation, the actual `t` must occupy one of the other two lift classes. Thus the final return exponent has a nested 3-adic discrete-log address, not just a scalar lower bound.

For `n>=2`, the first nontrivial level gives:

- if `R#=1 mod9`, then `t=3 mod6`;
- if `R#=7 mod9`, then `t=5 mod6`.

(The inherited `R#=4 mod9` branch is already excluded.)

**Status: PROVED ANALYTIC THEOREM.**

## 8. RL-L37 — k>0 repeated-order rigidity through depth 2R#

Return to the strict-preperiod comparison of RL-L23. Put

`C_h=D_h-E_h`

and

`rho_h=log2(x_h/y_h)`.

The exact relative product gives

`x_h/y_h = 2^(C_h) P_h`,      (R37.1)

where every correction factor in `P_h` lies between

`3/(3+1/R#)`

and

`(3+1/R#)/3`.

Set

`K_R=(3R#+1)/(3R#)`.

Then

`K_R^(-h) < P_h < K_R^h`.      (R37.2)

Therefore, whenever

`K_R^h<2`,      (R37.3)

the integer exponent difference already fixes the physical order unless it is zero:

- `C_h>=1  =>  x_h>y_h`;
- `C_h<=-1 =>  x_h<y_h`.      (R37.4)

A universal convenient horizon is

`h<=2R#`.      (R37.5)

Indeed

`2R# log(1+1/(3R#)) < 2/3 < log 2`.

Thus, through reverse depth `2R#`, a multi-crossing automaton does not need a continuous ratio state: away from the zero level, the sign of the integer walk `C_h` is the physical order.

This does not close `k>0`, because the preperiod length is not known to be at most `2R#`. It does, however, extend the RL-L23 first-crossing compression to repeated crossings over a root-proportional exact horizon.

**Status: PROVED ANALYTIC THEOREM.**

## 9. RL-L38 — every anchor transition is an exact multiplicative ceiling

Continue with one transition from

`W=2^n q`

to `W'`, with exit parameter `t` and next normalization valuation `mu'`. Put

`h=n-mu'`.

RL-L33 can be rearranged exactly as

`W' = aW + e`,      (R38.1)

where

`a = 3^h / 2^(h+t)`      (R38.2)

and

`e = (2/3)^(mu') (1-2^(-t))`.      (R38.3)

The formula is interpreted rationally when `h<0`. Since `mu'>=0` and `t>=1`,

`0<e<1`.      (R38.4)

But `W'` is an integer. Therefore `aW` is not an integer and

`W' = ceil(aW)`

`= ceil(3^h W / 2^(h+t))`.      (R38.5)

Thus, once the discrete exit data `(n,t,mu')` are fixed, there is no additional continuous/unit-valued transition error: the next normalized anchor level is the ceiling of one rational multiple of the current level.

Clearing denominators gives an integer affine form valid uniformly even when `h<0`:

`d W' = ell W + c`,      (R38.6)

with

`ell = 2^(mu') 3^n`,

`c = 2^(n+mu') (2^t-1)`,

`d = 2^(n+t) 3^(mu')`.      (R38.7)

**Status: PROVED ANALYTIC THEOREM.**

## 10. RL-L39 — common denominator and all-rotation integrality

Take a cyclic compressed word with transitions

`(n_j,t_j,mu_(j+1))`, `0<=j<P`,

and cyclically put

`s_j=n_j-mu_j >=1`.

Let

`M=sum_j mu_j`,

`L=sum_j s_j`,

`A=L+sum_j t_j`,

`D=2^A-3^L`.      (R39.1)

For a chosen rotation, compose the affine equations (R38.6). Write the result as

`Den_r W_r = Lin_r W_r + C_r`.      (R39.2)

The coefficient products are rotation-independent:

`Den_r = product_j d_j = 6^M 2^A`,      (R39.3)

`Lin_r = product_j ell_j = 6^M 3^L`.      (R39.4)

Hence every rotation has exactly the same denominator defect

`Den_r-Lin_r = 6^M D`.      (R39.5)

A closed compressed orbit therefore forces

`C_r = 6^M D W_r`      (R39.6)

for **every** rotation `r`. Equivalently,

`W_r = C_r / (6^M D)`.      (R39.7)

So a discrete compressed word determines at most one rational candidate anchor at every rotation. There is no free `q_r` left after the word is fixed. A genuine cycle must make all of these rational candidates simultaneously positive integers and must also realize the declared local exact valuations `(n_j,t_j,mu_(j+1))`.

Since

`W_r=2^(n_r) q_r`, `gcd(q_r,6)=1`,

a genuine cycle has the all-rotation numerator signature

`v2(C_r)=M+n_r`,      (R39.8)

`v3(C_r)=M`,          (R39.9)

and

`q_r = C_r / (6^M D 2^(n_r))`      (R39.10)

must be a positive 6-adic unit integer.

This is the requested common-denominator/rotation coupling: local plateau data alone now generate an exact finite divisibility test once a discrete word is specified.

**Status: PROVED ANALYTIC THEOREM.**

## 11. RL-L40 — numerator valuation triangularity localizes the real obstruction

Expand the composed numerator for one rotation as

`C = sum_i T_i`,      (R40.1)

where

`T_i = c_i (product_(k<i) d_k) (product_(k>i) ell_k)`.      (R40.2)

### 2-adic triangularity

Let the rotation start at index `0`. Then

`v2(T_0)=M+n_0`.      (R40.3)

For every `i>=1`, direct subtraction gives

`v2(T_i)-v2(T_0)`

`= sum_(k=1)^i s_k + sum_(k=0)^(i-1) t_k`

`>=2i`.      (R40.4)

Therefore the first term is the unique 2-adically minimal term and

`v2(C)=M+n_0`.      (R40.5)

So the 2-adic part of (R39.8) is **automatic** for every valid cyclic discrete word; it is not an additional global obstruction.

### Where nontrivial 3-adic cancellation can occur

Put

`r_i=v3(2^(t_i)-1)`,

`a_i=r_i-mu_(i+1)`,

`h_i=n_i-mu_(i+1)`.

Then

`v3(T_i)-M = a_i + sum_(k>i) h_k`.      (R40.6)

The local law RL-L32 has only three structural possibilities:

- `r_i<n_i`: `(a_i,h_i)=(0, positive)`;
- `r_i>n_i`: `(a_i,h_i)=(positive,0)`;
- `r_i=n_i`: the exact saturation boundary, where `(a_i,h_i)=(0,0)` without extra cancellation, or `(-c,-c)` when cancellation depth `c>0` occurs.

Suppose **no** transition hits the exact boundary `r_i=n_i`. Since

`sum_i h_i = L >0`,

there is a last index `i*` with `h_(i*)>0`. Equation (R40.6) then gives

`v3(T_(i*))=M`,

while every other term has strictly larger 3-adic valuation. Hence

`v3(C)=M`      (R40.7)

is automatic as well.

Therefore genuinely nontrivial 3-adic numerator cancellation in the common-denominator test is confined to exits satisfying

`v3(2^t-1)=n`.      (R40.8)

By LTE this boundary is equivalent to

`v3(t/2)=n-1`,      (R40.9)

so in particular

`t = 2*3^(n-1) a`, `3 does not divide a`.      (R40.10)

This sharply separates the remaining k=0 arithmetic:

1. **generic words, with no boundary exit:** numerator unit conditions are automatic, so the global obstruction is denominator/all-rotation divisibility plus realization of the local cylinders;
2. **boundary words:** an additional explicit 3-adic cancellation grammar must be satisfied.

This is a useful negative result as well as a reduction: merely checking numerator valuations will not close the generic case.

**Status: PROVED ANALYTIC THEOREM.**

## 12. RL-L41 — generic words reduce to one scalar denominator test

Call a cyclic compressed word **generic admissible** if for every transition

`r_j=v3(2^(t_j)-1) != n_j`,      (R41.1)

`mu_(j+1)=r_j` when `r_j<n_j`, and `mu_(j+1)=n_j` when `r_j>n_j`, with

`s_j=n_j-mu_j>=1`.      (R41.2)

Assume also the cycle slope condition

`D=2^A-3^L>0`.

RL-L40 gives, at every rotation,

`v2(C_r)=M+n_r`,

`v3(C_r)=M`.      (R41.3)

Since `D` is coprime to `6`, the factor `6^M` of the common denominator is therefore already present automatically in every `C_r`.

The rotation numerators satisfy the exact transport identity

`d_j C_(j+1) = ell_j C_j + c_j K`,      (R41.4)

where

`K=6^M D`.      (R41.5)

Modulo `D`, both `d_j` and `ell_j` are units, because they are products of powers of `2` and `3`. Hence

`D | C_j  <=>  D | C_(j+1)`.      (R41.6)

So `D`-divisibility at **one** rotation is equivalent to `D`-divisibility at every rotation.

### Sufficiency, not just necessity

Suppose `D|C_0`. Then by (R41.3) and (R41.6),

`K | C_r`

for every rotation, and therefore

`W_r=C_r/K`

is a positive integer satisfying

`v2(W_r)=n_r`, `v3(W_r)=0`.      (R41.7)

It remains to check that the declared local exit data are not merely formal. The affine equation gives, with `W_j=2^(n_j)q_j`,

`v2(3^(n_j) q_j - 1 + 2^(t_j))`

`= t_j + (n_(j+1)-mu_(j+1))`

`> t_j`.      (R41.8)

Therefore

`v2(3^(n_j)q_j-1)=t_j`.      (R41.9)

Writing

`z_j=(3^(n_j)q_j-1)/2^(t_j)`,

the same affine identity rearranges to

`3^(mu_(j+1)) W_(j+1) = 2^(mu_(j+1)) (z_j+1)`.      (R41.10)

Since `W_(j+1)` is a 3-adic unit and `n_(j+1)>mu_(j+1)`, this forces

`v3(z_j+1)=mu_(j+1)`      (R41.11)

and

`xi(z_j)=W_(j+1)`.      (R41.12)

Thus the declared exits are the **exact** Collatz exits and the integer anchor orbit is genuinely realized.

Consequently, for generic admissible words,

> **a positive periodic anchor orbit exists if and only if `D` divides one rotation numerator `C_r`.**      (R41.13)

All other rotations, the exact 2-/3-adic anchor valuations, and the local exit valuations then follow automatically.

This is the strongest compression of the k=0 generic case so far: a whole periodic anchor word has been reduced to one scalar divisibility test. The exact-boundary words `r_j=n_j` remain outside this equivalence because their 3-adic numerator cancellation is not automatic.

**Status: PROVED ANALYTIC THEOREM.**

## 13. What changed strategically

### k=0

The RL-4 state

`(plateau n, unit q, xi level W, exit t, next valuation)`

can now be compressed further to a deterministic induced anchor orbit

`u -> F(u)`

with:

- `u+1=2^n q`, `v3(u+1)=0`;
- exact 2-adic exit cylinder for `t`;
- almost deterministic `mu'` from `(n,t)`;
- exponential divisibility for saturation;
- a one-integer critical xi-direction strip;
- no fixed anchor in a nontrivial cycle under RL-E3;
- an exact root-side probe/discrete-log address at the final return;
- an exact ceiling recurrence `W_(j+1)=ceil(a_j W_j)`;
- a common denominator `6^M(2^A-3^L)` shared by every rotation;
- uniqueness of the rational anchor candidate for every fixed discrete word;
- automatic 2-adic numerator valuation, with nontrivial 3-adic numerator cancellation localized to exact saturation-boundary exits;
- for generic admissible words, a complete equivalence: one scalar condition `D|C_r` at one rotation is necessary and sufficient to realize the whole periodic integer anchor orbit.

The most important new pair is now a **two-sided root gate**:

- departure from `R#` is the RL-L27 low exit controlled by `v2(3^s q_0-1)`;
- arrival back at `R#` is the RL-L36 high return controlled by `v3(2^t R#+1)` and a nested discrete-log class for `t`.

### k>0

The first-crossing state remains discrete. RL-L37 shows that even repeated physical order is rigidly encoded by `C_h=D_h-E_h` through depth `2R#`, except at `C_h=0`.

## 14. Finite audit

`tools/verify_rl5_anchor_grammar.py` checks:

- 33,333 anchor-normalization instances;
- 26,668 induced-map consistency instances along neutral runs;
- 50,000 exact next-valuation laws;
- 50,000 parity-reset equivalences;
- 4,396 saturated-exit divisibility instances;
- 4,198 cancellation instances;
- 60,000 exact xi-ratio identities;
- 25,193 forced-rise instances;
- 20,988 forced-descent instances;
- 13,819 critical-strip instances with exact unit sign checks;
- 3,078 exact 2-adic exit-cylinder instances;
- exact saturation-mass and cancellation-depth rational checks;
- 34,807 sampled non-rise transitions satisfying `2t>=n`;
- 29 exact geometric half-depth mass identities;
- 8,340 final-return/root-probe identities;
- 8,057 strict final-return high instances;
- 10,000 final-return discrete-log class checks;
- 10,000 exact-valuation lift checks;
- 3,330 mod-9 return-residue checks;
- 249 exact `2R` rigidity-horizon inequalities;
- 121,170 finite same-endpoint relative-order rigidity checks;
- 60,000 exact multiplicative-ceiling identities;
- 60,000 integer affine-transition identities;
- 5,396 common-denominator product identities;
- 2,983 2-adic numerator-triangularity checks;
- 4,143 generic 3-adic unique-minimum checks;
- 75,894 compressed-word candidates in the declared diagnostic domain `P<=3`, `n,t<=6`, cancellation depth `<=2`; only three repetitions of the trivial `W=2` anchor survive, and no nontrivial candidate survives;
- 165,728 generic-admissible cyclic words with `P<=3`, `n,t<=8` tested against the RL-L41 scalar criterion; exactly three `D`-divisible words occur, all repetitions of the trivial `W=2` anchor, giving six exact realized edges and no nontrivial realization in this declared domain.

The inherited RL-4 verifier also passes.

**Status: EXACT FINITE CERTIFICATE for the stated audit domain.**

## 15. Current endpoint

RL is still open.

The common-denominator/rotation coupling requested by RL-4/RL-5 is now explicit, and RL-L41 compresses the **generic** k=0 case all the way to one scalar condition: `D|C_r` at one rotation is necessary and sufficient to realize the full periodic integer anchor orbit. There is no remaining independent all-rotation integrality test in that generic subcase.

The next k=0 theorem must therefore attack `D|C_r` itself. Use the low root departure gate and the high/discrete-log final-return gate to constrain the single numerator modulo `D=2^A-3^L`. A natural target is a denominator descent/lift theorem: prove that these two gates force `C_r !=0 (mod p)` for some prime `p|D`, or prove that every compatible residue lifts into a structured recurrent family and identify the next missing invariant.

Exact saturation-boundary exits `v3(2^t-1)=n` remain a separate subproblem because their 3-adic numerator cancellation can invalidate the generic equivalence until the boundary cancellation grammar is resolved.

For k>0, the next useful extension remains to replace the crude `2R#` rigidity horizon by a cumulative reciprocal-height budget, so that order rigidity can be restarted or transported across long preperiods instead of expiring at a fixed depth.

# RL123 — run-fibre packing globalization, CRT boundary fibres, and low-odd-count frontier

Date: 2026-08-27

## 0. Outcome and classification

RL123 continues the RL122 physical-strip route and obtains a genuine multi-fibre strengthening.

**No Gate A closure, Gate B closure, global nontrivial-cycle exclusion, or Collatz proof is claimed.**

New promoted mathematics/results:

1. **RL123.1 — sharp run-occupancy lower envelope** for fixed run count `t` (analytic).
2. **RL123.2 — depth-sensitive odd/even boundary CRT fibre theorem** (analytic).
3. **RL123.3 — strengthened full-ownership packing inequality** using the CRT fibre floor (analytic).
4. **RL123.4 — parameter-only run-count packing floor `H(L,Z)`** (analytic).
5. **RL123.5 — sliding-window formula for cyclic rotation transport**, including the exact shift-two identity (analytic).
6. **RL123.6 — low-odd-count frontier:** every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L>=10` (mixed: analytic packing plus an exact finite residual certificate of `8,606,677` rooted fixed-content words).

The strongest new structural point is that an odd-to-even run boundary is not merely in a dyadic fibre or a triadic fibre separately. It is in one **CRT fibre modulo `2^k 3^j`**, so distinct physical boundaries of the same depth type are spaced by the product modulus.

RL123 also proves a clean bridge from closest-rotation radius to run/window statistics: cyclic transport to a shift is exactly the `L1` dispersion of the corresponding sliding-window counts around a median.

---

## 1. Incoming authority

Use the frozen RL122 state.

For a hypothetical primitive nontrivial positive ordinary shortcut cycle, let:

- `w=d_0...d_(A-1)` be its cyclic parity word;
- `L=sum d_i`;
- `Z=A-L`;
- `D=2^A-3^L>0`;
- `x_i` be the actual physical cycle states rooted at the rotations;
- `W=max_i x_i-min_i x_i`.

Full ordinary ownership gives

`Q(r_i)=D x_i`.

RL110 supplies the independent fixed-content numerator diameter ceiling

`max_i Q(r_i)-min_i Q(r_i) <= B(A,L)`

with

`B(A,L)=(2^Z-1)(3^L-2^L)`.

Hence

`D W <= B(A,L)`.                                           (1.1)

RL122 supplies the one-fibre physical floors. If the cyclic word has zero-run starts counted by `Z_k` and one-run starts counted by `O_k`, then

`W >= (Z_k-1)2^k+1`                                       (1.2)

for every nonempty zero fibre, and

`W >= (O_k-1)3^k`                                         (1.3)

for every nonempty odd fibre.

The inherited primitive/full-`D` radius-three engine remains a closed **local** theorem only.

---

## 2. Run decomposition

Write the nonconstant cyclic word as alternating positive runs

`1^(o_1) 0^(z_1) 1^(o_2) 0^(z_2) ... 1^(o_t) 0^(z_t)`,

cyclically, where

`sum_i o_i=L`,
`sum_i z_i=Z`.

Thus `t` is both the number of odd runs and the number of zero runs.

For any positive composition `a_1+...+a_t=n`, define

`N_k(a)=sum_i max(a_i-k+1,0)`.

For the odd runs, `N_k(o)=O_k`; for the zero runs, `N_k(z)=Z_k`.

---

## 3. RL123.1 — sharp fixed-`t` run-occupancy envelope

For every `i`,

`max(a_i-k+1,0) >= a_i-(k-1)`.

Summing and using nonnegativity gives

`N_k(a) >= max(n-t(k-1),0)`.                               (3.1)

This lower bound is simultaneously sharp for every `k`: write

`n=qt+r`, `0<=r<t`,

and take the balanced composition with `r` parts `q+1` and `t-r` parts `q`. Direct substitution gives equality in (3.1) for all `k`.

Define

`c(n,t,k)=max(n-t(k-1),0)`.

Then define the fixed-`t` one-fibre floors

`E_0(Z,t)=max_{k:c(Z,t,k)>0} ((c(Z,t,k)-1)2^k+1)`,          (3.2)

`E_1(L,t)=max_{k:c(L,t,k)>0} ((c(L,t,k)-1)3^k)`.            (3.3)

### Theorem RL123.1

Every cyclic binary word with fixed `(L,Z,t)` satisfies

`P(w) >= max(E_0(Z,t),E_1(L,t))`.                          (3.4)

For unrestricted positive run compositions, the right side is the exact simultaneous lower envelope and is attained by balanced zero and one run lengths.

Classification: **analytic**.

### Primitivity precision

Equation (3.4) is a universal lower bound for primitive words as well. RL123 does **not** claim that the unrestricted balanced minimizer is always itself primitive. In the doubly divisible case, fully balanced run lengths can produce a periodic word. Therefore (3.4) is promoted as an exact run-composition envelope and a primitive lower floor, not as a closed formula for every exceptional primitive equality correction.

This is the remaining incompleteness of Priority A; it does not affect the stronger Priority-B theorem below.

---

## 4. RL123.2 — depth-sensitive boundary CRT fibres

Let `b_i` be the physical state at the boundary after the `i`-th odd run and before its following zero run.

If `o_i>=j`, then `b_i` is the endpoint of at least `j` consecutive odd shortcut steps. RL122.2 gives

`b_i == -1 (mod 3^j)`.                                    (4.1)

If `z_i>=k`, then the next `k` shortcut steps are even, so RL122.1 gives

`b_i == 0 (mod 2^k)`.                                     (4.2)

Define

`C_(j,k)(w) = #{ i : o_i>=j and z_i>=k }`.                (4.3)

Every one of these `C_(j,k)` physical boundary states lies in the same CRT class determined by

`x==0 (mod 2^k)`,
`x==-1 (mod 3^j)`.

Because `gcd(2^k,3^j)=1`, this is one residue class modulo

`M_(j,k)=2^k 3^j`.

Primitivity/simple-cycle ownership makes distinct cyclic boundaries distinct physical states. Therefore `C` distinct integers in one residue class modulo `M` have span at least `(C-1)M`.

### Theorem RL123.2 — boundary CRT fibre theorem

For every `j,k>=1` with `C_(j,k)>=1`,

`W >= (C_(j,k)-1) 2^k 3^j`.                               (4.4)

In particular, every odd-to-even boundary has `j=k=1`, so `C_(1,1)=t` and

`W >= 6(t-1)`.                                             (4.5)

Classification: **analytic global ordinary-owned physical theorem**.

This is a genuine multi-fibre gain over RL122: the spacing is the product `2^k3^j`, not the maximum of the separate dyadic and triadic spacings.

---

## 5. RL123.3 — strengthened full-ownership packing inequality

Define

`P_CRT(w)=max_{j,k:C_(j,k)>=1} (C_(j,k)-1)2^k3^j`,         (5.1)

and

`P_plus(w)=max(P(w),P_CRT(w))`.                            (5.2)

By RL122 and RL123.2,

`W>=P_plus(w)`.                                            (5.3)

Combining with full ownership and the RL110 diameter ceiling (1.1):

### Theorem RL123.3

Every hypothetical primitive nontrivial positive ordinary shortcut cycle satisfies

`D P_plus(w) <= (2^Z-1)(3^L-2^L)`.                        (5.4)

Thus any primitive ordinary word with

`D P_plus(w) > (2^Z-1)(3^L-2^L)`

is analytically excluded.

Classification: **analytic global exclusion criterion**.

---

## 6. RL123.4 — parameter-only run-count packing floor

For a word with actual run count `t`, RL123.1 and the coarse CRT boundary fibre (4.5) give

`W >= max(E_0(Z,t),E_1(L,t),6(t-1))`.                     (6.1)

Define

`H(L,Z)=min_{1<=t<=min(L,Z)} max(E_0(Z,t),E_1(L,t),6(t-1))`. (6.2)

### Theorem RL123.4

Every hypothetical primitive nontrivial positive ordinary shortcut cycle satisfies

`W>=H(L,Z)`                                                (6.3)

and hence

`D H(L,Z) <= (2^Z-1)(3^L-2^L)`.                           (6.4)

Classification: **analytic**.

`H` is deliberately conservative: it uses only the universal `j=k=1` CRT boundary family together with the sharp one-fibre fixed-`t` envelopes. Deeper `(j,k)` occupancy can only strengthen it.

---

## 7. RL123.5 — sliding-window formula for cyclic rotation radius

Let `rot_s(w)` denote the left cyclic shift by `s`, and let

`h_i^(s)=sum_{r=1}^s d_(i+r)`                              (7.1)

be the number of ones in the cyclic length-`s` window immediately after edge `i`.

For cyclic adjacent-transposition transport from `w` to `rot_s(w)`, an integer edge flow `f_i` must satisfy

`f_i-f_(i-1)=d_i-d_(i+s)`.                                 (7.2)

But

`h_i^(s)-h_(i-1)^(s)=d_(i+s)-d_i`,

so every integer solution is

`f_i=c-h_i^(s)`                                            (7.3)

for an integer circulation constant `c`.

The exact cyclic adjacent-transposition distance is the minimum `L1` flow norm. Therefore:

### Theorem RL123.5 — window-dispersion rotation formula

`dist_cyc(w,rot_s(w)) = min_{c in Z} sum_i |h_i^(s)-c|`.   (7.4)

Equivalently, `c` may be taken to be any median of the sliding-window counts.

Classification: **analytic combinatorial theorem**.

### Shift two

For `s=2`, the window counts lie in `{0,1,2}`. Their multiplicities are:

- `0`: `Z-t` occurrences (`00` interiors);
- `2`: `L-t` occurrences (`11` interiors);
- `1`: `2t` mixed occurrences.

Evaluating (7.4) at `c=0,1,2` gives

`dist_cyc(w,rot_2(w)) = min(2L,2Z,A-2t)`.                 (7.5)

Hence on the live complement `R_*>=4`, necessarily

`A-2t>=4`,

so

`t <= floor((A-4)/2)`.                                    (7.6)

This is a proved bridge from closest-rotation geometry to run count. It is not, by itself, a global radius-three producer.

---

## 8. RL123.6 — advancing the low-odd-count frontier to `L>=10`

RL122 already proves that every hypothetical primitive nontrivial positive ordinary cycle has `L>=6`.

RL123 now excludes `L=6,7,8,9`.

### 8.1 `L=6`

For any run count `t`:

- if `t<=3`, the sharp odd-run envelope gives `E_1(6,t)>=18`;
- if `t>=4`, the mod-6 boundary fibre gives `6(t-1)>=18`.

Thus `W>=18`.

For `L=6`,

`D=64*2^Z-729`,
`B=665(2^Z-1)`.

For `Z>=5`,

`18D-B = 487*2^Z-12457 >0`,

already positive at `Z=5` and increasing. Therefore every `L=6,Z>=5` primitive nontrivial candidate is analytically excluded.

The positivity condition `D>0` first allows `Z=4`, so only `(L,Z)=(6,4)` remains for the residual certificate.

### 8.2 `L=7`

For all `t`, either `t<=4` and `E_1(7,t)>=18`, or `t>=4` and `6(t-1)>=18`. Hence `W>=18`.

For `L=7`,

`D=128*2^Z-2187`,
`B=2059(2^Z-1)`.

For `Z>=8`,

`18D-B = 245*2^Z-37307 >0`,

already positive at `Z=8` and increasing.

Since `D>0` first occurs at `Z=5`, only `Z=5,6,7` remain for the residual certificate.

### 8.3 `L=8`

The parameter floor gives

`H(8,12)=25`.

For `Z>=13`, the inherited zero-fibre `k=1` bound gives `W>=2Z-1>=25`. Thus every `L=8,Z>=12` candidate satisfies `W>=25`.

Now

`D=256*2^Z-6561`,
`B=6305(2^Z-1)`,

and

`25D-B = 95*2^Z-157720 >0`

at `Z=12` and thereafter.

Since `D>0` first occurs at `Z=5`, only `Z=5,...,11` remain.

### 8.4 `L=9`

The parameter floor gives

`H(9,18)=41`,
`H(9,19)=42`.

For `Z>=20`, the zero-fibre `k=1` bound gives `W>=2Z-1>=39`. Therefore every `L=9,Z>=18` candidate satisfies the weaker uniform floor `W>=39`.

For `L=9`,

`D=512*2^Z-19683`,
`B=19171(2^Z-1)`,

and

`39D-B = 797*2^Z-748466 >0`

already at `Z=18` and increasing.

Since `D>0` first occurs at `Z=6`, only `Z=6,...,17` remain.

### 8.5 Exact residual certificate

The residual fixed-content ranges are exactly:

- `(6,4)`;
- `(7,Z)` for `5<=Z<=7`;
- `(8,Z)` for `5<=Z<=11`;
- `(9,Z)` for `6<=Z<=17`.

The verifier exhaustively enumerates every rooted binary word in those fixed-content ranges and checks the necessary ordinary ownership condition

`D | Q(w)`.

Total rooted words checked:

`8,606,677`.

Exactly six divisibility hits occur. They are the two alternating rooted words at each of

- `(L,Z)=(7,7)`;
- `(8,8)`;
- `(9,9)`.

Their quotients are the trivial-cycle states `1` and `2`; every hit is periodic and nonprimitive.

There are

`0`

primitive divisibility hits.

Therefore no primitive nontrivial ordinary shortcut cycle exists with `6<=L<=9`.

Combining with inherited RL122.5:

### Corollary RL123.6

Every hypothetical primitive **nontrivial** positive ordinary shortcut cycle must satisfy

`L>=10`.                                                    (8.1)

Classification: **mixed** — analytic semi-infinite packing exclusions plus an **exact finite certificate** on the explicitly listed residual ranges.

The finite certificate is not promoted beyond those ranges and is not a substitute for the analytic RL123.1–RL123.5 theorems.

---

## 9. Mandatory red teams

### RL20 fake-model discriminator — PASS

RL123.1 and RL123.5 are combinatorial statements about words, but no physical exclusion is inferred from them alone. RL123.2–RL123.4 require actual physical boundary states of a fully owned ordinary cycle. The RL20 fake word can satisfy local word geometry while failing ordinary ownership; it therefore does not satisfy the physical premise of the packing theorem.

The exact residual certificate likewise uses `D|Q(w)` only as a necessary ordinary-ownership condition and does not treat local grammar as ownership.

### RL79 generalized-increment discriminator — PASS

For generalized odd increment `s`, an endpoint of `j` odd steps satisfies

`x == -s (mod 3^j)`,

while a following zero run still gives

`x == 0 (mod 2^k)`.

Thus the CRT spacing modulus `2^k3^j` survives, but the residue class depends on `s`.

Crucially, the generalized word numerator and its fixed-content diameter scale by `|s|`. Therefore the ordinary packing consumer becomes

`D P_plus_s <= |s| B`,

not the ordinary `D P_plus<=B`. No factor `s` is cancelled. The low-`L` exact certificate is explicitly the ordinary `s=1` certificate.

### RL81 physical-versus-quotient discriminator — PASS

Every state used in RL123.2 is an actual boundary state in the assumed ordinary cycle. `Q/D` is interpreted physically only after full ownership. No auxiliary quotient label is promoted as a physical state.

### Primitivity — PASS / load-bearing

Primitivity/simple-cycle ownership is needed to make distinct cyclic boundaries distinct physical states, which is required for CRT spacing. The exact residual certificate explicitly finds periodic alternating divisibility hits and rejects them from the primitive nontrivial claim.

### Raw/Farey scope — PASS

RL123.1–RL123.6 use the full cyclic ordinary parity word. No first-Farey, raw-`g=1`, full-phase, or multiplicity restriction is introduced.

### Finite-certificate scope — PASS

The only promoted exact finite certificate covers exactly `8,606,677` rooted words in the residual `(L,Z)` ranges listed in Section 8.5. It does not imply any larger finite or infinite coverage.

---

## 10. Correction/demotion ledger

No inherited theorem is demoted.

Two precision points are frozen:

1. RL123.1 is the exact unrestricted run-composition envelope and a universal primitive lower floor; RL123 does not claim that every balanced equality pattern is primitive.
2. RL123.6 is a **primitive nontrivial-cycle** statement. The finite residual scan deliberately encounters repeated alternating trivial-cycle words and classifies them as periodic/nonprimitive rather than pretending they are excluded by a primitive theorem.

Global status remains:

- radius-three primitive/full-`D` engine: closed locally;
- Gate A: open globally;
- Gate B: open globally;
- global nontrivial-cycle exclusion: open;
- Collatz: not proved.

---

## 11. Strategic frontier after RL123

The run-fibre route has now produced three distinct global resources:

1. exact one-fibre run occupancy;
2. product-modulus CRT boundary packing;
3. a window-count representation of closest-rotation transport.

It also moves the certified low-odd-count frontier from `L>=6` to `L>=10`.

The next unresolved strip begins at `L=10`.

The parameter floor `H(10,Z)` analytically excludes `Z>=25`, while `D>0` first permits `Z=6`. Thus the live `L=10` residual strip is

`6<=Z<=24`.

A naive rooted-word enumeration of that strip contains

`417,221,532`

words, so simply extending the RL123 brute residual scan is no longer the preferred next move.

RL124 should instead exploit the new structure to compress that residual strip:

- deeper `C_(j,k)` CRT capacity/intersection constraints;
- width-capacity inequalities under the exact ceiling `W<=floor(B/D)`;
- the shift-window formula on `R_*>=4`;
- run-profile or meet-in-the-middle ordinary divisibility certificates only after analytic compression.

Do not return to generic p-adic, cocycle, Fourier, transducer, inverse, S-unit, or bulk-cascade routes unless a genuinely new input changes their frozen barriers.

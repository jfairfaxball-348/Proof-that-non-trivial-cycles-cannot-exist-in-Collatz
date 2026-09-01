# RL226 e=4 lossless cylinder normal form and residue barrier theorem

Date: 2026-09-01.

**Classification: proved exact recurrence normal form plus exact finite certificate.**

All statements remain conditional on the inherited sole high branch and on a physical H21 realization. Arithmetic candidates are necessary candidates only; they are not physical occurrences or charges.

## 1. Incoming exact state

RL225 supplies the e=4 root progression

`y_0 = 1,267,492,570,907 + 1,649,267,441,664 k`,

`15,106,005,985 <= k <= 18,969,385,559`,

with **3,863,379,575** raw arithmetic candidates. Terminal Hensel removes exactly **1,842** candidates. Candidate-coupled mandatory-height replay through transition 41 removes a disjoint **1,988,460**, leaving **3,861,389,273** combined survivors.

The fixed deterministic trajectory through phase 36 has

`y_36 = U_36 k + V_36`,

`U_36 = 900,567,811,781,994,726`,

`V_36 = 692,103,040,536,162,613`,

`h_36 = 19`.

In particular `v2(U_36)=1` and `V_36` is odd.

## 2. Lossless cylinder normal form

For any surviving deterministic continuation from phase 36 to phase `i`, let

`m = a_36 + ... + a_(i-1)`

be the cumulative exact 2-adic valuation consumed after phase 36. Then every cylinder can be written uniquely as

`k = r + 2^m t`

for one residue `r mod 2^m`, and on that cylinder

`y_i = U_i t + V_i`.

RL226 proves the following exact invariants:

1. **Branch-independent slope**

   `U_i = 3^(i-36) U_36`.

2. **Height determined by phase and precision**

   `h_i = 19 + b(i) - b(36) - m`,

   where `b(i)=floor(217976794617*i / 137528045312)`.

3. **Exact valuation branch consumes exactly its valuation in k-bits.**

   If the next deterministic valuation is `a>=1`, then among local `t` values there is exactly one residue class modulo `2^a` with `v2(3y_i+1)=a`. Passing to that class raises precision from `m` to `m+a`, keeps the new intercept odd, and multiplies the affine slope by exactly `3`.

The reason is structural: `v2(U_i)=1` for every phase and `V_i` is odd. Hence `3U_i` has exact 2-adic order one while `3V_i+1` is even. After dividing by two, the coefficient of `t` is odd, so divisibility by each additional power of two selects one and only one next low bit. Exact valuation `a` therefore fixes precisely `a` local bits.

Thus the inherited six-field state `(phase,r,m,u,v,h)` is losslessly reducible to

`(phase, r, m, v)`

with `u` and `h` derived exactly from `(phase,m)`.

## 3. What cannot be merged away

The exact low-bit residue `r` (equivalently the phase intercept `v`) is not redundant for the current finite candidate window.

At phase 43 there are cylinders with the same phase, precision `m=30`, height `h=0`, and the same branch-independent slope, but different residues. The verifier exhibits one such cylinder meeting the finite k-window in **3** candidates and another meeting it in **4** candidates.

Therefore a quotient that merges states only by `(phase,m)` (or by `(phase,m,h,u)`) is not lossless for exact finite-window counting. The residue/intercept information is the first exact datum that must still be represented by any deeper compressor. This does **not** rule out a more sophisticated BDD, transducer, residue automaton, or endpoint-aware quotient; it rules out simply discarding the residue translation.

## 4. Exact finite extension through transition 43

Using only the lossless compressed state above, the exact gap-free replay extends RL225 by two transitions:

- transition 42 newly fails **1,299,949** candidates;
- transition 43 newly fails **3,429,092** candidates.

Hence total mandatory-height deletions through transition 43 are

**6,717,501**,

and exact height survivors through transition 43 are

**3,856,662,074**.

Every one of the **1,842** terminal-Hensel-forbidden k values is replayed directly through transition 43 and none has yet failed the height condition. Therefore the terminal and height deletions remain disjoint through this extended depth. The exact combined survivor count is

**3,856,660,232**.

## 5. Scope and consequence

This is a stronger exact finite contraction and a reusable lossless normal-form theorem, but it is **not** e=4 closure. Terminal rank **31,435,476,727** remains live. Necessary terminal-rank counts remain:

- above-p: **7,091,831,283**;
- below-p: **6,324,034,587**;
- total: **13,415,865,870**.

Physical H21 incidence/charge, whole high-branch contradiction, Gate A, Gate B, and global nontrivial-cycle exclusion remain open.

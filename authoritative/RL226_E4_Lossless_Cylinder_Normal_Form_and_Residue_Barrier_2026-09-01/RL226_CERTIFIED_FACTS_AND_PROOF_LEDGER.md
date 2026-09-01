# RL226 certified facts and proof ledger

Date: 2026-09-01.

## Inherited frozen state

RL225 and earlier certified mathematics, corrections, demotions, scope locks, and verification-economy rules remain binding.

Incoming state:

- necessary terminal ranks: **13,415,865,870**;
- above-p sources: **7,091,831,283**;
- below-p sources: **6,324,034,587**;
- e=16 terminal rank **34,124,151,203** excluded;
- e=4 terminal rank **31,435,476,727** live;
- e=4 combined survivors through transition 41: **3,861,389,273**;
- remaining known above-p small offsets below 56: `e=4,28,33,40,45`;
- physical H21 incidence/charge unproved;
- whole high-branch contradiction, Gate A, Gate B, and global nontrivial-cycle exclusion open.

## RL226-T1 — lossless e=4 cylinder normal form

**Classification: proved analytic recurrence theorem.**

From phase 36 onward, write a live cylinder as `k=r+2^m t` and `y_i=u_i t+v_i`. Because `v2(U_36)=1` and the phase intercept is odd, exact valuation `a` selects exactly one local residue modulo `2^a`. Consequently:

- precision increases by exactly `a`;
- `u_i = 3^(i-36) U_36` is branch-independent;
- `h_i = 19+b(i)-b(36)-m` depends only on phase and precision;
- a lossless implementation need store only `(phase,r,m,v)`.

## RL226-T2 — exact residue/intercept barrier to naive state merging

**Classification: proved scope/barrier theorem with exact finite witness.**

The residue translation cannot simply be discarded. At phase 43 and precision 30, two cylinders have identical derived slope and height but intersect the finite k-window in different cardinalities, 3 and 4. Therefore merging by `(phase,m)` alone is not exact for the current finite family. A deeper compressor must preserve residue/intercept information directly or encode it in an equivalent exact transducer/BDD/endpoint state.

## RL226-C1 — transition-42/43 exact contraction

**Classification: exact finite arithmetic certificate.**

The compact verifier traverses every live dyadic cylinder, never individual billions of k values. It reproduces RL225 transition failures 36..41 and extends them by:

- transition 42: **1,299,949** new failures;
- transition 43: **3,429,092** new failures.

Total height deletions through transition 43: **6,717,501**. Height survivors: **3,856,662,074**.

Direct replay of all 1,842 terminal-Hensel-forbidden candidates shows zero height failures through transition 43, so the exact combined remainder is **3,856,660,232**.

## RL226 result classification

RL226 satisfies two success criteria from the target: it proves a reusable lossless compressed state theorem and obtains a substantially stronger exact finite contraction. It also identifies the first datum blocking the naive total merge.

It does **not** empty the e=4 family and does not delete terminal rank 31,435,476,727. No necessary-rank count changes.

## Global scope

Necessary terminal ranks remain **13,415,865,870** = **7,091,831,283** above-p + **6,324,034,587** below-p.

Offsets `e=28,33,40,45` are untouched by RL226. Physical H21 incidence/charge, whole high-branch contradiction, Gate A, Gate B, and global nontrivial-cycle exclusion remain open.

Knowledge catalogues remain `stale/deferred` and are not proof-state authority.

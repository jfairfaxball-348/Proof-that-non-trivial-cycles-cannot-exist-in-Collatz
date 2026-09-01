# RL228 certified facts and proof-state ledger

Date: 2026-09-01.

## Classification

RL228 promotes **two exact analytic lemmas**, one exact combinatorial state-growth certificate, and a **scoped method/scaling barrier** satisfying target success class **C**. It deliberately does **not** promote another e=4 transition-depth elimination.

No terminal rank is excluded. Gate A, Gate B, the sole-high-branch contradiction, physical H21 incidence/charge, and global nontrivial-cycle exclusion remain open.

## Frozen inherited state

The RL227 roadmap and RL226 proof/correction ledgers remain binding.

- e=4 root window: `15,106,005,985 <= k <= 18,969,385,559`;
- raw e=4 candidates: **3,863,379,575**;
- terminal-Hensel deletions: **1,842**;
- height deletions through transition 43: **6,717,501**;
- height survivors through transition 43: **3,856,662,074**;
- combined survivors through transition 43: **3,856,660,232**;
- e=4 terminal rank `31,435,476,727`: live;
- necessary terminal-rank frontier: **13,415,865,870**.

## RL228-T1 — exact dyadic interval bulk/fringe lemma

**Classification: proved exact analytic lemma.**

For an integer interval `I` of length `N` and a residue cylinder `k = r (mod 2^m)`, write `N=q_m 2^m+s_m`, `0<=s_m<2^m`. Then

`#(I ∩ {k ≡ r mod 2^m}) = q_m + epsilon_I(r,m)`

with `epsilon_I(r,m) in {0,1}`.

Thus precision alone determines the translation-independent dyadic bulk `q_m`; all residue dependence lies in one endpoint/fringe bit.

## RL228-T2 — common failure-modulus theorem

**Classification: proved exact analytic recurrence lemma.**

RL226 gives `h_i=E_i-m`, where `E_i=19+b(i)-b(36)`. At transition `i`, the allowed next valuation cap is

`cap=b(i+1)-b(i)+h_i=E_(i+1)-m`.

RL226's exact-valuation normal form gives one failure extension class modulo `2^cap`. Lifting back through the parent precision `m` makes every transition-`i` failure subcylinder a single class modulo

`2^(m+cap)=2^E_(i+1)`,

independent of its parent valuation history. Distinct live parents give distinct common-modulus failure residues.

Hence if `S_i` is the live cylinder count and `F_i` the transition failure count, exactly

`F_i = floor(N/2^E_(i+1))*S_i + R_i`,

where `R_i` is the number of common-modulus failure residues meeting the endpoint remainder of the finite window.

## RL228-C1 — exact e=4 endpoint scaling boundary

**Classification: exact combinatorial certificate plus scoped method barrier.**

For e=4:

- `E_43=30`;
- `E_44=31`;
- `E_45=33`;
- `N=3,863,379,575`;
- `2^31 < N < 2^32 < 2^33`.

Every phase-44 live cylinder has precision `m<=31`, and every residue class modulo at most `2^31` meets an interval of length `N>2^31`. Therefore endpoint placement prunes **no** admissible valuation-history state before phase 44. A precision-only dynamic programme gives the exact phase-44 state count

**`S_44 = 7,743,281`.**

But every transition-44 failure subcylinder has common modulus `2^E_45=2^33>N`, so

`floor(N/2^33)=0`.

The exact bulk/fringe identity therefore becomes

`F_44 = R_44`.

At this boundary the reusable translation-independent bulk contributes **nothing**. Exact transition-44 failure counting is entirely the endpoint-incidence problem for up to 7,743,281 distinct high-modulus failure residues.

RL228 deliberately does not enumerate those endpoint hits as a new finite extension, because the target says to pivot once only state-by-state endpoint propagation remains without a new uniform theorem.

## Exact anti-merge witness

Two phase-44 singleton cylinders have the same phase, precision `31`, height `0`, and current finite-window cardinality `1`, but opposite transition-44 fate.

- Cylinder A: residue `1,871,163,824 (mod 2^31)`; unique window representative `k=16,903,549,360`; valuations from transitions 36..43 are `[20,2,1,2,1,2,1,2]`, cumulative precision `31`; its transition-44 valuation is `1`, within the cap `2`.
- Cylinder B: residue `59,224,496 (mod 2^31)`; unique window representative `k=17,239,093,680`; valuations from transitions 36..43 are `[20,2,1,2,1,1,3,1]`, cumulative precision `31`; its transition-44 valuation is `4`, exceeding the cap `2`.

Therefore `(phase,precision,height,current-cardinality)` is not a future-exact quotient. Equivalent endpoint/residue information remains load-bearing.

## Scaling classification and pivot

RL228 does **not** prove every conceivable BDD, transducer, nonlocal residue automaton, or future algebraic compressor impossible. It proves the narrower barrier needed by the target:

1. the current engine has an exact bulk/fringe decomposition;
2. at transition 44 the bulk term becomes identically zero;
3. phase 44 already contains **7,743,281** live cylinders;
4. even equal-cardinality singleton states can have opposite next-transition fate;
5. absent genuinely new algebraic structure on the endpoint residues, deeper traversal is endpoint-state propagation rather than a uniform rank-family exhaustion theorem.

This is target success **C — decisive barrier**. RL229 therefore pivots to **physical H21 incidence and exhaustive charge**.

## Global scope locks

- e=4 terminal rank `31,435,476,727` remains live.
- The e=4 combined survivor count remains certified only through transition 43: **3,856,660,232**.
- Necessary terminal ranks remain **13,415,865,870**.
- No e=4 formula is transferred to `e=28,33,40,45`.
- Arithmetic height elimination is not physical H21 incidence or charge.
- Gate A and Gate B remain open; global nontrivial-cycle exclusion remains open.
- Knowledge catalogues remain `stale/deferred`.

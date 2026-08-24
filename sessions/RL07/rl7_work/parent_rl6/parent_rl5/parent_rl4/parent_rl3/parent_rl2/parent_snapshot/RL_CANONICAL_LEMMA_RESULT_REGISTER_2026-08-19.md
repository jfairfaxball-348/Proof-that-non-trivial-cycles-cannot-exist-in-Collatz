# Collatz R# RL — Canonical Lemma / Result Register

**Date:** 2026-08-19  
**Branch:** RL only.

## Status vocabulary

- **PROVED ANALYTIC THEOREM** — exact proof independent of finite sampling.
- **LITERATURE FACT / EXTERNAL INPUT** — taken from cited primary literature; not reproved here.
- **EXACT FINITE CERTIFICATE** — exhaustive exact statement on a declared finite domain only.
- **EXACT FINITE DIAGNOSTIC** — exact finite computation useful for strategy but without an extension theorem.
- **OPEN PROOF OBLIGATION** — required or strategically central unproved edge.
- **FAILED / REFUTED ROUTE** — shortcut defeated in its stated form.
- **NOT TRANSFERRED** — valid elsewhere but not licensed on this branch.

## A. Foundation and transfer results

| ID | Claim | Status | Role |
|---|---|---|---|
| RL-F1 | Red is forward/inverse closed; every red integer and every forward state of `R#` is `>=R#`. | **PROVED ANALYTIC THEOREM** | least-red barrier |
| RL-F2 | `R#` is odd and `R# != 2 mod3`. | **PROVED ANALYTIC THEOREM** | root arithmetic |
| RL-F3 | First accelerated exponent `b0=1`; hence `R#=3 mod4`. | **PROVED ANALYTIC THEOREM** | new RL-0 prefix constraint |
| RL-F4 | Second exponent `b1<=2`; hence `R# mod16 in {7,11,15}`. | **PROVED ANALYTIC THEOREM** | new 2-adic pruning |
| RL-F5 | `xi(r1)=R#+1` and `B(r1)=R#`; an initial run of exponent-1 steps preserves xi equality. | **PROVED ANALYTIC THEOREM** | exact entry neutral anchor |
| RL-F6 | `R# !=4 mod9`; combined residue survivors mod144 are the 15 classes listed in the foundation. | **PROVED ANALYTIC THEOREM** | revalidated xi pruning |
| RL-F7 | `k=0 => R#=C_min`; `k>0 => R#<C_min`. In `k=0`, `R#=1 mod3` and six mod144 root classes survive. | **PROVED ANALYTIC THEOREM** | branch split |
| RL-F8 | Two distinct inverse paths to one physical endpoint force a periodic root unless depths agree; thus root-path injectivity holds for `k>0` but fails on cycle roots. | **PROVED ANALYTIC THEOREM** | collision semantics |
| RL-A3 | Exact inverse affine/common-tail identities transfer algebraically. | **PROVED ANALYTIC THEOREM** | state representation |
| RL-N1 | `xi(y)-1=B^{v3(y+1)}(y)`. | **PROVED ANALYTIC THEOREM** | inverse descent coordinate |
| RL-N2 | Every red `y` has `xi(y)>=R#+1`. | **PROVED ANALYTIC THEOREM** | contradiction barrier |
| RL-N6 | A shortened-map inverse root `0 mod3` has only its direct doubling ray. | **PROVED ANALYTIC THEOREM** | local guardrail |

## B. Exact cycle and LREC results

| ID | Claim | Status | Role |
|---|---|---|---|
| RL-C1 | Odd affine iterate: `U^m(x)=(3^m x+Q_m(e))/2^E`. | **PROVED ANALYTIC THEOREM** | cycle/preperiod algebra |
| RL-C2 | Cycle equation `(2^A-3^L)c0=Q_L(a)` and all rotated copies; `D=2^A-3^L>0`. | **PROVED ANALYTIC THEOREM** | exact cycle integrality |
| RL-C3 | Every odd cycle state is nonzero mod3. | **PROVED ANALYTIC THEOREM** | residue structure |
| RL-L1 | Eliminated LREC equation `D(3^k R#+Q_k(b))=2^B Q_L(a)`. | **PROVED ANALYTIC THEOREM** | main Diophantine coupling |
| RL-L2 | Preperiod word fixes exact 2-adic root cylinder and a `3^k` entry cylinder. | **PROVED ANALYTIC THEOREM** | finite-state matching |
| RL-L3 | Suffix Matching: for `h<=min(k,L)`, the last `h` exponents of `b` and of the entry rotation of `a` have equal `Phi_h` signatures modulo `3^h`. | **PROVED ANALYTIC THEOREM** | new entry/cycle coupling |
| RL-L4 | `h=1`: `b_{k-1} == a_{L-1} (mod2)`; `h=2`: the compact mod-6 terminal-pair invariant agrees. | **PROVED ANALYTIC THEOREM** | first explicit suffix constraints |
| RL-L5 | Least-red prefix ceiling: for every odd prefix, `S_t <= t log2(3+1/R#)`. | **PROVED ANALYTIC THEOREM** | global minimality -> exponent constraint |
| RL-L6 | Entry/cycle slack: `B+A_j <= (k+j) beta_R` and `A_j-beta_R*j <= beta_R*k-B`. | **PROVED ANALYTIC THEOREM** | preperiod budget constrains entry rotation |
| RL-L7 | Cycle product identity `2^A=prod_j(3+1/c_j)`; hence `log2 3 < A/L <2`. | **PROVED ANALYTIC THEOREM** | slope envelope |
| RL-L8 | If `n1` cycle exponents equal 1, then `n1>=2L-A`. At least one exponent is 1 in every nontrivial positive cycle. | **PROVED ANALYTIC THEOREM** | cycle word structure |
| RL-L9 | Xi-weighted cycle bound: successor of an odd exponent has `v3(c+1)>=1` and height at least `(3R#+1)/2`; this sharpens the cycle product according to exponent parity. | **PROVED ANALYTIC THEOREM** | links 2-adic word to 3-adic barrier |
| RL-L10 | Writing `u=log2(3+1/R#)` and `v=log2(3+2/(3R#+1))`, every RL cycle obeys `log2 3 < A/L <= (2v-u)/(1-u+v) < u`. | **PROVED ANALYTIC THEOREM** | strict xi-weighted slope sharpening |

## C. External literature inputs

| ID | Fact | Status |
|---|---|---|
| RL-E1 | Collatz convergence computationally verified through `2^71`. | **LITERATURE FACT / EXTERNAL INPUT** — Barina 2025 |
| RL-E2 | Modern nontrivial-cycle period lower bound reported as `355,504,839,929` in the unshortened convention; convention conversion must be explicit. | **LITERATURE FACT / EXTERNAL INPUT** — Barina 2025 / Hercher line |
| RL-E3 | Nontrivial cycles require at least 92 local minima in Hercher's `m` terminology. | **LITERATURE FACT / EXTERNAL INPUT** — Hercher 2023, with 2026 corrigendum linked by journal |
| RL-E4 | Christoffel words maximize a rotation-minimum cycle functional for fixed parity counts. | **CURRENT PREPRINT / NOT CANONICAL** — Fernández & Ibáñez 2026 |

## D. Exact computations made this session

| ID | Result | Status | Certificate |
|---|---|---|---|
| RL-X0 | Supplied RL elementary baseline: 19,530 small exponent words + 800 direct accelerated iterations. | **EXACT FINITE CERTIFICATE** | `RL_BASELINE_VERIFICATION_LOG.txt` in parent bundle |
| RL-X1 | New LREC verifier passes affine identities, xi saturation, inverse affine words, collision audits, mod-9 exclusion and 324,726 suffix-signature checks. | **EXACT FINITE CERTIFICATE** for stated checks | `logs/RL_LREC_VERIFICATION_LOG.txt` |
| RL-X2 | Prefix survivor automaton under external `R#>=2^71` input: exact boundary/cylinder DP through depth 128; brute residue agreement through depth 8. | **EXACT FINITE DIAGNOSTIC** | `logs/RL_PREFIX_AUTOMATON_LOG.txt` |
| RL-X3 | At depth 42 the prefix automaton has 25 cumulative-sum states but `41,156,292,958,100,112` formal exponent words; conditional 2-adic mass about `0.00246825`. | **EXACT FINITE DIAGNOSTIC** | same log |

## E. Failed / blocked shortcuts

| ID | Route | Status | Reason |
|---|---|---|---|
| RL-G1 | Assume `R#` lies on the cycle. | **FAILED / REFUTED ROUTE** | `k>0` is logically possible and must be handled. |
| RL-G2 | Count distinct inverse words as distinct red integers everywhere in RL. | **FAILED / REFUTED ROUTE** | periodic roots admit genuine unequal-depth collisions. |
| RL-G3 | Treat the finite prefix automaton as an infinite exclusion. | **FAILED / REFUTED ROUTE** | enormous survivor family remains; no extension theorem. |
| RL-G4 | Use the affine cycle equation alone as new cycle exclusion. | **FAILED / INSUFFICIENT ROUTE** | it is classical and has many formal Diophantine survivors; minimality coupling is essential. |
| RL-G5 | Import RO Harmonic Regeneration/XCORL unchanged. | **NOT TRANSFERRED** | RL requires quotient-aware physical ownership/repeatability. |

## F. Open proof obligations

| ID | Obligation | Severity |
|---|---|---|
| RL-O1 | Turn arbitrary-depth suffix matching `Phi_h(b)=Phi_h(a)` into a finite/infinite exclusion or forced structural class. | **CRITICAL** |
| RL-O2 | Combine the prefix slack budget with cycle rotations/minimum constraints strongly enough to force a contradiction or finite survivor automaton with an extension theorem. | **CRITICAL** |
| RL-O3 | Exploit the xi-weighted cycle product beyond its current scalar strengthening; track `v3(c_j+1)` exactly around the cycle. | **HIGH** |
| RL-O4 | Construct the physical inverse-basin quotient for a periodic root and prove bounded ownership/collision multiplicity for any reuse of inverse-tree methods. | **HIGH** |
| RL-O5 | Split and close `k=0` (least red on cycle) and `k>0` (strict preperiod) if their strongest mechanisms differ. | **CRITICAL** |
| RL-O6 | Independently verify any Christoffel/extremal preprint result before placing it on the proof chain. | **MEDIUM / OPTIONAL** |
| RL-O7 | Produce a genuine infinite extension theorem; finite residue or depth pruning alone is not an RL exclusion. | **CRITICAL ENDPOINT** |

## Verdict

RL is not solved. The branch has, however, moved beyond a generic cycle-equation restatement: the new canonical object is a least-red preperiod/cycle system with exact 2-adic prefix restrictions, arbitrary-depth 3-adic suffix matching, xi-height constraints, rotation integrality, and collision-aware inverse semantics.

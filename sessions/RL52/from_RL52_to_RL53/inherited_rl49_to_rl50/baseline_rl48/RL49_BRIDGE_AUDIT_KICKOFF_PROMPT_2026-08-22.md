# RL49 Bridge-Audit Session Kickoff

Continue the Collatz R-sharp / RL research from `Collatz_Rsharp_RL48_to_RL49_Handover_2026-08-22.zip` as a skeptical research mathematician. This session is primarily a **radius-3 theorem-matching audit**, not a broad computational extension.

## 0. Mandatory verification

From the bundle root run:

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl48_handover_verifiers.sh
```

Treat any failure as a stop-and-repair event.

Read:

1. `README_START_HERE.md`
2. `RL48_PROOF_STATE_AND_BRIDGE_LEDGER.md`
3. `rl48_continued/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`
4. `rl48_continued/RL48_RADIUS3_MATCH_COROLLARY.md`
5. `RL48_REPRODUCIBILITY_LEDGER.md`

Use `inherited/Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip` for RL45/RL47 provenance when needed.

## 1. First and decisive priority — recover the exact RL18/RL19 radius-3 theorem

Retrieve the original audited RL18/RL19 theorem statement from earlier project handovers if accessible. Do not rely on a paraphrase from later sessions. Record:

- the exact theorem statement;
- all support/sparsity assumptions;
- orientation conventions;
- gcd/primitivity assumptions;
- boundary cases;
- modulus or prime-power hypotheses;
- any external analytic dependencies;
- which parts are analytic versus finite certificate.

If the exact source theorem cannot be recovered, do **not** declare Gate B closed. The correct result of the session is then to identify this missing provenance item explicitly.

## 2. Match the theorem line-by-line to the RL48 four-swap theorem

RL48 has proved, from current-bundle conventions, that the full phase condition is equivalent to a positive integer `N` with genuine Collatz trajectories

`N --u--> N+4`,

`N+4 --v--> N`,

where

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`.

The first two common odd steps convert the physical gap `4` to gap `9`; the split is `(0,1)` and the canonical local coordinate is `T=-14`.

Construct a hypothesis table with one row per radius-3 theorem assumption and one of:

- proved directly by RL48;
- inherited and verified;
- requires a new lemma;
- not satisfied.

Do not use phrases like “essentially the same” or “morally radius 3”. Give exact variable translations.

## 3. If every hypothesis matches, formally close Gate B

If and only if the exact audited radius-3 theorem applies, write a short theorem:

> **Full-phase radius-3 bridge.** Under the retained RL one-excursion hypotheses, the full phase condition is impossible.

The proof should consist of:

1. the RL48 full-word reconstruction;
2. the proper-factor identity;
3. full-denominator factorization;
4. construction of positive `N` and genuine `N <-> N+4` trajectories;
5. exact transformation to the radius-3 theorem's variables;
6. direct invocation of the audited theorem.

Then update the global proof ledger and determine whether Gate A remains logically necessary for the surviving RL branch.

## 4. If a hypothesis fails to match, isolate the smallest missing lemma

Do not reopen the old global resultant program automatically. State the exact unmatched radius-3 hypothesis and attack only the implication needed from the RL48 configuration.

Fallback objects already available:

- the rank-displacement defect
  `D=sum 3^(r-j)2^b_j(2^delta_j-1)`;
- under low area, at most `t+2` active defect ranks;
- phase congruence
  `12D+2^(a-t-2)=237*3^(ell-3) (mod 2^a-3^ell)`.

Use this only if the direct four-swap configuration does not already lie inside the radius-3 theorem.

## 5. Gate A only after the logical dependency is resolved

RL48 proved that the RL47 separable rank relaxation cannot exclude `z=q-t>=42`. Therefore do not spend the session polishing that relaxation.

First determine whether Gate B alone kills the full-phase branch in a way that makes the uniform terminal inequality unnecessary for closure. If Gate A remains necessary, formulate a new coupling invariant for synchronized height-one motion. q=134 may be used as a falsification laboratory, not as the main target.

## 6. Closure discipline

A claim of RL closure must explicitly establish:

1. exact applicability of the audited radius-3 theorem;
2. impossibility of the full phase condition for the live branch;
3. whether any non-full-phase/proper-factor branch remains and how it is excluded;
4. whether Gate A is logically required after Gate B;
5. all inherited dependencies and finite certificates separately labelled.

Do not claim a Collatz proof beyond the exact scope of the RL branch being audited.

## 7. Desired session endpoint

Best case:

- Gate B formally closed by the exact radius-3 theorem;
- global RL proof graph simplified and remaining gate(s) identified precisely.

Acceptable fallback:

- one explicit unmatched radius-3 hypothesis isolated as the sole Gate-B lemma, with a verifier/countermodel test and a clean next-session handover.

# RL274 — Radius-5 global encounter bridge discovery

Date prepared: 2026-09-07  
Status: **PREPARED, NOT STARTED**

Incoming classification: **RADIUS5_LOCAL_THEOREM_CLOSED**.

## Fixed promoted input

Treat the completed Radius-5 theorem as fixed, not as a target to reopen:

> Under the inherited audited RL238/RL265 admissibility hypotheses — positive `D=2^A-3^L>1`, primitive parity word, full-`D` numerator divisibility, and the retained local-theorem side conditions — no nontrivial cyclic self-rotation has exact cyclic earth-mover distance 5.

The full determinant decomposition is closed:
- `|kappa|=1`: RL270;
- `|kappa|=3`: RL271–RL272;
- `|kappa|=5`: RL273.

All nine Radius-5 topology families are covered.  Radius 5 is therefore a proved **local** obstruction, not yet a global cycle-exclusion theorem.

## Mission

Freeze the Radius ladder temporarily and answer as directly and rigorously as possible:

> **What is the weakest encounter theorem that would allow the now-proved Radius-5 local obstruction to be used globally against a hypothetical non-trivial Collatz cycle?**

This is a discovery/strategy session.  It is not a request to prove Radius 6, Radius 7, a general Radius-n theorem, or a global Collatz theorem prematurely.

## Required discovery work

1. Recover and restate the exact promoted Radius-5 theorem, including every scope hypothesis, and use it as fixed input.
2. Write the global implication actually needed from a hypothetical positive non-trivial Collatz cycle to a Radius-5-forbidden local configuration.
3. Work backwards from Radius 5 and formulate the **weakest sufficient encounter statement**.  Make quantifiers and the exact metric/self-rotation condition explicit wherever possible.
4. Separate:
   - sufficient but unnecessarily strong encounter statements;
   - statements that appear minimal or close to minimal;
   - consequences already forced by promoted cycle/parity-word structure;
   - genuinely new mathematical obligations.
5. Determine which mechanism the missing bridge fundamentally concerns:
   - recurrence / return frequency;
   - density or spacing of odd steps;
   - modular or parity-word structure;
   - self-rotation / near-self-rotation encounters;
   - pigeonhole / compactness / repetition;
   - Diophantine approximation;
   - another explicitly identified mechanism.
6. Test explicitly whether fixed Radius 5 is already large enough for any plausible encounter theorem.
7. If Radius 5 is insufficient, identify the exact reason: required radius exceeds 5, required object is not a fixed-radius self-rotation, a missing topology/metric notion is needed, or another precise obstruction.
8. Only if this bridge analysis itself shows that a larger local radius would materially help, state the exact additional local theorem needed and why.  Do not default to Radius 6.

## Strategic comparison

Explicitly compare expected mathematical leverage of:

- **Investment A:** prove Radius 6;
- **Investment B:** solve or materially reduce the weakest Radius-5 encounter theorem.

Assess which attacks the actual missing implication rather than merely extending local machinery.

## General local invariant question

Radius 3, Radius 4, and Radius 5 share substantial transport/determinant machinery.  Investigate conceptually:

> Are these finite-radius proofs exposing a general local invariant that should now be abstracted, rather than continuing radius by radius?

Do not launch a full general Radius-n proof unless the discovery work produces a genuinely clean route and demonstrates that it helps the bridge.

## Frozen

Unless the bridge analysis itself supplies a compelling reason to unfreeze:
- Radius 6;
- Radius 7 or higher;
- brute-force higher-radius enumeration;
- Lean formalisation;
- fifth-selector / unrelated selector work;
- unrelated historical pivots.

## Required final authoritative strategy document

End RL274 with a concise strategy document containing:

1. the exact completed Radius-5 theorem being used;
2. the weakest sufficient encounter theorem, stated formally or as close to formally as current knowledge permits;
3. a dependency diagram:

   `hypothetical non-trivial cycle`
   `        |`
   `        v`
   `weakest encounter theorem`
   `        |`
   `        v`
   `Radius-5 forbidden self-rotation`
   `        |`
   `        v`
   `contradiction`;

4. the exact implication currently missing;
5. whether Radius 6 would actually help that implication;
6. the recommended next research target chosen by mathematical leverage, not momentum.

Preferred classifications:
- `RADIUS5_BRIDGE_SUFFICIENCY_IDENTIFIED`;
- `RADIUS5_BRIDGE_REDUCED_TO_EXACT_TARGET`;
- `RADIUS5_INSUFFICIENT_FOR_IDENTIFIED_BRIDGE`;
- `GENERAL_LOCAL_PATTERN_IDENTIFIED`;
- `BRIDGE_EXACT_BARRIER`.

Do **not** claim a global proof unless every required implication has actually been established.

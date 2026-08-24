# Kickoff prompt for the audit/review session

Audit the attached `Collatz_Rsharp_RL16_Audit_Handover_2026-08-20.zip` as a skeptical mathematical reviewer before extending the research.

Primary goals:

1. Establish the exact current proof state: what is analytically proved, what depends on the external Laurent--Mignotte--Nesterenko two-logarithm theorem, what is only an exact finite certificate, and what is merely computational/session evidence.
2. Reconstruct the exact radius-3 case tree from RL10 onward and verify that the RL11--RL16 closures are exhaustive, with no omitted support/orientation/gcd/boundary cases hidden by symmetry.
3. Red-team the new RL16 proofs and rerun both verifiers.  In particular audit all resultant nonvanishing steps, monotonicity/envelope inequalities, LMN cutoffs, continued-fraction reductions, and exact finite coverage.
4. Audit RL-L104 independently.  The frozen result is only a sparse `1,3,9` congruence modulo the cubic cofactor `C`; the converse forcing equal spacing is OPEN.
5. Treat two later conversation claims as UNVERIFIED SESSION LEADS unless you reproduce them: (a) promotion of the sparse congruence to the full discrepancy `D`; (b) a pure arithmetic uniqueness scan through `a<=80` / 2,785 admissible parameter choices with no skew zero.
6. Give a sober “distance to closure” assessment with two separate answers: (i) distance to closing exact radius 3; (ii) distance to closing RL itself.
7. Identify the shortest plausible route forward.  Explicitly answer whether proving the cubic-cofactor converse would merely finish radius 3, or whether the existing RL root/return grammar already gives the missing bridge from radius-3 exclusion to an RL contradiction.

Important guardrails:

- Do not assume “radius 3 closed” implies RL closed.  The older global dependency map still identifies an infinite-structure/bridge problem.
- Do not promote finite scans to infinite theorems.
- Preserve the external LMN dependency explicitly.
- Prefer finding a flaw or missing hypothesis over harmonizing inconsistent notes.
- If the case tree is sound, state exactly which single branch remains for radius 3 and formulate the missing theorem in its cleanest normalized variables.
- If the global RL bridge is still absent, say so clearly and rank the best candidate bridges (distinguished root/return rotation distance, weighted multi-edge obstruction, suffix/xi extension theorem, residual-denominator descent).

Start by reading `START_HERE.md`, `AUDIT_STATUS_AND_DISTANCE_TO_RL.md`, `PROOF_CHAIN_AUDIT_CHECKLIST.md`, the two RL16 notes, and the fresh verification log.  Use `baseline/Collatz_Rsharp_RL15_Handover_2026-08-20.zip` only when you need the full inherited proof chain.

Deliver the review as:

- a proof-status table;
- a radius-3 branch-exhaustiveness table;
- a list of any proof gaps or fragile dependencies;
- a distance-to-radius-3 assessment;
- a separate distance-to-RL assessment;
- the top 2--3 concrete theorem targets for the next research session.

# RL55 Audit / Review / Roadmap Session Kickoff Prompt

Audit the attached `Collatz_Rsharp_RL54_to_RL55_Audit_Handover_2026-08-23.zip` as a skeptical research mathematician before extending the Collatz RL/3n+1 research.

## Mandatory first step — integrity and reproducibility

1. Verify the outer ZIP SHA-256 against the supplied `.sha256` sidecar.
2. Extract the bundle and run:
   `sha256sum -c SHA256SUMS_RL54_TO_RL55_AUDIT.txt`.
3. Run:
   `bash verification/run_all_rl54_audit_verifiers.sh`.
4. Treat any checksum or verifier failure as a stop-and-repair event.
5. If resources permit, independently compile and rerun the exact finite `L_terminal(8,17)=70` computation using `rl54_research/verify_rl54_terminal_exactx_split.cpp`. Do not infer correctness merely from the stored run log.

## Primary goal 1 — establish the exact proof state

Produce a skeptical proof ledger separating:

- analytic theorems;
- exact rational identities/inequalities;
- exact exhaustive finite certificates;
- inherited dependencies;
- computations whose source/run exists but which still need independent audit;
- heuristic observations/conjectural strategies.

At minimum audit the inherited `z>=41` threshold inside the safe continued-fraction survivor and make explicit that it is not a global denominator theorem.

## Primary goal 2 — red-team every genuinely new RL54 claim

### A. z=41 self-seeding recurrence

Reconstruct the defect lower bounds independently. Verify the constant `(t,17)` terminal budget through `t=11`, the break at `t=12`, the cleanup cap 18, and the interpretation of the terminal maxima `L(0..8,17)`.

### B. uniform `(R,R+4)` defect reduction

Let `R=z-27`. Independently derive why stages through `n>=29` need y-cap `R+3` and the two cleanup stages need `R+4`. Verify the monotonicity step used for `n>=30` and the special exact treatment at `n=29`.

Do not promote this reduction into a uniform terminal theorem; it is only a reduction unless the terminal side is proved.

### C. correction to the fixed `2^-1000` target

Independently derive

`K=q-z+3`, `R=z-27`, and hence `K+R=q-24`.

Then reconstruct the lower bound on the final x-zero weight and determine exactly when it prevents `w_last<2^-1000`. Check all endpoint normalizations and quantifiers. If the correction is valid, explicitly demote the earlier proposed all-R fixed-negligibility target.

### D. normalized terminal coordinate `P=2^r J`

Starting from the inherited backward `J` grammar, independently derive all four `P` updates. Check divisibility and state-domain restrictions, not just affine algebra. Verify `P_end=2^(q-24)` and determine whether this yields a genuine monotone potential, finite-state reduction, or merely a suggestive normalization.

### E. legal-prefix mass certificate

This is the highest-priority new finite computation.

Audit `rl54_research/verify_rl54_legal_prefix_mass_and_uniform_obstruction.py` line by line. Reconstruct the legal Markov state, parity-forced y-bit rule, height constraint, x-zero weight recurrence, sequential cap and objective. Check that memoization/dominance preserves the maximizing path and that no branch is incorrectly removed.

Independently verify or refute the claimed exact maximum

`Zx_26^legal,max = 34057930625026471931596 / 2954312706550833698643`

=`11.528207745072855...`.

If correct, verify the exact margin

`Delta = 143/12 - Zx_26^legal,max`

=`0.3884589215938109...`.

Determine precisely what additional theorem would be sufficient to turn `Zx_late<Delta` into a contradiction.

### F. greedy-prefix terminology and local death at column 20

Independently replay the previously called “greedy first-26 x-zero schedule”. Verify whether it really reaches `(d,J)=(1,-6)` after column 19 and has no legal y choice for the prescribed x-bit at column 20.

This is potentially a major proof-ledger issue. Distinguish:

1. a relaxed x-only mass-maximizing schedule under the sequential cap; and
2. an actually legal full Markov x/y prefix.

Audit RL53/RL54 wording and logic for any accidental conflation. In particular determine whether the already-certified z=37 and z=39 contradictions remain valid when this terminology is repaired. If anything breaks, stop and repair it before proceeding.

### G. bounded cut-state interval

Reconstruct the derivation of the positive cut-state cap `<1379` and inherited lower bound `>-1318`. Audit the cut definition, suffix counts, sign cases, zeta bound and dependence on any greedy assumption. Decide whether this really yields a finite interval of candidate integer J states useful for a theorem.

## Primary goal 3 — bridge/radius-3 strategic review

Re-state the status of radius 3, Gate A and Gate B after RL49-RL54. Do not revive the invalid half-period radius-3 shortcut.

Answer explicitly:

1. What exactly would still be needed for an RL -> radius-3 bridge?
2. Would closing the safe CF survivor suffice for Gate A, or only one denominator regime?
3. Is the new legal-prefix/late-mass route plausibly a Gate-A theorem, a full-phase impossibility theorem, or merely another survivor-local elimination?
4. Which missing lemma currently has the greatest global leverage?

## Primary goal 4 — set a ranked roadmap before doing new research

After the audit, produce a ranked plan for the next research session. Compare at least:

1. **Aggregate late-mass theorem:** prove `Zx_late < 0.3884589215938109...` under the inherited survivor hypotheses.
2. **Normalized-P theorem:** exploit `P=2^rJ` and `P_end=2^(q-24)` for an R-uniform potential, finite-state or divisibility obstruction.
3. **Bounded-J cut theorem:** turn the `-1318 < J_cut < 1379` phenomenon into a finite exact classification, if the cut assumptions survive audit.
4. **z=41 fallback:** continue `L(9,17),...` only if useful diagnostically or if the uniform approaches fail.
5. **Global bridge/Gate-A attack:** if all survivor-local routes appear inherently nonuniform, redirect effort to the missing global lemma rather than accumulating more z thresholds.

Rank each route by:

- mathematical leverage;
- risk of hidden inherited assumptions;
- whether it could plausibly become uniform;
- computational scalability;
- relevance to Gate A / radius-3 bridge / RL closure.

## Deliverable for this audit session

Before doing substantive new extension work, produce:

1. an updated proof-state table/ledger;
2. a list of any repaired or demoted claims;
3. a verdict on whether z=37 and z=39 remain intact after the “greedy” audit;
4. a verdict on the legal-prefix `11.528207745...` certificate;
5. a verdict on the fixed-`2^-1000` correction and `P` normalization;
6. a concise statement of how close or far the current work really is from Gate A and a valid radius-3 bridge;
7. a ranked roadmap for the next extension session.

Only after that review should the project resume active theorem hunting.

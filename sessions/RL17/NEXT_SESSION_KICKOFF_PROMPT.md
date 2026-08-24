# RL17 Repair + Strategic Advance Session Kickoff

Continue the Collatz R-sharp RL project from this handover as a repair-and-advance session, not as a passive audit.

Start with `START_HERE.md`, `RL17_AUDIT_FINDINGS_FREEZE.md`, `RL17_PROOF_STATUS_AND_BRANCH_LEDGER.md`, and `RL17_REPAIR_AND_STRATEGY_WORKPLAN.md`.  Rerun the RL16 and RL17 verifiers before using their outputs.

Primary objectives:

1. Reconstruct and freeze the missing analytic proof reports behind RL12 and RL13.  Do not treat their finite verifiers as proofs of the infinite reductions.
2. Repair the radius-3 case tree by explicitly attacking the two branches the old roadmap dropped:
   - coefficient-3 `P2 [2,1]` boundary in the `j=1` and `j=2` sectors;
   - `gcd(A,L)=3, gcd(A,m)=3` cubic three-orbit sector.
3. Use the new RL17 full-`D` sparse lemma as the preferred one-orbit cubic formulation.  Try to prove infinite sparse uniqueness; the `a<=80` / 2,785-parameter scan is evidence only.
4. Rebuild the radius-3 exhaustiveness table after every closure.  Do not claim “one branch remains” unless every gcd/support/orientation/boundary leaf is visibly accounted for.
5. Work strategically on RL itself before closing the session.  In particular, attempt to prove or falsify a **distinguished least-root/final-return rotation-distance bridge**.  If bounded distance is false, produce a countermodel and pivot to a weighted multi-edge obstruction.
6. Explore the ranked global alternatives only as theorem programs, not deeper finite scans: distinguished root/return rotation distance; weighted multi-edge obstruction; suffix/xi extension theorem; residual-denominator descent.
7. Keep the external two-logarithm dependency explicit wherever used and re-check theorem constants before freezing any new cutoff.

Required outputs for this session:

- a repaired proof-status table;
- an exhaustive radius-3 branch tree;
- written proof notes for any restored/closed branches;
- executable exact verifiers for finite tails;
- a strategic note recording a proved bridge lemma, a falsified bridge with counterexample, or a genuine unbounded-radius invariant;
- separate sober assessments of distance to exact radius 3 and distance to RL;
- a new zipped handover with SHA-256 manifest and kickoff prompt.

Guardrails: do not assume radius-3 closure implies RL; do not promote finite scans to infinite theorems; do not hide omitted cases under symmetry; prefer a discovered flaw or counterexample over preserving the old roadmap.

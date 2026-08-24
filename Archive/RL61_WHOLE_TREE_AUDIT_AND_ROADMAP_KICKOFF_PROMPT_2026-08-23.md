# RL61 whole-tree audit / review / roadmap reset — kickoff prompt

Audit the attached `Collatz_Rsharp_RL60_Freeze_to_RL61_Whole_Tree_Audit_Handover_2026-08-23.zip` as a skeptical research mathematician.

This is **not** initially a proof-extension session. The terminal-tail attack is deliberately frozen. Do not start by pushing K41/K43, tightening the current survivor, or reviving an old radius-3 bridge. First reconstruct the entire logical RL tree and produce an authoritative proof-state/roadmap reset.

## Gate 0 — integrity and provenance

1. Verify the outer `.sha256` sidecar.
2. Verify `SHA256SUMS_RL60_FREEZE_TO_RL61.txt`.
3. Verify the unchanged incoming RL59→RL60 handover sidecar under `inherited_current/`.
4. Read `HANDOVER_VALIDATION_STATUS.txt` and `verification/README_VERIFICATION_STATUS.md`.
5. Treat any checksum or inherited verifier failure as a stop-and-repair event.

## Gate 1 — reconstruct the whole RL branch tree

Use the recovered RL18/RL19/RL20 bundles, RL48–RL59 reference snapshots, and nested provenance to reconstruct the actual case tree rather than relying on recent shorthand.

Produce a branch ledger that answers, for every top-level and important second-level branch:

- exact hypotheses;
- exact target/conclusion;
- current status: analytic theorem / exact finite certificate / external certificate / audit-pending / conjecture / open / dead route;
- dependencies;
- whether the branch is exhaustive, local, or only a stress regime;
- what would close if that branch were eliminated.

In particular settle the nomenclature around “order-3 extremal”, “radius 3”, “Gate A”, “Gate B”, “one-excursion/full-phase”, “safe-CF”, and the current terminal-tail survivor. Do not assume that similarly named objects are identical.

## Gate 2 — radius-3 and Gate-B audit

Reconstruct the exact radius-3 closure from RL18/RL19 line by line.

Then reconstruct the bridge history:

- RL20 global bridge;
- RL43–RL48 same-root/full-phase attempts;
- RL48 four-swap construction;
- RL49 correction of the direct half-period radius-3 match.

State precisely:

1. what radius 3 proves locally;
2. why the RL48 direct invocation fails;
3. which Gate-B bridge ideas remain alive after RL49;
4. what exact new lemma would be needed for a genuine global RL→radius-3 connection.

Do not re-prove already audited radius-3 subcases unless a bundled verifier or theorem match fails.

## Gate 3 — Gate-A audit

Reconstruct the exact role of

`H >= t+3`.

Separate the uniform theorem from q-specific or safe-CF reductions.

Audit the method barriers:

- RL48 separable rank-relaxation barrier;
- RL50 height-one Collatz-conjugacy warning;
- any later local-mass route limitations.

Determine exactly which denominator/approximation regimes the safe continued-fraction reduction covers and which remain outside it.

This gate must answer whether killing the sole safe-CF survivor would close all of Gate A or only one restricted subtree.

## Gate 4 — audit the frozen RL60 increment

Only after the branch tree is reconstructed, inspect the RL60 terminal-tail claims.

### Internal finite thresholds

Audit `verification/residue_interval_cert.cpp` independently and replay the provided verifier script or an independent second implementation.

Check the claimed threshold table through

`N(39)=122,167,958,641`

and the derived

`z>=103,303,788,559`.

Keep finite computation separate from analytic consequences.

### External path-record reduction

Freshly audit the Barina path-record table/interface before promoting

`25 <= K <=129`.

If valid, record the exact resulting `z` interval from `K+z=q+3`.

If invalid or ambiguous, demote it cleanly without disturbing the internally certified K39 floor.

## Gate 5 — produce an authoritative “distance to closure” statement

The audit should finish with a concise but mathematically accurate answer to:

- Is the current safe-CF survivor the last open branch? If not, what remains?
- If it is eliminated, exactly what closes?
- What is the current status of Gate A globally?
- What is the current status of Gate B / the radius-3 bridge?
- Which branches have been neglected while RL50–RL60 focused on the survivor?
- Is any branch now obviously redundant because of later results?
- What are the smallest genuinely missing lemmas separating the current state from RL closure?

## Gate 6 — roadmap reset

Rank the next 3–5 research programs by expected leverage, not by continuity with the latest session.

At minimum compare:

1. resume the frozen safe-CF survivor using `t in {22,24,...,126}` if the external K bound survives audit;
2. develop a uniform Gate-A argument outside/above the safe-CF stress regime;
3. develop a genuinely new Gate-B bridge into the already-closed radius-3 theorem;
4. exploit the exact coupled height-one/full-phase invariants (`E`, telescoping, terminal power, backward grammar) in a way that is not merely a disguised global Collatz claim.

For each program give:

- exact theorem target;
- why it would matter globally;
- known blockers;
- best first experiment/lemma;
- stop/pivot criterion.

## Deliverables before any new deep proof attack

Create:

1. `RL61_AUTHORITATIVE_WHOLE_TREE_PROOF_STATE.md`
2. `RL61_BRANCH_DEPENDENCY_LEDGER.md`
3. `RL61_RADIUS3_GATEB_AUDIT.md`
4. `RL61_GATEA_AND_SAFE_CF_SCOPE_AUDIT.md`
5. `RL61_RL60_INCREMENT_REAUDIT.md`
6. `RL61_RANKED_RESEARCH_ROADMAP.md`

Only after those are complete should the session choose one branch for fresh extension.

## Closure discipline

Do not claim RL or Collatz is solved unless every top-level branch is explicitly discharged with hypotheses and dependencies checked.

Do not equate “sole safe-CF survivor” with “sole RL survivor.”

Do not treat a dead proof route as a dead theorem target.

Do not use arbitrary shortcut-Collatz settling as an assumption.

Do not silently promote external live computations or session-local scans to analytic theorems.

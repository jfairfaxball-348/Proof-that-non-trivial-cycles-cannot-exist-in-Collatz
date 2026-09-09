# RL291 — programme-wide audit, synthesis, overlap recovery, and fast-track review

Date prepared: 2026-09-09
Status: PREPARED, NOT STARTED

## Why RL291 exists

RL290 closed with considerable momentum on a gauge-invariant Bellman/checkpoint-kernel reformulation of Gate A.

The user has explicitly requested that this momentum be preserved but temporarily frozen because a broad programme review/audit is now more important.

RL291 is therefore an audit/synthesis session first, not a routine continuation session.

## Incoming proof state

RL290 closed as:

`GAUGE_INVARIANT_BELLMAN_CHECKPOINT_KERNEL_AND_HEIGHT_ONE_LAUNCHPAD_BARRIERS_PROVED`.

Gate A remains open with exact residual:

`k>=25`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen.

Fifth selector remains unscanned.

Radius 6+ remains frozen.

No global non-trivial-cycle exclusion is claimed.

## Mandatory mission

Produce a broad, authoritative audit of the research programme as it currently stands.

The audit must recover and reassess the programme era-by-era rather than reading only the latest handovers.

At minimum review approximately:

1. pre-RL100;
2. RL100-RL199;
3. RL200-RL269;
4. RL270-RL290, with especially close attention to the Gate-A work from roughly RL279 onward.

The exact cut points are organizational, not mathematical; adjust them if the repository structure suggests better natural eras.

## Required audit questions

For each era identify:

- the main proof objects and formulations introduced;
- promoted lemmas/theorems/certificates that remain valid;
- claims later corrected, demoted, superseded, or reinterpreted;
- routes that were abandoned and the exact reason;
- finite evidence versus analytic theorem;
- assumptions that entered later work implicitly;
- objects that later reappeared under different names;
- results whose significance changed after newer theorems;
- any old theorem that becomes stronger or more useful when combined with late-stage knowledge.

Across eras, explicitly search for:

- duplicate or equivalent invariants;
- hidden algebraic identities between separate ledgers;
- repeated rediscovery of the same obstruction;
- opportunities to merge proof routes;
- places where one later theorem discharges an older missing hypothesis;
- older finite reductions that may now become scalable;
- exact inequalities or congruences that were abandoned only because a then-missing bridge is now available;
- route barriers that should permanently remove tempting but dead directions;
- possible shortcuts / fast tracks that could bypass the current long route;
- any combination that could incidentally close Gate A or materially contract the residual without reopening a disallowed brute-force programme.

## Audit of opportunistic / unprompted work

The user specifically noted that there has been substantial unprompted or opportunistic work.

RL291 must explicitly distinguish:

- user-directed research;
- strategically justified pivots;
- useful opportunistic discoveries;
- route proliferation that produced little enduring value.

Do not discard useful mathematics merely because it arose opportunistically.

But do identify where the programme accumulated concepts without enough consolidation.

The desired outcome is a smaller, clearer authoritative map of what actually matters.

## Special late-stage review

Closely review the chain:

- RL279 scalable zero-rank / boundary conjugacy;
- RL280-RL282 positive excursion and terminal-backward work;
- RL283 upstream 2-adic reachability and boundary hazard;
- RL284 labelled accelerated reversibility;
- RL285 global 2-adic / Ferrers reformulation;
- RL286 component carry;
- RL287 phase transport and height-bounded skeleton;
- RL288 fixed-seed synchronization;
- RL289 affine ballot bijection / rejected tubes;
- RL290 seam gauges / Bellman checkpoint kernel / height-one launchpads.

Determine which of these are genuinely different and which are now known to be projections of one common structure.

RL290 already suggests important overlaps:

- RL282 pure-zero terminal tails extend to exact height one;
- RL283 `Beta` is the one-generation valuation projection of RL290's height-one Bellman kernel;
- RL284 labelled accelerated inverse rays are exactly present in RL290's stripped-unit predecessor rays;
- RL289's mixed-state minimum-area formulation and RL290's future-threat Bellman formulation are dual views of the same path-cost obstruction;
- RL287's zero-height boundary macros are exactly what RL290 quotients into checkpoint macro-edges.

Audit these carefully rather than assuming the interpretation is complete.

## Bellman route: preserve but do not privilege

The live RL290 route is:

`fixed-seed ancestry`
vs
`minimum historical area required to enter high Bellman-threat positive checkpoints`.

Key frozen objects include:

- post-departure seam variables `B,C`;
- exact gauge barriers from neutral prefixes, boundary cycles, mergers, and equal-area diamonds;
- future-threat envelope `Bcal`;
- positive-even checkpoint Bellman operator `V`;
- exact height-one successor kernel;
- universal exact height-one terminal launchpads;
- stripped-unit / labelled-accelerated renormalization;
- genuine chain `2514 -> 5378 -> 21842 -> 8192`.

This route has substantial momentum and must not be lost.

However RL291 must not assume it is the best continuation.

Compare it against the whole historical programme and report whether another route is now shorter, stronger, or newly viable.

## Fast-track / shortcut review

After the audit, explicitly produce a ranked shortlist of plausible next directions.

Include:

- any direct theorem that now appears close enough to attack immediately;
- any old route newly unlocked by later lemmas;
- any finite-to-analytic bridge that now looks realistic;
- any duality/equivalence that collapses two open problems into one;
- any proof-by-contradiction route using the fixed seed plus a terminal structure;
- any route that would materially contract the residual even without full closure.

A shortcut is welcome even if it does not use the RL290 Bellman framework.

Do not manufacture novelty for its own sake.

## Red-team requirement

The audit must actively search for:

- hidden dependence on unpromoted finite evidence;
- stale checkpoint assumptions;
- overstatements that survived through handovers;
- duplicated lemmas counted as independent constraints;
- incorrect promotion status;
- silent use of results from abandoned formulations;
- places where a barrier theorem was later forgotten;
- contradictions between eras.

If a correction is needed, state it explicitly and prioritize repair before new mathematics.

## Expected deliverables

RL291 should produce:

1. a programme-wide audit report;
2. an era-by-era theorem/object map;
3. an overlap/equivalence map;
4. a correction/demotion ledger if needed;
5. a list of permanently dead principal routes;
6. a list of live proof ingredients;
7. a ranked shortlist of next attacks / shortcuts;
8. a recommendation on whether to resume the RL290 Bellman route or pivot;
9. a compact plain-English summary of the current proof state.

A new mathematical theorem is not required for RL291 to succeed.

## Research discipline

Do not begin a large new exploratory attack before the audit is substantially complete.

If the audit reveals an immediate contradiction, correction, or nearly mechanical theorem-sized closure, it may be handled.

Otherwise freeze candidate new attacks as recommendations for the next research session.

Do not reopen Gate B, fifth selector, Radius 6+, or brute-force height-cap expansion as a substitute for the audit.

## Sources and authority

Treat current `main`, `authoritative/`, promoted session reports, theorem ledgers, verifier records, and correction/red-team files as authoritative in the repository's normal order.

Do not rely on conversation memory for mathematical authority.

Generated knowledge catalogues may be stale; use them as navigation aids only where consistent with authoritative session material.

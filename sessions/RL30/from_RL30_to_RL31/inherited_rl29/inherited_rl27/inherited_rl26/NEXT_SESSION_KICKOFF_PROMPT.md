Continue the RL/3n+1 research from the attached `Collatz_Rsharp_RL26_to_RL27_Handover_2026-08-21.zip` as a skeptical research mathematician.

Start by verifying `SHA256SUMS.txt`, then run all 19 `continuation/verify_rl*.py` scripts. Treat any verifier failure as a stop-and-repair event. Read `START_HERE.md`, `RL26_PROOF_STATUS_AND_NEXT_ATTACK.md`, and the RL24/RL25/RL26 notes named there before extending anything. Do not reopen radius-3 closure or already frozen RL21--RL26 branches unless a verifier/dependency failure requires it.

RL remains open. Keep proof status explicit: distinguish ANALYTIC results, EXACT FINITE CERTIFICATES, the inherited EXTERNAL COMPUTATIONAL INPUT `R>=2^71`, and finite trajectory witnesses that are not cycles.

Primary goal: attack the unique surviving exceptional cubic/weak-close geometry by coupling, rather than studying separately,

- the forced hard least-root prefix `11011...`;
- the inherited weak-close root class `R==91 mod288`;
- exact weak cubic gaps `G=12`, `H=4`;
- the RL20 exceptional final return `(n_close,t_close)=(1,1)`;
- the RL23 exact local packing saturation mechanism and the RL24 global valuation-supporting-line anchors.

Seek a nonlocal adjacent-block numerator/valuation lemma. In particular test whether root departure, the two balanced block words, and the exceptional final return force incompatible valuations, extra common-prefix divisibility, forbidden block adjacency, or a frequency restriction on the high-valuation exceptional core. A useful alternative is a numerator-difference cancellation specific to this sector that materially reduces the remaining `O(eY)` cubic upper bound.

Do not spend the session merely tightening the same six independent local packing inequalities or extending residue sieves without coupling them to closure: RL23/RL26 already exhibit infinite residue-compatible saturation segments. Keep the `g=2` factor branch secondary unless it produces a mechanism relevant to this exceptional geometry.

Before closing the session, update the proof ledger, add exact verifiers for any new finite/symbolic claims, rerun the full suite, and create the next zipped handover.

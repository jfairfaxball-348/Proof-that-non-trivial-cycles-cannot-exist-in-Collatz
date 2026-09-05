# RL251 — Gabriel's-horn capacity/discreteness exploration target

Date prepared: 2026-09-05
Mode: **temporary idea exploration; authoritative standards retained**

## Purpose of this session

Temporarily freeze the current active mathematical attack exactly where it stands.

Do **not** discard, rewrite, weaken, supersede, or reorganise the current authoritative target merely to accommodate this pivot. The existing line remains the clean return point recorded in `RL251_FROZEN_RETURN_TARGET.md`.

Instead, investigate whether the Gabriel's-horn-inspired proof architecture below can produce a genuinely useful new route toward closing RL.

If the pivot proves unfruitful, inconclusive, circular, or merely equivalent to machinery already possessed, explicitly close the pivot and return the handover target to the frozen authoritative line.

## Core idea to investigate

Gabriel's horn illustrates an important distinction: a surviving space may become arbitrarily small, or even have vanishing measure, without becoming empty.

Existing RL machinery has repeatedly narrowed admissible configurations using structures such as 2-adic cylinders, valuation restrictions, packing arguments, physical strips, transition obstructions, interval elimination, residue restrictions, increasingly deep finite-stage compatibility conditions, and other quantitative upper bounds on surviving RL configurations.

The pivot question is:

**Can these existing upper/narrowing results be paired with a genuinely discrete lower bound on the minimum "capacity", "width", "mass", "multiplicity", "room", or arithmetic structure required by even ONE genuine RL configuration?**

The desired architecture is conceptually `upper capacity available at depth k -> 0`, while independently `minimum capacity required by one genuine RL at depth k` remains large enough that eventually `available capacity < minimum cost of one RL`.

If rigorous, the infinite taper cannot continue. Metaphorically: Gabriel's horn can taper forever because its cross-section is continuously divisible. An RL configuration may instead be arithmetically quantised: eventually the admissible horn could become narrower than one indivisible RL "brick".

The mathematical task is to determine whether anything resembling this actually exists in the RL framework.

## Important distinction

Do **not** confuse any of the following with closure: density tending to zero; measure tending to zero; exponentially shrinking cylinder size; convergent sums of surviving capacities; probability-zero heuristics; an arbitrarily narrow interval; or arbitrarily high 2-adic precision.

A nested sequence `C_0 superset C_1 superset C_2 ...` can satisfy `mu(C_k)->0` while still containing one coherent infinite point.

Therefore the critical question is not merely "How small can we make the surviving RL space?" It is:

**Can a genuine RL possess an infinite compatible path through every finite restriction, and if not, what quantitative/discrete obstruction eventually prevents it?**

## Phase 1 — Audit existing machinery before inventing anything

Start from the latest authoritative ledger, checkpoint, session state, theorem/lemma inventory, and relevant current authoritative files. Preserve the frozen return line.

### A. Candidate upper/capacity side

Search the existing repo carefully for existing lemmas involving: 2-adic measure or cylinder depth; number of admissible residues; packing bounds; strip widths; interval lengths; block-count bounds; prefix defects; physical restrictions; valuation budgets; transition capacity; nested restrictions; geometric tier bounds; Farey/denominator restrictions; finite covering/cascade arguments; and any quantity decreasing monotonically as RL constraints deepen.

Extract these into a common schematic form where possible. Do not force incomparable quantities into one framework unless the identification is rigorous.

### B. Candidate lower/minimum-cost side

Search much more critically for any theorem or lemma saying that ONE genuine RL must consume or exhibit a nonzero discrete amount of something. Possibilities include: minimum number of residues; minimum interval separation; minimum multiplicity; minimum denominator/numerator spacing; integrality forcing a unit-sized gap; valuation granularity; minimum block occupancy; minimum transition count; minimum physical strip width; minimum determinant/resultant size; minimum lattice spacing; minimum admissible integer gap; parity or congruence granularity; product-formula/integrality lower bounds; a minimum amount of combinatorial branching needed for return; and any exact "one surviving RL costs at least X" statement.

"Capacity" and "cost" are conceptual names only. Use whatever exact invariant the mathematics naturally supports.

## Phase 2 — Attempt to formulate the bridge

If credible ingredients exist, try to formulate a precise statement `U_k < L_k` for sufficiently large/deep `k`, where `U_k` is a rigorous upper bound on the total room available to an RL-compatible object after current restrictions and `L_k` is a rigorous lower bound on the minimum room required by one actual RL-compatible object.

The quantities must be genuinely comparable and inhabit the same space/resource. Do not compare unrelated quantities merely because one tends to zero and another tends to infinity. Investigate several candidate invariants if necessary.

## Phase 3 — Infinite-path obstruction

Also investigate the equivalent topological/combinatorial formulation. The restrictions may define a tree of finite admissible prefixes/configurations. At every finite level some nodes may survive. The closure question is whether an infinite compatible branch exists.

Determine whether existing RL constraints establish something stronger than decreasing density, for example: eventual emptiness of a level; well-foundedness of the admissibility tree; bounded branch depth; unavoidable incompatibility between sufficiently separated constraints; failure of compactness caused by an arithmetic condition; finite certificates excluding every infinite branch; a descending integer-valued invariant that cannot descend indefinitely; or minimum separation/granularity conflicting with asymptotic narrowing.

Be explicit that ordinary nested compactness may work **against** exclusion. If every finite system is compatible inside an appropriate compact space, an infinite compatible point may exist. Identify exactly what breaks such an argument if claiming exclusion.

## Phase 4 — Compare with current Gate architecture

Answer explicitly:

1. Is this simply another presentation of the current Gate A narrowing argument?
2. Does it strengthen Gate A?
3. Could it convert a measure/density-tends-to-zero result into exact emptiness?
4. Does it require a new lower-bound lemma?
5. Is that lower-bound lemma already possessed implicitly?
6. Would the proposed bridge, if proved, close Gate A, close RL, or merely create another intermediate obstruction?
7. Is Gate B relevant to this architecture at all?

Do not overclaim closure.

## Phase 5 — Stress-test aggressively

Red-team any proposed Gabriel's-horn bridge. Construct abstract countermodels where possible in which all finite-stage capacities shrink to zero, every finite restriction is satisfiable, and nevertheless one infinite compatible point survives. Use these models to isolate the extra arithmetic discreteness actually needed.

Also test whether a proposed minimum RL cost itself shrinks with depth quickly enough that `U_k<L_k` never occurs.

Check for circular dependence on RL nonexistence; hidden compactness assumptions; confusing measure zero with emptiness; comparing quantities in incompatible normalisations; lower bounds disappearing after rescaling; statements true only for finite truncations; dependence on numerics where a proof is required; and assumptions failing for a single exceptional configuration.

The pivot counts as promising only if it survives these attacks.

## Preferred outcome hierarchy

### Outcome A — Strong success

Produce a rigorous new bridge theorem or clearly isolated lemma target of the form `existing shrinking/capacity machinery + explicit arithmetic minimum-cost lemma => no infinite RL-compatible branch`. If the missing lemma is narrow and well-defined, promote it as a serious future target.

### Outcome B — Partial success

Show that existing machinery already provides a strong upper/capacity half and identify precisely the missing lower/discreteness statement required to turn it into emptiness. State the missing statement cleanly enough for a future session to attack directly.

### Outcome C — Equivalence

Show rigorously that the Gabriel's-horn formulation is merely a repackaging of an existing authoritative target. Record the conceptual clarification but do not divert the research programme. Return the next target to the frozen authoritative line.

### Outcome D — Failure

Show that the analogy cannot be upgraded into useful mathematics, for example because an infinite compatible 2-adic point can survive arbitrary narrowing and no independent granularity lower bound is available. Document why, terminate the pivot cleanly, and restore the frozen target.

A negative result is useful if it prevents repeated future exploration of the same idea.

## Session discipline

Before changing anything in RL251: identify the current authoritative checkpoint; identify the active target frozen by RL250; record `RL251_FROZEN_RETURN_TARGET.md` explicitly as the RETURN TARGET; and preserve all existing frozen files unchanged unless normal bookkeeping genuinely requires otherwise.

Do not silently replace the proof programme with this pivot. Do not promote speculative statements into the lemma/proof ledger.

Clearly classify findings as proved; derived from existing proved lemmas; computationally observed; heuristic; conjectural; or failed.

Prefer reusing existing proven machinery over inventing large amounts of new mathematics. If a small new lemma naturally emerges and can be proved rigorously, pursue it. Continue beyond the first superficial observation. The purpose is to determine whether this architecture genuinely has mathematical teeth.

## Closeout requirements for RL251

At session end, produce a concise pivot verdict containing:

1. **Frozen return point** — the exact authoritative target/workstream frozen at session start.
2. **What was tested** — the Gabriel's-horn upper-capacity / lower-discreteness architectures examined.
3. **Existing lemmas reused** — authoritative ingredients actually used.
4. **Strongest rigorous conclusion** — no metaphor; state the strongest theorem/lemma/proposition actually justified.
5. **Missing bridge** — if promising, state the smallest clean mathematical statement still required.
6. **Pivot verdict** — choose exactly one:
   - `PROMISING — continue pivot`
   - `PROMISING BUT BLOCKED — isolate missing lemma`
   - `EQUIVALENT TO CURRENT WORK — return to frozen line`
   - `UNFRUITFUL — return to frozen line`
7. **Next authoritative target** — if promising, one precise next attack; otherwise restore `RL251_FROZEN_RETURN_TARGET.md` exactly.

## Central steering question

Keep returning to this throughout RL251:

**Are we merely proving that hypothetical RLs occupy less and less space, or can arithmetic discreteness prove that eventually there is not enough space for even one RL?**

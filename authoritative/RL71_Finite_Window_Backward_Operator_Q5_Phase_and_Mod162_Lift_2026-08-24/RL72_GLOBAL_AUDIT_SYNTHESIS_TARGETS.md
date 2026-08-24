# RL72 — GLOBAL AUDIT, LEMMA INVENTORY, SYNTHESIS, ROADMAP, AND CLOSURE TARGETS

Date prepared: 2026-08-24

## Purpose

RL72 is deliberately **not** a routine continuation of the backward-digit ladder. It is a global audit/review/planning and synthesis session across the searchable GitHub history, with one goal above all others:

> **identify the smallest combinations of already-proved lemmas that can close a genuinely global branch, and actually attempt those combinations before inventing more local machinery.**

The GitHub repository now provides searchable extracted mirrors under `sessions/RLXX/`, immutable historical archives under `Archive/`, and a small current `authoritative/` head. Use the searchable mirrors for discovery and comparison, but preserve provenance: where a claim becomes load-bearing, its authoritative bundle/ledger/checksum status controls.

The verification-economy rule remains in force. Do not recursively rerun seventy sessions of expensive finite computation. Verify the current RL71 gate, use frozen ledgers as the inherited proof-state baseline, and open old source files selectively when a candidate synthesis depends on their exact hypotheses.

---

## 1. Mandatory deliverables

Before RL72 ends, produce all of the following.

### A. Global lemma catalogue

Build a structured catalogue of every potentially reusable theorem/lemma/certificate from the historical programme, at minimum covering RL18–RL71 and selectively earlier sessions where the radius-3 tree or global identities depend on them.

For each item record:

- stable ID;
- session and source file;
- exact statement/output;
- exact hypotheses/input;
- status: analytic theorem / exact finite certificate / external computational certificate / computational evidence / conjecture / dead route / method barrier / superseded or corrected;
- dependencies;
- later corrections or scope restrictions;
- what current theorem can consume it;
- what would close if it were combined successfully;
- whether it distinguishes a genuine RL object from local/coboundary countermodels.

Do **not** catalogue merely by title. Record the mathematical interface of each lemma: what data goes in and what usable inequality, congruence, divisibility, geometry, or state information comes out.

### B. Correction and demotion ledger

Explicitly preserve all later repairs, including at least:

- RL59 decreasing-height terminal potential: rejected/repaired by RL62;
- finite `H<=24`: exact finite certificate only, never a uniform theorem;
- RL48 separable rank-relaxation: barrier theorem, not Gate-A falsification;
- RL49 correction to the RL48 half-period/radius-3 geometry;
- RL50 height-one shortcut-Collatz conjugacy warning;
- RL64 exact full-phase ownership definition;
- state/phase agreement: compatibility, not contradiction;
- local congruence + CRT: not Gate-A closure;
- `J<=2^H`: conjectural bounded evidence only;
- all RL62–RL71 classifications and scope restrictions.

Any historical claim contradicted by a later ledger must be marked superseded and must not be used silently.

### C. Dependency DAG and closure matrix

Update the RL61 whole-tree dependency graph through RL71. For each open top-level obligation, show:

1. exact currently available inputs;
2. exact missing edge/lemma;
3. whether discharging it closes a local family, a Gate-A sector, all Gate A, Gate B, all RL, or only a stress regime.

Create a **closure matrix** so it is impossible to confuse “kills one survivor” with “closes a global branch.”

### D. At least three serious synthesis attempts

Do not stop at inventory. Attempt at least three combinations of old + new machinery, with exact algebra or counterexample checks. At least one must target Gate A and at least one Gate B or a direct full-phase contradiction.

Record each as:

`candidate -> exact hypotheses -> derivation -> contradiction/closure OR precise failure -> reusable lesson`.

A failed synthesis is valuable only if the failure is exact enough to retire or narrow a route.

### E. Ranked roadmap with stop/pivot criteria

End with no more than 1–3 primary theorem targets. Each target must state:

- exact theorem statement;
- why it has global leverage;
- prerequisites already proved;
- smallest missing step;
- falsification/red-team test;
- what closes if proved;
- explicit stop/pivot criterion.

Do not default to q=6/q=7 merely because it is locally available.

---

## 2. Baseline global tree to audit and update

Use the RL61 whole-tree audit as the pre-RL62 baseline, then audit only the delta RL62–RL71 plus any older source needed for exact interfaces.

The inherited RL61 global picture was:

- exact radius-3 local theorem: **closed** through RL19, under its exact primitive `D`-divisible hypotheses;
- Gate A uniform terminal-area/valuation obligation: **open**;
- Gate B global RL-to-closed-obstruction bridge: **open**;
- local endpoint/final-return grammar bridge: **dead route** by RL20 countermodel;
- direct RL48 half-period radius-3 invocation: **dead route** after RL49 even-distance correction;
- RL48 separable cap/room + total-displacement relaxation: **method barrier** for large `z`;
- height-one dynamics stripped of full-phase constraints: exact shortcut-Collatz conjugacy warning (RL50).

RL62–RL71 materially changed Gate-A local information and ownership/phase precision, but no session has yet legitimately upgraded Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or Collatz itself.

---

## 3. High-priority historical lemma families to inventory

This list is a starting map, not permission to omit other useful lemmas discovered in GitHub.

### Family G — radius-independent/global RL identities (RL18–RL20)

Audit and interface-map at least:

- arbitrary-radius orbit polynomial / `D|Q` equivalence;
- RL19 positive lift
  `Z=sum_i 2^i 3^(-P_i)=(lambda-1)(4R+1)`;
- RL19 weighted-difference identity
  `sum_i q_i(3^(-G_i)-1)=4(lambda-1)(R_m-R)`;
- weighted populations
  `sum_(d_i=1)q_i=3R(lambda-1)`,
  `sum_(d_i=0)q_i=(R+1)(lambda-1)`;
- odd-step product
  `lambda=prod_(d_i=1)(1+1/(3x_i))`;
- global state-packing / near-resonance dichotomies;
- RL20 balanced-return weighted-difference route;
- RL20 strict-excursion packing route;
- exact RL20 local radius-4 countermodel and precisely which missing genuine-RL hypothesis it violates.

Question: can later full-phase ownership/state selectors turn any old identity into a nonzero integer `W` with

`D | W` and `0<|W|<D`?

### Family R3 — exact radius-3 closed theorem (RL7–RL19)

Do not reprove the tree. Catalogue its **input contract** exactly:

- cyclic adjacent-transposition distance exactly 3;
- primitive word;
- genuine `D`-divisibility;
- orientation/support/gcd sector requirements;
- any older LMN + finite dependencies.

Question: can any later ownership/full-phase lemma manufacture *all* these hypotheses from a genuine RL object? No partial bridge counts.

### Family D — defect/zero-position/phase-rank coupling (roughly RL43–RL56)

Audit especially:

- RL43 dependency map and invariant candidates;
- RL48 phase-to-rank-defect bridge;
- RL48 same-root selector / phase collapse;
- RL48 rank-relaxation barrier;
- RL54 uniform defect reduction;
- zero-position telescoping and defect-energy normalizations inherited around RL48–RL55;
- aggregate/late-mass work in RL55–RL56.

Question: can these nonseparable quantities consume RL65–RL71 exact rank-tail digits/residue floors to produce a lower bound scaling with the Gate-A target rather than a separable local cap?

### Family O — ownership/full-phase exactness (RL63–RL71)

Audit the exact current interfaces:

- RL63 even-exit selector / ownership target;
- RL64 full-phase recovery and exact ownership definition;
- RL65 rank-tail phase selector;
- RL66 last-active rank and phase digit ladder;
- RL67 previous-active interface and height-one reachability;
- RL68 nested descent and backward-digit ladder;
- RL69 third backward digit, q=3 phase match, mod-54 selector;
- RL70 fourth backward parity, q=4 match, residue floor;
- RL71 finite-window backward operator, q=5 match, mod-162 selector/floor.

Question: which of these outputs is genuinely **new global information** when paired with older identities, rather than merely a different encoding of the same displacement data?

---

## 4. Mandatory synthesis programmes

### Synthesis A — coupled Gate-A lower bound

Try to combine:

- RL48/RL54 defect-energy or zero-position telescoping;
- the exact full-phase ownership/rank-tail machinery RL64–RL71;
- RL71 residue floor `H>=delta_p+c_162`;
- exact terminal geometry / tail classes.

Target a theorem of the form

`H >= k`

in the current retained Gate-A notation (or rigorously translate to the inherited equivalent formulation if using older `t,z,e,q` notation).

A useful intermediate result is acceptable if it eliminates an **infinite** interface/tail family, not merely a finite scan.

Red-team against the RL48 separable witnesses: if the derivation survives after forgetting the coupled phase labels, it is probably too weak.

### Synthesis B — low-k / mod-162 exact-value closure

RL71 proves that inside a hypothetical nested violation with odd `k<=165`,

`delta_*=c_162`

exactly. Combine this with:

- exact tail-class formulas (all-`00`, mixed, nonmaximal all-`11`, allowed maximal all-`11`);
- terminal `R mod 243` or higher residues already available;
- area/order constraints on the earlier active ranks.

Try to close a nontrivial infinite congruence family or a full low-`k` nested sector. Do not confuse a bounded verifier absence with proof.

### Synthesis C — global ownership/divisibility Gate-B bridge

Return to RL20's two surviving global routes:

1. balanced-return weighted difference;
2. strict-excursion packing.

Inject the strongest later exact ownership/full-phase data from RL43–RL71. Seek either:

- `D|W`, `0<|W|<D`; or
- a pair satisfying **every** exact radius-3 input condition.

Reject any candidate that also holds in the RL20 `D∤Q` radius-4 local countermodel. That countermodel is a mandatory unit test for Gate-B candidates.

### Synthesis D — direct full-phase impossibility

Try a normalization combining:

- terminal power/state;
- defect/zero-position telescoping;
- rank-tail phase digits;
- full denominator `D` and ownership;
- global weighted difference/populations.

Again prefer a size-divisibility contradiction template. Retire the normalization immediately if it is an exact coboundary, vanishes identically, factors only through a proper divisor, or does not distinguish genuine RL ownership.

---

## 5. RL71-specific strategic constraint

RL71 proves a reusable finite-window theorem: every extra 3-adic digit exposes only one additional earlier rank, and the state/phase rank-tail encodings can be continued to any fixed finite depth.

Therefore:

> **Do not treat “derive q=6, then q=7” as a primary research programme unless the global audit identifies a specific downstream theorem that consumes those extra digits.**

Further digits are permitted as a supporting lemma only when a synthesis above needs them.

---

## 6. What “closer to closing something” means in RL72

Prefer outcomes in this order:

1. close Gate A or Gate B globally;
2. eliminate an infinite, previously open top-level interface/tail family;
3. prove a new global coupled lower bound that strictly narrows the missing Gate-A theorem;
4. manufacture a valid radius-3 bridge for a globally exhaustive family;
5. rigorously retire a major research route by a theorem/countermodel, thereby reducing the roadmap;
6. only then, improve finite precision or bounded scans.

The session should explicitly say which level was achieved.

---

## 7. Close-out requirement

RL72 is a standalone global audit/synthesis session. Before ending, freeze:

- lemma catalogue;
- correction/demotion ledger;
- dependency DAG;
- closure matrix;
- synthesis attempts and exact failures/successes;
- ranked 1–3 target roadmap;
- verifier/provenance status;
- the exact authoritative resulting proof state.

Then create the next numbered authoritative handover bundle and matching SHA-256 sidecar under the established repository workflow.

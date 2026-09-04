# RL247 target — Radius-3 / Radius-4 Sign, Domain, Cyclic-Distance, and Dependency Audit

Status: **PREPARED, NOT STARTED**.

This is a targeted mathematical integrity audit of the existing Radius-3 / Radius-4 theorem chain.

It is not a request to advance the current RL mathematical target unless the audit itself proves that a repair is required.

Preserve the current authoritative research state. Do not silently change, strengthen, weaken, or replace any theorem. If a correction is necessary, record it explicitly through the existing correction/demotion/proof-state machinery.

## Trigger for this audit

An external audit found the following exact counterexample to an over-broad formulation of the Radius-4 theorem.

Take

`d=00011110111`, `A=11`, `L=7`.

Then

`D=2^11-3^7=-139`

and, for the standard Collatz cycle numerator,

`Q(d)=18904=(-139)(-136)`.

Thus `D | Q(d)` and the corresponding integer cycle has starting value

`n=Q(d)/D=-136`.

This is a genuine negative Collatz cycle.

Moreover, the one-step cyclic rotation of `d` is at cyclic adjacent-transposition distance exactly `4`.

Therefore the unrestricted statement

> “No primitive binary word satisfying `D | Q(d)` has a nontrivial cyclic rotation at exact cyclic adjacent-transposition distance `4`”

is false.

For the ordinary positive Collatz-cycle problem, however, `Q(d)>0` and positivity requires

`D=2^A-3^L>0`.

The intended Radius-3 and Radius-4 machinery may already have lived entirely inside this positive-`D` domain. This audit must determine that from the actual proofs rather than assuming it.

---

## Primary questions

### 1. Exact theorem scope

Recover the exact authoritative Radius-3 theorem and exact authoritative Radius-4 theorem as actually proved.

For each theorem state explicitly:

- the ambient number domain;
- whether the object represents a positive Collatz cycle, arbitrary integer cycle, or something narrower;
- whether `D>0` is assumed, derived, used implicitly, or absent;
- whether positivity of the canonical states is assumed or proved;
- whether “full-D” was intended to mean merely `D | Q(d)`, or a stronger positive/full-phase object;
- primitivity requirements;
- exact cyclic-rotation requirements;
- exact definition of adjacent-transposition distance.

Do not infer scope from filenames or later summaries. Read the proof.

### 2. Negative-cycle test

Run the explicit negative-cycle word

`00011110111`

through every Radius-3 / Radius-4 definition and theorem hypothesis.

Identify the first exact hypothesis it fails.

If it satisfies all written hypotheses of a promoted theorem whose conclusion excludes its observed rotation, then that theorem is false as written and must be demoted or repaired.

If it fails because `D>0`, positivity, physical-state ownership, or an equivalent positive-cycle hypothesis is already present, document that precisely.

Do not dismiss the example merely because it is negative. Use it as a regression test for theorem scope.

### 3. Radius-3 provenance

Determine whether the inherited Radius-3 theorem has the same potential scope ambiguity.

Specifically search for any statement equivalent to `D | Q(d)` being treated as sufficient for the theorem without also restricting to the positive-cycle domain.

Check whether known negative integer Collatz cycles provide Radius-3 counterexamples or expose any analogous cyclic-distance issue.

If Radius-3 is already correctly positive-domain scoped, record the exact source establishing this.

If Radius-3 requires correction, propagate that correction forward through every theorem that inherited it.

### 4. Cyclic versus linear transposition distance

Independently verify that the Radius-3 and Radius-4 proofs use the same distance notion as their theorem statements.

In particular distinguish:

- adjacent swaps on a linear word;
- adjacent swaps on a cyclic word where positions `A-1` and `0` are adjacent;
- transport flows after choosing a cut/root;
- wrap-around flow across that cut.

Audit whether a cyclic wrap-around can introduce an omitted circulation/holonomy term when the transport is represented linearly.

The negative `A=11` example must be used as a concrete regression test here.

Do not accept “all flow topologies were enumerated” unless the enumeration genuinely contains cyclic wrap-around cases or proves why they reduce to the enumerated forms.

### 5. Numerator / rotation algebra

Re-derive, from the standard exact Collatz numerator identity, the change in `Q(d)` under the elementary adjacent swaps used by Radius-3 and Radius-4.

Check:

- orientation conventions;
- choice of cyclic root;
- shifts crossing the chosen root;
- whether `Q(rho^s d)` is related to `Q(d)` with any additional `D`-multiple term;
- whether such a term was discarded because it vanishes modulo `D`, and whether that is legitimate for every later integer equality rather than only congruences.

Identify any place where a congruence modulo `D` was silently promoted to an exact equality.

### 6. Sign-sensitive inequalities

Search Radius-3 and Radius-4 for every use of

`D>0`, `2^A>3^L`,

or equivalent inequalities involving

`2^A/3^L>1`.

Classify each use as:

- explicit hypothesis;
- derived from positivity;
- inherited external theorem;
- accidentally unstated assumption.

Particular care is required for continued fractions, logarithmic estimates, Baker/LMN bounds, and finite cutoffs, because reversing the sign of `D` changes the relevant side of the resonance inequality.

### 7. Dependency / circularity audit

Construct a concise dependency DAG for Radius-3 and Radius-4.

For every external ingredient—finite Collatz verification, lower bounds on hypothetical cycle size, Simons–de Weger style cycle bounds, continued fractions, Baker/LMN results, etc.—state:

- exact theorem imported;
- exact direction in which it is used;
- whether it assumes only the existence of a hypothetical cycle;
- whether it is independent of Radius-3 / Radius-4;
- whether it already assumes the nonexistence conclusion we ultimately seek.

Using a rigorous lower bound of the form

`hypothetical cycle => A>N`

is not circular merely because it excludes smaller cycles.

Flag circularity only if a dependency actually assumes or depends on the global nonexistence result being proved.

### 8. Positive Radius-4 theorem

After the audit, determine the strongest theorem that is genuinely justified.

The expected candidate is something of the form:

> Let `d` be a primitive cyclic parity word of a positive Collatz cycle, with `D=2^A-3^L>0` and `D | Q(d)`. Then no eligible nontrivial cyclic self-rotation of `d` has exact cyclic adjacent-transposition distance `4`.

Do not promote this wording merely because it avoids the negative counterexample.

It must be the theorem actually proved by the Radius-4 argument.

If further hypotheses are necessary—for example physical ownership, full phase, canonical-root conditions, or some narrower definition of “full-D”—state all of them explicitly.

### 9. Impact on the current Gate-B programme

Determine whether the current Radius-4 global-bridge programme works entirely inside the repaired positive-domain theorem.

In particular check that every retained object used by RL240+ satisfies, before Radius-4 is invoked:

- positivity;
- `D>0`;
- primitivity;
- genuine full-D ownership;
- the exact cyclic-distance convention;
- every other Radius-4 hypothesis.

If yes, classify the issue as a theorem-statement/provenance repair rather than a mathematical failure of Gate B.

If no, identify exactly which current dependency is invalid.

---

## Required outcomes

Finish with exactly one of the following mathematical classifications:

### `R3_R4_SCOPE_AUDIT_PASS`

Use only if Radius-3 and Radius-4 were already proved in the correct positive-cycle domain and the negative example merely exposes an over-broad later paraphrase.

Repair all misleading summaries/statements so `D>0` or the equivalent positive-cycle hypothesis is explicit.

### `R3_R4_STATEMENT_REPAIR`

Use if the underlying proofs are sound after explicitly restricting their theorem statements to the positive-cycle domain, but promoted wording or inherited scope was too broad.

Record a formal correction ledger entry and propagate the repaired statement forward.

### `R3_R4_PROOF_REPAIR_REQUIRED`

Use if some proof step relies on positivity/`D>0` without having legitimately established it, omits cyclic wrap-around cases, mishandles numerator holonomy, or otherwise contains a repairable mathematical gap.

Stop ordinary Gate-B advancement until repaired.

### `R3_R4_THEOREM_DEMOTED`

Use if a genuine counterexample survives all intended positive-cycle hypotheses or a foundational Radius-3/4 argument fails without an available repair.

Propagate the demotion through every dependent current claim.

---

## Mandatory regression tests

At minimum preserve these permanently:

1. **Negative Radius-4 regression**

   `d=00011110111`, `A=11`, `L=7`, `D=-139`, `Q=18904`, `n=-136`,

   with a nontrivial rotation at cyclic adjacent-transposition distance `4`.

   Any theorem intended only for positive cycles must reject this example through a named hypothesis.

2. **Trivial positive-cycle regression**

   Verify the ordinary positive trivial cycle against the repaired definitions and ensure it is not accidentally excluded through a malformed sign or primitivity condition.

3. Add any smallest Radius-3 negative-cycle regression discovered during this audit.

---

## Process constraints

- Do not do unrelated new mathematics.
- Do not start Radius 5.
- Do not claim Gate A or Gate B closure during this audit.
- Do not treat an AI-generated proof-status label as evidence.
- Do not silently rewrite history.
- Preserve historical files; use correction/demotion ledgers and current authoritative summaries.
- Prefer exact algebra and executable finite regression tests over prose assurances.
- Do not search the entire session archive blindly. Trace only live Radius-3 / Radius-4 provenance and dependencies.
- If running inside an active RL session, preserve the current mathematical target and return to it only after this audit has reached one of the classifications above.
- If running as a standalone cleanup session, do not create a new mathematical attack target unless a genuine proof repair is required.

The purpose of this audit is not to defend Radius-3 or Radius-4.

The purpose is to determine exactly what was proved, in exactly which domain, and make the repository impossible to misread on this point.

---

## Frozen post-audit return instruction

RL246's current mathematical success and unfinished target are frozen in `RL246_FROZEN_REOPEN_TARGET.md`.

After this audit has reached one of the required classifications and any required repair/demotion propagation is complete, reopen that target only if its dependencies remain valid under the audited Radius-3/Radius-4 scope.

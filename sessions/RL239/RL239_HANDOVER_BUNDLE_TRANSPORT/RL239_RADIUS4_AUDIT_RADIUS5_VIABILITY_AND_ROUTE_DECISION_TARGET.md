# RL239 — Radius-4 audit, Radius-5 viability, and route-decision target

## Mission

This is a **decision session**, not an automatic continuation to either Radius 5 or the Radius-4 global bridge. Its output must determine the mathematical focus of RL240.

Work in the exact inherited radius notion: cyclic adjacent-transposition distance between equal-length equal-weight binary words, with the inherited `D|Q` primitive full-`D` self-rotation setting.

## Goal 1 — vigorously audit and red-team Radius 4

This goal is first and gating. Make the audit concrete and adversarial, not a prose review.

Required checks:

1. Independently reconstruct the Radius-4 flow classification from `sum |G_i|=4`; prove there are no omitted height/topology cases.
2. Independently rederive rotation covariance of `D|Q` and every local/event identity used in the topology closures.
3. Replay the complete portable verifier suite from a clean unpack and verify `SHA256SUMS.txt` first.
4. Recheck every analytic-to-finite cutoff and its monotonic continuation, especially all LMN thresholds.
5. Recheck every strict-superset claim: verify the finite enumerator really contains every actual structural rotation in the claimed range.
6. Independently rederive the continued-fraction argument with `L/A` reduced first; enumerate all admissible multiples of convergents.
7. Red-team the `[1,1,1,1]` quotient recurrence, common-sign reduction, multi-unit closure, unified `T_i>=21` floor, spectral bounds, minimum-growth lemma, and final 22-pair strict-superset tail.
8. Use at least one implementation genuinely independent of the promoted verifier code for a meaningful finite overlap range; compare exact counts/survivors.
9. Check primitive/nonprimitive handling, especially the alternating `A=8,L=4,D=175` repetition.
10. Verify that no local theorem has been silently promoted into a Gate-B/global claim.

### Goal-1 output

Classify Radius 4 as exactly one of:

- `R4_AUDIT_PASS` — theorem survives independent audit;
- `R4_REPAIR_REQUIRED` — precise repair with affected leaves identified;
- `R4_DEMOTION_REQUIRED` — theorem or a required branch fails.

If repair/demotion is required, stop ordinary route comparison and perform the repository stop-and-repair protocol. Do not build Radius 5 on a broken Radius 4.

## Goal 2 — assess Radius-5 viability

Only after `R4_AUDIT_PASS`, assess—not necessarily prove—the literal Radius-5 analogue.

Required questions:

1. What is the exact `sum |G_i|=5` flow classification? Enumerate the new height patterns and all unit-height run partitions.
2. Which Radius-3/4 mechanisms transfer verbatim?
   - connected local-coefficient factorization;
   - complementary representatives;
   - multi-component cyclic-product bounds;
   - quotient-cycle recurrences;
   - spectral balancing;
   - LMN + continued-fraction finite reduction.
3. Which mechanisms genuinely worsen at radius 5?
   - number of components/sign patterns;
   - possible `|G|>=2` or mixed-height geometries;
   - skew classes and gcd structure;
   - local coefficient sizes;
   - recurrence state count;
   - quality of exponential defects.
4. Build small exact exploratory certificates sufficient to test the proposed classification/mechanics, but label them **EVIDENCE** unless they prove a finite statement.
5. Give a concrete estimate of whether Radius 5 looks like a smooth extension, a moderate new project, or a qualitatively new proof problem.

Do **not** claim a Radius-5 theorem unless it is actually proved and fully certified.

## Goal 3 — Radius-4 global bridge versus Radius 5

Compare the mathematical leverage of:

- **Route B4:** prove a global bridge forcing a putative RL object to encounter an exact Radius-4 pair;
- **Route R5:** prove the literal Radius-5 local theorem first, postponing the bridge.

Recover the exact inherited Radius-3 bridge target/obstruction and formulate the weakest legitimate Radius-4 bridge. Then assess concretely whether Radius 4 changes the global problem:

- Does the extra unit of transport materially enlarge certified coverage?
- Does it remove the known Radius-3 local-grammar countermodel mechanism, or merely move it?
- Can the bridge be reframed as a finite covering/packing/residue/return problem?
- Is there a monotone principle making radius 4 globally stronger, or can an RL object still thread around all radius-4 encounters?
- What exact new theorem would close the bridge?

Compare that bridge obstruction against the estimated proof complexity and likely incremental value of Radius 5.

### Mandatory final route decision

RL239 must end with one of:

- `ROUTE_DECISION = R4_GLOBAL_BRIDGE`
- `ROUTE_DECISION = R5_LOCAL_THEOREM`
- `ROUTE_DECISION = REPAIR_RADIUS4`

and justify it with a short evidence table: expected leverage, proof difficulty, dependency risk, and whether success would close Gate B or merely enlarge the local radius.

The successor RL240 target must implement that decision and only that decision.

## Standing red teams

- Radius means the inherited adjacent-transposition metric only.
- Local theorem != global bridge.
- Radius 5 is not presumed true or useful merely because Radius 4 worked.
- A larger local radius is not automatically globally stronger.
- Finite evidence is not an analytic theorem.
- No Gate B closure without an actual global bridge.
- No Gate A claim from Gate B work.
- Preserve the frozen RL231–RL237 charging programme unless a genuine dependency arises.

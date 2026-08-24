# START HERE — RL29 -> RL30 AUDIT / REVIEW handover

Date: 2026-08-21

## One-line state

**RL remains open.** The inherited radius-3 branch is still closed under its audited hypotheses/dependencies, while the surviving order-3/global bridge has been narrowed to the exceptional balanced geometry

`R == 91 (mod 288), (G,H)=(12,4)`.

RL28/RL29 made two potentially important advances that now require skeptical review:

1. forced synchronized rotations recover both the absolute factor `B-Y` and the relative Eisenstein factor `B*w^2-Y` exactly from a bounded family of rotated block numerators;
2. a new transport argument appears to upgrade the old `O(1)` crossing information to a rigorous `Omega(e/log e)` number of distinct aligned columns containing a phase above `2.9R`.

Neither statement should be treated as closing the bridge until the audit below is completed.

## Mandatory first actions for RL30

1. Read `RL29_AUDIT_LEDGER.md` first.
2. Read `RL29_SESSION_RESULTS_TO_AUDIT.md` and independently re-derive every claim labelled **PROPOSED ANALYTIC**.
3. Read `RL29_BRIDGE_DISTANCE_AND_CLOSURE_MAP.md` before deciding what “close to RL” means.
4. Run the inherited 20 verifiers under `inherited_rl27/` and the two new scripts in `rl29_additions/`.
5. Treat any verifier failure as stop-and-repair.
6. Reconstruct the logical dependency DAG from the global RL reduction to the exceptional order-3 sector. Do **not** assume that eliminating `(G,H)=(12,4)` automatically closes RL until the DAG says so.
7. Only after the audit, choose the next attack.

## Fresh release checks in this handover

- inherited verifier stack: 20/20 reproduced as PASS (one aggregate command hit the shell/runtime cap; the unfinished tail was rerun individually and all passed);
- new RL29 exact-ownership/lift verifier: PASS;
- new RL29 transport-scaling sanity verifier: PASS;
- exploratory simultaneous-lift run reproduced through depth 35.

See `RL29_AUDIT_RELEASE_VERIFICATION.md`.

## The audit question that matters most

The next session should answer, with a dependency diagram and quantitative estimate:

> **If the exceptional order-3 geometry can be eliminated, is that sufficient to close the current RL theorem, or is there another global bridge/case still missing? If it is sufficient, what exact strengthening of the new transport theorem is needed to make the existing global packing/CF gate contradictory?**

That answer is more valuable than another deep finite residue lift.

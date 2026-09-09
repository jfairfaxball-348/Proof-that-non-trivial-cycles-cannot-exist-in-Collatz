# RL290 closeout

Date: 2026-09-09

## Authority snapshot

- `BASE_HEAD`: `98d05bd1de0f4f57c93f55b0c648b9264409832c`
- incoming authority `START_HERE.md` blob: `63f6f83b7133401bfefd3e27dc54b3bdbd4d0845`
- incoming target blob: `fe77416383bc674dd59b233b6eaf63b32f3d011f`
- incoming RL: `RL290`
- successor RL: `RL291`

## Frozen classification

Primary:

`GAUGE_INVARIANT_BELLMAN_CHECKPOINT_KERNEL_AND_HEIGHT_ONE_LAUNCHPAD_BARRIERS_PROVED`

Gate A remains open with exact residual:

`k>=25`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## What RL290 established

RL290 started from RL289's fixed-seed affine ballot bijection and rejected-tube geometry.

The session proved an exact post-departure seam normal form

`B-C=2^(q-1)(K-1)`

but then proved successively stronger reasons that a seam charge attached to one chosen history is not a physical invariant:

1. neutral seed-prefix gauge;
2. positive zero-height boundary-cycle gauge;
3. fixed-seed physical branch mergers;
4. loop-free equal-area history diamonds.

This led to the canonical gauge-free replacement: a Bellman future-threat envelope over physical states.

The zero-height positive boundary subsystem was then quotiented into an exact positive-even checkpoint graph with strictly positive macro-edge costs.

The height-one macro-kernel was completely classified. It contains RL283's boundary `C/E` hazard system as its one-generation projection.

RL290 also proved the missing `h=1` member of RL282's pure-zero terminal-tail family:

for every odd terminal exponent `k>=3`, there are infinitely many positive locally admissible terminal blocks of exact total height one. Their launchpads form affine rays, all with valuation one.

The stripped-unit map

`t=nu_2(3J+2)`,
`u=(3J+2)/2^t`

was identified as:
- a specific cost-one Bellman successor `u+1`;
- one event inside RL283's boundary hazard;
- RL284's labelled accelerated odd Collatz image of `J/2`;
- a synchronized labelled accelerated renormalization of RL289's fixed-seed shadow pair.

Finally, a genuine certified chain

`(2514,15)->(5378,16)->(21842,17)->(8192,18)`

shows that one-generation boundary hazard can be much smaller than recursively propagated Bellman threat.

## Verification

Portable regression verifier:

`sessions/RL290/verification/verify_rl290_bellman_kernel.py`

Clean deterministic output:

`sessions/RL290/verification/RL290_FAST_VERIFIER_OUTPUT.txt`

It checks:

- exact one-step merger family samples;
- fixed-seed merger witnesses;
- the acyclic equal-area diamond;
- 1,029 height-one launchpad instances;
- 686 one-zero-shell survivors;
- 1,250 stripped-unit suffix instances;
- 81 positive boundary loop iterations;
- the exact cost-one chain `2514->5378->21842->8192`;
- the nested-hazard jump `1074:2 -> 1364:11`.

The verifier is regression support only. Promoted RL290 statements are analytic.

Proof-state/scope red team:

`sessions/RL290/verification/RL290_RED_TEAM.md`

records `PASS`.

## Scratch preservation

The user's closeout instruction explicitly requested that relevant scratch work be frozen.

The file

`sessions/RL290/RL290_SCRATCH_FREEZE.md`

preserves:
- seam derivation details;
- exact recurrences;
- private regression counts;
- positive boundary-loop masking formula;
- branch-merger and acyclic-diamond witnesses;
- Bellman definitions;
- launchpad families;
- stripped-unit formulas;
- synchronized ballot-shadow renormalization;
- exact height-one checkpoint kernel;
- certified extremal chains;
- finite evidence explicitly kept unpromoted;
- open Bellman-route leads.

These scratch leads are preserved for audit/recovery and are NOT automatically authorized as RL291's principal work.

## Finite evidence boundary

The observed inequality

`nu_2((3J+2)/2^nu_2(3J+2)+1) <= H-2`

survived the exact RL282 `H<=22` positive checkpoint set and a depth-33 fixed-length regression.

It remains explicitly `UNPROMOTED_FINITE_EVIDENCE_ONLY`.

It does not narrow the Gate-A residual.

## Transport

Closeout uses direct Git-object transport in one atomic commit from the exact base head.

The committed `sessions/RL290/` tree is the lossless handover.

`SHA256SUMS.txt` covers every frozen RL290 payload except itself.

No ZIP or outer sidecar applies.

Generated knowledge catalogues are unchanged and marked `stale/deferred`.

## Successor

The successor is deliberately NOT a simple continuation of the Bellman route.

Prepared authoritative successor:

`RL291_PROGRAMME_WIDE_AUDIT_SYNTHESIS_AND_FAST_TRACK_REVIEW_TARGET.md`

RL291 must first perform a broad audit/review of the research programme:

- era-by-era history, including roughly pre-RL100, RL100-199, RL200-269, and RL270-RL290;
- all promoted lemmas/theorems and major objects relevant to the live proof state;
- corrections/demotions and what survived them;
- overlaps and rediscoveries across eras;
- older ideas whose significance changes under late-stage knowledge;
- dormant proof ingredients;
- hidden equivalences between apparently separate routes;
- assumptions or inherited claims needing renewed scrutiny;
- possible shortcuts, fast tracks, or alternative attacks suggested by the synthesis;
- the current Bellman/checkpoint-kernel route as an important live option, not a privileged default.

The audit should explicitly identify work that was explored opportunistically or unprompted, separate useful mathematics from route proliferation, and recommend the smallest set of genuinely authoritative next directions.

Unless the audit itself exposes an immediate contradiction/correction or a nearly mechanical closure, RL291 should prioritize synthesis over fresh mathematical expansion.

## Catalogue

Generated knowledge catalogues remain `stale/deferred`.

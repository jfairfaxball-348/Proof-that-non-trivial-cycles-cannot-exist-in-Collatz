# RL296 scratch freeze — deliberately unpromoted material

Date: 2026-09-11

Everything in this file is non-authoritative unless separately stated in `RL296_REPORT.md`.

## 1. `(6,699)` diagnostic

The all-zero offset cycle

`33 -> 16 -> 24 -> 36 -> 54 -> 81 -> 40 -> 60 -> 90 -> 135 -> 67 -> 33`

was observed and exactly replayed during research.

A raw recursive prefix-tree owner search became diffuse: a deliberately capped experiment expanded hundreds of internal states and retained a large unresolved frontier. This is route diagnosis only.

Do not promote:
- an absence claim;
- a lower bound;
- a proof barrier;
- a statement that `(6,699)` cannot be closed by another representation.

## 2. `(5,206)` owner-shell diagnostics

Exact P-owner cone/shell calculations were used to discover replayable wall splices. Only the six splices embedded in the final portable verifier are promoted.

Timed-out or incomplete cost-28/cost-29 shell passes are not negative results for the three surviving wall states.

Do not infer that their P owner cost exceeds 29 or that no mixed-suffix certificate exists.

## 3. Mixed-predecessor searches

Several reverse/mixed predecessor searches were stopped because their state spaces diffused under the available foreground execution budget.

These are operational route diagnostics, not mathematical barriers.

## 4. Preferred engineering resume point

If a later session returns to front-door cleanup after the RL297 P audit, resume from the exact promoted residual:

`Bcal(4,39) <= max(`
` Bcal(P)+2,`
` Bcal(6,699)-24,`
` Bcal(13,2383314)-187,`
` Bcal(15,21490604)-243,`
` Bcal(15,21490598)-257 )`.

Do not reconstruct the already-closed `(5,264)`, `(5,351)`, `(6,898)`, or `(6,807)` sectors unless a verifier fails.

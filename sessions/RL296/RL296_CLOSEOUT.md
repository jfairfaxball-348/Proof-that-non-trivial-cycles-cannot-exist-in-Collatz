# RL296 closeout

Date: 2026-09-11

## Authority snapshot

Incoming `main` / `BASE_HEAD`:

`8d43a2e69a9fd6b3f317b8cc8b085a163d5ad691`

Incoming authority:

`authoritative/RL296_FINITE_WALL_SECTOR_CLOSURE_AND_Q17_OWNER_GATE_A_TARGET.md`

Incoming authority blob:

`2dc9f143727f32c561518913747f2ea493367934`

Incoming `authoritative/START_HERE.md` blob:

`ca35df3da585c5b82147162341d58bdadcc983ff`

## Frozen classification

`FINITE_5191_FRONTIER_RECONSTRUCTED_5264_5351_6898_6807_CLOSED_5206_THREE_WALL_RESIDUAL_PROVED`

## Proof state

Gate A remains open with exact inherited residual

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted results

- replayable reconstruction of the RL295 finite `(5,191)` frontier;
- `Bcal(6,736)<=Bcal(P)+36`;
- complete closure `Bcal(6,807)<=Bcal(P)+31`, using RL295's inherited Q17 all-depth tail;
- `Bcal(5,351)<=Bcal(P)+24`;
- `Bcal(6,898)<=Bcal(P)+31`;
- `Bcal(5,264)<=Bcal(P)+20`;
- exact reduction of `(5,206)` to three late-wall residual states;
- exact final `(4,39)` reduction

`Bcal(4,39) <= max(`
` Bcal(P)+2,`
` Bcal(6,699)-24,`
` Bcal(13,2383314)-187,`
` Bcal(15,21490604)-243,`
` Bcal(15,21490598)-257 )`.

## Verification

Portable suite:

`sessions/RL296/verification/verify_rl296_closeout.py`

Frozen output:

`sessions/RL296/verification/RL296_FAST_VERIFIER_OUTPUT.txt`

Target-specific red team:

`RL296_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`.

The complete suite passed in the candidate package and again from a clean reconstructed copy before transition.

## Not promoted / remains open

- three late-wall descendants of `(5,206)`: `(13,2383314)`, `(15,21490604)`, `(15,21490598)`;
- `(6,699)`;
- complete `(5,206)` closure;
- `Bcal(5,191)<=Bcal(P)+8`;
- `Bcal(4,39)<=Bcal(P)+2`;
- remaining non-P front-door states;
- front-door collapse to P;
- `Bcal(P)<=1`;
- Gate A;
- Gate B, fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

## Successor

Prepared successor:

`RL297_P_BOTTLENECK_RISK_FIRST_GATE_A_AUDIT_TARGET.md`.

By direct user instruction, RL297 pivots away from general front-door cleanup and performs an adversarial risk-first audit of

`Bcal(P)<=1`.

For RL297 research prioritisation only, remaining finite front-door engineering may be provisionally assumed completable. This is explicitly **not** a proof statement.

RL297 begins by attempting falsification: find an exact legal P future with Bellman score at least 2. If none is found, isolate the extremal/near-extremal P futures and the structural reason for the apparent ceiling.

## Catalogue

Generated `knowledge/` catalogues are unchanged and `stale/deferred`.

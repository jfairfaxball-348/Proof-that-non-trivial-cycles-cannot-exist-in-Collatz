# RL285 closeout

Date: 2026-09-09

## Authority snapshot

- `BASE_HEAD`: `f49f2d6edccec6656102c53b0844f668cbc064f1`
- incoming authoritative `START_HERE.md` blob: `01c080ac5f634307693f4b810a89469173f53fca`
- incoming target blob: `6a82a15649df245204af7cdb4e1610b5c8666f8d`
- incoming RL: `RL285`
- successor RL: `RL286`

## Frozen classification

Primary:

`GLOBAL_PREFIX_2ADIC_REFORMULATION_AND_FIRST_CARRY_BRIDGES_PROVED`

RL285 did not close Gate A. It converted the target into an all-prefix dominance/carry formulation, proved several exact bridges, established an exact `H<=22` all-raw-state certificate for the post-column 2-adic candidate, and isolated local/scalar barriers.

No inherited promoted theorem is corrected or demoted.

An unpromoted scratch claim `nu_2(J)<=H-d+1` was falsified by the reachable state `(2,4,2)` and is explicitly discarded.

## Gate-A proof state

Gate A remains open:

`H_can>=k`

at terminal `d=1,J=2^k`.

Exact residual:

`k>=25`, `k` odd, `H_can<k`.

Preferred checkpoint theorem:

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

RL285's all-depth candidate

`nu_2(K-1)<=H+d-1`, `K=J+2^d-1`,

is globally conjectural but exactly certified over all reachable raw states with `H<=22`.

## Verification

Portable verifier:

`verification/verify_rl285_prefix_2adic.py`

Recorded clean stdout:

`verification/RL285_FAST_VERIFIER_OUTPUT.txt`

Closeout proof-state/scope red team:

`verification/RL285_RED_TEAM.md`

Result: PASS.

Inherited RL282/RL283 expensive verification state is accepted under verification economy.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL285/` tree is the complete lossless handover.

`SHA256SUMS.txt` covers every frozen RL285 payload except itself.

No ZIP is used, so no outer `.zip.sha256` sidecar applies.

## Successor

RL286 continues Gate A from the new component/carry formulation. It must not treat the global post-column inequality as proved and must preserve all RL283/RL285 barriers.

## Catalogue

Generated `knowledge/` catalogues are unchanged and `stale/deferred` under connector-worker closeout policy.

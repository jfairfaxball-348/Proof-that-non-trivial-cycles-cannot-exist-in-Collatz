# RL284 closeout

Date: 2026-09-08

## Authority snapshot

- `BASE_HEAD`: `6c4e7bc567de48213c1c2061f6480dd172257285`
- incoming authoritative `START_HERE.md` blob: `745cb61ca5e476e28046adc1a866421a739a999b`
- incoming target blob: `628f7ea28d61ed6b7595cb4ea1563d8cab9c2b57`
- incoming RL: `RL284`
- successor RL: `RL285`

## Frozen classification

Primary:

`LABELLED_ACCELERATED_REVERSIBILITY_AND_LOCAL_IRREVERSIBILITY_BARRIERS_PROVED`

Subordinate:

- `ACCELERATED_ODD_LABELLED_BIJECTION_PROVED`
- `ADMISSIBLE_PREDECESSOR_RAY_PROVED`
- `LOCAL_PRIMALITY_BRANCH_INDIFFERENCE_PROVED`
- `MOD3_ORIENTATION_ACYCLICITY_BARRIER_PROVED`
- `VALUATION_ONLY_CYCLE_CHARGE_BARRIER_PROVED`

No inherited promoted theorem is corrected or demoted.

## Main promoted advance

For odd integer `n`, the labelled accelerated step

`3n+1=2^a m`

is bijective onto pairs with `m` odd, `3∤m`, `a>=1`, and `m==(-1)^a (mod 3)`, with exact inverse

`P_a(m)=(2^a m-1)/3`.

Admissible predecessors satisfy

`P_(a+2)(m)=4P_a(m)+1`.

Therefore retaining the exact valuation label removes the apparent local information loss. Primality supplies no local inverse-branch selection leverage.

The two-class mod-3 orientation graph is cyclic, and an additive valuation-only charge required to vanish on exact cycles satisfies `w(1)=w(2)=w(4)=0`.

These are precise barriers to the tested local irreversibility architecture; they do not rule out every possible state-dependent global cocycle.

## Gate-A proof state

Gate A remains open:

`H_can>=k`

at terminal `d=1,J=2^k`.

Exact residual:

`k>=25`, `k` odd, `H_can<k`.

Preferred sufficient theorem:

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

RL285 returns to this frozen programme.

## Verification

Portable verifier:

`verification/verify_rl284_structural.py`

Recorded clean stdout:

`verification/RL284_FAST_VERIFIER_OUTPUT.txt`

Closeout proof-state/scope red team:

`verification/RL284_RED_TEAM.md`

Result: PASS.

The inherited expensive RL282/RL283 verification state is accepted under verification economy.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL284/` tree is the complete lossless handover.

`SHA256SUMS.txt` covers every frozen RL284 payload except itself.

No ZIP is used, so no outer `.zip.sha256` sidecar applies.

## Successor

RL285 returns to the frozen upstream Gate-A target:

`globally reachable positive even d=1 checkpoint (J,H) => nu_2(J)<=H`.

Gate B, fifth selector, and Radius 6+ remain frozen.

## Catalogue

Generated `knowledge/` catalogues are unchanged and `stale/deferred` under connector-worker closeout policy.

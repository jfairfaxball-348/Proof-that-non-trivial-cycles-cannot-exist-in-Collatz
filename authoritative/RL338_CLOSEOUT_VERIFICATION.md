# RL338 closeout verification

Date: 2026-09-16
Status: GREEN FOR THE PROMOTED CLAIMS
Incoming `BASE_HEAD`: `6b1f64050acbf3464ecf7a973bc648e5be520f18`.

## Exact finite verification

Connector closeout reproduced the q=35-positive layers directly from the committed RL337 mechanical-factor/profile/residue machinery:

- p=5: `(pairs,templates,candidates,owned,boundary_cores)=(196,64120,299,161,68)`;
- p=6: `(154,130386,10,8,4)`;
- p=7: `(98,185360,0,0,0)`;
- p=8: `(42,204590,0,0,0)`.

The exceptional successor scan covered all 125 distinct `(right-context, exact exit-state)` interfaces. Contexts 22..28 were verified together and context 29 independently. Every successor right label 1..35 and every successor p=1..8 was checked. The result is 24 p<=4 owned continuations, all reduced charge <=-30; five p=7 `22->1` continuations at charge -88; and no other p=5..8 continuation. Context 29 has no p=1..8 owned continuation.

The reproducibility script is `verification/verify_rl338_q35_exhaustive.py`. It supports the same split ranges used at closeout.

## Portable fast verifier

Command:

`python3 -I verification/verify_rl338_q35_fast.py`

Observed output:

```text
RL338_Q35_FAST_GREEN
anchor 35(K-2H)-S<=43
layers [(5, 64120, 161), (6, 130386, 8), (7, 185360, 0), (8, 204590, 0)]
successor_margin exception<=8 short<=-30 p7low=-88 p>=9<=-14
consumer_rho60_floor 32546271992
consumer_bridge_floor 32546271999
cap 32546271999
```

## Independent red team

Command:

`python3 -I verification/red_team_rl338_q35.py`

Observed output:

```text
RL338_Q35_RED_TEAM_GREEN
singleton_max 0
p_ge_9_worst (-14, 29, 35, 9)
pairing_worst -6
final_constant 43
```

The red team specifically attacks the 21/22 potential boundary, surviving singleton support, all positive p=5..8 regions, the p>=9 tail, and the endpoint/pairing constant. It also triggered the correction recorded in `RL338_CORRECTION_AND_DEMOTION_LEDGER.md`: the earlier scratch wording omitted 24 p=1..4 successors, all of which are strongly negative.

## Transport

RL338 uses connector flat Git-tree transport. The committed Git tree/blob identities plus atomic commit/ref update/readback are the lossless transport; no new ZIP/sidecar is claimed. Knowledge catalogues are `stale/deferred` and are not part of the proof-state gate.

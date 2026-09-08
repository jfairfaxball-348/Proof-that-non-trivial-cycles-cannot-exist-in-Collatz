# RL281 closeout

Date: 2026-09-08

## Authority snapshot

- `BASE_HEAD`: `fe8263e9c3e6e9e34811c3430e1e7df4b3c9523c`
- incoming authority `START_HERE.md` blob: `f6701e5dfb365aac5ada72a39ada3453b1e5db76`
- incoming target blob: `859a7c96b3c3eca7dd66c2541f6c9e49137dff28`
- incoming RL: `RL281`
- successor RL: `RL282`

## Frozen classification

Primary:

`TWO_PHASE_GATE_A_COMPRESSION_PROVED`

Subordinate:

- `SHARP_EXCURSION_ZERO_MASS_ENVELOPE_PROVED`
- `POSITIVE_BLOCK_FULL_MASS_PRICING_PROVED`
- `DEPTH_TWO_EQUALITY_ENTRY_SCALE_SUPPRESSION_PROVED`
- `ONE_ZERO_2ADIC_HEIGHT_RIGIDITY_PROVED`
- `POSITIVE_BOUNDARY_ZERO_MASS_TELESCOPE_PROVED`
- `POSITIVE_PHASE_ZERO_MASS_CEILING_PROVED`
- `NEGATIVE_PHASE_DUAL_POTENTIAL_BUDGET_PROVED`
- `NEGATIVE_TO_POSITIVE_GATEWAY_DICHOTOMY_PROVED`
- `MOD3_REACHABILITY_INVARIANT_PROVED`
- `MINIMUM_POSITIVE_HEIGHT_THREE_PROVED`
- `K3_GATE_A_CASE_CLOSED_PROVED`

All promoted items are proved analytic mathematics. The `H<=2` closure is additionally backed by an exact finite certificate.

No mathematical correction or demotion was required during closeout.

## Scope

Gate A remains open with exact target `H_can>=k`.

RL281 proves:

`k` even is unreachable at a terminal,

and

`k=3` is Gate-A safe.

Therefore every hypothetical Gate-A violator is restricted to

`k>=5`, `k` odd, `H_can<k`.

The inherited necessary condition

`m0>=8`, equivalently `z>=k+6`

remains valid for any such violator.

Gate B is unchanged/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted advances

RL281 establishes:

1. a sharp zero-mass envelope for every first-return excursion, with the same unique depth-two equality family as the inherited defect envelope;
2. positive checkpoint full-mass pricing, including `F_next-F_in>S_E` for every multi-zero positive excursion;
3. exponential entry-state/scale suppression for high-zero depth-two equality excursions;
4. exact one-zero rigidity `h=nu_2(J+4)`;
5. an exact `B=Q(J+1)/2` telescope pricing every positive zero-height boundary zero;
6. total positive-phase zero mass `<15`;
7. a negative dual-potential entry charge `5Q/3` and total nonpositive-return entry-scale budget `<42/5`;
8. impossibility of direct strictly-negative-to-positive one-zero crossing;
9. the unique cheap gateway `J=0 --011,h=2--> J=3`, scale factor `8/9`;
10. the reachability invariant `J mod 3 in {0,(-1)^d}`, forcing terminal `k` odd;
11. the theorem `d=1,J>0 => H_can>=3`, closing Gate A completely at `k=3`.

## Verification

Portable verifier:

`verification/verify_rl281_two_phase.py`

Clean execution passes with:

- mod-3 legal transition regressions: 7,017;
- exact reachable `H<=2` closure: 28 states / 31 retained edges;
- first-return excursions: 13,909;
- depth-two equality excursions: 399;
- one-zero excursions: 199;
- negative-to-positive excursions: 1,889, all multi-zero;
- minimum normalized negative `C` excursion increment: `5/3`;
- positive-checkpoint block checks: 45,170;
- multi-zero checkpoint block checks: 44,158;
- terminal `F` ceiling: `110/3`;
- positive-phase zero-mass ceiling: `15`.

The recorded clean output is frozen in

`verification/RL281_FAST_VERIFIER_OUTPUT.txt`.

Closeout scope/proof-state red team:

`verification/RL281_RED_TEAM.md`

passes with no correction or demotion.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL281/` tree is the complete lossless handover. `SHA256SUMS.txt` covers every frozen payload except itself. No ZIP or outer `.zip.sha256` sidecar applies.

## Successor

Prepared successor:

`RL282_ODD_K_HEIGHT_ESCALATION_GATE_A_TARGET.md`

RL282 must attack only the residual odd-exponent region `k>=5`. Its principal task is a scalable height-escalation theorem from the exact terminal power-of-two condition plus the new mod-3 and valuation/mass-pricing structure. It must not restart completed excursion classification or make flat fixed-zero enumeration the principal programme.

## Catalogue

Generated knowledge catalogues are unchanged and are `stale/deferred` under the connector-worker closeout policy.

# RL280 closeout

Date: 2026-09-08

## Authority snapshot

- `BASE_HEAD`: `e3ace912c8663b0ec3e3dea836065dea878fe7e4`
- incoming authority `START_HERE.md` blob: `e49116c909fa4e0185ad75560b92c59762e0a244`
- incoming target blob: `6d5828b51fa19c38a291ea34545300b448371baf`
- incoming RL: `RL280`
- successor RL: `RL281`

## Frozen classification

Primary:

`SHARP_POSITIVE_EXCURSION_STATE_SCALE_LYAPUNOV_PROVED`

Subordinate:

- `SHARP_EXCURSION_STATE_VERSUS_HEIGHT_INEQUALITY_PROVED`
- `EXCURSION_COUPON_DECOMPOSITION_PROVED`
- `NESTED_ZERO_WEIGHT_AMPLIFICATION_PROVED`
- `SHARP_EXCURSION_ZERO_COMPLEXITY_HEIGHT_ENVELOPE_PROVED`
- `EXACT_DEPTH_TWO_EXTREMAL_NORMAL_FORM_PROVED`
- `SHARP_FIRST_RETURN_STATE_SCALE_THEOREM_PROVED`
- `EXTREMAL_2ADIC_3ADIC_RIGIDITY_PROVED`
- `POSITIVE_CHECKPOINT_RETURN_LYAPUNOV_PROVED`
- `GLOBAL_ENDPOINT_POTENTIAL_DEPENDENCY_IDENTIFIED`

No mathematical correction or demotion was required during closeout.

## Scope

Gate A remains open with exact target `H_can>=k`.

Every hypothetical Gate-A violator retains the inherited necessary condition

`m0>=8`, equivalently `z>=k+6`.

Gate B is unchanged/open and frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted advances

RL280 establishes:

1. exact first-return `P/Q` factorization and the sharp state-versus-height inequality;
2. a global one-parameter endpoint-potential extension;
3. exact excursion coupon decomposition;
4. nested zero-weight amplification;
5. a sharp zero-complexity/height defect envelope;
6. the unique depth-two equality normal form;
7. a sharp zero-count-dependent first-return state/scale theorem;
8. exact 2-adic/3-adic rigidity of the equality family;
9. strict positive-checkpoint Lyapunov growth for `F=Q(J+3)`;
10. the terminal ceiling `F<110/3`;
11. identification that the aggregate endpoint-potential terminal equation is dependent on the existing `2S+D` identity.

## Verification

Portable verifier:

`verification/verify_rl280_excursions.py`

Clean execution passes with:

- global endpoint-potential checks: 18,680;
- strict ascent checks: 4,800;
- first-return excursions: 13,909;
- depth-two equality excursions: 399;
- equality parameter pairs: 39;
- positive-checkpoint block checks: 45,170;
- minimum normalized checkpoint increment: `1241/2187`;
- terminal `F` ceiling: `110/3`.

The verifier output is frozen in

`verification/RL280_FAST_VERIFIER_OUTPUT.txt`.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL280/` tree is the complete lossless handover. `SHA256SUMS.txt` covers every frozen payload except itself. No ZIP or outer `.zip.sha256` sidecar applies.

## Successor

Prepared successor:

`RL281_POSITIVE_CHECKPOINT_GATE_A_CLOSURE_TARGET.md`

The successor must compose the new positive-checkpoint state/scale law with the inherited zero-mass/coupon/terminal-scale constraints. It must not restart the completed internal excursion classification or make flat eight-zero enumeration the principal programme.

## Catalogue

Generated knowledge catalogues are unchanged and are `stale/deferred` under the connector-worker closeout policy.

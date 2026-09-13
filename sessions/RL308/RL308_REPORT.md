# RL308 report — exact X prefix cut and strategic freeze for global mechanics reset

Date: 2026-09-13
Base commit: `7cc1a69a83e506e2ecfe0a4aa8ba8292595ebccd`
Base tree: `b8a82c74ad1976fd5471fa1125c36a35dd075fef`

Primary classification:

`X_FIXED_RESIDUE_COMPLETE_PREFIX_CUT_TO_TWO_RESIDUALS_PROVED_AND_CURRENT_LOCAL_PROGRAMME_FROZEN_FOR_GLOBAL_MECHANICS_REVIEW`

Gate A remains open. Gate B remains open/frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and stop condition

RL308 inherited the RL307 reduction

`Bcal(3,-28) <= max(`
` Bcal(2,-17)+2,`
` Bcal(4,39)-6,`
` Bcal(X)-8,`
` Bcal(Y)-9 )`

with

`X=(4,43)`,
`Y=(6,504)`,

and was asked to prove `Bcal(X)<=11`, `Bcal(Y)<=12`, or replace them by strictly smaller exact dependencies.

The session found one exact contraction for X and then stopped immediately on direct user instruction before attacking either new residual or Y.

No further mathematics was performed after closeout lock.

## 2. Exact complete prefix cut for X

Conditional only on the already-existing Gate-A obligation

`Bcal(2,-17)<=1`,

the following twelve X-prefixes form a complete prefix-free cut:

`010, 011, 100, 101, 110, 111,`
`0010, 0011, 00001, 00011, 00000, 00010`.

Their Kraft sum is exactly one.

No proper internal cut node is a positive-even `d=1` checkpoint, so a Bellman future cannot terminate before reaching a leaf and evade the cut.

Ten leaves reach physical states also reachable from `(2,-17)`:

| X word | common state | X cost | `(-17)` owner cost | branch bound under `Bcal(-17)<=1` |
|---|---|---:|---:|---:|
| `010` | `(3,23)` | 8 | 18 | 11 |
| `011` | `(3,44)` | 8 | 13 | 6 |
| `100` | `(5,216)` | 10 | 17 | 8 |
| `101` | `(5,347)` | 10 | 17 | 8 |
| `110` | `(4,90)` | 8 | 14 | 7 |
| `111` | `(2,18)` | 8 | 13 | 6 |
| `0010` | `(4,81)` | 13 | 20 | 8 |
| `0011` | `(4,153)` | 13 | 17 | 5 |
| `00001` | `(5,326)` | 20 | 27 | 8 |
| `00011` | `(5,495)` | 20 | 26 | 7 |

For any same physical leaf state `S`, the owner can copy the identical future suffix. Therefore the X contribution from that leaf is at most

`Bcal(2,-17) + c_owner(S) - c_X(S)`,

which gives the displayed bounds.

The two unresolved leaves are

`X --00000,cost20--> (7,2039)`

and

`X --00010,cost20--> (7,2546)`.

Hence exactly

`boxed:`
`Bcal(4,43) <= max(`
` 11,`
` Bcal(7,2039)-20,`
` Bcal(7,2546)-20 )`

conditional on `Bcal(2,-17)<=1`.

Consequently the original RL308 requirement

`Bcal(X)<=11`

would follow from only

`Bcal(7,2039)<=31`,
`Bcal(7,2546)<=31`.

This is an exact dependency contraction. Neither residual ceiling is proved.

## 3. Exact owner witnesses

The portable verifier freezes the exact `(2,-17)` owner words for all ten owned leaves. They are intentionally retained so this reduction can be resumed without reconstructing a Dijkstra search.

The verifier also checks prefix-freeness, exact Kraft equality, every X path and owner path, branch costs, and the absence of an internal positive-even checkpoint.

## 4. Supporting exact identities discovered during exploration

These are retained as useful scratch, not promoted as closure theorems:

`8 --011010,cost4--> (2,19)`,
`X --11101,cost11--> (2,19)`.

Thus one high-valuation X minimizer family shared a continuation with checkpoint 8 after a seven-unit ingress disadvantage.

Also

`X --1110111,cost13--> (1,15)`,
`Y --1111111100,cost19--> (1,15)`.

This exposed a six-unit Y/X common-state relationship on the observed minimizer family.

No theorem was proved that dangerous Bellman futures must enter either cylinder.

## 5. Finite shell evidence

Exact shortest-path scans through the already-run finite ranges gave minimum divisibility-shell costs:

| k | checkpoint 8 | X | Y |
|---:|---:|---:|---:|
| 6 | 9 | 16 | 22 |
| 7 | 10 | 17 | 23 |
| 8 | 11 | 18 | 24 |
| 9 | 12 | 19 | 25 |
| 10 | 13 | 20 | 26 |
| 11 | 13 | 20 | 26 |
| 12 | 15 | 22 | 28 |
| 13 | 15 | 22 | 28 |

This finite evidence shows an X/8 cost gap of seven and Y/X gap of six over those visible minima. It is evidence only; no all-depth relation is claimed.

## 6. Routes tested but not promoted

### Naive local logarithmic Bellman potential

The exploratory candidate

`phi(d,J)=ceil(log2(K+1))+d`

fails the needed edge inequality. An exact counterexample is

`(1,2) --0,cost0--> (2,6)`

where `phi` rises from 2 to 4.

Therefore this naive local potential cannot certify the desired Bellman ceilings.

### Large Y-by-X owner cut

An exact shallow state-owner exploration tried to bound Y directly through the X cone. Coverage did not converge: at depth 15 there were 11,769 unresolved frontier states, of which only 310 were owned under the attempted scalar allowance. The route was not promoted and was stopped rather than expanded into another large grammar.

### X minimizer-cylinder forcing

Finite scans suggested that high-valuation X minima use the `11101` ingress to `(2,19)`. A separate search excluding that full prefix found maximum score `-6` through the explored cost caps 30,40,50,60, but each run hit the imposed 1,000,000-state cap. Therefore this is incomplete computational evidence and explicitly NOT a certificate.

## 7. Precise live frontier at freeze

Promoted in RL308:

- the exact conditional X cut and reduction above.

Still open:

- `Bcal(7,2039)<=31`;
- `Bcal(7,2546)<=31`;
- `Bcal(X)<=11`;
- `Bcal(Y)<=12` — Y was not attacked after the checkpoint;
- `Bcal(2,-17)<=1`;
- `Bcal(4,39)<=3`;
- `Bcal(2,-84)<=2`;
- `Bcal(3,-28)<=3`;
- `Bcal(8)<=3`;
- `Bcal(P)<=1`;
- Gate A;
- Gate B;
- O1/O2/P8 and other inherited open obligations.

The current local programme is frozen, not demoted or rejected.

## 8. Strategic disposition

On direct user instruction, RL308 closes with the Bellman/scalar/Gate-A frontier preserved intact and no automatic local successor.

RL309 is instead a planning-only:

`GLOBAL MECHANICS REVIEW, PROOF-ARCHITECTURE RESET, AND ROADMAP REWORK`.

The review must reconstruct the route from a hypothetical positive non-trivial cycle to contradiction in plain mathematical language, audit all major machinery by global leverage, re-audit Gate A/Gate B from first principles, identify depth traps, rank a small number of end-to-end architectures, and prepare RL310.

RL309 must not execute the chosen mathematical attack.

## 9. Verification

Portable verifier:

`sessions/RL308/verification/verify_rl308_closeout.py`.

Fresh output:

`sessions/RL308/RL308_FRESH_VERIFICATION.txt`.

Result:

`RL308_CLOSEOUT_VERIFIER_GREEN`.

The verifier replays every load-bearing finite identity in the promoted X reduction and the explicitly frozen supporting common-state identities.

## 10. Scope

No inherited theorem is demoted.

Gate A OPEN.
Gate B OPEN/frozen.
Fixed-96 P/Q frozen.
Physical/resonance frozen at `a=7354673373747273032`.
Radius 6+ frozen.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.

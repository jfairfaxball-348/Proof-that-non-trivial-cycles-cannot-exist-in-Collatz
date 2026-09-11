# RL296 report — finite wall-sector reconstruction and contraction

Date: 2026-09-11

Primary classification:

`FINITE_5191_FRONTIER_RECONSTRUCTED_5264_5351_6898_6807_CLOSED_5206_THREE_WALL_RESIDUAL_PROVED`

Gate A remains open with exact inherited residual

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and disposition

RL296 inherited RL295's exact zero-depth wall normalization, the cut

`Bcal(4,39) <= max(Bcal(P)+2, Bcal(5,191)-6)`,

the exact P -> Q17 owner certificate, the `(6,807)` distinguished spine to Q17, the all-depth Q-tail owner theorem, and an unpromoted scratch reduction of `(5,191)`.

RL296 reconstructed the scratch frontier with explicit replayable P-owner witnesses, closed four of the six shallow residual sectors, and reduced a fifth sector `(5,206)` to exactly three late-wall states.

RL296 does **not** close `(4,39)`, because `(6,699)` and the three late-wall descendants of `(5,206)` remain open.

## 2. Reconstructed finite `(5,191)` frontier

The following exact prefix cuts are now frozen with explicit owner witnesses on every P-owned leaf:

`Bcal(5,191) <= max(Bcal(P)+8, Bcal(5,201)-4, Bcal(6,733)-13, Bcal(6,949)-18)`.

`Bcal(5,201) <= max(Bcal(P)+12, Bcal(5,206)-4, Bcal(5,264)-8, Bcal(5,351)-12)`.

`Bcal(6,733) <= max(Bcal(P)+21, Bcal(6,699)-5, Bcal(6,898)-10)`.

`Bcal(6,949) <= max(Bcal(P)+26, Bcal(6,807)-5)`.

Substitution into RL295's promoted `(4,39)` cut gives

`Bcal(4,39) <= max(`
` Bcal(P)+2,`
` Bcal(5,206)-14,`
` Bcal(5,264)-18,`
` Bcal(5,351)-22,`
` Bcal(6,699)-24,`
` Bcal(6,898)-29,`
` Bcal(6,807)-29 )`.

Classification:

`REPLAYABLE_FINITE_5191_WALL_FRONTIER_RECONSTRUCTED`.

## 3. Complete closure of `(6,807)`

RL295's distinguished word

`1000000101000101`

from `(6,807)` reaches `Q17` at source cost 169. Its sixteen first-deviation sectors are reconstructed exactly by the RL296 closeout verifier.

Fifteen of the sectors have explicit same-state P-owner words within the inherited +31 allowance. During closeout these witnesses were independently regenerated from the exact cost-<=23 P cone plus legal zero lifts, so the promoted result does not depend on missing scratch state.

The unique remaining sector is `(6,736)` at source cost 5.

For `(6,736)`, RL296 proves a complete first-departure cut along fourteen zero inputs. Every first-1 departure at positions 0 through 13 has an explicit P-owner witness. The all-zero remainder reaches exact `R_11=(11,K=3^11)` at source cost 116, while P reaches the identical `R_11` at cost 46.

Therefore

`Bcal(6,736) <= Bcal(P)+36`.

Combining this with the fifteen side-sector certificates and RL295's inherited all-depth post-Q17 theorem gives

`boxed: Bcal(6,807) <= Bcal(P)+31`.

Classification:

`Q17_PRETAIL_FINITE_CLOSURE_AND_6807_P_PLUS_31_BELLMAN_DOMINATION_PROVED`.

## 4. Complete closure of `(5,351)`

A ten-leaf prefix cut covers every future: first `1` among the first nine positions, or the all-zero anchor.

Each departure leaf has an explicit same-state P-owner witness. The all-zero branch reaches `(8,6312)` at source cost 47, while P reaches the identical state at cost 41.

The tightest finite margin is 2.

Hence

`boxed: Bcal(5,351) <= Bcal(P)+24`.

Classification:

`Bcal_5351_LE_Bcal_P_PLUS_24_FINITE_CERTIFICATE`.

## 5. Complete closure of `(6,898)`

A complete 20-leaf prefix code covers first `1` after `n=0,...,18` zeros plus the `0^19` anchor.

All 20 leaves have explicit forward P-owner words. The portable verifier checks exact source endpoints, owner endpoints, costs, prefix-freeness, and Kraft sum 1.

Minimum owner spare is 3.

Hence

`boxed: Bcal(6,898) <= Bcal(P)+31`.

Classification:

`Bcal_6898_LE_Bcal_P_PLUS_31_FINITE_CERTIFICATE`.

## 6. Complete closure of `(5,264)`

A complete 31-leaf prefix code covers every future from `(5,264)`.

Every leaf has an explicit forward P-owner word. The certificate is exact and one leaf is tight: minimum spare 0.

Hence

`boxed: Bcal(5,264) <= Bcal(P)+20`.

Classification:

`Bcal_5264_LE_Bcal_P_PLUS_20_FINITE_CERTIFICATE`.

## 7. Exact reduction of `(5,206)` to three late walls

The correct inherited target for the `(5,206)` residual is +16, not +14. This is because the `(4,39)` frontier term is `Bcal(5,206)-14` and the target comparison is `Bcal(P)+2`.

The final complete prefix decomposition contains:

- 27 explicit owner leaves from the main finite cut;
- the analytic `G_6` sink, using `G_d=(d,K=3^d-3)` and `G_d --00--> G_(d+1)`;
- the exact `R_15` anchor on the hard zero spine;
- six late-wall leaves with additional replayable P-owner splices;
- exactly three remaining residual leaves.

The remaining states are:

| state | source cost from `(5,206)` | allowed P cost |
|---|---:|---:|
| `(13,2383314)` | 173 | 189 |
| `(15,21490604)` | 229 | 245 |
| `(15,21490598)` | 243 | 259 |

Thus

`Bcal(5,206) <= max(`
` Bcal(P)+16,`
` Bcal(13,2383314)-173,`
` Bcal(15,21490604)-229,`
` Bcal(15,21490598)-243 )`.

Classification:

`Bcal_5206_EXACT_THREE_LATE_WALL_REDUCTION_PROVED`.

Important non-claim: `Bcal(5,206)<=Bcal(P)+16` is **not** proved.

## 8. Final `(4,39)` residual after RL296

Using the four complete closures above and the `(5,206)` three-wall reduction, the reconstructed `(4,39)` frontier contracts to

`boxed:`
`Bcal(4,39) <= max(`
` Bcal(P)+2,`
` Bcal(6,699)-24,`
` Bcal(13,2383314)-187,`
` Bcal(15,21490604)-243,`
` Bcal(15,21490598)-257 )`.

This is an exact promoted reduction, not a closure.

Therefore the remaining engineering obstruction behind `(4,39)` is precisely:

1. `(6,699)` with required allowance `Bcal(6,699)<=Bcal(P)+26`;
2. `(13,2383314)` with the inherited shifted allowance above;
3. `(15,21490604)`;
4. `(15,21490598)`.

## 9. `(6,699)` route diagnosis

The all-zero spine has an exact offset cycle

`33 -> 16 -> 24 -> 36 -> 54 -> 81 -> 40 -> 60 -> 90 -> 135 -> 67 -> 33`

in coordinates `K=3^d+offset`.

This is a genuine structural observation, but the attempted raw recursive prefix-tree cleanup became diffuse. A deliberately capped exploratory run closed many leaves but retained a large frontier.

No absence theorem, lower bound, or barrier is promoted from that computation.

Classification:

`UNPROMOTED_ROUTE_DIAGNOSTIC_ONLY`.

## 10. Corrections made during RL296

Two scratch bookkeeping statements were corrected before promotion:

1. the required `(5,206)` allowance is +16, not +14;
2. an exploratory statement that `(6,898)` had a unique difficult leaf was too aggressive; the final 20-leaf verifier found and closed all actual exceptional leaves.

Neither correction changes inherited repository authority. The promoted statements in this report use only the corrected values.

## 11. Verification

Portable self-contained closeout verifier:

`sessions/RL296/verification/verify_rl296_closeout.py`.

It embeds the exact finite witness data for the reconstructed frontier, Q17 pre-tail sectors, `(6,736)`, `(5,351)`, `(6,898)`, `(5,264)`, and the final `(5,206)` three-wall reduction. It replays every promoted finite owner path from P, checks exact source paths/costs, and checks gap-free prefix partitions.

Frozen output:

`sessions/RL296/verification/RL296_FAST_VERIFIER_OUTPUT.txt`.

All verifiers pass.

Target-specific red team:

`RL296_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`.

## 12. What remains open

Not proved:

- `Bcal(5,206)<=Bcal(P)+16`;
- `Bcal(6,699)<=Bcal(P)+26`;
- `Bcal(5,191)<=Bcal(P)+8`;
- `Bcal(4,39)<=Bcal(P)+2`;
- closure of the other non-P RL292 front-door states `(2,-17)`, `(2,-84)`, `(3,-28)`;
- collapse of the five-state front door to P;
- `Bcal(P)<=1`;
- any `k>=31` contraction;
- Gate A;
- Gate B, fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

## 13. Strategic successor pivot

By direct user instruction, RL297 deliberately does **not** continue general front-door cleanup as its primary mission.

For RL297 only, the remaining finite front-door engineering is provisionally assumed completable with the required credits **for research prioritisation only**. This is not a proof claim and must never be used as one.

RL297 is a risk-first adversarial audit of the presumed final Gate-A bottleneck

`boxed: Bcal(P)<=1`, `P=(2,3)`.

The first task is to attempt falsification by finding an exact legal P future with

`nu_2(J_end)-Delta H >= 2`.

If no counterexample is found, RL297 must isolate the extremal/near-extremal P futures and seek the structural mechanism enforcing the apparent ceiling.

General front-door cleanup may be resumed only when directly required by the P analysis or in a later session after the P bottleneck has been stress-tested.

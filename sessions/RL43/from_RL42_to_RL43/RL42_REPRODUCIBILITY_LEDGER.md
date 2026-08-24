# RL42 reproducibility ledger

Date: 2026-08-22

## Status labels

- **ANALYTIC**: proof is contained in the retained mathematical note; verifier is only a sanity check.
- **EXACT FINITE CERTIFICATE**: conclusion depends on exhaustive finite computation over a rigorously reduced set; source and rerun output are retained.
- **INHERITED**: supplied by the prior handover; use the nested provenance bundle if deeper audit is needed.
- **EXPLORATORY / UNFROZEN**: observed in-session but not retained as a certificate; must be reproduced before use.

## Current chain

| Item | Status | Retained source | Current role |
|---|---|---|---|
| RL41 arithmetic checkpoint | Exact arithmetic sanity | `rl41_checkpoint/verify_rl41_arithmetic_checkpoint.py` | Near-pair/factorization constants and retained local arithmetic |
| Moved-rank sparse bridge | Analytic + sanity verifier | `rl42_additions/RL42_MOVED_RANK_SPARSE_BRIDGE.md` | Identifies moved odd mass with displaced ordered ranks and sparse support |
| Prefix-cap gap vs moved mass | Analytic + sanity verifier | `rl42_additions/RL42_PREFIX_CAP_GAP_VS_MOVED_MASS.md` | Coarse `P_+` lower bounds; predecessor to efficiency bridge |
| Lightweight `rho>=28` reconstruction | Analytic reduction + exact bounded certificate | `rl42_additions/RL42_LIGHTWEIGHT_RHO28_RECONSTRUCTION.md` | Replaces missing RL41 area-26/27 dependency; now superseded numerically |
| `rho=28` excess-DP elimination | Exact finite certificate | `rl42_additions/RL42_RHO28_EXCESS_DP_ELIMINATION.md` | Gives `rho>=29`; now superseded numerically |
| Transport-efficiency bridge | **ANALYTIC** | `rl42_additions/RL42_TRANSPORT_EFFICIENCY_BRIDGE.md` | Gives `rho>(45/4)G`, hence `rho>=46` |
| Crossing-excess transport floor | Analytic + **EXACT FINITE CERTIFICATE** | `rl42_additions/RL42_CROSSING_EXCESS_TRANSPORT_FLOOR.md` | Gives `rho>=48` |
| `rho=48` elimination | **EXACT FINITE CERTIFICATE** | `rl42_additions/RL42_RHO48_ELIMINATION.md` | Eliminates equality; gives **`rho>=49`** |
| `rho=49` crossing family sparsity | **EXPLORATORY / UNFROZEN** | none | Reproduce before use |

## Important dependency distinction

The theorem/certificate chain for `rho>=49` does **not** depend on reconstructing the lost RL41 area-26/27 large transient search tables.

The prior RL41->RL42 bundle is retained under `inherited/` solely for provenance and for auditing earlier arguments.

## Required first rerun

From the handover root:

```bash
bash verification/run_all_rl42_verifiers.sh
```

Expected final line:

```text
ALL RETAINED RL41/RL42 VERIFIERS: PASS
```

The stored output is `verification/MASTER_VERIFIER_RUN.txt`.

## Audit cautions for RL43

1. Do not silently upgrade the bounded statement “no crossing with `e<=3`, `p<=47`” into an infinite theorem.
2. Recheck sign conventions when omitting negative rank terms in the ordered-rank numerator inequality.
3. Preserve the exact meaning of `P`, `P_+`, `rho`, `delta_m`, excursion `p_E`, `r_E`, and `e_E`; several inequalities become false if these are conflated.
4. The `rho=48` DP is a safe over-approximation. Its usefulness is one-sided: no endpoint in the superset proves impossibility; surviving endpoints would require further physical filtering.
5. The `rho=49` three-layer reduction is a target, not yet an elimination theorem.
6. RL and the `g=2` branch remain open.

# RL46 Reproducibility Ledger

Date: 2026-08-22

Run from the bundle root.

## Required first step

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl46_structural_verifiers.sh
bash verification/run_rl46_q55_verifier.sh
```

Any failure is a stop-and-repair event.

## Core RL46 sources

- `rl46_additions/verify_fixed_pair_prefixcap_cutofffree.py`
  - no excess cutoff; repaired virtual neutral-pump activation;
  - fixed-pair exact prefix-cap structural search.
- `rl46_additions/verify_min_excess_65_41_fast.py`
  - exact minimum-excess DP without parent storage; used by the core verifier.
- `rl46_additions/min_excess_fixed_target_65_41.py`
  - same minimum-excess DP with explicit 59-column path reconstruction; retained as the human-auditable witness generator.
- `rl46_additions/verify_fixed_pair_violation_layerdp.py`
  - actual-column minimum-H dominance DP for strict terminal-valuation violations.
- `rl46_additions/verify_fixed_pair_boundary_layerdp.py`
  - same DP including the equality boundary.
- `rl46_additions/search_exactcap_pair_repaired.py`
  - repaired finite-E virtual-pump search retained for regression testing / comparison.

## Recorded outputs

- `out_cutofffree_pair_46_29.txt`
- `out_cutofffree_pair_65_41.txt`
- `out_min_excess_target_65_41.txt`
- `out_layerdp_violation_149_94.txt`
- `out_boundary_149_94.txt`
- `out_layerdp_violation_214_135.txt` — partial q=79 log only.

## Expected core conclusions

1. `(46,29)` cutoff-free search: `hits 0`.
2. `(65,41)` cutoff-free search: exactly one hit, equal to
   `(22,2,16,38,39,0,0,False,60,31)`.
3. `(65,41)` minimum-excess DP: target present, `min_e 125`.
4. `(149,94)` boundary DP: `violations []` and `equalities []`, which also implies no strict violation.

The core verifier checks these conclusions by rerunning the source programs. The separate strict-violation output is retained as an independent regression record. Runtime depends on hardware; the q=55 boundary search is the expensive part.

## Inherited RL45

`inherited/rl45_output/` is the unpacked RL45 research output, including its two verifiers and its own checksum ledger. The original RL45 zip and sidecar are also retained in `inherited/` for provenance. To rerun the inherited RL45 computational suite separately, use `bash verification/run_inherited_rl45_verifiers.sh`. It is intentionally not part of the RL46 core runner because the RL45 H<=23 certificate is substantially heavier.

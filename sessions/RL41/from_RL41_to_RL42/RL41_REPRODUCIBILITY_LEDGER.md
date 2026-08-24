# RL41 reproducibility ledger

Date: 2026-08-22

## Fully retained

- Entire RL40->RL41 handover archive, itself containing RL39 inheritance and RL40 verifiers/notes.
- `stream_25_fast.cpp` — exact area<=25 streaming excursion/envelope generator used in RL41.
- `stream25_fast_stats.txt` — retained exact counts/envelopes through area 25.
- `global_dp25_g4.py` — compressed `G=4` area-25 distortion search source.
- `qmod_area24_alltargets.py` — absolute numerator-residue verifier logic for all ten area-24 `(46,29)` targets.
- `verify_rl41_arithmetic_checkpoint.py` and its PASS record.
- `stream_25_repro.cpp` — reconstruction source showing how to add the absolute `Q_alpha,Q_beta` columns to the excursion stream. It is intentionally source-only; a naive monolithic run writing all rows exceeded the per-call runtime ceiling in this handover session and should be partitioned in RL42.

## Partially retained / requires regenerated scratch tables

`global_dp25_g4.py` expects generated files such as `small_types_18_fast_raw.tsv` and `cross_types_25_fast_raw.tsv`.

`qmod_area24_alltargets.py` additionally expects raw absolute shape tables with `Q` columns.

These raw tables are derivable from the retained enumerator sources but are not bundled because the attempted monolithic regeneration was interrupted before completion. Do not use partial scratch outputs; none are included.

## Completed in RL41 session but source/data not fully retained

The following computations were reported complete during RL41 but need reconstruction for independent artifact audit:

- area-25 all-22-target absolute numerator elimination;
- area-25 `G=8` zero-path check;
- area-26 chunked exact crossing enumeration and its 29,099 crossing table;
- area-26 compressed DP yielding 38 `(46,29)` and 2 `(65,41)` candidates;
- area-26 absolute residue elimination of all 40;
- area-27 special `1+7+19` branch scan;
- area-27 complete compressed search: zero `G=8`, zero `G=12`, 66 `G=4` abstract survivors all at `(46,29)` or `(65,41)`;
- area-27 full/small-modulus residue elimination;
- witness-modulus searches identifying `44110909` and `323399`.

These findings are preserved numerically and structurally in `RL41_PROOF_STATUS_AND_RL42_ATTACK.md` so they can be reconstructed exactly.

## Audit policy for RL42

Use `rho>=28` as the working continuation checkpoint, but before citing it as independently verifier-backed, reconstruct and rerun areas 26 and 27. Any mismatch is a stop-and-repair event.

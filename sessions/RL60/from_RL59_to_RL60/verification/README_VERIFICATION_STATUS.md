# RL59 -> RL60 verification status

Date: 2026-08-23

The outer RL58->RL59 archive checksum was verified exactly at the start of RL59.

The original combined inherited verifier encountered its documented heavy exact-search runtime bottleneck; no mathematical assertion failure was observed. Lightweight inherited algebra/grammar checks were run separately and passed during RL59.

The new RL59 verification runner performs only the new targeted checks and reproducible finite boundary searches. It does not rerun every historical heavy search.

## New checks

1. `verify_rl59_typeB_normalizedP_obstruction.py`
   - exact normalized-P contradiction for the concrete four-pump Type-B exit;
   - PASS in RL59.

2. `verify_rl59_defect_compatible_fourpump_entry.py`
   - exact prefix witness to `(73,47,1,3)`;
   - exact defect `<5/3`;
   - four local pumps produce `>5/4` aligned mass;
   - PASS in RL59.

3. `verify_rl59_final_tail_forcing.py`
   - rational regression for the earlier final-tail bounds;
   - PASS in RL59.

4. `verify_rl59_strengthened_tail_bootstrap_arithmetic.py`
   - checks `M_final>23/4` coefficient arithmetic;
   - checks K25/K27/K29 conversion to forced zero counts;
   - includes corrected K27 arithmetic;
   - PASS in RL59.

5. `search_small_terminal_ancestors.cpp`
   - exact deterministic shortcut search for the K>=25 boundary;
   - below boundary: no hit through `11,184,809`;
   - at boundary: first hit `11,184,810`, K=25.

6. `search_terminal_ancestors_kmin.cpp`
   - generalized exact deterministic shortcut search;
   - K>=27 below/at boundary reproduced;
   - K>=29 below/at boundary reproduced.

## Audit classification

The finite searches are exact integer computations and their boundary runs reproduce. They still use one algorithmic design and caching strategy. Before publication-grade promotion, RL60 should independently audit or reimplement the search logic.

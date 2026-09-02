# RL235 verification

Portable fast suite:

`sh verification/run_fast_rl235_verifiers.sh`

It checks the exact repaired charge levels, the 13 reconstructed generic-budget overages, exact rational K-pricing for every overage that needs it, the invariant-specific H21 spacing penalty, the repaired `>712` floor, derived variation bounds, and the H20 incidence/spacing-185 successor threshold.

`verify_rl235_full_prefix_rebuild.py` independently reconstructs all 7,531 atomic cells from inherited first-defect arithmetic and full-prefix filtering, then proves exactly 13 can exceed a conservative charge envelope. It is the exhaustive reconstruction audit and is intentionally separate from the portable fast suite.

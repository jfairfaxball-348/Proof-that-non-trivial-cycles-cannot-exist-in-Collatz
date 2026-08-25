# RL93 correction and demotion ledger

## Corrected preliminary successor charge

During live frontier propagation, the preliminary arithmetic continued using `L_common=10,000,053` after the 15M ultra tier became load-bearing. That common charge is too strong for ultra-only covered blocks.

The promoted RL93 theorem uses `L_common=15,000,053`.

Effects:

- at `k=2,921,750,255`: capacity `365,524 -> 365,567`, margin `+5,253 -> +5,210`;
- at `k=2,921,750,257`: capacity `365,526 -> 365,569`, margin `-10,736 -> -10,779`.

The signs are unchanged, so the exact eliminated interval and new endpoint are unchanged.

Classification: bookkeeping repair; preliminary displayed margin tuples demoted, theorem endpoint retained.

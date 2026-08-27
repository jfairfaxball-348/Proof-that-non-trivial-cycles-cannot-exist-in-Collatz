# RL134 verification

Run:

`bash verification/run_fast_rl134_verifiers.sh`

The verifier uses exact integer/rational arithmetic and rigorous rational logarithm intervals. It checks the inherited CF neighborhood and floor lock, the RL134 determinant-shell thresholds and translate bases, the `g<=11` discrepancy classification inequalities, the `g=1` `m<2^75` bound, the sharpened top-rho shallow-population constants, and the absolute `2^79` / `2^80` state windows.

The analytic least-state ownership theorem is proved in the main report. Population lower bounds and their state-count consequences remain conditional on the inherited external `R#>=2^71`.

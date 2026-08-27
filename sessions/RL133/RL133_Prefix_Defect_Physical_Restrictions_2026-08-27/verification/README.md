# RL133 verification

Run `./run_fast_rl133_verifiers.sh`.

The verifier uses exact rational interval arithmetic for `log 2` and `log 3` to reconstruct the first-survivor CF neighborhood, verify the survivor discrepancy and floor lock, reproduce the determinant-one mechanical shift, and regenerate the exact shallow-defect population constants.

The least-state prefix squeeze and defect physical-height theorem are analytic proofs in the report; the verifier checks their load-bearing arithmetic constants rather than replacing those proofs with sampling.

The population statements remain conditional on the inherited external input `R#>=2^71`. The new prefix-defect theorem is scoped to the full-count `g=1` realization of the first reduced survivor.

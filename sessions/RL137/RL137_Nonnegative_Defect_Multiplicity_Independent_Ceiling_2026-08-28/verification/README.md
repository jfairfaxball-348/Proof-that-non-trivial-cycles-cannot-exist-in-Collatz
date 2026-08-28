# RL137 verification

Run `bash verification/run_fast_rl137_verifiers.sh`.

The verifier uses exact `Fraction` arithmetic and rigorous logarithm
enclosures to reconstruct the one-period mechanical-weight upper bound and
certify `R/(3 Delta)<2^75`. The block cancellation is analytic and proved in
the RL137 report. No external least-cycle floor is used by the verifier.

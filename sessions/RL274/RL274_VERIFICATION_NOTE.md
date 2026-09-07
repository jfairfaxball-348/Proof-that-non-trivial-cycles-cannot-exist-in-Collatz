# RL274 verification note

Date: 2026-09-07
Worker: connector worker with local sandbox verification.

Candidate verification:
- analytic verifier: PASS
- transport normal-form checks: 7,722
- even-parity checks: 1,446
- determinant-discrepancy identity/inequality checks: 85,956
- doubling identity/negative-mass checks: 66,400
- internal SHA256 manifest: PASS
- clean fresh ZIP unpack: PASS
- verifier rerun from clean unpack: PASS with identical output

The verifier exhaustively checks all nonconstant binary words of lengths 4 through 9 for the transport/parity/discrepancy identities in its stated finite ranges, and all binary words of lengths 5 through 11 for the stated doubling checks.

This is verification of the RL274 analytic identities and scope discipline. It is not a finite certificate for global Collatz exclusion.

Knowledge catalogues: stale/deferred.

# RL337 closeout

Date: 2026-09-16
Status: CLOSED AND FROZEN

RL337 did not close R1, Gate A, Gate B, or the global positive non-trivial-cycle theorem. It did materially sharpen the exact-state frontier.

The principal theorem is the exact affine profile-collapse identity: admissible profile deformation preserves total exponent, lowers the affine carry by an explicit nonnegative sum of `1-2^-Q_k` terms, and the carry-drop concatenates with positive weights. The correct fixed-terminal consequence is that the profiled source is smaller than the zero-profile mechanical source.

A second analytic result gives an all-length right-suffix compression: because every positive run ends at height one and may fall by at most one per rank, every fixed-depth right suffix has a finite profile grammar independent of the total positive-run length.

The most useful exact physical diagnostic is the p=5 witness family `(24,27)`, `(24,28)`, `(24,29)`: all three labels correspond to the same physical source, the same run-exit state, and profile `(2,1,2,1,1)`, while the reverse orientations have no physical realization. This supports the hypothesis that anonymous fallback edges are introducing nonphysical cycle structure.

RL337 also corrected an important scratch sign error. No theorem depending on the incorrect direction is retained. The attempted mechanical-reference least-state barrier, ordinary residue ordering, cyclic denominator argument, and exploratory 3-adic decoding remain demoted or diagnostic only.

Portable verifier:

`python3 -I sessions/RL337/verification/verify_rl337_affine_profile_and_identity.py`

Expected output is frozen in `sessions/RL337/RL337_VERIFIER_OUTPUT.txt`.

The successor should not resume blind p-by-p enumeration. RL338 should attack exact shared-state ownership for the arbitrary-positive fallback layer, preferably by combining the fixed-depth right-suffix grammar with exact residue/state reconstruction. The target is a support-uniform physical quotient in which one can prove acyclicity, owned descent, or another exact obstruction.

`PARENT_DIFFICULTY_DELTA = EASIER`.

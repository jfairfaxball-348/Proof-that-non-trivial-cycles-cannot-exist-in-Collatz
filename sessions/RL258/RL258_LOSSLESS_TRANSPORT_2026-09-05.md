# RL258 lossless transport note

Date: 2026-09-05

The promoted RL258 state is frozen directly in the Git tree under
`sessions/RL258/`.

The directory contains the incoming authority snapshot, mathematical
certificate report, correction/demotion ledger, closeout report, exact
portable verifier, recorded verifier output, successor RL259 target and
kickoff, and internal SHA256 manifest.

This connector closeout uses the committed session directory itself as the
lossless transport. Every promoted text artifact is present byte-for-byte in
the Git tree and covered by `SHA256SUMS.txt`.

No binary ZIP is required for reconstruction, matching the immediately prior
RL257 connector convention.

# RL257 lossless transport note

Date: 2026-09-05

The promoted RL257 state is frozen directly in the Git tree under
`sessions/RL257/`.

The directory contains:

- the mathematical report;
- correction/demotion ledger;
- closeout report;
- exact portable verifier;
- recorded verifier output;
- successor RL258 target and kickoff;
- internal SHA256 manifest.

This connector closeout uses the committed session directory itself as the
lossless transport. Every promoted text artifact is present byte-for-byte in
the Git tree and covered by `SHA256SUMS.txt`.

No binary ZIP is required for reconstruction.

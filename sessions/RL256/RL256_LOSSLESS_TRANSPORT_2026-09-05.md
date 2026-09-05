# RL256 lossless transport note

The complete RL256 closeout payload is frozen directly under `sessions/RL256/`
as ordinary UTF-8 repository files, including:

- theorem/checkpoint document;
- correction/demotion ledger;
- closeout report;
- session-state/successor handover;
- successor target;
- portable verifier;
- fresh-verification record;
- internal `SHA256SUMS.txt`.

This connector closeout uses the committed session directory itself as the
documented lossless transport. No binary ZIP is required to reconstruct the
promoted proof state: every promoted artifact is present byte-for-byte in the
Git tree and is covered by the internal SHA256 manifest.

Knowledge catalogues are stale/deferred.

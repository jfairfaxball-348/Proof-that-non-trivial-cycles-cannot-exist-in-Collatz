# RL254 documented lossless transport

Date: 2026-09-05

This closeout uses the repository protocol's documented lossless session-directory transport.

Canonical repository transport is the frozen `sessions/RL254/` directory containing:
- the exact incoming START_HERE and RL254 target;
- the promoted theorem report;
- closeout report;
- correction/demotion ledger;
- successor state and RL255 target;
- `SHA256SUMS.txt`;
- portable verifier;
- fresh-verification record.

An independent local canonical ZIP is built from the same payload before promotion. Its SHA256 is recorded in the fresh-verification file.

The binary ZIP is not stored in the repository; the checked filewise session payload is the lossless canonical repository handover.

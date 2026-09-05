# RL253 documented lossless transport

Date: 2026-09-05

This connector-worker closeout uses the repository protocol's allowed documented lossless transport in place of storing an additional binary ZIP object.

Canonical repository transport is the frozen `sessions/RL253/` directory containing the incoming target, theorem checkpoint, closeout report, correction/demotion ledger, successor state/target, `SHA256SUMS.txt`, portable verifier, and fresh-verification record.

An independent local canonical ZIP, `RL253_Exact_38_Window_Beta6_Obstruction_2026-09-05.zip`, was built from the same payload and verified before promotion.

ZIP SHA256: `df8291e8b2c6a7737900a52f8edc272b9ac2275d2366e7380ad241560c97eca7`

Checks: ZIP CRC PASS; internal SHA256SUMS PASS; portable verifier PASS.

The binary ZIP is not stored in the repository; the checked filewise session payload is the lossless canonical repository handover.

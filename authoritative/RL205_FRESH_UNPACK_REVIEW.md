# RL205 fresh-unpack review

Date: 2026-08-31. Final candidate closeout review.

RL205 is a strategic theorem-selection generation with no new mathematical theorem or
finite mathematical certificate.

The final deterministic one-root ZIP is required to pass:

- ZIP CRC test;
- extraction into an empty temporary directory;
- internal `SHA256SUMS.txt` verification;
- `python3 verification/verify_rl205_route_tournament.py` from the clean unpack;
- exact comparison of verifier output with `RL205_FAST_SUITE_OUTPUT.txt`.

The closeout process performs those checks before Git promotion. Promotion is forbidden if
any check fails or if BASE_HEAD / incoming authoritative tree identity changes.

Knowledge catalogue refresh remains stale/deferred and is non-blocking under `AGENTS.md`.

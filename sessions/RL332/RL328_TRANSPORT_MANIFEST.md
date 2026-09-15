# RL328 transport manifest

Date: 2026-09-15
Transport: documented lossless Git-tree transport for connector-worker promotion

Incoming RL: RL328
Successor RL: RL329
BASE_HEAD: `f66176e3ae9dd502b0b99b90937e6f7aa5501429`

The frozen `sessions/RL328/` tree and successor `authoritative/` tree are intentionally byte-identical. Git blob identities plus the immutable Git tree provide the lossless transport/checksum boundary for this connector transition.

Portable verifier suite:

- `verification/verify_rl328_route_viability.py`
- `verification/red_team_rl328_route_viability.py`

A deterministic local ZIP of the same candidate was separately constructed, SHA-256 hashed, fresh-unpacked, and passed the verifier/red-team suite; it is redundant and not load-bearing for the committed Git-tree transport.

Knowledge catalogues: stale/deferred.

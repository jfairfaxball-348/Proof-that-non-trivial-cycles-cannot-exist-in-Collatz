# RL327 transport manifest

Date: 2026-09-15
Transport: physical deterministic ZIP plus outer SHA-256 sidecar

Incoming RL: RL327
Successor RL: RL328
BASE_HEAD: `f37a2984065548440a8ae0973060f97a40a44a2b`

Canonical bundle: `RL327_to_RL328_Handover.zip`
Outer sidecar: `RL327_to_RL328_Handover.zip.sha256`

The ZIP contains the complete flat successor handover package rooted at `START_HERE.md`. Its internal `SHA256SUMS.txt` covers every package file except itself. The portable verifier suite is:

- `verification/verify_rl327_owned_excess_density.py`;
- `verification/red_team_rl327_owned_excess_density.py`.

The deterministic ZIP uses sorted paths, stored file mode `0644`, timestamp `2020-01-01T00:00:00`, and deflate compression.

Codex exploratory scripts, checkpoint state, and command log are preserved separately under the frozen `sessions/RL327/scratch/` tree; they are not successor authority.

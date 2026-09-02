# RL235 provenance

Date: 2026-09-02

Incoming authoritative state: RL234 STOP-AND-REPAIR at repository `main` after infrastructure-only commit `2ecbe7e3d9a829451976e3944ab97f6ba869bb54`.

Load-bearing inherited sources:

- RL234 stop-and-repair theorem and exact charging-gap verifier: incoming authoritative package tree `2eb4a804304dba82ee98ce778c31c10cc031322b`;
- RL231 chronological recurrence theorem and verifier: frozen RL231 package tree `98b2f247ca6e2c40808cd519c148e0320f5ba6b7` under `sessions/RL232/`;
- RL232 H17 cross-family results and RL233 finite-modulus decomposition are preserved exactly as recorded in RL234's proof/correction ledgers.

RL235 reconstructs the first-defect/full-prefix state space directly into `verification/verify_rl235_full_prefix_rebuild.py`. `verification/verify_rl235_full_prefix_rebuild.py` is the exact certificate reconstruction path and proves the exhaustive 7,531-cell partition plus the exact 13 conservative-envelope overages. The portable fast suite then reruns all load-bearing charging/K-pricing/bottleneck arithmetic on those 13 explicitly frozen overage cells.

Connector-worker closeout uses GitHub tree/blob/ref identities plus local exact Python/hash verification; no repository-shell command is claimed.

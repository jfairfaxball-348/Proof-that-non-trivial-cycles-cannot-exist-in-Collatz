# RL299 — lossless transport note

The promoted `sessions/RL299/` directory contains the report, proof/barrier ledger, physical replay record, external-provenance note, closeout, successor target, incoming-target snapshot, internal SHA256 manifest, and portable verification sources as individual Git blobs.

`SHA256SUMS.txt` hashes every promoted handover payload file except itself. Closeout verified those hashes and reran `verification/verify_rl299_fast.py` from the final closeout copy.

The exhaustive U4 physical replay is represented by its gap-free shard log plus the portable C reproducer; it is not rerun in the fast suite because it evaluates 408,827,892 trajectories.

Knowledge catalogues are `stale/deferred` under the connector closeout policy and are not proof-state authority.

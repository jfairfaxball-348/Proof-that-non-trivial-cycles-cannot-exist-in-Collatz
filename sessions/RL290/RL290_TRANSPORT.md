# RL290 transport

Date: 2026-09-09

Connector-worker closeout transport uses direct Git objects.

Base:

`98d05bd1de0f4f57c93f55b0c648b9264409832c`

Procedure:

1. freeze the complete RL290 payload under `sessions/RL290/`;
2. include the main analytic report, closeout, scratch freeze, verifier, deterministic verifier output, red team, successor target, README, and SHA256 manifest;
3. replace the authoritative RL290 target with the RL291 audit target;
4. update `authoritative/START_HERE.md`;
5. create one tree from the exact base tree;
6. create one commit with the base head as sole parent;
7. fast-forward `main` exactly once;
8. read back `main`, authoritative files, and key RL290 payloads.

No ZIP archive is used.

No `.zip.sha256` sidecar applies.

`SHA256SUMS.txt` covers every frozen RL290 payload except itself.

Generated knowledge catalogues remain unchanged and `stale/deferred`.

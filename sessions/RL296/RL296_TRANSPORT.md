# RL296 transport

This transition uses the connector-worker direct Git-object transport permitted by `AGENTS.md` and `docs/VERIFICATION_AND_CLOSEOUT.md`.

There is no ZIP transport and therefore no outer ZIP sidecar.

Lossless transport/integrity is provided by:

1. complete UTF-8 session files frozen under `sessions/RL296/`;
2. internal `SHA256SUMS.txt`;
3. clean reconstruction into a fresh local directory followed by manifest verification;
4. rerun of the portable closeout verifier suite from that clean reconstruction;
5. Git blob SHA identities, one explicit base-tree-derived Git tree, one commit, and one non-forced `main` ref advance;
6. post-commit readback of the remote ref, frozen session, and successor authority.

Generated knowledge catalogues are stale/deferred and are not part of the mathematical integrity boundary.

# RL289 connector-worker lossless transport

RL289 is closed using direct GitHub Git-object transport.

The handover is authenticated by:

- one atomic commit whose parent is the recorded RL289 base head;
- committed blob/tree identities for the complete `sessions/RL289/` payload;
- exact reuse of the incoming RL289 target blob inside the frozen session;
- the portable verifier and recorded PASS output;
- the RL289 red-team PASS;
- exact successor-target blob identity between the frozen RL289 handover and `authoritative/`;
- post-commit remote readback.

This connector-worker closeout uses the repository's documented lossless direct-object transport convention. No ZIP archive or `SHA256SUMS.txt` sidecar is required.

Generated knowledge catalogues are unchanged and `stale/deferred`; they are not mathematical authority.

# RL287 connector-worker lossless transport

RL287 is closed using direct GitHub Git-object transport.

The handover is authenticated by:

- one atomic commit whose parent is the recorded RL287 base head;
- committed blob/tree identities for the complete `sessions/RL287/` payload;
- exact reuse of the incoming RL287 target blob inside the frozen session;
- the portable verifier and recorded PASS output;
- the RL287 red-team PASS;
- exact successor-target blob identity between the frozen RL287 handover and `authoritative/`;
- post-commit remote readback.

This connector-worker closeout uses the repository's documented lossless direct-object transport convention. No ZIP archive or `SHA256SUMS.txt` sidecar is required.

Generated knowledge catalogues are unchanged and stale/deferred; they are not mathematical authority.

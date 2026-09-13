# RL311 lossless transport note

Environment: connector worker.

Base authority snapshot:

- base HEAD: `d54bb13118f6fd80b8fc0632e8441f62c932495c`;
- base tree: `c79b4d03f626e2d4079c42bd73472630dcbc9bca`;
- incoming authoritative target blob: `3ae4b5e53254d1e2a1f150db04602521b51f73f0`.

RL311 is transported losslessly by the repository-resident text files in
`sessions/RL311/` plus their internal `SHA256SUMS.txt`. No ZIP bundle is used for
this connector-worker generation; this note is the documented-lossless-transport
form permitted by the closeout convention.

Candidate verification:

- `verify_rl311_closeout.py`: PASS in a clean local sandbox;
- incoming RL310 exact verifier was accepted under verification economy and was
  additionally replayed during closeout from the repository-resident script;
- no large finite RL311 certificate is claimed;
- RL311 theorem-grade items are analytic or exact finite Bellman replays as
  classified in `RL311_CLOSEOUT.md`.

Corrections/demotions are explicit in the closeout. In particular:

- the scratch block-strip lower bound assuming every block contains a `1` is not promoted;
- `E_j<=floor(kappa_ext/A)` is corrected to the valid rounded consequence;
- the short balanced-return theorem uses the independent valid bound `0<=E_j<=h`.

Successor authority consists only of:

- `authoritative/START_HERE.md`;
- `authoritative/RL312_SHORT_OWNED_BALANCED_RETURN_CONSUMER_TARGET.md`.

Generated knowledge catalogues are `stale/deferred` and intentionally unchanged.

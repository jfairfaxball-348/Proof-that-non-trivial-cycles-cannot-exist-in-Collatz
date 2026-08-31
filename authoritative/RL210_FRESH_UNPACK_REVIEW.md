# RL210 fresh-unpack review

Connector closeout uses the documented lossless-transport option in
`docs/VERIFICATION_AND_CLOSEOUT.md`. The incoming immutable authority is pinned by
BASE_HEAD `3412fc6b8fefa2a5eba4626dc3dd73a6322739b5` and incoming authoritative
tree `c918e8f1fdf4b0e30daf24c3af84ffd75c8d575a` in
`transport/INHERITED_GIT_OBJECTS.json`.

The RL210 overlay ZIP is built with an internal `SHA256SUMS.txt`, checked against
its outer `.zip.sha256` sidecar, extracted into a new empty temporary directory,
and every manifest entry is verified there. From that clean extraction,
`verification/verify_rl210_global_prefix_overlap.py` reproduces the exact finite
certificate and `verification/verify_rl210_proof_state.py` passes successor
uniqueness, transport identities, counts, correction locks and physical/Gate
locks.

Unchanged inherited subtrees/blobs are accepted by exact Git identity under
verification economy. The complete successor authority is assembled from those
pinned inherited objects plus the verified RL210 overlay before one atomic Git
ref advance. `sessions/RL209` is the frozen incoming authority; successor
authority is completed RL210 with unique incoming RL211 target.

Promotion additionally requires remote `main` still to equal BASE_HEAD immediately
before commit/ref advance, followed by readback of the remote ref, frozen session
and successor `authoritative/START_HERE.md`. Knowledge catalogues remain
**stale/deferred** and are outside the proof-state gate.

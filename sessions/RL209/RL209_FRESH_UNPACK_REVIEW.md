# RL209 fresh-unpack review

Connector closeout uses the documented lossless-transport option in
`docs/VERIFICATION_AND_CLOSEOUT.md`. The incoming immutable authority is pinned by
BASE_HEAD `a080622ce3d020c249b71c8b12552361601810de` and incoming authoritative
tree `159e625b25c7cd9aadf6f53f03e0a63643906c32` in
`transport/INHERITED_GIT_OBJECTS.json`.

The RL209 overlay ZIP was built with an internal `SHA256SUMS.txt`, checked against
its outer `.zip.sha256` sidecar, extracted into a new empty temporary directory,
and every manifest entry was verified there. From that clean extraction,
`verification/verify_rl209_pointwise_root_cone.py` reproduced the stored exact
certificate byte-for-byte and `verification/verify_rl209_proof_state.py` passed
successor uniqueness, transport identities, counts, correction locks, physical/Gate
locks and target uniqueness.

The unchanged inherited subtrees/blobs are accepted by exact Git identity under
verification economy. The complete successor authority is assembled from those
pinned inherited objects plus the verified overlay before one atomic Git ref
advance. `sessions/RL208` is the frozen incoming authority; successor authority is
completed RL209 with unique incoming RL210 target.

Promotion additionally requires remote `main` still to equal BASE_HEAD immediately
before commit/ref advance, followed by readback of the remote ref, frozen session
and successor `authoritative/START_HERE.md`. Knowledge catalogues remain
**stale/deferred** and are outside the proof-state gate.

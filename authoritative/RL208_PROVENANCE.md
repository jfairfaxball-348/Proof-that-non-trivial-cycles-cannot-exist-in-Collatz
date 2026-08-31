# RL208 provenance and verification economy

BASE_HEAD at RL208 startup/closeout: `50308656ab2b97cb34efcfd5c546280d45884685`.
Incoming authoritative tree: `281c81d6a78dbf97084796edb1f9f99c66c1b8ea`.
The intervening post-RL207 commit changed only generated knowledge catalogues,
`tests/test_rl_conveyor.py`, and `tools/rl_catalog.py`; it did not change the
incoming authoritative tree.

The RL207 handover records a passed outer checksum/internal manifest/clean-unpack
and complete inherited fast gate.  RL208 accepts the unchanged RL206 mathematical
verifiers and outputs by exact Git blob identity under verification economy.
The new RL208 layered-root verifier was executed independently twice from local
clean files and returned the same exact 2,765,120,323 deletion and
13,423,606,911 remainder; its certificate additionally performs a coordinate-
swapped recount of every layer.

Connector closeout uses documented lossless transport: immutable inherited Git
subtrees/blobs are identified in `transport/INHERITED_GIT_OBJECTS.json`; the new
RL208 overlay is ZIP-packed with an internal SHA256 manifest and outer sidecar,
fresh-unpacked locally, and its current verifier/proof-state guard rerun there.
The repository transport stores that exact ZIP losslessly as numbered base64 parts
with `PART_SHA256SUMS.txt` and `reconstruct_rl208_bundle.py`; reconstruction must
match the outer ZIP SHA256 before use.
The final complete successor authority is assembled from those exact inherited
objects plus the verified overlay before the single Git ref update.

No full 16-billion-rank materialization or recount is claimed.  Exact floor-sum
counts certify the new predicate.  Knowledge catalogues are left unchanged and
reported **stale/deferred** for RL208.

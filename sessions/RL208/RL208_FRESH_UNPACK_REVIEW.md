# RL208 fresh-unpack review

Connector closeout uses the documented lossless-transport option in
`docs/VERIFICATION_AND_CLOSEOUT.md`.  The immutable inherited portion is pinned
by Git tree/blob identities plus `transport/INHERITED_SHA256SUMS.txt`; the new
RL208 overlay is the verified ZIP payload.  Repository transport uses numbered
base64 parts plus a reconstruction script and per-part hashes to reproduce that
exact ZIP byte-for-byte.

Before promotion, the overlay ZIP passed CRC testing, was extracted into a new
empty temporary directory, and every physical overlay file passed the internal
`SHA256SUMS.txt` check.  From that clean extraction,
`verification/verify_rl208_layered_root_cone.py` reproduced the stored JSON
certificate byte-for-byte and `verification/verify_rl208_proof_state.py` passed
successor uniqueness, transport identities and all scope locks.

The unchanged inherited RL206 verifier scripts and outputs are accepted by exact
Git blob identity against the already-passing RL207 handover under verification
economy; no shell rerun of those unchanged scripts is falsely claimed.  The
complete successor authority is assembled from the pinned inherited objects and
the fresh-unpacked overlay before the single ref update.

Promotion additionally requires remote `main` to remain at BASE_HEAD
`50308656ab2b97cb34efcfd5c546280d45884685` with incoming authoritative tree
`281c81d6a78dbf97084796edb1f9f99c66c1b8ea`, followed by atomic commit/ref
advance and readback.  Knowledge catalogues are stale/deferred and are not part
of the proof-state gate.

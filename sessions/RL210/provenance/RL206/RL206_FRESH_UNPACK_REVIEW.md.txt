# RL206 fresh-unpack review

Final candidate must pass, and did pass before its atomic promotion:
ZIP CRC; outer SHA256 sidecar; fresh extraction into an empty temporary
directory; exact manifest coverage and hashes; exact byte comparison with
frozen candidate; all four portable verifier scripts; equality of mathematical
outputs with their recorded certificates; proof-state scope checks.

This is a packaging/current-verification claim, not a proof by finite testing
of the analytic theorems. Their proofs and independent reviews are included.
The exact outgoing ZIP digest and replayed verifier output hashes are recorded
in the local candidate's FRESH_UNPACK_EVIDENCE.json before promotion. Every
bundle payload byte is sealed by SHA256SUMS.txt and the outer sidecar.

Incoming authority snapshot and remote BASE_HEAD are reconfirmed separately
before the one coherent session/authority commit and remote-ref advance.
Catalogue status: stale/deferred, explicitly non-blocking and not claimed current.

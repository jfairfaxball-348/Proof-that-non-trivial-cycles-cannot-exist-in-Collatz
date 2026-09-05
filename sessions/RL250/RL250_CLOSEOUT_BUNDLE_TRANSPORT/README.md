# RL250 closeout bundle transport

Lossless base64 transport for the canonical RL250 ZIP.

Verify `PART_SHA256SUMS.txt`, concatenate `RL250_bundle.zip.b64.part*` in lexical order, base64-decode, verify canonical ZIP SHA256 `17090bacbab6f08361adcd85d7bedaebf689d6f1a3aa94e6bb8dbe7abdb8345b`, fresh-unpack, verify `SHA256SUMS.txt`, and run `verification/verify_rl250_terminal_window_covering.py`.

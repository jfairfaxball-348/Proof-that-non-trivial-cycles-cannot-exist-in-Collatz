# RL271 fresh-unpack verification

Date: 2026-09-07

A candidate session bundle was unpacked into a clean temporary directory and `sessions/RL271/verification/run_fast_suite.sh` was executed from the unpacked copy.

Result: **PASS**.

The fresh run reproduced:
- corrected 3,514-tuple three-component cover; `[3,1,1]` 6,857,644 states and `[2,2,1]` 3,302,985 states, both with zero full-`D` hits;
- `[2,1,1,1]` 9,673,883 states with zero full-`D` hits, plus exact agreement of the independent secondary reconstruction;
- singleton primary sparse certificate: 13,640,991 side entries, zero admissible low-64 collisions, zero full-`D` hits;
- singleton alternate split: zero admissible collisions and zero full-`D` hits;
- `[4,1]` 10,762 total structural states, 7,748 positive-`D` states and zero full-`D` hits;
- exact determinant-pair metadata and pair-file hashes.

The exhaustive `A<=18` all-flat direct-word red team is retained separately with a successful frozen output; it is omitted from the fast suite because it is intentionally slower than the compressed certificates.

No new mathematics was performed during this fresh-unpack stage; this is closeout verification of the already achieved RL271 results.

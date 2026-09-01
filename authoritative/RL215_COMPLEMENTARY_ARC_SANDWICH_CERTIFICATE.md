# RL215 exact complementary-arc sandwich certificate

Date: 2026-09-01. Classification: **exact finite arithmetic certificate**, conditional on the proved analytic lower bound in `proofs/RL215_COMPLEMENTARY_ARC_SANDWICH_THEOREM.md`.

The verifier `verification/verify_rl215_arc_sandwich.py` reconstructs the full RL212/RL214 e=16 prefix domain and projects the new RL215 lower bound onto every exact RL214 progression.

Certified counts:

- exact e=16 root prefixes: **108,950**;
- H21-compatible prefixes: **45,046**;
- new integer root lower bound: **24,913,843,845,551,577,787,381**;
- inherited root upper bound: **31,285,589,992,934,194,300,574**;
- kmin 28,812: **26,133** prefixes;
- kmin 28,813: **18,913** prefixes;
- two-sided candidates before terminal filter: **331,935,455**;
- terminal-Hensel removals inside the window: **170**;
- two-sided candidates after terminal filter: **331,935,285**;
- prefixes deleted: **0**;
- minimum/maximum post-filter candidates per prefix: **7,367 / 7,369**;
- reachable eta classes modulo2187: **469**;
- new necessary-rank exclusions: **0**.

Post-filter mod18 candidate counts:
`0:107901476`, `8:58066202`, `9:107901377`, `17:58066230`.

Post-filter H21-state candidate counts:
`011:215802853`, `111:116132432`.

Relative to RL214's 1,629,818,931 post-terminal arithmetic candidates, RL215 removes
**1,297,883,646** arithmetic candidates. These are not terminal-rank exclusions or
physical populations.

Canonical witness digest:
`f059976b3627bde3b97e009b2f7ae6dd055d23eee7e5a641704fa61663962fe7`.

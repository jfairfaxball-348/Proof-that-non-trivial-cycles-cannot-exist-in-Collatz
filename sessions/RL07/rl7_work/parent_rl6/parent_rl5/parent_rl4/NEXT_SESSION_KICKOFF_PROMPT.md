Continue the Collatz R# RL branch from RL-4.

Read in order:

1. `README.md`
2. `RL4_CROSSING_SLACK_AND_CYCLE_EXIT_2026-08-19.md`
3. `RL4_CANONICAL_REGISTER_DELTA_2026-08-19.md`
4. `RL4_ROADMAP_UPDATE_2026-08-19.md`
5. `logs/RL4_CROSSING_EXIT_VERIFICATION_LOG.txt`
6. parent RL-3 report/register as needed

Re-run the RL-4 verifier first.

Primary target: continue the **k=0 plateau/exit grammar** from RL-L28/L29. The general plateau normal form is already proved. Quantify how often a periodic cycle must use deep exits `t>=n` or regular-high exits, and fuse that cost with the cycle product slope/common denominator. Also isolate the `s=L` one-plateau Diophantine boundary.

Secondary target: for `k>0`, use RL-L23/L25 to study multiple order crossings. Test whether every crossing forces a sign reversal in cumulative exponent difference that consumes a monotone phase/slack or total-variation budget. Treat the tail-smaller no-upcross case separately.

Do not spend time on raw Phi suffix matching or root-only xi ceilings; both routes have already been structurally exhausted.

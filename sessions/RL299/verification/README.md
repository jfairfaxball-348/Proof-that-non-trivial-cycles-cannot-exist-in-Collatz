# RL299 verification

`verify_rl299_fast.py` is the portable closeout verifier. It uses exact rational atanh bounds for `ln 2` and `ln 3`, checks the certified continued-fraction prefix, determinant-coordinate identities, block margins, gap-free U4 shard partition, exact quotient counts, extremal stopping witnesses, the sharpened imbalance lemma, and the four-step B-ancestry identity/barrier trigger.

`verify_rl299_physical_full.c` is the reproducible exhaustive physical-envelope verifier. Compile with a C compiler, then pass a half-open `h` interval. The five U4 ranges frozen in `RL299_FULL_PHYSICAL_REPLAY_LOG.txt` cover `h=0..204413945` without gaps. `--single H` independently replays any witness.

The full U4 replay is intentionally not part of the fast suite because it evaluates 408,827,892 trajectories. The closeout log records the gap-free shard outputs obtained during RL299; the portable C verifier preserves reproducibility.

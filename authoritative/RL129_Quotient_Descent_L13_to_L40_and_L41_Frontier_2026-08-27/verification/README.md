# RL129 verification

Run:

```bash
./run_fast_rl129_verifiers.sh
```

The suite performs three independent checks:

1. exhaustive small-word rotation/bound red-team;
2. exact regeneration of all `L=13..40` quotient ceilings;
3. compiled exact descent verification for every odd start through `30,400,121`.

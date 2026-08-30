# RL181 verification

Run:

```sh
bash verification/run_fast_rl181_verifiers.sh
```

`verify_rl181_pair_gap_occupancy.py` uses exact integer/Fraction arithmetic plus rigorous rational log/exp enclosures. It consumes only explicitly frozen RL180 certified bounds and checks the new uniform K corridor, shallow p-shift adjacency counts, repeated ordered-height-type multiplicities, and the four normalized-width occupancy fractions.

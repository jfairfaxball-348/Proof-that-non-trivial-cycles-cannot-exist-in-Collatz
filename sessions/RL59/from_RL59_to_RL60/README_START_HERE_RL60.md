# README — start here for RL60

Date: 2026-08-23

This handover continues the Collatz R-sharp / RL research from RL59.

## Immediate status

RL59 did **not** prove Gate A, Gate B, RL, or the Collatz conjecture, and did not eliminate the sole safe-CF survivor.

It did produce three important advances:

1. the exact RL58 synchronized `J=3 <-> 5` pump is **terminally neutralized** by a normalized terminal potential;
2. the burden moves to the final positive height-one synchronized tail, which is forced to carry more than `23/4` aligned mass;
3. an exact finite shortcut-dynamics search for odd terminal `K>=25` plus the terminal potential forces the survivor to satisfy at least

   `z >= 9,457,747`.

The strongest current route is a two-sided terminal bootstrap in the variables `K` and `z`, using

`K + z = q + 3`

with the inherited fixed `q`, together with lower envelopes for the smallest shortcut state that can reach any admissible terminal predecessor with odd `K>=K0`.

## Files to read first

1. `RL59_FINAL_PROOF_STATE_AND_RL60_TERMINAL_TAIL_BOOTSTRAP_ROADMAP.md`
2. `RL59_NEW_TERMINAL_POTENTIAL_AND_TAIL_LEMMAS.md`
3. `RL60_TERMINAL_TAIL_BOOTSTRAP_KICKOFF_PROMPT_2026-08-23.md`
4. `verification/README_VERIFICATION_STATUS.md`

The complete prior RL58->RL59 handover is preserved under `inherited_rl58_to_rl59/`.

## Integrity / regression

First verify the outer handover checksum, then run

```bash
bash verification/run_all_rl59_to_rl60_verifiers.sh
```

Treat any assertion failure or changed finite boundary as stop-and-repair.

The `K>=27` and `K>=29` finite boundaries have been reproduced in this session, but they are still best classified as exact finite computations pending an independent implementation audit.

## Important correction

Earlier session prose stated that the `K>=27` boundary forces at least `11,209,546` final aligned zeros. That arithmetic was wrong.

The correct value from

`floor(115*J_min/272)+1`, `J_min=26,512,143`

is

`11,209,179`.

The finite boundary `n_min=13,256,071` itself reproduces exactly.

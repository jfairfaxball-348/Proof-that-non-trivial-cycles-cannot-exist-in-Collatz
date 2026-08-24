# RL53 final proof state and RL54 roadmap

Date: 2026-08-23

## Executive status

RL and Collatz are **not closed**.

The inherited exact radius-3 branch remains certified. Gate B remains open because RL49 proved that the natural half-period rotation has cyclic transposition distance `2(a-t-3+H)`, not radius 3. Do not resurrect the old direct full-phase -> radius-3 identification.

Gate A `H>=t+3` remains open globally. The strongest strategic direction remains a full-phase impossibility theorem that could bypass the failed Gate-B shortcut.

## New RL53 theorem/certificate

For the sole stable continued-fraction survivor, RL53 eliminates both

`z=37` and `z=39`.

Combined with the inherited eliminations `z=27,29,31,33,35` and odd parity, the certified threshold advances to

`z >= 41`.

This statement applies only inside the inherited safe continued-fraction gate. It is not uniform over all denominators.

## z=37 closure

The exact terminal/defect cascade is

`(1,36)=97 -> (3,22)=69 -> (5,14)=52 -> (7,15)=57 -> (8,14)=59 -> (9,14)=60`.

It forces all ten late x-zero weights tiny. Then the exact non-greedy first-26 mass ceiling `11.798579834936028 < 143/12` forces the greedy first-26 schedule and `u_26=70`. Five delayed first-26 matching y-zeros already cost `2.059051471067492 > 5/3`, so the final suffix is `(10,14)`. Its exact terminal maximum is 60, versus the genuine suffix length `ell-38`.

Hence z=37 is impossible.

## z=39 closure

The exact cascade is

`(1,38)=104`, `(3,26)=78`, `(5,17)=60`, `(7,16)=60`, `(8,15)=58`, `(9,15)=61`, `(10,16)=65`, `(11,16)=67`.

This forces all twelve late weights tiny. The greedy first-26 schedule and `u_26=70` are again forced. The final suffix budget is `(12,16)`.

The exact terminal maximum is

`L_terminal(12,16)=67`,

while the genuine suffix length is

`ell-36 = 77692117359936589367`.

Contradiction. Therefore z=39 is impossible.

The two heaviest exact-x layers are backed by complete deterministic partition logs: 128/128 chunks for exact eleven and 512/512 chunks for exact twelve, both with global maximum 67.

## Reproducibility

Run

`bash rl53_research/run_rl53_frontier_verifiers.sh`

This checks the exact rational z=37 and z=39 bootstrap and audits the complete heavy chunk logs.

The deterministic C++ terminal solvers are included for independent recomputation. The file `rl53_research/RL53_EXACT_TERMINAL_RESULTS.txt` records all terminal maxima used in RL53.

## What is certified

- inherited radius-3 branch itself;
- RL49 correction invalidating the old direct radius-3 bridge;
- inherited stable-survivor eliminations z=27,29,31,33,35;
- RL53 elimination z=37;
- RL53 elimination z=39;
- stable continued-fraction survivor therefore has `z>=41`.

## What remains open

- z=41 and higher odd z in the stable survivor;
- any uniform theorem eliminating all remaining z;
- Gate A globally;
- Gate B / a valid global-to-radius-3 bridge;
- denominators outside the safe continued-fraction gate;
- RL closure and Collatz.

## RL54 primary target

Attack `z=41`, but do not simply continue an endless z-by-z brute-force sequence.

The z=39 cascade shows a repeatable monotone structure. RL54 should run two tracks in parallel:

1. **Concrete z=41 closure.** Start with the one-x-zero class `(1,40)`. If it is terminal-small, the first defect feedback after two tiny late weights permits at most 16 delayed first-26 y-zeros, giving the next target `(3,30)`. Continue with monotone cuts as in z=39.
2. **Uniformization.** Extract a recurrence or envelope for the successive suffix budgets and terminal maxima as a function of z. Determine whether the defect gain can dominate the growth in late-y budget for all odd z, or whether a new obstruction appears.

A uniform terminal/defect theorem would be much more valuable than merely reaching z=43 or z=45.

## Critical proof-state warnings

Do not claim:

- Gate A is proved;
- Gate A alone closes RL via radius 3;
- the z>=41 threshold covers all denominators;
- RL or Collatz is solved;
- the old half-period rotation gives radius 3.

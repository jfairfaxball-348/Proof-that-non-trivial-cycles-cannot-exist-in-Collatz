# RL52 final proof state and RL53 roadmap

Date: 2026-08-23

## Executive status

The RL branch and Collatz are **not closed**.

The inherited exact radius-3 branch remains a proved/certified component, but the previously hoped-for direct full-phase -> radius-3 identification is invalid. RL49 proved that the natural half-period rotation has cyclic transposition distance

`2(a-t-3+H)`,

not radius 3. Therefore **Gate B is open** and the old direct shortcut must not be resurrected.

Gate A remains the main live global structural target:

`H >= t+3`.

However, Gate A alone no longer automatically closes RL through the inherited radius-3 theorem. The strongest current strategic target is a **full-phase impossibility theorem** for the retained branch. Such a theorem would bypass the failed direct Gate-B shortcut entirely.

## Stable continued-fraction survivor: new certified threshold

Starting from the stable published `2^71` floor and the sole safe continued-fraction survivor, the exact coupled terminal-power program has now eliminated

`z = 27, 29, 31, 33, 35`.

The inherited parity condition makes `z` odd. Therefore the current certified stable threshold is

`z >= 37`.

This is a theorem/certificate only for the sole stable continued-fraction survivor. It is **not** a uniform proof of Gate A and does not control denominators outside the safe continued-fraction gate.

## Exact retained inputs

The productive RL51/RL52 mechanism uses the inherited exact inequalities and grammar:

- `Zx > 143/12`;
- `E < 5/3`;
- sequential x-zero cap `w_j < 17/30`;
- defect identity `E = sum_j w_j [1-(2/3)^r_j]`;
- terminal condition `J_end = 2^k`;
- exact backward coordinate `Q_d = J + 2^d - 1`.

Backward maps:

- `11: Q -> 2Q/3` when `3|Q`;
- `10: Q -> 2Q+1` (one y-zero);
- `00: Q -> 2Q-(3^d-1)` (one x-zero and one y-zero);
- `01: Q -> 2Q/3-3^(d-1)` when `d>1` and `3|Q` (one x-zero).

The height is redundant:

`d = 1 + (# y-zero edges used) - (# x-zero edges used)`.

## RL52 exact zero-event automaton

RL52 replaced exploding column-by-column BFS with an exact zero-event recursion.

At state `Q != 0`, let `v=v3(Q)`. Before the next zero event there can be exactly `r=0,...,v` backward `11` edges; an `01` event requires `r<v`. Every non-`11` event consumes at least one zero budget, so the recursion is finite.

The verifier carries `Q mod 3^P`. It rejects any run where the available ternary precision would make `v3(Q)` ambiguous. No positivity pruning is used, so the grammar is conservative.

Regression checks reproduced earlier sharp maxima:

- z=27 relaxed tail `(x<=0,y<=26)`: `56`;
- z=29 coupled tail `(x<=2,y<=6)`: `19`;
- z=31 coupled tail `(x<=4,y<=12)`: `38`.

## z=33 eliminated

RL51 had already proved

- `p_26 <= 56`, hence `u_26 <= 81`;
- at most 10 of `y_1,...,y_26` occur after `u_26`;
- terminal suffix budgets `x-zero <= 6`, `y-zero <= 16`.

RL52 proves exactly

`L_terminal(6,16) = 54`.

But a genuine z=33 suffix has required length at least

`ell - 53 = 77692117359936589350`.

Contradiction.

## z=35 eliminated by terminal/defect bootstrap

There are eight late x-zero indices `27,...,34`.

### Stage 1

`L_terminal(1,34)=85`.

This forces the last two x-zero weights to be less than `2^-1000`. Feeding their negligible mass back into the scalar and defect inequalities gives

- `p_26 <= 56`;
- at most 10 delayed first-26 y-zeros;
- total suffix y-budget `<=18`.

### Stage 2

`L_terminal(3,18)=52`.

The last four x-zero weights are negligible. Feedback improves to

- `p_26 <= 53`;
- at most 8 delayed first-26 y-zeros;
- suffix y-budget `<=16`.

### Stage 3

`L_terminal(5,16)=54`.

The last six x-zero weights are negligible. Feedback improves to

- `p_26 <= 49`;
- at most 6 delayed first-26 y-zeros;
- suffix y-budget `<=14`.

### Stage 4

`L_terminal(7,14)=51`.

All eight late x-zero weights are negligible. Therefore the first 26 x-zeros must carry essentially all `Zx > 143/12`. The exact best non-greedy first-26 schedule is only `11.798579...`, so the unique greedy schedule is forced and

`u_26 = 70`.

If five of the first 26 matching y-zeros were after column 70, their exact minimum defect contribution is

`2.059051471... > 5/3`.

Hence at most four are delayed. Including the eight later y-zero indices gives final suffix budgets

`x-zero <= 8`, `y-zero <= 12`.

Finally

`L_terminal(8,12)=48`,

while the genuine suffix must have length

`ell - 40 = 77692117359936589363`.

Contradiction. Thus z=35 is impossible.

## What is proved, open, and forbidden to claim

### Certified / exact

- inherited radius-3 branch itself;
- RL49 correction killing the old direct full-phase -> radius-3 match;
- RL51 eliminations z=27,29,31;
- RL52 elimination z=33 by exact `(6,16)` terminal automaton;
- RL52 elimination z=35 by exact analytic bootstrap plus exact terminal automata;
- sole stable continued-fraction survivor therefore has `z>=37`.

### Open

- z=37 and higher odd z in the stable survivor;
- Gate A globally;
- Gate B / any valid global-to-radius-3 bridge;
- denominators outside the safe continued-fraction gate;
- full RL closure and Collatz.

### Do not claim

- that Gate A is already proved;
- that proving Gate A alone automatically invokes radius 3;
- that the stable z-threshold covers all denominators;
- that RL or Collatz is solved;
- that the old half-period radius-3 bridge can be repaired by relabeling the same rotation.

## RL53 primary target: z=37

A direct event recursion for `(x<=1,y<=36)` is materially larger. Do **not** respond by merely increasing CPU time.

The one-x-zero terminal class has additional structure: with at most one x-zero, every predecessor word splits into at most two x-zero-free `11/10` segments separated by a single `00` or `01` event. Exploit this directly.

Recommended order:

1. Derive or implement a specialized exact solver for an x-zero-free `11/10` predecessor segment from a terminal 3-adic state and a y-zero budget.
2. Compose two such segment solvers around the unique possible x-zero event to obtain a sharp exact bound for `(1,36)`.
3. Validate the specialized solver against known cases, especially `(1,34)=85` and any x-zero-free inherited terminal bounds.
4. If `(1,36)` is bounded far below the astronomical required suffix, force the last two z=37 x-zero weights negligible.
5. Feed that negligible mass into the same scalar/defect bootstrap used for z=35.
6. Iterate: terminal-near late x-zeros -> smaller effective future scalar mass -> smaller delayed-y budget -> tighter terminal class.
7. Only after z=37 is either eliminated or a genuine obstruction is exposed should the session generalize the bootstrap parametrically in z.

A high-value secondary goal is to identify a monotone recurrence or uniform inequality showing that the bootstrap improves as z grows. A uniform terminal/defect theorem could convert the finite z-by-z eliminations into the desired full-phase impossibility result.

## Reproducibility

Start with the bundle checksum. Then run:

`bash rl51_research/run_rl51_latest_verifiers.sh`

and

`bash rl52_research/run_rl52_gatea_verifiers.sh`

Treat any failure as a stop-and-repair event.

For deeper provenance, the inherited RL50 verification tree remains in this bundle. Do not spend the new session rerunning every historical suite unless a frontier verifier or checksum fails, or a dependency must be independently audited.

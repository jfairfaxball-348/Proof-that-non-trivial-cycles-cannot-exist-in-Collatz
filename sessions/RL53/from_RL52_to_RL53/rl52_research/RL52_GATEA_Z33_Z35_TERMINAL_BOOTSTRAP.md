# RL52 — Gate A terminal bootstrap: z=33 and z=35 eliminated

Date: 2026-08-23

## Status

**Exact analytic + exact finite terminal certificates.**

This update continues the sole stable continued-fraction survivor attack.  It does **not** close Gate A globally, RL, or Collatz.

The inherited stable inputs are `Zx>143/12`, `E<5/3`, the sequential x-zero cap `w<17/30`, zero-displacement energy

`E = sum_j w_j [1-(2/3)^r_j]`,

and the terminal power condition `J_end=2^k` in the exact backward `Q_d=J+2^d-1` grammar.

## 1. Exact zero-event terminal automaton

The backward maps are

- `11: Q -> 2Q/3` when `3|Q`;
- `10: Q -> 2Q+1` (one y-zero);
- `00: Q -> 2Q-(3^d-1)` (one x-zero and one y-zero);
- `01: Q -> 2Q/3-3^(d-1)` when `d>1` and `3|Q` (one x-zero).

The height is redundant:

`d = 1 + (# y-zero edges used) - (# x-zero edges used)`.

At any state `Q!=0`, let `v=v3(Q)`.  Before the next zero-event, a predecessor word may contain exactly `r=0,...,v` backward `11` edges; an `01` event requires `r<v`.  If no more zero-event is used, the longest continuation is exactly the remaining `v` many `11` edges.  Since every zero-event consumes at least one of the finite zero budgets, this gives a finite recursion that enumerates every terminal predecessor suffix in the relaxed exact divisibility grammar.

The implementation carries `Q mod 3^P`; every dividing edge lowers available ternary precision by one.  A run is accepted as a certificate only if no state becomes `0 mod 3^P` at its current precision, so every `v3` decision encountered is exact.  This is a conservative terminal grammar because no positivity pruning is used.

The new verifier reproduces inherited terminal maxima:

- z=27, `(x<=0,y<=26)`: 56;
- z=29, `(x<=2,y<=6)`: 19;
- z=31, `(x<=4,y<=12)`: 38.

## 2. z=33 eliminated

RL51 already proved

- `p_26<=56`, hence `u_26<=81`;
- at most ten of `y_1,...,y_26` occur after `u_26`;
- therefore the suffix after `u_26` has at most six x-zero and sixteen y-zero edges.

The zero-event automaton proves the exact relaxed terminal maximum

`L_terminal(6,16)=54`.

But the genuine suffix has length at least

`ell-53 = 77692117359936589350`.

Hence `z=33` is impossible.

## 3. z=35 bootstrap

There are eight x-zero indices `27,...,34` after the first 26.

### Stage A — last two x-zeros are terminal-near

With all 34 y-zero edges allowed, the exact terminal maximum with at most one x-zero is

`L_terminal(1,34)=85`.

Thus the last two x-zero weights are each `<2^-1000` (a deliberately enormous safety margin, using `g_end<27/2^k`).

Discarding those two tiny weights in the scalar/defect inequalities reduces the effective non-negligible future to indices `27,...,32`.  Exact rational bounds give

- `p_26<=56`;
- at most ten of the first 26 y-zeros lie after `u_26`;
- the whole suffix therefore has `y-zero<=18`.

### Stage B — last four tiny

The terminal automaton gives

`L_terminal(3,18)=52`.

Hence the last four x-zero weights are tiny.  Now only indices `27,...,30` need be retained in scalar mass.  The exact bounds improve to

- `p_26<=53`;
- delayed first-26 y-zeros `<=8`;
- suffix `y-zero<=16`.

### Stage C — last six tiny

The terminal automaton gives

`L_terminal(5,16)=54`.

Thus the last six x-zero weights are tiny.  Retaining only indices `27,28` in future scalar mass gives

- `p_26<=49`;
- delayed first-26 y-zeros `<=6`;
- suffix `y-zero<=14`.

### Stage D — all eight tiny

The terminal automaton gives

`L_terminal(7,14)=51`.

Therefore all eight x-zero weights `27,...,34` are `<2^-1000`.  The first 26 x-zeros must now carry `Zx>143/12`.  The exact best non-greedy first-26 schedule has mass `11.798579...<143/12`, even after adding eight `2^-1000` errors.  Hence the first 26 schedule is uniquely the greedy one and

`u_26=70`.

If five of the first 26 matching y-zeros were after column 70, their minimum defect contribution is `>2.05>5/3`.  Thus at most four are delayed.  Together with the eight later y-zero indices, the suffix after `u_26` has budgets

`x-zero<=8, y-zero<=12`.

Finally

`L_terminal(8,12)=48`,

while the genuine suffix length is

`ell-40 = 77692117359936589363`.

Contradiction.  Therefore `z=35` is impossible.

## 4. Updated stable survivor

RL51 had eliminated `z=27,29,31`; this update eliminates `z=33,35`.  Since the inherited parity condition makes `z` odd,

`boxed: sole stable continued-fraction survivor has z>=37`.

## 5. What this does and does not close

Gate A is still open globally.  Gate B is also open: RL49 corrected the earlier direct radius-3 theorem match and proved the half-period rotation has cyclic transposition distance `2(a-t-3+H)`, not radius 3.

The strongest target remains a full-phase impossibility theorem; that would bypass the failed direct Gate-B shortcut.  The terminal-power/defect bootstrap is currently the most productive mechanism toward it.

## 6. Next target: z=37

A direct `(1,36)` terminal recursion is materially larger.  The next implementation should optimize the one-x-zero terminal class rather than simply increase CPU time.  With at most one x-zero, the word splits into two x-zero-free `11/10` predecessor segments; memoizing/solving that one-dimensional reverse grammar should give a much cheaper exact bound for the first bootstrap step.  Then repeat the scalar/defect feedback used at z=35.

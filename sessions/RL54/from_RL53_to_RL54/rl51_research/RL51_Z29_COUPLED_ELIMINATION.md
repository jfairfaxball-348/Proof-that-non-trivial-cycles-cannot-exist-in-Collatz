# RL51 — coupled elimination of z=29

Date: 2026-08-23

## Status

**ANALYTIC COUPLING + EXACT FINITE TERMINAL CERTIFICATES.**

For the sole stable continued-fraction survivor, `z=29` is impossible. Together with parity, this upgrades the survivor to `z>=31`.

This uses only the stable RL50/RL51 inputs: `Zx>143/12`, `E<5/3`, the sequential x-prefix cap `w<17/30`, the exact displacement identity

`E = sum_j w_j [1-(2/3)^(v_j-u_j)]`,

and the terminal state `J=2^k` with the exact backward `Q_d=J+2^d-1` grammar.

## 1. Last two x-zeros are terminal-negligible

At `z=29` there are 28 internal x-zeros and 28 internal y-zeros. An exact residue BFS from terminal `Q_1=2^k+1`, allowing at most one x-zero edge and all 28 y-zero edges, proves:

`maximum terminal suffix length with <=1 x-zero = 72`.

Therefore the last and second-last x-zero both lie in a fixed 73-column terminal window. Using `g_end<27/2^k`, either pre-zero weight is `<2^-1000` by a deliberately enormous margin.

## 2. First 26 x-zero schedule is forced

The exact best non-greedy 26-zero sequential-cap mass is

`11.798579834936... < 143/12`,

whereas the genuine survivor requires `Zx>143/12`. The two terminal weights contribute less than `2*2^-1000`, so the first 26 zeros cannot be non-greedy.

Hence their x-one counts are exactly

`[2,4,5,7,9,10,12,14,16,17,19,21,22,24,26,28,29,31,33,34,36,38,40,41,43,45]`,

and the 26th x-zero is at zero-based column

`u_26=70`.

## 3. Defect forces almost all matching y-zeros before the cut

If at least five of matching y-zero indices `22,...,26` occurred after column 70, their earliest possible positions would be `71,...,75`. Using the forced x-weights, their minimum defect contribution is

`2.059051471067... > 5/3`,

contradicting the stable survivor bound `E<5/3`.

Thus at most four of `y_1,...,y_26` lie after column 70. Since `v_27>=u_27>70` and `v_28>=u_28>70`, the suffix after column 70 contains at most six y-zero edges total and exactly two x-zero edges.

## 4. Reduced terminal suffix is impossible

A second exact backward residue BFS from `Q_1=2^k+1`, now allowing at most two x-zero edges and at most six y-zero edges, proves

`maximum such terminal suffix length = 19`.

But the internal word has length `ell+25`, so after `u_26=70` the required suffix length is

`ell-46 = 77692117359936589357`.

Contradiction.

Therefore `z=29` is impossible. Since the sole candidate has odd `q` and inherited parity forces even `t`, `z=q-t` is odd, hence

`z>=31`.

## Verification

Run:

`python3 rl51_research/verify_rl51_z29_coupled_twozero_elimination.py`

# RL51 extended progress and next attack

Date: 2026-08-23

## Executive status

Gate A remains open globally. RL and Collatz are not solved.

For the sole stable continued-fraction survivor, however, RL51 now proves:

- `z=27` impossible;
- `z=29` impossible;
- `z=31` impossible;
- parity therefore gives `z>=33`.

The z=29 and z=31 eliminations are exact coupled terminal-power results, not scalar-envelope improvements.

## New mechanism

The productive loop is now:

1. use `Zx>143/12` and the sequential x-prefix cap to bound an early x-zero cut (`p_26`, or force the first 26 schedule);
2. use `E=sum w_j[1-(2/3)^r_j] <5/3` to bound how many matching y-zeros can be delayed beyond that cut;
3. infer small `(x-zero,y-zero)` budgets for the remaining terminal suffix;
4. kill that suffix by exact backward arithmetic from `J_end=2^k`.

This closes z=29 and z=31.

## Exact current frontier: z=33

The same coupling proves:

- `p_26<=56`, hence `u_26<=81`;
- at most 10 of the first 26 matching y-zeros occur after `u_26`;
- therefore the suffix after `u_26` contains at most 6 x-zero edges and at most 16 y-zero edges;
- its required length is at least `ell-53`.

The remaining task is an exact terminal predecessor bound for the `(6,16)` budget class.

## Recommended next attack

Do not return to the old separable rank envelope. Build an accelerated terminal automaton in the exact `Q_d` coordinate:

- compress consecutive backward `11` steps using the current 3-adic valuation;
- treat `10`, `00`, `01` as zero-events;
- track `(xzero_count,yzero_count,height)` plus a compact exact 3-adic/affine state;
- exploit the z=33 cut constraints, and if useful carry a residual defect/mass budget to prune zero-event states;
- seek either extinction of the `(6,16)` class or a concrete extremal terminal word showing why that state is insufficient.

## Proof-state discipline

Stable theorem/certificate:

- sole survivor has `z>=33`.

Open:

- z=33 and higher odd z;
- Gate A `H>=t+3` globally;
- denominators outside the safe continued-fraction gate;
- global RL closure.

Do not state that RL or Collatz is solved.

# RL279 — scalable zero-rank state compression and canonical height-growth target

Date prepared: 2026-09-07
Status: PREPARED, NOT STARTED

## Incoming classification

RL278 closed as

`GLOBAL_SIX_ZERO_GATE_A_CONTRACTION_PROVED`

with subordinate

`FIXED_ZERO_EXACT_FINITE_REDUCTION_ENGINE_IDENTIFIED`.

Gate A remains

`H_can >= k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator now satisfies

`m0=z-k+2>=7`, equivalently `z>=k+5`.

## Exact inherited conclusions to preserve

1. The global zero-rank threshold is
   `S_m0=sum 2^(t-1)(2/3)^(u_t)>17/2`.
2. Four, five, and six internal zeros are exactly Gate-A safe.
3. RL278 gives a non-arbitrary fixed-level reduction engine based on exact sub-threshold gaps plus canonical all-one closure.
4. At the `5 -> 6` step the exact bound is `u6<=28`; exact replay leaves 458 legal six-zero prefixes and zero Gate-A violators.
5. The absolute ordered-rank moment budget from RL277 remains
   `413/16 < sum 2^eta_j < 61`.
6. Fixed-level finiteness alone is not yet a uniform Gate-A theorem; threshold gaps can shrink and family sizes can grow.

## Mission

Turn the fixed-zero engine into a scalable structural theorem.

Preferred order:

1. Derive an exact run-compressed transition law between successive zero events, using the deterministic all-`1` dynamics rather than expanding every column.
2. Track the corresponding exact increment of `H_can` across each compressed run/zero interruption.
3. Seek an invariant or amortized inequality forcing canonical height to grow with zero budget strongly enough that `m0>=7` eventually implies `H_can>=k` under the full-phase relation.
4. Use the existing exact finite families only to initialize or falsify the proposed invariant; do not make a flat seven-zero enumeration the main theorem.
5. If a uniform height-growth inequality fails, isolate the exact recurrent state pattern responsible and prove the strongest correct compressed alternative.

## Useful structural lead

For an all-`1` column from state `(d,J)`:

- if `J` is even and `d>1`, the next state has `d'=d-1` and `J'=J/2`;
- if `J` is odd, `d'=d` and `J'=(3J+2^d-1)/2`.

A productive normalization may therefore use

`K=J+2^d-1`,

for which an odd all-`1` step gives `K'=3K/2` at fixed `d`.

This lead is not yet promoted as a global invariant; derive and red-team it from the exact recurrence before use.

## Success criteria

Preferred:

- prove a uniform lower bound on `H_can` in terms of zero budget/run data that closes or sharply contracts Gate A;
- or prove a finite/run-compressed automaton theorem whose state space no longer grows combinatorially with fixed `m0`;
- or isolate a precise scalable obstruction showing why the RL278 induction cannot yield a uniform height theorem without an additional invariant.

A further fixed-budget contraction may be recorded as supporting evidence, but is not sufficient by itself as the main RL279 result.

## Forbidden repeats

Do not:

- restart flat zero-count enumeration as the principal programme;
- universalize Branch-C-only beta/counterflow conclusions;
- restart the selector conveyor belt;
- repackage the CRT/full-phase reconstruction;
- revive RL48 separable rank relaxation;
- use total variation as excursion without a new boundary theorem;
- start Radius 6+;
- merge Gate B into Gate A without a new proved coupling.

Gate B remains frozen unless an explicit new coupling is proved.

# RL278 closeout

Date: 2026-09-07

Classification:

`GLOBAL_SIX_ZERO_GATE_A_CONTRACTION_PROVED`

Subordinate:

`FIXED_ZERO_EXACT_FINITE_REDUCTION_ENGINE_IDENTIFIED`

## Promoted frontier

Starting from the RL277 global zero-rank threshold

`S_m0 = sum 2^(t-1)(2/3)^(u_t) > 17/2`,

RL278 proves an exact, non-arbitrary six-zero finite reduction.

The exact maximum five-zero weighted sum below the threshold is

`M5 = 501898/59049`

at `(1,1,1,2,10)`, so the exact gap is

`37/118098`.

If the first five zeros remain below threshold, that gap forces `u6<=28`. If the first five have already crossed threshold, the promoted RL277 family has maximum `u5=7` and at most 11 further all-one columns before terminal/stop, forcing `u6<=18`. Hence globally `u6<=28`.

Exact canonical replay then gives:

- 7,081 six-zero relaxed tuples;
- 458 legal canonical prefixes;
- 170 terminal closures;
- 47 full-phase scale-box terminals;
- zero terminals with `H_can<k`.

Therefore

`H_can<k => m0>=7 => z>=k+5`.

This strictly strengthens RL277's `z>=k+4` dangerous-region contraction.

## Reusable mechanism

RL278 identifies an exact fixed-zero level induction:

1. compute the exact sub-threshold maximum `M_n` by monotone upper-envelope pruning;
2. use the positive gap `17/2-M_n` to bound the next zero rank when the prefix has not crossed threshold;
3. use exact all-one closure of the already-crossed canonical family to bound the next zero rank in the complementary branch;
4. enumerate the resulting finite canonical family exactly.

This is reusable level-by-level, but is not yet a uniform Gate-A proof: the threshold gaps may shrink and family sizes may grow. A scalable state/run compression or direct height-growth theorem is still required.

## Scope

Gate A remains open with target `H_can>=k` at terminal `d=1,J=2^k`.

Gate B unchanged/open and frozen. Fifth selector not scanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## Verification

Portable verifier passes and independently certifies the exact gap, the rank bound `u6<=28`, all six-zero counts, the full phase-box replay, and zero Gate-A violators.

Successor RL279 should use the exact finite-reduction engine structurally rather than merely repeat a larger flat enumeration. Priority is a run/state compression or a direct lower bound coupling zero-rank interruptions to `H_can` strongly enough to scale with `k`.

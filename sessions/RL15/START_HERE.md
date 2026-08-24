# Collatz R-sharp RL15 handover — 2026-08-20

## Baseline
Start from `baseline/Collatz_Rsharp_RL14_Handover_2026-08-20.zip` for the full inherited project state.
The `rl15/` directory contains the new delta result.

## New closure in RL15
The complete coprime one-orbit same-direction

`j=1, P3, [1,1,1]`

strict-interior branch is now closed, including the genuinely scalene target left live by RL14.

The key new identity is obtained from the `j=1` defect

`C=2L-A=3h`:

`tau^h = 4/3 (mod D)`.

This gives a short binomial `3X^h-4`, with `h<B/4`.  Rotating the simplex to omit a largest gap gives a nonzero resultant divisible by `D` and a universal shape-free envelope

`|R_h| < 2^A exp(-0.31 B)`.

The inherited LMN two-logarithm theorem cuts the infinite tail at `L<42000`; an exact parameter-only certificate checks 19,161 coprime first-congruence pairs and leaves zero survivors.

## Strongest live targets
1. coefficient-5 `P3 [2,1]` boundary;
2. `j=2, P2` lift;
3. separate `gcd(A,L)=3` cubic-cofactor branch.

Highest priority: test whether the new short-defect binomial/resultant survives the `P3 [2,1]` boundary degeneration.  If its sparse boundary polynomial can be rotated so that its degree is at most `2B/3` (or another fixed fraction of `B`), the same LMN + exact-parameter architecture may close that branch quickly.

## Verification
Run:

`python rl15/verify_rl15_j1_p3_short_defect.py`

The included log records a successful run.

## Guardrail
RL remains open. Radius 3 is not yet completely closed.

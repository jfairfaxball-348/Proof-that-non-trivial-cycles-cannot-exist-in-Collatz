# RL323 red-team report

Date: 2026-09-14
Status: PASS FOR STATED RL323 SCOPE

## R1 — ordinary ownership

PASS.

`D_t` is defined from actual physical states in the two genuine ordered rows. The identities

`A_t+3^cB_t=D0(3^cU_t+V_t)`,
`3^cB_t-A_t=H D_t`

use numerators of actual length-`a` ordinary segments. RL323 does not relabel the RL320/RL322 affine factors as physical rows.

## R2 — geometry-only countermodel

PASS.

The decisive recurrence for `D_t` contains the ordinary `+1` forcing terms. The RL322 geometry-only countermodel does not supply these state equations, so RL323 does not contradict or bypass that barrier by renaming geometric quantities.

## R3 — cyclic-wrap scratch claim

PASS AFTER EXPLICIT DEMOTION.

The attempted odd-rank cyclic wrap was invalid and is withdrawn in `RL323_CORRECTION_AND_DEMOTION_LEDGER.md`. No promoted RL323 theorem depends on it.

## R4 — matched-rank ownership

PASS.

At the actual first transition into `D>0`, `u_t=1`, so `t=u_j`. Rankwise order plus the prefix-count difference identifies the actual early-row interval

`beta=v[v_j:u_j]`

with length `u_j-v_j` and weight `c_t`. This is the same kind of genuine matched-rank interval used by RL321, but it is extracted at the first `H`-carry crossing rather than at the global least root.

## R5 — common quotient at arbitrary recut

PASS.

The Euclidean transport step uses only a genuine positive ordinary tail `beta` beginning with `1`:

`z=2^rM+eta`, `0<eta<2^r`,
`2^rJ=3^h eta+B`,
`Q=3^hM+J`, `0<J<3^h`.

It does not import RL321's least-root-only bounded-carry estimate. Hence applying the common-quotient identity at the crossing recut is legitimate.

## R6 — strict `J<3^(h-1)` and `h>=2`

PASS.

The only possible first-crossing parity pairs are `(1,1)` and `(1,0)`. In both cases the one-step recurrence forces

`0<=Q-3^hP<3^(h-1)`.

The ordinary tail gives `Q-3^hP=J>0`, so the inequality is strict and `h=1` is impossible.

## R7 — bottom-third residual

PASS.

From

`2^rJ=3^h eta+B`,
`B>0`,
`J<3^(h-1)`

one obtains

`eta<2^r/3`.

No tail-only converse or saturation claim is made.

## R8 — external numerical bound

PASS IN EXTERNALLY CONDITIONAL SCOPE ONLY.

The lower bound

`q>=3182833230`

and hence

`r<=77265916075`

use the inherited external `m>=2^71` certificate and the exact first-survivor pair. The portable verifier replays the rational log enclosure and checks the boundary integer `q=3182833229` exactly.

The unconditional ordered-row theorem is only the zero-carry/bottom-third/narrow-window structure.

## R9 — no finite-certificate overclaim

PASS.

The absolute displacement bound is enormous. RL323 does not enumerate it, call it a complete finite certificate, or claim an existing obstruction covers every bounded case.

## R10 — parent-level scope

PASS.

RL323 proves a forced bounded extracted matched-rank interface, not yet a bound on the original least-root canonical interface and not yet an owned descent. Gate A, Gate B, global exclusion, and `g=1` remain open.

Verdict: promotion-safe with the stated correction and scope.

# RL305 scratch freeze

Date: 2026-09-12
Status: NOT PROMOTED EXCEPT WHERE REPEATED IN `RL305_PROOF_AND_SCOPE.md`

This file preserves useful frontier ideas that should not be reconstructed from conversation history.

## 1. Preferred normalized variables

For odd `D>=3`:

`X_L(D)=Bcal(L_D)-B_L(D)`,
`X_R(D)=Bcal(RW_D)-B_R(D)`,

where

`B_L(D)=(D^2+D-6)/2`,
`B_R(D)=(D^2+3D-4)/2`.

For the D0 departures:

`X_A(d)=Bcal(A_d)-C_A(d)`,
`X_F(d)=Bcal(F_d)-C_F(d)`,

where

`C_A(d)=d^2-2d-1`,
`C_F(d)=d^2-d-2`.

The scalar goal is `X<=3` on all these families plus `Bcal(8)<=3`.

## 2. Exact weighted rewrite formulas available immediately

From RL303 exact mergers and RL302 credits:

- `L_D -> RW_(D-2)` weight `k-D-4`;
- `L_D -> L_(D-2)` weight `k-2D-5`;
- `RW_D -> L_(D-2)` weight `k-3D-2`;
- `RW_D -> RW_(D-2)` weight `k-2D-8`;
- adjacent `L_D -> RW_D` run branch weight `D-k-1`.

These are branch inequalities, not a complete grammar.

## 3. High-value structural observation

The D-to-D-2 first weight is negative for `k<D+4`, while the adjacent-wall weight is negative for `k>D-1`.

There is substantial short/long-run overlap at the level of weights. This is a lead only: the two rewrites do not automatically cover the same branch partition, so no closure follows until RL306 proves a gap-free prefix/transducer cover.

## 4. Fixed-96/PQ reuse

RL304's fixed-96 and twelve-factor grammar should be imported only if it closes a residual state of the weighted quotient or supplies a negative normalized cycle/potential step.

Do not resume P/Q merely to derive a larger unweighted residual grammar.

## 5. Candidate max-plus certificate form

A successful finite quotient could be certified by a potential `phi(state)` satisfying

`weight(edge)+phi(next)-phi(state) <= 0`

on every covered edge, with strict negativity on every nontrivial directed cycle after exact zero-renewal quotienting, and sink values already bounded by 3.

Equivalent negative-cycle / longest-path formulations are acceptable.

## 6. Early failure test

Freeze/pivot if:

- an exact legally repeatable positive-weight cycle remains;
- a zero/positive cycle cannot be quotiented as an exact renewal;
- a new unbounded integer parameter appears with no monotone credit;
- complete coverage forces the quotient back to unrestricted checkpoint futures.

## 7. Parallel fallback

If the scalar wall quotient fails, return to:

- RL292 static boundary danger tree;
- RL293 merger-invariant minimum-area balls and principal-representative theorem;
- RL289 fixed-seed ballot/rejected-tube geometry;

but target only the seven exact scalar ceilings, not stronger universal ownership.

# RL307 — checkpoint-8 shell-owner / affine-ballot Gate-A target

Date prepared: 2026-09-12
Status: PREPARED, NOT STARTED

## Incoming classification

RL306 closes as

`SCALAR_WALL_HARD_PIVOT_AND_AFFINE_SHELL_OWNER_REDUCTION_PROVED`.

Gate A remains open. The fixed-96 P/Q continuation is frozen after satisfying RL306's hard-pivot criterion. The principal live route is fixed-source ancestry expressed through divisibility shells and arbitrary-source affine ballot trees.

## Absolute objective

Prove or falsify the checkpoint-8 shell-owner theorem

`M_seed(k)=3+M_8(k)`

for every relevant `k>=2`, or prove the weaker dangerous-region form sufficient for Gate A.

Here

`M_s(k)=min { added area from source s to a positive even checkpoint E : 2^k divides E }`.

The inequality

`M_seed(k)<=3+M_8(k)`

is immediate from the genuine fixed-seed-to-8 history of height three. The hard direction is

`M_seed(k)>=3+M_8(k)`.

## Exact inherited reduction

For `k>=2`, RL306 combines RL302 and RL292 into

`M_seed(k)=3+min(`
` M_R3(k), M_8(k), M_D0(k), M_(4,39)(k),`
` M_(2,-17)(k)-2, M_(2,-84)(k)-1, M_(3,-28)(k))`.

Therefore it is sufficient to prove that checkpoint 8 is pointwise no more expensive than the other six shifted shell functions.

This is strictly weaker than same-endpoint ownership, O1, O2, or the universal P/8 identity.

If shell ownership is proved, Gate A reduces exactly to

`M_8(k)>=k-3` for all `k`,

equivalently

`Bcal(8)<=3`.

## Primary affine formulation

For canonical source `S=(d,K)`, use

`g_S(u)=3^d(u+1)-K-1`.

Finite canonical futures are exactly ballot-positive paired ordinary half-step Collatz trajectories of `u` and `g_S(u)`.

For the fixed seed and checkpoint 8:

`g_seed(u)=3u+14`,
`g_8(u)=3u-7`,

so

`g_seed(u)=g_8(u+7)`.

Thus a seed witness and a candidate checkpoint-8 owner can share the same right ordinary Collatz trajectory. The shell-owner theorem should be attacked as an exchange between the left trajectories `u` and `u+7`, with area measured by the ballot depth path.

## Preferred success criteria

A theorem-sized success is one of:

1. an explicit area-nonincreasing exchange sending every dangerous seed shell witness to a checkpoint-8 shell witness of the same or greater 2-adic precision;
2. a min-plus shell potential proving `M_seed(k)>=3+M_8(k)`;
3. sourcewise proofs of the six shifted shell-owner inequalities;
4. a strict dangerous-region contraction with a proved decreasing parameter;
5. an exact counterexample to shell ownership, together with the smallest replacement target implied by it.

The theorem may be restricted to the dangerous region if that is enough for Gate A; do not prove a stronger universal statement without need.

## Checkpoint-8 residual after shell ownership

The literal theorem required afterward is

`M_8(k)>=k-3`.

Exact RL306 finite certificates cover `k<=28`. The next unresolved shell is `k=29`, but **do not** make sequential cost-cap extension the principal route.

The stronger historical excess-one pattern remains conjectural and is not required.

## Useful inherited exact structure

- checkpoint 8 has affine section `3u-7` and a forced free first `01` paired column to `(2,15)`;
- balanced source-8 futures satisfy
  `2^N J=7*3^r+3Q_x-Q_y+2^N`;
- first even returns from 8 are analytically safe for the `+3` scalar ceiling;
- dangerous odd first-return branches are forced onto principal parity-cylinder representatives;
- cascade sections satisfy `g_(A o B)=g_B o g_A`;
- the seven RL305 sources have the explicit affine atlas frozen in RL306.

## Prohibited substitutions

Do not make the default route:

- fixed-96 P/Q continuation;
- another unweighted commutation grammar;
- same-endpoint universal ownership;
- O1/O2/P8 merely because they are historically familiar;
- generic height-cap expansion;
- per-Ferrers-cell valuation Lipschitz induction;
- a local endpoint-only or finite shifted-valuation potential;
- a coordinate change without a min-plus/decreasing theorem.

## Falsification discipline

Actively search for a shell where one of the six shifted competitors beats checkpoint 8. If found, freeze the exact witness and revise the shell-owner target rather than forcing the conjecture.

Finite enumeration is permitted as a falsification/equality-discovery tool but is not an all-depth proof.

## Scope

Gate A OPEN.
Gate B OPEN/frozen.
`Bcal(8)<=3` OPEN.
`Bcal(P)<=1` OPEN.
Checkpoint-8 excess-one OPEN.
O1/O2/P8 OPEN.
Fixed-96 P/Q frozen.
Physical/resonance frozen at `a=7354673373747273032`.
Radius 6+ frozen.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.

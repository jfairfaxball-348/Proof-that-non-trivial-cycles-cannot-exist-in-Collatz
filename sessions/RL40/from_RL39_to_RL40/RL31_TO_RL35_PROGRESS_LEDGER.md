# RL31-RL35 progress ledger

Date: 2026-08-21

## RL31 — exceptional balanced-prefix envelope

Scope: exact exceptional three-way-balanced `(G,H)=(12,4)` branch.

Result:

`R log(lambda)/L < 0.2475897011175711`

and, under inherited `R>=2^71`,

`L/gcd(A,L) >= 57,490,527,167`.

Mechanism: cap every balanced prefix scale `q_j=2^j/3^p(j)` and dominate by an exact 300-step greedy envelope. This was local to the exceptional branch.

Verifier: `rl31_to_rl35_additions/verify_rl31_balanced_prefix_envelope.py`.

## RL32 — repaired global high-run support

Scope: global.

Result:

`limsup R log(lambda)/L <= 0.24755857969692248...`

and CF floor

`57,494,140,717`.

Mechanism: use the actual high-run valuation inequality, not the earlier coarse density surrogate; replace an unattainable support anchor by dynamically attainable type-II direct-return anchors.

Verifier: `verify_rl32_refined_highrun_support.py`.

## RL33 — induced successor coupling

Scope: global support refinement.

Result:

coefficient `0.24669513589536314...`, CF floor `57,594,668,838`.

Key structural fact: direct type-II `k=3,h=1` is forced into next low-chain length `k=2`; it cannot be optimized as an independent item.

Verifier: `verify_rl33_induced_block_support.py`.

## RL34 — type-II continuation / induced superblock

Scope: global.

Result:

coefficient `0.24629753781691484...`, CF floor `57,641,137,625`.

Mechanism: exact induced superblock for the forced exceptional `k=3 -> k=2` pair. The two remaining zero-slack anchor items are

- `T`: `(n,V)=(5,8)`, map `G_T(x)=(243x+319)/256`;
- `S`: `(n,V)=(12,19)`, map `G_S(x)=(531441x+1568693)/524288`.

Coverage repair: the `h == 1 (mod 12)` continuation requires an explicit `h=13` base because the `h=1` exceptional block is paired rather than supported individually.

Verifier: `verify_rl34_typeII_continuation_support.py`.

## RL35 — anchor-run charging

Scope: global; analytic for `R>=10000`.

Result:

`lambda Q^L <= T^(12A-19L) S^(8L-5A)`,

where `Q=1+1/(2000R)`.

Thus

`limsup R log(lambda)/L <= 0.245797537816914843649...`

and under inherited `R>=2^71`,

`L/gcd(A,L) >= 57,699,734,483`.

Mechanism:

- nonanchor items carry enough strict support slack to reserve charge for themselves and up to two neighboring anchors;
- exact admissible anchor words of lengths 3, 4, and 5 pay their own `Q` factor through the induced affine low-state dynamics;
- pure 1- or 2-anchor cycles are excluded by affine fixed-point analysis.

This is the first post-RL30 theorem here that extracts a fixed global gain from successor dynamics rather than only changing a local support line.

Verifier: `verify_rl35_anchor_run_charging.py`.

## Current obstruction

The new denominator floor remains below the next relevant CF denominator `65,470,613,321`. Therefore the quantitative improvement alone does not remove a major branch from the RL30 audit DAG.

The next session should try to turn the **method**, rather than the constant, into a branch-closing resource.

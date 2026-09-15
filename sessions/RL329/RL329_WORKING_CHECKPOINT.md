# RL329 working checkpoint — first global ownership attack on the >=3-positive barrier

Date: 2026-09-15
Status: ACTIVE SESSION / NOT PROMOTED
Incoming authoritative HEAD: `828db8a17863a676e35df61168741e31fd721c63`
Working branch: `rl329-global-structure`

## Incoming target

RL328 proved a method barrier for the unchanged RL327 conservative graph: because every positive run of length at least three was admitted without ownership filtering, the graph contained a repeatable `N(49)->N(49)` edge with `Z=49`, `K=3`, forcing any fixed-boundary density coefficient on that graph to be at least `49/3`.

RL329 is required to attack the >=3-positive obstruction or replace the consumer; shorter-singleton enumeration is not the default programme.

## New exact diagnostic: all owned three-positive bridges

The scratch verifier `scratch/verify_rl329_three_positive_ownership.py` applies the same exact physical reconstruction discipline used by RL327, now to every positive q-run of length exactly three.

For

`q_0=q_4=0`, `q_1,q_2,q_3>0`,

physical gaps can decrease by at most one at a step. The complete three-positive excursion shapes are therefore

- `(1,1,1)`;
- `(1,2,1)`;
- `(2,1,1)`;
- `(2,2,1)`;
- `(3,2,1)`.

The verifier exhausts:

- every adjacent zero-run pair with total 47 through 98;
- every rational-mechanical factor of the required length;
- the exact gap perturbation induced by each of the five q-shapes;
- every odd endpoint lift in the inherited band `2^71 <= P < 2^76+2^36`;
- the inherited high-carry least-state ownership filter `n>=20390252058`.

The exact retained multiplicities are

`47:288, 48:104, 49:44, 50:20, 51:5, 52:2`,

and **zero for every total 53 through 98**.

Hence every physically reconstructed high-carry three-positive bridge has adjacent zero total at most 52.

In particular the RL328 conservative `N(49)->N(49)` three-positive edge has **no physical high-carry realization**.

Classification: **exact active-session finite certificate / not yet authoritative promotion**.

## Exact linkage inside the three-positive layer

Indexing consecutive bridges by equality of the first state on their shared zero plateau leaves exactly two physical links, both represented by the single pair-type link

`(2,45) -> (45,2)`.

There is no repeatable `(49,49)` physical link and no all-large self-cycle in this exact three-positive layer.

Classification: **exact active-session ownership diagnostic / not yet independently red-teamed**.

## Supporting longer-run scratch

Using the same reconstruction code locally during RL329, the exact high-carry survivor counts were also extended through positive-run lengths 4, 5, and 6:

- `p=4`: totals `{47:189, 48:59, 49:12, 50:3, 51:1}`; no same-layer large-bridge link;
- `p=5`: totals `{47:118, 48:44, 49:18, 50:9, 51:6, 52:2, 53:1}`; no same-layer large-bridge link;
- `p=6`: totals `{47:108, 48:34, 49:9, 50:2}`; no same-layer large-bridge link.

Across the exact `p=3..6` layers there are only two large-bridge physical links total, both the `p=3` links above.

These p=4..6 figures are preserved here as **supporting scratch only**. They are not load-bearing until a portable checker and independent red team are frozen.

## Structural algebra exposed by the computation

Let `b_i` be the baseline rational-mechanical gaps on a zero-to-zero excursion and let

`g_i=b_i+q_i-q_(i-1)`, `q_0=q_L=0`.

For the backward affine constant used by the forced-residue reconstruction,

`C(g)=sum_{j=1}^L 3^(j-1) 2^(g_(j+1)+...+g_L)`.

The telescoping gap perturbation gives the exact identity

`C(g)=sum_{j=1}^L 3^(j-1) 2^(b_(j+1)+...+b_L) 2^(-q_j)`.

Thus every nontrivial positive excursion strictly lowers the affine constant relative to its mechanical baseline while keeping the total exponent unchanged. This is a candidate analytic route to a monotone owned-state drift / descent theorem and may explain why the conservative >=3-positive edges disappear after physical reconstruction.

Classification: **working analytic lemma; indexing and global-use scope still require red-team audit before promotion**.

## Strategic consequence

RL328's `49/3` obstruction was a valid barrier for the **unchanged conservative graph**, but the exact p=3 reconstruction shows that its particular repeatable cycle is not a physical high-carry trajectory. This reopens long-positive-run ownership as a viable route exactly as RL329 requested.

This does **not** close R1. It also does not yet prove a uniform theorem for arbitrary positive-run length. The existing linear consumer still cannot be declared sufficient from the finite p=3..6 evidence alone.

## Next attack

Do not return to shorter-singleton enumeration as the main programme.

Primary next step: turn the affine-constant identity into an all-length zero-to-zero excursion theorem. Seek one of:

1. a uniform ownership bound on adjacent zero total for every positive-run length;
2. a strict monotone drift of the owned plateau state that forbids repeatable large bridges;
3. a genuinely smaller owned return produced when the drift crosses the least-state boundary.

If the all-length theorem fails, isolate the first positive-run length admitting a genuine repeatable high-carry large bridge and feed its exact geometry—not the old unrestricted graph—into the consumer analysis.

R1 OPEN. Gate A OPEN. Gate B OPEN. `g=1` separate. Global positive non-trivial-cycle exclusion OPEN.

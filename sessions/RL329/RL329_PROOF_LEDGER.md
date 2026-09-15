# RL329 proof ledger — owned singleton successors and support-uniform density contraction

Date: 2026-09-15
Status: FROZEN WITH RL329 CLOSEOUT
Incoming authoritative HEAD: `828db8a17863a676e35df61168741e31fd721c63`
Working branch: `rl329-global-structure`

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch at

`(a,ell)=(217976794617,137528045312)`, `d=80448749305`, `lambda=2^a/3^ell<1+2^-40`,

with authoritative incoming carry cap

`1<=n<=32596612662`

and inherited high-carry ownership architecture. RL324's local-propagation barrier remains binding. Gate A, Gate B, R1, and global positive non-trivial-cycle exclusion remain open.

RL328 proved that the unchanged RL327 conservative graph has a repeatable unrestricted `>=3`-positive `N(49)->N(49)` cycle, so shorter-singleton density alone cannot close R1 on that graph. RL329 therefore attacks missing physical ownership rather than merely changing the linear consumer.

## RL329.1 — exact total-45 singleton ownership at the self-consistent threshold

Assume for contradiction

`n>=32562630354`.

Using the same exact rational-mechanical reconstruction discipline as RL327, exhaust every singleton excursion `0,1,0` whose adjacent zero total is 45 through 98, every rational-mechanical factor, every odd endpoint lift in

`2^71 <= P < 2^76+2^36`,

and retain only realizations compatible with the displayed carry threshold and global least-state ownership.

The exact surviving multiplicities are

`45:4755, 46:1633, 47:556, 48:173, 49:46, 50:14, 51:6`,

and zero above 51. They occupy 231 ordered pair types.

Classification: **exact gap-free finite ownership certificate at the self-consistent RL329 threshold**.

## RL329.2 — exact large-to-large shared-state linkage

Consecutive owned singleton bridges are linked only when the first physical state on their shared zero plateau is equal. Determinism then fixes the shared plateau.

Across all 7,183 surviving singleton realizations, exactly 14 physical large-to-large links remain, represented by 13 conservative pair-type links.

Classification: **exact physical shared-state ownership theorem over the retained layer**.

## RL329.3 — exact owned-large -> short-singleton successor theorem

The earlier density graphs forgot physical identity whenever a singleton bridge had adjacent zero total below the retained threshold. RL329 restores that identity on every transition leaving an owned large bridge.

For each owned large realization, let the first state on its right zero plateau be the exact physical successor endpoint. For every candidate following short singleton pair `(right_zero,next_zero)` with total at most 44, solve its exact forced residue and reconstruct it from that same physical endpoint. Retain the graph transition only if at least one owned realization physically supports the successor.

Across all 231 large pair types there are exactly

`286`

permitted conservative pair-type transitions from an owned large bridge to a short singleton.

This rejects, among many others, the transitions making the previous limiting singleton cycles, including `(45,4)->(4,39)`.

Classification: **exact physical successor-ownership theorem; no unowned pair-type reset after a large singleton is permitted**.

## RL329.4 — two-positive layer retained exactly

At the same threshold the complete two-positive certificate has multiplicities

`45:2029, 46:707, 47:270, 48:93, 49:34, 50:11, 51:2`,

and no survivor above total 51.

Classification: **exact finite certificate, reconstructed at the RL329 threshold**.

## RL329.5 — conservative automaton and density theorem

Build an automaton with states

- `N(z)`, `1<=z<=49`, after a short singleton or any positive run of length at least two;
- `L(a,b)` for each of the 231 retained owned singleton pair types.

Transitions are:

1. short singleton transitions of total at most 44 from `N` states;
2. short singleton transitions from `L` states only when certified by RL329.3;
3. retained large singleton transitions, with exact RL329.2 linkage for `L->L`;
4. every two-positive transition of adjacent zero total at most 51;
5. **every positive run of length at least three without restriction**.

Thus the graph remains a conservative superset of every physical high-carry word and does not use the p=3 scratch diagnostic.

It has 280 states and 22,991 edges. An integer potential checked on every edge proves

`Z <= 22 K + 66`.

The coefficient 22 is sharp for this conservative graph: the unrestricted short-singleton layer still contains the total-44 loops `N(22)->N(22)` and `N(21)<->N(23)`.

Classification: **proved finite-state support-uniform density theorem backed by exact physical successor ownership**.

## RL329.6 — residue-weighted telescope and self-consistent carry contraction

At `rho=60`, with `T=ell-rho`, the density theorem gives

`K>=5979480226`.

Apply the inherited RL327 residue-weighted telescope consumer with the same exact quartic rational enclosure. The portable verifier proves

`n < 32562630353.14829...`.

Hence under the bootstrap assumption `n>=32562630354` there is a contradiction, and therefore

`n<=32562630353`.

The inherited `rho<=59` inequality lies far below this threshold. For `rho>=60`, the RL327 monotonicity argument still applies because the rounded density floor changes by at most one while each newly omitted ideal term removes more than the largest possible restored one-rank loss.

Thus the contraction covers every live `rho`.

This improves the authoritative RL327 cap by

`33982309`.

Classification: **proved self-consistent carry contraction from exact owned-successor structure plus the inherited exact residue-weighted telescope**.

## RL329.7 — p=3 and constant-height diagnostics remain subordinate

RL329 also found that the specific RL328 unrestricted `N(49)->N(49)` p=3 edge has no high-carry physical realization and developed exact constant-height plateau diagnostics. These remain useful strategic evidence, but the promoted density contraction above does not depend on them.

## Binding barrier / next obstruction

The current graph's coefficient 22 is sharp because total-44 short-singleton transitions from `N` states are still admitted without physical state identity. Therefore repeating the same large-bridge successor refinement cannot improve the asymptotic coefficient below 22.

The next theorem must attack one of:

1. exact ownership/linkage of consecutive total-44 short singleton bridges;
2. a monotone physical-state drift across the short-singleton layer;
3. an all-length zero-to-zero excursion theorem subsuming both short and long positive runs;
4. a nonlinear consumer strong enough to exploit the retained height structure.

Do not revert to total-43, total-42 singleton enumeration as a blind threshold programme. The remaining obstruction is specifically the unowned `N->N` total-44 reset.

## Verification

Portable verifier:

`verification/verify_rl329_owned_successor_density.py`

Independent structural red team:

`verification/red_team_rl329_owned_successor_density.py`

Both are green. The red team independently reconstructs the singleton and two-positive layers, shared-state links, large-to-short successor relation, every graph inequality, sharp total-44 cycles, and the final carry cap.

## Final scope

R1 Parent Bridge: OPEN.
Gate A: OPEN.
Gate B: OPEN.
`g=1`: separate.
Global positive non-trivial-cycle exclusion: OPEN.

`PARENT_DIFFICULTY_DELTA = EASIER`

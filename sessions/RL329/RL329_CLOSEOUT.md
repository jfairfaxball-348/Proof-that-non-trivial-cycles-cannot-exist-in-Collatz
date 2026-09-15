# RL329 closeout — owned-successor density contraction and total-44 frontier

Date: 2026-09-15
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `828db8a17863a676e35df61168741e31fd721c63`
Working branch: `rl329-global-structure`
Successor: RL330

## Executive conclusion

RL329 does not close R1, Gate A, Gate B, the full `g=2` branch, or global positive non-trivial-cycle exclusion.

It does, however, produce a new theorem-grade support-uniform density contraction by restoring exact physical successor ownership where the RL327/RL328 conservative bridge graph had previously forgotten state identity.

At the self-consistent high-carry threshold `n>=32562630354`, the exact singleton reconstruction through adjacent zero total 45--98 leaves 7,183 owned realizations in 231 ordered pair types. Exact shared-plateau linkage leaves 14 physical large-to-large links / 13 conservative pair-type links, and exact reconstruction from each owned large bridge permits only 286 large-to-short singleton pair transitions.

Together with the exact two-positive layer and conservative admission of every run of length at least three, the resulting 280-state / 22,991-edge automaton has an integer potential proving

`Z <= 22 K + 66`.

At `rho=60` this forces

`K>=5979480226`.

Feeding that density into the inherited residue-weighted telescope gives

`n < 32562630353.14829...`,

so the bootstrap assumption contradicts itself and the authoritative carry cap contracts to

`n<=32562630353`.

This improves the incoming cap by exactly

`33982309`.

`PARENT_DIFFICULTY_DELTA = EASIER`.

## Verification

Portable verifier:

`verification/verify_rl329_owned_successor_density.py`

Independent structural red team:

`verification/red_team_rl329_owned_successor_density.py`

Frozen outputs begin with

`RL329_OWNED_SUCCESSOR_DENSITY_VERIFIER_GREEN`

and

`RL329_OWNED_SUCCESSOR_RED_TEAM_GREEN`.

The red team independently reconstructs the singleton and two-positive layers, shared-state links, large-to-short successor relation, every potential inequality, the sharp limiting total-44 cycles, and the final carry cap.

## Exact new obstruction

The coefficient 22 is sharp for the promoted conservative graph because the short-singleton `N->N` layer still forgets physical identity at adjacent zero total 44. In particular the graph admits the total-44 loops

`N(22)->N(22)`

and

`N(21)<->N(23)`.

Therefore merely repeating the same large-bridge successor refinement at lower thresholds cannot improve the asymptotic coefficient below 22. The next session must attack this total-44 physical-reset obstruction or replace the consumer.

## Preserved subordinate diagnostics

RL329 also preserves, but does not use in the promoted contraction:

1. an exact p=3 ownership certificate showing that the specific RL328 unrestricted `N(49)->N(49)` three-positive edge has no high-carry physical realization;
2. exact constant-height plateau certificates, including `q=0` plateau length at most 49 and `q=1` plateau length at most 51 in the certified high-carry regime;
3. supporting p=4..6 finite reconstruction scratch;
4. the working affine-constant identity

   `C(g)=sum_j 3^(j-1) 2^(b_(j+1)+...+b_L) 2^(-q_j)`,

   showing every nontrivial positive excursion lowers the backward affine constant relative to its mechanical baseline at fixed total exponent;
5. the finite-run enumeration barrier: if all run lengths through `P` are controlled but every run of length at least `P+1` is conservatively admitted, the fallback graph still contains a repeatable `N(49)->N(49)` cycle with asymptotic ratio `49/(P+1)`. Thus run-by-run enumeration is not a viable main closure programme.

Items 1--4 remain subordinate diagnostics / working mathematics unless separately promoted later. Item 5 is a proved method barrier.

## Binding inherited barriers

RL324's local-propagation counterfamily remains binding. No rank-by-rank displacement propagation theorem is restored.

Do not use the root-aligned `G<2^35` theorem in the live late-row-root branch.

The external `2^71` least-state floor remains conditional. Internal-only frontier remains `ell>=190537`; external-certificate-conditional frontier remains `ell>=49547666544`.

## Final state

R1 Parent Bridge: OPEN.
Gate A: OPEN.
Gate B: OPEN.
`g=1`: separate.
Global positive non-trivial-cycle exclusion: OPEN.

The authoritative carry cap entering RL330 is

`1<=n<=32562630353`.

RL329 is closed and frozen. RL330 must not begin without a new kickoff instruction.
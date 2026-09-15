# RL329 closeout — owned-successor density contraction and total-44 frontier

Date: 2026-09-15
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `828db8a17863a676e35df61168741e31fd721c63`
Successor: RL330

## Executive conclusion

RL329 does not close R1, Gate A, Gate B, the full `g=2` branch, or global positive non-trivial-cycle exclusion.

It produces a theorem-grade support-uniform density contraction by restoring exact physical successor ownership where the RL327/RL328 conservative bridge graph had forgotten state identity.

At the self-consistent threshold `n>=32562630354`, exact singleton reconstruction over adjacent zero totals 45--98 leaves 7,183 owned realizations in 231 ordered pair types. Exact shared-plateau linkage leaves 14 physical large-to-large links / 13 pair-type links. Exact reconstruction from each owned large bridge permits only 286 conservative large-to-short singleton pair transitions.

Together with the exact two-positive layer and conservative admission of every run of length at least three, the resulting 280-state / 22,991-edge automaton proves

`Z <= 22 K + 66`.

At `rho=60` this forces `K>=5979480226`. The inherited residue-weighted telescope then gives

`n < 32562630353.14829...`,

hence

`n<=32562630353`.

This improves the incoming cap by exactly `33982309`.

`PARENT_DIFFICULTY_DELTA = EASIER`.

## Verification

`verification/verify_rl329_owned_successor_density.py`

`verification/red_team_rl329_owned_successor_density.py`

Both frozen outputs are GREEN. The independent red team reconstructs the singleton and two-positive layers, shared-state links, large-to-short successor relation, every potential inequality, the sharp total-44 cycles, and the final carry cap.

## Exact next obstruction

The coefficient 22 is sharp for the promoted conservative graph because the short-singleton `N->N` layer still forgets physical identity at adjacent zero total 44. In particular it admits `N(22)->N(22)` and `N(21)<->N(23)`.

RL330 must attack this physical-reset obstruction or replace the consumer. Blindly continuing total-43, total-42, ... singleton threshold enumeration is not the default programme.

## Preserved subordinate work

RL329 also freezes the exact p=3 ownership diagnostic, constant-height plateau diagnostics, p=4..6 reconstruction scratch, and the affine-constant positive-excursion identity. These are legitimate possible ingredients but are not load-bearing for the promoted carry contraction.

The finite-run enumeration barrier is promoted as a method barrier: controlling only finitely many positive-run lengths while admitting all longer runs conservatively cannot be the main closure architecture.

## Scope

RL324 local propagation remains barred. Root-aligned `G<2^35` is not valid in the live late-row-root branch. External `2^71` least-state floor remains conditional.

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.

R1 Parent Bridge OPEN. Gate A OPEN. Gate B OPEN. `g=1` separate. Global positive non-trivial-cycle exclusion OPEN.

RL329 is closed and frozen. RL330 is prepared but not started.
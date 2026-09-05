# RL250 closeout report

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**.

## Result

RL250 materially contracts the live Branch-C `beta(P)=6` obstruction without invoking Radius 4.

The strongest promoted result is

`boxed: z=a-ell>=289`.

The proof combines exact beta=6 profile topology and q-shift variation; q-orbit binary integrability; an exact lift from `(P,q)` support data back to `P_i=r-W_i(q)` and `ar-qell=2`; the canonical terminal identity `t=k-3>=28`; a new exact cyclic terminal-window cover/packing lemma; and an exact resonance/determinant certificate excluding every branch with `z<289`.

The first arithmetic scale not eliminated by this lemma is uniquely

`(a,ell,z,q,r)=(783,494,289,317,200)`

and its terminal selector satisfies

`31<=k<=59`.

## Integrity / scope

RL249's historical/current-q demotion and flawed q-ordered covering demotion remain binding. The RL250 cover/packing lemma is independently proved and verified and does not use either demoted statement.

Gate A: open.
Gate B: open.
Radius 4: not invoked.
Radius 5: inactive.
Branch C beta=6: still live at the first frontier above.

## Verification

Canonical ZIP SHA256:
`17090bacbab6f08361adcd85d7bedaebf689d6f1a3aa94e6bb8dbe7abdb8345b`.

Portable verifier `verification/verify_rl250_terminal_window_covering.py` inside the canonical bundle passes with:

- `profile_topology_classes=19`
- `small_integrability_instances=1324`
- `resonance_triples_z_lt_289=18`
- `determinant_branches_z_lt_289=20`
- `terminal_window_killed_branches=20`
- `first_unexcluded=(a,ell,z,q,r)=(783,494,289,317,200)`
- `first_unexcluded_k_range=31..59`

Fresh-unpack verification and internal SHA256 manifest: PASS.

## Frozen return line

If the successor Gabriel's-horn exploration is closed as blocked/equivalent/unfruitful, resume exactly here:

**RETURN TARGET:** Resume the beta=6 Branch-C attack after the RL250 Terminal-Window Covering checkpoint: `z=a-ell>=289`; first arithmetic scale not excluded by the lemma is `(a,ell,z,q,r)=(783,494,289,317,200)` with `31<=k<=59`; continue the exact iterated zero-run / deterministic canonical event-versus-rigid terminal-ownership attack. Gate A/B remain open; Radius 4 has not been invoked.

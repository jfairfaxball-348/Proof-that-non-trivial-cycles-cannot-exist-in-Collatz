# START HERE — RL27 -> RL28 handover

Date: 2026-08-21

## One-line state

**RL remains open.** Radius 3 should not be reopened absent a verifier/dependency failure. The order-3/global bridge has been narrowed to one exceptional balanced geometry, and RL27 repaired the full cubic spread and exposed a new adjacent-block synchronization target.

## Mandatory first actions

1. Read `RL27_PROOF_STATUS_AND_NEXT_ATTACK.md`.
2. Read `rl27_additions/RL27_FULL_SPREAD_REPAIR_AND_ADJACENT_BLOCK_OWNERSHIP.md`.
3. Read `RL27_METHOD_EVIDENCE_AND_NOGO.md` so that the two recently tested dead-end strategies are not repeated as if new.
4. Run all inherited verifiers in `inherited_rl26/continuation/verify_*.py` and then run `rl27_additions/verify_rl27_full_spread_adjacent_ownership.py`.
5. Treat any verifier failure as stop-and-repair.
6. Only then begin the RL28 attack in `NEXT_SESSION_KICKOFF_PROMPT.md`.

The release used 20 verifiers total and all passed. See `RL27_RELEASE_VERIFIER_RUN.txt`.

## Primary frontier

Under the inherited weak-close hypotheses the unique surviving cubic geometry is

`R == 91 (mod 288),  G=12, H=4`,

with three balanced block prefixes

`11011 / 11101 / 11111`.

The next theorem target is a **first synchronized sign-reversal / numerator-difference lemma** coupling the three adjacent macroblocks. The goal is to turn the forced endpoint permutation into a scaling obstruction, not merely another finite residue exclusion.

## Important repair

RL25/RL26 defined

`Delta=max(|U-V|,|V-W|,|W-U|)`

but their lattice verifier optimized only the two differences relative to `W`. RL27 restores the omitted `U-V` difference. At the surviving `(G,H)=(12,4)` geometry the exact spread is

`Delta = 4(2B+3Y)`,

not `4(3B+Y)`.

The old lower bounds remain conservative; the sharpness wording was wrong.

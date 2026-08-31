# START HERE — authoritative RL199 handover

Current handover: **RL199 — H21 Oriented Lift Index, Minimal Prehistory, and Terminal Defect**.  
Incoming job: **RL200**.

RL199 parameterizes every surviving H21 `tau=34` co-owner by one positive oriented lift `eta`:

`Y_0^-=2^34 eta-1`,
`Y_0^+=2^34(eta+21)-1`.

The two RL198 state choices and the terminal sign are exactly the four necessary classes

`eta=0,8,9,17 (mod 18)`:

- 0: `011`, lower endpoint reaches height 21, positive terminal defect;
- 8: `111`, lower endpoint reaches height 21, positive terminal defect;
- 9: `011`, upper endpoint reaches height 21, negative terminal defect;
- 17: `111`, upper endpoint reaches height 21, negative terminal defect.

Terminal nonnegative height removes one exact Hensel lift residue inside each class but does not
remove a whole class. The common `tau=34`-through-terminal pair-gap interface is independent of
`eta`; the next attack must use an oriented absolute endpoint/signed datum.

No H21 state is excluded and no H21 charging budget is released.

Read the RL199 report, certified-facts ledger, correction/demotion ledger, red-team report, and
`proofs/RL199_H21_ORIENTED_LIFT_INDEX.md`.
Run `sh verification/run_fast_rl199_verifiers.sh`.

Next target: `RL200_H21_ORIENTED_LIFT_GLOBAL_SELECTOR_TARGET.md`.

# Authoritative start

RL338 is CLOSED AND FROZEN. RL339 is the unique incoming research session and is not started.

Current stage: R1 Parent Bridge. Global proof status: OPEN. Scope remains the ordered genuine `g=2`, `Z0>0`, `K<0` parent at `(a,ell)=(217976794617,137528045312)`. The least-state floor `m>=2^71` remains externally conditional.

Unique live target: `RL339_PARENT_BRIDGE_Q35_CLOSURE_TARGET.md`.

Read in this order:

1. `RL338_SESSION_STATE_AND_RL339_KICKOFF.md`
2. `RL339_PARENT_BRIDGE_Q35_CLOSURE_TARGET.md`
3. `RL338_PROOF_LEDGER.md`
4. `RL338_EXACT_CERTIFICATE.md`
5. `RL338_CORRECTION_AND_DEMOTION_LEDGER.md`
6. `RL338_GLOBAL_PROOF_ROADMAP_STATUS.md`
7. `RL338_CLOSEOUT_VERIFICATION.md`
8. inherited RL337/RL336 ledgers only for named dependencies

Portable startup verifier:

- `python3 -I verification/verify_rl338_q35_fast.py`

Independent red team:

- `python3 -I verification/red_team_rl338_q35.py`

Heavy finite-certificate reproduction is available as `verification/verify_rl338_q35_exhaustive.py`; it is not required for routine startup after the committed flat-tree identity and fast checks pass.

Key correction warning: the q=35 exceptional successor layer has 24 exact p=1..4 continuations in addition to five p=7 continuations. All are strongly negative. Do not reuse the earlier scratch phrase that “only five continuations exist.”

The live theorem is `35(K-2H)-S<=43`; the conditional carry cap is `n<=32546271999`. R1 is still OPEN. RL339 should try to consume these directly into parent closure before considering q=36.

Do not mix this research branch with the separate Lean formalisation project.

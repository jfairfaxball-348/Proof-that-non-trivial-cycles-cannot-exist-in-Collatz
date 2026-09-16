# RL337 authoritative start

RL336 is closed and frozen in `sessions/RL336/`. RL337 is the unique incoming RL and is not started.

Current stage: R1 Parent Bridge. Global proof status: OPEN. Ordered genuine `g=2`, `Z0>0`, `K<0` parent only. The least-state floor `m>=2^71` remains externally conditional.

Unique live target: `RL337_PARENT_BRIDGE_AFFINE_OWNERSHIP_TARGET.md`.

Read in this order:

1. `RL336_SESSION_STATE_AND_RL337_KICKOFF.md`
2. `RL337_PARENT_BRIDGE_AFFINE_OWNERSHIP_TARGET.md`
3. `RL336_PROOF_LEDGER.md`
4. `RL336_CORRECTION_AND_DEMOTION_LEDGER.md`
5. `RL336_GLOBAL_PROOF_ROADMAP_STATUS.md`
6. `RL336_CLOSEOUT_VERIFICATION.md`
7. inherited `RL335_PROOF_LEDGER.md` only for dependencies

Portable current verifier commands from this `authoritative/` directory:

- `python3 -I verification/verify_rl336_q32_prefix.py`
- `python3 -I verification/verify_rl336_q32_consumer.py`
- `python3 -I verification/verify_rl336_zero37_part1.py`
- `python3 -I verification/verify_rl336_zero37_part2.py`
- `python3 -I verification/verify_rl336_zero37_part3.py`
- `python3 -I verification/verify_rl336_zero36_part1.py`
- `python3 -I verification/verify_rl336_zero36_part2.py`
- `python3 -I verification/verify_rl336_zero36_part3.py`
- `python3 -I verification/verify_rl336_zero36_part4.py`
- `python3 -I verification/verify_rl336_zero36_part5.py`
- `python3 -I verification/red_team_rl336.py`

This is a ZIP/sidecar packaged authority. The bundle is `RL336_HANDOVER_BUNDLE.zip`; its outer checksum is `RL336_HANDOVER_BUNDLE.zip.sha256`. Do not mix this branch with the separate Lean formalisation project. Knowledge catalogues may be stale/deferred and are lookup caches, not mathematical authority.

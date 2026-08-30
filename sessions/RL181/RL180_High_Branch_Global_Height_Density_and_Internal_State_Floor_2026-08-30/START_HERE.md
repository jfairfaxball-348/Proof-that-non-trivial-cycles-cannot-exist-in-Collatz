# RL180 authoritative handover — start here

1. Run `sha256sum -c SHA256SUMS.txt`.
2. Run `bash verification/run_fast_rl180_verifiers.sh`.
3. Read `RL180_HIGH_BRANCH_GLOBAL_HEIGHT_DENSITY_AND_INTERNAL_STATE_FLOOR_2026-08-30.md`.
4. Read `RL180_CERTIFIED_FACTS_AND_PROOF_LEDGER.md` and `RL180_CORRECTION_DEMOTION_LEDGER.md`.
5. Continue with `RL181_HEIGHT_DENSITY_SHALLOW_POPULATION_AND_PAIR_GAP_COUPLING_TARGET.md`.

Incoming authority frozen at commit `da1fb0312376cb7766848d52f0d7977c49a549ee`, authoritative tree `0cd46d9fb1e6eabd0133b2b6e0e8366790d8b2b5`.

Verification economy applies: after the manifest and fast verifier pass, accept the frozen RL180 ledger. Do not recursively replay historical expensive certificates unless a verifier fails, a dependency is unresolved, or a contradiction triggers stop-and-repair.

# RL67 handover — start here

This bundle freezes the authoritative RL67 research state on 2026-08-24.

Start with `RL67_SESSION_STATE_AND_KICKOFF_2026-08-24.md`. Then read
`RL67_PREVIOUS_ACTIVE_INTERFACE_AND_HEIGHT_ONE_REACHABILITY.md` for the full new mathematics.

At the start of RL68 verify only the current gate:

1. outer RL67 `.sha256` sidecar;
2. freshly unpacked internal `SHA256SUMS.txt`;
3. `bash verification/run_fast_rl67_verifiers.sh`.

Apply the verification economy rule in the session ledger. Do not recursively reopen historical bundles unless a verifier fails, a needed definition is unresolved, or an apparent contradiction triggers stop-and-repair.

Important proof-state warning: the canonical height-one inequality `J<=2^H` is **not proved**. It is bounded evidence plus a research target. RL67 explicitly records counterexamples to a naive local magnitude induction.

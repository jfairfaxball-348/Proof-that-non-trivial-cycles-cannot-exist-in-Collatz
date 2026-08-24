# G10 semantic contract bundle

Frozen 11 August 2026.

Contents:
- `G10_Rules_Contract_v1.json`: machine-readable state/rule contract.
- `g10_contract.py`: executable metadata/reference layer; deliberately no chess move generator.
- `test_g10_contract.py`: executable tests for history, claims and automatic terminal precedence.
- `G10_Conformance_Vectors_v1.json`: frozen vectors for G11 independent move-generation/state-conformance work.

Boundary: G10 freezes semantics. G11 must implement two genuinely independent legal-move/state engines and run the frozen vectors plus exhaustive/adversarial conformance tests. No G10 test result is a claim of independent move-generation verification.

# RL-5 Session Provenance

- Date: 2026-08-19
- Parent artifact: `Collatz_Rsharp_RL4_Seed_2026-08-19.zip`
- Inherited verifier: `parent_rl4/tools/verify_rl4_crossing_exit.py` — PASS
- New verifier: `tools/verify_rl5_anchor_grammar.py` — PASS
- External input used structurally: Hercher, *There are no Collatz m-Cycles with m <= 91* (Journal of Integer Sequences 26 (2023)), with the journal's June 14 2026 corrigendum. The project uses only the stated consequence `m>=92`; the external proof is not reproduced here.
- Research status: RL remains open.
- Continuation result: RL-L38--RL-L41 derive the exact ceiling/affine anchor recurrence, common-denominator rotation formula, numerator valuation triangularity, and the generic one-rotation scalar criterion `D|C_r`.
- Extended diagnostic: 165,728 generic admissible compressed words with `P<=3`, `n,t<=8` audited under RL-L41; no nontrivial realization in the declared domain.

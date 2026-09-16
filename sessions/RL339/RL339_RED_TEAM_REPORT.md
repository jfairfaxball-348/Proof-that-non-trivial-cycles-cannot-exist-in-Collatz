# RL339 independent red-team report

Date: 2026-09-16. Status: GREEN FOR PROMOTED SCOPE.

Independent scripts reconstruct the finite word population from phase cuts, profile grammar, modular residue, exact backward parity and integrality, and deterministic forward escape. They do not import the RL338 mechanical core used by the primary reconstructor.

- `verification/reproduce_total43.py`: all 28 ordered pairs, 721 admissible templates, 80,403 candidate rows; max escape 186.
- `verification/reproduce_large_singletons.py`: totals 44..70, 378 pairs, 11,865 templates, 39,361 rows; max escape 185. It asserts the per-total candidate counts 44:26432, 45:8680, 46:2852, 47:934, 48:306, 49:103, 50:39, 51:11, 52:3, 53:1, 54..70:0.
- `verification/reproduce_q35_critical.py`: all q=35 nonnegative high-to-high p=5..8 layers, with exact `(pairs,templates,rows,distinct_sources,max_escape)` listed in `RL339_EXACT_CERTIFICATE.md`.
- `verification/red_team_rl339.py`: independently checks zero-slack edge classification, group-four anchor pairing, the step-44 phase and rational logarithm/exponential lower bound, rho=60 cap endpoint, and the monotonic-step inequalities.

The independent checks confirm the claimed ranges and no unresolved candidate. They do not remove the external floor condition, prove R1, or discharge Gate A/B.

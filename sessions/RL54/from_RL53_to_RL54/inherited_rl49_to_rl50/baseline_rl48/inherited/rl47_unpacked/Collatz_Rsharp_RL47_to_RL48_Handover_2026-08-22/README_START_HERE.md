# RL47 -> RL48 Handover — Start Here

Date: 2026-08-22

This handover continues the Collatz R-sharp / RL program after RL47. The main RL47 advance is that the formerly partial q=79 terminal-area frontier is now an exact finite certificate, and the one-excursion geometry has gained two new exact analytic coordinates: a phase coordinate `Phi` that quotients neutral `11` motion, and a rank-transport identity in which the area `H` is literally total displacement of matched moved ranks.

## Mandatory first commands

From the bundle root:

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl47_core_verifiers.sh
bash verification/run_rl47_q134_stress_verifier.sh
```

Any checksum or verifier failure is a stop-and-repair event.

The q134 stress verifier is logically independent of the q79 certificate. It is included because it tests the stronger height-one macro/residue implementation at the next substantially larger pair.

Then read, in order:

1. `RL47_PROOF_STATE_AND_PROGRESS.md`
2. `RL47_RADIUS3_BRIDGE_AND_CLOSURE_ROADMAP.md`
3. `RL47_REPRODUCIBILITY_LEDGER.md`
4. `RL48_RESEARCH_KICKOFF_PROMPT_2026-08-22.md`

The previous RL46->RL47 bundle is preserved intact under `inherited/` for provenance and reconstruction of inherited RL45/RL46 claims.

## Executive proof state

### Analytic theorems / exact identities newly established in RL47

- cap-death monotonicity: once the exact prefix-cap ratio drops below one, no cap-legal terminal can ever be reached;
- exact phase coordinate
  `Phi = 2^n (T + 3^d - 1) / 3^(p_alpha+d)`, with every `11` edge satisfying `Delta Phi = 0`;
- terminal phase identity `Phi_terminal = 9 zeta (1+2^-(t+3))`;
- exact rank displacement identity `H = sum_j (a_j-b_j)`;
- exact normalized rank-position terminal identity recorded in `RL47_PROOF_STATE_AND_PROGRESS.md`;
- a rigorous relaxed rank-transport upper bound excluding all strict violations for q=17 and q=24, and excluding the high-t tails for q=55,79,134.

### Exact finite certificates newly established in RL47

- `(a,ell,q)=(214,135,79)`: no retained prefix-cap terminal geometry with `H<t+3`; the formerly partial q=79 frontier is closed exactly.
- Regression agreement on q=17, q=24, q=55 with the same fixed-t future-hull verifier.
- `(363,229,134)`: the stronger height-one macro/residue verifier excludes strict violations for `t=2,4,...,16`.

### Still open

- the uniform cutoff-free theorem `H>=t+3` for every retained one-excursion terminal geometry;
- q=134 for the remaining even strip `18<=t<=114` (while `t>=116` is excluded analytically);
- the quantitative same-root radius-3 bridge using `f=3T^q-2`, `L=2T^ell-1`, and the phase polynomial `P`;
- global RL closure.

## Strategic warning

Do not try to prove settling of the unrestricted height-one quotient: it contains the ordinary Collatz map exactly. Do not revive the falsified universal absolute-resultant bound from RL45. The live route is to use prefix-cap / low-area structure to prove the terminal inequality uniformly and to translate that same low-displacement structure into a same-root arithmetic obstruction suitable for the already-closed radius-3 theorem.

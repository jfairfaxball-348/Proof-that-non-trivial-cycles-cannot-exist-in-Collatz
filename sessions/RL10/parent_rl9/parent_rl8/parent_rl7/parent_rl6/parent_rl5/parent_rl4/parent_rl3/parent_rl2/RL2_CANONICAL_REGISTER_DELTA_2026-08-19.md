# RL-2 Canonical Register Delta — 2026-08-19

This delta supplements `RL_CANONICAL_LEMMA_RESULT_REGISTER_2026-08-19.md`.

| ID | Claim | Status |
|---|---|---|
| RL-L11 | `Phi_h(e)` is exactly the modulo-`3^h` integrality code for a length-`h` accelerated inverse word ending at `y`. | **PROVED ANALYTIC THEOREM** |
| RL-L12 | Any two legal same-endpoint inverse histories have identical `Phi_h`; inherited suffix matching is not a relative tail/cycle constraint. | **PROVED ANALYTIC THEOREM / REINTERPRETATION** |
| RL-L13 | Periodically unwrapping the cycle extends the equality to every `h<=k`; the extension is automatic and non-pruning. | **PROVED ANALYTIC THEOREM** |
| RL-G6 | `Phi` + inverse legality + least-red floor + local xi admits analytic infinite lift towers; that local automaton cannot exclude RL. | **FAILED / REFUTED ROUTE** |
| RL-L14 | For `k>0`, `b_{k-1}!=a_{L-1}` while their parities agree; the terminal exponent difference is nonzero even. | **PROVED ANALYTIC THEOREM** |
| RL-L15 | Backward height defect obeys `3δ' = 2^dδ +(2^d-3)R#-1`; exactly `d=1` contracts toward `R#`, all `d>=2` expand. | **PROVED ANALYTIC THEOREM** |
| RL-L16 | Side-branch xi probe: `q_d=v3(2^(d-1)y+1)` gives exact `xi(p_d(y))`; for `y=R#=1 mod3`, `q_d <= floor((d-1)log2/log(3/2))`. | **PROVED ANALYTIC THEOREM** |
| RL-L17 | Initial forward exponent-1 run from `R#` has exact length `v2(R#+1)-1` and is exactly xi-neutral. | **PROVED ANALYTIC THEOREM** |
| RL-X4 | New verifier audits inverse-code equivalence, same-root collapse, xi-safe lifts, xi probes, height recurrence and neutral-run length on declared finite domains. | **EXACT FINITE CERTIFICATE** |

## Open obligations after RL-2

- **RL-O1 is reformulated, not closed:** raw suffix classification is solved as an inverse-code identity; the remaining need is a *relative* tail/cycle invariant.
- **RL-O2 remains CRITICAL:** fuse height defect with cycle rotations/minimum constraints.
- **RL-O3 is upgraded:** use the full xi side-branch probe profile `q_d(y)`, not only `m=v3(y+1)`.
- **RL-O5 remains CRITICAL:** `k=0` and `k>0` should now be attacked with different state systems.
- **RL-O7 remains CRITICAL:** no finite diagnostic is an infinite exclusion without a lift theorem.

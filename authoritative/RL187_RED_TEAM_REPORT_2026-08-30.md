# RL187 red-team report

Date: 2026-08-30

Result: **PASS with no closure claim**.

## Checks

1. **Incoming authority / verification economy — PASS.** Startup froze `main=55fee2ec...`, root tree `970fa2e...`, authoritative tree `bff1a080...`. The RL186 manifest/fresh-unpack/fast-suite/red-team records were PASS and the exact RL186 verifier logic was independently replayed.
2. **Zero-prefix telescoping — PASS.** The identity `d_j=c_j+M_j-M_(j+1)` is summed through the `tau` zero transitions, ending at the first-defect endpoint maximum. This gives `D=tau+ell+h_0-H`; no endpoint is omitted.
3. **RL186 valuation splice — PASS.** At first defect `C_tau` is odd, so `D=v_2(C_0)` and `C_tau=3^tau odd(C_0)` are used exactly as inherited.
4. **Mechanical-rank interval — PASS.** Terminal rank comes from the actual chronological rotation by `B=A-L mod L`; the rank interval is an exact floor/carry condition, not a frequency heuristic.
5. **Joint ownership — PASS.** Multiple starts selecting one physical terminal defect must share the same physical terminal numerator, height, and mechanical residue. The joint-family table is an upper-capacity theorem only.
6. **RL186 consistency — PASS.** The independent RL187 enumeration reproduces the entire frozen RL186 `tau=28,...,39` terminal-height vocabulary exactly before adding joint rank compatibility.
7. **Block-span off-by-one — PASS.** A first defect at offset tau consumes at least `tau+1` phase positions from start through terminal defect. All survival-density denominators use `tau+1`, never tau.
8. **Multiscale capacity — PASS.** The full `N_28,...,N_39` staircase is computed from exact joint families. `N_37` independently reproduces the inherited `2L/39` cap.
9. **Charging multiplicity — PASS.** For `H<=17`, all individually possible offset charges fit within `2^-(H+1)`; for `H>=18`, every maximal exact co-ownership family is checked. Thus no terminal defect is overcharged when several starts select it.
10. **Carry handling — PASS.** Ordinary selected-defect charging excludes the carry. The positive carry `>1/2` is added only in the separate signed consumer.
11. **Signed total — PASS.** A rational interval re-certifies `0<F2<1/2`; the lower bounds on each sign follow from absolute mass plus this signed total.
12. **Variation versus excursion — PASS.** `>443`, `>221.5`, and `>73.8` are explicitly total/directional variation statements. No chronological K-prefix escape is inferred.
13. **Near-crossover survivor — PASS.** The `{35,36,37}` family with `(T,H)=(3^37,21)` is recorded as surviving the current necessary tests. It is not silently treated as impossible.
14. **Historical barriers — PASS.** No arbitrary ternary residue capacity, unconstrained word BFS, RL168-RL171 generic rank/lattice route, or RL173 auxiliary functional is substituted for physical proof.
15. **No false closure — PASS.** The sole high type, preferred branch, Gate A/B, non-trivial-cycle exclusion, and Collatz all remain open.

## Main remaining obligation

The closest staircase crossover is `N_35`. Its sole density-`3/38` witness is the joint terminal family `{35,36,37}` at `(3^37,21)`. RL188 should attack that one family physically; until it is excluded or forced to use additional block span, no `N_35` contradiction is certified.

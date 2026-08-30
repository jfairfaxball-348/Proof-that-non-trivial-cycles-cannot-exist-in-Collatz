# RL181 red-team report

Date: 2026-08-30

- **Incoming authority:** PASS. Frozen at commit `c6c446fce485e91acd4595663ccb317c9577de80`, authoritative tree `d22e75f9a22630ea740d8bd3b1c0111be56078b8`.
- **Corrected physical functional:** PASS. Only `2^G` corrected flow is used.
- **Periodic carry:** PASS. The unique mechanical carry at `t=L-p` is separated from ordinary p-shift edges; no modular wrap is silently treated as carry-free.
- **Physical versus normalized:** PASS. `x_i=y_i/2^h_i` is explicitly a normalized coordinate of an actual physical state, not an odd state of the cycle.
- **Negative-flow charging:** PASS. Every negative term is noncarry; its target mechanical-loss term is distinct under the p-shift permutation, so the global charge has no multiplicity leak.
- **K corridor arithmetic:** PASS. Rational log/exp enclosures certify the displayed integer corridor from the frozen RL180 `W` upper bound.
- **Shallow adjacency:** PASS. The `2N-L` bound is a directed-cycle incidence theorem; no phase-order shortcut is used.
- **Dyadic numerators:** PASS. Denominator and parity statements are restricted to actual noncarry physical p-shift pairs. Arbitrary lattice points are not promoted as physical states.
- **Width occupancy:** PASS. The reciprocal mechanical-weight lower envelope is minimized over arbitrary selected residue positions before the certified `m` ceiling is applied.
- **Historical barriers:** PASS. RL168-RL171 and the higher-modulus barrier remain frozen; no generic rank/chain argument is repackaged as new mathematics.
- **No false closure:** PASS. The `(37,0,23,-1)` high type and all global gates remain open.

Fast verifier: PASS before candidate packaging.

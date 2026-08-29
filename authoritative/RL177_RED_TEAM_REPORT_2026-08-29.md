# RL177 red-team report — 2026-08-29

## Scope

This review stress-tests only the new RL177 early-mismatch, flow-quantization,
zero/positive common-height split, and finite-local-automaton claims.  It
accepts the frozen RL176/RL175 ledgers under verification economy.

## Checks

- **Corrected coordinate:** PASS.  Every defect uses
  `G_i=S_{p+i}-S_p-S_i`; the old RL173 `3^(-G)` functional is not revived.
- **Carry-free identity:** PASS.  `J+1<=37<t=L-p`, so
  `b_{p+i}=b_p+b_i` throughout the local interface and
  `G_i=h_i-h_{p+i}` is valid there.
- **Lifted order:** PASS.  `E_{p+i}=1+E_i-LG_i`; before first mismatch this
  gives consecutive integer defects, and RL168.1 legitimately converts
  their order into physical state order.
- **First-flow quantum:** PASS.  The two sign branches were derived
  separately before being written in the unified formula.  The power of two
  is `v=v2(g_p)`, not an assumed approximation.
- **Mandatory carry compensation:** PASS.  At `t`,
  `G_t=1+h_t>0` and the contribution is
  `rho_t(2-2^-h_t)>=rho_t>1/2`.  Combining this with the inherited strict
  half-barrier correctly yields the positive-first-defect compensation law.
- **Zero-height classification:** PASS.  Nonnegative next heights force
  `c_J=2` and the two exponent choices `1,2`; the exact verifier enumerates
  all and only the 14 allowed indices under `v<=37`.
- **Positive-height support count:** PASS.  The two height-`H` phases are
  distinct, and at least one of the two next phases has height at least
  `|d|`; with `p+37<L` this third phase is distinct.
- **Mechanical-loss inequality:** PASS.  The proof uses only `rho_i>1/2`
  and the three certified positive phases; it does not assume support
  density.
- **Stronger half-barrier:** PASS.  It reuses exactly the certified RL175
  exponential inequalities and improves the loss coefficient from `5/8` to
  at least `3/4` only in the `H>=1` branch.
- **Automaton scope:** PASS.  The 15,872 count is over identified local tuples,
  not full exponent histories, and its survival statements are explicitly a
  method barrier, not physical existence.
- **High valuations:** PASS.  `v=36` has no zero-height tuple; `v=37` has
  zero height only at `J=23`, two signs.
- **External provenance:** PASS.  No new core theorem uses `m>=2^71`.
- **No false closure:** PASS.  No cycle branch or Collatz is claimed closed.

## Conclusion

PASS for promotion as a narrowing/compensation result.  RL178 should attack
the required negative-flow/height-return mechanism rather than rerun the
same local feasibility automaton.

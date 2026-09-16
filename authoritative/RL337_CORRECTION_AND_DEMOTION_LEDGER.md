# RL337 correction and demotion ledger

Date: 2026-09-16
Status: FROZEN WITH RL337 CLOSEOUT

This ledger records only RL337 scratch corrections. No inherited authoritative theorem is demoted.

## C1 — fixed-terminal affine-source sign corrected

During exploratory discussion the direction of the fixed-terminal source comparison was stated incorrectly.

For a gap word `w`,

`3^L x_L = 2^H x_0 - C(w)`,

so

`x_0=(3^L x_L+C(w))/2^H`.

RL337 proves `C(g)<C(h)` for every nonzero positive profile `g` relative to its zero-profile mechanical reference `h`. Therefore

`x_0(g)<x_0(h)`

at the same terminal state, not the reverse.

All scratch reasoning using the opposite sign is discarded. The frozen RL337 proof ledger uses only the corrected direction.

## C2 — mechanical-reference least-state barrier demoted

A scratch calculation attempted to show that the zero-profile mechanical reference stays above the least state by a large numerical margin and then to use that as a descent barrier. Because the source-order interpretation used in that route had the wrong sign, this calculation is not promoted and must not be cited as a theorem or method barrier.

The corrected affine identity may still be useful to bound profile carry-drop, but that requires a fresh ownership argument.

## C3 — no ordinary residue monotonicity

Carry ordering does not induce ordinary numerical ordering of the canonical residue modulo `3^L`. Exploratory comparisons wrap in both directions. Any successor residue argument must be 3-adic/exact-state, not an ordinary order argument.

## C4 — no cyclic use of the linear `q_t` interval

The live `q_t` sequence inherited from RL326 is a linear least-root interval of length `ell-rho`. RL337 briefly explored a divisibility condition modulo `2^a-3^ell`; no cyclic theorem was promoted because the omitted `rho`-tail is not automatically supplied by the live linear profile.

## C5 — subordinate diagnostics only

The following remain diagnostics, not promoted theorems:

- exploratory triangular 3-adic profile decoding;
- denominator/divisibility experiments;
- the idea that higher profile heights might automatically improve the current q-charge enough to close R1;
- any q=33 claim beyond the frozen RL336 diagnostic status.

The exact p=5 shared-state witness recorded in the RL337 proof ledger is a verified finite diagnostic, not an all-length result.

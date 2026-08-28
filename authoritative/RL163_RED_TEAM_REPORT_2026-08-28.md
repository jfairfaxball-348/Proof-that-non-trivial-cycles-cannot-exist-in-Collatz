# RL163 red-team report

Status: PASS, with scope limits retained.

- Re-derived `Ap=uL+1` directly and checked the unique carry start from `A(L-p)=-1 mod L`.
- Checked arcs crossing the physical root cut through lifted `S` and `b`; there is no missing wrap term.
- The affine identity comes from ordinary `3y+1`, not generalized-increment scaling.
- The long phase arc has a physical positive odd numerator; no quotient representative or phase polynomial is substituted for it.
- Summing all arcs was counted two ways and returns only `pA`; no capacity or exclusion is claimed.
- `g>1`, global Gate closure, nontrivial-cycle exclusion, and Collatz remain open.

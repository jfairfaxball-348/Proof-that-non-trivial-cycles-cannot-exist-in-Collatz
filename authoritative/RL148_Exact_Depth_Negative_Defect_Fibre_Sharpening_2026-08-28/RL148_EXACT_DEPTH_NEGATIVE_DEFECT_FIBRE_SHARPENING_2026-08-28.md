# RL148 — Exact-depth negative-defect fibre sharpening

## Status

**Proved analytic ordinary-owned physical-fibre theorem** in the inherited
RL136 isolated-negative-excursion range.  No multiplicity or global branch is
excluded.

For an isolated `h=-1` excursion, RL136 gives an actual negative state
`y == 3 (mod 4)` and entry boundary `z=2^d y` at exact depth
`d=h_(j-1)+c`.  Hence

`z == 3*2^d (mod 2^(d+2))`.                                  (1)

Let `E^=_d` be the number of isolated excursions with exact depth `d`.
Their entry boundaries are distinct actual states in one residue class modulo
`2^(d+2)`, so their span is at least `(E^=_d-1)2^(d+2)`.  The global least
state is odd and lies below these even entries.  Therefore

`W >= (E^=_d-1)2^(d+2)+1`.                                  (2)

This strengthens RL136's `>=d` dyadic packing modulus by a factor four on an
exact-depth stratum.  It does not dominate the old bound after different
depths are pooled.

The associated exit `e=(3y+1)/2` obeys
`3z+2^d=2^(d+1)e` and `e == -1 (mod 3)`.  This supplies no fixed residue of
`z` modulo three, so no unsupported CRT-product packing is claimed.

## Scope and red teams

All states are the actual ordinary states supplied by RL136; candidate
determinant positions are not used.  The ordinary `+1` recurrence is
load-bearing.  The theorem does not force an excursion, exclude mixed height,
negative defect generally, `g=1`, Gate A/B, non-trivial cycles, or Collatz.

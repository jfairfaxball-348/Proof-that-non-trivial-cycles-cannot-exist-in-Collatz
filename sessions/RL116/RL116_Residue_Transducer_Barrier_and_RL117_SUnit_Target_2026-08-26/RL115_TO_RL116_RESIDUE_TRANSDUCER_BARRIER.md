# RL116 — exact-residue transducer barrier and route transition

## Outcome and classification

RL116 tested the two-base finite-transducer route. No uniformly finite,
ownership-preserving transducer or synchronizing defect is proved. The result
is an analytic **barrier for the direct exact-residue construction**: a
translation-compatible machine which accumulates the ordinary numerator modulo
the variable denominator and exactly decides `D|Q` requires all `D` residue
states. This violates the required uniform finiteness because the live input
has no established bound on `D=2^A-3^L`.

Let a residue machine identify two classes `r != s` in `Z/DZ` while allowing
additive continuation. The final correction `c=-r` gives `r+c=0` but
`s+c != 0` modulo `D`; exact divisibility therefore separates the two states.
Consequently an exact translation-compatible quotient has at least `D`
states. The literal transition state `(binary position, ternary rank, Q mod
D)` is thus unbounded in its final component.

This does not prove that no finite transducer can ever work: escaping the
lemma would require a new theorem that the actual legal selected-support
continuations avoid all separating corrections. No such theorem is inherited
or established here. A parity/local-grammar machine would avoid the residue
state only by failing the required ownership and RL20 tests. The stated route
therefore meets its stop condition and passes to the legal S-unit gap route.

No Gate closure, nontrivial-cycle exclusion, or Collatz conclusion is claimed.

## Red teams

- **RL20:** its nonzero `Q mod D` is rejected only by the full residue test,
  not by radius-four grammar. A quotient that forgets this distinction is not
  an RL116 construction.
- **RL79:** generalized increment supplies `D|sQ`; no `s` is cancelled, and
  the ordinary residue test is not made increment-invariant.
- **RL81:** `Q/D` is physical only after the exact zero residue is known.
- **Primitivity:** retained only for the inherited distinct selected rotations
  and `S!=0`; it supplies no bounded residue state.
- **Scope and finite work:** no Raw/Farey scope is used. The included finite
  check validates the separation algebra for `D=2..64` only; the lemma itself
  is the displayed general calculation and is not a transducer theorem.

## Dependencies and next route

This barrier uses RL109 ordinary ownership and the RL115 unbounded Fourier
resolution observation. It corrects no inherited claim. Begin RL117 with a
legal coordinate restriction for an S-unit gap; do not revive the direct
residue transducer without a new legal-continuation theorem.

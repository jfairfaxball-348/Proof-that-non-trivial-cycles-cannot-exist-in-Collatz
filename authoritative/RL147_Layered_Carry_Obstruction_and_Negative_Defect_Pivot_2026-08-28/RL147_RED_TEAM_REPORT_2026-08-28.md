# RL147 red-team report

- **Ordinary affine ownership:** PASS. The proof begins from the ordinary
  numerator and denominator; no generalized-increment normalization is used.
- **Layer factorization:** PASS. Only the proved weighted sum is used. No
  individual binary layer is called owned.
- **Mechanism-versus-existence:** PASS. The height-two example is a local
  recurrence witness, explicitly not an actual cycle.
- **Scope:** PASS. No exclusion is claimed for mixed height, negative defect,
  `g=1`, global gates, non-trivial cycles, or Collatz.
- **Frozen barriers:** PASS. The RL145 local population route is not reopened.

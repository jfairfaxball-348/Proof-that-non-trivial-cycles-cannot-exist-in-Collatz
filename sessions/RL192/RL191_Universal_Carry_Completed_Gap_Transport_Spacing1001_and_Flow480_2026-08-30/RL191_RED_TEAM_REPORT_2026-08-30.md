# RL191 Red-Team Report

Date: 2026-08-30

Result: **PASS WITH SCOPE GUARDRAILS**.

## Checks performed

### 1. Did the proof silently reuse the invalid common-mechanical assumption?

No.  RL191 derives
`2^{c_i}Delta_{i+1}=3Delta_i+epsilon_i`
from the inherited full-period `K/rho` identities.  The actual physical source bit `c_i` is used.  The mechanical threshold is therefore handled by the exact source word rather than assumed absent.

### 2. Is the carry source genuinely covered?

Yes.  At the unique carry source the inherited carry relation gives
`G_i=h_i+1`, so
`epsilon_i=2-2^{-h_i}` and hence `1<=epsilon_i<2`.
The verifier uses the more conservative bound `|epsilon|<2` at every transition.

### 3. Are the two RL190 exceptional ranks merely skipped?

No.  They are explicitly evaluated under the universal transition and both exact target gaps are missed.

### 4. Does the 46..1000 scan miss mechanical-word changes inside rank intervals?

No.  Every necessary overlap is split at every preimage, for every source offset, of both modular wrap `0` and threshold `R`.  Endpoint words are asserted equal on each integer atom.  The certificate checks 24,173 atoms across 432 nonempty separations.

### 5. Is floating point used in an exclusion decision?

No.  The target-miss inequalities, density calculation, population counts, and charging checks use Python integers/Fractions.  The recorded minimum safety margin is derived exactly.

### 6. Is spacing >=1001 overclaimed?

No.  Separations 46..1000 are excluded; RL190 already supplied spacing >=46.  The exact logical conclusion is spacing >=1001.  No statement is made about whether separation 1001 or larger is realizable.

### 7. Is the new `N35` bound exact?

Yes.  The grouped density reduction uses `S>=963`, inherited
`K<=floor(2S/37)`, and a 37-residue exact check.  The final floor and remainder are integer-checked.

### 8. Was charging safety weakened to obtain >480?

No.  Every inherited RL187 low-height and high co-ownership family is rechecked.  H20 `{31,32,33,34,35,36}` and H21 `{33,34,35}` bind exactly.

### 9. Was the H21 dangerous core solved implicitly?

No.  No incidence, sign, or recurrence restriction on
`D=[23369453298,41775866136]` is certified.  H21 remains open and binding.

### 10. Is total variation being converted into chronological excursion?

No.  The closeout records only aggregate ordinary absolute flow, each signed flow mass, and each directional `K` variation.  No ordering/excursion conclusion is drawn.

### 11. Are necessary ranks treated as realized states?

No.  Rank overlaps and mechanical words are used only as a necessary state-space certificate.  Exclusion is valid on that superset; realization is not asserted.

### 12. Does RL191 close the branch or Collatz problem?

No.  The sole high branch, isolated/extremal triples, H21 physical-incidence problem, and global gates remain open.

## Verdict

The RL191 advance is suitable for promotion as an exact strengthening of the sole high-branch proof state.  No correction/demotion event is required.

# RL206 correction / demotion ledger

Date: 2026-08-31. Two explicit mathematical corrections; no silent repair.

## RL206-C1 — raw versus normalized block increment

First invalid dependency: `sessions/RL20/RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md`
R20G.12. Its preceding exact normalized block identity implies
`Delta H_j=(z^j/Y)3^(-E_(j+1))Q(B_j)`, not `(z^j/Y)Q(B_j)`.
A positive-length block has a strict increment iff its numerator is positive,
equivalently it contains a 1. The symbolic derivation and exact rational
witnesses are in `corrections/RL20_INCREMENT_NORMALIZATION_REPAIR.md`.
Preserve height geometry, nonnegative monotonicity and total strip width;
reject any lower bound using the omitted normalization. No historical file
is edited or global claim demoted because of this correction.

## RL206-C2 — source/terminal coordinate mismatch

First invalid dependency: RL203 dyadic-prefix proof section 4, immutable commit
`51daff87f4661a7f206a60df62492bc3d2d19f57`. The terminal-rank core applies at
phase `a+34`, not tau34 source phase a. Correct `p-a>=39` to `>=37`,
root-prefix depth `>=63` to `>=60`, and first root-normalization depth
`>=100` to `>=97`. These stronger inherited numeric statements are withdrawn
at their asserted source scope. Necessary terminal rank 33709842710 at source
a=p-37 is the exact predicate witness, not a physical realization.
See `corrections/RL203_SOURCE_TERMINAL_INDEX_REPAIR.md` and its independent review.
The endpoint/eta-parity laws and the qualitative below-p mod2^56 information
boundary survive; 60>56 and 97>56. RL203 deleted no ranks, so the inherited
terminal-rank set/count remains **16,188,727,234**, with no restoration/deletion.

## Scope and operational records

The new no-go concerns only the explicitly defined families. Quotient-state
residues, modulo-D-squared input, nonrational arithmetic, and independently
constrained global geometry remain open. No new Gate or global result follows.
The finite-arc bound must be uniform in the free parameter; cycle closure
cannot silently be imposed after varying that parameter.

Mechanical events: Git HTTPS access lacked credentials; authenticated GitHub
Git-object tools provide the authorized atomic transition. A provisional scratch
test incorrectly put the RL20 fake in lambda<16/15; it was corrected before the
successful finite run to the exact `16/15<lambda<3`. That draft-test bug is
separate from C1/C2 and changes no inherited classification.

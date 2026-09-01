# RL223 research report

Date: 2026-09-01.

RL223 attacked the odd-modulus tail-numerator proposal from RL222 and obtained
success criterion 4: a theorem-quality blindness result for the tested
count-only observable.

For ordinary binary words of the exact remaining length
`N=217976794593` and odd count `M=137528045296`, the affine numerator residues
are all of `Z/qZ` for every `q<=283635` coprime to 6.  The proof is uniform and
constructive: `q` equal-count Euler blocks may each move one odd step by one
position, and every switch adds the same unit modulo `q`.

An independent finite-state DP exhausts all 340 eligible moduli from 5 through
1023.  Every one saturates, with a minimal saturating prefix of length at most
16.  The inherited common witness target intersects the relaxed word-side set
for every tested modulus.

RL223 also replayed the exact common-witness parity prefix through phase51 and
constructed a modulo-5 formal completion with the exact global counts and the
correct target residue.  This is a deliberate type guard: the prefix is actual,
but the selectable blocks are formal and are not claimed to continue the exact
phase-51 endpoint.

The result eliminates a tempting but insufficient state representation.  A
finite automaton that tracks only remaining length, remaining odd count, and
tail-numerator residue cannot select candidates in the proved modulus range.
For a legal tail the residue test is exactly the endpoint-return condition
`y_end=y0 mod q`; the missing input is the actual candidate-specific legal-tail
language or an exact quotient of it.

No candidate, prefix, or rank deletion is promoted.  Gate A, Gate B, branch
contradiction, and global nontrivial-cycle exclusion remain open.

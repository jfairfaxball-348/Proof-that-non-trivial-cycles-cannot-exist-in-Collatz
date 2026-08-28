# RL154 — bidirectional singleton transfer and terminal-height barrier

RL154 gives a proved analytic reduction plus an exact finite arithmetic
certificate.  It does not exclude the `g=1` survivor.

Let the ordinary singleton cycle be rooted at its least odd state `m<2^75`,
with nonnegative defect `h_j=b_j-S_j`, `b_j=floor(Aj/L)`.

For a prefix ending at step 75, `S_75>=75`.  The affine prefix equation

`2^S y_75=3^75 m+C`, `C>0`,

therefore fixes `m` modulo `2^75`; within the state ceiling this is an exact
candidate.  Conversely, if the final 75 exponents have sum `T`, then

`2^T m=3^75 y_(L-75)+C_tail`,

so `m == 2^(-T)C_tail (mod 3^75)`.  Since `3^75>2^75`, the terminal word
also fixes the exact candidate whenever its canonical residue is below the
ceiling.  This is the correct two-sided meet datum.

It is not a finite certificate from local constraints.  The exact dynamic
count of nonnegative, positive-exponent height prefixes of length 75 is

`15,537,359,898,820,273,235,593,329,305,889`.

Moreover, at the terminal cut `j=L-75`, positivity only gives

`h_j<=b_j-j=80,448,749,261`.

That bound is attained in the local grammar: take exponent one through the
cut, make one downward jump, and follow the mechanical tail.  Thus no small
terminal-height cutoff follows from the inherited defect recurrence,
prefix-sign theorem, or least-state lower inequality.  The latter is already
automatic for every nonnegative prefix because `2^S<3^j`.

This freezes one route only: a viable singleton meet-in-the-middle proof must
use new global full-modulus affine ownership to prune terminal heights or
residues.  It must not use an arbitrary height cutoff, split defect levels
into independently owned congruences, or import RL139's `g>1` factor
obstruction.

No correction/demotion, frontier advance, Gate closure, or Collatz claim is
made.


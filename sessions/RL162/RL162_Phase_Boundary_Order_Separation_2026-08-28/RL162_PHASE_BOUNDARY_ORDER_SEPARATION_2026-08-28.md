# RL162 — phase-boundary order-separation barrier

## Scope

RL162 tests whether the corrected dense phase polynomial can be compressed to
a sparse boundary polynomial and controlled using chronological physical run
information.  The direct transfer fails: phase adjacency is a different
cyclic order from physical time adjacency.  This is an exact method barrier,
not a cycle construction or exclusion theorem.

## 1. Exact height-one boundary compression

In the singleton nonnegative-defect height-one subcase set

\[
E=\{Aj\bmod L:h_j=1\},\qquad
P_h(T)=2\sum_{r=0}^{L-1}T^r-\sum_{r\in E}T^r.
\]

RL157's corrected phase has `2rho^L=1 (mod D)`, with
`D=2^A-3^L`.  For

\[
B_E(T)=1+(T-1)\sum_{r\in E}T^r,
\]

one obtains

\[
B_E(\rho)=-(\rho-1)P_h(\rho). \tag{1}
\]

The factor `rho-1` is a unit modulo `D`: a prime divisor of both it and `D`
would make `2rho^L=1` read `2=1`.  Thus the boundary and dense phase
conditions are equivalent; no second ownership condition is created.

## 2. The order-separation theorem

### Theorem RL162-A

No bound on ordinary chronological run boundaries can, from the positive
exponent/nonnegative-defect grammar alone, bound the number of boundaries of
`E` in increasing phase-residue order.

### Proof

For every `n>=2`, take

\[
A=4n,\quad L=2n+1,
\]

and set `h_j=1` precisely for `2<=j<=n+1`, all other `h_j=0`, and
`h_L=h_0=0`.  Then `gcd(A,L)=1`, while `2^{4n}>3^{2n+1}` because it holds at
`n=2` and its ratio grows by `16/9` each increment of `n`.  With
`b_j=floor(Aj/L)`, all exponents

\[
a_j=b_{j+1}-b_j+h_j-h_{j+1}
\]

are positive: the upward height jump occurs where `b_2-b_1=2`, the downward
jump only increases the exponent, and elsewhere the mechanical increment is
one or two.  Hence this is a valid positive-exponent nonnegative-defect
grammar.

Its height-one set is one chronological interval, so it has two physical-time
boundaries.  But `A=-2 (mod L)` and `A^{-1}=n (mod L)`.  Its `n` phase
residues are pairwise nonadjacent: a physical index difference `1<=d<n` has
phase difference `-2d`, never `+1` or `-1` modulo `2n+1`.  Thus every phase
point is isolated and there are `2n` phase-residue boundaries.  The
discrepancy is unbounded. ∎

## 3. Consequence and scope controls

The boundary polynomial counts changes under the physical step
`j -> j+A^{-1} (mod L)`, not under `j -> j+1`.  Existing physical run and
run-fibre results therefore cannot directly sparsify it.  The family is a
valid grammar, not an ordinary cycle; actual-owner constraints at the
`A^{-1}` step remain open.  The result does not revive the demoted RL155/RL156
normalization, RL158 resultants, or RL159 joint-SNF route.

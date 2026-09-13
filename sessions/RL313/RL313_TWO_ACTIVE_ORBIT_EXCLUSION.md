# RL313 — exclusion of exactly two active shift-orbits

Date: 2026-09-13
Status: CLOSED RL313 RESULT
Classification: EXACT ANALYTIC ALL-SCALE FULL-D CONSUMER

## 1. Setup

Let a proper balanced shift have

`d=gcd(A,s)`, `n=A/d`, `s=t d`, `gcd(t,n)=1`.

Assume at least one shift-orbit is inactive.  By RL312, after rotating to an
inactive orbit the word is cut into `n` consecutive rows `B_k`, each of length
`d` and common weight `ell0`.

For row `k`, let

`P_k(j)=# ones in the first j row positions`.

At a start in row `k`, column `j`, the length-`s` window contains `t` row
weights with the initial/final partial rows exchanged, so exactly

`G_(k,j)=P_k(j)-P_(k+t)(j)`.

Because `k -> k+t` is transitive, column `j` is inactive iff `P_k(j)` is
constant over all rows.

Put

`X=2^d`, `Y=3^ell0`,
`H=(X^n-Y^n)/(X-Y)`.

As in RL312, `H` is coprime to both 2 and 3.

## 2. Exactly two active columns: complete geometry

Suppose exactly two row columns/cuts are active.

### Adjacent active cuts

If the active cuts are consecutive, all rows agree outside one three-bit
window.  That window has fixed weight 1 or 2.  After removing the common
monomial factor `C=2^u 3^v`, its possible variable numerator alphabet is

`{1,2,4}`

for local weight 1, or

`{5,7,10}`

for local weight 2.

Hence the normalized variable coefficient range is at most 5, in particular
strictly less than `X=2^d`.

### Separated active cuts

If the active cuts are separated, all row variation consists of two disjoint
adjacent swaps `10 <-> 01`.

After removing a common monomial `C=2^u3^v`, every row numerator has form

`q_k=q_base+C(A eps_k+B eta_k)`

with `eps_k,eta_k in {0,1}`,

`A=3^r`, `B=2^v2`,

and the geometry gives

`A<=Y/3 < X/3`,
`B<=X/4`.

Therefore the normalized alphabet diameter is at most

`A+B < X/3+X/4 < X`.

## 3. Small-coefficient cofactor lemma

Grouping the full numerator by equal-length/equal-weight rows gives

`Q_full = q_base H + C S`,

where `S` is the positive-coefficient geometric evaluation of the normalized
row alphabet.

Full-D ownership says `D=(X-Y)H | Q_full`.  Multiplying by `X-Y` and using
`gcd(H,C)=1` gives

`H | S`.

Thus `S=r H` for some integer `r`, or equivalently

`sum_k (a_k-r) X^k Y^(n-1-k)=0`

for normalized coefficients `a_k`.

Because the geometric weights are positive, `r` lies between the minimum and
maximum `a_k`.  Therefore every coefficient `b_k=a_k-r` has

`|b_k| < X`.

Lemma: if `gcd(X,Y)=1`, `|b_k|<X`, and

`sum_k b_k X^k Y^(n-1-k)=0`,

then all `b_k=0`.

Proof: reduce modulo `X`.  Since `Y` is invertible modulo `X`,
`X|b_0`; the strict coefficient bound forces `b_0=0`.  Divide by `X` and
repeat.

Hence all normalized row coefficients are equal, contradicting genuine
variation at the two active cuts.

## 4. Theorem

For a primitive positive full-D cycle and a proper balanced shift in the
inactive branch,

`boxed: exactly two active shift-orbits are impossible.`

Together with RL312's zero/single-orbit exclusions, every surviving inactive
terminal shift has at least three active shift-orbits.

This is an all-scale sparse-support consumer, not a Radius-6 or fixed-radius
grammar.  It does not assert that three or more active orbits are impossible.

## 5. Scope

The portable RL313 verifier exhaustively checks the two-active-cut row
classification and normalized coefficient-range claim for all row lengths
through 10.  The theorem itself is analytic.

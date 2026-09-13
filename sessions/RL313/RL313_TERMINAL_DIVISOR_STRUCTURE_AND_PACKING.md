# RL313 — terminal divisor structure, row packing, and state-floor contraction

Date: 2026-09-13
Status: CLOSED RL313 RESULT
Classification: ANALYTIC THEOREMS + EXACT FINITE ARITHMETIC CERTIFICATE

## 1. Setup

Start from the RL312 inactive-orbit branch for the RL311 balanced shift

`A=ga`, `L=g ell`, `s=ma`, `c=gcd(g,m)`, `d=ac`.

After a genuine cyclic rotation the full primitive cycle word is partitioned into

`n=g/c`

consecutive rows of exact counts

`(d,ell0)=(ac,c ell)`.

Every row boundary is a genuine phase of the same full-D owned integer cycle.  No
local denominator ownership is asserted.

Put

`X=2^d`, `Y=3^ell0`, `D0=X-Y>0`.

For row numerator `q_k` and boundary state `x_k`,

`X x_(k+1) = Y x_k + q_k`.

## 2. Descent depth is at most one

For the descended shift `s*=d=ca`, the expected balanced count is `ell0=c ell`.
At every row boundary the next `d` bits are one complete terminal row, so the
canonical flow for shift `d` is zero on the entire boundary shift-orbit.

In RL311 coordinates the descended multiplier is `m*=c`.  Since `c|g`,

`gcd(g,m*)=gcd(g,c)=c=m*`.

Thus the RL312 divisor map

`T_g(m)=gcd(g,m)`

is idempotent:

`T_g(T_g(m))=T_g(m)`.

If `c<m` there is exactly one strict gap reduction `m -> c`; reapplying the same
inactive-orbit theorem at that scale cannot reduce further.

More generally, for terminal-row-aligned shift `q d`, `1<=q<n`,

`gcd(A,q d)=d gcd(n,q)`.

Every such shift has zero flow at each terminal row boundary.  Its inactive
partition therefore only coarsens the terminal rows by the factor `gcd(n,q)`;
it never refines below `d`.

This closes the "can the same gcd descent iterate indefinitely?" question: no.

## 3. Boundary states are weighted row-numerator averages

Iterating the equal-slope row recurrence around the `n` rows gives, for each
cyclic starting row,

`(X^n-Y^n)x_k = sum_(j=0)^(n-1) X^j Y^(n-1-j) q_(k+j)`,

up to the harmless reversed cyclic indexing convention.

The positive coefficients sum to

`H=(X^n-Y^n)/(X-Y)`.

Hence

`q_min/D0 <= x_k <= q_max/D0`.

Because the full cycle is primitive, the `n` row-boundary states are distinct
integers.  Therefore

`n <= floor(q_max/D0)-ceil(q_min/D0)+1`

and in particular

`q_max-q_min >= (n-1)D0`.

For an arbitrary binary row of length `d`, weight `ell0`, the exact extreme
numerators are

`Q_min = 3^ell0-2^ell0`,

`Q_max = 2^(d-ell0)(3^ell0-2^ell0)`.

Thus every terminal survivor obeys

`(n-1)(2^d-3^ell0)
 <= (2^(d-ell0)-1)(3^ell0-2^ell0)`.

This uses integer boundary ownership and primitivity, not the RL20 whole-block
coboundary.

## 4. Stronger minimum-boundary span theorem

Rotate the row cycle so that `x_0` is the least row-boundary state.  Primitivity
forces both neighboring boundary states to be different from `x_0`, hence

`x_1>=x_0+1`,
`x_(n-1)>=x_0+1`.

The outgoing and incoming row numerators satisfy

`q_0 >= D0 x_0 + X`,

`q_(n-1) <= D0 x_0 - Y`.

Therefore the actual row alphabet must have numerator diameter at least

`boxed: q_max-q_min >= X+Y = 2^d+3^ell0`.

Combining with the universal row-numerator range gives the support-independent
necessary condition

`boxed:
 (2^(d-ell0)-1)(3^ell0-2^ell0)
 >= 2^d+3^ell0.`

## 5. External state-floor contraction

RL310 carries the inherited external minimum-state floor

`R >= 2^71`.

Since every terminal boundary is a genuine cycle state and

`x_k <= Q_max/D0`,

a terminal survivor must satisfy

`2^71 (2^d-3^ell0)
 <= 2^(d-ell0)(3^ell0-2^ell0).`

Also `n>=2` and the active RL311 sector has `lambda<3`, so

`3^ell0 < 2^d < sqrt(3) 3^ell0`.

This interval has multiplicative width `<2`, hence at most one integer `d` for
each `ell0`.

Exact integer enumeration of every admissible pair with `ell0<=115` gives 91
pairs and none reaches the `2^71` floor.  The largest boundary upper bound below
the cutoff is

`(ell0,d)=(111,176)`,
`floor(Q_max/D0)=751281177470410612498`.

The first row-count pair that passes this necessary test is

`boxed: (ell0,d)=(116,184)`

with upper bound

`2804721460384257848662`.

Consequently every terminal survivor satisfies

`boxed: ell0>=116, d>=184`.

At reduced level, writing `(d,ell0)=c(a,ell)` with `gcd(a,ell)=1`, the exact
finite arithmetic check shows no `ell<=16` can reach the state floor under the
same `n>=2`, `lambda<3` restriction.  The first reduced denominator capable of
doing so is

`boxed: (ell,a,c)=(17,27,7)`

giving `(ell0,d)=(119,189)`.

Thus every terminal survivor also satisfies

`boxed: ell>=17`.

## 6. Scope

These are necessary conditions for the inactive/terminal branch.  They do not
close that branch, Gate A, Gate B, or global non-trivial-cycle exclusion.

No endpoint-ratio inheritance after descent is used.
No local denominator ownership is used.
The finite arithmetic is a bounded certificate for the stated cutoffs only; it
is not a proposal to grow a row-weight case search.

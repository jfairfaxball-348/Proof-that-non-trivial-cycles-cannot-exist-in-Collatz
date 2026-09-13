# RL314 cross-era splice, correction, and barrier ledger

Date: 2026-09-13
Status: FROZEN RL314 AUDIT MATERIAL

## 1. Valid terminal inactive-run spacing lemma

In an RL313 terminal equal-row decomposition, write row counts `(d,ell0)`,
`X=2^d`, `Y=3^ell0`, `D0=X-Y`, and let there be `n>1` rows.

Suppose two inactive cuts are separated by a common parity word `W` of length
`H` and weight `r`. For each row-boundary state `x_k`, let `x'_k` be the state
after reading the common word `W`.

Because the same parity word acts on every row,

`2^H x'_k = 3^r x_k + Q_W`

with the same `Q_W`. Subtracting two rows gives

`2^H(x'_k-x'_l)=3^r(x_k-x_l)`.

Since powers of 2 and 3 are coprime,

`2^H | (x_k-x_l)`,
`3^r | (x'_k-x'_l)`.

Both cuts are inactive, so each may serve as an equal-row boundary cut. RL313
therefore bounds the state interval at each cut by the row-numerator range.
Distinctness and residue spacing imply the necessary condition

`(n-1) max(2^H,3^r) (2^d-3^ell0) <= qmax-qmin`.

Using the universal row-numerator range gives the explicit bound

`(n-1) max(2^H,3^r) (2^d-3^ell0)
 <= (2^(d-ell0)-1)(3^ell0-2^ell0)`.

This is a valid theorem-grade consequence of terminal integer ownership plus a
common inactive block.

## 2. Strategic correction

An earlier scratch illustration applied the inequality to
`(d,ell0)=(184,116)` with `n=10000`.

That was invalid because terminal survivors are still in the inherited
`lambda<3` sector:

`(2^d/3^ell0)^n < 3`.

For `(184,116)` this restricts `n` to a small value.

After restoring this condition, the spacing lemma does not universally force a
support lower bound stronger than RL313's already-proved exclusion of support
0, 1, and 2.

Therefore the lemma is preserved but its parent classification is corrected to

`PARENT_DIFFICULTY_DELTA = LATERAL`.

No claim that it forces unbounded fragmentation is promoted.

## 3. Historical overlap

RL251 already identified the rigorous useful "Gabriel's horn" mechanism as
physical multi-occupancy packing:

multiple genuine owned states in one congruence fibre force a minimum physical
span.

The RL314 lemma is a new application of that principle to RL313 terminal rows,
not a new project-level resource.

The same historical missing ingredient remains:
force enough owned occurrences/depth/fragmentation in the same resource to
exceed an independent upper budget.

## 4. Support-three no-carry barrier

RL313's exactly-two-active proof reduces full-D cofactor divisibility to a
geometric polynomial relation with every normalized coefficient of absolute
value `<X=2^d`. Modulo-X descent then forces all coefficients to vanish.

For three active cuts, natural fixed-weight row families permit normalized
numerator alphabets whose diameter exceeds `X` in the surviving large terminal
regime. Hence the decisive no-carry hypothesis fails.

This does not prove that support three is possible under full-D ownership.
It proves only that the RL313 two-active argument does not extend mechanically.

A small finite scratch check found no cofactor survivor at small row lengths.
This is evidence only and is NOT promoted as an all-scale theorem.

## 5. Controlled-branch gauge normalization barrier

For the RL311 controlled branch, the integer rescaling

`S_j = 3^(h-E_j) x_(ja)`

turns each gcd-block transition into a constant-slope integer recurrence.

This is algebraically valid but does not add an independent constraint:
its 3-adic valuation staircase reconstructs the chronological odd-count data
already present in the block word.

Therefore recurrence-only gauge normalization is not an acceptable RL315
success criterion.

## 6. Binding use in successor selection

The spacing lemma may be reused later as a terminal consumer, but RL315 should
not continue a support-by-support grammar.

The exact preferred successor remains:
use genuinely full-D/integer information to eliminate the RL311 controlled
branch `g<=h+1` by forcing a repeated gcd-block level.

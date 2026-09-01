# RL228 — dyadic bulk/fringe decomposition and endpoint scaling barrier

Date: 2026-09-01.

**Classification: exact analytic recurrence lemmas + exact combinatorial state certificate + scoped route barrier.**

All statements remain conditional on the inherited arithmetic candidate bridge. They do not manufacture physical H21 occurrences.

## 1. Incoming recurrence

RL226 gives the exact phase-36+ normal form

`k=r+2^m t`,  `y_i=u_i t+v_i`,

with `u_i=3^(i-36)U_36` and

`h_i=19+b(i)-b(36)-m`.

Define `E_i:=19+b(i)-b(36)`, so live states satisfy `h_i=E_i-m>=0`.

For e=4 the finite root window is

`I=[15,106,005,985,18,969,385,559]`,

of length `N=3,863,379,575`.

## 2. Exact interval bulk/fringe lemma

For any residue `r mod 2^m`, write `N=q2^m+s`, `0<=s<2^m`. Split the interval into `q` complete blocks of `2^m` consecutive integers plus a remainder of length `s`. Each complete block contains every residue exactly once; the remainder contains each residue at most once. Therefore

`#(I ∩ {k≡r mod 2^m}) = q + epsilon(r)`, `epsilon(r)∈{0,1}`.

This is exact. The first term is a residue-independent bulk; the second is pure endpoint incidence.

## 3. Common failure modulus

At phase `i`, the next admissible valuation cap is

`cap=b(i+1)-b(i)+h_i=E_(i+1)-m`.

Because RL226 proves `v2(u_i)=1` and odd intercept, the failure event `a>cap` is exactly one extension class modulo `2^cap` in the local variable `t`. The parent already fixes `m` low bits of `k`, so every failure subcylinder has total precision

`m+cap=E_(i+1)`.

Hence all transition-`i` failure classes share the same modulus `2^E_(i+1)`. Distinct live parents are disjoint, so their failure residues at that modulus are distinct.

Applying the interval lemma gives the exact identity

`F_i=floor(N/2^E_(i+1)) S_i + R_i`,

where `S_i` is the live-state count and `R_i` is the endpoint-remainder incidence count among the distinct failure residues.

## 4. The e=4 boundary

The inherited envelope gives

`E_43=30`, `E_44=31`, `E_45=33`.

Because `N>2^31`, every residue class modulo `2^m` with `m<=31` occurs in the e=4 window. Therefore every admissible phase-44 valuation-history cylinder is nonempty in the finite window.

Let `c_i(m)` count phase-`i` states of cumulative precision `m`. Since each exact valuation increment is a positive integer and the only height condition is `m<=E_i`, the endpoint-independent recurrence is

`c_(i+1)(m') = sum_{m<m'} c_i(m)`, for `m'<=E_(i+1)`,

with `c_36(0)=1`.

It gives exact state totals:

`1,20,230,1770,12395,65524,361277,1906336,7743281`

for phases 36 through 44 respectively. The first eight reproduce RL226; phase 44 has **7,743,281** live cylinders.

Now `2^E_45=2^33=8,589,934,592>N`. Thus

`floor(N/2^33)=0`,

and the exact transition-44 identity is simply

`F_44=R_44`.

The uniform dyadic bulk has vanished. Any exact transition-44 count must determine which of the millions of distinct high-modulus failure residues actually land in the finite endpoint window, unless some new algebraic theorem aggregates those residues.

## 5. Same-cardinality states are not future-equivalent

A cardinality-only endpoint summary does not repair this.

Take the phase-44 singleton cylinder with residue `1,871,163,824 mod 2^31`. Its unique window representative is `k=16,903,549,360`. Direct replay from `y_36=U_36 k+V_36` gives valuations

`[20,2,1,2,1,2,1,2]`

through transitions 36..43, so cumulative precision is 31 and height is 0 at phase 44. The next cap is 2, while the transition-44 valuation is 1: it survives.

Take instead residue `59,224,496 mod 2^31`. Its unique representative is `k=17,239,093,680`, with valuations

`[20,2,1,2,1,1,3,1]`

through transitions 36..43, again cumulative precision 31 and height 0. Its transition-44 valuation is 4, so it fails the same cap 2.

Both parent cylinders have current cardinality 1. Therefore `(phase,m,h,current_count)` is not future-exact.

## 6. Route conclusion

The target asked for either a reusable family exhaustion engine or a decisive exact scaling barrier. The bulk/fringe theorem supplies a reusable description, but at the e=4 stress-test boundary it demonstrates why the present route ceases to be uniform: its bulk term becomes zero and exact continuation is endpoint incidence over millions of states.

This is not an impossibility theorem for all future compressors. It is a decisive barrier for the **current candidate-coupled dyadic-cylinder / endpoint-oblivious aggregation route**. Continuing to transition 44/45 by enumerating endpoint hits would violate the target's explicit pivot rule.

RL229 is therefore assigned to the **physical H21 incidence and exhaustive charge bridge**.

No e=4 rank deletion is claimed; the certified survivor count remains the RL226 count through transition 43.

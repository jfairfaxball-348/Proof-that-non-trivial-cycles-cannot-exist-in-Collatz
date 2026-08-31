# RL195 owned local realizability and the odd-modulus barrier

Date: 2026-08-31. RL195 independently reviewed local theorem and certificate.
Incoming handover RL194; current incoming job RL195.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
The parent established the fresh incoming gate before this bounded task.

## Result and precise scope

Every accepted path of the inherited RL194 depth-3 parity graph is realized
by infinitely many pairs of **local positive odd accelerated trajectories**
with the exact initial owned numerator `C=3^37`, the prescribed local height
data, and all prescribed exact exponents. This is a realization theorem
only in the explicitly uncoupled local relaxation below. It constructs
neither a cycle nor a physical high-branch terminal or p-separated pair.

All 42 initial ordered unequal height pairs of maximum21, and all paths
through the common three-transition word212, are covered. Adding any
compatible finite odd-modulus congruence on the initial owned affine line
cannot eliminate a path: its dyadic seed class can be combined with that
congruence by the elementary coprime-modulus construction. In particular,
initial 3-adic congruences alone, if compatible with that affine line, cannot
strengthen this particular post-terminal local filter.

This is stronger than saying that the graph fails to exclude an initial
pair. State merging loses no cross-step odd-state consistency: **every
accepted path** has local integer witnesses. The missing global conditions
are explicitly listed in Section6.

## 1. Incoming definitions and the local relaxation

The branch qualification of the intended physical application remains
`(37,0,23,-1)`. An ordinary terminal has

`(h,hp)=(21,j)` or `(j,21)`, `0<=j<=20`, and `C0=3^37`.

For positive odd integers X and Z, put `g=h-hp`,
`eX=max(-g,0)`, `eZ=max(g,0)`. The exact owned line is

`2^eZ Z - 2^eX X = C0`.

The initial local parameter is `t=Z` if g>=0, with `X=2^g t-C0`,
or `t=X` if g<0, with `Z=2^(-g)t+C0`.

The local relaxation asks only for two finite sequences of positive odd
integers satisfying

`3X_j+1=2^a_j X_(j+1)`, `3Z_j+1=2^b_j Z_(j+1)`,

with exact valuations `a_j,b_j>=1`, and the prescribed nonnegative heights

`h_(j+1)=h_j+c_j-a_j`, `hp_(j+1)=hp_j+c_j-b_j`.

Both source arms have `c_0,c_1,c_2=2,1,2`, inherited as a gap-free ordinary,
common-mechanical statement on a superset of the current extremal rank
core. We do not extend that word, change its rank scope, or certify a fourth
transition. The two trajectories are not required to be segments of the
same global orbit.

The inherited graph state is `(h_j,hp_j,C_j)`. Its one-step numerator is

`N=3C_j+2^g_j-1` if g_j>=0;

`N=3C_j+1-2^(-g_j)` if g_j<0.

For proposed exponents a,b, put
`u=max(-g_j,0)+a`, `v=max(g_j,0)+b`.
The graph accepts exactly when its height caps hold and

- if u!=v, `v2(N)=min(u,v)`;
- if u=v, `v2(N)>u`.

Its successor numerator is `C_(j+1)=N/2^min(u,v)`.
All inherited graph numerators in the certified three transitions are
positive. Their parity is odd for unequal successor heights and even for
equal successor heights.

## 2. Exact seed class for one finite acceleration word

For a positive-integer word `a_0,...,a_(n-1)`, let

`A_j=sum_(k<j)a_k`, `S_0=0`,
`S_(j+1)=3S_j+2^A_j`.

Induction gives

`X_j=(3^j X_0+S_j)/2^A_j`.

All the specified valuations hold exactly if and only if

`X_0 == (2^A_n-S_n) * (3^n)^(-1) (mod 2^(A_n+1))`.        (1)

This residue is odd. Necessity follows from X_n being odd. For sufficiency,
the endpoint numerator has valuation A_n. Going backwards,

`3*(3^j X_0+S_j)=(3^(j+1)X_0+S_(j+1))-2^A_j`.

Since `A_(j+1)>=A_j+1`, the right side has valuation exactly A_j.
Division by odd3 preserves that valuation. Iteration proves that each X_j
is odd, and the displayed recurrence then proves each exact acceleration.
For X_0 positive, every forward state is positive. The same argument holds
for the b-word of the Z arm, with sums B_j and constants T_j.

This finite-word lemma is analytic; the actual physical word and finite
enumeration in this result still stop after exactly three transitions.

## 3. Why the parity graph is sufficient for every local path

Fix an accepted path of length n and its exponent words. At its endpoint
put

`u=eX+A_n`, `v=eZ+B_n`, `m=min(u,v)`,

`D_n=3^n C0 + 2^eZ T_n - 2^eX S_n`.

The normalized graph recurrence gives, by induction,

`g_n=v-u`, `D_n=2^m C_n`.                              (2)

For completeness, at intermediate j,

`D_(j+1)=3D_j+2^(eZ+B_j)-2^(eX+A_j)`.

Factoring `2^min(eX+A_j,eZ+B_j)` gives exactly the inherited one-step
numerator rule, and the next minimum power grows by the graph's local
normalizing exponent. This proves (2) without choosing any odd states.

Let `rX (mod 2^(A_n+1))` and `rZ (mod 2^(B_n+1))` be the exact word seed
classes in (1). The owned line and both seed classes are simultaneously
solvable precisely when

`C0 + 2^eX rX - 2^eZ rZ == 0 (mod 2^(m+1))`.          (3)

Indeed, varying the two seed integers changes their owned difference by
integer combinations of `2^(u+1)` and `2^(v+1)`. Their greatest common
divisor is `2^(m+1)`, proving necessity and sufficiency of (3).

Multiplication by odd `3^n` transforms the left side of (3), modulo its
modulus, into

`D_n + 2^u - 2^v`.

If u!=v, the accepted graph has odd C_n; by (2), D_n is `2^m` modulo
`2^(m+1)`, and `2^u-2^v` has the same residue. Their sum is zero.
If u=v, the graph has even C_n, so D_n is already zero modulo `2^(m+1)`
and the other terms cancel exactly. Thus (3) always holds.

Since one of eX,eZ is zero, parametrizing the owned line by t reduces these
compatible seed conditions to a single residue class

`t == r (mod 2^M)`                                    (4)

with odd r. This is a whole class, not an isolated solution. Explicitly,
for g>=0 combine

`t==rZ (mod 2^(B_n+1))`,
`2^g t==C0+rX (mod 2^(A_n+1))`.

Divide the latter congruence by its power of two when it imposes a condition,
then take the stronger of the two compatible dyadic classes. For g<0,
combine the corresponding conditions with X as the parameter. This is the
construction implemented by the verifier.

Taking sufficiently large positive members of (4) makes both X_0 and Z_0
positive. Equation(1) then supplies two exact positive odd trajectories.
The ordinary owned algebra gives the same C_j at every intermediate state,
and the prescribed exponent caps give exactly the recorded nonnegative
height values. Conversely, any such local trajectories necessarily satisfy
the graph valuation rules. Hence the accepted paths are exactly the locally
realizable paths in this defined relaxation.

## 4. Odd-modulus and size constraints do not break this local sufficiency

Let an additional initial condition, after restricting to the owned affine
line, allow the residue `t==s (mod D)` for any odd positive D. Because
`gcd(2^M,D)=1`, solving

`t=r+2^M k`, `k==(s-r)*(2^M)^(-1) (mod D)`

combines it with (4). The solutions form an infinite arithmetic progression
of common difference `2^M D`. Arbitrarily large solutions exist, so any
fixed lower bounds on the two initial states, or on all states in these
finite trajectories, can also be satisfied. Every finite trajectory value
is an affine function of t with positive slope.

For multiple odd-modulus initial conditions, this conclusion applies when
their restriction to the owned line is nonempty; an internally inconsistent
odd-modulus system is not claimed repairable. Conditions involving other
global vertices or path-dependent global identifications are not reduced
to initial congruences without a separate proof.

In particular, every compatible class modulo `3^s` can be adjoined. Since
`C0=3^37` is divisible by3, choosing t nonzero modulo3 makes both initial
odd states nonzero modulo3. Every later odd state is automatically nonzero
modulo3 because `2^a X'=3X+1`. The finite certificate uses the stronger
specific seed condition `t==1 (mod 3^5)` on every tested path.

Thus there is no additional obstruction from composing these finite
accelerated trajectories, from positivity or a fixed lower size threshold,
or from compatible initial 3-adic congruences alone. The result does not
say that every proposed global 3-adic condition is compatible with the
owned line or that stronger globally coupled congruences are powerless.

## 5. Exact finite replay and witnesses

Run this packaged verifier from the package root:

`python3 verification/verify_rl195_owned_local_realizability.py`

It independently implements the integer necessary transition rule, checks
the inherited complete merged-state counts, then retains every path without
merging exponent histories. It constructs each dyadic seed class, adjoins
`t==1 (mod 3^5)`, selects positive odd seeds, and checks exact valuations,
heights and owned numerator at every step. A second member of every seed
family is also replayed. All arithmetic is integral and deterministic.

An independent research-stage review found that the general seed helper
unconditionally rejected initial multiples of3 despite allowing arbitrary
compatible odd-modulus classes. That assertion was repaired, and supplied
odd residues are now normalized modulo their modulus. An additional336
bounded helper regressions cover all42 roots with eight modulus/residue
inputs, including t=0 modulo3, modulus1, and noncanonical representatives.
The original complete t=1 modulo3^5 replay and its digest are unchanged.
This is a verifier-interface repair, not an inherited mathematical demotion.

| Depth | Merged states | Edges from merged states | Full paths |
| --- | ---: | ---: | ---: |
| 1 | 540 | 540 | 540 |
| 2 | 4,202 | 4,517 | 4,517 |
| 3 | 25,417 | 30,977 | 34,039 |

All 42 initial pairs and all44 four-source sign patterns have witnesses in
the local relaxation. Different paths may merge to the same graph state;
the full-path count intentionally exceeds the final merged-edge count.
No graph state, edge or path count is a physical terminal population.

Deterministic digest of the complete ordered witness replay:

`34837dc796e7637e7044c1ad3393a31a2baef7129ea9b9154d7775928810277f`.

For the two inherited immediate-zero interfaces, two illustrative initial
local witnesses chosen by the verifier are:

- `(h,hp)=(20,21)`: `(X,Z)=(487,450283905890998337)`, exponents `(1,2)`;
- `(h,hp)=(21,18)`: `(X,Z)=(3653,56285488236375127)`, exponents `(4,1)`.

These examples are not full-depth witnesses by themselves and are not
physical orbit constructions. The verifier's complete depth-3 replay,
rather than these two examples, certifies all the stated full paths.

## 6. Barrier and still-missing physical conditions

The local relaxation does not impose:

- `Z_0` is the state reached after the actual p successive accelerated
  steps from `X_0`, where `p=65470613321`;
- closure after `L=137528045312` steps with the actual total exponent A;
- one shared global height word, canonical anchor `h_0=0`, fixed mechanical
  phases, all p-edge relations and the special carry;
- the complete extremal tau=37 zero-defect prehistory, canonical start
  location, corrected-K bounds, occupation/window moments, or H21 ownership.

The integer witnesses cannot be inserted into a physical high-branch word
without proving those missing compatibilities. The theorem is therefore a
precise method barrier: a consumer of this depth-3 graph must add information
beyond local positive-odd forward consistency and compatible initial
odd-modulus congruences. A global p-edge coupling, location, common-prehistory
constraint, or another genuinely additional physical restriction remains
open; no such restriction is discharged here.

## 7. Classification, coverage and provenance

- **Proved analytic mathematics within the defined relaxation:** the exact
  finite-word seed class, equivalence between accepted paths and local
  positive-odd realization, infinite families, and compatible odd-modulus
  augmentation, all within the defined relaxation.
- **Exact finite certificate within the defined relaxation:** every path from
  all42 initial pairs at depths1,2,3 under212, including34,039 final paths
  and44 sign patterns; exact witness replay and inherited graph counts.
- **Method barrier:** the strengthened local
  consistency filter cannot exclude either common-word atom or any initial
  pair. This is not a barrier to genuinely additional global congruences.
- **Open:** global physical realization/exclusion, p/L coupling, phase and
  prehistory constraints, depth>=4 physical word/certificate, H21 incidence,
  all branch and global conclusions.

Uncovered computational range: no transition depth>=4 is computed or
certified. No chronological-speed range is extended. There is no unfinished
partial scan. No inherited result or mathematical classification is changed.

Only current authoritative sources were used:
`RL195_PHYSICAL_WINDOW_TRANSPORT_AND_ZERO_HEIGHT_INCIDENCE_TARGET.md`,
`RL194_RANK_ORDER_WEIGHTED_SPEED_HEIGHT_OCCUPATION_AND_OWNED_PREFIX_2026-08-31.md`,
the RL194 proof/correction ledgers,
`proofs/RL194_OWNED_PREFIX_INTERFACE.md`, and its named verifier. No broad
history, catalogue or external mathematical source was needed.

Completed independent red team: verified the endpoint-to-prefix sufficiency
in (1), the modulo `2^(m+1)` normalization/sign in (3), positivity and odd-
modulus augmentation, and that no physical p-edge/cycle claim is inferred.
The helper finding is resolved; see reviews/OWNED_LOCAL_RED_TEAM.md.

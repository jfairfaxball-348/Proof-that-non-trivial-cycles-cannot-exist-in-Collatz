# RL195 zero geometry — independent red-team review

Date: 2026-08-31.  **PASS — NOT PROMOTED.**
Reviewer: independent physical-window/denominator subagent.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.

No blocking mathematical, coverage, or scope finding.  No source file,
authority, session, Git object or remote ref was changed by this review.

## 1. Exact reviewed artifacts

- `.rl-work/RL195/agent_zero_geometry/ZERO_GEOMETRY.md`
  SHA256 `44b45350557bce9972c6d9fa1f3cf2258068c806fe53809bb1f26a2e1bb1cf71`.
- `.rl-work/RL195/agent_zero_geometry/verify_zero_geometry.py`
  SHA256 `d9b9db907e6f5d91e06ead5a1bf12a27e4113b21365650661017610103abafdd`.

Both files were read in full.  The submitted verifier ran to completion and
returned PASS.  Independent arithmetic additionally reconstructed the
actual rank-cell partitions and both relaxed witnesses without importing
the submitted verifier, and tested all four binary doublet choices and
31 rational cardinality-dual thresholds.

## 2. Disjoint c=1 geometry and canonical coefficient exception

PASS.  Rank advances by B modulo L, so `[0,R)` maps bijectively onto
`[B,L)` with disjoint source and target sets.  The physical recurrence
`h_(i+1)=h_i+c_i-a_i`, `a_i>=1`, is universal, including mechanical
switches, the p-shift carry source, and the period boundary.  At c=1 it
gives `h_(i+1)<=h_i`; therefore a zero source has a zero successor.

The only possible canonical coefficient changes for a one-step pair are
at phases0, p-1 or L-1.  The latter two have ranks R+1 and R respectively,
outside the c=1 source interval.  Phase0 is explicitly separated because
there is no d_0.  Thus `d_(r+B)=2d_r/3` for every `1<=r<R`, and the fixed
pair contributes `d_B=2theta/3`, with `h_0=h_1=0`, `J_0=1`.

The three permitted binary selections on an ordinary c=1 pair are
`(0,0),(0,1),(1,1)`.  Their exact cardinality-dual maximum equals
`max(0,5d_r/3-2t)` for every t>=0.  The proof properly compares the
high-only case both when its excess is positive and when it is not.
It does not replace the special fixed pair by an ordinary free pair.

## 3. Disjoint c=2 geometry and zero-weight capacity

PASS.  First vertices `[2R,L)` map to second vertices `[R,B)` by
`r -> r-R`; singleton c=2 ranks are `[B,2R)`.  These pieces are disjoint
and cover all c=2 vertices.  Since `R<B<2R` and `L<3R`, there are no
mechanical words11 or222, including cyclic seams.

Neither coefficient-change source rank R nor R+1 is in `[2R,L)`, so
`d_(r-R)=4d_r/3` holds on every selected doublet, including the one whose
first source is the p-shift carry rank L-1.  The binary inequality
`d_r*u+d_(r-R)*v <= d_(r-R)+d_r*u*v` is valid in all four cases.

Together with c=1 propagation this gives exactly

`Z0 <= C + sum_(1<=r<R)d_r J_(I(r))`

`        + sum_(2R<=r<L)d_r J_(I(r))`.

There is no multiple charging: the selected source sets are disjoint and
neither contains phase0.  All base weights form the one interval `[R,2R)`.
The endpoint identities `I(R-1)=z-1`, `I(2R-1)=z-2`, and mechanical bits
`c_(z-2),c_(z-1)=2,1` prove the exact capacity

`C=w_(R-1)-w_(2R-1)=3lambda*alpha/16=3(1+theta)/16`.

The use of strict `d_r<theta` is also correct: `J=1` gives only `Z0<=C`.
Once an independently certified physical `M>C` is imposed, necessarily
J>1, and `M<=Z0<C+theta*(J-1)` is justified.  This component properly
leaves the actual numerical J floor to the parent rather than assigning
an unchecked integer rounding.

## 4. Gap-free actual-constant partition checks

PASS.  Every discontinuity of a mechanical indicator at offsets0,1,2 is
the inverse image of rank0 or rankR.  Splitting at all these preimages
therefore proves constancy throughout each cell, not merely at sampled
endpoints.  The four mechanical word populations independently obtained
are:

| Word | Number of canonical source ranks |
| --- | ---: |
| 121 | 33709842709 |
| 122 | 23369453298 |
| 212 | 57079296007 |
| 221 | 23369453298 |

Their sum is exactly L=137528045312.  The count of c=1 sources is R and
the count of initial22 doublets is L-2R.

For the one-adjacent-edge witness, all source/target zero-indicator
boundaries and the source mechanical boundary were independently pulled
back to rank space.  The complete half-open partition was:

`[0,1)`, `[1,33709842709)`, `[33709842709,57079296007)`,
`[57079296007,57079296008)`, `[57079296008,114158592014)`,
`[114158592014,114158592015)`, `[114158592015,137528045312)`.

These seven cells are disjoint and cover every rank.  Their exact weighted
counts are `N0=57079296007`, `J=1`, and `sum a_i=217976794617=A`.
All a_i are positive.  The submitted generator includes every indicator
boundary, so its equal-endpoint checks are supported by a gap-free
piecewise-constant proof.

## 5. Actual-constant relaxed countermodels and the exact-moment boundary

PASS WITH THE STATED RELAXATION SCOPE (no correction requested).

The first witness has zero ranks `{0} union [R+1,2R)`.  Its only c=1 zero
source is rank0, whose target rankB is also zero.  Every other zero source
maps to a positive-height vertex.  This proves J=1 and excludes all
height-zero triples, while N0 exceeds the incoming count floor.  Its exact
zero-weight sum is `Z0=C-d_R<C`, so it explicitly fails every physical
moment lower bound M>C.  It is not a counterexample to the new physical
incidence theorem.

The second witness has positive height exactly on the p phases `[2,p+2)`.
Its sole increase is at source1 with c_1=2, so a_1=1; its sole decrease is
at p+1 and is always legal.  Every other source has a_i=c_i>=1.  The two
changes cancel in the full exponent sum.  The complete temporal partition
at `0,1,2,p+1,p+2,L` proves N0=L-p=72057431991 and an entirely zero-free
p-window, without enumerating L phases.  This is analytic all-phase
coverage, not a purported rank scan.  In particular this witness also has
h_p=1 and does not satisfy the incoming h_p=0 anchoring.

Section5 explicitly omits the exact fixed-K0 moment, positive odd-orbit
realization, early G signature and terminal constraints from both witness
definitions.  The second witness is not claimed to have passed that moment;
the first is explicitly ruled out by it through M>C.  Therefore neither
conflicts with the separate denominator-equivalence theorem: for a complete
admissible height word, an **exact** dyadic normalized K0 would force odd
integrality, but a necessary N0 floor or other loose moment inequalities
would not.  This distinction is preserved correctly.

## 6. Verifier result and classification checks

Command run:

`python3 .rl-work/RL195/agent_zero_geometry/verify_zero_geometry.py`

Output matched all asserted values:4 mechanical word cells,7 one-edge
witness cells, both actual N0 values and J=1,256 bounded toy arrays with
7 admissible arrays, and6 submitted local-dual thresholds.  Independent
binary/dual checks and independently generated complete cells also passed.

The toy `(A,L)=(8,5)` regression is not being promoted as any actual-branch
phase coverage.  The actual countermodel certificates concern only the
explicit height/count relaxation.  No rank cardinality is treated as a
physical terminal count, no chronological zero-zero edge as an H21 owned
incidence, and no cycle realization or branch/global closure is asserted.
The review found no inherited contradiction or required demotion.

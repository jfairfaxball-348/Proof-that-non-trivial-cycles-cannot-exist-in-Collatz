# RL195 — mechanical zero propagation and chronological edge geometry

Date: 2026-08-31. RL195 independently reviewed closeout proof.
Incoming job RL195, verified handover RL194.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
The parent established the fresh incoming start gate.

All physical conclusions below are conditional on the sole high branch
`(37,0,23,-1)`. No terminal, odd orbit or cycle is constructed. The two
explicit countermodels in section 5 are to a stated height-only relaxation,
not to the full incoming authority or its moment identity.

## 1. Definitions and scope of the physical input

Use the incoming constants

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`R=L-B=57079296007`, `p=65470613321`, `u0=103768467013`,
`Ap-u0 L=1`, `z=L-p=72057431991`.

Thus `R<B<2R`, `L=B+R`, and `B-R=23369453298`. Canonical phase i has
rank `r_i=iB mod L` and inverse `I(r)=pr mod L`. The mechanical bit is

`c_i=floor(A(i+1)/L)-floor(Ai/L)`.

It equals 1 for `0<=r_i<R` and 2 for `R<=r_i<L`. Rank advances by B
modulo L in one chronological step. All heights are periodically indexed.

In addition to nonnegative integral heights and `h_0=0`, use the actual
accelerated height recurrence

`h_(i+1)=h_i+c_i-a_i`, where `a_i=v2(3y_i+1)>=1`.

This is the same physical height/exponent rule used in the incoming owned
prefix proof. For the implications below, only the displayed recurrence,
integrality and nonnegativity are needed. The odd-state recurrence and
positivity are not discarded from physical claims: they simply are not
needed for these necessary consequences.

Write `x_i=1` when `h_i=0`, and `x_i=0` otherwise. Let

`J_i=x_i*x_(i+1)`, `J=sum_(0<=i<L)J_i`.

J counts actual chronological edges with two height-zero endpoints. It is
not an ordinary-p-edge defect count, zero-defect-run count, terminal count,
H21 incidence or ownership multiplicity.

The RL194 weights are `rho_i=2^floor(Ai/L)/3^i`,
`w_r=rho_(I(r))`, `d_r=w_(r-1)-w_r` for `1<=r<L`.
With `alpha=3^p/2^u0`, `lambda=2^A/3^L`,
`eta=alpha-1`, `theta=lambda*alpha-1`, they satisfy

`d_r=theta*rho_(I(r))` for `0<I(r)<p`,

`d_r=eta*rho_(I(r))` for `p<=I(r)<L`,

and `0<d_r<theta`. There is no `d_0` in the rank moment.

## 2. Disjoint mechanical-one matching, including its exception

For `0<=r<R`, the one-step successor rank is `r+B` in `[B,L)`.
These R source/target pairs are disjoint: the low and high intervals are
disjoint and the map is a bijection between them. The middle interval
`[R,B)` is outside this matching.

At any such source, c=1 and a>=1 give

`h_(I(r+B))<=h_(I(r))`.

Consequently every height sublevel propagates across this edge. In
particular, `x_(I(r))<=x_(I(r+B))`, and

`J_(I(r))=x_(I(r))` for `0<=r<R`.                 (1)

The two canonical coefficient-boundary predecessor ranks are

`r_(p-1)=R+1`, `r_(L-1)=R`.

Both have c=2. For `1<=r<R`, the source phase is neither 0, p-1 nor L-1;
it and its successor therefore lie in the same coefficient class of d.
Since c=1 gives `rho_(i+1)=(2/3)rho_i`, one gets the exact identity

`d_(r+B)=(2/3)d_r`, `1<=r<R`.                    (2)

The exceptional pair r=0 must not be assigned a fictional d_0. Here
`h_0=0` and c_0=1 force `h_1=0`, `a_0=1`, and `J_0=1`. Its target
rank is B, `rho_1=2/3`, and

`d_B=2theta/3`.                                  (3)

For a zero-weight/cardinality dual with threshold t>=0, an ordinary pair's
legal zero selections have excess weights

`0`, `d_(r+B)-t`, `d_r+d_(r+B)-2t`.

The high-only option never exceeds the maximum of the other two: if its
excess is positive then t<d_(r+B)<d_r and the double selection is better;
otherwise zero is better. Thus its dual contribution is exactly

`max(0,5d_r/3-2t)`.

This is a local optimization identity, not by itself a new numerical
occupation bound. The fixed pair (0,B) is handled separately by (3).

## 3. Disjoint mechanical-two doublets

All c=2 sources split into the following disjoint pieces:

- first vertices of two-step c=2 runs: ranks `[2R,L)`;
- their successors: ranks `[R,B)`, paired by `r -> r-R`;
- singleton c=2 vertices: ranks `[B,2R)`.

Indeed, for r>=R the successor rank is r-R; it is still at least R
exactly when r>=2R. Its next successor is r-2R, which is less than R
because `L<3R`. A c=1 source always has a c=2 successor because B>R.
Hence there are no mechanical words 11 or 222, and the listed c=2
doublets are disjoint, including around the canonical seam.

Neither coefficient-boundary predecessor rank R nor R+1 lies in
`[2R,L)`. On every doublet the coefficient class is unchanged and c=2,
so the exact weight relation is

`d_(r-R)=(4/3)d_r`, `2R<=r<L`.                   (4)

In particular the second vertex has the larger d weight.

## 4. Weighted zero capacity in terms of chronological zero-zero edges

Set

`Z0=sum_(1<=r<L)d_r*x_(I(r))`,

`C=sum_(R<=r<2R)d_r`.

For a c=2 doublet, put `u=x_(I(r))`, `v=x_(I(r-R))`. For binary u,v,
(4) implies

`d_r*u+d_(r-R)*v <= d_(r-R)+d_r*u*v`.

Sum this inequality over all disjoint doublets, bound a singleton by its
full weight, and use (1) on the c=1 sources. The base weights are exactly
the interval `[R,2R)`, giving the complete necessary inequality

`Z0 <= C + sum_(1<=r<R)d_r*J_(I(r))`

`          + sum_(2R<=r<L)d_r*J_(I(r))`.           (5)

No physical vertices are multiply charged: the first extra sum uses
c=1 sources and the second uses the first source of a c=2 doublet. Both
sets exclude phase zero. All other chronological J edges may be ignored
in this upper bound.

The base capacity has a short exact value. The inverse-rank endpoints are
`I(R-1)=z-1` and `I(2R-1)=z-2`. The mechanical transitions at z-2,z-1
have bits 2,1, and `rho_z=lambda*alpha/2`. Hence

`w_(R-1)=3lambda*alpha/4`,

`w_(2R-1)=9lambda*alpha/16`,

`C=w_(R-1)-w_(2R-1)=3lambda*alpha/16`

` =3(1+theta)/16`.                               (6)

Since J_0=1 and every included d is strictly less than theta, (5) implies
`Z0<=C+theta*(J-1)`. If an independently proved physical lower bound
`Z0>=M` has `M>C`, then J>1 and strictness is justified:

`M<=Z0<C+theta*(J-1)`, so `J-1>(M-C)/theta`.       (7)

The strict step is not asserted before M>C: at J=1, (5) only gives
Z0<=C. RL194 supplies `M=2F-3rho_z+1`,
`F=3(lambda-1)2^37`; the separately reviewed moment-adjacency proof certifies
the numerical consequence of (7). This component does not assign an
unchecked numeric J floor. J here is the root report's J00, not the branch
parameter J=23. No H21 or zero-defect-run inference is made from it.

## 5. Sharp barriers for the height-only/count-only relaxation

A height-admissible relaxation retains the actual A,L,c, integral periodic
h>=0, h_0=0, and formal integral `a_i=h_i+c_i-h_(i+1)>=1`. It does
not impose a positive odd-state solution, the physical fixed-K0 moment,
the early G signature, or the terminal constraints. Every physical word
satisfies these retained conditions; the converse is not claimed.

### 5.1 Only one adjacent-zero edge despite the incoming N0 floor

Define zero ranks by

`Z={0} union [R+1,2R-1]`,

and set h=0 there, h=1 elsewhere. Then `N0=R=57079296007`, which exceeds
the incoming floor43742681439. The only zero at a c=1 source is phase0;
its successor rank B is also in Z. Thus every zero-to-positive transition
has c=2, so all formal a_i are at least1. Periodicity gives
`sum_i a_i=sum_i c_i=A` without any independent valuation assumption.

Every zero source of rank `[R+1,2R-1]` has successor rank `[1,R-1]`,
which is nonzero. The zero at rank0 has successor B, which is zero.
Therefore **J=1 exactly**, the single edge0->1 already forced by anchoring.
No triple of height-zero vertices occurs. This proves that the recurrence,
anchoring and incoming N0 lower bound alone cannot force more than one
chronological adjacent-zero edge.

It is not a barrier to (7): this witness has `Z0=C-d_R<C` and so fails
any physical moment lower bound M>C. This precisely identifies the extra
information used by the parent's physical incidence argument.

### 5.2 A zero-free p-window with even larger zero occupation

Define h_i=1 for `2<=i<=p+1`, and h_i=0 at all other canonical phases.
The sole height increase is the step1->2, where c_1=2; the height decrease
at p+1 is always allowed. At all other steps a_i=c_i. Thus this is again
a height-admissible relaxation with `h_0=h_1=0` and

`N0=L-p=72057431991 > 43742681439`.

Nevertheless the full chronological p-window `[2,p+2)` contains no
height-zero vertex. Thus bare occupation, even with the actual mechanical
height recurrence, does not force a zero in every p-window. It does not
follow that such a window is compatible with the full moment, anchored
early signature, atom criteria, odd-state recurrence, or physical cycles.

## 6. Verification and classification

Run `python3 verification/verify_rl195_zero_geometry.py` from the package root.

The verifier checks exact constants and all actual rank cells needed for
the countermodel and mechanical local-word partition, without enumerating
L phases. It exhausts all256 height assignments `h_0=0`,
`h_1,...,h_4 in{0,1,2,3}` for `(A,L,p,u0)=(8,5,2,3)`, retaining exactly
those satisfying the height recurrence. Exact rational checks cover (1)--
(6), their zero-edge accounting, boundary exception, and the local dual.
Those toy arrays are algebraic regression checks, not actual-branch
coverage or physical realization certificates.

Classification: sections2--4 are proved analytic necessary consequences
of the inherited physical recurrence and weights. The actual rank-cell
check is an exact finite certificate for the stated height-only witness.
Section5 is a precisely scoped method barrier to using only its retained
height/count assumptions. The numerical evaluation of (7), further
p-window localization and all H21/branch/global obligations remain outside
this component. No inherited claim has been demoted or contradicted.

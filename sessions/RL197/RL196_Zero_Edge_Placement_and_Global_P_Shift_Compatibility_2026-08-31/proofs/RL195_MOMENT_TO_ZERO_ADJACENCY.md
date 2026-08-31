# RL195 moment-to-chronological zero-adjacency theorem

RL195 closeout proof and exact constant certificate. Date: 2026-08-31.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.

## Scope and input

All physical claims are conditional on the sole high branch `(37,0,23,-1)`.
No cycle, extremal atom or terminal is constructed or excluded. This result
counts actual chronological adjacent height-zero vertices, not necessary
terminal ranks, p-shifted co-ownership, clean starts or H21 incidences.

Use the incoming constants

`L=137528045312`, `B=80448749305`, `R=L-B=57079296007`,
`p=65470613321`, `z=L-p`, `A=L+B`, `K0=2^37`.

They satisfy `0<R<B<2R<L`. Rank is `r_i=iB mod L` and its inverse is
`I(r)=pr mod L`. The mechanical exponent is c=1 at ranks `[0,R)` and c=2
at ranks `[R,L)`. Actual acceleration exponents a_i are positive integers,
and the physical height recurrence is

`h_(i+1)=h_i+c_i-a_i`, with cyclic h>=0 and h_0=0.             (1)

This is stronger than only h_(i+1)<=h_i+1. In particular a c=1 source at
height zero has a_i=1 and its successor also has height zero.

Write `x_r=1` exactly when h_(I(r))=0, and

`J=#{i mod L : h_i=h_(i+1)=0}`.                            (2)

The incoming rank weights are `w_r=rho_(I(r))`,
`d_r=w_(r-1)-w_r>0` for 1<=r<L. With

`alpha=3^p/2^u0`, `eta=alpha-1`, `theta=lambda*alpha-1`,

d_r equals theta*w_r for 0<I(r)<p and eta*w_r for p<=I(r)<L.
In particular d_r<theta. Define the actual weighted zero occupation

`Z0=sum_(1<=r<L) d_r*x_r`.

RL194's rank moment, including the unique carry, gives

`F=3(lambda-1)K0`, `rho_z=(1+theta)/2`,

`Z0 >= M := 2F-3rho_z+1`.                                 (3)

The factor 1/2 off height zero in that proof uses integer nonnegative
heights; (3) is not an assumption about arbitrary real-valued occupancy.

## 1. Disjoint mechanical geometry

Every c=1 source r in [0,R) has chronological successor rank r+B in[B,L).
These are disjoint pairs. Thus x_r=1 implies x_(r+B)=1 and the source at
rank r contributes one actual edge to J.

The c=2 sources split into:

- disjoint doublets: first rank r in[2R,L), successor rank r-R in[R,B);
- singleton c=2 ranks [B,2R), between c=1 sources chronologically.

Here 'doublet' concerns the mechanical digits only. It does not presume
that either height is zero. Together the second doublet vertices and the
singletons form exactly the rank interval [R,2R).

For first doublet phase i=I(r), neither i=p-1 nor i=L-1 is possible:
their ranks are R+1 and R, both below 2R. Consequently i and i+1 have the
same eta/theta coefficient and do not wrap the canonical origin. Since
c_i=2, rho_(i+1)=(4/3)rho_i. Hence exactly

`d_(r-R)=(4/3)d_r` for 2R<=r<L.                          (4)

There is no silent replacement of a lifted weight by a canonical one.

## 2. Charge excess weighted occupation to actual zero-zero edges

For a doublet put s=d_r and t=d_(r-R)=(4/3)s. Its two binary indicators
satisfy the elementary exact inequality

`s*x_r+t*x_(r-R) <= t+s*x_r*x_(r-R)`.                    (5)

It holds for all four indicator choices; it uses s<=t. The product on
the right is an actual chronological zero-zero edge at source rank r.
For singleton ranks, simply use d_r*x_r<=d_r. Low ranks 1<=r<R already
have x_r equal to their chronological zero-edge indicator by (1).
Summing disjoint terms gives the physical incidence inequality

`Z0 <= C + sum_(1<=r<R) d_r*J_(I(r))`

`          + sum_(2R<=r<L) d_r*J_(I(r))`,                 (6)

where J_i is the zero-zero edge indicator and

`C=sum_(R<=r<2R)d_r=w_(R-1)-w_(2R-1)`.

All charged source phases in (6) are distinct and exclude phase zero.
But h_0=0 and c_0=1 force h_1=0, so J_0=1. Thus the number of charged
edges is at most J-1. Once M>C is established, at least one charged edge
exists. Since every charged d_r is strictly smaller than theta, (3)/(6)
then imply the strict bound

`M <= Z0 < C+theta*(J-1)`.                               (7)

No unweighted pigeonhole argument using 2N0-L has been used.

## 3. The base capacity is an exact small multiple of the carry weight

The inverse ranks satisfy

`I(R-1)=z-1`, `I(2R-1)=z-2`.

The transition from z-2 to z-1 has digit2, and that from z-1 to z has
digit1. The phases are canonical and do not wrap. Therefore

`w_(R-1)=3rho_z/2`, `w_(2R-1)=9rho_z/8`,

`C=3rho_z/8=3(1+theta)/16`.                              (8)

Using (3),

`(M-C)/theta=(2F-11/16)/theta-27/16`.                    (9)

The exact rational verifier proves M>C and encloses the right-hand side
of (9) strictly between 9719139551 and 9719139552. Equation (7) says that
the integer J-1 is strictly larger than that quantity. Consequently

`J >= 9719139553`.                                      (10)

Every counted edge has h_i=h_(i+1)=0 and therefore physical exponent
a_i=c_i. Equation (10) is conditional analytic mathematics with an exact
constant certificate. The value is not a count of any finite necessary
state graph and does not assert that a high-branch word exists.

## 4. Verification and limits

Run `python3 verification/verify_rl195_moment_adjacency.py` from the package root.
Actual-constant checks use 96-term rational logarithm series with rigorous
tails and rational expm1 enclosures. All interval decisions are exact.
The mechanical partition is established analytically over its complete
rank intervals, not by sampling phase points.

An additional exhaustive toy regression uses A=8,L=5,p=2 and all256 arrays
h_0=0, h_1,...,h_4 in{0,1,2,3}; it selects exactly those obeying (1) with
positive exponents. It checks every selected array's physical incidence
inequality, complete rank partition, moment, boundary and strictness cases.
These arrays are algebraic regressions, not actual high-branch phases or
integer-orbit realization certificates.

The inherited N0>=43742681439, extremal corridor/finite speed filters,
spacing>=1001, ordinary flow/directional variation, and H21 budget are
unchanged. No p-shifted height-zero pair count or H21 clean-start ownership
follows without an additional theorem. All atom, branch and global gates
remain open. The full proof/verifier and independent higher-order constant
replay passed review. This note's J is the J00 edge count of the root report,
not the branch parameter J=23.

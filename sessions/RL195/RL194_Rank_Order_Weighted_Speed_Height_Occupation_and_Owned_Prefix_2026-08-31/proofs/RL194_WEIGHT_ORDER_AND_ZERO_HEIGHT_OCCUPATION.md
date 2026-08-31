# RL194 — rank-weight order, positive windows, and height occupation

RL194 closeout proof, independently reviewed.

Incoming handover: RL193; incoming job: RL194.
BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.
The parent established the fresh incoming integrity/fast-verification gate.

All physical statements are conditional on the sole high branch
`(v,H,J,d)=(37,0,23,-1)`.  No atom, terminal rank, state or cycle is
constructed.  No H21 budget, Gate or global conclusion changes.

## 1. Inputs and provenance

Use the current RL193 definitions

`A=217976794617`, `L=137528045312`, `B=A-L`,
`p=65470613321`, `u0=103768467013`, `Ap-u0 L=1`,
`z=L-p=72057431991`, `K_0=2^37`.

For canonical `0<=i<L`, put

`r_i=iB mod L`, `rho_i=2^floor(Ai/L)/3^i`,
`v_i=2^(-h_i)`, `q_i=rho_i v_i`, `f_i=rho_i epsilon_i`.

The heights are nonnegative integers, periodic modulo L, with `h_0=0`.
We retain

`lambda=2^A/3^L=exp(delta)>1`, `0<delta<2^-40`,
`q_(i+L)=lambda q_i`, `rho_(i+L)=lambda rho_i`,
`K_(i+L)=lambda K_i`, `f_i=3(K_(i+1)-K_i)`.

Canonical `rho_0=1` and `1/2<rho_i<1` for `0<i<L`.
For ordinary i, `epsilon_i=v_(i+p)-v_i` with the height index reduced
modulo L; the unique carry source z has `epsilon_z=2-v_z`.

Only the named narrow RL181 dependency was additionally consulted:

`sessions/RL182/RL181_Shallow_Pair_Gap_Corridor_and_Normalized_Width_Occupancy_2026-08-30/`.

Its main report, proof ledger and correction ledger preserve the full lifted
identity `exp(s)q_(i+p)/q_i=2^G_i`, where `s=p ln3-u0 ln2`.
Thus the unified shift identity below is an **inherited restatement**, not
a claimed new discovery.  The RL181 ledger lists shallow populations for
`h<=1,...,4`, shallow-pair adjacency, and normalized-width occupation.
The zero-height count derived here is a different actual vertex statistic;
it is not an H21 clean-start, defect, triple, pair-ownership or terminal count.
No broad history replay or novelty claim about unconsulted history is made.

## 2. Exact carry-completed q-shift

Define

`alpha=3^p/2^u0`, `eta=alpha-1`, `theta=lambda alpha-1`.

The Bezout identity gives

`ln alpha=(ln2-p delta)/L`.

Since `ln2>1/2` and `p<2^39`, the inherited `delta<2^-40` proves
`alpha>1`, and consequently `theta>eta>0`.

For every lifted source i the inherited physical relation is exactly

`f_i=alpha q_(i+p)-q_i`.                                  (1)

For completeness, if the source rank is not `L-1`, the floor increment over
p phases is u0, so `alpha rho_(i+p)=rho_i` and (1) is the ordinary error
formula.  At source z the increment is `u0+1`, the target height is zero,
and `alpha q_(z+p)=lambda alpha=2rho_z`; (1) becomes
`f_z=rho_z(2-v_z)`.  This also proves

`rho_z=lambda alpha/2=(1+theta)/2`.                        (2)

The lift in (1) must not be replaced with a canonical q value when `i+p>=L`.

## 3. Rank weights strictly decrease and rank-initial flow is nonpositive

Let `I(r)=pr mod L`, `w_r=rho_(I(r))`, and `V_r=v_(I(r))` for
`0<=r<L`.  Here `r_(I(r))=r`, `I(0)=0`, `I(L-1)=z`, `w_0=V_0=1`.

For every `1<=r<L`, with target phase `i=I(r)`, one has

`w_(r-1)/w_r = alpha` if `p<=i<L`,

`w_(r-1)/w_r = lambda alpha` if `0<i<p`.

This follows by comparing the predecessor phase `i-p`, and inserting the
factor lambda exactly when its canonical representative is `i-p+L`.
Thus

`1=w_0>w_1>...>w_(L-1)=rho_z>1/2`.

Put `d_r=w_(r-1)-w_r>0`.  For every `1<=m<L`, summation by parts gives

`S_m=sum_(r=0)^(m-1) w_r(V_(r+1)-V_r)`

`   =-w_(m-1)(1-V_m)-sum_(r=1)^(m-1)d_r(1-V_r)<=0`.       (3)

Equality holds exactly when `h_(I(r))=0` for every `1<=r<=m`.
The carry is not in any source set of (3); it occurs at rank `L-1`.

This is an exact sign/weight correlation in **mechanical-rank order**.
The set of sources of a chronological prefix is usually not a rank-initial
interval, so (3) does not imply a chronological excursion or fixed
chronological sign.  The small exact witnesses in the verifier illustrate
this distinction; they are algebraic countermodels to that order substitution,
not realizations of the actual high branch.

## 4. Positive moving-window representation of the physical K coordinate

For every lifted i define the genuinely lifted windows

`C_i=sum_(j=i)^(i+p-1)q_j`,

`Y_i=sum_(j=i)^(i+L-1)q_j`,

and the positive constant `beta=(alpha-1)/(lambda-1)`.
Then

`3K_i=alpha C_i+beta Y_i`.                                (4)

Proof: `C_(i+1)-C_i=q_(i+p)-q_i` and
`Y_(i+1)-Y_i=(lambda-1)q_i`.  Hence the difference of the right-hand side
of (4) is `alpha q_(i+p)-q_i=f_i`, the same as the difference of `3K_i`.
Their difference is constant in i.  Both sides are lambda-quasiperiodic,
so this constant equals lambda times itself, and must be zero as
`lambda!=1`.  Every coefficient and summand of (4) is positive.

For canonical `0<=a<L`, let `P_a=sum_(i=0)^(a-1)q_i`.  Then
`Y_a=Y_0+(lambda-1)P_a`, so the exact chronological displacement is

`3(K_a-K_0)=alpha(C_a-C_0)+(alpha-1)P_a`.                 (5)

Applying only the already-certified RL193 atom-specific prefix signs gives:

- lower / `2^38` atom:
  `C_a>C_0-(1-alpha^(-1))P_a`;
- upper / `2^37` atom:
  `C_a<C_0-(1-alpha^(-1))P_a`.

In particular the upper atom forces strict loss of actual p-window q mass.
The lower inequality does not necessarily assert `C_a>C_0`.
These are conditional physical window constraints, not atom exclusions.
The canonical early-defect signature has not been moved to another origin.

## 5. Exact full-period moments and actual zero-height occupation

In this section Q denotes weighted q mass (called Q_mass in the root
handover), not the inherited terminal-rank split Q=88514772733.

Let `Q=Y_0=sum_(i=0)^(L-1)q_i` and `P=C_0=sum_(i=0)^(p-1)q_i`.
Equation (4) gives the positive moment identity

`3*2^37=beta Q+alpha P`.                                  (6)

Since `0<P<Q`,

`3*2^37/(beta+alpha)<Q<3*2^37/beta`.

The exact rational verifier certifies the convenient integer enclosure

`67,236,063,233 < Q < 80,336,439,250`.                     (7)

Q is weighted q mass; it is not a number of physical phases.

The rank summation gives an additional occupation theorem.  Set

`F=sum_(i=0)^(L-1)f_i=3(lambda-1)2^37`.

Including the carry exactly and using `V_0=1` gives

`F=2rho_z-1+sum_(r=1)^(L-1)d_r V_r`,                     (8)

or, in canonical q coordinates,

`F=theta+eta sum_(p<=i<L)q_i+theta sum_(1<=i<p)q_i`.

Let `N_0=#{0<=i<L:h_i=0}`, an **actual physical height occupation**,
and let

`Z_0=sum_(1<=r<L, h_(I(r))=0)d_r`.

Outside height zero, nonnegative integral heights imply `V_r<=1/2`.
Since `sum_(r>=1)d_r=1-rho_z`, (8) yields

`Z_0>=2F-3rho_z+1`.                                      (9)

The right side is positive by the exact numerical certificate.  Each
`d_r` is either `eta rho_(I(r))` or `theta rho_(I(r))`, hence is strictly
less than theta.  There are exactly `N_0-1` height-zero ranks in `1..L-1`;
the missing one is phase zero.  Positivity in (9) ensures `N_0-1>0`, and
therefore

`N_0-1 > (2F-3rho_z+1)/theta`

`       = (2F-1/2)/theta-3/2`.                            (10)

The fully rational logarithm/exponential enclosure proves

`(2F-1/2)/theta-3/2 > 43,742,681,437`.

Since `N_0-1` is an integer, the new necessary physical bound is

`N_0 >= 43,742,681,439`.                                 (11)

This is conditional on physical monodromy and the fixed branch value
`K_0=2^37`; it is not obtained by counting candidate terminal ranks.
It supplies no H21 terminal count, no zero-defect run count, no ownership
multiplicity and no H21 charging-budget release.  In particular the
adjacency lower bound `2N_0-L` would still be negative at this floor.

## 6. Reproducible exact arithmetic and scope

Run:

`python3 verification/verify_rl194_weight_order.py` from the package root.

For log n, write `t=(n-1)/(n+1)` and use all terms `k=0,...,79` of
`2 sum t^(2k+1)/(2k+1)`, with positive tail at most
`2t^161/(161(1-t^2))`.  This provides exact Fraction enclosures for
ln2, ln3, delta, `x=ln alpha`, and `y=ln(lambda alpha)`.

For `0<x<1`, the enclosure for `exp(x)-1` is

`x+x^2/2 < exp(x)-1 < x+x^2/[2(1-x/3)]`.

The upper bound follows because the terms from degree two onward have
successive ratio at most `x/3`.  These rational bounds prove (7), positivity
in (9), and the strict integer comparison used for (11), with no floating
point and without constructing the enormous integers `2^A` or `3^L`.

The verifier also exhausts all 256 assignments `h_0=0`,
`h_1,...,h_4 in {0,1,2,3}` for the small algebraic case `(A,L,p)=(8,5,2)`.
It checks all rank-prefix boundaries, exact carry treatment, the q-shift,
the moment identity, the moving-window recurrence and quasiperiodicity.
These 256 checks are finite algebraic regression tests only, not a search
through any part of the actual physical phase space.

Classification: (3)--(6), (8)--(11) are complete analytic deductions
conditional on the inherited physical identities; the small constants in
(7)/(11) have exact rational certificates.  Equation (1) is an inherited
restatement.  The RL194 root proof ledger records the combined classification.
There is no incomplete phase scan or asserted physical realization.
The rank-versus-chronology distinction and the missing H21 incidence
consumer remain explicit open obligations.

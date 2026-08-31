# RL201 — absolute endpoint reconstruction and a coupled real-mass fiber

Date: 2026-08-31. Frozen RL201 component.
Incoming RL201; BASE_HEAD `e47dcb720028b4465d125c342fe86fb8daac3aa9`.
The parent passed the incoming gate. A temporary logarithm-helper review was
resolved by the parent without an inherited theorem or range demotion.

All physical conclusions below are conditional on the sole high branch
`(37,0,23,-1)`. No eta class, physical H21 occurrence, H21 charge, branch,
Gate or global cycle conclusion is established here.

## 1. Exact inherited definitions and dependency boundary

Use

`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u=103768467013`, `Ap-uL=1`, `B=A-L`, `K0=2^37`.

For canonical chronological phase `i`, put

`b_i=floor(Ai/L)`, `h_i=b_i-S_i`,
`rho_i=2^b_i/3^i`, `q_i=rho_i*2^(-h_i)`,
`z_i=q_i*y_i`, `x_i=y_i/2^h_i=z_i/rho_i`.

The canonical physical heights are nonnegative integers and satisfy
`a_i=b_(i+1)-b_i+h_i-h_(i+1)>=1`. All quantities have their inherited
L-quasiperiodic lift: q, rho, z and K multiply by
`lambda=2^A/3^L>1`; y and h are periodic. Define

`alpha=3^p/2^u>1`, `beta=(alpha-1)/(lambda-1)>0`,
`P_a=sum_(0<=j<a)q_j`, `Q=P_L`,
`C_i=sum_(i<=j<i+p)q_j` and `Y_i=sum_(i<=j<i+L)q_j`,

with genuinely lifted q in the last two sums.

The inherited identities are

`3(z_(i+1)-z_i)=q_i`,
`3K_i=alpha*C_i+beta*Y_i`,
`K0=K_0=2^37`.

Sources: RL181 main report/ledger frozen under `sessions/RL182/`; RL194
`proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md` and RL195
`proofs/RL195_PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`, frozen
under `sessions/RL197/RL196_Zero_Edge_Placement_and_Global_P_Shift_Compatibility_2026-08-31/`.
The z telescope, complete p-chain and moving-window inversion are inherited
restatements, not new discoveries claimed here.

RL199 supplies the absolute H21 tau=34 endpoint

`Y_0^-=2^34*eta-1`, `Y_0^+=2^34*(eta+21)-1`,

with common height one. Its source canonical rank j is in
`[40886621976,57079296006]` under RL200. If the source phase is a, then
`j=aB modL` and `a=pj modL`. The p-shift edge is noncarry since j<L-1.
The lower normalized endpoint is exactly x_a; its partner is x_(a+p modL).

## 2. Absolute endpoint as a complete rank-gap moment

Let `I(r)=pr modL`, `d_r=K_(I(r))/rho_(I(r))`, `0<=r<L`.
The inherited positive p-chain gives

`x_(I(r+1))-x_(I(r))=d_r` for `0<=r<L-1`,
`2x_0-x_(I(L-1))=d_(L-1)`.

Summing proves

`x_0=sum_(0<=r<L)d_r`,
`x_(I(j))=sum_(0<=r<L)d_r+sum_(0<=r<j)d_r`.       (1)

Thus the H21 lift obeys the exact absolute rank identity

`eta=[1+2 sum_(r<L)d_r+2 sum_(r<j)d_r]/2^34`.       (2)

This is not a chronological order claim. The rank-initial partial sum in
(1) follows the single p-shift chain, whereas d_r itself is the value of
K at chronological phase I(r). The carry is already included once and
only once in the full sum. Necessary rank j does not supply the complete
rank-gap profile in (2).

## 3. Exact fixed-K0 endpoint functional

The z telescope and full closure give

`z_a=m+P_a/3`, `m=Q/[3(lambda-1)]`.

At the H21 source a, common height one therefore gives

`2^33*eta-1/2=x_a
 =[Q+(lambda-1)P_a]/[3(lambda-1)rho_a]`.             (3)

At phase zero the exact fixed moment is

`3K0=alpha*P_p+beta*Q`.

Eliminating Q, using `beta=(alpha-1)/(lambda-1)`, proves

`3(alpha-1)rho_a(2^33*eta-1/2)
 =3K0-alpha*P_p+(alpha-1)*P_a`.                     (4)

No approximation in lambda, alpha or rho is permitted in (4).
It is the chronological-prefix form of the absolute position information
carried by (2), with the fixed K0 normalization imposed exactly.

Define the joint prefix functional

`J_a=alpha*P_p-(alpha-1)*P_a`.

Then

`eta=2^-34+(3K0-J_a)/[3(alpha-1)rho_a*2^33]`.       (5)

At fixed canonical a, exact J_a determines eta. More weakly, a residue or
certified interval for J_a narrow enough for one of the arithmetic lattice
classes in (5) could select a state or sign. The fixed scalar K0 moment
alone does not provide J_a.

The eta-integer lattice has J_a spacing

`D_a=3(alpha-1)rho_a*2^33`,

and the four surviving mod18 classes correspond exactly to the four
J_a arithmetic lattices obtained by substituting
`eta=18k+c`, `c in {0,8,9,17}` in (4). This is an exact reparameterization,
not a newly satisfied arithmetic constraint or a class selection.

The inherited coarse bounds already quantify this scale:

`1/20 < D_a < 2/15`.                                (6)

Indeed write `delta=A ln2-L ln3`, with `0<delta<2^-40`.
The Bezout identity gives
`s=ln alpha=(ln2-p*delta)/L`. Since `p<2^36` and
`2/3<ln2<7/10`,

`29/(48L)<s<7/(10L)`.

For `0<s<1`, the exponential series gives
`s<exp(s)-1<s/(1-s)`. Using `1/2<rho_a<=1`,

`29*2^33/(32L) < D_a < 21*2^33/(10L-7)`.

The exact actual-constant comparisons are

`29*2^33/(32L)=30408704/537218927 > 1/20`,
`21*2^33/(10L-7)=25769803776/196468636159 < 2/15`.

The elementary log bounds can be checked without decimal arithmetic:
`ln2=2 sum_(k>=0)(1/3)^(2k+1)/(2k+1)>2/3`, and bounding all terms after
the first by their denominator-three geometric tail gives `ln2<25/36<7/10`.
Thus unit eta resolution corresponds to a strictly subunit increment of
the exact joint prefix mass. Equation (6) alone does not supply such a mass
bound or a residue.

## 4. A precise coupled continuous-mass flexibility theorem

This section relaxes the integer-height requirement. Begin with any finite
positive real q-word satisfying `0<q_i<=rho_i`, extend it by
`q_(i+L)=lambda*q_i`, and define the positive reconstructed coordinates

`z_i=Y_i/[3(lambda-1)]`, `x_i=z_i/rho_i`,
`K_i=(alpha*C_i+beta*Y_i)/3`.

It satisfies the exact lifted z transport and K moving-window laws. It is
not asserted to arise from integer heights or positive integer acceleration
exponents. An arbitrary starting real q-word need not have `K_0=2^37`.
The perturbation below preserves its exact starting phase-zero K value,
whatever that value is. Application to the branch-normalized relaxation
additionally assumes that the starting word satisfies `K_0=2^37` exactly;
no such actual-constant starting word is constructed here.

Let integers a,n obey

`a>=1`, `n>=0`, `a+n+1<p`, `a+p+n+1<L`.

Protect every q coordinate in `[a,a+n]` and `[a+p,a+p+n]`, as well as
phase-zero and phase-p anchors if those were imposed. Choose indices

`b in [a+n+1,p-1]`, `d in [a+p+n+1,L-1]`,

and assume both chosen coordinates are strictly inside their caps:

`0<q_b<rho_b`, `0<q_d<rho_d`.

For a real parameter t change only

`q_b -> q_b+beta*t`,
`q_d -> q_d-(beta+alpha)*t`.                         (7)

Put

`Tminus=min(q_b/beta,(rho_d-q_d)/(beta+alpha))`,
`Tplus =min((rho_b-q_b)/beta,q_d/(beta+alpha))`.

Both are positive. For every `-Tminus<t<Tplus`, all q coordinates remain
positive and at or below their caps, and protected coordinates do not change.

**Exact preservation.** The perturbed word has the same K0 and the same
K_i for every chronological `a<=i<=a+n`.

Proof. In all these windows including phase zero, b is in the p-window and
d is outside it. Neither index is in the chronological prefix `[0,i)`.
Consequently `delta Q=-alpha*t`, `delta P_i=0`, and `delta C_i=beta*t`.
The identity `Y_i=Q+(lambda-1)P_i` then gives

`3 delta K_i=alpha*beta*t-beta*alpha*t=0`.

The same calculation at zero gives exact delta K0=0. Neither altered index
is a protected local q coordinate, phase zero, or phase p.

**Exact endpoint displacement.** Nevertheless

`delta x_i=-alpha*t/[3(lambda-1)rho_i]` for `a<=i<=a+n`.

In particular, at an h=1 H21 source, the lift coordinate computed from the
absolute endpoint changes by

`delta eta=-alpha*t/[3(lambda-1)rho_a*2^33]`.        (8)

At the paired phase i+p the chronological prefix gains beta*t, and
`delta Y_(i+p)=-t`. Since `rho_(i+p)=rho_i/alpha` on these unwrapped
noncarry edges, the normalized partner endpoint changes by the same
amount. Thus every protected normalized p-gap is unchanged as well as
every protected K value.

**Full strict-corridor qualification.** If the starting finite q-word also
satisfies a strict full-period K corridor, sufficiently small nonzero t
preserves that corridor. If its minimum margin from both walls is epsilon>0,
one sufficient extra condition is

`|t|<3*epsilon/[lambda*(beta+alpha)*(2*beta+alpha)]`.

Indeed the coefficient of any canonical q_j in 3K_i is one of
`beta`, `beta+alpha`, `lambda*beta`, `lambda*(beta+alpha)`; applying the
triangle inequality to (7) proves the displayed bound. This condition
does not claim such a word or such a margin exists for the full physical
H21 constraints.

**Exact residue-reaching qualification.** Write

`c_a=alpha/[3(lambda-1)rho_a*2^33]>0`.

Within the stated strictly interior family `-Tminus<t<Tplus`, and ignoring
any additional corridor restriction, the attainable eta values are exactly
the open interval

`(eta0-c_a*Tplus, eta0+c_a*Tminus)`.

An integer eta target is reached by this chosen open family of (7) exactly
when its corresponding `t=(eta0-eta_target)/c_a` obeys every imposed strict
bound. This does not describe cap-limited boundary values that may also be
feasible under the broader non-strict caps `q_i<=rho_i`. No bound proving that
this interval reaches another mod18 class has been established for an
actual physical word. Terminal valuation, tau35 state compatibility,
dyadic heights and positive integral exponents remain separate constraints
in this relaxed model. They are not silently preserved by (7).

The theorem proves a nonconstant absolute-position direction in an
explicitly defined coupled real-mass fiber. It does **not** prove the full
exact fixed-K0 admissible-height-word consumer insufficient, and it does
not itself prove all four H21 classes survive that complete consumer.

## 5. Exact scope against the inherited denominator theorem

RL195 proves that a complete globally admissible *integer* height word
with exact K0=2^37 already reconstructs an odd-integral orbit. The present
continuous perturbation generally destroys the required power-of-two form
`q_i/rho_i=2^(-h_i)`, with h_i a nonnegative integer, and must not be applied
as if it preserved that theorem's hypotheses. Dyadic rationality alone is
weaker than that required form.

Therefore the minimal missing information identified here is a restriction
on the exact joint prefix mass J_a (equivalently the complete rank-gap
moment in (2)) compatible with the single globally admissible height word.
It is not an additional generic integrality check after a complete exact
fixed-K0 height word has already been supplied.

## 6. Classification

- Equations (1)--(5): complete conditional analytic endpoint identities;
  their transport inputs are inherited, and no historical novelty beyond
  this explicit oriented-endpoint specialization is claimed.
- Equation (6): conditional analytic lattice-scale bound with exact
  actual-constant rational comparisons.
- Section 4: analytic flexibility theorem for a named continuous-mass
  relaxation, conditional on all stated feasibility/slack assumptions.
- No actual-constant H21 real-mass model, dyadic word, rank population,
  residue exclusion or cycle realization is claimed.
- `verification/verify_rl201_endpoint_moment.py` is an exact finite algebraic regression of
  these identities on manageable toy Bezout systems. Such a regression is
  not an actual-constant high-branch certificate or a replacement for proof.

## 7. Completed verification and frozen component

Portable command from the package root:

`python3 verification/verify_rl201_endpoint_moment.py`

Result: PASS.

- Actual-constant rational comparisons for `1/20<D_a<2/15` passed.
- Toy Bezout `(A,L,p,u)=(27,17,12,19)`: 12 exact signed perturbations.
- Toy Bezout `(A,L,p,u)=(46,29,12,19)`: 68 exact signed perturbations.

Each toy range contains all integers `a in [1,L-1]`, `n in [0,3]` meeting
`a+n+1<p` and `a+p+n+1<L`. It chooses the first permissible b,d and tests
both `t=-Tminus/2` and `t=Tplus/2`. Every test checks the full-period direct
z transport, complete rank-chain inversion including the carry, fixed-K0
endpoint formula at every canonical phase, all canonical moving-window
coefficient classes, protected local data, endpoint displacement and the
global perturbation bound. All arithmetic uses exact integers/Fractions.

No actual-constant phase/height-word search was undertaken or claimed.
The 80 toy perturbations are complete over the displayed finite toy range,
not over all possible continuous words or any physical H21 state space.

This component is frozen in the RL201 handover. Its authority is established
only by the verified coherent commit, remote ref advance and readback recorded
in the repository transition; the canonical ledger fixes its exact scope.

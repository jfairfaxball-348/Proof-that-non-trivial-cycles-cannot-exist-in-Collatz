# RL206 — cyclic recurrence cokernel and exact no-go scope

Date: 2026-08-31. Status: **proved analytic mathematics**, with the exact family scope below.

Classification: **proved analytic mathematics** for Theorems 1–3;
**method barrier** only for the family explicitly defined in section 4.
Canonical classification is in the RL206 proof ledger.

Dependency: `../interfaces/RL206_FROZEN_INTERFACE.md`, read after the reported start gate and
verified RL206-C1 repair. Only the full-word recurrence is used here, not the strip
increment, a radius-three leaf, or an unproved Gate-B witness/modulus.

**Scope warning.** This classifies additive RHS compatibility obstructions
annihilating `B Z^A`, not every residue or observable of an owned integer solution.
In particular `(c·f/D) mod D` on `f in B Z^A` retains information from `c·f mod D^2`
and lies outside the annihilator family. This is not an all-quotient-residual no-go,
and it does not close Gate B.

## 1. Definitions and exact transport

Fix a binary word `d=(d_0,...,d_(A-1))`, with `0<L=sum_i d_i<A` and
`D=2^A-3^L>0`. Thus `A>=2`, `D` is odd, and `gcd(D,6)=1`.
Write `a_i=3^(d_i)` and `P_i=sum_(j<i)d_j`. Define

`(Bx)_i=2 x_(i+1)-a_i x_i`, cyclically with `x_A=x_0`.

The physical forcing is `f=d`. For the module theorem keep `B` fixed but allow any
formal `f in Z^A`. This extension does not make arbitrary forcings parity words.
Set

`c_i=2^i 3^(L-P_(i+1))=2^i product_(h=i+1,...,A-1) a_h`,

`T(f)=c·f`.

All exponents are nonnegative. The entries `c_0=3^(L-d_0)` and
`c_(A-1)=2^(A-1)` are coprime. Computing one column at a time gives

`c^T B=D e_0^T`:                                             (1)

column zero is `2 c_(A-1)-a_0 c_0=D`; column `j>=1` is
`2 c_(j-1)-a_j c_j=0`. For the physical forcing,

`T(d)=sum_(d_i=1) 2^i 3^(L-1-P_i)=Q(d)`.                    (2)

Define cyclic numerators for arbitrary forcing by

`N_i(f)=sum_(k=0,...,A-1) 2^k [product_(h=k+1,...,A-1) a_(i+h)] f_(i+k)`.

Subscripts are cyclic and an empty product is one. Then `N_0=T`, and shifting
the sum gives

`2 N_(i+1)(f)-a_i N_i(f)=D f_i`.                             (3)

All terms at `f_(i+k)` for `1<=k<A` cancel; the remaining coefficient at `f_i`
is `2^A-product_h a_h=D`. Thus `x_i=N_i(f)/D` solves `Bx=f`. This solution is
unique, since a homogeneous solution satisfies `2^A x_0=3^L x_0` and hence
`x_0=0`, followed by every coordinate zero. For `f=d`, the numerators are exactly
`N_i(d)=Q(rot_i(d))` from the frozen interface.

## 2. Theorem 1: cokernel and Smith normal form

For `tau(f)=T(f) mod D`,

`ker(tau)=B Z^A`, and `tau:Z^A -> Z/DZ` is onto.              (4)

Consequently `coker(B)` is cyclic of order `D`, and the Smith normal form is

`diag(1,...,1,D)`.                                          (5)

This includes `D=1`, when the cokernel is zero.

**Kernel proof.** If `f=Bx` for integer `x`, equation (1) gives `T(f)=D x_0`.
Conversely if `D|N_0(f)`, reduce (3) modulo `D`. Since 2 is invertible modulo `D`,
induction gives `D|N_i(f)` for all `i`. The unique rational solution is integral,
so `f in B Z^A`. Finally `c_(A-1)=2^(A-1)` is a unit modulo `D`, proving
surjectivity. This establishes (4) directly without a lattice-index theorem.

**Explicit unimodular reduction.** Only the diagonal and full cyclic permutation
contribute to the determinant, giving

`det B=(-1)^(A-1) D`.                                       (6)

Put `alpha=c_0`, `beta=c_(A-1)`, and choose integers `u,v` with
`alpha*u+beta*v=1`. Define the columns of `U` by

- column 0: `u e_0+v e_(A-1)`;
- column `j`, `1<=j<A-1`: `e_j-c_j (u e_0+v e_(A-1))`;
- column `A-1`: `-beta e_0+alpha e_(A-1)`.

The first/last two-by-two transformation has determinant one; the middle columns
are elementary column subtractions. Hence `det U=1`. The inverse rows are
`c^T`, then `e_j^T` for `1<=j<A-1`, then `-v e_0^T+u e_(A-1)^T`.
In particular `c^T U=e_0^T`.

Let `S=diag(D,1,...,1)` and `W=S^(-1) U^(-1) B`. By (1), the first row of
`U^(-1)B` is `D e_0^T`, so `W` is integer. Equation (6) yields
`det W=(-1)^(A-1)`, hence `W` is unimodular. Thus

`U^(-1) B W^(-1)=S`.

Move the first row and column to the last position to obtain (5). This explicit
integer reduction proves the asserted Smith form without relying on sampled cases.

## 3. Theorem 2: all additive compatibility congruences

For any `M>=1` and integer vector `lambda`, these conditions are equivalent:

1. `lambda·f == 0 mod M` for every `f in B Z^A`;
2. `lambda^T B == 0 mod M` coordinatewise;
3. there is a unique `t in Z/MZ` satisfying `D t == 0 mod M` and
   `lambda_i == t c_i mod M` for all `i`.

**Proof.** Testing the domain basis vectors gives equivalence of 1 and 2.
By (4), a homomorphism from `Z^A` to `Z/MZ` vanishing on `B Z^A` descends uniquely
to `Z/DZ`. Such a map is determined by the image `t` of `1`; the only requirement
for `r mod D -> t r mod M` to be well-defined is `D t=0`. Composition with `tau`
gives exactly 3, including its uniqueness. No assumption `M|D` was made.

Writing `g=gcd(D,M)`, there are precisely `g` maps, represented by
`t=(M/g)k`, `0<=k<g`. At `f=d` every such test is

`M|t Q(d)`, equivalently `m|Q(d)`,                           (7)

where `m=M/gcd(M,t)` and **`m|gcd(M,D)`**. For `t=0`, `m=1`.
Both assertions follow by cancelling `gcd(M,t)`; the remaining factors of `M`
and `t` are coprime, so `M|D t` forces `m|D`.

A finite collection with effective factors `m_1,...,m_k` is exactly
`lcm(m_1,...,m_k)|Q`, and that least common multiple divides `D`. Several proper
factor tests may collectively recover full ownership when their least common
multiple is `D`; they do not create another independent compatibility direction.
Full ownership is `M=D,t=1`.

Proper factors can be strictly weaker. The exact word `110000` has
`A=6,L=2,D=55,Q=5`; thus `5|Q` but `D` does not divide `Q`. It is not an owned
cycle. A branch modulus such as `2^a-3^ell` cannot silently replace full `D`;
all remaining factors and additional branch ownership hypotheses must be accounted
for. If an affine congruence vanishes on the entire image lattice, setting `f=0`
forces its constant to vanish modulo `M`, reducing it to the theorem above.

## 4. Theorem 3: the whole precisely specified elimination family

For fixed `d`, the **recurrence-linear compatibility family** consists exactly of:

- additive RHS congruences `lambda·f == 0 mod M` annihilating `B Z^A`;
- rational affine zero identities `F(x,f)=p·x+q·f+k` valid for every formal solution
  `f=Bx`, with no additional inequalities or arithmetic assumptions;
- arbitrary finite combinations of these outputs.

The coefficients and moduli may depend arbitrarily on the fixed word and phase.
Thus this covers every choice of coefficients, not a finite list of guessed
residuals. Rational elimination is included whenever, after clearing denominators,
its final output meets one of these definitions. Validity is universal in formal
forcing at fixed `B`.

Theorem 2 classifies all the congruences. For the zero identities,

`F(x,Bx)=(p+B^T q)·x+k`

vanishes for all rational `x` iff `k=0` and `p=-B^T q`. Equivalently

`F(x,f)=q·(f-Bx)`.                                          (8)

Hence every zero identity is a rational combination of the recurrence rows.
Every compatibility congruence is ordinary ownership or its factor projection.
More phases, arcs, or linear combinations **within this family** cannot create
an independent compatibility obstruction.

This is the entire claimed no-go scope. It does not show that every linear-looking
observable of a quotient solution belongs to the family. Each proposed consumer
must be tested against the definition, not classified by notation alone.

## 5. Essential exception: quotient residues and modulo-D-squared information

For `D>1`, define only on the image lattice

`psi(f)=(T(f)/D) mod D`, for `f in B Z^A`.

Equation (1) gives `psi(Bx)=x_0 mod D`. This additive map on `B Z^A` does not
annihilate that lattice: `psi(B e_0)=1` whereas `psi(0)=0`. Every annihilator
in Theorem 2 vanishes at both. Therefore `psi` is outside the classified family,
even though it is additive on its domain and linear after division by `D`.

The value `T(f) mod D` is zero everywhere on that domain and does not determine
`psi`; `T(f) mod D^2` does determine it. On owned physical forcing this is
precisely `R_0 mod D=(Q(d)/D) mod D`. The example uses formal forcings to expose
the logical limitation, not to assert existence of a nontrivial ordinary cycle.
When `D=1`, the displayed residue is trivial; this does not extend the theorem
to solution residues at other moduli.

The no-go excludes residues of integral solutions, arithmetic at larger moduli
before dividing ownership, quotient-dependent weights, nonlinear predicates,
positivity, least-state/strict-excursion/packing inequalities, physical-state
witness selection, and additional branch information. Such consumers may supply
further constraints. This result neither supplies nor rules out their success.

## 6. Red teams and honest strategic consequence

- **RL20 fake:** inherited `D>1,gcd(D,Q)=1` makes `tau(d)` nonzero, so it has no
  integer solution. Integrality is essential to the lattice kernel. This ownership
  discriminator gives no contradiction for words already satisfying `D|Q`.
- **RL79:** the cyclic cokernel agrees with pure rotation-residue rank-one collapse;
  it does not extend that collapse to `Q/D mod D`.
- **Coboundary/tautology:** (8) classifies universal linear zero identities as
  recurrence combinations. It does not assert every geometrically selected
  residual is a cyclic coboundary.
- **Proper factor:** (7) states the exact effective factor, including when several
  factor tests collectively recover `D`.
- **Generalized increment:** compatibility for forcing `s d` is `D|s Q`.
  For `g=gcd(D,Q)`, this is equivalent to `(D/g)|s`. The least positive generalized
  increment is `s=D/g`, with integer states `Q_i/g` and normalized states `Q_i/D`.
  This reproduces the inherited increment formula without erasing ordinary
  integrality or treating quotient residues as homogeneous zero identities.
- **Scale:** no uniform free-context bound, packing contradiction, or exhaustive
  bounded configuration claim has been made.
- **Globality:** the algebraic theorem covers all words in its stated domain;
  this is not a Gate-B contradiction. Gates A/B and global cycle exclusion remain
  open; no rank exclusion or physical H21 conclusion is added.

The limited pivot reason is rigorous: further pure recurrence-linear compatibility
elimination cannot create the independent information requested by the Gate-B
route. Work must add an ingredient outside that family. H21 independent-information
completion is the inherited fallback. This theorem alone does not establish the
broader claim that every natural quotient-residual approach has failed, and must
not be recorded as that broader success criterion.

## 7. Independent finite verification

`verification/verify_rl206_quotient_module.py` uses standard-library Python and exact integers. Its
declared, complete finite range is:

- all binary words with `2<=A<=9`, `0<L<A`, and `D>0`: both transport-matrix inverse
  identities, `Q` specialization, determinant, explicit unimodular reduction,
  coprime proper minors, and the generalized increment;
- all such words with `2<=A<=4`, all `1<=M<=9`, and every coefficient vector
  in `{0,...,M-1}^A`: equality of the full annihilator sets and their cardinality;
- all such words with `2<=A<=5` and every forcing in `{-1,0,1}^A`: exact kernel
  equivalence and integrality;
- the proper-factor example and the quotient-residue exception at all tested `D>1`.

These checks supplement the analytic proof; they imply no untested finite coverage
or global Collatz conclusion. Run:
`python3 verification/verify_rl206_quotient_module.py`.

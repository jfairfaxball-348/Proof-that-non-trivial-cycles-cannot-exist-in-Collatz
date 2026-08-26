# RL115 — dyadic–triadic Fourier resolution barrier and route transition

Date: 2026-08-26

## Outcome and classification

RL115 tested the next retained RL113 route: an ownership-sensitive Fourier
statistic on the selected zero-flow-cut support that would yield a strict
coefficient-mass loss. No such statistic or mass-loss theorem is proved.

The analytic result is a **method barrier**. Additive characters applied only
to the transport support see its sum `S`, and exact character orthogonality
therefore restates `D|S`. Characters applied to an individual numerator do
distinguish full ownership, but their exact resolution is the variable group
`Z/DZ` (or an equivalent order-`D` family). It has no uniform finite-state or
modulus bound on the unrestricted hypothetical-cycle input, and the resulting
identity is merely the indicator of `D|Q`, not a support mass loss. This hits
the RL115 stop condition; the next retained route is the two-base finite
transducer.

No Gate A or Gate B closure, nontrivial-cycle exclusion, or Collatz closure
is claimed.

## Fourier-resolution dichotomy

For `D>0`, write `e_D(t)=exp(2 pi i t/D)`. The finite Fourier identity is

`I_D(n) = (1/D) sum_(t=0)^(D-1) e_D(t n) = 1 if D|n, and 0 otherwise`.  (1)

For the selected RL109 support,

`S=sum_j epsilon_j 2^(a_j)3^(b_j)`.

Every additive character statistic assembled from those terms factors through
the residue class of `S` modulo its chosen modulus. At modulus `D`, (1)
evaluated on `S` is exactly the inherited condition `D|S`; it cannot
distinguish whether the two individual numerators were owned. This is the
RL114 subtraction barrier in Fourier form.

To retain full ownership one can instead evaluate (1) on each numerator:

`I_D(Q(u)) I_D(Q(v)) = 1[D|Q(u)] 1[D|Q(v)]`.               (2)

By the RL114 rotation identity, the two factors add no independent local
constraint: one owned rotation implies the other. Formula (2) is therefore
an exact encoding of whole-word ownership, not a new statistic of a selected
two-base support.

Moreover, a finite quotient that detects the zero class of `Z/DZ` against
every nonzero residue must be injective: if `f: Z/DZ -> G` has
`f(x)=0` only for `x=0`, its kernel is zero, hence `|G|>=D`. Equivalently,
the complete character resolution (1) uses a cyclic group and roots of unity
of order `D`. Since the live target supplies no a priori global bound on
`D=2^A-3^L`, replacing this by a uniformly bounded finite group either loses
ownership information or assumes the missing bound. A variable `D`-sized
group is precisely the unbounded-modulus/state outcome prohibited by RL115.

No step above bounds the coefficient mass of the selected terms. The
orthogonality identities are exact residue bookkeeping; they remain true for
arbitrary residues and do not supply the strict mass loss required after
RL110.

## Mandatory red teams

- **RL20:** its ordinary numerator has a nonzero class modulo its own `D`.
  Thus (1) evaluated on that individual numerator is zero, while an
  `S`-only character statement would not be an ownership test. RL115 uses
  this only as a discriminator, not as a theorem about the fake.
- **RL79:** under generalized increment `s`, the numerator is `sQ` and the
  available test is `I_D(sQ)`, not `I_D(Q)`. No factor `s` is cancelled and
  no increment-invariant statistic is promoted.
- **RL81:** `Q/D` is physical only after the individual divisibility test;
  neither a character value nor a support quotient is called a state.
- **Primitivity:** it is still used only in the inherited selection of
  distinct rotations and the nonzero conclusion `S!=0`.
- **Scope:** no Raw/Farey material is used; the barrier is conditional on the
  unrestricted ordinary full-ownership interface.
- **Finite work:** the verifier checks finite instances of the algebraic
  identity only. It is a sanity test, not a Fourier inequality, a scan, or a
  cycle certificate.

## Dependencies and next route

This report depends on RL109's unscaled owned sparse multiple, RL110's
all-legal support barrier, and RL114's rotation-ownership identity. It makes
no correction or demotion of inherited mathematics. It stops only the
Fourier formulation currently specified: a later Fourier route would need a
new, quantitatively controlled ownership-bearing structure beyond exact
residue orthogonality.

Begin RL116 with the two-base finite-transducer first obligation in the next
target. Preserve the original fallback order; do not revive the stopped
Fourier statistic under a new label.

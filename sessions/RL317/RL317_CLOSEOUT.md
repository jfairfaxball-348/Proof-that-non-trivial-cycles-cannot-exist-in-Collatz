# RL317 closeout — absolute dual-shadow factor, cofactor residue, and first fibre

Date: 2026-09-14
Completed RL: RL317
Successor RL: RL318
Status: FROZEN CANDIDATE

## 1. Outcome and scope

RL317 attacked the missing absolute `D0=X-Y` ownership in the genuine `g=2`
dual-shadow interface inherited from RL316.

It proves that chronological composition of the late and early shadow rows
recovers `D0` exactly and leaves a single cofactor residue `epsilon mod H`.
Positive cofactor divisibility gives strict descent to a smaller primitive
`g=2` cycle.  A nonzero residue gives complementary full-denominator
remainders and an exact integer-path wrong-bit clock.

After content reduction the nonzero-residue shadow is precisely the inherited
RL79 canonical generalized-increment cycle for `T_h`, paired with the physical
cycle scaled into the same `T_h` dynamics.  This identifies standalone
quotient/carry invariants as an exact method barrier; only the non-homogeneous
cross-content pairing remains live.

Following the prescribed fallback, RL317 independently replays the first
reduced fibre with a portable exact verifier.  It recovers all sourced RL315
constants and improves the multiplicity cap using RL131's stronger already
certified descent endpoint.

Gate A remains open. Gate B remains open. Global positive non-trivial-cycle
exclusion remains open. No Collatz-conjecture claim is made. The separate Lean
formalisation project is untouched.

## 2. Inherited `g=2` object

Let `(a,ell)` be reduced, `gcd(a,ell)=1`, and put

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`, `D=D0H`.

The genuine balanced rows `u,v` carry the least boundary state `R` to
`x=R+G` and back. With `U=Q(u)`, `V=Q(v)`,

`U=D0R+XG`, `V=D0R-YG`, `U-V=HG`.

Let `tau,sigma` be the rankwise late/early envelope rows and put
`q_tau=Q(tau)`, `q_sigma=Q(sigma)`. RL316 proves

`q_tau+q_sigma=U+V`,

and, with `epsilon=q_tau-U>=0`,

`q_tau=D0R+XG+epsilon`,

`q_sigma=D0R-YG-epsilon`.

The reduced rational shadows strictly and symmetrically bracket `R,x`. The
RL315 quotient is `n=XG+epsilon`, and for fixed `tau`, `n mod X` uniquely
decodes `u`.

## 3. Exact full shadow-composition factorization

For a length-`a`, weight-`ell` row `w`, write

`F_w(t)=(Yt+Q(w))/X`.

Chronological numerator concatenation gives

`Q(tau sigma)=Yq_tau+Xq_sigma=D0(HR-epsilon)`,

`Q(sigma tau)=Yq_sigma+Xq_tau=D0(Hx+epsilon)`.

Thus both full two-row shadow words are automatically `D0`-owned in the
genuine balanced-return setting. Their rational fixed states are

`z_-=R-epsilon/H`, `z_+=x+epsilon/H`,

and `z_-+z_+=R+x`. Positivity of the shadow numerators gives `z_-,z_+>0`.

The roles of the two inherited factors are distinct and essential. Absolute
`D0|U+V` makes the concatenations `D0`-owned; physical `H|U-V` makes `R,x`
integers and leaves exactly

`D|Q(tau sigma) <=> H|epsilon <=> D|Q(sigma tau)`.

Neither factor alone gives this conclusion.

Classification: **analytic theorem**.

## 4. Cofactor-divisible descent

If `epsilon=kH`, both shadow fixed states are the positive integers

`R-k`, `x+k`.

Full numerator divisibility makes the prescribed word a genuine parity-owned
integer Collatz cycle. Indeed, for a binary full word with positive integer
fixed state, reduction modulo two owns the first bit; applying that step gives
the integer fixed state of the one-place rotation, and induction owns the full
orbit.

If `k>0`, the new cycle has a state below `R`. It is primitive of multiplicity
two: a repetition count divides `gcd(2a,2ell)=2`, while repetition twice would
force `tau=sigma`, impossible because `q_tau-q_sigma=HG+2epsilon>0`.

Therefore a least-state primitive `g=2` counterexample has the dichotomy

`epsilon=0` or `H does not divide epsilon`.

At `epsilon=0`, fixed-weight numerator injectivity gives `tau=u` and
`sigma=v`. This is the rankwise ordered-row branch, not row repetition. The
RL21 countermodel saturates this geometry while failing `D0`, so no closure is
claimed.

Classification: **analytic descent theorem**.

## 5. Complementary remainder and integer-path mismatch theorem

In the nonzero-residue branch write

`epsilon=kH+r`, `0<r<H`, and put `M=R-k`, `N=x+k`.

Then

`z_-=M-r/H`, `z_+=N+r/H`,

and exact Euclidean division at `D=D0H` gives

`Q(tau sigma)=D(M-1)+D0(H-r)`,

`Q(sigma tau)=DN+D0r`.

The two nonzero full-D remainders are complementary and sum to `D`.

The integer `M=ceil(z_-)` differs from the lower shadow by `r/H`. Since `H`
is odd and coprime to six, the shadow is a 2-adic integer with exact parity
word `tau sigma`. Two equal-parity Collatz steps divide their difference by
two, with an optional factor three, and lower its 2-adic valuation by one.
Thus the positive integer orbit starting at `M` follows the shadow word for
exactly

`t=v2(r)`

steps, then takes the opposite bit. If `P_j` is the shadow prefix weight,

`M_j-z_j=3^(P_j)r/(2^jH)` for `0<=j<=t`.

Because `0<r<H<2X=2^(a+1)`, `t<=a`. If `t=a`, necessarily `r=X`; the integer
follows all of `tau`, lands at `x+k+1`, and disagrees at the first bit of
`sigma`.

For fixed `tau`, `n mod X` decodes `u`, hence also the full signature

`epsilon=q_tau-Q(u)`, `k`, `r`, `v2(r)`.

The mismatch phase is invariant along the unbounded physical-scale direction
inside a decoded row class.

Classification: **analytic theorem and corollary**.

## 6. Exact generalized-increment reduction and method barrier

Put

`d=gcd(H,epsilon)`, `h=H/d`, `E=epsilon/d`.

Then `h>1`, `gcd(h,E)=1`, and

`Q(tau sigma)=D0d(hR-E)`,

`Q(sigma tau)=D0d(hx+E)`.

As `gcd(D0,H)=1`,

`gcd(D,Q(tau sigma))=gcd(D,Q(sigma tau))=D0d`.

RL79's canonical generalized-increment theorem therefore applies with

`s=D/(D0d)=h`.

The word `tau sigma` is a primitive coprime-content positive integer cycle of

`T_h(y)=y/2` for even `y`, `(3y+h)/2` for odd `y`,

with balanced boundary states

`hR-E -> hx+E -> hR-E`.

Homogeneity, `T_h(hz)=hT_1(z)`, scales the physical cycle into a second
primitive-period `T_h` orbit at `hR,hx`, every state divisible by `h`. The two
boundary pairs have exact symmetric separation `E`.

Comparing the two lower trajectories recovers first disagreement at
`v2(E)=v2(epsilon)`, precisely RL316's row first-difference valuation. It adds
no independent ownership equation.

Consequently standalone quotient/carry, normalized-state, moment, product,
permutation, or other homogeneous `T_h` invariants land exactly in RL79's
binding method barrier and cannot force `h=1`. Future work must consume the
non-homogeneous cross-content relation between the content-`h` and
coprime-content cycles.

Classification: **analytic theorem plus decisive method barrier**.

## 7. Independent exact first-fibre replay

The portable verifier independently implements the frozen RL130 minimum-state
formula, RL134 determinant strip, RL134/RL135 one-period mechanical bound,
RL310 segment-packing inequality, and the accepted RL131 descent endpoint.

It scans every integer `41<=ell<=190537`, 190,497 values with no gaps. The
largest pre-wall odd ceiling is

`7,216,128,937 at ell=158670`.

The first failure is

`(a,ell)=(301994,190537)`,

with integer minimum-state ceiling `984,572,842,736` and odd ceiling
`984,572,842,735`. Exact integers also prove

`2^301993<3^190537<2^301994`, `gcd(301994,190537)=1`.

Rational logarithm intervals certify

`0.000000064507502771755580 < Delta <`
`0.000000064507502771755581`,

`0.017732260045684521336305 < theta <`
`0.017732260045684521336306`,

and `56theta<1<57theta`.

The determinant-zero range `1<=g<=56` has exact one-period least-state ceiling

`R<=710,220,447,737`.

RL315's older-floor cap `g<=10,199,842` is reproduced. Its conditional cap
`g<=9,728,182` attached to the claimed descent through `19,671,092,983` is
also reproduced arithmetically, but that run is not promoted.

RL131 already has a stronger frozen exact all-start descent certificate
through `23,506,639,475`. Using the consequent floor
`R>=23,506,639,477` gives the improved certified cap

`g<=9,355,556`.

The monotone full-count minimum-state expression has exact ceiling

`R<=1,311,372,708,449`

at that cap. This replaces the RL315 rough `1.365e12` scratch estimate.

Certificate file SHA-256:

`dfdb70f67b657410e2219ed3aca79d2116bb5c9c3e8fa434a837bc5d948e0edb`.

Classification: **exact finite arithmetic and rational-interval certificate**.
The old 19.67-billion scratch run is neither needed nor promoted; its entire
range is already covered by RL131. The 11.75-billion-start RL131 computation
is accepted under verification economy and was not rerun.

## 8. Verification

Portable commands from the bundle root:

```sh
python3 -I verification/verify_rl317_dual_shadow_composition.py
python3 -I verification/verify_rl317_cofactor_mismatch.py
python3 -I verification/verify_rl317_generalized_increment_reduction.py
python3 -I verification/verify_rl317_first_reduced_fibre.py
```

All pass. Exact bounded counts:

- 111,350 ordered row-pair composition checks and RL21 missing-`D0` replay;
- 221 `D0`-owned nonzero-remainder mismatch checks;
- 1,024,422 factor/content checks;
- 1,017,228 two-clock checks;
- 190,497 contiguous `ell` values in the first-fibre replay.

The analytic proofs above establish unrestricted identities. Bounded row-word
enumerations are regression evidence, not global certificates.

## 9. Red teams and corrections

1. `D0` and `H` ownership are both used; neither is silently localized.
2. Rational shadows become integer cycles only when full `D` divides their
   numerator.
3. `q_sigma/D0<R` remains noncontradictory by itself.
4. The positive divisible-residue descent preserves primitive multiplicity two.
5. The mismatch clock does not assert that a smaller integer converges.
6. The generalized-increment lift is a barrier, not ordinary ownership.
7. RL206 additive compatibility and RL233 finite-modulus barriers remain.
8. RL315's unverified descent run and its raw scan provenance are not promoted.
9. The RL316 `a<=22` simultaneous-factor scan remains evidence only.
10. `g=1` remains separate.

Two verifier-development defects were repaired before freeze: a test condition
initially omitted inherited `H` ownership, and two harnesses had exact-arithmetic
serialization/type issues. No mathematical theorem or certificate failed.

## 10. Successor frontier

The surviving `g=2` alternatives are exact:

1. `epsilon=0`: rankwise ordered rows `tau=u`, `sigma=v`, still distinct;
2. `epsilon>0`, `H` not dividing `epsilon`: a content-`h` physical copy and a
   coprime-content shadow cycle for the same `T_h`, separated by `E`.

RL318 should seek a non-homogeneous ordinary-`+1` consumer of this pairing or
an order/ownership theorem forcing the ordered rows to agree. It must not
restart standalone `T_h` invariants.

The exact first-fibre fallback is now split into determinant-zero
`1<=g<=56` and determinant-bearing `57<=g<=9,355,556`; support-by-support word
grammar remains forbidden.

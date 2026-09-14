# RL322 proof ledger — negative canonical elimination and positive-branch ownership barrier

Date: 2026-09-14
Status: FROZEN WITH RL322 CLOSEOUT
Incoming BASE_HEAD: `5473c663f2891909c3cece93c4263b4e24715536`

## Scope

Work is in the RL319–RL321 `g=2` late-row-root alternative at the conditional first external survivor

`(a,ell)=(217976794617,137528045312)`,
`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`,

with inherited externally conditional least-state window

`2^71 <= m < 2^75`.

The internal-only frontier remains `ell>=190537`; the external-certificate-conditional frontier remains `ell>=49,547,666,544`. The external `2^71` floor is not re-proved here.

RL321's canonical split is retained:

`w=alpha beta`, `|alpha|=p`, `wt(alpha)=ell`, `|beta|=r`, `wt(beta)=s`,
`z=2^r M+eta`, `0<eta<2^r`,
`2^r J=3^s eta+B`, `0<J<3^s`,
`Z0=XM-Ym`, `W0=Xm-YM>0`.

## RL322.1 — negative-branch prefix rigidity

Assume `Z0<0`. RL321 writes

`n=m-M>=1`, `lambda0=nX-D0m`, `nu=2^r-eta`,

with

`m=floor(nX/D0)`,
`2^29<n<=2^35`,
`A=X-lambda0-2^p nu`.

Let the one positions of the genuine `ell`-odd prefix `alpha` be

`0<=i_1<...<i_ell<p`.

With the ordinary numerator convention,

`A=sum_{j=1}^ell 3^(ell-j) 2^(i_j)`

and the universal minimum is attained at `i_j=j-1`:

`A_min=Y-2^ell`.

Put `E=A-A_min`. RL321's negative-corner estimate gives

`0<=E=D0+2^ell-lambda0-2^p nu < X 2^-40`.

If any of the first 66 ranks were delayed, choose the first delayed rank `j<=66`. Its single contribution to `E` is at least

`3^(ell-j) 2^(j-1) >= 3^(ell-66) 2^65`.

The inherited first-survivor inequality `Y/X>1-2^-40` and the exact elementary check

`3^66/2^105 < 1-2^-40`

imply

`3^(ell-66) 2^65 > X 2^-40`,

contradiction. Therefore

`i_j=j-1` for `1<=j<=66`.

So the actual physical shortcut prefix begins with

`1^66`.

Classification: **analytic ordinary-owned prefix theorem**, conditional only through the inherited first-survivor numerical inequality used above.

## RL322.2 — exact Branch-B elimination

A positive integer whose first 66 shortcut parity bits are all odd satisfies

`m == -1 (mod 2^66)`.

Write

`m=2^66 h-1`.

The inherited state window gives exactly

`33<=h<=512`.

Set

`delta=D0/X=1-Y/X`.

From `m=floor(nX/D0)=floor(n/delta)`,

`m delta <= n < (m+1) delta`.

Hence for each of the 480 possible values of `h`, an integer `n` would have to lie in

`[(2^66 h-1)delta, 2^66 h delta)`.

The portable verifier encloses

`Delta=a log 2-ell log 3`

by the exact rational atanh series, then encloses

`delta=1-exp(-Delta)`

using the alternating Taylor bounds

`x-x^2/2 < 1-exp(-x) < x-x^2/2+x^3/6`.

For every `33<=h<=512`, the resulting rigorous outer interval lies strictly inside one open unit interval `(k,k+1)`. Therefore none contains an integer `n`.

The smallest certified distance to the nearest integer boundary is greater than

`0.000775775058362`.

Thus **the canonical negative branch `Z0<0` is impossible at the conditional first external survivor**, uniformly over all remaining `r,s,beta` support/height.

Classification: **analytic reduction plus exact gap-free finite rational certificate in externally conditional scope**.

## RL322.3 — positive-branch geometry-only ownership barrier

Let

`d=a-ell=80,448,749,305`,

which is odd and satisfies `0<d<ell`. Define exact balanced row words

`u=1^(ell-1)0^d1`,
`v=1^ell0^d`.

Their one positions are rankwise ordered. Root at the last one of `u`. The rooted length-`2a` word is

`W=1^(ell+1)0^d1^(ell-1)0^d`.

For `C(t)` the prefix-one count and `F(t)=aC(t)-ell t`, a four-segment calculation gives `F(t)>=0` at every phase and `F(a)=a>0`. This is therefore an exact model of the nonnegative least-root defect and late-row-root geometry.

The matched-rank canonical split is

`alpha=1^ell`, `p=ell`,
`beta=10^(d-1)`, `r=d`, `s=1`.

Since `d` is odd, the canonical tail residual

`eta=(2^(d+1)-1)/3`

is an integer and follows `beta` to `J=2`:

`2^d J=3 eta+1`.

Thus

`A=Y-2^ell`

and the induced positive-branch affine quantity is

`Zgeom=A-2^ell eta=(3Y-2X-2^(ell+1))/3`.

The inherited exact first-survivor bound `X/Y<1+2^-40` yields

`3Y-2X > Y(1-2^-39)`.

Since `ell>4`, `Y/2>2^(ell+1)`, and `1-2^-39>1/2`; hence `Zgeom>0`.

But also

`0<Zgeom<A=Y-2^ell`,

while `Y-2^ell` is the universal minimum numerator of any length-`a`, weight-`ell` ordinary row. Therefore `Zgeom` is not an ordinary balanced-row numerator.

This is an exact combinatorial countermodel/method barrier at the exact first-survivor pair, not a physical cycle. It proves that positivity of `Z0`, nonnegative least-root defect, ordered rows, matched-rank localization, and canonical tail dynamics do **not** by themselves promote the positive affine quantity to a genuinely owned balanced return.

Classification: **analytic exact combinatorial countermodel / method barrier**.

## Degree of freedom actually removed

RL322 removes one entire sign branch of the RL321 canonical late-row normal form:

`Z0<0` is excluded at the conditional first external survivor for every remaining support height and every tail support.

This is stronger than a parameter narrowing. It is a genuine branch elimination, and within that branch its coercion is support-independent.

However, the surviving `Z0>0` branch retains unbounded support/height, and RL322 proves that the most direct geometry-only ownership promotion is false. No all-scale theorem covering the surviving owned structure is obtained.

Therefore

`PARENT_DIFFICULTY_DELTA = LATERAL`.

The parent should not be labelled EASIER merely because one local sign branch vanished: the project-level missing all-scale ordinary/full-`D` ownership consumer remains unproved.

## Verification

Portable verifier:

`verification/verify_rl322_negative_branch_and_positive_barrier.py`

It performs exact rational logarithm enclosures, the exact 480-case Branch-B unit-interval certificate, the 66-prefix threshold check, and symbolic/arithmetic checks for the Branch-A countermodel.

## Open scope

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
`g=1`: separate and unresolved.
Root-aligned `kappa=0` / actual reverse-crossing obligations remain frozen and unresolved.

# RL322 Branch A geometry-only ownership barrier

Status: VERIFIED AND FROZEN WITH RL322
BASE_HEAD: `5473c663f2891909c3cece93c4263b4e24715536`

Let `d=a-ell=80,448,749,305`, which is odd and satisfies `0<d<ell`.
At the exact first-survivor pair define balanced rows

`u = 1^(ell-1) 0^d 1`,
`v = 1^ell 0^d`.

Their one positions are rankwise ordered. Root at the last one of `u`. The rooted length-`2a` word is

`W = 1^(ell+1) 0^d 1^(ell-1) 0^d`.

For its prefix count `C(n)`, `F(n)=a C(n)-ell n` is nonnegative on every phase. In particular `F(a)=a>0`, so this is late-row-root geometry.

The matched-rank split is

`alpha=1^ell`, `p=ell`,
`beta=1 0^(d-1)`, `r=d`, `s=1`.

Since `d` is odd,

`eta=(2^(d+1)-1)/3`, `J=2`.

Thus

`A=Y-2^ell`

and

`Zgeom=A-2^ell eta=(3Y-2X-2^(ell+1))/3`.

Using the inherited exact first-survivor bound `X/Y<1+2^-40`,

`3Y-2X-2^(ell+1) > Y(1-2^-39)-2^(ell+1)>0`,

where the final inequality follows already from `ell>=4`, `2^(ell+1)<Y/2`, and `1-2^-39>1/2`.

Hence `Zgeom>0`. But

`0<Zgeom<A=Y-2^ell`,

while `Y-2^ell` is the universal minimum numerator of a length-`a`, weight-`ell` ordinary binary row. Therefore `Zgeom` is not such a numerator.

This is an exact combinatorial countermodel/method barrier at the exact first-survivor `(a,ell)`, not a physical cycle. It proves that Branch-A positivity plus nonnegative least-root defect, ordered rows, matched-rank localization, and canonical tail dynamics do not by themselves promote `Z0` to an ordinary balanced return. An additional ordinary/full-`D` physical consumer is required.

Classification: **analytic exact combinatorial countermodel / method barrier**.

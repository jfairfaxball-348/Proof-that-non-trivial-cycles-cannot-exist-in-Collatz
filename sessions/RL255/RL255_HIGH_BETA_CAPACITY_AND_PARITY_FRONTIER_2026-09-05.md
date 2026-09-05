# RL255 — high-beta Branch-C capacity and parity-frontier contraction

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

## Promoted results

For every simultaneous surviving Branch-C object, writing `b=beta(P)`:

1. the exact isolated-singleton / 1-Lipschitz capacity inequality is

`boxed: b+2 <= floor((a-3b+1)^2 / 4)`;

2. every retained object satisfies

`boxed: a>=1100, z>=406, ell>=694`;

3. the resonance corridor sharpens uniformly to

`boxed: a/ell <= 233/147`,

hence

`z/a <= 86/233`, `H/a <= 3/233`;

4. in the non-halving branch (`H,n` not both even),

`boxed: beta(P)>=356`

and the physical complement packing inequality

`boxed: a-36H >= 1068`

holds;

5. every non-halving survivor satisfies

`boxed: a>=1986, z>=733, ell>=1253`.

The first uniform arithmetic selector not eliminated by these RL255 inequalities is uniquely the halving tuple

`boxed: (a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

At that first frontier, the exact half-window parameters are `K=7`, `t=2`, and the retained beta range is finite:

`260 <= beta(P) <= 354`.

## 1. Branch-C positive-profile capacity theorem

Branch C has isolated negative singleton roots. Because

`P_(i+1)-P_i in {-1,0,1}`,

an isolated negative root must be exactly `-1`, and successive negative roots have cyclic distance at least three.

Let the `b` cyclic distances between successive `-1` roots be

`g_1,...,g_b`, with `g_j>=3`, `sum g_j=a`.

Inside a gap of length `g`, every profile is bounded above by the two-sided 1-Lipschitz tent

`-1 + min(t,g-t)`.

Therefore the positive P-mass in that gap is at most

`C(g)=floor((g-2)^2/4)`.

Write `x=g-3>=0` and `f(x)=C(3+x)=floor((x+1)^2/4)`.
The function `f` is superadditive on nonnegative integers. The four parity cases give directly:

- even/even excess `2uv`;
- even/odd excess `2uv+u`;
- odd/even symmetrically;
- odd/odd excess `2uv+u+v`.

Hence total positive mass is maximised, for fixed `a,b`, by placing all length excess into one gap:

`sum C(g_j) <= C(a-3(b-1))`.

RL254 gives total positive P-mass exactly `b+2`, so

`b+2 <= floor((a-3b+1)^2/4)`.

This is an analytic necessary condition, not a heuristic density estimate.

For the RL254 branch floors this gives:

- halving `b>=260` => `a>=812`;
- non-halving `b>=355` => `a>=1102`.

## 2. Exact first-frontier contraction

Combine:

- the RL254 parity split;
- zero budget `b<=z-k+4`;
- retained `k>=31`, so `z>=b+27`;
- the capacity inequality above;
- the exact resonance window;
- `19/12<a/ell<=149/94`;
- determinant selector `a r-q ell=2`.

A complete exact integer scan through `a<=1100` leaves exactly one selector after the branch-specific beta/capacity tests:

`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

All smaller determinant/resonance candidates fail either the halving capacity floor or the stronger non-halving capacity/zero-budget floor.

Therefore every retained Branch-C object has

`a>=1100`.

The same exact scan shows no retained object with `z<406`; and `a/ell<=149/94` then gives `ell>=694`.

Thus

`boxed: a>=1100, z>=406, ell>=694`.

The first retained tuple is halving, because `H=14` and `n=4`.

## 3. Resonance sharpening to 233/147

With `ell>=694`, suppose

`a/ell > 233/147`.

Integrality gives

`147a-233ell>=1`.

Therefore

`a-log_2(3) ell >= ell(233/147-log_2(3))+1/147`.

Already at `ell=694` this exceeds the retained upper phase width

`(1/2)log_2(16/15)`,

contradicting the exact resonance window.

Hence

`a/ell <= 233/147`.

Equivalently,

`z/a <= 86/233`.

For `H=19z-7a`,

`H/a <= 19*(86/233)-7 = 3/233`.

## 4. Non-halving: use all 38 useful 38-windows

RL254 used 37 useful 38-windows. The sharper `H/a<=3/233` permits the full useful family of 38 windows with starts

`-51,-50,...,-14`.

Their guaranteed zero excess over the baseline 14 totals exactly

`358`.

They are pairwise q-segment disjoint. If two starts differ by `1<=d<=37`, overlap gives

`mq-ca=d`, `0<|m|<H`.

Combining with `Hq-na=38` gives

`a | (38m-Hd)`.

But

`|38m-Hd| <= 38(H-1)+37H = 75H-38 < a`

because `H<=3a/233`. Hence `38m=Hd`.

If `d!=19`, then `19|H`; the companion relation forces `19|n`, hence `19|a,q`, contradicting `gcd(a,q)|2`.

If `d=19`, then `H=2m`; the companion relation forces `n` even, so `H,n` are both even, contradicting the non-halving hypothesis.

Thus all 38 segments are disjoint, and total positive P-mass is at least 358:

`b+2>=358`.

So

`boxed: b>=356`

in the non-halving branch.

## 5. Non-halving physical complement packing

Let `U` be the union of those 38 q-segments. Because the starts are consecutive and the segment map is injective, `U` is also the disjoint union of `H` physical intervals, each of length 38.

Let `N_U` be the number of Branch-C negative roots in `U`. Since every negative root is `-1` and the raw P-sum on `U` is at least 358, the positive mass inside `U` is at least

`358+N_U`.

Total positive mass is `b+2`, hence

`N_U <= b-356`.

Therefore at least

`b-N_U >= 356`

negative singleton roots lie outside `U`.

The complement of `H` disjoint length-38 blocks has total length `a-38H` and at most `H` physical gaps. A gap of length `g` contains at most `ceil(g/3)` negative roots because Branch-C negative roots have cyclic spacing at least three. Thus the complement can contain at most

`sum ceil(g_j/3) <= (a-38H+2H)/3 = (a-36H)/3`

negative roots.

Since it must contain at least 356,

`boxed: a-36H >= 1068`.

This is a finite-site packing theorem, not a measure/density argument.

## 6. Exact non-halving frontier

Now combine, in the non-halving branch:

- `b>=356`;
- `z>=b+27>=383`;
- the capacity theorem, giving `a>=1105`;
- `a/ell<=233/147`;
- determinant/resonance eligibility;
- `a-36H>=1068`.

An exact scan through the first surviving scale eliminates every non-halving selector below

`(a,ell,z,q,r,H,n)=(1986,1253,733,1352,853,25,17)`.

Thus every non-halving survivor satisfies

`boxed: a>=1986, z>=733, ell>=1253`.

The tuple above is the first non-halving arithmetic selector not killed by the RL255 inequalities; it is not claimed to be a genuine full-phase cycle.

## 7. First halving frontier data

The uniform first surviving selector remains

`(1100,694,406,317,200,14,4)`.

Here

`K=H/2=7`, `t=n/2=2`,

so the exact 19-window relations are

`7q = 2a+19`,
`7B = 2z+7`.

The capacity theorem at `a=1100` excludes `b>=355`, while RL254 gives `b>=260`. Hence

`260<=b<=354`.

Zero budget then gives

`31<=k<=z-b+4<=150`.

This finite halving frontier is the natural next target.

## Scope

RL255 materially contracts the high-beta Branch-C bridge but does not close a gate.

- Gate A: open.
- Gate B: open.
- Radius 4: not invoked.
- Radius 5: inactive.
- No global cycle exclusion is claimed.

Large `beta(E)` remains only physical-envelope information; it is not converted to Radius 4 without the exact ownership/distance hypotheses.

All RL249/RL250 demotions remain binding. RL251 Gabriel-horn equivalence remains frozen.

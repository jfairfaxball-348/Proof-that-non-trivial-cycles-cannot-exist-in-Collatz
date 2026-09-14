# RL323 proof ledger — physical H-carry crossing and zero-carry matched-rank contraction

Date: 2026-09-14
Status: FROZEN CANDIDATE FOR RL323 CLOSEOUT
BASE_HEAD: `d060213279faecb865b0ef6566aa6aff35ec6972`
Incoming authoritative tree: `b6dc892b587618b6327aa67375a40f84042ec58b`

## Scope retained

Work remains in the `g=2` ordered late-row branch inherited from RL315–RL322.

At the conditional first external survivor,

`(a,ell)=(217976794617,137528045312)`,

put

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`, `d=a-ell=80448749305`.

The inherited external least-state window remains conditional:

`2^71 <= m < 2^75`.

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.

Gate A remains OPEN. Gate B remains OPEN. Global positive non-trivial-cycle exclusion remains OPEN. `g=1` remains separate.

## RL323.0 — correction of unpromoted scratch

An early scratch route defined a normalized matched-rank defect at odd ranks and proved a correct interior recurrence. It then attempted to close that recurrence cyclically with a sign-flipping wrap identity.

That wrap identity is invalid: after the final odd rank of one balanced row, the physical transition lands in the other row, so the same-rank defect does not close on itself in the asserted way.

The proposed cyclic one-crossing theorem derived from that wrap is WITHDRAWN. It was never authoritative and no earlier RL result is affected.

A later checkpoint also described a bound on a post-crossing physical tail as a matched-rank displacement too strongly. That label is corrected below: RL323.3 supplies the actual matched-rank displacement theorem.

Classification: explicit correction/demotion of unpromoted scratch only.

## RL323.1 — phase-aligned physical H-carry recurrence

Use the genuine ordered balanced rows `u,v` of length `a`, weight `ell`, with physical boundary states

`u: R -> x=R+G`,
`v: x -> R`,

and rankwise ordered one positions.

For aligned phase `t`, let `U_t,V_t` be the actual physical states in rows `u,v`, and put

`c_t=C_v(t)-C_u(t) >= 0`,
`D_t=3^(c_t) U_t - V_t`.

The ordinary shortcut map gives the exact one-step recurrence

- `(u_t,v_t)=(0,0)`: `D_(t+1)=D_t/2`;
- `(1,1)`: `D_(t+1)=(3D_t+3^(c_t)-1)/2`;
- `(0,1)`: `D_(t+1)=(3D_t-1)/2`;
- `(1,0)`: `D_(t+1)=(D_t+3^(c_t-1))/2`, where necessarily `c_t>=1`.

Hence

`D_t>0 => D_(t+1)>0`.

At the row endpoints,

`D_0=R-x=-G<0`,
`D_a=x-R=G>0`.

Therefore there is a unique transition from the nonpositive region into the positive region. After that transition `D_t` stays positive to the row endpoint.

This recurrence uses the actual ordinary `+1` dynamics and is not available in the RL322 geometry-only countermodel.

Classification: analytic ordinary-physical theorem, support-uniform.

## RL323.2 — full `D0/H` ownership at every aligned phase

The actual length-`a` segment from `U_t` to `V_t` has weight `ell+c_t`; the complementary actual length-`a` segment from `V_t` to `U_t` has weight `ell-c_t`.

Let their genuine ordinary numerators be `A_t,B_t`. Then

`X V_t = 3^(ell+c_t) U_t + A_t`,
`X U_t = 3^(ell-c_t) V_t + B_t`.

Exact elimination gives

`A_t + 3^(c_t) B_t = D0(3^(c_t) U_t + V_t)`,          (2.1)

`3^(c_t) B_t - A_t = H D_t`.                           (2.2)

Thus `D_t` is exactly the `H`-factor quotient of a difference of two genuinely owned ordinary numerators. No affine surrogate is promoted to ownership.

At the least-root phase, (2.1)–(2.2) specialize to the frozen RL320 weighted `D0/H` factorization with `D_t=-K`.

Classification: analytic full ordinary ownership identity, support-uniform.

## RL323.3 — zero-carry matched-rank crossing theorem

Let `t` be the phase immediately before the unique transition into `D>0`.

The transition cannot occur on `(0,0)` or `(0,1)`, so `u_t=1`. Write `t=u_j`, the `j`-th one position of the late row, and put

`h=c_t`.

The rankwise ordered early row has `v_j<u_j`, and the genuine physical interval

`beta = v[v_j:u_j]`

has

`r=|beta|=u_j-v_j`,
`wt(beta)=h`.

Thus `r` is a genuine matched-rank displacement and `r>=h`.

Put

`P=U_t`, `Q=V_t`.

Since `D_t<=0`, write

`E=Q-3^h P=-D_t >=0`.

The crossing recurrence, in either possible crossing case `(1,1)` or `(1,0)`, forces

`0 <= E < 3^(h-1)`.

Now apply the ordinary Euclidean tail transport to the actual tail `beta`.
Let `z` be its genuine starting state, write

`z=2^r M+eta`, `0<eta<2^r`,

and let `J=T^r(eta)`. Then

`2^r J=3^h eta+B`,
`Q=3^h M+J`,
`0<J<3^h`.

But `0<=Q-3^hP<3^h`, so the common quotient is exactly

`M=P`.

Therefore

`E=J`, and in fact

`0<J<3^(h-1)`.                                          (3.1)

Consequences:

- `D_t<0` strictly immediately before the first positive crossing;
- `h>=2`;
- the first physical crossing has exactly zero integer carry:
  `floor(Q/3^h)=P`;
- the canonical dyadic residual lies in the bottom third:
  `0<eta<2^r/3`, because `B>0` in
  `2^rJ=3^h eta+B`.

These are support-uniform and do not use the external `2^71` floor.

Classification: analytic ordinary-owned matched-rank theorem, support-uniform.

## RL323.4 — genuinely owned narrow prefix window

Let `alpha` be the complementary first part of the same actual length-`a` segment, so

`w=alpha beta`,
`|alpha|=p`,
`wt(alpha)=ell`,
`p+r=a`.

Let `A=Q(alpha)`. Since `M=P`,

`z=2^rP+eta`.

The genuine prefix equation

`2^p z=Y P+A`

therefore gives

`A=D0 P+2^p eta`.                                        (4.1)

Using `0<eta<2^r/3` and `p+r=a`,

`D0 P < A < D0 P + X/3`.                                (4.2)

Thus the first physical crossing forces a genuinely owned length-`p`, weight-`ell` numerator into an `X/3`-wide interval, independently of support.

Classification: analytic ordinary-owned support-uniform contraction.

## RL323.5 — conditional multi-billion zero-count / matched-displacement bound

Now use the inherited external least-state floor `m>=2^71`.

Put

`q=p-ell`.

This is the number of zero bits in `alpha`, and

`r=d-q`.

Because `alpha` starts at the odd physical state `P`, let

`0=i_1<i_2<...<i_ell<p`

be its one positions. Every odd state encountered in `alpha` is an actual cycle odd state and hence is at least `m`.

Comparing state growth up to the `j`-th odd event gives

`2^(i_j) <= (P/m)(3+1/m)^(j-1)`.                        (5.1)

Also, since `alpha` has only `q` zeros,

`i_j <= q+j-1`.                                          (5.2)

The ordinary numerator expansion is

`A/(YP)=sum_(j=1)^ell 2^(i_j)/(3^j P)`.

Combining (5.1) and (5.2), splitting after rank `2q`, and bounding the remaining geometric tail yields

`(D0/Y)m < (2q/3)(1+2^-34)+1`.                          (5.3)

The factor `1+2^-34` is justified by

`(1+1/(3m))^ell <= 1/(1-ell/(3m)) < 1+2^-34`.

Using the same exact rational atanh-series enclosure for

`Delta=a log 2-ell log 3`

as the frozen RL322 verifier, together with

`D0/Y=e^Delta-1>Delta`

and `m>=2^71`, the portable RL323 verifier proves that (5.3) is impossible for

`q<=3182833229`.

Therefore

`q>=3182833230`.                                         (5.4)

Since `d=80448749305`,

`r=d-q <= 77265916075`.                                  (5.5)

Finally,

`2<=h<=r<=77265916075`.                                  (5.6)

This is an exact support-independent bound on a forced genuinely owned matched-rank interface, conditional on the inherited external least-state floor and exact first external survivor.

Classification: analytic reduction plus exact rational constant certificate in externally conditional scope.

## What RL323 does and does not close

RL323 materially advances the parent-level ownership programme:

- the entire ordered physical interface has a genuine `H`-carry sign law;
- a unique physical sign transition is forced;
- at that transition an actual matched-rank interval has zero integer carry;
- the ordinary residual is forced into the bottom third of its dyadic cell;
- the complementary genuine `ell`-odd prefix lies in an `X/3` ownership window;
- at the conditional first external survivor the forced matched-rank displacement and height are absolutely bounded.

But RL323 does NOT yet prove the literal smallest RL323 target for the original least-root canonical interface. In particular it does not prove that the least-root canonical `r,s,beta` itself is bounded, nor does it construct a strictly smaller owned reduced balanced return.

No finite enumeration of the bound `77265916075` is claimed or licensed.

Gate A, Gate B, the global positive non-trivial-cycle exclusion, and `g=1` remain open.

`PARENT_DIFFICULTY_DELTA = EASIER`

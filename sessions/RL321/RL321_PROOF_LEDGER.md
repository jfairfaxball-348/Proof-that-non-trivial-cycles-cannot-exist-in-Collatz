# RL321 proof ledger — canonical residual ownership, matched-rank tail, and bounded-carry collapse

Date: 2026-09-14
Status: FROZEN WITH RL321 CLOSEOUT

## Scope

Work is in the RL319/RL320 late-row-root alternative at the conditional first external survivor

`(a,ell)=(217976794617,137528045312)`,
`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`,

with inherited externally conditional least-state window

`2^71 <= m < 2^75`.

The internal-only frontier remains `ell>=190537`; the external-certificate-conditional frontier remains `ell>=49,547,666,544`.

## RL321.1 — exact genuine prefix/tail split

Let the actual late-rooted first half have length `a`, weight `ell+s`, start at the global least odd state `m`, and end at antipode `y`. Cut immediately before its last `s` one-bits:

`w=alpha beta`, `|alpha|=p`, `|beta|=r=a-p`, `wt(alpha)=ell`, `wt(beta)=s`.

Let `z` be the genuine cut state and `A=Q(alpha)`, `B=Q(beta)`. Then

`2^p z = Y m + A`,
`2^r y = 3^s z + B`,
`U_s = 3^s A + 2^p B`.

For any RL320 decomposition `K=y-3^s m=3^s c+theta`, set `N=m+c`, `Z=XN-Ym` and `L=z-2^rN`. Exact algebra gives

`A-Z=2^p L`,
`3^s L=2^r theta-B`.

Since `beta` begins with `1`, `B` is odd and therefore `L` is odd. Hence

`v2(A-Z)=p` exactly.

Classification: analytic ordinary-owned split.

## RL321.2 — tail-residue saturation barrier

For every `s>=1` and every unit residue `theta (mod 3^s)`, some suffix

`beta=1^s0^t`

realizes

`B == 2^(s+t) theta (mod 3^s)`.

The realization can be chosen as a genuine positive ordinary tail above the least state under the inherited external scale window. Therefore suffix congruence, suffix ownership, and the least-state floor alone do not constrain the nonzero ternary residue.

Classification: analytic local physical-run counterfamily / method barrier. It is not a cycle.

## RL321.3 — canonical positive remainder and common quotient

Define the genuine Euclidean quotient and remainder at the cut by

`M=floor(z/2^r)`, `eta=z-2^rM`, `0<eta<2^r`.

The gap `z-eta=2^rM` forces `eta` to follow the same genuine `r`-bit tail `beta`. Put `J=T^r(eta)`. Then

`2^r J=3^s eta+B`,
`y=3^sM+J`.

For every positive `n<2^R` following an `R`-step shortcut word with `q` odd bits, induction gives

`T^k(n)<3^(q_k)2^(R-k)`,

so in particular

`0<J<3^s`.

Thus

`M=floor(z/2^r)=floor(y/3^s)`.

Writing `c0=M-m`, the late-row contact has the canonical ordinary-owned decomposition

`K=3^s c0+J`, `0<J<3^s`, `3 does not divide J`.

The inherited physical prefix/complement inequalities and first-survivor logarithmic cap give

`-2^35 <= c0 < 2^35`.

Define

`Z0=D0m+Xc0=XM-Ym`,
`W0=D0m-Yc0=Xm-YM`.

Then `W0>0`; `Z0` is odd, hence `Z0>0` or `Z0<0`.

Classification: analytic ordinary-owned theorem, conditional only where the inherited external state scale is used for the numerical carry cap.

## RL321.4 — two genuine ell-odd proper-factor identities

Let `C` be the numerator of the genuine complementary `ell`-odd segment from `z` back to `m`. Then

`2^r A+C=D0(z+2^r m)`,
`2^r A-C=H(z-2^r m)`.

Both segments are ordinary-owned. This is not a relabelling of RL320's non-owned balanced surrogate and does not split RL147's mixed-height layers.

Classification: analytic ordinary ownership identity.

## RL321.5 — matched-rank support localization

Return to the inherited ordered balanced rows `u,v`, with one-positions rankwise ordered `u_j>=v_j`. If the global least odd state occurs at the `j`-th one of the late row `u`, then the canonical RL321 tail is exactly

`beta=v[v_j:u_j]`,
`r=u_j-v_j`,
`wt(beta)=s`.

Thus the tail length is the displacement of one matched physical rank, and `r>=s`.

Classification: analytic support-localization theorem.

## RL321.6 — bounded post-antipode residual exit clock

From `z-eta=2^rM`, integer parity synchronization gives identical parity bits for exactly

`r+t0`, where `t0=v2(M)`.

After the first `r` tail bits carry `z->y` and `eta->J`, the residual integer `J` follows the genuine second half from `y` for exactly `t0` further phases, then takes the opposite bit.

Under the inherited external scale,

`2^71-2^35 <= M < 2^76`,

so

`t0<=75`.

If `Z0<0`, then `M<m<2^75`, so `t0<=74`.

The first residual mismatch is not itself a crossing/descent contradiction: immediately before it the physical/residual gap ratio is still `>2^39`.

Classification: analytic ordinary-owned localization + exact integer comparison.

## RL321.7 — negative-corner duality and saturation barrier

In the `Z0<0` branch put

`nu=2^r-eta`, `D=3^s-J`.

The complementary residual follows the same word `beta` under

`T_-(n)=n/2` for even `n`, `(3n-1)/2` for odd `n`,

and lands at `D`:

`2^r D=3^s nu-B`.

The corner is locally saturated at arbitrary height: for every `h>=40`,

`r=s=h`, `beta=1^h`, `eta=2^h-1`, `J=3^h-1`, `nu=D=1`

satisfies the local residual dynamics. Therefore tail-only corner geometry cannot bound `r` or `s`.

Classification: analytic duality theorem + exact local method barrier. This is not a cycle.

## RL321.8 — negative-branch Beatty bounded-carry collapse

Assume `Z0<0`. Put

`n=-c0=m-M>=1`, `lambda0=-Z0=nX-D0m>0`, `nu=2^r-eta>=1`.

The genuine prefix identity becomes

`A=X-lambda0-2^p nu`.

The universal fixed-weight numerator minimum is

`A>=Y-2^ell`.

Hence

`lambda0+2^p nu <= D0+2^ell`.

This forces

`0<lambda0<D0`,

so the physical least state is uniquely determined by the bounded carry:

`m=floor(nX/D0)`.

Equivalently

`M=floor(Ym/X)`,
`lambda0=Ym mod X`, `0<lambda0<D0`.

Conditional on the external least-state floor and the inherited carry bound,

`2^29<n<=2^35`.

Using RL319's exact logarithmic cap and `a-ell=80,448,749,305`,

`(D0+2^ell)/X<2^-40`.

Therefore

`1<=nu<2^(r-40)`, so `r>=41`,

and from `2^rD=3^snu-B`,

`0<D/3^s<2^-40`, so `s>=26`.

Classification: analytic ordinary-owned contraction; the lower bound `n>2^29` is externally conditional. This is not yet a gap-free finite exclusion: the carry range is bounded, but support parameters remain.

## Correction / demotion

An attempted all-rank bound used the root-aligned estimate `G<2^35` inside the distinct late-row-root branch. That scope transfer is invalid. The resulting proposed bound `u_q<=floor(aq/ell)+37` and any height-38 consequence are DEMOTED and NOT promoted.

## Final scope

No branch is closed globally. Gate A remains open. Gate B remains open. Global positive non-trivial-cycle exclusion remains open. `g=1` remains separate.

`PARENT_DIFFICULTY_DELTA = EASIER`

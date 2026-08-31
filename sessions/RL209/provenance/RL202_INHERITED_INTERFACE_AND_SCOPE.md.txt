# RL202 inherited interface and scope

Date: 2026-08-31. All physical implications remain conditional on the sole high
branch `(37,0,23,-1)`.

Use
`A=217976794617`, `L=137528045312`, `B=80448749305`,
`R=57079296007`, `p=65470613321`, `u0=103768467013`,
`z=L-p=72057431991`, `Ap-u0L=1`, `pB=1 mod L`.
For canonical phase i, rank is `r_i=iB modL`, inverse phase `I(r)=pr modL`,
`b_i=floor(Ai/L)`, `rho_i=2^b_i/3^i`, and physical heights are nonnegative
integers with `h_0=0` and `a_i=b_(i+1)-b_i+h_i-h_(i+1)>=1`.
Inherited anchors include `h_0=h_1=h_p=h_(p+1)=0`.

Set `lambda=2^A/3^L`, `delta=ln(lambda)`, `0<delta<2^-40`,
`K_0=2^37`, `K_(i+L)=lambda K_i`, and `v_i=2^(-h_i)`.
At every noncarry source,
`3(K_(i+1)-K_i)=rho_i(v_(i+p)-v_i)`.
The unique p-shift carry source is phase `z=L-p`; canonical `rho_0=1` and
`1/2<rho_i<1` for `0<i<L`.

For H21, retain the binding `{33,34,35}` family and terminal constant
`T=7*3^35=350220815692997949`. At tau34 the two oriented endpoints have common
height one and
`Y^-_0=2^34 eta-1`, `Y^+_0=2^34(eta+21)-1`.
The next 33 acceleration exponents are exactly one. The four necessary eta
classes remain `0,8,9,17 mod18` with the inherited Hensel/lift exclusions.

RL201 incoming necessary terminal ranks are
`[25583192106,41775866136]` minus the 12 isolated deletions
`26058127773,26058127774,28746802249,28746802250,31435476726,
34124151202,36398517184,36398517185,36812825678,39087191660,
39087191661,41775866136`, for 16,192,674,019 ranks.
The exact terminal law is
`K_H21(r)=rho_(I(r))*T/2^21`, strictly decreasing in canonical rank.

RL201's exact joint-prefix identity, continuous-mass relaxation barrier, coupled
finite reverse barrier, support correction and RL195 complete-word denominator
equivalence all remain binding. Necessary ranks are not physical realizations;
no H21 charge or global closure is inherited.

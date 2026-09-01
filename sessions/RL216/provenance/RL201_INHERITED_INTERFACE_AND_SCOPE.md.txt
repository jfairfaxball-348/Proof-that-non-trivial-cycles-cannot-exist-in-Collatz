# RL201 inherited interface and scope

Date: 2026-08-31. All physical implications are conditional on the sole high branch
`(37,0,23,-1)`. This file restates load-bearing inherited data; it does not promote
new historical discoveries or replace earlier correction/demotion ledgers.

## Constants, phase and normalized quantities

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`R=2L-A=57079296007`, `p=65470613321`, `u0=103768467013`.
`Ap-u0L=1`, `pB=1 mod L`, `t=L-p=72057431991`.
For every lifted integer phase i, set `b_i=floor(Ai/L)`, `c_i=b_(i+1)-b_i`.
Canonical rank is `r_i=iB mod L`; inverse phase is `I(r)=pr mod L`.
The mechanical bit is 1 for `r_i<R`, 2 otherwise.

A complete admissible height word is L-periodic with nonnegative integer h,
`h_0=0`, and `a_i=c_i+h_i-h_(i+1)>=1` at every phase. The physical orbit has
positive odd integers y satisfying `3y_i+1=2^a_i y_(i+1)`, `y_(i+L)=y_i`.
Define `S_i=b_i-h_i`, `rho_i=2^b_i/3^i`, `q_i=rho_i*2^(-h_i)`,
`x_i=y_i/2^h_i`, and `z_i=q_i*y_i=rho_i*x_i`.
Write `lambda=2^A/3^L>1`, `alpha=3^p/2^u0>1`,
`beta=(alpha-1)/(lambda-1)>0`. The lifted rho,q,z,K multiply by lambda
after L; h,y are periodic. Exact logarithmic defect:
`delta=A ln2-L ln3`, `0<delta<2^-40`. Canonical `1/2<rho_i<=1`.

`C_i=sum_(i<=j<i+p)q_j`, `Y_i=sum_(i<=j<i+L)q_j`, with lifted terms.
Inherited transport and inversion are `3(z_(i+1)-z_i)=q_i` and
`3K_i=alpha*C_i+beta*Y_i`. The branch has exact `K_0=2^37`, and canonical
full-period corridor `128081997553<K_i<146795909391`.
The signed defect is `G_i=h_i-h_(i+p)`. At a noncarry source the inherited drift is
`K_(i+1)-K_i=q_i(2^G_i-1)/3`; this is the case used by the terminal consumer.
This noncarry formula is not asserted unchanged at the separate p-shift carry.
Inherited anchor data include `h_0=h_1=h_p=h_(p+1)=0`, `a_0=1`, and
`G_0=G_1=...=G_23=0`; these are not supplied by an arbitrary local fixture.

The p-shift carry is `epsilon(i)=b_(i+p)-b_i-u0`, equal to 1 only at rank L-1.
The normalized gap is `K_i/rho_i=2^epsilon(i)*x_(i+p)-x_i`, using periodic x.
This is distinct from chronological canonical wrap i=L-1, whose source rank is R.
The two mechanical p-shift seam phases are t-1 and t.

## H21 oriented interface and inherited rank frontier

Binding H21 family: `{33,34,35}`; canonical inherited floor 67 remains unchanged.
At tau=34 the ordered endpoints have common height one and
`Y^-_0=2^34 eta-1`, `Y^+_0=2^34(eta+21)-1`.
For `0<=s<=33`, `Y^-_s=2^(34-s)3^s eta-1` and
`Y^+_s=2^(34-s)3^s(eta+21)-1`; the first 33 exponents are exactly one.
The preterminal common height is 20, mechanical bit 2; the terminal maximum height
is 21. `C34=21*2^34=360777252864`, `Cpre=14*3^34=233480543795331966`,
`T=7*3^35=350220815692997949`, terminal gap `Delta=T/2^21`.

State 011 is exactly eta=0 mod9, common tau35 height 0 and leading exponent 1.
State 111 is exactly eta=8 mod9, common tau35 height 1 and leading exponent 2.
The terminal sign is positive for even eta (lower labelled endpoint at height21),
negative for odd eta (upper labelled endpoint at height21).
For positive sign `nu=v2(3^34(eta+21)-1)`; for negative sign
`nu=v2(3^34 eta-1)`. The other terminal height is `21-nu`; `1<=nu<=21`.
The four necessary eta classes are 0,8,9,17 modulo18.

With M=37748736=9*2^22, inherited all-rank Hensel exclusions are:
class0:18670500; class8:1893284; class9:6087609; class17:27059129 modulo M.
They exclude nu>=22, not entire mod18 classes.

RL200 core: `D_K=[25583192106,41775866136]`, with 12 isolated deletions:
`26058127773,26058127774,28746802249,28746802250,31435476726,34124151202,
36398517184,36398517185,36812825678,39087191660,39087191661,41775866136`.
The interval has 16192674031 ranks; after deletions 16192674019 necessary ranks
remain. RL200 removed 2213738806 formerly surviving necessary ranks. None is a
physical population count. Exact terminal law:
`K_H21(r)=rho_(I(r))*T/2^21`, strictly decreasing in canonical rank.
The tau34 rank is `(r-34B) mod L` in `[40886621976,57079296006]`.
The tau36 and tau37 source rank intervals are respectively
`[17517168678,33709842708]` and `[74596464685,90789138715]`, giving extra
backward source bits 1,2. The signed next increment is
`sigma*rho_(I(r))*(2^nu-1)/(3*2^21)`.

## Binding denominator and method boundaries

Inherited RL195: a complete admissible integer height word reconstructs a unique
positive rational orbit; every reduced odd denominator is the same. A dyadic
normalized p-gap, in particular the exact K0=2^37 moment, forces that orbit to
be positive odd-integral. Thus generic integrality is not another missing test
once the full admissible word and exact moment are given. Intervals, local
templates and arbitrary continuous q words do not meet those hypotheses.

Retain RL199's unoriented common-pair information-loss result and RL200's finite
uncoupled reverse-prehistory barrier. RL201's new coupled barrier is qualified
separately and does not rule out full-word, anchored or overlap consumers.
Do not revive the excluded H21 zero-edge route, replace owned H21 incidence with
N0/J00 abundance, identify rank order with chronological order, or turn variation
into excursion. All finite-cutoff, canonical-lift, physical/necessary, charging,
branch, Gate A/B, and global proof-state qualifications remain binding.

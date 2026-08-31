# RL206 corrected inherited H21 interface for RL207

All physical implications are conditional on the sole high branch
`(37,0,23,-1)`. Necessary labels are not physical realizations or charges.

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`, `pB=1 modL`,
`z=L-p=72057431991`, `lambda=2^A/3^L`, `0<ln(lambda)<2^-40`.
Canonical phase i has rank `r_i=iB modL`; inverse phase `I(r)=pr modL`.
`b_i=floor(Ai/L)`, `rho_i=2^b_i/3^i`, `S_i=b_i-h_i`,
`q_i=2^S_i/3^i=rho_i 2^(-h_i)`, `P_a=sum_(0<=j<a)q_j`.
Heights are nonnegative integers with
`a_i=b_(i+1)-b_i+h_i-h_(i+1)>=1` and
`h_0=h_1=h_p=h_(p+1)=0`. The physical height word is L-periodic;
q, rho and K have their inherited lambda-quasiperiodic lift.

Write `alpha=3^p/2^u`, `beta=(alpha-1)/(lambda-1)`,
`C_i=sum_(i<=j<i+p)q_j`, `Y_i=sum_(i<=j<i+L)q_j`, using lifted q.
The inherited potential is `3K_i=alpha C_i+beta Y_i`, with `K_0=2^37`.
At noncarry sources, `3(K_(i+1)-K_i)=rho_i(2^(-h_(i+p))-2^(-h_i))`.
The unique p-shift carry must be handled using the lifted convention.

## Source versus terminal

At a tau34 source phase a, the paired oriented endpoints have common height one,
`Y^-_0=2^34 eta-1`, `Y^+_0=2^34(eta+21)-1`. The next 33 chronological
acceleration exponents are one. The terminal phase is `i=a+34 modL` and
its rank is `r=iB modL`; source rank is `(r-34B) modL`.
The retained tau family is `{33,34,35}`, terminal constant
`T=7*3^35=350220815692997949`, and `K_H21(r)=rho_(I(r))*T/2^21`
is strictly decreasing in terminal rank.

The exact necessary terminal predicate is the inclusive interval
`[25583192106,41775866136]`, minus the twelve isolated ranks
`26058127773,26058127774,28746802249,28746802250,31435476726,
34124151202,36398517184,36398517185,36812825678,39087191660,
39087191661,41775866136`, minus the four anchor ranks
`26058127775,28746802251,36398517186,39087191662`, and minus ranks whose
terminal phase is in `[0,2^24)` or `[L-2^24,L)` while their rank is outside
`[38643145224,38659291956]`. Its inherited exact cardinality is
**16,188,727,234**. The untranslated source core is instead
`[40886621976,57079296006]`; transport every exclusion with its correct phase.

Eta classes remain `0,8,9,17 mod18`. Eta mod9 chooses the inherited 011/111
state; parity chooses terminal orientation. For even eta use odd `s=eta+21`
and positive sign; for odd eta use odd `s=eta` and negative sign.
Terminal valuation `nu=v2(3^34 s-1)` must satisfy `1<=nu<=21`; terminal
heights are 21 and 21-nu. The forbidden Hensel residue has nu>=22, equivalently
`s=(3^34)^(-1) mod2^22`. At terminal rank 25583192106 the additional
first-rank cuts forbid eta 37544868 (class0) and 20767652 (class8) modulo
37748736 only at that rank. Do not generalize these to whole eta classes.

## Exact endpoint moment and corrected boundary

`3(alpha-1)rho_a(2^33 eta-1/2)=3K_0-alpha P_p+(alpha-1)P_a`.
Let `d=3^p-2^u` and
`E_a=3*2^(u+37)-3^p P_p+d P_a`.
At source height one, `U_a=E_a/2^(b_a-1)=d 3^(1-a)(2^34 eta-1)`.
All denominator powers of 3 are odd units in the 2-adic calculations.
Truncations through 34 bits are eta-independent; bit 35 is exactly eta
parity already present in the forced tail. Hensel-level eta information
requires U through 56 bits. Rewriting this equality is not an independent
determination of U or eta.

With C2 applied, every below-p necessary source has `p-a>=37`, root-prefix
depth `u-(b_a-1)>=60`, and first root-normalization depth `>=97`.
Both root contributions vanish modulo 2^56. The earlier 39/63/100 values
are invalid at source scope. No reflected a>p statement is inherited.

RL195 complete-word denominator equivalence, RL201's continuous-mass and
coupled finite-reverse barriers, and all ownership/charging/Gate locks remain
binding. Generic integrality after specifying an admissible complete word
and exact K0 is not a new independent consumer. Original selected sources
are preserved byte-for-byte in `provenance/`, with C2 taking precedence over
the uncorrected historical RL203 source text.

# RL214 — discrete ownership quotient bridge and positive root cap

Date: 2026-09-01.

Classification:
- Sections 1–2: **proved analytic mathematics**, conditional on the inherited complete-word and H21 interfaces.
- Section 3: **exact finite certificate** over the complete RL212 e=16 root-prefix population and the complete bounded lift interval produced by Section 2.
- Section 4: **scoped method barrier**, not an all-quotient no-go.

All physical conclusions remain conditional on a physical H21 realization of the inherited sole high branch `(37,0,23,-1)`.

## 1. Coordinate bridge: the H21 root is the owned full-word quotient state

RL206 fixes a complete binary word `d` of length `A`, weight `L`, and
`D=2^A-3^L>0`. Its full-step recurrence is

`2R_(m+1)-3^(d_m)R_m=d_m`.

For a complete word, its unique rational cyclic solution is

`R_m = Q(rot_m(d))/D`.

Now take the accelerated odd-state word used by the H21 interface. If its acceleration exponents are `a_0,...,a_(L-1)`, expand it to the full binary word by placing a `1` at cumulative positions
`s_i=a_0+...+a_(i-1)` and zeros between consecutive positions. Start at the H21 root, so `s_0=0`.

Each block of the full recurrence from `s_i` to `s_(i+1)` is precisely

`2^(a_i) y_(i+1)=3y_i+1`.

Uniqueness of the full rational solution therefore gives
`R_(s_i)=y_i` for every odd phase. At the root,

`y_0=R_0=Q(d)/D`.                                             (1)

This proves the bridge requested by RL214. It also identifies exactly what is still missing. Full ownership says `D|Q(d)` and hence that (1) is integral, but the residue

`y_0 mod D = (Q(d)/D) mod D`

depends on `Q(d) mod D^2`. RL206 already proved that this quotient residue is outside its recurrence-linear annihilator no-go. Equation (1) does not itself determine the extra D-adic digit.

## 2. A global root inequality from the positive owned p-arc

Use the inherited root identities
`h_0=h_p=0`, `b_p=u`, and `y_p-y_0=K_0=2^37`.
Iterating the first `p` accelerated odd steps yields

`2^u y_p = 3^p y_0 + P`,                                     (2)

where `P>0` is the ordinary affine numerator of the nonempty p-arc. Inserting
`y_p=y_0+K_0` gives

`2^u K_0=(3^p-2^u)y_0+P`.                                    (3)

Let `alpha=3^p/2^u`. Then (3) proves

`0<y_0<K_0/(alpha-1)`.                                       (4)

This is independent of the collapsed RL201 e=16 endpoint moment: (4) uses strict positivity of the full p-arc numerator, not a rearrangement of the root z-telescope.

For a portable rational cap, let `delta=A ln2-L ln3`. The inherited bound is
`0<delta<2^-40`, and `Ap-uL=1`. Hence

`L ln(alpha)=pL ln3-uL ln2
             =(pA-uL)ln2-p delta
             =ln2-p delta`.

Because `p<2^36`, `p delta<1/16`.
The convergent positive atanh series gives

`ln2=2(1/3+1/(3*3^3)+1/(5*3^5)+...)>2/3`.

Therefore

`L ln(alpha)>2/3-1/16=29/48`.

Thus `alpha>1`, and since `alpha-1>ln(alpha)`,

`29 y_0 <48 L K_0`.                                          (5)

For the inherited constants, the largest integer permitted by (5) is

`31285589992934194300574`.

## 3. Complete bounded-lift certificate at e=16

RL212's recurrence has 108,950 exact phase-16 height-one prefixes; 45,046 satisfy the H21 mod-9 state law. Its exact root p-gap gives a unique unit-preserving lift modulo `3^17` for each.

The RL214 verifier reconstructs all prefixes independently using exact integers. For the canonical representative `0<=eta_*<3^17`, it verifies

`4167<=eta_*<=129137967`

and

`27763779757799<=y_0^*<=864676287134182727<3*2^58`.

Increasing eta by `3^17` increases y0 by

`2^58 * 3^17 / 3^16 = 3*2^58`.

Hence every exact lift is uniquely

`eta=eta_*+k3^17`,
`y_0=y_0^*+k(3*2^58)`,

and positivity is exactly `k>=0`. Inequality (5) makes `k` finite:
`k<=36180` for 34,652 prefixes and `k<=36181` for 10,394 prefixes.
The complete bounded family has 1,629,819,720 candidates.

The inherited terminal test has `nu>=22` precisely at the Hensel residue
`3^(-34)=1893305 mod2^22` for the appropriate odd terminal parameter. Solving that congruence directly along each bounded k-progression removes 789 arithmetic candidates in 789 distinct prefixes. Every prefix retains at least 36,180 candidates.

Post-filter counts by `eta mod18` are:
`0:529801527`, `8:285107835`, `9:529801531`, `17:285108038`.
All 469 RL212 reachable classes modulo2187 remain represented.

The verifier digest over the complete prefix/lift-bound data is
`cd0f9235a557a8f70c8fed89a802da95222fcc5bc80b7644e6dba57f71346136`.

## 4. Exact barrier and next information requirement

RL214 succeeds in turning the discrete quotient/root variable into a finite exact candidate family, but it does not obtain a quotient residue sharp enough to eliminate a prefix.

The precise missing datum is one of the following equivalent types:

1. `Q(d) mod D^2`, hence `(Q(d)/D) modD`;
2. an independently anchored residue of `y_0`;
3. an independently anchored congruence/valuation for the p-arc numerator `P` in (3);
4. another complete-word invariant not algebraically contained in the inherited root telescope.

The positivity inequality alone is saturated by all 45,046 current H21 prefixes. The ordinary terminal valuation removes only 789 individual bounded lifts and no prefix. RL209's signed-successor root-window anchor remains outside the e=16 terminal phase and is not generalized here.

No state, mod18 class, terminal rank, physical H21 incidence/charge, branch, Gate, or global nontrivial-cycle conclusion is changed.

# RL213 — e=16 endpoint-moment collapse and G56 saturation

Date: 2026-09-01.

Classification:
- Section 1: **proved analytic mathematics**, conditional on the inherited RL201/RL210/RL212 H21 interface.
- Section 2: **exact finite certificate** over the complete stated RL210 first-divergence start-case domain.
- Sections 1–2 yield **scoped method barriers**, not physical existence results or all-global-consumer no-go theorems.

All physical statements remain conditional on a physical H21 realization of the sole inherited high branch `(37,0,23,-1)`.

## 1. The inherited absolute endpoint moment is redundant at e=16

Use the inherited notation

`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u=103768467013`, `Ap-uL=1`, `alpha=3^p/2^u`, `K0=2^37`,
`q_i=rho_i 2^(-h_i)`, `P_a=sum_(0<=j<a)q_j`, `z_i=rho_i x_i`.

RL201 gives the exact fixed-K endpoint moment at an H21 source phase a:

`3(alpha-1)rho_a x_a = 3K0-alpha P_p+(alpha-1)P_a`,       (1)

where `x_a=2^33 eta-1/2` because the source height is one.

For the exact short above-p source `a=p+16`, RL210 proves `h_t=h_(p+t)` for `0<=t<=16`; the no-carry formula gives

`b_(p+t)=u+b_t` for these t. Hence

`q_(p+t)=q_t/alpha`, `rho_(p+16)=rho_16/alpha`,            (2)

and therefore

`P_(p+16)=P_p+P_16/alpha`.                                  (3)

Insert (2)–(3) into (1) and multiply by alpha:

`3(alpha-1)rho_16 x_a = 3alpha K0-alpha P_p+(alpha-1)P_16`. (4)

RL210/RL212 also give the exact matched e=16 p-gap `K_16=K0`, so

`rho_16(x_a-x_16)=K0`.                                      (5)

The root z-telescope through phase 16 is

`P_16=3(z_16-z_0)=3(rho_16 x_16-y_0)`.                     (6)

Substitute (5)–(6) into (4). The `rho_16 x_16` terms cancel and leave

`alpha P_p=3(K0-(alpha-1)y_0)`.                              (7)

But (7) is already the root `0->p` z-telescope. Indeed `rho_p=1/alpha`, `h_0=h_p=0`, and the inherited root p-gap is `y_p-y_0=K0`, so

`P_p=3(z_p-z_0)=3(y_p/alpha-y_0)`

and multiplying by alpha gives (7) identically.

Therefore (1), under the exact current e=16 matched-prefix identities, is not an independent equation for eta. In particular it cannot by itself shrink the RL212 469 surviving eta classes modulo2187 or delete the e=16 rank.

**Scope.** This is not a theorem that every complete-word moment is redundant. A newly proved restriction on `P_p`, an owned quotient/root residue, a nonlinear/global inequality, or another invariant can add information not present in (1).

## 2. G56 is saturated after the inherited m=24 orientation cut

RL210 proves that every physical above-p source with offset at least 56 has a first p-separated exponent mismatch m satisfying

`24<=m<=37`, `min(S_m,S'_m)=37`.                            (8)

Before m, the sequences agree. At m the larger exponent is some

`k in {38,...,b_m}`.                                        (9)

Consider the exact abstract continuation problem defined only by:

- (8)–(9) and either orientation at m;
- strict increase of each exponent sequence;
- `S_t,S'_t<=b_t` through t=55;
- RL210's congruence

`sum_(t=0)^55 (2^(S'_t)-2^(S_t))3^(-t) = -3*2^37 (mod 2^56)`. (G56)

There are exactly

`sum_(m=24)^37 2(b_m-37)=304`

start cases.

`verification/verify_rl213_global_consumer_barriers.py` performs a gap-free exact search of this complete finite domain. It factors G56 by `2^37`, searches modulo `2^19`, and uses only the exact low-bit pruning rule: after a partial state with current exponents s,s', every future contribution is divisible by

`2^min(19,min(s,s')+1-37)`.

A partial residue whose already frozen low bits differ from the target cannot be repaired. Exponents at least 56 contribute zero modulo `2^56`; among such choices the least legal exponent weakly dominates larger choices by leaving maximal future room. Every positive result is finally rechecked directly in the full modulus `2^56`.

The result is exact:

- one infeasible case: `m=24`, `k=38`, `S_24=37<S'_24=38`, reproducing the inherited RL210 orientation obstruction;
- all remaining **303** start cases have explicit valid continuations through phase55.

Feasible/total counts for m=24,...,37 are

`1/2,4/4,8/8,10/10,14/14,16/16,20/20,24/24,26/26,30/30,32/32,36/36,40/40,42/42`.

The deterministic witness digest is

`dd7dc63df94e0360f556fa255fea04e75463f8502f57588e051b49b081be2c5a`.

Thus G56 combined only with strict increase and the mechanical upper bounds has no further start-case exclusion beyond RL210's already promoted m=24 orientation cut.

**Scope.** The 303 continuations are arithmetic prefix witnesses only. They do not prove that any remaining case extends to a physical H21 word, an owned full cycle, or a globally admissible height word. Additional absolute/full-word information may still exclude them.

## 3. Consequence for the next route

RL212's e=16 ternary holes remain genuine local information, but neither the existing endpoint moment nor a bare continuation of G56 consumes them. The next route must add a genuinely discrete/global datum outside those saturated families. The preferred candidate is the full-word owned quotient/root residue left open by RL206, after proving the exact coordinate bridge to the H21 representation.

No rank deletion, H21 state/parity/valuation selector, physical incidence/charge, branch contradiction, Gate closure or global nontrivial-cycle exclusion is proved.

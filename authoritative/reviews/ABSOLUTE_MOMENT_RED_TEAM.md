Review provenance note: source paths and SHA256 values below identify the reviewed
unsealed source copies. The final portable proof/verifier paths are under proofs/ and
verification/; their final bytes are authenticated by the package manifest and fresh suite.

# RL201 independent red team — absolute endpoint and fixed moment

Date: 2026-08-31. Frozen RL201 component.

Verdict: **PASS for the explicitly scoped final candidate**, after the
clarifications recorded below. No inherited mathematical state is changed.
This review performed verification only, with no new route exploration.

## Reviewed artifacts and provenance

Primary note:
`.rl-work/RL201/pchain/RL201_ABSOLUTE_ENDPOINT_AND_FIXED_MOMENT.md`

SHA256 at final review:
`9a12a606795bd46c60e7fd2e7d8803a1ae6cd137d9eefdd8ee68eaf78cdbf087`.

Verifier: `.rl-work/RL201/pchain/verify_endpoint_moment.py`

SHA256:
`2fcee2762ad6cc877f821cdd5d714a13633c47d6a9349d24deab43678aaa7f75`.

Targeted source checks used the RL181 certified ledger under
`sessions/RL182/RL181_Shallow_Pair_Gap_Corridor_and_Normalized_Width_Occupancy_2026-08-30/`,
and the RL194 weight-order/moving-window proof and RL195 reconstruction/
denominator proof carried in
`sessions/RL197/RL196_Zero_Edge_Placement_and_Global_P_Shift_Compatibility_2026-08-31/proofs/`.
These were checked only for the exact live identities and scope at issue;
there was no broad historical replay or novelty audit.

## 1. Rank, carry, and endpoint identities

The noncarry p-step shifts mechanical rank by one. The final rank edge
has normalized gap `2*x_0-x_(I(L-1))`, not `x_0-x_(I(L-1))`.
Summing all L edges therefore gives exactly `sum d_r=x_0`.
The rank-initial partial sum then gives
`x_(I(j))=sum_(r<L)d_r+sum_(r<j)d_r`.
This checks the carry once, the sign, all endpoint indices, and the
distinction between mechanical-rank order and chronological phase.

At the H21 tau=34 source both heights equal one, and its ordinary p-gap
is positive. Thus the source is the lower endpoint and
`x_a=Y_0^-/2=2^33*eta-1/2`. The stated rank interval does not include
the p-shift carry rank `L-1`. Substitution gives the displayed complete
rank-gap formula for eta without any missing orientation factor.

## 2. Fixed moment and lattice spacing

The lifted telescope gives `3(z_(i+1)-z_i)=q_i` and
`z_a=Q/[3(lambda-1)]+P_a/3`. Eliminating Q from
`3K_0=alpha*P_p+beta*Q`, with
`beta=(alpha-1)/(lambda-1)`, independently gives

`3(alpha-1)rho_a(2^33*eta-1/2)`
`=3K_0-alpha*P_p+(alpha-1)*P_a`.

The sign and factors in
`J_a=alpha*P_p-(alpha-1)*P_a` and in the solved eta expression are
correct. Increasing eta by one decreases J_a by
`D_a=3(alpha-1)rho_a*2^33`; each individual mod18 class has spacing
`18D_a` in J_a. The note claims only this reparameterization, not a new
satisfied constraint or a selected residue.

The actual-constant spacing estimate is also valid. From
`p<2^36`, `delta<2^-40`, and `2/3<ln2<7/10`, one obtains
`29/(48L)<ln alpha<7/(10L)`. Applying
`s<exp(s)-1<s/(1-s)` and `1/2<rho_a<=1` gives the stated lower and
upper fractions. Their reductions and comparisons to `1/20` and `2/15`
are exact. The atanh-series justification `ln2<25/36` is conservative
and strict; no floating-point enclosure is being substituted.

## 3. Continuous perturbation, protected windows, and phase factors

The strict index hypotheses make both b,d choice intervals nonempty.
They place b after every protected source, before p, and inside every
protected p-window; they place d after every protected source window.
Neither is phase zero, phase p, or a protected local coordinate.
Consequently

`delta Q=-alpha*t`, `delta P_i=0`, `delta C_i=beta*t`

for every protected i and at phase zero. The exact cancellation in K
is correct, and preserves the exact *starting* K_0 value.

At the partner i+p, the prefix contains b but not d, giving
`delta P_(i+p)=beta*t` and `delta Y_(i+p)=-t`.
The hypotheses also imply `i+p<L`, excluding the p-carry source.
Thus `rho_(i+p)=rho_i/alpha`, with no omitted lambda factor, and
both normalized endpoints move by exactly
`-alpha*t/[3(lambda-1)rho_i]`. Their gap is unchanged.

The formulas for Tminus/Tplus have the correct inequalities and signs.
Strictly interior b,d coordinates ensure a nonempty open t-interval.
The eta displacement and the reversal of its interval endpoints are
correct because the coefficient c_a is positive.

Every canonical q-coordinate coefficient in `3K_i` is among
`beta`, `beta+alpha`, `lambda*beta`, `lambda*(beta+alpha)`.
The triangle inequality therefore proves the stated uniform bound
`|delta K_i|<=lambda*(beta+alpha)*(2*beta+alpha)*|t|/3`.
At the lifted endpoint L, K_L=lambda*K_0 is unchanged as well.
The strict-corridor preservation claim is conditional on an existing
finite word with a positive minimum margin and sufficient coordinate
slack; the note does not establish either for an actual H21 word.

## 4. Discrete feasibility and novelty limits

The reviewed theorem concerns positive real q masses. It does not
preserve the exact discrete form `q_i/rho_i=2^(-h_i)` with integral
nonnegative h_i, the global positive integer acceleration inequalities,
all odd endpoint conditions, terminal valuations, or tau35 state
compatibility. Nonconstant real eta displacement does not by itself
reach two different integer eta values, much less two mod18 classes.
The final note states these limitations explicitly.

The RL195 denominator theorem applies only after a complete globally
admissible integer-height word and exact branch K_0 have been supplied.
It then already forces odd-integral reconstruction. The perturbation
cannot be used to contradict or bypass that theorem. No complete
integer-height-word consumer is proved insufficient here.

The full p-chain, z telescope, and moving-window inversion are correctly
identified as inherited. The contribution is their explicit oriented
H21 endpoint specialization, a quantitative lattice scale, and a
conditional flexibility direction in a named real-mass relaxation.
No claimed novelty depends on an unexamined historical absence.

The source-phase restrictions of the perturbation theorem are real
hypotheses. The theorem is not asserted for every H21 rank or for an
existing actual-constant model. No physical population, H21 charge,
branch/Gate closure, or cycle exclusion follows.

## 5. Clarifications coordinated during review

The author applied and the reviewer reread these precision repairs:

1. Final q masses remain **at or below** caps; protected anchors may
   already equal their caps.
2. An arbitrary real starting word need not have K_0=2^37. Branch use
   additionally assumes that exact starting moment; the perturbation
   preserves whatever starting value was supplied.
3. The power-of-two form with integral h is distinguished from the
   weaker condition of merely dyadic rational q/rho.
4. The exact open attainable eta interval and its iff statement refer
   to the chosen strictly interior t-family. A cap-limited boundary
   value could also satisfy the broader non-strict caps, and is not
   falsely excluded from the full feasible set.

These were candidate-scope clarifications, not demotions of inherited
theorems. No unresolved correction remains in the reviewed artifact.

## 6. Reproduced finite verification

Ran `python3 .rl-work/RL201/pchain/verify_endpoint_moment.py`.

Output:

```text
PASS actual-constant rational comparisons: 1/20 < D_a < 2/15
PASS toy Bezout (27, 17, 12, 19): 12 exact signed perturbations
PASS toy Bezout (46, 29, 12, 19): 68 exact signed perturbations
PASS exact absolute-endpoint, p-chain, fixed-moment and coupled-fiber regression
Scope: toy algebra only; no actual high-branch height-word or eta-class certificate
```

The 80 perturbations cover precisely the advertised toy (a,n) ranges,
the first permissible b,d at each pair, and the two named strict
interior t choices. They are algebraic regressions with exact Fractions,
not an actual-constant finite word certificate. The analytic arguments
above, rather than an unperformed finite scan, support the general
identities and conditional deformation theorem.

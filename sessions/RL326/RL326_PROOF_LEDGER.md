# RL326 proof ledger — mechanical-excess density and 229-million carry contraction

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL326 CLOSEOUT
Incoming BASE_HEAD: `82d9102e013fcf5d239e3cfee4a9b4c69b82fa00`
Successor: RL327

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch at

`(a,ell)=(217976794617,137528045312)`, `d=a-ell=80448749305`,
`lambda=2^a/3^ell<1+2^-40`,

with the externally conditional least-state window

`2^71<=m<2^75`.

The incoming canonical carry is `c0=-n`, `M=m-n`, and RL325 gives

`1<=n<=33068504812`.

All conclusions below retain the internal/external scope split recorded by RL325. Gate A, Gate B, R1, and global positive non-trivial-cycle exclusion remain open. The RL324 local-propagation barrier remains binding.

## RL326.1 — sharper crossing-start telescope

Let `j` be the RL324 crossing rank, `k` the canonical least-root rank, and

`T=k-j=ell-rho`, `rho=j+ell-k`.

For `1<=t<=T`, put

`U_t=u_k-u_(k-t)`,
`q_t=U_t-ceil(at/ell)>=0`,
`c_t=3^t/2^(ceil(at/ell))`.

The exact RL325 recurrence may be unrolled from the negative crossing defect `e_j<0`, not merely from `j+1`. Dropping that negative initial term and the factors `1-2^(-d_i)<1` gives

`e_k < (1/3) sum_(t=1)^T c_t 2^(-q_t)`.

Since `e_k=n-eta/2^r>n-1`,

`n < 1 + I_rho - K/(12 Lambda)`,

where `Lambda=1+2^-40`, `K=#{t:q_t>0}`, and `I_rho=(1/3)sum_(t=1)^T c_t`. Indeed `c_t>1/(2lambda)>1/(2Lambda)` and every positive `q_t` removes more than `c_t/6>1/(12Lambda)` from the ideal sum.

Classification: **proved analytic refinement of the genuine linear RL325 telescope**.

## RL326.2 — complete 49-gap mechanical-factor certificate

If `q_t=0`, the physical odd state `P_(k-t)` obeys

`m<=P_(k-t)<2 lambda m<2^76+2^36`.

The lower inequality is global least-state ownership. The upper inequality follows from

`2^(U_t)m=3^t P_(k-t)+B_t`, `B_t>0`, and
`3^t/2^(ceil(at/ell))>1/(2lambda)`.

On a consecutive zero run of the `q_t`, the actual backward odd gaps are exactly

`ceil(a(t+1)/ell)-ceil(at/ell)`.

Because `gcd(d,ell)=1`, every length-49 factor is obtained from one of the 50 rational-mechanical intercept intervals. The verifier enumerates all 50 factors exactly. For a factor `g_1,...,g_49`, backward integrality forces the endpoint into one residue modulo `3^49` via

`C_0=0`, `C_s=2^(g_s)C_(s-1)+3^(s-1)`,
`2^(sum g_s) P == C_49 (mod 3^49)`.

Since `3^49>2^76+2^36`, each factor has at most one endpoint in the physical state band. Exactly three factors have an odd endpoint there. Reconstructing their 49 backward odd states gives

`max over candidates (minimum state in the block)`
` = 22689747442539873328123`.

Now `Z0>0` gives

`n < (1-1/lambda)m < Delta m`,

where `Delta=a log 2-ell log 3`. The exact logarithmic enclosure verifies

`Delta * 22689747442539873328123 < 20390252058`.

Therefore, for every `n>=20390252058`, no exact mechanical block of 49 consecutive backward odd gaps can occur.

Classification: **exact gap-free finite certificate over all 50 genuinely owned mechanical factors, coupled to an analytic state-band theorem**.

## RL326.3 — positive-excess density theorem

Assume `n>=20390252058`. Among `q_0,...,q_T`, with `q_0=0`, a run of 50 zero values would contain 49 exact mechanical gaps and is impossible by RL326.2.

If `K` of `q_1,...,q_T` are positive, the `K+1` zero runs each have length at most 49. Hence

`T+1-K <=49(K+1)`,

so

`K>=ceil((T-48)/50)`.

This density uses the global least state and exact ordinary odd-to-odd ownership. It is absent from, and compatible with, the RL324 local counterfamily.

Classification: **proved analytic support-uniform density theorem backed by RL326.2**.

## RL326.4 — global carry contraction

The ideal full coefficient sum satisfies

`sum_(t=1)^(ell-1)c_t`
` < sum_(q=1)^(ell-1)2^(q/ell-1)`
` = 1/[2(2^(1/ell)-1)]-1/2`.

Using the 280-term rational lower enclosure `L_280<log 2` and `exp(x)-1>x+x^2/2`, the verifier uses the exact rational upper bound

`S_up=1/[2(L_280/ell+(L_280/ell)^2/2)]-1/2`.

For `T=ell-rho`, the omitted end is bounded below by

`(1/Lambda) sum_(r=1)^(rho-1) 2^(floor(ar/ell))/3^r`.

For `rho=60`, RL326.3 gives

`K>=ceil((ell-60-48)/50)=2750560905`.

The exact rational certificate then gives

`n < 32839291403.596188...`,

hence

`n<=32839291403`.

For `rho<=59`, the independent RL325 carry inequality gives

`n<17179869184.848957...`.

For `rho>=60`, the displayed upper bound decreases strictly with `rho`: each new omitted term decreases it by more than `1/(6Lambda)`, while the rounded density lower bound can relax by at most one rank, restoring at most `1/(12Lambda)`.

Thus the bound covers every live `rho`, not just the maximal-carry endgame.

Classification: **proved analytic all-rho contraction plus exact rational finite constant certificate**.

## RL326.5 — incoming maximal-carry endgame consumed

The new global cap excludes the entire incoming maximal carry

`n=33068504812`,

and therefore all three RL325 placements `rho in {60,61,62}` at that carry. No support enumeration of the original unbounded interface is used.

Classification: **proved branch-endpoint elimination as a corollary of the stronger global contraction**.

## Corrections, barriers, and non-results

1. No promoted result uses the root-aligned `G<2^35` theorem in the live late-row-root branch.
2. The telescope is linear; no cyclic wrap is used.
3. The finite certificate covers all 50 possible length-49 mechanical factors, not a sampled support family.
4. The exploratory endpoint searches for budgets 4 through 10 are not needed by, and are not promoted with, the density theorem.
5. R1 remains open for `1<=n<=32839291403`.

`PARENT_DIFFICULTY_DELTA = EASIER`.

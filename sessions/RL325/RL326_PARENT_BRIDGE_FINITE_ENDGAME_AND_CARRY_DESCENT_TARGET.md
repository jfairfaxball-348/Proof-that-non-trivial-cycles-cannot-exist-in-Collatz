# RL326 — finite endgame and carry descent for the remaining R1 parent bridge

Date prepared: 2026-09-15
Status: PREPARED, NOT STARTED

## GLOBAL PROOF ROADMAP

`CURRENT_STAGE = R1`
`CURRENT_STAGE_NAME = Parent Bridge`
`CURRENT_STAGE_PROGRESS = 60%`
`GLOBAL_PROOF_STATUS = OPEN`

## Absolute objective

Close, or materially advance toward closing, the remaining `Z0>0, K<0` parent obstruction using the genuine global ownership machinery frozen by RL325.

The live branch is

`c0=-n<=-1`, `M=m-n<m`,

with the certified carry bound

`1<=n<=33068504812`.

Do not restart the barred local matched-rank displacement propagation route.

## First priority — consume the maximal-carry finite endgame

At

`n=33068504812`,

RL325 proves

- `rho=j+ell-k in {60,61,62}`;
- `d_j<=36`;
- `L=a-u_k<=62`;
- the canonical-to-boundary physical suffix has at most one zero;
- for `rho=60,61` the suffix is exactly `1^h` and `2^h | (m+1)`.

Use the genuine physical/ordinary ownership of these bounded endgames to prove one of:

1. contradiction;
2. a strictly smaller genuinely owned balanced return;
3. a further strict carry contraction;
4. an explicit bounded canonical witness already excluded by a frozen theorem/certificate.

An exact finite certificate is legitimate if and only if it covers the **entire genuinely owned bounded endgame** produced by RL325 and its scope is explicit. Do not enumerate the original unbounded support.

## Second priority — convert the top-slice closure into all-carry descent

After consuming the maximal carry, seek a monotone/self-consistent descent in `n` using the pair of RL325 inequalities

`n < 5/6 + lambda 2^(floor(d rho/ell))`

and

`n < B_* - [1/(3 lambda)] sum_(r=1)^rho 2^(floor(a r/ell))/3^r`.

The goal is to show that every remaining integer carry is forced into a bounded owned endgame, or that exclusion of the current maximum lowers the maximum and repeats with a finite descending certificate until no `n>=1` remains.

If a direct descending induction is not available, an equivalent support-independent absolute bound on the original canonical `(r,s,beta)` interface is also sufficient for the R1 target.

## Binding correction

Do **not** use

`G<2^35`

in the live late-row-root branch. RL319 proves that cap only in the root-aligned alternative. The valid live-branch inequality is

`n-5/6 < lambda G`,

which RL325 combines with the crossing-prefix bound `G<2^z` and the global zero budget.

## Binding barriers

Preserve RL324.6:

- no rank-by-rank displacement propagation;
- no claim that small positive defect controls the next displacement;
- no local least-state lower-bound iteration;
- no bare modulus escalation;
- no cyclic-wrap recurrence.

Any successful all-carry theorem must consume genuine global structure absent from the local counterfamily.

## Exact certificate inputs

Frozen constants:

`a=217976794617`,
`ell=137528045312`,
`d=80448749305`,
`lambda=X/Y<1+2^-40`.

RL325's portable verifier uses exact `Fraction` arithmetic and the 280-term rational lower enclosure for `log 2`.

## Preserved scope

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.
External `2^71` least-state floor remains conditional.
Gate A OPEN.
Gate B OPEN.
`g=1` separate.
Global positive non-trivial-cycle exclusion OPEN.

Advance to `R2` only if the full remaining parent bridge is actually closed.

# RL156 — Bézout/state notation repair for the dense singleton phase identity

## Status

**Correction / portability repair.** RL156 repairs a notation collision in
RL155 and retains its exact algebra unchanged. It supplies no cycle
exclusion, Gate closure, or new finite frontier.

## The correction

RL155 inherited `m` as the least odd state, but also wrote `Ap-mL=1` for a
Bézout relation. These are different integers. In this bundle they are
permanently distinguished as follows:

- `M` is the least odd state of a hypothetical physical cycle;
- choose integers `p,u` satisfying `Ap-uL=1`;
- `rho=2^u 3^(-p)` modulo `D=2^A-3^L`.

Thus the full-modulus singleton ownership identity is, without any state/
Bézout ambiguity,

`sum_(j<L) rho^(Aj-LS_j)=0 (mod D)`.                       (1)

For the nonnegative defect path
`h_j=floor(Aj/L)-S_j`, this becomes

`Aj-LS_j=(Aj mod L)+Lh_j`,                                 (2)

and `rho^L=1/2` modulo `D`. Reducing the corresponding phase polynomial
modulo `3T^L-2`, then clearing its common denominator by `3^H`, leaves at
each residue `r=Aj mod L` the strictly positive coefficient

`2^h_j 3^(H-h_j)`,                                         (3)

where `H=max_j h_j`. Coprimality of `A,L` gives one such term at each
residue. The ordinary numerator divisibility and (1) remain equivalent; no
converse is claimed.

## Scope

This is only a notation repair. It does not turn dense positive coefficients
into a contradiction, does not split defect levels, and does not reinstate
the excluded sparse, `F_1`, small-prime, or legacy `g=2` resultant routes.
The physical `g=1` nonzero nonnegative-defect owner remains open.

## Classification

- correction: **notation-only**, no mathematical demotion;
- retained result: exact analytic phase/numerator equivalence;
- open obligation: arithmetic discrimination of the coupled dense remainder.

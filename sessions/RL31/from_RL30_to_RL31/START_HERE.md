# START HERE — RL30 audit -> RL31 handover

Date: 2026-08-21

## Corrected one-line state

**RL remains open.** RL30 validates the new RL29 exact ownership, `e>=67`, transport, and `Omega(e/log e)` theorems inside the exact exceptional three-way-balanced branch, but rejects the claim that this branch is the unique remaining global RL obstruction.

## Most important audit correction

Eliminating

`R==91 (mod288), (G,H)=(12,4)`

would **not** close RL from the current proof DAG. The unresolved graph still includes non-near-resonant/huge-length cases, strict-excursion/no-balanced-return cases, order-2 and general cyclotomic balanced returns, and non-extremal order-3 sectors.

Read `RL30_AUDIT_REPORT.md` before extending the research.

## Verified RL29 upgrades

RL30 independently accepts, under their stated branch hypotheses:

- `R==667 mod4608`, `R>=5275`, forced nine-bit prefixes;
- exact `B-Y` ownership from synchronized rotations;
- exact Eisenstein `Bw^2-Y` ownership;
- `e>=67`;
- universal orbit-sum and pair-transport identities;
- the 47-positive-imbalance threshold;
- `Omega(e/log e)` distinct aligned columns containing a phase above `2.9R`.

All 22 inherited/RL29 verifiers pass. RL30 also adds a quantitative-target verifier.

## Quantitative correction

`1/4` is not an RL contradiction threshold. The current supporting coefficient is

`457841/1843200 ~= 0.248394639756944`.

The next inherited CF denominator gate under the external `R>=2^71` floor is at coefficient scale about

`0.190911609404599`,

so the required further drop is about `0.05748303035`. Crossing that gate still would not prove RL.

## Best next attack

Attack a **weighted synchronization / odd-or-valuation charging lemma**. Raw `Omega(e/log e)` high-column count is insufficient because its density vanishes and high columns can all be even. A successful theorem should assign every synchronized/unsynchronized excursion either:

1. useful high odd correction-product savings, or
2. a 2-adic valuation/block-type penalty,

and prove total gain `>= c e/R` in log-product units for some fixed `c>0`.

Do not return to deeper residue lifting as the primary strategy.

# RL301 — external class-record finite-delay certificate

Date frozen: 2026-09-11
Status: promoted **external finite computational certificate dependency**

## Consumer statement

RL301 uses exactly:

`for every positive n < 46500000000000000000, ordinary Collatz delay D(n) <= 2456`.

No larger external delay range is used.

## Source A — Eric Roosendaal current status / definitions

URL:
`https://ericr.nl/wondrous/`

Checked: 2026-09-11.

Relevant source facts:

- all numbers up to `46.5 * 10^18` are reported checked for class records;
- a Class Record is the lowest element of a Delay Class;
- the highest confirmed delay record shown is delay 2456 at `28019077177231758495`.

## Source B — class-record table

URL:
`https://www.ericr.nl/wondrous/classrec.html`

Checked: 2026-09-11.

Relevant source facts:

- the table states: `All 2425 Class Records up to 46,500000,000000,000000`;
- the class-2456 entry is `28019077177231758495`;
- there is no class record of a higher delay class below the completed bound.

## Source C — progress history

URL:
`https://ericr.nl/wondrous/progress.html`

Checked: 2026-09-11.

Relevant source fact:

- the progress history records on 2026-06-30: `All blocks up to 46,500 completed`.

The page status when checked was dated 2026-08-31.

## Source D — confirmed delay-record semantics

URL:
`https://www.ericr.nl/wondrous/delrecs.html`

Checked: 2026-09-11.

Relevant source semantics:

- a delay record is considered confirmed only after all smaller starting values have been checked and found to have lower delay.

This source corroborates the displayed 2456 record but is not required for the class-record implication below.

## Exact finite implication consumed by RL301

Suppose `0<n<46500000000000000000` and let `d=D(n)`.

By definition, the class record `R_d` is the least positive integer with delay d, so

`R_d <= n < 46500000000000000000`.

The externally complete class-record table below this bound therefore contains `R_d`. The largest delay class represented below the bound is 2456. Hence `d<=2456`.

Therefore

`boxed: D(n)<=2456 for every positive n<46500000000000000000`.

## Independent in-repository replay

`verification/verify_rl301_fast.py` computes ordinary Collatz delay directly and verifies

`D(28019077177231758495)=2456`.

It also independently verifies every consumer-side resonance, ancestry, envelope, and selector-margin calculation.

## Reproducibility boundary

Internally reproducible:

- the load-bearing record value and its ordinary delay;
- exact continued-fraction/resonance arithmetic;
- exact B-ancestry and `J_B=J_Y-4` conversion;
- exact B-ancestor envelope and threshold comparison;
- exact promoted frontier.

Externally depended upon:

- completeness of the historical class-record search below `46.5*10^18`.

RL301 does not promote any larger range, convergence-only range, or global stopping claim.

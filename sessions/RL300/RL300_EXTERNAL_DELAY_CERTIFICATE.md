# RL300 — external finite-delay certificate provenance

Date frozen: 2026-09-11
Status: promoted **external finite computational certificate dependency**

## Consumer statement

RL300 uses exactly this external statement:

`for every positive n < 4761963248413673697, ordinary Collatz delay D(n) <= 2334`.

No larger external range is used.

## Source A — OEIS A006877

URL:
`https://oeis.org/A006877`

Retrieved/checked: 2026-09-11.

Relevant source facts:

- A006877 is defined as starting values which set new records for number of steps to reach 1 in the `3x+1` problem.
- OEIS explicitly states that both the `3x+1` steps and the halving steps are counted.
- OEIS links its table to Eric Roosendaal's 3x+1 Delay Records.
- the sequence page was shown as last modified 2026-08-10 when checked.

## Source B — OEIS A006877 b-file

URL:
`https://oeis.org/A006877/b006877.txt`

Retrieved/checked: 2026-09-11.

The b-file header states that its data are from
`http://www.ericr.nl/wondrous/delrecs.html`
as of 2024-08-06.

The two consecutive entries used by RL300 are:

`142 3571472436310255273`
`143 4761963248413673697`

Only this pair is load-bearing for RL300.

## Source C — Eric Roosendaal delay-record semantics

URL:
`https://www.ericr.nl/wondrous/delrecs.html`

Search-index copy checked: 2026-09-11.

Relevant source semantics:

- the page describes its table as currently known and confirmed delay records;
- it states that a record is only considered confirmed when all smaller numbers have been checked and found to have a lower delay.

The general definitions page
`https://www.ericr.nl/wondrous/`
defines the ordinary Collatz sequence and defines a Delay Record `N` by the strict property that every smaller `M` has smaller delay.

## Independent in-repository replay

`verification/verify_rl300_fast.py` computes the ordinary Collatz delay directly and verifies:

`D(3571472436310255273)=2334`
`D(4761963248413673697)=2337`.

Therefore, under the externally certified consecutive-record status, every positive start below the second value has delay at most 2334.

## Reproducibility boundary

The consumer-side arithmetic is completely reproducible from this repository:

- the two source record values;
- their independently replayed delays;
- conversion from ordinary delay to half-Collatz stopping time and then to `J`;
- all resonance and physical-envelope calculations.

The historical exhaustive computation establishing that the pair is consecutive/confirmed is not rerun by RL300. That fact remains an explicitly labelled external finite computational dependency.

This is stronger provenance than the RL299 unpromoted web-status lead, but it is not represented as an internally reproduced exhaustive certificate.

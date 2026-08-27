# RL129 session state and RL130 kickoff

## Completed RL number

`RL129`

## BASE_HEAD

`d39d50f762dee5435ab60b59cce4d20b3b1f07ee`

## Frozen promoted result

The complete odd-count range `13<=L<=40` is excluded for primitive positive ordinary shortcut cycles.  The inherited frontier advances from `L>=13` to:

`L>=41`.

RL129's key analytic lemma is that if `D|Q`, the quotient `n=Q/D` follows the exact halved Collatz map under cyclic word rotation.  Choosing a transition root that starts with `1` and ends with `0` gives

`Q <= 2^(Z-1)(3^L-2^L)`.

For fixed `L` the resulting quotient ratio is strictly decreasing throughout the positive-`D` range, so its maximum occurs at the smallest positive `Z`.  Exact evaluation over `L=13..40` gives the global integer quotient ceiling

`n <= 30,400,121`,

with the worst bound at `L=39, Z=23`.

An exact induction-based verifier checks all `15,200,061` odd starts through this ceiling and proves that every one descends to the trivial `1<->2` orbit.  Such an orbit has periodic parity word `10`, so it cannot supply a primitive word with `L>=13`.

## Verification summary

Fresh-unpack fast suite passes:

- exhaustive small-word rotation/bound red-team: PASS;
- exact `L=13..40` quotient-bound regeneration: PASS;
- exact odd-start descent certificate through `30,400,121`: PASS.

## Correction/demotion ledger

No inherited promoted result is demoted.

RL126's empty-depth-fibre repair remains inherited.  The originally proposed RL129 H-floor/capacity enumeration was superseded before promotion; no partial exploratory capacity work is promoted or required.

## Frozen global scope

- primitive ordinary low-odd-count frontier: `L>=41`;
- Gate A: open;
- Gate B: open;
- global nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

## RL130 kickoff

Extend the quotient-descent frontier beyond `L=40` without weakening the RL129 proof discipline.  Start at `L=41`, where the exact transition-root quotient ceiling is `727,618,641`.  Determine a sensible next contiguous `L` block, certify all newly required odd quotients exactly, and investigate analytic/continued-fraction structure in the minimal positive denominator `2^(L+Z)-3^L` to control ceiling spikes.  Preserve all inherited ownership, primitivity, scope, verification-economy, sustained-attack, and correction/demotion rules.

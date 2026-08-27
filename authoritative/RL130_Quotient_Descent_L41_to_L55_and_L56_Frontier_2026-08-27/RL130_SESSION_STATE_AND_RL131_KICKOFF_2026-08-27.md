# RL130 session state and RL131 kickoff

## Completed RL number

`RL130`

## BASE_HEAD

`59750d2644e7cdfb426bc3b3a50b1ba7b2b6e20c`

## Frozen promoted result

The complete odd-count range `41<=L<=55` is excluded for primitive positive
ordinary shortcut cycles. The inherited frontier advances from `L>=41` to
`L>=56`.

The inherited quotient-rotation lemma and transition-root numerator bound
remain the analytic input. At the first positive denominator for each
`41<=L<=55`, the exact global quotient ceiling is `n <= 6,496,657,853`, with
the worst bound at `L=54, Z=32`. The exact induction verifier checks all
`3,248,328,927` odd starts through that ceiling and proves that every one
descends to the trivial `1<->2` orbit. Such an orbit has parity word a repeat
of `10`, so it cannot supply a primitive word with `L>=41`.

## Verification summary

Fresh-unpack fast suite passes:

- exhaustive small-word rotation/bound red-team: PASS;
- exact `L=41..55` quotient-bound regeneration: PASS;
- exact odd-start descent certificate through `6,496,657,853`: PASS.

## Continued-fraction / denominator diagnostic

Writing `alpha=log_2(3)`, `A=ceil(L*alpha)`, and `delta=A-L*alpha`, the exact
symbolic quotient-bound ratio is `R_L = 2^(Z-1)(1-(2/3)^L)/(2^delta-1)`.
Thus the method's baseline ceiling scale is already exponential in `Z=A-L`,
while unusually small positive `delta` adds a spike factor. The continued
fraction of `alpha` begins `[1;1,1,2,2,3,1,5,2,23,...]`; its above-side
convergent `65/41` explains the especially small `delta` at `L=41` (about
`0.01654`) and the visible local spike. This is a route-scaling diagnostic,
not a theorem excluding any further candidates.

## Correction/demotion ledger

No promoted mathematical claim is demoted. The RL129 outer-sidecar repair is
inherited: it corrected only a stale archive digest after the archive payload,
internal manifest, and fresh-unpack verifier suite were independently checked.

## Frozen global scope

- primitive ordinary low-odd-count frontier: `L>=56`;
- Gate A: open;
- Gate B: open;
- global nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

## RL131 kickoff

Extend the quotient-descent frontier from `L=56`. The immediate
first-positive-denominator ceiling is `23,506,639,475` at `L=56`; design a
chunked, resumable, exact induction scan that can certify this higher range
without promoting a partial interval. Continue to use exact arithmetic, retain
the quotient rotation and primitivity arguments, and investigate whether a
sharper transition-root bound can reduce the intrinsic exponential ceiling.

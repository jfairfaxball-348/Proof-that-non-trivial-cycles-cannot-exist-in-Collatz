# RL202 correction / demotion ledger

Date: 2026-08-31. No inherited theorem, range or certificate conclusion is
demoted.

## Closeout verifier-record repair

An unpromoted scratch verifier initially attached an ordering-sensitive SHA256
digest to a materialized list of root-window exclusions. The computed set/count
and mathematical boundary tests were unchanged, but the recorded digest did not
match the verifier's list ordering during closeout. The first invalid dependency
was therefore the scratch digest contract, not the mathematical exclusion.

RL202 removes that non-load-bearing digest entirely. The promoted verifier defines
the exclusion set by exact phase/rank predicates, certifies its two rank walls by
rigorous logarithm intervals, and counts the complete modular windows by exact
floor sums. This repair changes no inherited proof state and introduces no
mathematical demotion.

## Required scope locks

- 3,946,781 is a count of newly excluded **necessary terminal ranks**, not a
  physical H21 population.
- The surviving interval `[38643145224,38659291956]` is mandatory only for an
  H21 terminal whose canonical terminal phase lies in either stated root window;
  it is not a new global terminal-rank core by itself.
- The combined global necessary set is the inherited RL201 set minus the exact
  root-window predicate and four additional anchor-collision ranks. It is not a
  contiguous interval.
- The speed argument is carry-free and uses a deliberately conservative `+1`
  allowance for `K_L-K_0`; do not silently tighten or extend it.
- The positive-tail collision argument does not establish a new zero-edge route
  or H21 ownership event.
- All eta/state/sign, finite-cutoff, rank/time, physical/necessary, H21 charging,
  branch, Gate and global locks remain binding.

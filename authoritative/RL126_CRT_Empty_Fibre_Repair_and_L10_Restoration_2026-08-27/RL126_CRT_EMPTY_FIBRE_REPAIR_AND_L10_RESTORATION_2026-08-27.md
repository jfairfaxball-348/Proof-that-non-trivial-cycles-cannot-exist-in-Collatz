# RL126 — CRT empty-fibre repair and `L=10` restoration

## Stop-and-repair event

RL126 found that the RL124 CRT-capacity verifier evaluated `(c-1)` using an unsigned integer even when the depth fibre count `c` was zero.  An empty fibre contributes no spacing bound, but the underflow created an enormous false bound and falsely excluded profiles.  The affected certificate counts in RL124 were therefore invalid.

The correction is explicit: a CRT term is evaluated only when `c>=1`.

## Corrected certificate

The corrected exhaustive run covers the same primitive ordered `L=10`, `6<=Z<=24` profile family:

- primitive profiles: `92,555,670`;
- analytically capacity-excluded: `88,500,808`;
- residual profiles: `4,054,862`;
- exact cyclic-root tests of the necessary `D|Q` condition: `108,197,833`;
- divisibility hits: `0`.

Every primitive binary word has a transition-rooted run profile in this enumeration.  A capacity-rejected profile contradicts the inherited physical CRT/one-fibre width bounds; every surviving profile is tested at every cyclic root.  Thus the corrected exact certificate again excludes the RL123 `L=10`, `6<=Z<=24` residual strip.

## Restored state and scope

The conclusion that every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L>=11` is restored, now with corrected counts and provenance.  RL125's separate analytic statement that an `L=11` candidate must have `7<=Z<=33` remains valid.

This is a correction/repair, not a Gate A or Gate B closure.  Global nontrivial-cycle exclusion and Collatz remain open.

## RL127 kickoff

Resume constrained exact capacity generation for `L=11`, `7<=Z<=33`, using a CRT implementation that explicitly ignores empty fibres and independent direct recomputation checks on generated survivors.

# RL-2 Roadmap Update — 2026-08-19

## Rank 1 — k>0 relative height/rotation automaton

Replace the shared endpoint residue `Phi_h` as the principal state by the pair of physical inverse branches:

- tail branch `x_h=r_{k-h}`;
- periodically unwrapped cycle branch `z_h=c_{-h mod L}`.

Track at minimum:

- `delta_h=x_h-R#` or normalized `(x_h+1)/(R#+1)`;
- relative order/sign of `x_h-z_h`;
- tail exponent versus cycle exponent at the current reverse step;
- cycle phase modulo `L`;
- xi probe state `q_d(x_h)` for a small analytically justified probe set;
- prefix slack / forward cumulative exponent budget.

Primary target: prove that a branch beginning at `delta_0=c0-R#>0`, staying nonnegative, and ending at `delta_k=0` cannot coexist with the periodic comparison branch and all xi probes.

## Rank 2 — k=0 root-side xi probe sieve

Here `R#=C_min` and `R#=1 mod3`. Exploit the infinite valuation ceilings

`v3(2^(d-1)R#+1) <= floor((d-1)log2/log(3/2))` for every even `d`.

Fuse the first several analytically strongest probes with:

- six inherited mod-144 root classes;
- exact neutral-run length `v2(R#+1)-1`;
- cycle minimum rotation (`a_0=1`, `a_{L-1}` even);
- all-rotation common denominator integrality.

Do not treat a finite residue sieve as a proof unless a lift theorem classifies all higher probes.

## Rank 3 — cycle-wide side-branch probe profile

For every cycle state `y`, use

`xi(p_d(y)) = 2^q(2^(d-1)y+1)/3^q >= R#+1`.

This yields exact lower bounds on `y/R#` conditional on `q=q_d(y)`. The target is a rotation-frequency theorem showing that the periodic exponent word cannot avoid enough high-q probes while maintaining the cycle product slope.

## Rank 4 — only then reconsider inverse-basin counting

The new infinite-lift construction shows why mere existence of xi-safe inverse branches is cheap. Any counting route must still solve periodic-root physical ownership/collision multiplicity before it can become proof-bearing.

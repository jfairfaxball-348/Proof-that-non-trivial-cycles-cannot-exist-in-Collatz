# RL203 — H21 dyadic prefix information boundary

Date: 2026-08-31.

RL203 attacked the inherited joint-prefix moment after the RL202 root-anchor cut.
The outcome is a precise information boundary rather than an eta-class
elimination.

The exact endpoint moment normalizes to an odd 2-adic unit
`U_a=d*3^(1-a)*(2^34 eta-1)`, where `d=3^p-2^u`. The first 34 bits contain no
eta information; the next bit is precisely `eta mod 2`, already equivalent to
the terminal orientation/sign from RL199. Direct evaluation of the forced tau34
unit-cost tail gives exactly the same `2^35` residue, so no independent selector
is hidden in that shallow truncation.

The existing Hensel terminal restriction needs eta modulo `2^22`, hence endpoint
precision `2^56`. The first below-p source whose rank even enters the inherited
necessary core cannot occur until `a=p-39`: offsets 1..33 hit the positive-tail
zero-anchor obstruction, and offsets 34..38 map outside the inherited core. At
`p-39` the normalized root-prefix contribution begins at 2-adic depth 63, and
the depth increases farther from p. Thus for every below-p necessary source the
RL202 root anchor is absent from the complete Hensel-resolution truncation.

This does not show the exact complete-word route is dead. It identifies the
missing datum sharply: on the below-p side, a `2^56` attack must acquire
post-terminal completion information or another genuinely global coupling
rather than expecting the root normalization or already-forced 34-step tail to
choose the eta class/sign by themselves.

No necessary rank, eta class, state, sign, charge, Gate or global obligation is
closed in RL203. The inherited necessary count remains **16,188,727,234**.

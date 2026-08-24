# Collatz R# RL-5 Handover

RL-5 converts the k=0 plateau grammar into a deterministic anchor return map and then couples that map to the common cycle denominator.

The main new compression is exact:

`W_(j+1)=ceil(3^(h_j) W_j / 2^(h_j+t_j))`.

Clearing denominators and composing a cyclic compressed word gives, at every rotation,

`W_r=C_r/[6^M(2^A-3^L)]`.

Thus a fixed discrete word has at most one rational candidate anchor orbit. The composed numerator is automatically correct 2-adically, and its 3-adic unit condition is automatic unless an exit hits the exact saturation boundary `v3(2^t-1)=n`. In the generic no-boundary case this collapses further: **`D=2^A-3^L` dividing one rotation numerator is necessary and sufficient for the entire periodic integer anchor orbit to exist**, with all local exit valuations then forced exactly by the affine recurrence. Boundary exits form the separate 3-adic cancellation subproblem.

Earlier RL-5 results remain: exponential saturation cost, half-depth cost for any xi non-rise, exact final-return root probe/discrete-log address, and k>0 relative-order rigidity through reverse depth `2R#`.

The verifier also audits 165,728 generic admissible words with `P<=3`, `n,t<=8` against the scalar criterion; only three repetitions of the trivial `W=2` anchor are `D`-divisible. This is not a proof for arbitrary cycles.

No nontrivial-cycle exclusion is claimed.

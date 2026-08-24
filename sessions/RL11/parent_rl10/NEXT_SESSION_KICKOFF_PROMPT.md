Continue the Collatz R# RL research from the attached RL-10 handover bundle.

Do not restart earlier radius-1/radius-2 work. Inherited analytic facts include:

1. primitive `D`-divisible cycle rotations have transposition distance at least 3 (RL-9);
2. exact radius 3 has exactly three unit-flow edges, with support partitions `[3]`, `[2,1]`, `[1,1,1]` (RL-L62);
3. the connected `[3]` branch is analytically impossible (RL-L63);
4. in the coprime branch there is a common unit `theta` with `theta^L=2`, `theta^A=3` mod `D` (RL-L64);
5. `Q` divisibility is the geometric discrepancy sum `sum theta^(-H_i)=0` (RL-L65);
6. a radius-3 self-rotation is a three-jump walk `H_(i+m)=H_i+e+A G_i` (RL-L66);
7. mixed coprime one-orbit cases reduce to three explicit sparse forms, and same-direction coprime one-orbit cases reduce to `sigma^a+3sigma^b+9sigma^c=0` (RL-L67).

Highest priority: attack the sparse forms, using the natural-edge adjacency constraints on jump times. Second priority: prove the `gcd(A,L)=3` cubic-cofactor branch forces an exact third-repeat. Third priority: derive the `gcd(A,m)=3` three-orbit analogue.

The verifier's finite scan through `A<=40` has exactly one `D`-divisible radius-3 family: `101010/010101` with `(A,L,D)=(6,3,37)`, which is `(10)^3` and nonprimitive.

Keep guardrails: RL remains open; radius 3 remains analytically open in disconnected branches; do not promote finite evidence to theorem.

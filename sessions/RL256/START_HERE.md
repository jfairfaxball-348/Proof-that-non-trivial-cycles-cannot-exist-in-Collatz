# Frozen session — RL256

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

RL256 attacked the exact first halving selector
`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

Promoted RL256 contraction:

- terminal exponent `k` is reduced from `31<=k<=150` to
  `k in {31,33}`;
- for `k=31`, the exact weighted flank excess satisfies `E_31<=27`;
- for `k=33`, terminal-tail exclusion sharpens the complement isolated-root
  packing capacity to `286`, hence `E_33<=5`;
- consequently `k=33` forces both adjacent four-one blocks and at least one
  physical run `1^7` next to the canonical terminal structure;
- `k=33` also retains the lower bound `beta(P)>=281`.

A later in-session canonical terminal-state tree is explicitly **DEMOTED**:
it traced backwards from `J=2^33` without first restoring the omitted final
canonical `10` column. No `k=33` elimination is promoted from that tree.

Gate A remains open. Gate B remains open. Radius 4 is not invoked.
Radius 5 remains inactive.

Successor authority: RL257.

# RL256 session state and RL257 kickoff

Date: 2026-09-05

## Frozen outgoing state

Exact selector:
`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

Promoted terminal contraction:

- `k in {31,33}`;
- `k=31 => E_31<=27`;
- `k=33 => beta(P)>=281`;
- `k=33 => E_33<=5` and an adjacent physical `1^7` block.

Do not use the demoted provisional four-state terminal tree.

## Successor

RL257 should first restore the exact historical endpoint convention:

- the full physical word is `u=110 x 1 0^(k-3)`;
- the internal canonical pair path ends before the omitted terminal `(1,0)`;
- terminal `J=2^k` is reached only after that omitted final canonical `10`.

Then couple the `k=33` physical flank rigidity to the correctly indexed
absolute `(d,J)` ledger. Eliminate `k=33` only if a fully owned contradiction
is proved. If successful, attack the sole `k=31` branch with its `E_31<=27`
flank budget.

Gate A/B remain open at kickoff. Radius 4 is not invoked.

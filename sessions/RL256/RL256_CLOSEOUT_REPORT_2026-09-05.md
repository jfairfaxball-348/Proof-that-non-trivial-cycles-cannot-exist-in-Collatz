# RL256 closeout report

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

RL256 materially contracts the exact first halving selector
`(1100,694,406,317,200,14,4)`.

Promoted:

- `k in {31,33}`;
- `k=31 => E_31<=27`;
- `k=33 => beta(P)>=281`;
- `k=33 => E_33<=5`;
- `k=33` forces both adjacent four-one blocks and at least one physical `1^7`
  run next to the terminal structure.

Closeout red-team corrected a provisional absolute-state indexing mistake:
the omitted final canonical `10` column must be restored before backward
terminal tracing. The provisional four-state `k=33` tree and any claimed
`k=33` elimination from it are explicitly demoted.

No MILP result is promoted.

Gate A remains open. Gate B remains open. Radius 4 has not been invoked.
Radius 5 remains inactive. Global non-trivial-cycle exclusion remains open.

RL257 is prepared to re-index the full-phase terminal ledger correctly and
attack `k=33` first, then `k=31` if needed.

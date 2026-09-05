# RL256 correction and demotion ledger

Date: 2026-09-05

## Retained

The following RL256 results survive closeout red-team and are promoted:

1. `k in {31,33}` at the exact first halving selector.
2. `k=31 => E_31<=27`.
3. `k=33 => beta(P)>=281`.
4. `k=33 => E_33<=5`.
5. `k=33` forces both adjacent four-one blocks and at least one physical
   `1^7` run adjacent to the terminal structure.

These use only the exact 19-window identities, isolated `-1` root packing,
the exact q-window derivative, terminal physical zeros, `sum P=2`, and
inherited odd `k>=31`.

## Demoted

A later in-session backward canonical tree that started from terminal
`J=2^33` and enumerated four predecessor states is **not promoted**.

Reason: the historical full-phase convention places the canonical terminal
state after the omitted final `(1,0)` column. The provisional tree failed to
restore that final canonical `10` before tracing the forced internal ones.
Its absolute state indexing is therefore shifted.

Any claimed `k=33` elimination or terminal-state classification derived from
that provisional tree is also demoted.

## Computational evidence not promoted

An exploratory MILP found the exact selector infeasible under strong and even
weakened singleton conditions. No exact auditable certificate was extracted,
so this remains non-evidentiary computational guidance only.

## Binding older demotions

All RL249/RL250 demotions remain binding. The RL251 Gabriel-horn equivalence
remains frozen. No local physical P/Q pattern is treated as a Radius-4 input
without the audited ownership and exact-distance hypotheses.

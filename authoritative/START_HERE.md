# Authoritative start — RL257 correctly indexed terminal two-case attack

Incoming state: **RL257**.

Completed incoming generation: **RL256 — exact first-halving terminal contraction**.

RL256 promotes, at the unique first halving selector
`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`:

- `k in {31,33}`;
- `k=31 => E_31<=27`;
- `k=33 => beta(P)>=281`;
- `k=33 => E_33<=5`;
- `k=33` forces a physical `1^7` run adjacent to the terminal structure.

Important correction: RL256's provisional four-state backward terminal tree
is demoted. It omitted the final canonical `10` column that lies between the
end of the internal path and terminal `J=2^k`.

RL257 is **PREPARED, NOT STARTED**.

Read `RL257_CORRECTLY_INDEXED_TERMINAL_TWO_CASE_TARGET.md` first.

Gate A/B remain open. Radius 4 is not invoked. Radius 5 remains inactive.

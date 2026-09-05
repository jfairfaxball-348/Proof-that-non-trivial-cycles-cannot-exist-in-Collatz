# RL256 — exact first halving frontier target

Date prepared: 2026-09-05
Status: **PREPARED, NOT STARTED**

## Incoming result

RL255 contracts the uniform Branch-C frontier to the unique first surviving halving selector

`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

At this selector:

- `K=H/2=7`, `t=n/2=2`;
- exact 19-window identities hold:
  `7q=2a+19`, `7B=2z+7`;
- `260<=beta(P)<=354`;
- `31<=k<=150`;
- the 33 useful 19-window q-segments are pairwise disjoint;
- `beta(E)>=1032`.

RL255 also pushes the non-halving frontier to `a>=1986`, so the immediate global first frontier is halving.

## Authoritative target

Attack the exact `(1100,694,406,317,200)` halving selector before broadening again.

Priority:

1. Use `K=7` to turn the 33 disjoint 19-window sums into explicit finite constraints on the seven q-layers of P.
2. Combine the finite beta range `260..354` with Branch-C singleton gaps and the exact capacity inequality; classify equality/near-equality profile shapes where useful.
3. Lift the resulting P-support restrictions through `P_i=r-W_i(q)` and the derivative `P_(i+1)-P_i=u_i-u_(i+q)`.
4. Feed only exact owned structures into the canonical `(d,J)` / full-phase ledger.
5. Seek Gate A, exact full-phase contradiction, or a fully eligible owned Radius-4 encounter.

Do not treat survival of the arithmetic selector as survival of a cycle.

Gate A open. Gate B open. Radius 4 not invoked. Radius 5 inactive.

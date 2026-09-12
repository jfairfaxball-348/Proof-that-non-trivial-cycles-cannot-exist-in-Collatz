# RL305 proof and scope ledger

Date: 2026-09-12

## Final classification

`GATE_A_MINIMAL_SCALAR_DEPENDENCY_AUDIT_AND_MAXPLUS_WALL_FAST_TRACK_IDENTIFIED`

## Promoted analytic / exact derived results

1. From RL302's exact recurrences, for every positive even `E!=2`:
   `m_P(E)=2+min(m_R3(E),m_8(E),m_D0(E))`.

2. After handling the harmless exceptional endpoint `E=2`:
   `Bcal(P)=max(Bcal(R3_tower),Bcal(8),Bcal(D0))-2`.

3. Therefore:
   `Bcal(P)<=1`
   iff
   `Bcal(R3_tower)<=3`,
   `Bcal(8)<=3`,
   `Bcal(D0)<=3`.

4. Substitution into RL292's exact five-state front door yields the exact seven-scalar Gate-A dependency graph:
   - `Bcal(R3_tower)<=3`;
   - `Bcal(8)<=3`;
   - `Bcal(D0)<=3`;
   - `Bcal(4,39)<=3`;
   - `Bcal(2,-17)<=1`;
   - `Bcal(2,-84)<=2`;
   - `Bcal(3,-28)<=3`.

5. O1, O2, and the universal P/8 identity are stronger sufficient routes, not necessary logical dependencies of Gate A.

6. RL297's strategic wording is corrected:
   `Bcal(8)<=3` literally gives the nonempty ceiling `nu_2(E)<=A+3`;
   the historical `nu_2(E)<=A+1` excess-one conjecture is stronger by two units.
   No previously promoted theorem is demoted.

7. For the D0 zero spine:
   `C_A(d)=d^2-2d-1`,
   `C_F(d)=d^2-d-2`,
   and
   `Bcal(D0)<=3`
   iff
   `Bcal(A_d)<=C_A(d)+3` and
   `Bcal(F_d)<=C_F(d)+3`
   for all `d>=3`.

8. The R3 tower zipper identifies the normalized tight-wall family targets:
   `Bcal(L_D)<=B_L(D)+3`,
   `Bcal(RW_D)<=B_R(D)+3`
   for odd `D>=3`, jointly with the checkpoint-8 ceiling and the shallow renewal branch.

9. Reweighting the exact RL303 D-to-D-2 mergers by RL302 wall credits gives normalized max-plus edge weights:
   - `L_D -> RW_(D-2)`: `k-D-4`;
   - `L_D -> L_(D-2)`: `k-2D-5`;
   - `RW_D -> L_(D-2)`: `k-3D-2`;
   - `RW_D -> RW_(D-2)`: `k-2D-8`.
   The adjacent-wall `L_D -> RW_D` branch has weight `D-k-1`.

These weighted formulas are exact only on the legal prefix families inherited from RL303. They are not a complete transducer theorem.

## Strategic findings

- The recent O1/P8 programme over-generalized the scalar theorem needed by Gate A.
- RL302–RL304 wall/PQ algebra remains valuable when reweighted by the actual Bellman credits.
- Syntactic grammar termination is not required if a complete weighted quotient has a decreasing potential / negative cycles.
- The successor should test this directly before resuming unweighted P/Q commutation.

## Historical audit conclusion

Across the programme, branch coverage, ownership, incidence, cancellation, upstream checkpoint reachability, and fixed-seed ancestry versus rejected-tube danger repeatedly express the same missing global resource.

No forgotten historical theorem was found that already closes Gate A.

Radius-4 remains a valid local theorem but its global encounter bridge remains open.

The physical/resonance route remains a strong finite accelerator with a finite-ladder barrier.

## Corrections / demotions

New theorem demotions: none.

New strategy/wording correction:
- `Bcal(8)<=3` is not identical to checkpoint-8 excess-one `nu_2(E)<=A+1`.

Historical corrections/demotions listed in earlier authoritative reports remain in force.

## Open

- Gate A;
- Gate B;
- O1/O2/P8;
- `Bcal(P)<=1`;
- `Bcal(8)<=3`;
- checkpoint-8 excess-one;
- RL296 residuals and the other non-P front-door sources;
- global non-trivial-cycle exclusion.

## Frozen routes

- RL304 fixed-96/twelve-factor P/Q grammar: preserved and reusable, not default priority.
- physical/resonance route: frozen at `a=7354673373747273032`.
- Radius 6+: frozen.
- Lean formalisation: separate.

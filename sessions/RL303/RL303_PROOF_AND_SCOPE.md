# RL303 proof and scope ledger

Date: 2026-09-12

## Promoted analytic mathematics

1. Exact checkpoint-8 all-depth entries to `L_D` and `RW_D` miss the RL302 tight credits by a uniform `+3`.
2. General dyadic wall-lift theorem:
   `C_(D,t) 0^D = W_(D,t)` with cost `(D^2-D-2)/2`, where `W_(D,0)=L_D`, `W_(D,1)=RW_D`.
3. Fixed-cell factorisation `RW_D=Q^((D-1)/2) o U`, with `Q=(2,18)`, `U=(1,6)`.
4. Collision-free restatement of the inherited factorisation `L_D=R2 o RW_(D-2)`.
5. Translation-invariant adjacent-wall normal form
   `S 0 1^k01 = S^+ 1^(k+1)00`
   and its exact leading-P sibling for every unit wall translate `S^+=S+(0,3^d)`.
6. Four exact all-depth `D -> D-2` wall merger families with continuation differences `4-k`, `6-k`, `2-k`, and `7-k`.
7. Leading-P first-wall structural reduction: before the left P factor first reaches formal depth zero, the physical P-side accumulates strictly positive relative historical reserve; the first rejected descent normalizes to an integer wall debt `H_a=(0,a)` adjacent to the remaining positive factor.
8. Exact physical quadratic counterfamily showing generic linear-in-D wall-debt amortisation is false:
   for `D=6n+3`, `W_(D,4)1^(3n)` versus `W_(D,0)(110)^n` has relative cost `-3n(n-1)/2`.
9. Exact physical P/Q commutation identity `(P o Q)01110=Q o P` with cost 14.
10. Exact Q-return family `Q 0(10)^r110=Q` with cost 2 and propagated output `00(01)^r11`.
11. Direct root correction: `R3 011=RW_3` at cost 7 while checkpoint 8 reaches `RW_3` by `01001` at cost 6.

## Important non-claims

- O1 is not proved or refuted.
- The four `D -> D-2` families are not claimed to form a complete prefix cut.
- No generic leading-P or trailing-P monotonicity is claimed.
- No generic integer-wall-debt ownership theorem is claimed; Section 8 above rules out the simplest linear-credit version.
- The P/Q identity is one-cell commutation only; no repeated full-stack grammar is yet proved.
- No universal cheap entry to higher dyadic lattice cells `t>=2` is claimed.
- Bounded shortest-path evidence from the research process is not promoted as an all-depth theorem.

## Corrections / notation discipline

- Use `Rt(d)` for tower `(d,3^d)` and `RW_D` for the right tight wall. The older overloaded letter `R` caused an apparent but not real inconsistency in the RL302 factorisation.
- The root-level renewal detour after `R3 011` is superseded by the direct checkpoint-8 ownership splice at `RW_3`.

## Still open

- O1: `m_R3(E)>=m_8(E)` all depth.
- O2 in full.
- `m_P(E)=m_8(E)+2` all depth.
- `Bcal(P)<=1` / checkpoint-8 excess-one.
- RL296 non-P front-door residuals.
- Gate A.
- Gate B.
- Global non-trivial-cycle exclusion.

## Frozen branches

RL301 physical/resonance work remains frozen at external selector frontier `a=7354673373747273032`. Radius 6+ and the separate Lean formalisation remain out of scope.

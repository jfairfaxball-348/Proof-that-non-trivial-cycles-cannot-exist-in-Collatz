# RL303 closeout

Date: 2026-09-12
Base commit: `7a83d6fb5344acc4e477ae5d19fed9414534acda`
Base tree: `c8a98ddaa2ebf3e9295c7a0aafa90910df36b92e`
Successor: RL304

## Final classification

`DYADIC_WALL_LATTICE_TRANSLATION_NORMAL_FORM_P_FIRST_WALL_REDUCTION_AND_GENERIC_LINEAR_DEBT_BARRIER_WITH_PQ_COMMUTATION_PROVED`

## Promoted state

1. Checkpoint 8 has exact all-depth entries to both tight wall families at uniform debt `+3` relative to the RL302 wall credits.
2. The L/R walls extend to an exact dyadic lattice `W_(D,t)` with pure-zero boundary lifts.
3. `RW_D` is an iterated fixed-Q cascade `Q^((D-1)/2) o U`; the inherited L factorisation is restated without the R-notation collision.
4. RL302's L/R run-length theorem generalizes to every adjacent wall translation `S -> S^+`.
5. Four exact all-depth `D -> D-2` merger families close large recursive wall cylinders.
6. Every leading-P sibling accumulates positive relative reserve before its first P-factor wall hit, where it normalizes to an integer wall debt `H_a`.
7. A legal physical counterfamily proves generic linear-credit wall-debt amortisation false: fixed four-cell separation can incur quadratic adverse paired cost.
8. A new exact physical P/Q commutation identity `(P o Q)01110=Q o P` costs 14.
9. Q has an exact all-r cost-2 return family `Q 0(10)^r110=Q`, giving a concrete successor grammar target.

## Proof-state qualification

O1 remains open. Hence O2, the universal P/8 identity, `Bcal(P)<=1`, checkpoint-8 excess-one, and Gate A remain open.

The session materially changes the Bellman strategy: generic wall-debt amortisation is now ruled out, and the preferred continuation is fixed-cell P/Q commutation on the actual `Q^n o U` right-wall stack.

## Corrections / demotions

- use `RW_D` for the right tight wall and `Rt(d)` for the tower; the older overloaded `R` notation caused an apparent false inconsistency;
- simple dyadic precursor ownership is not a universal closure route;
- root P-renewal after `R3 011` is superseded by a direct checkpoint-8 splice at `RW_3`;
- six-cell lattice rebasing is unproved and remains scratch;
- bounded shortest-path and renewal-tree observations remain evidence only.

## Verification

The self-contained closeout verifier `sessions/RL303/verification/verify_rl303_structural.py` is green. See `RL303_FRESH_VERIFICATION.txt`, frozen verifier output, and `SHA256SUMS.txt`.

## Successor

`RL304_PQ_COMMUTATION_O1_TARGET.md`

RL304 should remain on O1 and build a complete finite commutation/refactorisation grammar that moves the leading P factor through the fixed Q stack in `RW_D=Q^n o U`, with exact physical cost accounting against the inherited wall credits. It must not revert to generic integer wall-debt amortisation, which RL303 now disproves as a proof strategy.

## Catalogue status

`stale/deferred` — generated knowledge catalogues are unchanged and outside the promotion gate.

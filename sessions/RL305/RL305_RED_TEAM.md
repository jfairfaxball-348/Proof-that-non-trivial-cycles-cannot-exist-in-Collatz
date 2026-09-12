# RL305 red team

Date: 2026-09-12

Result: `RL305_AUDIT_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`

## 1. No Gate-A overclaim

The new scalar reductions do not prove any of the seven required scalar ceilings. Gate A remains open with inherited terminal residual `k>=31`, odd, `H_can<k`.

## 2. Exceptional endpoint E=2

RL302's source recurrences are stated for `E!=2`.

For the Bellman-envelope identity, `E=2` cannot change the source maximum because:

- `nu_2(2)=1`;
- source costs are nonnegative, so the E=2 score is at most 1;
- checkpoint 8 itself contributes score 3 to `Bcal(8)`.

Thus the maximum source envelope is controlled by non-2 endpoints. On the P side, the exact P-to-8 path gives score 1, while the E=2 contribution is not larger. The scalar identity is therefore unaffected.

## 3. Extended-real safety

The min/sup manipulation remains valid if an envelope is infinite: finite minima convert endpoint scores to finite maxima, and sup over a finite maximum is the maximum of the sups. No finiteness of `Bcal` is assumed by the algebraic reduction.

## 4. R3 notation collision

Earlier sessions use `R3` for more than one object. RL305's scalar identity uses RL302's tower source `(d,K)=(3,27)`. The report calls it `R3_tower` where ambiguity matters.

## 5. Checkpoint-8 correction scope

The statement corrected is strategic wording, not a promoted theorem.

The finite RL293 excess-one certificate remains valid. The all-depth excess-one conjecture remains open. No proof depending on excess-one is reclassified as proved.

## 6. Wall-family scope

The normalized max-plus weights are derived only for the exact legal RL303 prefix families. They do not establish:

- a complete prefix code;
- finite-state closure;
- a decreasing potential;
- negative total weight on all cycles;
- O1;
- `Bcal(P)<=1`.

RL306 must prove coverage before using the weighted graph as a closure theorem.

## 7. Generic wall-debt barrier remains active

RL303's quadratic adverse counterfamily is not erased by credit normalization. Any successor transducer must explicitly exclude, absorb, or negatively weight the corresponding legal behavior. It may not assume generic linear debt amortisation.

## 8. P/Q grammar remains unclosed

RL304's fixed-96/twelve-factor grammar is preserved exactly. RL305 does not reinterpret its finite grammar as an all-depth termination theorem.

## 9. Non-P front door remains load-bearing

Even a future proof of `Bcal(P)<=1` is insufficient for Gate A. The four non-P front-door inequalities remain open, with `(4,39)` only reduced to RL296's explicit residuals.

## 10. Historical authority

RL305 did not rerun every historical expensive finite certificate. It relied on the repository's accepted frozen authority under verification economy and reopened exact reports where a live dependency mattered.

No new historical correction requiring demotion was found.

## 11. Frozen-route integrity

- physical/resonance remains frozen at `a=7354673373747273032`;
- Radius 4 remains valid local mathematics;
- Radius 6+ remains frozen;
- Lean work remains separate.

## 12. Successor falsification rule

RL306 must pivot rather than proliferate coordinates if a complete normalized quotient exhibits an iteratable nonnegative Bellman-excess cycle or cannot avoid an infinite unresolved state parameter without rebuilding unrestricted checkpoint futures.

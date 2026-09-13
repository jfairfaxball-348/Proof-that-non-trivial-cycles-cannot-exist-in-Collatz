# RL308 red team

Date: 2026-09-13
Result: `RL308_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`

## Checks

1. **Conditional hypothesis retained.**
   The X reduction is explicitly conditional on the still-open `Bcal(2,-17)<=1`. RL308 does not silently promote that inherited obligation.

2. **Complete cut, not sampled prefixes.**
   The twelve leaves are pairwise prefix-free and their exact Kraft sum is one.

3. **Early checkpoint escape excluded.**
   Every proper internal cut node is replayed and checked not to be a positive-even `d=1` checkpoint. Thus a Bellman future cannot terminate before the cut and bypass the leaf analysis.

4. **Physical-state splice validity.**
   Each of the ten owned X leaves is replayed to a physical state reached exactly by the frozen `(2,-17)` owner word. Future legality and Bellman continuation depend on the physical state, so the cheaper/credited owner may copy the identical suffix.

5. **Costs checked independently.**
   X ingress costs, owner ingress costs, and branch bounds are recomputed by the portable verifier.

6. **Residuals not declared safe.**
   `(7,2039)` and `(7,2546)` remain open at ceiling 31. The theorem is a dependency reduction, not closure of X.

7. **Y untouched.**
   No result from the exploratory Y/X state-owner scan is promoted. `Bcal(Y)<=12` remains wholly open.

8. **Finite minimizer evidence not globalized.**
   Common-state shortest-word patterns through `(2,19)` and `(1,15)` are supporting exact identities only. There is no claim that dangerous all-depth futures must use them.

9. **State-capped excluded-prefix scan not certified.**
   The X-without-`11101` computations hit their one-million-state cap and are explicitly classified as incomplete evidence.

10. **Naive potential failure retained.**
    The local logarithmic potential counterexample is recorded so the failed shortcut is not accidentally revived as a theorem.

11. **No Gate-A overclaim.**
    The RL307 `(-28)` node remains open because X and Y ceilings and the inherited `(-17)` / `(4,39)` obligations are not all closed.

12. **Strategic pivot is not a mathematical demotion.**
    Freezing the current local programme changes priority only. It does not alter the proof status of any theorem or certificate.

## Final disposition

The only new promoted mathematical claim is the exact conditional X prefix-cut dependency reduction at its stated scope.

The strategic successor is planning-only RL309.

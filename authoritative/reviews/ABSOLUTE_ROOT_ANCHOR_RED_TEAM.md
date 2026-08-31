# RL202 absolute-root-anchor red team

Date: 2026-08-31. PASS after scope tightening.

Checks performed:

1. The speed estimate is used only where the unique p-shift carry source
   `z=L-p` is absent. Both length-`2^24` root windows are strictly separated
   from z.
2. The backward window is anchored at lifted `K_L=lambda K_0`, not silently at
   `K_0`. The proof carries an explicit conservative `+1`, justified from
   `delta<2^-40`; no equality of the two anchors is asserted.
3. The rank interval is consumed only for H21 terminals whose **terminal phase**
   lies in the named windows. It is not promoted as a new unconditional global
   rank core.
4. Strict reverse-rank monotonicity is inherited and re-certified with the same
   sign-correct log enclosure contract repaired in RL201.
5. Modular counting covers complete windows with exact floor sums. Seven forward
   candidates already deleted by RL201 are subtracted exactly; none is double
   counted backward.
6. The four new zero-height collisions are outside the root windows. The proof
   uses the exact 34 positive H21 heights only; it does not infer zero-edge
   ownership or revive a barred route.
7. The failed scratch list digest is not proof state. Replacing it by exact set
   predicates and counts removes an ordering dependency without changing the
   mathematical result.
8. Necessary ranks are never called physical populations. All four eta classes,
   H21 charge, state/sign and Gate/global obligations remain open.

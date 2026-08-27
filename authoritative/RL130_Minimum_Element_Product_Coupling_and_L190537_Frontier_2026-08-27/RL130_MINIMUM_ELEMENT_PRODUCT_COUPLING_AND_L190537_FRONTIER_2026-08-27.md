# RL130 - minimum-element product coupling and the L>=190,537 frontier

Date: 2026-08-27

RL130 advances the internally certified primitive positive ordinary shortcut-cycle frontier from `L>=41` to **`L>=190,537`**. Gate A and Gate B remain open; global nontrivial-cycle exclusion and the Collatz conjecture remain open.

## Classification
- inherited analytic: RL129 quotient-cycle dynamics; RL19 odd-step product identity / least-state framework;
- new analytic: exact-p0 transition-root Q bound, minimum-state rational ceiling, monotonicity in A;
- exact finite arithmetic: complete L=41..190537 frontier scan;
- exact finite computational checkpoint: all odd starts through 15,671,092,983 descend under the halved Collatz map, produced in-session and frozen under verification economy;
- unpromoted: adaptive residue-class descent beyond the wall and any external-floor enlarged frontier.

## Sharpened transition-root bound
Choose a cyclic root starting in 1 and ending in 0. Then p_0=0 and p_j<=Z-1+j for j>=1, so
`Q <= 3^(L-1) + 2^Z(3^(L-1)-2^(L-1))`.
This sharpens the relaxed RL129 bound.

## Minimum-element coupling
RL19 gives `lambda=2^A/3^L=product_odd(1+1/(3x_i))`. If m is the least cycle state, then m is odd and x_i>=m, hence
`log(lambda)<=L/(3m)`. Also `log(lambda)>=(lambda-1)/lambda`, so
`m <= L*2^A/[3(2^A-3^L)]`.
Thus `m <= floor(L*2^A/(3D))`, D=2^A-3^L. For fixed L this ratio decreases with 2^A, so the worst case is the smallest A with 2^A>3^L.

## Exact frontier
Against the frozen descent checkpoint B=15,671,092,983, exact integer scanning gives: every 41<=L<=190,536 has largest possible odd m<=B; the largest pre-wall odd ceiling is 7,216,128,937 at L=158,670. The first failure is L=190,537, A=301,994, integer ceiling 984,572,842,736 and odd ceiling 984,572,842,735. Therefore RL129+RL130 certify the primitive ordinary frontier L>=190,537.

The accepted external peer-reviewed 2^71 least-state computation is not used to enlarge this internally promoted frontier in RL130. Hercher/corrigendum-dependent consequences are likewise non-load-bearing here.

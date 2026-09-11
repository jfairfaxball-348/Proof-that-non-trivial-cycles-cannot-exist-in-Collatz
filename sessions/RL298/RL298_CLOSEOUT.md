# RL298 closeout

Date: 2026-09-11

RL298 closes as

`SELECTOR_FRONTIER_EXACT_FINITE_PHYSICAL_CERTIFICATE_TO_A301994_WITH_RESONANCE_COORDINATES`.

## Main result

The frozen selector/branch programme was resumed from the exact post-RL262 predicate. The fifth retained selector is

`(a,ell,z,q,r,H,n)=(1436,906,530,1119,706,18,14)`,

with no retained selector for `1418 <= a < 1436`.

RL298 then replaced the increasingly expensive ordered-prefix branch tree by a simpler exact physical certificate derived from the promoted RL263 physical two-trajectory identity.

For an admissible phase quotient `N == 19 (mod 24)`, define

`A0=(9N+5)/8`, `B0=(27N+127)/8`

and iterate the half-Collatz map. A genuine full phase at selector `(a,ell,...)` has internal length `m=a-k-1`, common internal one-count `rho=ell-3`, and inherited odd terminal exponent `k>=31`. Hence `m<=a-32`. If the two physical trajectories cannot each accumulate `rho` odd steps by this longest possible horizon, the whole selector is impossible.

Using the exact full-phase quotient equation gives a finite selector-dependent ceiling `Nstar`. Exact integer selector scanning and finite physical replay establish:

- 2,648 retained selectors through `a=100000`;
- 8,057 retained selectors through `a=301994`;
- maximum `Nstar` through `a=100000` is `803113`, at selector
  `(75235,47468,27767,25781,16266,928,318)`;
- the first severe post-100000 resonance spike is the final selector in the frozen window,
  `(301994,190537,111457,50508,31867,3725,623)`,
  with `Nstar=136073747`;
- every required physical trajectory for `N<=803113`, `N==19 (mod24)`, reaches `1` within 291 half-Collatz steps;
- every required physical trajectory for `N<=136073747`, `N==19 (mod24)`, reaches `1` within 588 half-Collatz steps;
- the minimum value of `2*rho-(a-32)` over selectors through `a=100000` is 314;
- over `100000<a<=301994` it is 26214.

After first reaching `1`, the half-Collatz orbit is the exact `1 <-> 2` cycle, so in any remaining suffix odd steps occur every second step. The stopping bounds above therefore force the physical one-count strictly below `rho` throughout the frozen selector window.

Consequently every one of the 8,057 retained selectors through `a=301994` is eliminated.

This is an exact finite certificate, not a global theorem.

## New exact selector-coordinate identities

Writing

`z=a-ell`, `B=q-r`, `H=12a-19ell`, `n=12q-19r`,

the determinant condition `a*r-q*ell=2` is equivalent to

`B*H-z*n=14`,
`q*H-a*n=38`,
`r*H-ell*n=24`.

For a halving selector `H=2K`, `n=2t` this becomes

`K*B-z*t=7`,
`K*q-t*a=19`,
`K*r-t*ell=12`.

These identities explain the small `(K,t)` relations repeatedly observed in earlier selector certificates.

## Correction / demotion

A scratch interpretation developed during RL298 suggested that the ordered dyadic prefix congruence might force a selector-independent alternating/half-density corridor.

That interpretation is rejected.

RL263 already proves that on every genuine physical full-phase pair the ordered-prefix congruence is an automatic physical-gap telescope. RL263 also restores the stronger modulus `2^m` in the inherited odd-`k`, `N==19 (mod24)` scope.

The repeated prefix/residue patterns remain valid descriptive arithmetic, but they are not an independent obstruction and must not be used as a global density theorem.

The selector eliminations frozen here do not depend on that discarded interpretation; they use deterministic physical trajectories plus terminal one-count ownership.

## What remains open

RL298 does not prove:

- Gate A;
- Gate B;
- a uniform all-selector stopping theorem;
- a uniform bound on future resonance spikes;
- global non-trivial-cycle exclusion.

The RL297 P-bottleneck result remains parked weak-green background only.

## Successor direction

RL299 should start from the frozen exact finite certificate, independently replay its fast arithmetic side, and investigate the arithmetic structure of future resonance spikes. The goal is to determine whether the physical quotient certificate can be made uniform or extended in certified resonance blocks without assuming any unproved global Collatz stopping statement.

Do not revive the RL298 ordered-prefix corridor interpretation.

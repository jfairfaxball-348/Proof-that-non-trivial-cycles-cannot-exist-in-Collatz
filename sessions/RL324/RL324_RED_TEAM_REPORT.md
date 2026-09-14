# RL324 red-team report

Date: 2026-09-14
Status: PASS FOR STATED RL324 SCOPE

## R1 — no reuse of the withdrawn cyclic wrap

PASS.

RL324 uses only the interior matched-rank recurrence after proving `j<ell`. It makes a linear sign-transition statement only. No same-row cyclic wrap or cyclic one-crossing theorem is revived.

## R2 — state alignment at the zero-carry rank

PASS.

At the RL323 extracted matched rank,

`beta=v[v_j:u_j]`

starts at the early-row physical state `Q_j`, while the common Euclidean quotient is the late-row physical state `P_j`. Therefore the frozen identity

`z=2^rP_j+eta`

is exactly

`Q_j=2^(d_j)P_j+eta`

and `Delta_j=-eta`.

## R3 — interior-rank prerequisite

PASS.

RL323 gives crossing height `h>=2`. At the final late-row odd rank the early-row lead immediately before that odd event is one, so the first zero-carry crossing cannot be final. Hence `j<ell`.

## R4 — equality case and quotient orientation

PASS.

The recurrence gives `Delta_(j+1)>=0`. Equality is excluded by odd parity when `d_(j+1)>0` and by primitivity when `d_(j+1)=0`.

Thus `Delta_(j+1)>0`, and because it is strictly smaller than the dyadic cell size,

`Q_(j+1)=2^(d_(j+1))(P_(j+1)-1)+eta_(j+1)`

with a genuine Euclidean remainder `0<eta_(j+1)<2^(d_(j+1))`.

## R5 — full ownership

PASS.

The sign flip is read through the genuine complementary `ell`-odd numerator identity

`2^d A-C=-H Delta`.

No affine factor is relabelled as an ordinary row.

## R6 — original canonical rank bridge

PASS.

At the least-root canonical rank,

`Delta=-2^r c0-eta`.

Since `0<eta<2^r`, its sign is exactly determined by whether `c0>=0` or `c0<=-1`. RL321's

`K=3^s c0+J`, `0<J<3^s`

makes this equivalent to the sign of `K`.

## R7 — K>0 canonical bound

PASS IN EXTERNALLY CONDITIONAL FIRST-SURVIVOR SCOPE.

For `c0>=0`, the genuine canonical prefix numerator satisfies

`A=D0m+Xc0+2^p eta>D0m`.

This is the load-bearing lower inequality used by the RL323.5 zero-count proof, so the same exact rational boundary certificate yields

`r_can<=77265916075`.

No support enumeration is used.

## R8 — adjacent lower-side bound

PASS IN EXTERNALLY CONDITIONAL FIRST-SURVIVOR SCOPE.

The subtractive prefix error is `<X/2^(a_j)`. Global minimality bounds its normalized contribution by `<(X/Y)/3`.

The portable RL324 verifier replays the frozen rational logarithm enclosure and proves that, after subtracting the rigorous worst-case loss `(1+2^-40)/3`, the old excluded boundary `q=3182833229` still misses by more than `0.1224622103775`.

## R9 — propagation counterfamily

PASS AS A METHOD BARRIER ONLY.

The `(d,Delta)=(3,1)` construction with arbitrary exact `v2(3P+1)=a` consists of genuine local ordinary odd-to-odd transitions and gives `d'=a+2`, `Delta'=5`.

It is not claimed to be a cycle, an ordered full return, or a counterexample to any global ownership theorem. It only blocks local propagation arguments that do not use those global hypotheses.

## R10 — RL141/RL142 scope

PASS.

The bounded nearby-integer mismatch clock in the remaining `K<0` branch does not automatically satisfy the height-one multiblock hypotheses of RL141/RL142; in particular the live branch is `g=2`.

## R11 — parent/global scope

PASS.

RL324 does not close the full parent bridge. It closes/bounds the `K>0` canonical sign half and isolates the remaining `Z0>0, K<0` branch. R1 remains open; R2–R7 remain open.

Verdict: promotion-safe with stated scope.

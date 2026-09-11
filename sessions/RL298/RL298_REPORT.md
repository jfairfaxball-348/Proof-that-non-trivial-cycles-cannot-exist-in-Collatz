# RL298 report — selector return, physical quotient certificate, and resonance frontier

Date: 2026-09-11
Incoming main: `56d1a7caf563c7cac98faf7cb5515f63d31b6235`

## 1. Authority recovered

RL298 reconstructed the exact selector predicate from the promoted RL260/RL262 verifier family:

- exact resonance;
- determinant-two solutions;
- selector coordinates `z=a-ell`, `B=q-r`,
  `H=19z-7a=12a-19ell`,
  `n=19B-7q=12q-19r`;
- halving / non-halving floors and capacity conditions.

The fourth selector from RL262 is
`(1417,894,523,317,200,18,4)`.

## 2. Fifth through eighth selectors

The next retained selectors are exactly:

1. fifth: `(1436,906,530,1119,706,18,14)`;
2. sixth: `(1753,1106,647,1436,906,22,18)`;
3. seventh: `(1772,1118,654,485,306,22,6)`;
4. eighth: `(1921,1212,709,802,506,24,10)`.

Initial scratch replayed these with the RL262 full-phase finite machinery and found zero survivors. A later RL263 audit showed that the attempted selector-independent interpretation of the prefix congruence was tautological on genuine physical pairs. The finite conclusions survive, but the final frozen certificate uses the cleaner physical trajectory formulation below.

## 3. RL263 physical reformulation

In the inherited odd-terminal full-phase branch, RL263 proves that the canonical internal words are the parity itineraries of

`A0=(9N+5)/8`,
`B0=(27N+127)/8`

under the half-Collatz map

`F(x)=x/2` for even x,
`F(x)=(3x+1)/2` for odd x.

A genuine full phase requires both internal words to have length

`m=a-k-1`

and common one-count

`rho=ell-3`.

Since inherited terminal ownership gives odd `k>=31`,

`m <= a-32`.

Thus it is sufficient to rule out weight `rho` at the longest possible horizon.

## 4. Exact quotient ceiling

Let

`M=2^a-3^ell`.

RL65/RL262 give

`(N-2)M = 237*3^rho - 12*Dcal - 2^(a-k+1)`

with `Dcal>=0` and `N==19 (mod24)`.

For fixed selector the right side is maximized at the largest admissible odd `k<=z+2`. This gives the finite exact ceiling used by the verifier:

`Nstar = floor((237*3^rho - 2^(a-kmax+1))/M) + 2`.

Only `N=19,43,67,... <= Nstar` need be checked.

## 5. Stopping-time-to-weight lemma

Suppose one physical trajectory reaches `1` after at most `s` half-Collatz steps. After that it follows

`1 -> 2 -> 1 -> 2 -> ...`.

At horizon `m`, its total number of odd steps is at most

`ceil((m+s)/2)`.

Therefore if

`2*rho - m >= s+2`,

the trajectory cannot have accumulated `rho` odd steps by horizon `m`.

If the same bound holds for both physical trajectories for every admissible `N`, the selector is impossible.

This is a finite deterministic certificate. It does not assert a uniform stopping theorem for arbitrary integers.

## 6. Exact selector frontier

The exact integer scan uses no floating-point resonance test. It maintains `2^a`, `4^a`, `3^ell`, and `9^ell` by integer recurrence, with `ell` the unique integer satisfying

`3^ell < 2^a < 3^(ell+1)`,

then applies the exact resonance test

`15*4^a < 16*9^ell`.

Counts:

- retained selectors through `a=100000`: 2,648;
- retained selectors through `a=301994`: 8,057;
- post-100000 selectors in the frozen extension: 5,409.

The last selector is

`(301994,190537,111457,50508,31867,3725,623)`.

## 7. Finite physical envelopes

### Through a=100000

Maximum quotient ceiling:

`Nstar=803113`

at

`(75235,47468,27767,25781,16266,928,318)`.

Exhaustive physical replay over all `N==19 (mod24)` through this ceiling found that both required starting trajectories reach `1` within 291 half-Collatz steps.

Across all retained selectors in this window,

`min(2*rho-(a-32)) = 314`.

Since `314 >= 291+2`, every selector is eliminated by the stopping-time-to-weight lemma.

### 100000 < a <= 301994

Maximum quotient ceiling:

`Nstar=136073747`

at the final resonance spike

`(301994,190537,111457,50508,31867,3725,623)`.

There are 5,669,739 admissible quotients in this envelope and 11,339,478 physical starting trajectories. Exhaustive replay found every one reaches `1` within 588 half-Collatz steps.

Across all retained selectors in this window,

`min(2*rho-(a-32)) = 26214`.

Since `26214 >= 588+2`, every selector in the window is eliminated.

At the spike itself:

`rho=190534`,
`mmax=301962`.

The generic stopping bound gives at most

`ceil((301962+588)/2)=151275`

odd steps, versus the required 190534, a deficit of 39259.

## 8. Selector-coordinate determinant compression

With

`z=a-ell`,
`B=q-r`,
`H=12a-19ell`,
`n=12q-19r`,

direct substitution into `a*r-q*ell=2` gives

`B*H-z*n=14`,
`q*H-a*n=38`,
`r*H-ell*n=24`.

Conversely,

`a=(19z-H)/7`,
`ell=(12z-H)/7`,
`q=(19B-n)/7`,
`r=(12B-n)/7`.

For halving selectors `H=2K`, `n=2t`:

`K*B-z*t=7`,
`K*q-t*a=19`,
`K*r-t*ell=12`.

This is an exact analytic simplification worth retaining for future resonance-family work.

## 9. Red-team correction: ordered-prefix corridor

RL298 briefly pursued a universal prefix residue/corridor interpretation. Repository authority RL263 is decisive against that use.

RL263 proves

`C-S_p = 2^p * 3^(rho-Y_p) * (B_p-3^(d_p-1)A_p)`,

hence the ordered prefix congruence is automatic on genuine physical full-phase trajectories. It is not an independent density constraint.

RL263 also proves in the inherited odd-k scope

`Dcal = C - 2^m * (1+(N-2)*2^(k-1))/3`,

so the correct promoted modulus is `2^m`.

The corridor interpretation is therefore demoted and must not be continued.

## 10. Scope

Gate A remains open.
Gate B remains open.
RL297 P-bottleneck work remains weak-green and parked.
Radius 6+ remains frozen.
RO/divergent-orbit work remains out of scope.
The Lean formalisation repository is separate.
No global non-trivial-cycle exclusion is claimed.

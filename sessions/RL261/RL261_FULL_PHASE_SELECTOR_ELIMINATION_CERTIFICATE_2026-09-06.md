# RL261 exact full-phase elimination certificate

Date: 2026-09-06
Classification: **EXACT FINITE CERTIFICATE**
Scope: the single selector `(a,ell,z,q,r,H_sel,n)=(1287,812,475,485,306,16,6)`.

## Result

There is no genuine full-phase survivor at this selector.  The exact terminal
frontier first contracts to

`k in {31,33,35,37,39}`

and every one of those five terminal exponents is then eliminated by the
ordered rank-defect/full-phase quotient certificate described below.

This removes the whole third selector from the branch simultaneously unresolved
by Gate A and Gate B.  It does **not** close Gate A, Gate B, RL, or the Collatz
conjecture globally.

## Exact selector geometry

The identities are

- `1287*306 - 485*812 = 2`,
- `19*475 - 7*1287 = 16`,
- with `B=485-306=179`, `19*179 - 7*485 = 6`.

The even-halving geometry gives `K=8`, `t=3` and

- `8*485 = 3*1287 + 19`,
- `8*179 = 3*475 + 7`.

The eight exact 33-site physical blocks are

`[129,161] [297,329] [446,478] [614,646] [782,814] [931,963] [1099,1131] [1248,1280]`.

The complement gaps have lengths

`[135,116,135,135,116,135,116,135]`,

total complement size `1023`.

For terminal tail lengths `tau=28,30,32,34,36,38,40`, the exact tail capacities
are respectively

`338,337,337,336,335,335,334`.

The corresponding guaranteed-root values used here are

`R(tau)=262,283,300,313,322,327,328`.

The canonical nine-bit right-prefix family from `(d,J)=(1,-13)` has exactly
199 legal members.  Its minimum weighted-zero cost is 11, attained only by
`110110111` and `110111010`.

At `tau=38`, available tail room is `335-(327-2)=10<11`; hence `k>=41` is
impossible.  Together with the inherited lower terminal restriction, the exact
pre-phase frontier is `{31,33,35,37,39}`.

## Full-phase identity used

RL261 uses the promoted RL65 full-phase/rank-defect theorem.  With

- internal length `m=a-k-1`,
- common internal one-count `rho=ell-3=809`,
- `M=2^a-3^ell`,
- ordered one positions `a_j,b_j`, and
- rank defect
  `Dcal = sum_j 3^(rho-j) (2^(a_j)-2^(b_j)) >= 0`,

the full-phase quotient satisfies

`(N_phase-2) M = 237*3^rho - 12*Dcal - 2^(a-k+1)`,

with `N_phase>0` and `N_phase == 3 (mod 8)`.

Non-negativity gives `N_phase<=1209` for every live `k`.  Integrality together
with `N_phase == 3 (mod 8)` leaves exactly 50 possible values:

`N_phase = 19,43,67,...,1195` (step 24).

For a canonical prefix of length `p`, let `S_p` be the exposed ordered rank
partial sum.  Every future term is divisible by `2^p`, so a genuine phase must
satisfy

`Dcal == S_p (mod 2^p)`.

The verifier follows the actual canonical `step_x` transition, updates the
ordered x/y ranks and `S_p`, enforces the exact quotient-implied `Dcal`, and
prunes when either internal word can no longer finish with total weight 809.
No relaxed middle automaton is used.

## Exact finite counts

| k | budget-feasible | capacity survivors | phase-compatible pairs | `(prefix,N_phase)` classes | maximum death depth |
|---:|---:|---:|---:|---:|---:|
| 39 | 47 | 46 | 7 | 3 | 15 |
| 37 | 784 | 724 | 121 | 17 | 880 |
| 35 | 7,458 | 6,634 | 1,269 | 35 | 884 |
| 33 | 43,695 | 41,814 | 7,934 | 37 | 888 |
| 31 | 198,420 | 194,960 | 36,457 | 37 | 892 |

Every listed phase class dies exactly.  Thus all five live terminal exponents
have zero genuine full-phase survivors.

The long-lived classes and their exact death depths are hard-coded and checked
by `verification/verify_rl261_full_phase.py`; all omitted classes die by depth
27 or earlier (and all three `k=39` classes die by depth 15).

## Consequence and limits

The third selector `(1287,812,475,485,306,16,6)` is eliminated completely.
This is stronger than proving the individual Gate-A inequalities for these
terminal exponents.

Gate A remains open uniformly beyond this selector.  Gate B remains open.
Radius 4 was not invoked.  Radius 5 remains inactive.

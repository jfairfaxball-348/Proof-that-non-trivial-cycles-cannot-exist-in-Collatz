# RL59 new terminal-potential and terminal-tail lemmas

Date: 2026-08-23

This file records the new RL59 mathematics separately from exploratory computation.

## 1. Normalized terminal potential

Let

`g = 2^i / 3^p`.

For a positive state after the inherited 26-zero cut that is genuinely embeddable into the fixed safe-CF terminal endpoint, the normalized backward `P` grammar gives

`J <= zeta * 3^(p-d+4) / 2^(i+1)`.

Equivalently,

`J*g <= zeta * 3^(4-d) / 2`.

At height one this is

`J*g <= (27/2) zeta`,

and at height two

`J*g <= (9/2) zeta`.

The proof uses `P=2^r J`, where `r` counts late x-zeros. In the backward grammar the homogeneous multipliers are

- `11`: `2/3`;
- `10`: `2`;
- `00`: `1`;
- `01`: `1/3`;

and every affine correction except `10` is nonpositive, while `10` has zero affine correction. The remaining homogeneous exponent is fixed by the terminal exponent counts and the inherited relation `K+R=q-24` / equivalent ledger notation.

The next session should independently reconstruct this general derivation line-by-line; the bundled regression script directly checks its Type-B consequence.

## 2. Exact maximal pump exits

For a maximal synchronized pump block

`J=3 --11--> 5 --00--> 3`

repeated `m` times, write the final pump scalar as `G`.

The aligned pump mass is

`A_m = 2(G-g0)`.

There are two relevant exits.

### Type A

Exit word: `00,01`.

Endpoint:

`(d,J,Q)=(2,6,9)`.

The exit scalar is `4G`. The second exit zero has weight `2G<17/30`, hence

`G<17/60`

and therefore

`A_m < 2G < 17/30 < 5/4`.

So Type A can never terminate a threatening pump block.

### Type B

Exit word: `11,11,01`.

Endpoint:

`(d,J,Q)=(2,15,18)`.

The exit scalar is

`g_exit=(8/9)G`.

The normalized terminal potential gives

`15*(8/9)G <= (9/2)zeta`,

hence

`G <= (27/80)zeta`.

Thus

`A_m < 2G <= (27/40)zeta < 17/25 < 5/4`,

using the inherited safe phase upper bound.

Therefore the exact RL58 pump cannot supply the required late aligned mass in any genuine safe-CF terminal suffix, irrespective of its repetition count.

The bundled Type-B verifier also checks the concrete four-pump exit in normalized `P` form:

`P_exit=480`, while terminal compatibility gives `P_exit<145.37...`.

## 3. Prefix-side obstruction is genuinely gone

A defect-compatible exact prefix reaches the unique four-pump entry target

`(i,p,d,J)=(73,47,1,3)`

with 26 x-zeros and exact matched defect

`22521943623158297371116 / 26588814358957503287787`

`=0.8470458035... < 5/3`.

Appending four pumps produces aligned mass

`1.5348775613... > 5/4`.

Thus local cap / prefix / defect conditions do not kill the pump. Its failure is genuinely terminal.

## 4. Aggregate synchronized-mass telescope

At height one,

`Psi = g(J+1)/2`.

For synchronized edges,

- `00`: `Delta Psi = g`;
- `11`: `Delta Psi = 0`.

Therefore aligned mass telescopes exactly through arbitrary height-one synchronized motion.

Any nonterminal positive synchronized block that later exits height one through `01` is bounded by the terminal potential at the exit interface. This removes the need to analyze separate pump patterns one-by-one.

The only possible reservoir for very large late aligned mass is therefore the final positive height-one synchronized tail after the last `10` return and before the terminal endpoint.

## 5. Final synchronized-tail forcing

Let `(J0,g0)` be the height-one state immediately after the last `10` return.

The preceding height-two terminal potential gives

`J0*g0 <= (3/2)zeta`.

Because the final tail is nontrivial and must reach odd terminal `K>=25`, `J0=1` cannot work; hence `J0>=3`. Therefore

`g0 <= zeta/2`

and

`Psi0 = g0(J0+1)/2 <= zeta`.

At the terminal endpoint,

`Psi_end = (27/4) zeta (1+2^-K)`.

Hence the final aligned `00` mass is

`M_final = Psi_end-Psi0 > 23/4`.

This strengthens the earlier RL59 bound `M_final>45/8`.

The earlier exact regression also proves, without using `J0>=3`,

- `M_final>45/8`;
- final synchronized `11` mass `>17/3`;
- at least 10 `00` events;
- at least 16 `11` events;
- at least five maximal `00` runs.

The `23/4` strengthening is used in the terminal-ancestor bootstrap below.

## 6. Shortcut-Collatz conjugacy of the final tail

At height one define

`n=(J-1)/2`.

The synchronized deterministic evolution is exactly

- if `n` is even: `n -> n/2`;
- if `n` is odd: `n -> (3n+1)/2`.

An admissible terminal exit to `J_end=2^K` can occur only at

`n=2^K-1`

or

`n=(2^K-2)/3`,

with odd `K>=25`.

This is the precise Collatz-conjugate subsystem at the current proof frontier.

## 7. Exact finite K>=25 ancestor boundary

A deterministic exact C++ search checks every positive starting `n` and follows the shortcut orbit until it reaches a previously certified no-hit trajectory, a repeated state, or an admissible terminal predecessor.

It finds:

- every `n<=11,184,809` avoids all admissible odd `K>=25` terminal predecessors;
- `n=11,184,810=(2^25-2)/3` is the first hit, with `K=25`.

Therefore every state belonging to a genuine final terminal tail satisfies

`n>=11,184,810`,

hence

`J>=22,369,621`.

At height one the terminal potential and `zeta<136/135` give

`g < 68/(5J)`.

Thus every aligned zero in the final tail has weight strictly less than

`68 / (5*22,369,621)`

`=68/111,848,105`

`≈6.07967e-7`.

Since `M_final>23/4`, the number `A` of aligned zeros in the final tail obeys

`A > 115*22,369,621/272`,

so

`A>=9,457,745`.

The whole word has only `z-1` internal x-zeros, so

`z>=9,457,746`.

The inherited survivor has odd `z`, yielding

`z>=9,457,747`.

This is the strongest currently promoted RL59 survivor reduction, subject to independent audit of the finite shortcut search implementation.

## 8. Higher-K exact finite boundaries

The same exact search was reproduced at two stronger terminal thresholds:

### K>=27

First starting state:

`n_min=13,256,071`.

It reaches the `K=27` terminal predecessor

`n=44,739,242=(2^27-2)/3`.

Thus

`J_min=26,512,143`,

and the same `23/4` mass / terminal-potential calculation forces

`A>=11,209,179`.

**Correction:** earlier session prose accidentally wrote `11,209,546`; `11,209,179` is the correct arithmetic.

### K>=29

First starting state:

`n_min=125,687,199`.

It reaches

`n=536,870,911=2^29-1`.

Thus

`J_min=251,374,399`,

forcing

`A>=106,279,618`.

These two boundaries reproduce exactly in the bundled verifier runner, but should remain classified as exact finite computation pending independent implementation audit.

## 9. Current method frontier

The new bootstrap has the form

`K >= K0`

`=> n >= n_min(K0)`

`=> J >= 2*n_min(K0)+1`

`=> every final zero is tiny`

`=> z is large`.

Meanwhile the inherited exact exponent relation couples the variables in the opposite direction:

`K+z=q+3`.

The next target is to turn this into a genuine contradiction or a finite terminal remainder, without assuming a global Collatz fact about the shortcut subsystem.

Do not claim closure merely from large lower bounds on `z`.

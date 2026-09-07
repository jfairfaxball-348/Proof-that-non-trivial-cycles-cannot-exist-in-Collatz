# RL278 — global six-zero Gate-A contraction and exact finite-reduction engine

Date: 2026-09-07

## Classification

Primary:

`GLOBAL_SIX_ZERO_GATE_A_CONTRACTION_PROVED`

Subordinate:

`FIXED_ZERO_EXACT_FINITE_REDUCTION_ENGINE_IDENTIFIED`

Gate A remains open uniformly. Gate B is unchanged/open and remains frozen in this session. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming exact state

RL278 starts from the promoted RL277 zero-rank identity. Let

`rho = 2/3`

and let the internal zero ranks of the canonical `x` word be

`0 <= u_1 <= ... <= u_m0`.

RL277 proves that every retained full-phase terminal object satisfies the necessary envelope inequality

`S_m0 := sum_(t=1)^m0 2^(t-1) rho^(u_t) > 17/2`.          (1.1)

RL277 also proves that `m0=4` and `m0=5` are Gate-A safe, hence any hypothetical Gate-A violator obeys

`m0 >= 6`, equivalently `z >= k+4`,

where

`m0 = z-k+2`.

The RL278 mission is to close `m0=6` without an arbitrary rank cutoff and to isolate a reusable finite-reduction mechanism.

## 2. Exact gap immediately below the five-zero threshold

For a fixed number `n` of zeros, define

`S_n(u_1,...,u_n) = sum_(t=1)^n 2^(t-1) rho^(u_t)`

for nondecreasing nonnegative integer ranks.

Every such `S_n` has, in lowest terms, odd denominator: after clearing powers of `3`, no factor `2` remains in the denominator. Therefore

`S_n != 17/2`                                                     (2.1)

for every finite rank tuple.

For exact finite search below the threshold, use the following monotone upper-envelope rule. Suppose a prefix through rank `j-1` has partial sum `P`, and the next rank is chosen as `u`. Since all later ranks are at least `u`, the largest completion at that choice is

`P + (2^n-2^(j-1)) rho^u`.                                      (2.2)

This decreases strictly with `u`. Hence, once this upper envelope is no larger than the best already-certified sub-threshold value, all larger `u` are rigorously pruned. This is a finite branch-and-bound proof, not an imposed enumeration cutoff.

Applying the exact envelope search at `n=5` gives

`M_5 := max{S_5 : S_5 < 17/2}`

with

`boxed: M_5 = 501898/59049`,                                    (2.3)

attained at the unique verifier witness

`(u_1,...,u_5) = (1,1,1,2,10)`.

Thus the exact five-zero gap is

`gamma_5 = 17/2 - M_5 = 37/118098`.                             (2.4)

The verifier independently reproduces the older regression value

`M_4 = 25/3`

at witness `(0,0,2,2)`.

Classification: **exact analytic/combinatorial finite certificate**.

## 3. Exact sixth-rank bound

Assume now `m0=6`, so

`S_6 = S_5 + 32 rho^(u_6) > 17/2`.                              (3.1)

Split according to the first five zeros.

### Case A: `S_5 < 17/2`

By (2.4),

`32 rho^(u_6) > gamma_5 = 37/118098`.

Exact comparison gives

`32 rho^28 > 37/118098`,

while

`32 rho^29 < 37/118098`.

Therefore

`boxed: u_6 <= 28`.                                             (3.2)

No arbitrary outer rank bound is used.

### Case B: `S_5 > 17/2`

RL277 already gives the exact five-zero threshold-crossing canonical family:

- 206 relaxed monotone tuples;
- 72 legal canonical prefixes;
- maximum fifth zero-rank `u_5=7`.

Replay the deterministic all-`1` continuation from each of those 72 legal prefixes. Before terminal closure or canonical stop, the maximum possible run contains exactly 11 further one-columns. Therefore a sixth zero, if it is to occur at all, must interrupt that continuation within those 11 columns, giving

`u_6 <= 7+11 = 18`.                                             (3.3)

Combining the two cases yields the global exact six-zero rank reduction

`boxed: u_6 <= 28`.                                             (3.4)

Classification: **analytic finite reduction plus exact canonical closure certificate**.

## 4. Exhaustive six-zero canonical replay

Enumerate exactly the nondecreasing tuples

`0 <= u_1 <= ... <= u_6 <= 28`

satisfying

`S_6 > 17/2`.

There are exactly

`7081`

relaxed tuples.

Deterministic canonical replay leaves exactly

`458`

legal prefixes through the sixth zero. Among those legal prefixes, the actual maximum sixth rank is only

`u_6=14`,

but the promoted proof uses the independently derived rigorous bound `u_6<=28`.

Because `m0=6`, after the sixth zero the `x` word contains only ones. Exact all-one closure gives:

- `170` terminal canonical paths;
- `47` terminals satisfying the inherited full-phase scale box;
- `0` phase-box terminals with `H_can<k`.

The phase-box terminal `(k,H_can)` pairs are exactly

`(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(3,10),(3,11),`

`(5,18),(5,19),(5,20),(5,21),(5,22),(5,23),(5,25),(5,26),(5,31)`.

Every such pair is Gate-A safe.

Therefore a hypothetical Gate-A violator cannot have six internal zeros.

Classification: **exact finite canonical certificate**.

## 5. Promoted dangerous-zero contraction

RL277 excludes `m0=4,5` for Gate-A violators. Section 4 excludes `m0=6`. Hence

`boxed: H_can < k  =>  m0 >= 7`.                               (5.1)

Using `m0=z-k+2`,

`boxed: H_can < k  =>  z >= k+5`.                              (5.2)

This strictly strengthens the promoted RL277 global conclusion `z>=k+4`.

Scope remains global full-phase/Gate-A scope. No Branch-C-only counterflow theorem is imported.

## 6. Reusable fixed-zero finite-reduction mechanism

The six-zero proof exposes a level-by-level exact mechanism that is reusable at any fixed zero budget.

For fixed `n`, let

`M_n = max{S_n : S_n < 17/2}`

when computed by the monotone upper-envelope recursion (2.2), and let

`gamma_n = 17/2-M_n > 0`.

To pass from `n` zeros to `n+1` zeros under the necessary threshold `S_(n+1)>17/2`, split:

1. **Below-threshold prefix:** if `S_n<17/2`, then the last term must bridge `gamma_n`, so
   `2^n rho^(u_(n+1)) > gamma_n`, which gives an explicit finite rank bound.
2. **Already-crossed prefix:** if `S_n>17/2`, the first `n` zeros lie in the exact finite canonical threshold-crossing family already certified at level `n`. Exact deterministic all-one closure of that finite family gives a finite interruption bound unless a genuine all-one canonical cycle is encountered; the verifier checks this obstruction explicitly.
3. Taking the larger of the two bounds gives an exact finite search region for level `n+1`.

At the `5 -> 6` step, this gives the bounds `28` and `18`, respectively, and closes the six-zero family exactly.

This is the promoted sense of

`FIXED_ZERO_EXACT_FINITE_REDUCTION_ENGINE_IDENTIFIED`.

It is not yet a uniform asymptotic Gate-A theorem. The gap `gamma_n` can shrink rapidly, and the size of the exact canonical family can grow. Therefore merely iterating fixed `n` forever is not promoted as a proof strategy for Gate A.

## 7. Exact remaining obstruction

The new contraction moves the dangerous region outward by one zero but does not itself force

`H_can >= k`

for arbitrary `m0`.

The scalable target is now clear: compress the level-by-level finite families into a run/state automaton or prove a direct growth law coupling zero budget to canonical height, for example a lower bound on `H_can` that grows sufficiently with the number and placement of zero-rank interruptions.

A successor should consume the exact state transition structure exposed here rather than merely repeat one more uncompressed enumeration.

## 8. Verification

Portable verifier:

`sessions/RL278/verification/verify_rl278_six_zero.py`

checks:

- exact branch-and-bound maxima `M_4` and `M_5` with no arbitrary rank cutoff;
- the exact gap `gamma_5=37/118098`;
- the six-zero rank bound `u_6<=28`;
- RL277 five-zero family regression and its 11-column maximum all-one run;
- 7,081 six-zero relaxed tuples;
- 458 legal six-zero canonical prefixes;
- 170 terminal closures;
- 47 full-phase scale-box terminals;
- zero Gate-A violators.

The verifier passes from the promoted repository recurrence only.

# RL21 — integer state-gap synchronization and first-divergence blow-up

Date: 2026-08-20

## Status

**ANALYTIC.**  The bundled verifier is a finite sanity check only.

This note isolates a genuinely integer/ownership phenomenon that every rational fixed-orbit countermodel can evade: two integer Collatz trajectories whose starting states differ by a highly 2-divisible gap must have identical parity itineraries until that 2-adic divisibility is exhausted.

For the `g=2` balanced-return branch this recovers the earlier `v2(Q(u)-Q(v))` statement dynamically and adds a quantitative consequence: the first parity disagreement necessarily produces a phase separation of order the least state.

## 1. Exact parity synchronization from the integer gap

Use the full-parity shortcut map

`T(n)=n/2` for even `n`,

`T(n)=(3n+1)/2` for odd `n`.

Let `a<b` be positive integers and put

`r=v2(b-a)`.

As long as two current states have the same parity, their difference transforms as

- `Delta -> Delta/2` on an even/even step;
- `Delta -> 3 Delta/2` on an odd/odd step.

In either case the 2-adic valuation drops by exactly one.

Therefore:

> **The first `r` parity bits of the two trajectories agree, and the parity bits at position `r` differ.**  (R21I.1)

Equivalently, after the common `r`-step prefix the state difference is a positive odd integer.

This is the dynamical form of the fixed-weight `Q` lemma used earlier in the half-balanced case.  It does not require equal word weights; it is a direct consequence of integer parity ownership.

## 2. Application to a `g=2` balanced return

Let `R` be the least state and let

`x=R+G`, `G>0`,

be the balanced half-cycle state.  Suppose the two half blocks have equal length `a` and equal odd count `ell`, so

`T^a(R)=x`,

`T^a(x)=R`.

The two half-words cannot agree in all `a` positions: on one common affine branch their difference after `a` steps would remain positive, whereas the endpoints are swapped and have difference `-G`.

Hence

`r=v2(G)<a`,                                                (R21I.2)

and the two half-word parity strings agree exactly through positions `0,...,r-1` and first disagree at `r`.

In the near-minimum branch already proved in RL21,

`4 | G`,

so `r>=2`.

This is a purely integer-cycle statement.  Rational words with a formal integer-looking `Q` difference do not acquire it unless their displayed states are actual integers with the declared parities.

## 3. First-divergence blow-up

Let

`y=T^r(R)`,

`z=T^r(x)=y+delta`,

where `delta` is positive and odd.  The two states have opposite parity.

Assume, as in an actual least-state cycle, that the current states and their next states are all at least `R`.

### Orientation `0/1`

If `y` is even and `z` odd, then

`T(z)-T(y) = y + (3 delta+1)/2 > R`.                        (R21I.3)

### Orientation `1/0`

If `y` is odd and `z` even, then

`T(z)-T(y) = (delta-2y-1)/2`.                              (R21I.4)

For any positive `delta`,

`max(delta, |delta-2y-1|/2) >= (2y+1)/3`.                 (R21I.5)

Combining the two orientations gives the uniform minimax statement

> **within the divergence step, either the pre-step or post-step pair has separation at least**
>
> `(2R+1)/3`.                                               (R21I.6)

Since both phase states in that pair are at least `R`, at least one of them is at least

`R+(2R+1)/3 = (5R+1)/3`.                                  (R21I.7)

Thus a pair of low integer states separated by the balanced gap cannot remain mutually close once their parity itineraries first diverge: a separation of order `R` is forced immediately.

## 4. Two high-separation episodes in the half-balanced cycle

The same argument can be started again at the half-cycle cut, where the pair is `(x,R)` and the next `a` steps use the opposite pair of half-words.  Therefore a primitive `g=2` balanced cycle has a corresponding first-divergence blow-up in each half.

At minimum this yields two distinct phase locations at which the paired half-cycle trajectories are separated by at least `(2R+1)/3`; consequently the cycle contains high phases at least `(5R+1)/3` in both halves.

This is not yet a contradiction.  Two high phases are too sparse by themselves to beat the existing global population bound.  The value of the lemma is that it is a **genuinely integrality-sensitive replacement** for the failed rational strip-width intuition.

## 5. Strategic use

The next viable question is not whether a single divergence is large; it is whether a large adjacent-transport/prefix-flow path forces **many** such integer divergence/re-synchronization episodes.  If the number of forced high episodes can be bounded below by the transport area or by the number of sign changes in the prefix-flow path, then RL19/RL20 state packing could become quantitatively relevant.

A theorem of that form would survive the RL21 rational countermodels precisely because those models do not own the formal parity words as integer state trajectories.

Verifier: `verify_rl21_integer_gap_synchronization.py`.

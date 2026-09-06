# RL268 — Radius-5 determinant-one `[2,1,1,1]` closure

Date: 2026-09-06  
Classification: **RADIUS5_KAPPA1_2111_CLOSED**

Incoming authoritative head: `785c9eaf1db327937783cb4358fb5d263cb48110` (RL267).

## 1. Scope

RL268 remains entirely inside the inherited Radius-5 determinant-one sector `|kappa|=1` and closes only the flat topology `[2,1,1,1]`.

Frozen and untouched:
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration;
- the general Radius-n programme;
- `|kappa|=3` and `|kappa|=5`.

Inherited without change from RL265–RL267:
- `D=2^A-3^L`, positive domain `D>1`;
- exact parity-word numerator and rotation/root-crossing identities;
- exact cyclic earth-mover flow `g`;
- in determinant one, after orienting to `kappa=+1`, `qA-mL=1`;
- `gcd(A,L)=gcd(m,A)=1`;
- exact zero-flow-cut edge identity;
- exact determinant-window identity `W_i(m)=q-g_{i-1}`;
- full-`D` divisibility of every rotation numerator and hence of the exact numerator difference;
- audited RL238 Laurent–Mignotte–Nesterenko dependency, subject to exact hypothesis matching.

Closed before RL268: `[3,2]`, `[3,1,1]`, `[2,2,1]`.

## 2. Complete cyclic order classification

For `kappa=+1` there are three positive unit edges and two negative unit edges. A `[2,1,1,1]` flow has four nonzero components: one component of length two and three singleton components.

After anchoring the length-two component, exactly four cyclic sign orders remain:

1. `++ ... + ... - ... - ...`;
2. `++ ... - ... + ... - ...`;
3. `++ ... - ... - ... + ...`;
4. `-- ... + ... + ... + ...`.

Every ellipsis is a nonempty zero-flow gap. These are the four orders enumerated by the complete finite certificate. The `kappa=-1` orientation is obtained by interchanging source and target and is independently replayed in the small-range red team.

## 3. Four-component support cut

There are `A-5` zero-flow positions split among four nonempty gaps. The largest zero gap therefore has length at least

`ceil((A-5)/4)`.

Cut immediately after a largest zero gap and rotate source and target together. The five nonzero flow edges then lie in a linear support whose edge-index span is at most

`U4 = A-1-ceil((A-5)/4) = floor((3A+1)/4)`.

This is the correct four-component replacement for RL267's three-component support cut. RL267's `floor((2A+2)/3)` bound is not reused.

## 4. Determinant window and the mixed edge bound

Define the shorter determinant window by

`h=min(m,A-m)`

and its base one-count

`r = q` if `m<=A-m`,
`r = L-q` if `m>A-m`.

The promoted determinant-window identity gives exact counts `r+epsilon` on the shorter cyclic window, with the endpoint correction `epsilon` determined by the adjacent flat flow value and therefore in `{-1,0,1}`.

Positive domain gives `L/A < log(2)/log(3) < 2/3`. Combining this with `qA-mL=1` yields the uniform integer bound

`0 <= r <= floor(A/3)`.

Apply the zero-flow cut above to the exact five-edge identity. Order the five edge monomials by physical index, remove their common powers of `2` and `3` (legal because `gcd(D,6)=1`), and compare each edge to its predecessor. The 2-exponent variation is controlled by the support span `U4`; the 3-exponent variation is the corresponding shorter-window one-count, with only the fixed endpoint/sign corrections from the five flat edges. Edge-by-edge application of `W_i(m)=q-g_{i-1}` over the four sign orders gives the conservative normalized estimate

`0 < |E| <= 5 * 3^(7+r) * 2^(U4-r)`.

Equivalently,

`0 < |E| <= C * 2^U4 * (3/2)^r`,
`C=5*3^7`.

The full theorem hypothesis remains

`D | E`,

with the entire positive `D`, never a proper factor.

The portable finite verifier independently reconstructs the binary word from the flow recurrence before evaluating the five edge terms. The independent brute-force red team reconstructs `Q(tau^m x)-Q(x)` directly and confirms the exact edge identity after a valid zero-flow cut.

## 5. Infinite reduction: non-bracketing case

Let

`alpha=log(3)/log(2)`,
`Lambda=A log(2)-L log(3)>0`.

As in RL266/RL267, determinant one gives

`A/L - m/q = 1/(qL)`.

If `m/q>alpha`, then

`Lambda > log(2)/q > log(2)/A`.

Using `1-exp(-Lambda)>Lambda/2` for `0<Lambda<=1` (and the weaker constant bound for `Lambda>=1`) gives

`D > (log(2)/(2A))*2^A > 2^A/(3A)`.

With `r<=floor(A/3)`, define

`B0(A)=5*3^7*2^(U4-floor(A/3))*3^floor(A/3)`.

Exact integer comparison shows

`2^A > 3 A B0(A)`

for every `A=430,...,441`. Under `A -> A+12`, `U4` rises by 9 and `floor(A/3)` rises by 4, so `B0` is multiplied by `2^5*3^4=2592`, while the lower-bound ratio gains

`4096*A/(2592*(A+12)) = 128A/(81(A+12)) > 1`

for `A>=21`.

Therefore every non-bracketing candidate satisfies

`A <= 429`.

## 6. Infinite reduction: bracketing case and LMN

The only remaining infinite case is

`m/q < alpha < A/L`,
`qA-mL=1`.

Normalize the mixed edge bound by `2^A`. For sufficiently large `A`, its right side is `<1/2`, hence

`Lambda <= 2 * 5*3^7 * 2^(U4-r-A) * 3^r`.

The inherited audited RL238 LMN specialization applies with exactly the same bases `2,3` and coefficients `A,L`. Determinant one gives `gcd(A,L)=1`, so the RL238/RL239 reduced-denominator/multiple correction introduces no multiplicity here.

In the inherited `M=21` regime the necessary inequality is

`log(2C) + (U4-A)log(2) + r log(3/2)
 + 22*21^2 log(2)log(3) >= 0`,

with `C=5*3^7` and `r<=floor(A/3)`.

A rational upper certificate uses

- `log(2C) < 10`;
- `log(2) > 0.693` in the negative term;
- `log(3/2) < 0.406`;
- `log(2) < 0.694`, `log(3) < 1.099` in the positive LMN term.

The resulting rational upper bound is already negative for all twelve residues `A=195422,...,195433`, and drops by exactly `455/1000` under `A -> A+12`. Hence no `M=21` bracketing survivor has `A>195421`.

The `M=21` regime extends beyond `5.27e8` under the same safe `L<A` estimate used in RL266/RL267. Beyond that transition, replacing `M` by the standard logarithmic upper bound makes the necessary expression strongly negative at the transition; its derivative remains negative because the linear decay term is bounded away from zero while the LMN correction grows only like `log(A)^2`. Thus there is no large-`A` re-entry.

Every bracketing survivor therefore satisfies

`A <= 195421`.

## 7. Exact determinant-pair / Stern-Brocot cover

The analytic verifier performs two exact covers.

First, it enumerates every determinant-one positive-domain pair through `A<=429`. There are exactly

`34,931`

such pairs. Applying the exact mixed size test

`D <= 5*3^(7+r)*2^(U4-r)`

leaves exactly

`967`

pairs, with maximum `A=174`.

Second, it traverses the determinant-one Stern-Brocot bracket around `alpha` using only exact integer comparisons `2^n ? 3^d`. Up to the LMN cutoff `A<=195421` there are exactly 35 upper-neighbour rows. The size test leaves only six:

`(A,L;m,q) =`
`(5,3;3,2),`
`(8,5;3,2),`
`(27,17;19,12),`
`(46,29;19,12),`
`(65,41;19,12),`
`(149,94;84,53)`.

All six are already contained in the complete `A<=429` determinant-pair cover. Thus the 967-row file `verification/rl268_2111_pairs.csv` is a complete finite size cover.

## 8. Gap-free structural finite certificate

For each of the 967 determinant pairs and each of the four cyclic sign orders, the verifier enumerates every positive composition of the `A-5` zero positions into the four required nonempty gaps.

For each gap configuration it solves the exact recurrence

`x_i-x_(i+m)=g_i-g_(i-1)`

around the unique `m`-cycle (`gcd(m,A)=1`). A configuration is structural only when the reconstructed levels can be shifted into `{0,1}` and have exactly `L` ones.

Counts:

- determinant pairs: **967**;
- four-order gap configurations: **179,403,060**;
- structural candidates: **9,510,691**;
- maximum structural `A`: **174**;
- full-`D` hits: **0**.

By cyclic order:

| order | gap configurations | structural candidates | full-`D` hits |
|---|---:|---:|---:|
| `++,+,-,-` | 44,850,765 | 2,405,606 | 0 |
| `++,-,+,-` | 44,850,765 | 2,410,327 | 0 |
| `++,-,-,+` | 44,850,765 | 2,405,606 | 0 |
| `--,+,+,+` | 44,850,765 | 2,289,152 | 0 |

Primitivity is deliberately not used as a filter. The finite certificate is therefore stronger than the written primitive theorem scope.

Every divisibility test is against the whole positive integer `D=2^A-3^L`.

## 9. Independent red team through `A<=18`

A separate implementation brute-forces all positive-domain words and all nontrivial rotations through `A<=18`, reconstructs the cyclic earth-mover median flow directly, selects exact distance 5, `|kappa|=1`, topology `[2,1,1,1]`, and evaluates `Q(tau^m x)-Q(x)` directly.

It obtains:

- raw `[2,1,1,1]`, `|kappa|=1` instances: **21,596**;
- `kappa=+1`: **10,798**;
- `kappa=-1`: **10,798**;
- full-`D` numerator-difference hits: **0**;
- direct `Q(x)` full-`D` hits: **0**;
- proper-factor-only numerator-difference instances: **1,608**;
- determinant mismatches: **0**;
- exact edge-identity mismatches after a legal zero-flow cut: **0**.

The permanent negative-domain sentinel is reproduced exactly:

`A=11, L=7, D=-139, Q=18904`.

It remains outside the positive-domain theorem scope.

## 10. Promoted result

Promoted local leaf:

> In the inherited positive-domain, primitive/full-`D` Radius-5 setting, no exact-distance-5 self-rotation with `|kappa|=1` and flat transport topology `[2,1,1,1]` exists.

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

Together with RL266/RL267, the only determinant-one topology still open is `[1,1,1,1,1]`.

This does **not** prove Radius 5. After determinant one is complete, the `|kappa|=3` and `|kappa|=5` sectors remain to be treated unless separately eliminated by a later theorem.

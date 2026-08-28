# RL146 — Contact-carry order closure

Date: 2026-08-28

## Status

**Proved analytic mathematics, conditional only on the frozen inherited RL145 height-one owner framework.**

RL146 closes the primitive height-one ownership branch for every multiplicity `g>1`.
It does **not** address `g=1`, mixed-height owners, negative-defect configurations, Gate A/B globally, all non-trivial Collatz cycles, or the Collatz conjecture.

## 1. Frozen inherited setting

Use the RL145 constants

- `A = 217,976,794,617`,
- `L = 137,528,045,312`,
- `X = 2^A`,
- `Y = 3^L`,
- `b_r = floor(A r/L)` for `0 <= r <= L`,
- `W_r = 2^{b_r} 3^{L-1-r}` for `0 <= r < L`.

The height-one owner has a binary height word `h_j in {0,1}`.  Write block `t` as
`h_{t,r}=h_{tL+r}`, and let its contact set be

`C_t = {r : h_{t,r}=0}`,

with contact weight

`c_t = sum_{r in C_t} W_r`.

RL145 proved that, for an ordinary-owned cyclic height-one object of multiplicity `g>1`, there are integer carries `d_t` (cyclically indexed modulo `g`) satisfying

`c_{t+1}-c_t = Y d_t - X d_{t+1}`,

and

`sum_t d_t = 0`.

RL145 also proved that distinct contact subsets have distinct contact weights.  Hence `c_t=c_s` implies `C_t=C_s`.

The RL145 local CRT/population coefficient route is intentionally not used below.

## 2. Residue-by-residue carry ladder

Define

`epsilon_{t,r} = 1_{r in C_{t+1}} - 1_{r in C_t}`.

Because contact is the complement of the binary height digit,

`epsilon_{t,r} = h_{t,r} - h_{t+1,r}`

and therefore `epsilon_{t,r} in {-1,0,1}`.

The RL145 carry equation becomes

`sum_{r=0}^{L-1} epsilon_{t,r} 2^{b_r} 3^{L-1-r} = Y d_t - X d_{t+1}`.      (2.1)

For a fixed interface `t -> t+1`, define an integer ladder

`z_{t,0}=d_t`,

`z_{t,r+1}=3 z_{t,r} - epsilon_{t,r} 2^{b_r}`.                         (2.2)

Unrolling (2.2) and using (2.1) gives

`z_{t,L}=X d_{t+1}=2^A d_{t+1}`.                                      (2.3)

### Lemma 2.1 — backward 2-adic divisibility

For every `0 <= r <= L`,

`2^{b_r} | z_{t,r}`.

**Proof.** At `r=L`, this is (2.3), because `b_L=A`.  Suppose
`2^{b_{r+1}} | z_{t,r+1}`.  Since `b_{r+1} >= b_r`, both
`z_{t,r+1}` and `epsilon_{t,r}2^{b_r}` are divisible by `2^{b_r}`.
Equation (2.2) therefore gives `2^{b_r} | 3 z_{t,r}`.  Since `3` is odd,
`2^{b_r} | z_{t,r}`.  Descend to `r=0`.  QED.

Define the normalized integer state

`y_{t,r}=z_{t,r}/2^{b_r}`.

Then

`y_{t,0}=d_t`, `y_{t,L}=d_{t+1}`.                                     (2.4)

Let

`a_r=b_{r+1}-b_r`.

Because `1 < A/L < 2`, one has `a_r in {1,2}`.  Dividing (2.2) by
`2^{b_r}` and substituting `epsilon_{t,r}=h_{t,r}-h_{t+1,r}` gives the exact local ladder law

`3 y_{t,r} + h_{t+1,r} = 2^{a_r} y_{t,r+1} + h_{t,r}`.                 (2.5)

## 3. Strict order is preserved at every residue

### Lemma 3.1 — one-step strict-order preservation

For any two interfaces `t,s` and any residue `r`,

`y_{t,r} > y_{s,r}` implies `y_{t,r+1} > y_{s,r+1}`.

**Proof.** Subtract (2.5) for `s` from (2.5) for `t`:

`3 Delta y_r + Delta h_{next,r} = 2^{a_r} Delta y_{r+1} + Delta h_{current,r}`.   (3.1)

If `Delta y_r >= 1`, the left side is at least `3-1=2`, because each height digit is binary.  If instead `Delta y_{r+1} <= 0`, the right side is at most `0+1=1`.  This is impossible.  QED.

Iterating Lemma 3.1 through all `L` residues and using (2.4) yields

`d_t > d_s  =>  d_{t+1} > d_{s+1}`.                                  (3.2)

Thus cyclic shift by one block strictly preserves every strict comparison among the carry values.

## 4. A finite cyclic carry vector cannot be nonconstant

### Lemma 4.1 — cyclic order lock

All carries are equal.

**Proof.** Suppose two carries differ.  Choose indices `i,j` with
`d_i>d_j`, and put `q=j-i (mod g)`, so `q` is nonzero modulo `g`.
Applying (3.2) repeatedly `q` times gives

`d_i > d_{i+q}` implies `d_{i+q} > d_{i+2q}`,

and so on.  The orbit of adding `q` modulo `g` has finite length
`m=g/gcd(g,q)`.  Hence

`d_i > d_{i+q} > ... > d_{i+mq}=d_i`,

an impossibility.  Therefore no two carries differ.  QED.

The inherited identity `sum_t d_t=0` now forces

`d_t=0` for every `t`.                                                  (4.1)

Substituting into the RL145 carry equation gives

`c_{t+1}=c_t` for every `t`.                                            (4.2)

By RL145 subset-weight injectivity,

`C_{t+1}=C_t` for every `t`.                                            (4.3)

Therefore every reduced height-one block is identical.  In the inherited height-word parametrization this repeats the exponent block with period `L`; for `g>1` that is imprimitive, contradicting the primitive-owner hypothesis.

## 5. Main theorem

### Theorem RL146.1 — primitive height-one owner exclusion for `g>1`

Under the frozen RL145 ordinary-owned height-one framework, **no primitive height-one owner exists for any multiplicity `g>1`**.

The proof is analytic.  The decisive mechanism is not density or CRT population.  It is an order-preserving integer carry ladder whose end state is the next cyclic carry.

## 6. Why this is stronger than the requested RL146 coefficient gain

RL146 was opened to seek a global packing/density contradiction from the cyclic contact-carry system, with a mixed-height pivot if that failed.  The ladder argument instead eliminates the entire primitive height-one `g>1` branch before any coefficient estimate is needed.

Consequently:

1. the RL145 `162/13` saturation barrier remains a genuine barrier for the local counting method;
2. it is no longer an obstruction to closing the height-one branch, because RL146 uses a different invariant;
3. endpoint first/last-contact locks from RL145 remain true but are not needed for the closure;
4. the next live question is whether the carry-order mechanism can be lifted beyond binary height one.

## 7. Exact scope boundary and next obstruction

The binary condition is used critically in Lemma 3.1: the two height-digit differences contribute at worst `-1` on the left and `+1` on the right, while the carry gap is multiplied by `3`.  For general mixed heights, those digit differences need not be bounded by one, so the same comparison proof does not automatically survive.

RL147 should therefore test, in this order:

1. a layer decomposition of nonnegative mixed heights into binary superlevel sets;
2. whether ownership/carry relations descend to compatible layerwise ladders;
3. whether a weighted or lexicographic order survives when layers interact;
4. if not, freeze the exact mixed-height obstruction and pivot to the genuine negative-defect branch rather than returning to saturated height-one population counting.

## 8. Red-team checklist

- No new divisibility is assumed: Lemma 2.1 is deduced backward from the exact RL145 end divisibility `2^A | z_{t,L}`.
- No CRT residue-class independence is assumed.
- No population coefficient is used.
- The order proof compares two interfaces at the same mechanical residue, so `a_r` is common.
- The cyclic contradiction uses only finite cyclic indexing.
- Contact-weight equality is promoted to contact-set equality only via the inherited RL145 subset-weight injectivity theorem.
- The primitive contradiction is asserted only for `g>1`.
- No statement here closes `g=1`, mixed heights, negative defect, all nontrivial cycles, or Collatz globally.

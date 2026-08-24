# RL49 — exact radius-3 theorem match audit and correction

Date: 2026-08-22

## Status

**ANALYTIC**, using the recovered RL10/RL19 theorem definitions together with the audited RL48 full-word reconstruction.

This note corrects the conditional interpretation in `RL48_RADIUS3_MATCH_COROLLARY.md`.  The RL48 `N <-> N+4` pair has a depth-three parity split, but the recovered RL10/RL19 term **radius 3** means *cyclic adjacent-transposition distance exactly 3 between a full parity word and one of its rotations*.  These notions are not equivalent.

The half-period rotation supplied by the RL48 four-swap construction has an exact even transport distance, in fact

`dist_cyc(uv,vu) = 2(a-t-3+H)`.

Consequently the direct invocation of the RL19 radius-3 closure is unavailable.

---

## 1. Recovered theorem scope

RL10 defines, for equal-weight binary words `d,d'`, the prefix flow

`G_i=P_i(d')-P_i(d)`.

For an exact cyclic adjacent-transposition radius-3 pair, after a cut at an unused edge,

`dist_transp(d,d') = sum |G_i| = 3`, 

and the flow has exactly three nonzero unit edges.  RL19 closes this exact radius-3 self-rotation regime for primitive `D`-divisible cycle words, subject to the inherited audited branch tree and its explicit older dependencies.

Thus the theorem input is not merely:

- two positive cycle states separated by 4; or
- agreement for two parity bits followed by a split on the third bit.

It is a global statement about the full parity word and a cyclic rotation of that word.

---

## 2. RL48 full-phase cycle and the relevant rotation

RL48 reconstructs

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`,

with both words of length `a` and weight `ell`.  Under the full phase condition there is a positive integer `N` with genuine Collatz trajectories

`N --u--> N+4`,

`N+4 --v--> N`.

Hence the full cycle word is

`d=uv`,

of length `A=2a`, weight `L=2ell`, and its rotation by `a` positions is

`tau^a d = vu`.

This is the rotation corresponding to the two distinguished states `N` and `N+4`.

---

## 3. Exact half-rotation transport formula

For `0<=i<=a` define the half-word prefix discrepancy

`h_i=P_i(v)-P_i(u)`.

Since `u,v` have equal weight,

`h_0=h_a=0`.

For the full words `d=uv` and `d'=vu`, their prefix flow satisfies

- `G_i=h_i` for `0<=i<=a`;
- `G_(a+j)=-h_j` for `0<=j<=a`.

For cyclic adjacent transport, every integer edge flow differs from this prefix flow by an additive circulation constant `c`, so

`dist_cyc(d,d') = min_(c in Z) sum_i |G_i+c|`.

The multiset of `G_i` is symmetric under `g -> -g` and contains zero.  Therefore `0` is a median and the minimum occurs at `c=0`.  Hence

`dist_cyc(uv,vu)=2 sum_(i=1)^(a-1) |h_i|`.                 (R49.1)

In the retained canonical positive one-excursion orientation, `h_i>=0` until the terminal return, so absolute values can be dropped.

---

## 4. Translation into the RL47 area variable H

After the common prefix `11`, the mandatory local split is `(0,1)`, so the half-word discrepancy becomes `1`.  Let the internal block have length

`m=a-t-4`.

RL47's local height starts at `d_0=1`, evolves along the `m` internal columns, remains positive, and ends at `d_m=1` immediately before the omitted terminal `(1,0)` column.  The terminal column returns the half-word prefix discrepancy to zero; the following `t` synchronized zeros keep it zero.

RL47 defines

`H=sum_(j=0)^(m-1) (d_j-1)`.

The sum of the nonzero half-word prefix discrepancies is

`d_0+d_1+...+d_m`

`= [sum_(j=0)^(m-1) d_j] + d_m`

`= (H+m)+1`.

Therefore

`sum_(i=1)^(a-1)|h_i| = H+m+1 = H+a-t-3`,

and (R49.1) becomes

`boxed: dist_cyc(uv,vu)=2(a-t-3+H)`.                       (R49.2)

This is an exact identity, not a bound.

In particular the distinguished half-period rotation always has **even** radius.  It can never be an exact radius-3 pair.

---

## 5. Audited examples

For the retained RL47 `(a,ell,t)=(65,41,2)` structural witness, the two-trajectory verifier gives `H=104`.  Thus

`dist_cyc(uv,vu)=2(65-2-3+104)=328`.

For the inherited RL45 `(65,41,t=0)` proper-factor countermodel, `H=3`, hence

`dist_cyc(uv,vu)=2(65-0-3+3)=130`.

These examples are not full-phase solutions, but they audit the metric translation on the exact inherited one-excursion geometry.

---

## 6. Primitivity of a hypothetical full-phase word in the one-excursion branch

The mismatch is not repaired by saying that `uv` might be a nonprimitive repetition whose primitive core has radius 3.

Assume `d=uv=w^k`, where `w` is primitive and `k>1`.  Since `u!=v` (their third bits are `0` and `1`), `k` cannot be even: if `k` were even, the shift by `a=|d|/2` would be an integral number of primitive periods and `uv=vu` with identical half-period parity sequences.

Thus `k` is odd, say `k=2s+1`.  Writing `|w|=2c` gives `a=kc`, and write the primitive word as `w=rs` with `|r|=|s|=c`.  Then

`u=(rs)^s r`,

`v=s(rs)^s`.

Because `u,v` have equal weight, `wt(r)=wt(s)`.  Hence their prefix discrepancy returns to zero already after the first `c=a/k` symbols.

In the retained near-resonant branch `2^a/3^ell<16/15`, one has `ell>a/3`; since `t<=q=a-ell`, the canonical one-excursion terminal return occurs after position

`a-t >= ell > a/3 >= a/k=c`.

Thus `c` is a strict interior prefix of the canonical excursion.  A zero there contradicts the one-excursion hypothesis (the discrepancy is positive between the mandatory `(0,1)` entrance and the terminal `(1,0)` return).

Therefore `k=1`: a hypothetical full-phase `uv` in the retained one-excursion branch is primitive.

So the RL19 primitive-word hypothesis can be met; the failed hypothesis is genuinely the exact-radius-3 transport condition.

---

## 7. Line-by-line theorem match

| RL19/RL10 input | RL48 four-swap object | Status |
|---|---|---|
| full `D`-divisible cycle word | `d=uv`, with `2^(2a)-3^(2ell) | Q(uv)` under full phase | MATCH |
| positive cycle | phase quotient gives positive `N` and genuine trajectories | MATCH |
| primitive word | Section 6 under retained one-excursion + near-resonance hypotheses | MATCH (new lemma) |
| a distinct cyclic rotation | shift by `a`: `uv -> vu` | MATCH |
| **exact cyclic adjacent-transposition radius 3** | distance is `2(a-t-3+H)` | **FAILS** |
| RL10 three-unit-flow support | half-rotation flow is the entire one-excursion and its negative | **FAILS** |

The failure occurs before the later RL19 gcd/support subcases are relevant.

---

## 8. Correct status of Gate B

The direct claim

> full phase -> `N <-> N+4` depth-three split -> invoke RL19 radius 3

is **false as a theorem match**.

What RL48 did prove remains useful:

1. the full phase condition is root-specific and exact;
2. it is equivalent to the positive two-half return `N <-> N+4`;
3. the phase can be rewritten as the rank-defect congruence

   `12D_rank + 2^(a-t-2) = 237*3^(ell-3) (mod 2^a-3^ell)`.

The viable radius-3 route must therefore be a genuine **arithmetic transplant**: derive from the full phase/rank-defect data a separate self-rotation whose *global cyclic transposition distance* is at most 3, or reproduce the RL19 sparse uniqueness contradiction directly.  A third-bit split by itself is not such a bridge.

Gate B returns to **OPEN**, but in a more sharply defined form than before RL48.

---

## 9. Consequence for Gate A

Gate A is not made obsolete by the four-swap theorem.  The exact metric identity instead shows

`dist_cyc(uv,vu)=2(a-t-3+H)`.

If Gate A is proved (`H>=t+3`), then the distinguished half-rotation satisfies

`dist_cyc(uv,vu)>=2a`,

so Gate A actually pushes this particular rotation *farther* from radius 3.  Any successful use of the radius-3 theorem must therefore create a different derived rotation/arithmetic object rather than apply it to the half-period pair itself.

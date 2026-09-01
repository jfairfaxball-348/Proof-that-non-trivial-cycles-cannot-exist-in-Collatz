# RL219 — bounded-blue physical floor and finite dyadic-library sparsity

Date: 2026-09-01.

## Scope

This note works only on the inherited e=16 H21 branch and the exact RL217/RL218 arithmetic interface. It proves two route-level results and **does not delete any RL217 phase-51 arithmetic candidate** by itself.

The inherited shortcut Collatz map is

`T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.

The inherited H21 constants are

`A=217976794617`, `L=137528045312`,
`b_i=floor(A i/L)`, `lambda=2^A/3^L`,
with the certified analytic bound

`0 < ln(lambda) < 2^-40`.

A physical H21 realization has nonnegative integer heights and exact acceleration exponents

`a_i=b_(i+1)-b_i+h_i-h_(i+1) >= 1`.

At the common e=16 coordinate, `h_16=1` and

`y_16 = 2^34 x - 1 - 3^16 2^13`.

The accompanying exact verifier reconstructs the inherited prefix windows and proves

`y_16 >= Y16_MIN = 63923554738764449832959`

for every non-deleted e=16 prefix and every admissible k in the larger pre-phase-51 window family. Hence the same lower bound holds for every RL217 phase-51 survivor.

---

## Theorem T1 — full-period physical shortcut floor

Assume one of the current e=16 arithmetic candidates extends to a **physical** H21 realization, so all heights on the physical word are nonnegative. Then every shortcut-Collatz state in the complete `L`-odd-step traversal containing its phase-16 state is strictly greater than

`B_H21 = floor(Y16_MIN/8) = 7990444342345556229119`.

### Proof

For `0<=d<=L`, let

`E_d = sum_(j=0)^(d-1) a_(16+j)`.

Telescoping the exact height recurrence gives

`E_d = b_(16+d)-b_16+h_16-h_(16+d)`.

Since `h_16=1` and physical heights are nonnegative,

`E_d <= b_(16+d)-b_16+1`.

For real `x,y`, `floor(x+y)-floor(x) < y+1`. Therefore

`b_(16+d)-b_16 < A d/L + 1`,

so

`E_d < A d/L + 2`.

After `d` accelerated odd steps, repeated substitution gives

`2^E_d y_(16+d) = 3^d y_16 + C_d`

with `C_d>=0`. For `d>0`, the additive term is positive; for `d=0` the desired bound is immediate. Thus

`y_(16+d) > 3^d y_16 / 2^E_d`

and hence

`y_(16+d) > (y_16/4) * (3/2^(A/L))^d`

`= (y_16/4) * lambda^(-d/L)`.

Because `lambda>1` and `d<=L`, `lambda^(d/L)<=lambda`. The inherited bound `ln(lambda)<2^-40`, together with the elementary inequality `ln 2 > 1/2 > 2^-40`, gives `lambda<2`. Therefore

`y_(16+d) > y_16/(4 lambda) > y_16/8 >= Y16_MIN/8`.

Every ordinary shortcut state between two consecutive accelerated odd states is obtained before the final halvings and is therefore at least the following odd state. Hence the same strict floor holds for all intervening even shortcut states. One `L`-odd-step traversal is a complete physical H21 period. ∎

### Corollary T1a — stable verified interval is below the physical floor

Barina (Journal of Supercomputing 81, 810, 2025, DOI `10.1007/s11227-025-07337-0`) reports computational convergence verification for all starting values through `2^71`.

The exact finite comparison is

`B_H21 - 2^71 = 5629261100910733622271 > 0`.

Therefore a physical e=16 H21 cycle state cannot lie in the stable externally certified interval `[1,2^71]`.

**Classification:** T1 is analytic mathematics conditional only on the inherited physical-H21 hypotheses and inherited `lambda` bound. The `2^71` statement is an **externally inherited computational certificate**, not an analytic proof of Collatz.

### Interpretation lock

T1 does **not** delete all phase-51 arithmetic candidates. A phase-51 candidate is only a necessary arithmetic survivor; it need not possess nonnegative height through the complete period. If an exact computation later proves such a candidate reaches `[1,2^71]`, that is a legitimate certificate that the candidate is nonphysical/blue. T1 says the bounded interval cannot itself be treated as a physical endpoint set without the missing exact equality/trajectory bridge.

---

## Theorem T2 — finite-library dyadic-ray pullbacks remain singleton probes

Let `S={s_1,...,s_m}` be any finite set of positive certified-blue seeds, and let `W={w_1,...,w_r}` be any finite library of fixed raw legal-backward-word templates. For one pair `(s,w)`, let `w` have raw length `n`, `h` odd-inverse letters, and RL218 constant `C_w>=0`. Apply the fixed word to the dyadic seed ray `2^t s` whenever the output is a positive legal integer:

`Y_t = (2^(n+t) s - C_w)/3^h`.

Then the current exact e=16 root band contains at most one endpoint value `Y_t` for that pair `(s,w)`.

Consequently a finite seed set times a finite fixed-word library, even after **unbounded dyadic saturation of every seed**, produces only a finite union of exact endpoint equalities on the current root band. Its RL218 affine pullback cannot produce a non-singleton k residue class merely from the dyadic parameter `t`.

### Proof

Whenever both expressions are considered algebraically,

`Y_(t+1) = 2 Y_t + C_w/3^h >= 2 Y_t`.

Restricting to the legal/integral subsequence can only increase the spacing between successive retained t-values.

The exact inherited current e=16 root band is

`R_MIN = 24913843845551577787381`,
`R_MAX = 31285589992934194300574`.

The verifier pins

`R_MAX < 2 R_MIN`

with margin

`2 R_MIN - R_MAX = 18542097698168961274188`.

Two positive values with multiplicative spacing at least two therefore cannot both lie in `[R_MIN,R_MAX]`. Thus each `(s,w)` contributes at most one endpoint value to the entire current root band. For a fixed endpoint value, the inherited affine root equation on any one prefix has at most one k. A finite collection remains a finite singleton union. ∎

**Classification:** analytic no-go / compression theorem for this finite-library dyadic architecture.

### What T2 does not cover

T2 does not rule out an unbounded certified-blue family in which the non-dyadic word shape, its `C_w`, its number of odd inverses, or the underlying seed family changes coherently with a parameter. It also does not rule out an independently proved arithmetic progression or another additive/affine certified-blue family. Those are precisely the structures left open for RL220.

---

## RL219 route consequence

Together with the inherited RL218 results:

- fixed seed + fixed word gives at most one k;
- the explicit RL80 LTE blue comb has zero intersections with all inherited prefix bases;
- the seed-1 reverse tree through depth 86 has zero matches;

RL219 now adds:

1. a physical H21 shortcut-state floor `>7990444342345556229119`, placing the stable `[1,2^71]` verified interval strictly below any physical e=16 endpoint; and
2. a theorem that finite fixed-word libraries applied to unbounded dyadic seed rays still collapse to finitely many singleton endpoint probes in the narrow current root band.

No candidate, prefix, state, residue class, eta class, rank, Gate, or global claim is deleted. The surviving blue route must acquire genuinely new **unbounded, non-dyadic, parameterized exact basin structure** if it is to compress the RL217 lattice.

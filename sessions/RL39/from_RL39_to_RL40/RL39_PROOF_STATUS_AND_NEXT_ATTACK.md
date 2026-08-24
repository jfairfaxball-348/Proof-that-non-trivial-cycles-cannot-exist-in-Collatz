# RL39 proof status and next attack

Date: 2026-08-21

## Executive status

RL is **not closed**. The current highest-value open target is the audited order-2 / `g=2` balanced-return branch.

The session produced two exact bridge mechanisms that should be treated as the starting point for RL40 rather than reopening already-closed radius-3 work:

1. **RL38 scaled-gap telescoping / crossing charge** removes synchronized runs from the multiplicative gap dynamics exactly and forces the unique physical sign-changing excursion to pay linearly for the synchronized odd mass immediately before it.
2. **RL39 odd-or-valuation transport charge** converts every unsynchronized full-parity column into genuine odd-state correction-product currency, with a quadratic penalty when many columns are hidden behind one large outgoing 2-adic valuation.

Together these repair the two bookkeeping gaps that prevented RL37 from yielding a uniform branch-closing inequality.

## Inherited quantitative facts that remain active

Use the notation

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`, `z=X/Y>1`,

with least cycle state `R`, balanced half-state `R+G`, and order-2 half words of length `a` and weight `ell`.

The inherited near-resonant branch has:

- `R >= 2^71` as an **external inherited lower bound**, not proved inside these local notes;
- `z < 16/15`;
- in the `g=2` near-minimum branch, `R` and `R+G` odd and `4|G`;
- exact correction-product relation
  `A/L = log_2(3) + log(lambda)/(L log 2)`;
- RL35 global packing coefficient `0.245797537816914843649...`, still above the next CF gate;
- next relevant CF coefficient gate approximately `0.1909116`;
- RL37 exact low-transport consequence `rho >= 16`.

Do not confuse any of these branch-specific statements with a proof of global RL.

## RL36 bridge facts

For prefix-count difference

`d_j = p_v(j)-p_u(j)`

and total transport area

`rho = sum_j |d_j|`,

maximal excursions own genuine high odd states and valuation mass. In particular, every unsynchronized column forces one trajectory high, and excursion-owned odd states have aggregate outgoing valuation at least the excursion length.

The transport area is exactly the minimum adjacent-swap distance between the two half words. Each adjacent `10 <-> 01` swap changes the affine numerator by one signed `2^i 3^k` monomial, giving a sparse S-unit relation at low `rho`.

The exact RL36 verifier passes 65,174 equal-weight word-pair checks.

## RL37 low-transport closure

The global sign-reversal budget plus exact canonical-excursion enumeration closes all `rho <= 15` cases. Hence

> `rho >= 16`

for any genuine surviving order-2 / `g=2` balanced return in the near-resonant branch.

The verifier checks 148,520 canonical positive excursions through area 15.

## RL38 — exact scaled-gap telescoping

At a prefix-count synchronization define scaled physical gap

`W_j = q_j (v_j-u_j)`.

On every synchronized run, `W_j` is exactly constant. Therefore all multiplicative gap distortion is concentrated on maximal excursions.

For an excursion `E=[s,t]` with common odd weight `p_E`, length `h_E`, and physical gap `Delta_j=v_j-u_j`, define

`J_E = |Delta_t| / ((3^p_E/2^h_E)|Delta_s|)`.

Then

> `prod_E J_E = z`,

and therefore

> `lambda = prod_E J_E^2`.

So synchronized runs cancel **exactly** from the scaled-gap multiplicative problem.

For a positive inward excursion of transport area `r` immediately preceded by a synchronized run containing `c` common odd columns, the relative inward kick satisfies

> `t_E < 3^(r-1-c)`.

Consequences:

- if `r <= c`, then `t_E < 1/3`;
- if `t_E >= 1/2`, then `r >= c+1`;
- if the excursion changes the physical gap sign, then
  `r >= c+2`.

There is also an exact local integer crossing floor:

> no sign-changing integer excursion exists for area `r <= 6`;

and at area 7 the unique canonical positive crossing is

`alpha=000011`, `beta=101000`, incoming gap `1`, outgoing gap `-1`, `J=64/9`.

Hence the mandatory crossing excursion obeys

> `r_cross >= max(7, c_pre+2)`.

This is the no-`log R` replacement for the synchronized-anchor estimate attempted in RL37.

## RL39 — odd-or-valuation transport charge

For one maximal excursion, use its leading trajectory and let its owned odd states be `y_k`, with assigned halving-chain column multiplicities `l_k`. Let

`H_k = log_3(((3y_k+1)z)/R)`

and `alpha=log_3 2`.

Then the exact excursion-area inequality is

> `r <= sum_k [ l_k H_k - alpha l_k(l_k-1)/2 ]`.

Globally, over all excursion-owned odd states,

> `rho <= sum_y [ l_y H_y - alpha l_y(l_y-1)/2 ]`.

Each `l_y` is bounded by the genuine outgoing valuation `nu(y)`, and

`sum_y l_y <= A`.

The same height variable controls the actual correction factor:

> `R log(1+1/(3y)) <= z/(3^H_y-z/R)`.

Useful floors:

- first owned odd state in an excursion: `H >= log_3 6`;
- every later owned odd state: `H > 2`;
- if `l>=2`, then `H >= 1+(l-1)log_3 2`.

Thus many high full-parity columns can no longer be hidden behind one large valuation without a compensating exponential odd-state height cost.

## The exact remaining mathematical target

The next session should **not** search broadly. It should optimize RL38 and RL39 together.

The desired output is a rigorous supporting inequality of the form

`log(lambda) <= F(rho, H_exc, A, L, R)`

or, preferably after eliminating nuisance variables,

`R log(lambda)/L <= c0 + c1 * Phi(rho/L, A/L)`

with constants strong enough that one of the following happens:

1. the coefficient is forced below the next CF gate (`~0.1909116`) for every surviving `rho>=16`; or
2. the parameter region not covered by the product bound forces sufficiently large/effective transport that RL38's sign-reversal budget eliminates it.

The exact identity

`A/L = log_2(3) + log(lambda)/(L log 2)`

must be used self-consistently rather than treating `A/L` as independent.

### Recommended optimization order

1. **Single-state extremizer.** For fixed assigned multiplicity `l`, solve or bound the maximal correction contribution
   `log(1+1/(3y))`
   subject to the RL39 transport charge
   `lH - alpha*l(l-1)/2`.
   Derive the sharp convex/concave envelope needed for aggregation.

2. **Aggregate by valuation multiplicity.** Use `sum l_y <= A` and, if helpful, the exact full-cycle identity `sum nu=A`. Determine whether concentrating valuation is favorable or unfavorable for maximizing `log lambda` at fixed `rho`.

3. **Separate effective and ineffective excursions.** RL38 gives an exponentially small kick when `r-c` is small. Use the mandatory sign reversal to force at least one excursion with enough `r-c`; combine this with the global `rho>=16` floor.

4. **Close the overlap numerically first, then prove it analytically.** It is acceptable to use a finite exact/rational optimizer to identify the extremal pattern, but freeze only a theorem whose remaining finite check is explicit and auditable.

5. **Only if this fails**, investigate whether the excursion distortion identity `lambda=prod J_E^2` admits a sharper direct bound in terms of transport area than the correction-product route.

## Failed / retired avenues

Do not blindly retry the following:

- **Naive gcd collapse across excursion numerator differences.** Small equal-density examples exist where several excursion differences share gcd `3`. There is no universal coprime-gcd theorem in the form first hoped for.
- **Per-synchronized-anchor `O(log R/R)` charging.** RL38 shows synchronized runs cancel exactly in the scaled-gap product, so this is obsolete and weaker.
- **Assuming `v2(G)=2` automatically gives common prefix `11`.** It only gives two common parity bits. In the low-transport RL37 closure, `11` required a separate least-state minimality argument.
- **Treating high even phases as independent high odd states.** RL39 is the correct valuation-aware bookkeeping repair.
- **Further shaving RL35's local support coefficient without a branch-closing mechanism.** The gain is too small relative to the next CF gate.

## Evidence discipline

- RL remains open.
- Radius-3 closure results elsewhere in the project do not by themselves bridge to global RL.
- Some older radius-3 leaves depend on the published Laurent–Mignotte–Nesterenko two-logarithm theorem.
- `R>=2^71` is inherited external input.
- RL36--RL39 analytic statements should be red-teamed before being used in a final proof.
- Verifier success is an exact finite/symbolic certificate for the enumerated claims, not a substitute for the analytic theorem around it.

# RL30 skeptical audit/review report

Date: 2026-08-21

## Executive verdict

**RL remains open.** The RL29 handover is internally intact and all supplied verifiers reproduce. The new RL29 mathematics is substantially sound **within the exact exceptional three-way-balanced branch**, but the handover overstates the global scope of that branch.

The main audit conclusions are:

1. **22/22 supplied verifiers pass independently.** The 20 inherited RL21–RL27 verifiers pass; the RL29 exact-ownership/lift verifier passes; the slower RL29 transport-scaling verifier also passes when completed separately.
2. The following RL29 claims can be promoted from “proposed analytic” to **analytic, conditional on the stated exceptional branch hypotheses**: the exact absolute and Eisenstein relative ownership identities; the `e>=67` gate; the universal orbit-sum identity; the pairwise transport identity and 47-positive-imbalance threshold; and the `Omega(e/log e)` high-column theorem.
3. The principal correction is logical scope: **`R==91 (mod 288), (G,H)=(12,4)` is not proved to be the unique remaining global RL branch.** It is the weakest/extremal configuration inside a much narrower near-resonant, order-3, three-way-balanced programme, and `(12,4)` is globally forced only in finite/special extremal packages—not for every order-3 survivor.
4. Therefore **eliminating `(G,H)=(12,4)` would not close the current RL theorem.** Several bridge layers remain: the non-near-resonant/huge-length branch; the near-resonant strict-excursion/no-balanced-return branch; balanced returns of order 2 and general order; and non-extremal order-3 balanced sectors.
5. The often-quoted `1/4` coefficient is **not an RL contradiction threshold**. It was a local/global packing benchmark already crossed at RL23. Under the external floor `R>=2^71`, the next continued-fraction denominator gate corresponds to a coefficient near `0.1909116094`, far below the current `0.2483946398`; crossing that next denominator would still not itself prove RL.
6. The exact recovery of `B-Y` and `B^2+BY+Y^2` is real algebra, but it does **not** currently interface with the closed radius-3 sparse theorem: the natural rotated numerators are dense, and the common factors are present by exact block identities rather than by a forbidden sparse zero.

## 1. Verification and integrity

- Outer archive SHA256: **PASS**.
- Internal `SHA256SUMS.txt`: **PASS**.
- Inherited verifier stack: **20/20 PASS**.
- RL29 exact ownership/lift verifier: **PASS**.
- RL29 transport/scaling verifier: **PASS**.
- RL30 quantitative audit verifier: **PASS**.

No stop-and-repair verifier event occurred.

The inherited `R>=2^71` minimum-state bound remains **EXTERNAL COMPUTATIONAL INPUT**. The radius-3 proof tree also retains the explicitly documented published LMN two-logarithm dependency in several older branches.

## 2. Proof-state table

| Statement | RL30 status | Evidence / scope |
|---|---|---|
| Exact radius-3 primitive `D`-divisible self-rotation obstruction | **PROVED conditional on inherited dependency ledger** | Analytic case tree; several older leaves use published LMN + exact finite certificates; final cubic one-orbit leaf analytic |
| “Every RL object is forced into radius <=3” | **FALSE AS A PROVED BRIDGE / not available** | Inherited work explicitly says this bridge is not proved; local grammar has countermodel evidence |
| Global odd-step product/state-packing identities | **PROVED** | Analytic, radius-independent |
| Global reduction to near resonance or huge length | **PROVED dichotomy, not closure** | Analytic; numerical huge-length consequences may use external `R>=2^71` |
| Near-resonant canonical imbalance is nonnegative | **PROVED** | Analytic |
| A balanced canonical return always exists | **NOT PROVED** | Strict-excursion/no-balanced-return branch remains open |
| Every balanced return has order 3 | **NOT PROVED** | Order 2 and general cyclotomic orders remain |
| Order-3 three-way balanced cubic lattice/range identities | **PROVED in stated branch** | Analytic |
| All non-weak order-3 sectors are excluded | **NOT PROVED** | They pay stronger lower bounds/physical-gap costs, but no global contradiction is established |
| `R==91 mod288, (G,H)=(12,4)` is the unique global survivor | **FALSE / OVERSTATED** | Only an extremal weak-close subgeometry; exact `(12,4)` is not globally forced for all order-3 survivors |
| RL29 lift `R==667 mod4608`, `R>=5275`, nine-bit prefixes | **PROVED within exact exceptional branch** | Exact finite residue/leastness argument; does not use external `2^71` floor |
| `gcd(A0,A2,A6)=B-Y` and integer Bezout extraction | **PROVED** | Direct synchronized-rotation algebra; state-sum Bezout combination equals 1 |
| `gcd_{Z[w]}(F0,F6)=B w^2-Y` up to a unit | **PROVED** | Explicit Eisenstein Bezout identity; quotient factors are coprime |
| `e>=67` | **PROVED within exact exceptional branch** | Correction-product ratio + elementary binomial/geometric bound + `R>=5275` |
| Universal orbit-sum identity | **PROVED** | Direct affine-word identity; finite verifier agrees |
| Triple-synchronized columns contribute zero to relative mode | **PROVED, with cancellation caveat** | Each synchronized summand is exactly zero; unsynchronized summands can still cancel mutually |
| Pairwise transport identity / 47 positive-imbalance times | **PROVED** | Exact prefix identity; negative terms only strengthen the counting requirement |
| `Omega(e/log e)` aligned high columns | **PROVED within exact exceptional branch** | Synchronized-run residue-span argument is valid after explicit endpoint/off-by-one audit |
| Positive-density high **odd** states | **NOT PROVED** | High columns may be even; `Omega(e/log e)` is too sparse to force odd occupancy |
| Weighted `Omega(e)` product gain | **NOT PROVED** | Current run-length/divisibility estimate alone does not supply it |
| Algebraic import of RL29 factor ownership into radius-3 sparse uniqueness | **NOT PROVED** | Natural `F_s` are dense; exact factorization is not a sparse forbidden zero |
| Lift-density depth-35 data | **EXPLORATORY** | Reproducible finite evidence only |

## 3. Audit of the new RL29 mathematics

### 3.1 Finite lift and forced prefixes — accepted

In the exact weak/extremal branch, simultaneous leastness of the starts `R`, `R+12`, `R+4` through the ten-step lift leaves the bounded `R=91` branch and the unbounded class `R==155 mod512`. Intersecting with `R==1 mod9` gives `R==667 mod4608`. The actual trajectory of `667` drops to `572` at step 24, so the next possible member is `5275`.

The nine-bit parity prefixes and the synchronized gap values at `s=6` and `s=9` are exact consequences of the residue class. No `R>=2^71` input is used here.

### 3.2 Absolute ownership — accepted

At a synchronized shift `s`, rotating all three equal-density blocks preserves length `b` and weight `e`: the suffix odd-count loss in one block is exactly replaced by the equal prefix count in the next block. Thus

`U_s=Bv_s-Yu_s`, `V_s=Bw_s-Yv_s`, `W_s=Bu_s-Yw_s`

are genuine rotated balanced numerators and

`A_s=U_s+V_s+W_s=(B-Y)(u_s+v_s+w_s)`.

At `s=0,2,6`, the exact relation

`200 S_2-207 S_0-64 S_6=1`

shows `gcd(S_0,S_2,S_6)=1`, hence

`gcd(A_0,A_2,A_6)=B-Y`

and

`B-Y=200A_2-207A_0-64A_6`.

No orientation defect was found.

### 3.3 Relative Eisenstein ownership — accepted

With `w^2+w+1=0`,

`F_s=U_s+wV_s+w^2W_s=(Bw^2-Y) alpha_s`,

`alpha_s=u_s+w v_s+w^2 w_s`.

At `s=0,6`,

`alpha_0=-4+8w`, `N(alpha_0)=112`,

`alpha_6=-14+31w`, `N(alpha_6)=1591=37*43`.

The explicit identity

`(-19-11w)alpha_0+(5+3w)alpha_6=1`

proves the quotients generate the unit ideal, so in the Eisenstein integers

`gcd(F_0,F_6)=Bw^2-Y`

up to a unit. Taking the norm recovers `B^2+BY+Y^2`. Also

`gcd(B-Y,B^2+BY+Y^2)=1`

because modulo `B-Y` the second factor is `3Y^2`, while `B-Y` is coprime to both 3 and `Y`.

### 3.4 `e>=67` — accepted

For the equal-count `u,v` tails after `s=9`, the odd-correction product identity

`P=(2^L/3^m)(endpoint/start)`

is exact. Their ratio is

`K_9=((R+12)(2187R+29143))/((R+4)(2187R+3031))`.

All cycle phases are at least the least state `R`, hence every numerator-tail odd correction is at most `1+1/(3R)` and the denominator product is `>1`. Therefore

`K_9<(1+1/(3R))^(e-7)`.

If `e-7<=59`, then for `59/(3R)<1`,

`(1+1/(3R))^59 <= 1/(1-59/(3R))=3R/(3R-59)`.

The exact polynomial comparison in the verifier shows `K_9>3R/(3R-59)` for every `R>=5275`, contradiction. Thus `e>=67`.

### 3.5 Orbit-sum and transport identities — accepted

For any length-`b`, weight-`e` parity word,

`Z=sum 2^j/3^{p(j)} = 4Q/Y+B/Y-1`

follows by summing the affine contribution of each odd step (equivalently by a direct word-numerator identity).

In the exceptional three-block setup this yields the exact relative-mode formula

`sum_j q_j(1+w3^{-a_j}+w^2 3^{-c_j}) = 4(z w^2-1)(-4+8w)`.

When `(a_j,c_j)=(0,0)`, the summand is zero because `1+w+w^2=0`. Thus the relative mode has no direct synchronized support. This does **not** imply positivity or noncancellation of the unsynchronized support.

At a `u/v` synchronization time `s`, the truncated word identity gives

`sum_{j<s} q_j(1-3^{-a_j})=48-4r_s G_s`.

If `G_s<0`, the left side is `>48`. Only indices with `a_j>0` contribute positively, and each positive term is `<q_j<z(R+12)/R`. Since

`46 z(R+12)/R <48`

for `R>=5275`, `z<46/45`, at least 47 positive-imbalance indices are required. The strict/non-strict directions are safe.

### 3.6 `Omega(e/log e)` high-column theorem — accepted with clarified indexing

For each aligned trajectory state,

`R <= q_i(j)x_i(j) < z(R+12)`.

If a column is unsynchronized, two scale factors differ by at least a factor 3, giving one state

`>3R^2/[z(R+12)]>2.928R`.

For a maximal synchronized run of `L` aligned columns, the first `L-1` transitions are common parity bits (and there is one more common transition if the run terminates at the block endpoint). A length-`r` common parity vector fixes an integer state modulo `2^r`. The three aligned states are distinct, so their physical span is at least `2^(r+1)`. Hence the common scale `q` at run start satisfies at least the safe bound

`q*2^L < W`,

`W=z(R+12)-R < 23e/90+552/45`.

At the `k`th column of that run,

`q_{j+k} <= 2^k q < W/2^(L-k)`.

Thus only the last

`C(e)=ceil(log_2(2.9(23e/90+552/45)))`

columns of a synchronized run can possibly have all three states at most `2.9R`. If `U` is the number of unsynchronized columns and `H` the number of high columns, then

`H>=U`,

`H>=b-C(e)(U+1)`.

Optimizing gives

`H >= (b-C(e))/(C(e)+1)=Omega(e/log e)`

because `b>log_2(3)e`.

The three blocks are adjacent disjoint length-`b` portions of the order-3 cycle, so the counted phases are distinct.

## 4. Reconstructed global dependency DAG

The inherited proof graph is not a funnel into the exceptional order-3 geometry. It is approximately:

```text
Hypothetical primitive positive RL object
|
+-- Exact radius-3 theorem
|    +-- CLOSED only if a genuine RL bridge forces a radius<=3 self-rotation
|    +-- no such global bounded-radius bridge is proved
|
+-- Radius-independent product / state-packing identities
     |
     +-- non-near-resonant / large-lambda branch
     |    +-- forces huge L (conditional numerical versions use R>=2^71)
     |    +-- NOT contradictory
     |
     +-- near-resonant branch (e.g. lambda<16/15)
          |
          +-- canonical gcd-block imbalance E_j >= 0
          |
          +-- no proper balanced return / strict excursion
          |    +-- OPEN; RL21 repaired the naive strip-width argument
          |
          +-- one or more balanced canonical returns
               |
               +-- order 2 / g=2-type factor split
               |    +-- simultaneous absolute + gap factor problem OPEN
               |
               +-- general cyclotomic order n>=4
               |    +-- proper cofactor/state ownership OPEN
               |
               +-- order 3 with three equally spaced balanced cuts
                    |
                    +-- absolute + relative cubic modes available
                    +-- global range/lattice inequalities available
                    |
                    +-- favorable orientations/residues
                    |    +-- stronger costs, but NOT globally excluded
                    |
                    +-- weakest/extremal sector
                         R==1 mod3, G>H, weakest root residue
                         |
                         +-- weak-close/root package -> R==91 mod288
                         +-- exact shortest-vector equality -> (G,H)=(12,4)
                         +-- RL29 new ownership/transport theorems
                         +-- still NOT excluded
```

There is also a separate final-return/root dichotomy: the exceptional `(n_close,t_close)=(1,1)` weak close is unique in one hard root class, but other closes merely have stronger defect/high-length consequences; they are not eliminated.

### Direct answer to the audit question

**No. Eliminating `R==91 mod288,(G,H)=(12,4)` would not imply RL from the current bundle.** It would remove the exact weakest/extremal geometry where several obstruction mechanisms align. It would not eliminate:

- the non-near-resonant/huge-length branch;
- the near-resonant strict-excursion/no-balanced-return branch;
- `g=2` / order-2 balanced returns;
- general higher cyclotomic balanced returns;
- non-extremal order-3 balanced returns and stronger residue/orientation sectors, which are constrained but not contradictory;
- the missing global bridge from arbitrary RL structure to the already-closed radius-3 theorem.

This is the most important correction to the RL29 handover framing.

## 5. Quantitative distance to closure

### 5.1 The `1/4` margin

The inherited rational supporting-line coefficient is

`c0=457841/1843200=0.248394639756944...`

and

`1/4-c0=2959/1843200=0.00160536024305556...`.

But **`1/4` is not an RL contradiction threshold**. It is a packing benchmark that RL23 already crossed. Therefore there is no remaining “gain of `0.001605...` needed to close RL.” The bundle’s wording around a “critical 1/4” should be retired or explicitly qualified.

### 5.2 Next continued-fraction gate under the external floor

The inherited notes identify the next relevant denominator as

`q*=65,470,613,321`.

For the simple Legendre coefficient scale under `R0=2^71`, the threshold is

`c_CF = R0 log 2 /(2 q*^2)`

`=0.1909116094045987...`.

Thus the current asymptotic coefficient would need to fall by approximately

`0.2483946397569444-0.1909116094045987`

`=0.0574830303523457`,

about **23.14% of the current coefficient**, merely to cross that next CF denominator. Even that is not an RL contradiction; it only improves the denominator floor.

In the order-3 branch `L=3e`, an asymptotic coefficient improvement `Delta c` corresponds to an extra log-product saving of roughly

`3 Delta c * e/R`.

So:

- the numerical gap from `1/4` to the current coefficient corresponds to `0.004816080729... * e/R`;
- the current-to-next-CF gap corresponds to `0.172449091057... * e/R`.

These are useful normalization scales, not closure theorems.

## 6. Does `Omega(e/log e)` help the existing packing argument?

Only subasymptotically if each high column yields at most bounded normalized gain.

A count `H=Omega(e/log e)` among `Theta(e)` phases has vanishing density. Any bounded per-column correction-product saving therefore contributes only

`O(e/(R log e))`

to the log product, i.e. an `O(1/log e)` improvement in the normalized supporting coefficient. That tends to zero and cannot repair any fixed positive coefficient gap.

For scale: an odd phase at `2.9R` instead of `R` has best-case first-order normalized correction saving

`(1/3)(1-1/2.9)=0.2183908...`.

Even under the unrealistic assumption that every RL29 high column were such a useful odd phase, `Omega(e/log e)` still gives only vanishing coefficient gain.

## 7. Can long synchronized runs carry `Omega(e)` weighted gain?

**Not from the current span argument alone.**

The run estimate says a synchronized run of length `L` has at most `C(e)=Theta(log e)` potentially low columns. This is strong when `L>>log e`, but the extremal counting configuration can consist of about `e/log e` synchronized runs each of length `Theta(log e)`, separated by unsynchronized columns. In that configuration the theorem only forces `Theta(1)` high columns per run.

The `2`-adic congruence itself does not force `Theta(log e)` odd-correction savings per such run. A common synchronized itinerary can contain long zero stretches; the states may remain even, with the divisibility absorbed into long halving runs. A new theorem would have to charge that divisibility to a global resource that the current supporting line treats favorably.

So the hoped-for implication

`long synchronized run => gain proportional to run length`

is **open**, not a consequence of RL29.

## 8. Can high even phases be converted to high odd phases with bounded multiplicity?

**No bounded-multiplicity conversion follows from the present hypotheses.**

Every high even phase does trace backward through its halving chain to an odd phase that is itself above a lower threshold; for a phase `x>2.9R`, the originating odd state is at least roughly `(2x-1)/3>1.93R`. However one very high odd state can generate arbitrarily many high even phases before halving below the threshold if its outgoing 2-adic valuation is large.

Thus the natural map “high even phase -> preceding odd phase” has unbounded multiplicity. Globally, the number of even phases is `A-L ~ (log_2 3-1)L`, which is positive density and easily large enough to contain an `o(L)` set such as `Omega(e/log e)`. So the RL29 high-column theorem alone does not force even one positive-density set of useful high odd corrections.

A viable bridge needs an **odd-or-valuation charging lemma**: either many distinct high odd states occur, or concentration of high even states forces a valuation/block-type penalty that improves the global product inequality.

## 9. Can the 47-positive-imbalance threshold be sharpened into a scaling theorem?

The threshold 47 is correct but intrinsically constant in its present form. It comes from the fixed initial gap `12`, the fixed reversal threshold `48`, and the uniform cap on each positive transport term.

Sharper use of exact `q_j` values may increase the constant, and negative transport terms can only make the required positive mass larger, but no existing argument forces the number of synchronized sign reversals to grow with `e`. Without repeated reversals, a fixed transport threshold cannot change an asymptotic supporting coefficient.

A scaling use would need a new conserved/monotone “transport area” that accumulates over many excursions, not just the first sign reversal.

## 10. Algebraic bypass audit

The RL29 algebraic ownership is exact and nontrivial as bookkeeping, but it is not yet a radius-3 bridge.

The radius-3 cubic closure applies to a **sparse three-term relation in the rotation phase `rho`**, with support geometry coming from three adjacent transpositions. Its norm/resultant arguments depend crucially on that sparse support and on bounded centered exponent geometry.

By contrast,

`F_s=U_s+wV_s+w^2W_s=(Bw^2-Y)alpha_s`

is a dense linear combination of full block numerators. At `s=0,6`, the quotients `alpha_s` are even explicitly coprime, so the common factor is recovered exactly—but this is an equality forced by the block endpoint equations, not a forbidden sparse zero.

The orbit-sum formula reinforces the issue: the relative mode is a weighted sum over **all unsynchronized aligned times**. Synchronized columns cancel, but the remaining support need not be small, and those terms can cancel each other.

No forced low-support cancellation, proper-factor divisibility of a sparse numerator, or new resultant nonvanishing condition is presently established. Therefore Route B should be treated as **exploratory** until an actual sparsification identity is produced.

## 11. Distance-to-closure assessment

The project is not “one lemma from RL.” It is closer to identifying a useful **type of missing bridge theorem** than it was at RL20, but several logical layers remain.

The smallest plausible theorem that would materially advance the current exceptional subprogramme is:

> **Weighted synchronization/valuation bridge.** In the exact three-way-balanced exceptional geometry, every synchronized/unsynchronized excursion can be charged either to a useful high odd correction factor or to a valuation/block-type resource, with total normalized saving at least `c e/R` for a fixed `c>0`.

Such a theorem could convert RL29’s structural scaling into a fixed asymptotic packing improvement. It would **not by itself close RL globally**, because the global DAG still contains the other branches listed above.

To close the full current RL theorem, one needs either:

1. a global theorem forcing every hypothetical RL object into a branch covered by such a contradiction (or into radius 3), **plus** the branch contradiction; or
2. a radius-independent algebraic/weighted invariant that simultaneously handles the strict-excursion, general balanced-order, and huge-length alternatives.

Thus multiple layers remain.

## 12. Recommended next attack

**Primary: weighted synchronization packing, reformulated as odd-or-valuation charging.**

Reasons:

- RL29’s `Omega(e/log e)` theorem is valid and gives real nonlocal structure;
- the failure mode is now precise: vanishing raw density and high-even multiplicity;
- long synchronized zero runs naturally create large 2-adic valuation, while common odd steps create useful correction-product savings, so a dichotomy coupling the two is structurally aligned with the existing RL24 supporting-line machinery;
- a successful theorem can be quantified directly in normalized log-product units.

The next theorem should not merely count high columns. It should assign to each maximal synchronized run/excursion a certified **packing gain** and prove the total gain is `Omega(e)`.

**Secondary: algebraic sparsification.** Continue only if a concrete cancellation reduces a rotated `F_s` or a bounded linear combination of rotations to genuinely low support in `rho`. Exact factor ownership alone is insufficient.

**Avoid:** deeper fixed-modulus residue lifting as a primary route; treating `1/4` as a closure threshold; or assuming that eliminating `(12,4)` completes the global proof.

## 13. Post-audit attack result

The audit itself yields one useful no-go refinement for the next session:

> **High-column-to-high-odd bounded charging is unavailable.** The multiplicity can be arbitrarily large through a long even tail, so any successful weighted bridge must explicitly account for outgoing 2-adic valuation (or an equivalent block resource).

That narrows the next attack to a two-resource inequality rather than a raw high-state count.

# RL135 — multiplicity defect lift, mesoscopic least-state ceilings, and determinant-two continuation

Date: 2026-08-27

## 0. Outcome and classification

RL135 continues from the repaired and freshly verified RL134 authoritative state at the first reduced above-side survivor

`(A,L)=(217,976,794,617,137,528,045,312)`

with

`Delta=A log(2)-L log(3)>0`,
`theta=L Delta/log(2)=0.1783030376029087...`.

It advances the multiplicity branch without closing it.

New promoted results:

1. **RL135.1 — broad one-sided defect theorem.** For every multiplicity
   `1<=g<=771,316,334,039`, every proper accelerated prefix satisfies
   `h_j>=-1`, where `h_j=floor(Aj/L)-S_j`.
2. **RL135.2 — nonnegative defect through multiplicity six.** For every
   `1<=g<=6`, every proper prefix satisfies `h_j>=0`.
3. **RL135.3 — least-state ceilings.** Every hypothetical realization with
   `1<=g<=6` has `m<2^75`; every realization with
   `1<=g<=771,316,334,039` has `m<2^76`; and a refined exceptional-shell
   count gives `m<2^75` for every `1<=g<=28,000,000,000`.
4. **RL135.4 — canonical-contact absolute gap.** For `g<=6`, any physically
   realized canonical contact lies less than `169,751,105,674` above the
   least odd state. No contact existence is inferred.
5. **RL135.5 — determinant-two continuation.** For `12<=g<=16`, the only
   positive-prefix count-pair candidates are the canonical, determinant
   `±1`, and determinant `±2` translate families stated below. At `g=17`,
   determinant `±3` first becomes strip-eligible.
6. **RL135.6 — conditional absolute state populations through `g=16`.**
   Conditional on the inherited external least-cycle input `m>=2^71`,
   explicit multiplicity-dependent lower bounds are obtained for distinct
   odd states below `2^79` and `2^80`.

No multiplicity is excluded. The internally certified primitive ordinary
frontier remains `L>=190,537`; conditional on the inherited external
`R#>=2^71`, the frontier remains `L>=49,547,666,544`. Gate A and Gate B
remain open. No global nontrivial-cycle exclusion or Collatz proof is claimed.

## 1. Incoming authority and repaired start gate

RL135 starts from corrective commit

`528465486fa9bd6d09bf0df08dc2d269ff71cc29`.

The RL134 mathematical state is unchanged by that corrective commit. The
original RL134 bundle reconstructs losslessly from the committed transport,
has SHA-256

`6ff26609ee5414dc7a2434b6bb3b7993577936894eb7c392395edf36ab6b21ec`,

and its recorded fresh-unpack report gives:

- outer sidecar: PASS;
- fresh unzip: PASS;
- internal `SHA256SUMS.txt`: PASS;
- fast verifier suite: PASS.

Verification economy is therefore applied.

Inherited exact data used here:

- `U=(103,768,467,013,65,470,613,321)`, determinant `-1`;
- `W=(114,208,327,604,72,057,431,991)`, determinant `+1`;
- `V=(10,439,860,591,6,586,818,670)`, determinant `+2`;
- `5 theta<1`;
- `11 theta<2<12 theta`;
- for `g<=6`, every **positive** proper prefix is canonical;
- for `7<=g<=11`, the only off-axis positive candidates are determinant
  `±1` translates;
- the RL134 one-period mechanical-weight computation gives
  `sum rho_r < 99,205,514,478` and the resulting `g=1` ceiling `m<2^75`.

The external input `R#>=2^71` is not internalized. Every use of it below is
marked conditional.

## 2. Notation and exact identities

Assume a hypothetical primitive positive ordinary accelerated cycle has full
counts `(gA,gL)` and is rotated to its least odd state `m`. Write

`3 y_i+1 = 2^(a_i) y_(i+1)`, `a_i>=1`.

For `0<=j<=gL` put

`S_j=a_0+...+a_(j-1)`,
`q_j=2^(S_j)/3^j`,
`h_j=floor(Aj/L)-S_j`,
`rho_j=2^(floor(Aj/L))/3^j`.

Then

`q_j=rho_j 2^(-h_j)`.                                      (2.1)

Because `floor(Aj/L)>Aj/L-1`,

`rho_j > (1/2) exp(j Delta/L) > 1/2`.                      (2.2)

RL134's physical least-state prefix squeeze is

`q_j < exp(g Delta)`                                       (2.3)

for every proper prefix.

The full cycle-closing identity is

`(exp(g Delta)-1)m = (1/3) sum_(j=0)^(gL-1) q_j`.          (2.4)

The mechanical weights repeat by blocks:

`rho_(tL+r)=exp(t Delta) rho_r`,                            (2.5)

for `0<=t<g`, `0<=r<L`. Hence

`sum_(j<gL) rho_j
 = ((exp(gDelta)-1)/(exp(Delta)-1)) sum_(r<L) rho_r`.       (2.6)

These identities are physical/ordinary: (2.3) and (2.4) use least-state
ownership and the actual `+1` affine recurrence.

## 3. RL135.1 — broad one-sided defect `h>=-1`

If

`g Delta < log(2)`,                                        (3.1)

then (2.3) gives `q_j<2`.

If a proper prefix had `h_j<=-2`, then by (2.1)-(2.2),

`q_j >= 4 rho_j > 2`,

a contradiction.

### Theorem RL135.1

Whenever `g Delta<log(2)`, every proper prefix satisfies

`h_j>=-1`.                                                 (3.2)

The exact rational-log verifier certifies

`771,316,334,039 Delta < log(2)`

and verifies that the same safe interval inequality no longer holds at the
next integer. Therefore (3.2) is certified for

`1<=g<=771,316,334,039`.                                   (3.3)

Classification: **analytic theorem + exact rational-interval endpoint
certificate**.

This is not a multiplicity upper bound. It says that an enormous
multiplicity range can have at most a one-unit negative mechanical defect.

## 4. RL135.2 — nonnegative defect for `g<=6`

Suppose `1<=g<=6`. RL134.2 says that every physically positive proper
prefix is an exact canonical contact

`(S_j,j)=(kA,kL)`,

and every such contact has `h_j=0`.

If some prefix had `h_j<0`, then `h_j<=-1`; by (2.1)-(2.2),

`q_j >= 2 rho_j >1`.

Thus its discrepancy is positive, so RL134.2 forces it to be canonical,
contradicting `h_j<0`.

### Theorem RL135.2

For every `1<=g<=6` and every proper prefix,

`h_j>=0`.                                                  (4.1)

Classification: **analytic physical consequence of RL134.2**.

Importantly, no canonical contact is assumed to exist. The theorem also
covers the branch with no positive proper prefix.

## 5. RL135.3 — least-state ceilings

### 5.1 Uniform `m<2^75` for `g<=6`

By RL135.2, `q_j<=rho_j`. Using (2.4)-(2.6),

`m <= [sum_(r<L) rho_r]/[3(exp(Delta)-1)]
   < [sum_(r<L) rho_r]/(3 Delta).`                         (5.1)

The right side is exactly the one-period expression certified in RL134 to be
less than `2^75`.

Therefore every hypothetical realization with

`1<=g<=6`

satisfies

`m<2^75`.                                                  (5.2)

This is internal and does not use `R#>=2^71`.

### 5.2 Broad `m<2^76`

Let `x=gDelta`. From (2.3)-(2.4),

`m < gL exp(x)/(3(exp(x)-1))
   = [L/(3Delta)] [x exp(x)/(exp(x)-1)].`                  (5.3)

The function `f(x)=x exp(x)/(exp(x)-1)` is increasing for `x>0`, since its
derivative has numerator `exp(x)(exp(x)-1-x)>0`.

For `0<x<log(2)`,

`f(x)<2 log(2)`.

Thus on the full range (3.3),

`m < 2L log(2)/(3Delta)
   = 2L^2/(3theta)
   < 2^76`.                                                (5.4)

The final inequality is exact-rationally verified.

### 5.3 Refinement using the exceptional `h=-1` population

Under `gDelta<log(2)`, RL135.1 gives only `h= -1,0,1,...`.

If `h_j=-1`, write the RL134 determinant

`r_j=S_j L-jA`.

Then `r_j` is positive. Since the determinant strip has `r_j<gtheta`, there
are fewer than `gtheta` possible positive determinant values, and each fixed
determinant has at most `g` translates in `0<j<gL`. Hence the number `P` of
`h=-1` phases obeys

`P < g^2 theta`.                                           (5.5)

At such a phase, `q_j=2rho_j<exp(gDelta)`, so
`rho_j<exp(gDelta)/2`. Compared with the baseline `sum rho_j`, the total
extra contribution from exceptional phases is therefore less than

`g^2 theta exp(gDelta)/2`.

Combining this with (2.4), the one-period RL134 bound, and the safe
inequalities

`exp(gDelta) <= 1/(1-g Delta_hi)`,
`exp(gDelta)-1 > g Delta_lo`,

gives the exact-verifier upper envelope

`m < M_RL134 + g theta_hi /
              [6 Delta_lo (1-g Delta_hi)]`.                (5.6)

At

`g=28,000,000,000`

this remains strictly below `2^75`. The same particular coarse envelope is
above `2^75` at `g=29,000,000,000`; that is a method threshold, not evidence
that any actual cycle exists there.

### Theorem RL135.3

Every hypothetical realization at the first survivor satisfies:

- `m<2^75` for `1<=g<=28,000,000,000`;
- `m<2^76` for `1<=g<=771,316,334,039`.

Classification: **analytic inequalities + exact rational interval
certificate**.

The smaller `g<=6` proof is stronger structurally because it uses exact
nonnegative defect and geometric cancellation; the 28-billion extension
allows sparse `h=-1` exceptions.

## 6. RL135.4 — canonical-contact physical gap

Let `g<=6` and suppose a canonical contact is actually realized at
`j=kL`, `1<=k<=g-1`, with endpoint state `y`.

The complementary affine identity and positivity give

`m <= y < exp((g-k)Delta)m`.                               (6.1)

Using `m<2^75` and `g-k<=5`,

`0 <= y-m < (exp(5Delta)-1)2^75`.

The verifier uses `exp(x)-1 < x/(1-x)` to certify

`y-m < 169,751,105,674`.                                  (6.2)

For a primitive cycle a distinct contact state must in addition satisfy
`y-m>=2`, but (6.2) does not contradict that spacing.

Classification: **analytic physical band + exact arithmetic**.

No canonical contact existence is inferred.

## 7. RL135.5 — determinant-two continuation through `g=16`

RL134 already identifies the determinant `+2` continued-fraction neighbor

`V=(10,439,860,591,6,586,818,670)`,

with `V_A L-V_L A=2`.

The determinant `-2` base obtained from the exact translate
parametrization is

`V_-2=(207,536,934,026,130,941,226,642)`,

with determinant `-2`.

The exact verifier proves

`11Delta < d_(+2) < 12Delta`,                              (7.1)

and

`-11Delta < d_(-2) < -10Delta`.                           (7.2)

It also certifies

`16theta<3<17theta`.                                       (7.3)

Therefore for `12<=g<=16`, the strip allows only determinants
`r in {-2,-1,0,1,2}`, and the discrepancy windows give the following exact
candidate families:

- canonical: `(kA,kL)`, `1<=k<=g-1`;
- determinant `+1`: `W+k(A,L)`, `0<=k<=g-7`;
- determinant `-1`: `U+k(A,L)`, `6<=k<=g-1`;
- determinant `+2`: `V+k(A,L)`, `0<=k<=g-12`;
- determinant `-2`: `V_-2+k(A,L)`, `11<=k<=g-1`.

These are candidate count pairs, not realization or existence claims.

At `g=17`, determinant `±3` becomes strip-eligible and this explicit
classification stops.

For `g<=16`, a negative mechanical defect can only be `h=-1`, and it
corresponds to a positive determinant shell. Consequently the maximum number
of `h=-1` candidate phases is

`P(g)=0` for `g<=6`,
`P(g)=g-6` for `7<=g<=11`,
`P(g)=2g-17` for `12<=g<=16`.                              (7.4)

Classification: **analytic consequence + exact determinant/rational-log
arithmetic**.

## 8. RL135.6 — conditional state populations through `g=16`

This section alone uses the inherited external least-cycle floor

`m>=2^71`.                                                 (8.1)

For `g<=16`, use (7.4), the one-period RL134 mechanical-weight bound, and
the exact cycle identity. Let

`N_k=#{0<=j<gL : h_j<=k}`.

For `M=2^(k+1)`, deep phases contribute at most `rho/M`; shallow
nonexceptional phases contribute at most `rho`; and an `h=-1` phase needs at
most one additional `rho`. The exact verifier bounds every individual
mechanical weight by `exp(gDelta)` and obtains the following conservative
floors:

| g | max `h=-1` phases | `N_3` floor | `N_4` floor |
|---:|---:|---:|---:|
| 1 | 0 | **176,421,674** | **3,399,794,205** |
| 2 | 0 | 352,686,524 | 6,741,665,312 |
| 3 | 0 | 529,029,786 | 10,112,497,968 |
| 4 | 0 | 705,373,047 | 13,483,330,624 |
| 5 | 0 | 881,716,309 | 16,854,163,279 |
| 6 | 0 | 1,058,059,571 | 20,224,995,935 |
| 7 | 1 | 1,234,402,831 | 23,595,828,590 |
| 8 | 2 | 1,410,746,092 | 26,966,661,245 |
| 9 | 3 | 1,587,089,353 | 30,337,493,899 |
| 10 | 4 | 1,763,432,613 | 33,708,326,554 |
| 11 | 5 | 1,939,775,874 | 37,079,159,209 |
| 12 | 7 | 2,116,119,133 | 40,449,991,862 |
| 13 | 9 | 2,292,462,393 | 43,820,824,516 |
| 14 | 11 | 2,468,805,653 | 47,191,657,170 |
| 15 | 13 | 2,645,148,912 | 50,562,489,823 |
| 16 | 15 | 2,821,492,172 | 53,933,322,477 |

For `g=1`, the table deliberately retains RL134's sharper top-weight
optimization instead of the weaker generic RL135 estimate.

The complementary physical prefix identity gives

`y_j < exp(gDelta) 2^(h_j) m/rho_j`.                       (8.2)

Since `rho_j>1/2`, and the exact refined least-state envelope through
`g=16` satisfies the needed margins, the verifier certifies:

- every listed `h<=3` phase is an actual odd state below `2^79`;
- every listed `h<=4` phase is an actual odd state below `2^80`.

Primitivity makes these cycle states distinct.

Thus the `N_3,N_4` rows are also conditional lower bounds on the number of
distinct actual odd cycle states below `2^79,2^80`, respectively.

This is **not** an unstructured scan to `2^80` and is not a finite exclusion
certificate.

Classification: **analytic physical consequence + exact rational
arithmetic + inherited external computational input**.

## 9. Canonical-contact and sliding-window barriers

### 9.1 Canonical numerator split

At a canonical split, the natural numerator-difference identity reduces to

`S=D_full (y-m)`,

where `y,m` are actual physical states. This is ordinary ownership itself.
It does not produce a new divisibility contradiction. Repackaging it as a
"small multiple" would violate the RL110 barrier.

**Status: method barrier / dead route in its present form.**

### 9.2 RL123 sliding-window transport

A canonical count contact says that one length-`kA` window has exactly
`kL` ones. RL123.5, however, gives the cyclic rotation distance from the
**entire** sliding-window dispersion,

`dist_cyc(w,rot_s(w))=min_c sum_i |h_i^(s)-c|`.

One mean-contact window does not control that global `L1` dispersion.
Therefore canonical contact alone does not trigger the inherited radius-three
engine.

**Status: insufficient bridge; retain only if a global dispersion bound is
added.**

## 10. Red teams

### RL20 fake-model discriminator — PASS

RL135.1-RL135.4 begin from RL134's actual least-state prefix squeeze and
ordinary cycle-closing identity. Fixed-content fake words do not acquire
those physical premises from counts alone.

### RL79 generalized-increment scaling — PASS

The least-state formulas use the ordinary `+1` affine numerator. No
generalized increment is cancelled.

### RL81 physical-versus-quotient — PASS

Every `m` and `y_j` in the state ceilings/windows is an actual assumed cycle
state. No quotient representative is promoted to a physical state.

### Primitivity — PASS

Distinct-state population claims use primitivity explicitly. No candidate
prefix count pair is called physically realized without ownership.

### External provenance — PASS

Only Section 8 uses inherited `R#>=2^71`. It remains externally sourced.

### Closure scope — PASS

No multiplicity is excluded, no frontier is advanced, Gate A/B remain open,
and Collatz is not proved.

## 11. Correction/demotion ledger

No inherited theorem is demoted.

New route demotions/barriers:

1. canonical-contact numerator splitting without an additional support or
   spacing theorem reduces to `S=D(x'-x)` and is not a closure;
2. a single canonical mean window does not control the RL123 global
   sliding-window dispersion.

No frontier changes.

## 12. Strategic consequence

RL134 showed that multiplicity initially opens only a thin determinant strip.
RL135 converts that strip into a much stronger physical statement: up to
`771,316,334,039` copies, the least-state prefix path may dip at most one
mechanical unit below the balanced line, and the exceptional negative phases
are sparse enough to keep the least state below `2^75` through
28 billion copies.

The next useful attack is therefore not another bare shell enumeration.
It should force those zero/one-unit defect excursions to interact with actual
owned state fibres, repeated canonical phase markers, or a genuinely global
sliding-window/packing constraint.

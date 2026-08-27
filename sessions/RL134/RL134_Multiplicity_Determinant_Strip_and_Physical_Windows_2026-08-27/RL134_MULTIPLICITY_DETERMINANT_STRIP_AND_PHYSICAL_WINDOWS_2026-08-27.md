# RL134 — multiplicity determinant strip and absolute physical windows at the first CF survivor

Date: 2026-08-27

## 0. Outcome and classification

RL134 continues the RL133 target at the first reduced above-side survivor

`(A,L)=(217,976,794,617,137,528,045,312)`,

with

`Delta=A log(2)-L log(3)>0`.

It advances both live branches without closing either one.

New promoted results:

1. **RL134.1 — physical multiplicity determinant-strip theorem**: for full counts `(gA,gL)`, every positive proper prefix discrepancy is forced into an exact thin determinant strip and an explicit translate family (analytic + exact lattice arithmetic).
2. **RL134.2 — low-multiplicity shell classification**: for `g<=6`, positive proper prefixes can occur only at exact canonical survivor-block contacts; for `7<=g<=11`, the only additional possibilities are translates of the two determinant-one CF neighbors (analytic consequence + exact rational log arithmetic).
3. **RL134.3 — coprime least-state upper bound**: every hypothetical `g=1` realization has least odd state `m<2^75` (analytic consequence + exact rational interval arithmetic).
4. **RL134.4 — sharpened shallow-defect populations**: conditional on inherited external `m>=2^71`, the RL133 floors improve to
   `#{h<=3}>=176,421,674` and
   `#{h<=4}>=3,399,794,205`.
5. **RL134.5 — absolute shallow-state windows**: under the same external floor, at least `176,421,674` actual odd cycle states lie below `2^79`, and at least `3,399,794,205` lie below `2^80`.

No internal or external `L` frontier advances. No multiplicity is excluded solely by RL134. Gate A, Gate B, global nontrivial-cycle exclusion, and Collatz remain open.

## 1. Incoming authority and start gate

The incoming authoritative state is RL133.

`BASE_HEAD=196ee7fe627c09889664f3508962b7a1e12025bf`.

The committed authoritative tree at startup is the RL133 generation, containing the verified extracted directory, ZIP, sidecar, and fresh-unpack report. The uploaded handover ZIP has SHA-256

`d23f45e2d87ad742d0add0918b0b574724f3454b9a3c32af3437cd02e517731e`

and the fresh-unpack start gate passes:

- outer sidecar: PASS;
- fresh unzip: PASS;
- internal `SHA256SUMS.txt`: PASS;
- `verification/run_fast_rl133_verifiers.sh`: PASS.

Verification economy is therefore applied. No recursive historical expensive certificate is rerun.

Frozen incoming frontiers:

- internal primitive ordinary frontier: `L>=190,537`;
- conditional on inherited external `R#>=2^71`: `L>=49,547,666,544`.

RL133 proves the all-prefix nonnegative defect theorem only for full-count multiplicity `g=1`; `g>1` remains open.

## 2. Full-multiplicity least-state prefix squeeze

Assume a hypothetical primitive positive ordinary cycle has full accelerated counts

`(A_full,L_full)=(gA,gL)`,

where `g>=1`, and rotate to its least odd state `m`.

Write the accelerated orbit as

`3y_i+1=2^(a_i)y_(i+1)`

with `a_i>=1`, and for a proper prefix `1<=j<gL` put

`S_j=a_0+...+a_(j-1)`,

`q_j=2^(S_j)/3^j`,

`delta_j=S_j log(2)-j log(3)`.

Exactly as in RL133, positivity of the complementary affine numerator and least-state ownership give

`q_j < exp(g Delta)`,

hence

`delta_j < g Delta`.                                      (2.1)

This is the physical input for everything that follows. It is not inferred from reduced count data alone.

## 3. RL134.1 — determinant strip and translate classification

Put

`epsilon=Delta/log(2)=A-L log_2(3)>0`

and define the integer determinant

`r_j=S_j L-jA`.

Then the identity

`delta_j=(log(2)/L)(r_j+j epsilon)`                       (3.1)

is exact.

Therefore a **positive** proper prefix satisfies

`0 < r_j+j epsilon < gL epsilon`.                         (3.2)

Equivalently,

`-j epsilon < r_j < (gL-j)epsilon`.                       (3.3)

Define

`theta=L epsilon=L Delta/log(2)`.

The exact verifier certifies

`theta = 0.1783030376029087...`

with rigorous rational enclosure. Since `0<j<gL`, (3.3) implies the global shell bound

`|r_j| < g theta`.                                        (3.4)

Thus multiplicity does not reopen an unrestricted two-dimensional lattice. A physically positive prefix must lie in only the determinant shells intersecting this narrow strip.

### Explicit lattice translates

RL133's previous below-side neighbor is

`U=(u,q)=(103,768,467,013,65,470,613,321)`

and satisfies

`uL-qA=-1`.

Hence

`qA == 1 (mod L)`,

so `q` is the inverse of `A mod L`.

For any integer determinant `r`, define

`j_r = (-r q) mod L`, `0<=j_r<L`,

`S_r = (j_r A+r)/L`.

Every integer lattice pair `(S,j)` with

`SL-jA=r`

is uniquely of the form

`(S,j)=(S_r+kA,j_r+kL)`                                   (3.5)

for an integer `k`.

Let

`d_r=S_r log(2)-j_r log(3)`.

Then the physical positive-prefix condition is exactly

`0<j_r+kL<gL`,                                            (3.6)

`0<d_r+k Delta<g Delta`.                                  (3.7)

### Theorem RL134.1

For a hypothetical physical cycle with full counts `(gA,gL)`, every positive proper accelerated prefix belongs to one of the determinant-shell translate families (3.5) satisfying (3.6)–(3.7), and only shells with `|r|<g theta` need be considered.

Classification: **analytic physical theorem + exact integer lattice parametrization**.

This is stronger than a count-only gcd-block statement because (2.1), and hence the thin strip, comes from actual least-state ownership and the positive affine complementary numerator.

## 4. RL134.2 — exact low-multiplicity shells through `g=11`

The exact verifier certifies

`11 theta < 2 < 12 theta`.                                (4.1)

Therefore for every `g<=11`, a positive prefix can have only

`r in {-1,0,1}`.

For `g<=5`, already `g theta<1`, so only `r=0` is possible.

### The zero shell

Because `gcd(A,L)=1`,

`r=0`

forces

`(S,j)=(kA,kL)`.

For a proper prefix this gives the canonical contacts

`1<=k<=g-1`.                                              (4.2)

Each such contact has discrepancy exactly `k Delta`.

### The `+1` shell

The unique base representative in `0<j<L` is the inherited intermediate above-side neighbor

`W=(s,t)=(114,208,327,604,72,057,431,991)`,

with

`sL-tA=1`.

Put

`d_+=s log(2)-t log(3)`.

The verifier proves rigorously

`6 Delta < d_+ < 7 Delta`.                                (4.3)

Thus the `+1` shell contributes precisely

`W+k(A,L)`, `0<=k<=g-7`,                                  (4.4)

when `g>=7`, and contributes nothing for `g<=6`.

### The `-1` shell

The base representative is `U`, with

`d_-=u log(2)-q log(3)`.

The verifier proves

`-6 Delta < d_- < -5 Delta`.                              (4.5)

Consequently `U+k(A,L)` first becomes positive at `k=6`, and for a `g`-fold full count the admissible proper translates are precisely

`U+k(A,L)`, `6<=k<=g-1`,                                  (4.6)

when `g>=7`.

### Theorem RL134.2

For `1<=g<=6`, every positive proper prefix is an exact canonical contact

`(S,j)=(kA,kL)`, `1<=k<=g-1`.

In particular, **no off-axis positive prefix is possible for `g<=6`**.

For `7<=g<=11`, every positive proper prefix is one of exactly these candidate families:

- canonical contacts `(kA,kL)`, `1<=k<=g-1`;
- `W+k(A,L)`, `0<=k<=g-7`;
- `U+k(A,L)`, `6<=k<=g-1`.

These are candidate prefix count pairs, not existence claims.

At `g=12`, the shell bound first permits determinant `|r|=2`, so a new shell genuinely enters and the explicit `g<=11` classification stops there.

Classification: **analytic consequence + exact finite rational-log and determinant arithmetic**.

Strategically, this means the multiplicity obstruction remains one-dimensional through `g=6` and only gains the two determinant-one neighbor families through `g=11`.

## 5. RL134.3 — `g=1` least-state upper bound `m<2^75`

Return to the coprime full-count branch `g=1`.

RL133 proves

`h_j=floor(Aj/L)-S_j >= 0`

and

`q_j=rho_j 2^(-h_j)`,

where

`rho_j=2^(floor(Aj/L))/3^j`.

Hence

`sum q_j <= sum rho_j`.                                   (5.1)

The exact cycle-closing affine identity is

`(2^A-3^L)m = sum_(j=0)^(L-1) 3^(L-1-j) 2^(S_j)`.

After dividing by `3^L`,

`(exp(Delta)-1)m = (1/3) sum q_j`.                        (5.2)

Therefore

`m = (sum q_j)/(3(exp(Delta)-1))
   < (sum rho_j)/(3 Delta)`.                              (5.3)

RL133's exact arithmetic gives a rigorous upper bound on `sum rho_j`. Reusing the same rational logarithm intervals, the RL134 verifier certifies directly that the right side of (5.3) is less than

`2^75`.

### Theorem RL134.3

Any hypothetical physical `g=1` realization of the first survivor satisfies

`m < 2^75`.                                                (5.4)

This upper bound is internal to the `g=1` argument and does not use the external `R#>=2^71` input.

Combining it with the inherited external floor gives the explicitly conditional window

`2^71 <= m < 2^75`.                                       (5.5)

Classification: **analytic consequence + exact finite rational-interval arithmetic**; (5.5) additionally uses the inherited external certificate.

## 6. RL134.4 — sharpened shallow-defect population force

RL133 bounded shallow populations by replacing every selected `rho_j` by `1`. RL134 uses the exact permutation structure of the mechanical weights.

For `1<=j<L`, let

`r_j = Aj mod L`.

Then `r_j` permutes `1,...,L-1`, and

`rho_j = exp((j/L)Delta) 2^(-r_j/L)`.                     (6.1)

Thus for any set of `N>=1` phases,

`sum_selected rho_j
 <= 1 + exp(Delta) sum_(r=1)^(N-1) 2^(-r/L)`.             (6.2)

The verifier upper-bounds the finite geometric tail rigorously using

`1-exp(-x) >= x-x^2/2`

and, for the small relevant `y`,

`1-exp(-y) <= y-y^2/2+y^3/6`.

Let

`N_k=#{0<=j<L : h_j<=k}`

and `M=2^(k+1)`. Splitting shallow and deep phases gives

`sum q_j
 <= (sum rho_j)/M
    +(1-1/M)(sum_(h_j<=k) rho_j)`.                        (6.3)

Conditional on inherited external `m>=2^71`, the exact identity (5.2) gives

`sum q_j > 3*2^71*Delta`.

Combining this lower force with (6.2)–(6.3), the exact verifier proves:

### Theorem RL134.4

Conditional on inherited external `R#>=2^71`, every hypothetical `g=1` realization has at least

`176,421,674`

odd phases with `h<=3`, and at least

`3,399,794,205`

odd phases with `h<=4`.

These strictly improve RL133's certified floors

`176,343,262` and `3,370,832,656`.

Classification: **analytic optimization + exact rational arithmetic + inherited external computational input**.

## 7. RL134.5 — absolute physical windows for the shallow population

For every proper `j`,

`rho_j=2^(-{j beta})>1/2`.

RL133's physical band gives

`y_j < exp(Delta) 2^(h_j) m/rho_j
     < exp(Delta) 2^(h_j+1) m`.                           (7.1)

Using the exact `m` upper bound computation behind RL134.3, the verifier certifies

- if `h_j<=3`, then `y_j<2^79`;
- if `h_j<=4`, then `y_j<2^80`.

Together with RL134.4:

### Theorem RL134.5

Conditional on inherited external `R#>=2^71`, a hypothetical `g=1` realization must contain at least

- `176,421,674` distinct actual odd cycle states below `2^79`;
- `3,399,794,205` distinct actual odd cycle states below `2^80`.

This is a physical population theorem. It is **not** a claim that all integers below `2^80` have been externally verified, and it is not a finite exclusion certificate.

Classification: **analytic physical-state consequence + exact arithmetic + inherited external floor**.

## 8. Red teams and barriers

### RL20 fake-model discriminator — PASS

The determinant strip begins from the actual least-state prefix squeeze (2.1). An arbitrary fixed-content word does not acquire that premise merely from its counts.

### RL79 generalized-increment scaling — PASS

The `g=1` state upper bound and physical-window consequences use the ordinary `+1` cycle-closing numerator identity. No generalized-increment cancellation is claimed.

### RL81 physical-versus-quotient — PASS

All `m` and `y_j` in Sections 5–7 are actual assumed cycle states. No auxiliary quotient representative is silently promoted to a physical state.

### Multiplicity scope — PASS

RL134 does not claim `g<=11`, or that `g<=6` is excluded. It classifies the allowed positive-prefix lattice families **conditional on a specified multiplicity**. At `g=12` determinant-two shells are explicitly left open.

### External-floor provenance — PASS

Only the sharpened population floors and their absolute state-count consequences use inherited external `R#>=2^71`. The determinant-strip theorem and `m<2^75` upper bound do not.

### Bare-CF / count-only gcd barrier — respected

Continued-fraction neighbor arithmetic is used only after the physical least-state strip has been proved. No new frontier is inferred from a bare approximation inequality or count-only gcd decomposition.

### Radius-three scope — respected

RL134 does not infer a radius-three entry from shallow defect alone. The inherited local radius engine remains closed but is not newly triggered here.

## 9. Correction/demotion ledger

No inherited theorem is demoted.

No frontier changes:

- internal primitive ordinary frontier: `L>=190,537`;
- conditional on inherited external `R#>=2^71`: `L>=49,547,666,544`.

The first reduced survivor remains open.

The `g=1` branch is substantially narrower but not excluded. The `g>1` branch now has an exact physical determinant-shell classification, but multiplicity itself is not bounded or excluded.

Gate A: open globally.

Gate B: open globally.

Global nontrivial-cycle exclusion: open.

Collatz conjecture: not proved.

## 10. Strategic frontier after RL134

RL135 should consume the new restrictions rather than restart retired routes.

1. **Low multiplicity `2<=g<=6`:** positive prefixes can only be canonical contacts `(kA,kL)`. Couple those contacts to actual state ownership. At a contact the prefix ratio is exactly `exp(k Delta)`, so the corresponding physical state lies in a very narrow multiplicative band above the least state. Seek a spacing, congruence, block-numerator, or distinct-state contradiction among these canonical near-minimum contacts.
2. **Multiplicity `7<=g<=11`:** add the two explicit determinant-one neighbor translate families and test whether their forced state bands can coexist with canonical contacts and full ownership.
3. **`g=1`:** exploit the absolute window `2^71<=m<2^75` and the billions of shallow states below `2^80` together with exact ownership/CRT spacing or the RL123 window-transport theorem. Do not replace this by an unstructured brute scan to `2^80`.
4. **Higher multiplicity:** use the general determinant translate theorem to admit the determinant-two shell at `g=12` and enumerate only newly opened shells, with exact rational-log thresholds.

Do not claim a Gate or global closure unless the corresponding full branch is discharged.

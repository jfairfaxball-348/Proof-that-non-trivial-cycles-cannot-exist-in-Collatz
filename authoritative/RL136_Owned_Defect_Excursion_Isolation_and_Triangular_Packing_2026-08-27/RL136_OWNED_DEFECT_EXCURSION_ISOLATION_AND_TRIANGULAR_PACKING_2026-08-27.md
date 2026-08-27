# RL136 — owned defect-excursion isolation, three-fibre signatures, and triangular packing

Date: 2026-08-27

## 0. Outcome and classification

RL136 continues from the verified RL135 state at the first reduced above-side survivor

`(A,L)=(217,976,794,617,137,528,045,312)`

with

`Delta=A log(2)-L log(3)>0`,
`theta=L Delta/log(2)=0.1783030376029087...`.

RL136 does **not** exclude a multiplicity and does not close either global gate. It does, however, turn the inherited one-defect statement into an owned local physical structure and improves the mesoscopic least-state ceiling by almost a factor two in multiplicity.

New promoted results:

1. **RL136.1 — terminal localization and isolation of negative defect.** Any physical `h_j=-1` phase requires more than `1/theta>5` reduced blocks to remain. Every such phase with at most `320,125,202,432` reduced-block units remaining is isolated and exits immediately to `h=0`. In particular all negative phases are isolated for every `g<=320,125,202,432`.
2. **RL136.2 — owned three-fibre excursion signature.** In the isolation range, every negative excursion is an actual near-minimum odd state `==3 (mod 4)`, exits in one accelerated exponent `a_j=1` to an actual odd state `==-1 (mod 3)`, and is entered through an actual dyadic boundary whose depth is determined by the predecessor defect.
3. **RL136.3 — triangular exceptional-shell population bound.** The physical `h=-1` population is bounded by the triangular translate envelope
   `P(g) <= sum_(1<=r<g theta) (g-floor(r/theta))`,
   rather than the rectangular `P<g^2 theta` estimate used in RL135.
4. **RL136.4 — improved contiguous least-state ceiling.** The triangular bound, consumed through the physical cycle-closing identity, proves
   `m<2^75` for every
   `1<=g<=56,336,298,016`.
   The same monotone certified envelope is at or above `2^75` at the next integer; this is a method threshold, not evidence of a cycle.
5. **RL136.5 — sharpened low-shell physical windows.** Through `g=16`, every realized determinant `+1` negative phase lies less than `339,502,211,350` above `m`, every realized determinant `+2` negative phase lies less than `169,751,105,674` above `m`, and the last admissible translate of any positive shell in the promoted `m<2^75` range lies less than `33,950,221,135` above `m` if it is physically realized.

The internally certified primitive ordinary frontier remains `L>=190,537`. Conditional on the inherited external `R#>=2^71`, the frontier remains `L>=49,547,666,544`. No multiplicity is excluded. Gate A and Gate B remain open. Global nontrivial-cycle exclusion remains open. Collatz is not proved.

---

## 1. Incoming authority and verification economy

Incoming authoritative commit:

`fb5066f21a4b63f86d5e96b51c03d87a1d5a59b5`.

The RL135 fresh-unpack record gives:

- outer sidecar: PASS;
- fresh unzip: PASS;
- internal manifest: PASS;
- fast verifier: PASS.

Verification economy is applied. No historical expensive certificate is rerun.

Inherited results used here include:

- every proper prefix has `h_j>=-1` for `1<=g<=771,316,334,039`;
- every proper prefix has `h_j>=0` for `g<=6`;
- physical prefix squeeze `q_j<exp(g Delta)`;
- `rho_j>(1/2)exp(j Delta/L)`;
- determinant strip for every physically positive prefix;
- the exact translate parametrization of a determinant shell;
- one-period mechanical-weight upper envelope from RL134/RL135;
- the RL122 owned run-fibre theorem and RL123 sliding-window transport theorem as global resources.

The external input `R#>=2^71` is not needed for RL136.1--RL136.5.

---

## 2. Notation

Assume a hypothetical primitive positive ordinary accelerated cycle has full counts `(gA,gL)` and is rooted at its least odd state `m`.

Write

`3 y_j+1 = 2^(a_j) y_(j+1)`, `a_j>=1`,

and

`S_j=a_0+...+a_(j-1)`,
`b_j=floor(Aj/L)`,
`h_j=b_j-S_j`,
`q_j=2^(S_j)/3^j`,
`rho_j=2^(b_j)/3^j`.

Then

`q_j=rho_j 2^(-h_j)`                                      (2.1)

and the inherited physical inequalities are

`q_j y_j > m`,                                             (2.2)

`q_j y_j < exp(g Delta)m`.                                (2.3)

Put

`epsilon=Delta/log(2)`,
`theta=L epsilon`,
`r_j=S_j L-jA`.

For a physically positive prefix,

`0<r_j+j epsilon<g theta`.                                (2.4)

---

## 3. RL136.1 — terminal localization of `h=-1`

Suppose `h_j=-1`.

From (2.1),

`q_j=2 rho_j`.

The inherited mechanical estimate gives

`rho_j>(1/2)exp(j Delta/L)`,

so

`q_j>exp(j Delta/L)`.                                     (3.1)

Combining (3.1) with the physical complementary inequality (2.3),

`y_j < exp((g-j/L)Delta)m`.                               (3.2)

This is an owned physical height bound. It depends on the actual least state and the actual affine cycle.

### 3.1 A terminal no-negative zone

Because `h_j=-1`, its discrepancy is positive and the determinant is a positive integer. Thus `r_j>=1`. Equation (2.4) gives the stronger phase-sensitive inequality

`r_j < (g-j/L)theta`.                                     (3.3)

Therefore every negative phase satisfies

`(g-j/L)theta>1`.                                         (3.4)

RL135 already certifies `5 theta<1`. Hence a negative phase requires **strictly more than five reduced blocks to remain**. The final five full reduced blocks are automatically nonnegative-defect territory.

### 3.2 Isolation threshold

The exact RL136 verifier certifies

`320,125,202,432 Delta < log(4/3)`                         (3.5)

while the same rigorous endpoint inequality fails at the next integer.

Put

`G_iso=320,125,202,432`.

If a negative phase satisfies

`g-j/L <= G_iso`,                                         (3.6)

then (3.2) gives

`m <= y_j < 4m/3`.                                        (3.7)

The verifier also certifies

`G_iso theta < A-L`.                                      (3.8)

For `h_j=-1`, write `t=jA mod L`, so `r_j=L-t`. The mechanical increment

`c_j=b_(j+1)-b_j`

is `2` exactly when `r_j<=A-L`. By (3.3), (3.6), and (3.8), every phase under consideration has

`c_j=2`.                                                   (3.9)

If `a_j>=2`, then

`y_(j+1)=(3y_j+1)/2^(a_j) <= (3y_j+1)/4`.

Since `y_j<4m/3`, integrality gives `3y_j+1<=4m`, so `y_(j+1)<=m`. A proper return to `m` contradicts primitivity and a value below `m` contradicts least-state ownership. Therefore

`a_j=1`.                                                   (3.10)

The defect recurrence gives

`h_(j+1)=h_j+c_j-a_j=-1+2-1=0`.                           (3.11)

### Theorem RL136.1

Every physical `h=-1` phase with at most `G_iso` reduced-block units remaining exits immediately to `h=0`. In particular, for every

`1<=g<=320,125,202,432`,

every negative defect phase is a one-phase isolated excursion.

Classification: **analytic ordinary-owned theorem + exact rational-log endpoint certificate**.

This is stronger than the inherited statement `h>=-1`: through more than 320 billion multiplicities, the path cannot remain on the negative level for two consecutive phases.

---

## 4. RL136.2 — owned three-fibre signature of an isolated excursion

Let `h_j=-1` be an isolated negative phase in the RL136.1 range.

### 4.1 Negative state: mod 4 fibre

RL136.1 gives `a_j=1`. Exact accelerated valuation therefore means

`v_2(3y_j+1)=1`,

so

`y_j == 3 (mod 4)`.                                       (4.1)

Together with (3.7), each negative excursion is an actual odd physical state in the narrow band

`m <= y_j < 4m/3`.                                        (4.2)

The least state itself also has first accelerated exponent one in any nontrivial positive cycle, hence `m==3 (mod 4)`. Distinct negative states are consequently separated from one another, and from `m`, in steps divisible by four.

### 4.2 Exit state: mod 3 fibre

With `a_j=1`,

`y_(j+1)=(3y_j+1)/2`.

Since both accelerated states are odd,

`y_(j+1)+1 = 3(y_j+1)/2`,

hence

`y_(j+1) == -1 (mod 3)`.                                  (4.3)

The exit states are odd, so in ordinary integer spacing they occupy one class modulo six. Also (4.2) gives

`(3m+1)/2 < y_(j+1) < 2m`.                                (4.4)

### 4.3 Entry boundary: dyadic fibre

Because the negative phase is isolated, let

`H=h_(j-1)>=0`,
`c=b_j-b_(j-1) in {1,2}`.

The defect recurrence at entry is

`-1 = H+c-a_(j-1)`,

so

`a_(j-1)=H+c+1`.                                          (4.5)

Let `z` be the actual ordinary shortcut state immediately after the odd step from `y_(j-1)`. The remaining `a_(j-1)-1` halvings take `z` to `y_j`, so

`z=2^(H+c)y_j`.                                           (4.6)

Thus the entry boundary lies in the actual dyadic fibre

`2^(H+c) | z`.                                             (4.7)

If `E_d` isolated excursions have entry depth `H+c>=d`, their distinct physical entry-boundary states are distinct multiples of `2^d`. By the inherited RL122 physical-fibre argument,

`W >= (E_d-1)2^d+1`.                                      (4.8)

### Theorem RL136.2

An isolated negative excursion has a linked **dyadic-entry / mod-4 near-minimum / mod-3 exit** physical signature. Equation (4.8) is an owned packing bridge from defect-excursion statistics to the global physical width.

Classification: **analytic ordinary-owned physical corollary**.

This is not merely the determinant lattice. Candidate count pairs do not acquire (4.1)--(4.8) unless they are actual phases of an assumed ordinary cycle.

---

## 5. RL136.3 — triangular exceptional-shell population

RL135 used the coarse bound `P<g^2 theta` for the number `P` of `h=-1` phases. The exact translate inequality is substantially sharper.

Fix a positive determinant `r`. Let its unique base phase be

`0<j_r<L`,

and write every translate as

`j=j_r+kL`, `0<=k<=g-1`.

Equation (2.4) becomes

`r + (j_r/L+k)theta < g theta`.                            (5.1)

Therefore the number `N_r` of physically possible `h=-1` translates in determinant shell `r` satisfies

`N_r <= g-floor(r/theta)`.                                 (5.2)

Only integers `1<=r<g theta` can occur. Hence

### Theorem RL136.3

`P(g) <= sum_(1<=r<g theta) (g-floor(r/theta))`.            (5.3)

Classification: **analytic lattice consequence of the owned positive-prefix strip**.

The right side is triangular: high determinant shells enter late and possess fewer translates. For exact state estimation, the verifier replaces the true `theta` by a rigorous upper enclosure and uses `floor(x)>=x-1`, yielding the convenient continuous envelope

`P(g) < theta_hi (g+1)^2/2`.                               (5.4)

This is approximately half of the old rectangular `g^2 theta` estimate in the mesoscopic regime.

---

## 6. RL136.4 — `m<2^75` through 56,336,298,016

Let

`R=sum_(r<L) rho_r`

be the inherited one-period mechanical weight. The exact block identity gives the baseline cancellation

`sum_(j<gL) rho_j = [(exp(gDelta)-1)/(exp(Delta)-1)] R`.    (6.1)

If `h_j>=0`, then `q_j<=rho_j`. At an `h=-1` phase,

`q_j=2rho_j`,

so the excess above the mechanical baseline is one additional `rho_j`. The physical prefix squeeze gives

`2rho_j=q_j<exp(gDelta)`,

hence each exceptional phase adds less than `exp(gDelta)/2`.

Using the cycle-closing identity,

`(exp(gDelta)-1)m=(1/3)sum q_j`,                           (6.2)

we obtain

`m < R/[3(exp(Delta)-1)]
     + P(g) exp(gDelta)/[6(exp(gDelta)-1)]`.               (6.3)

The first term is bounded by the inherited RL134/RL135 exact rational envelope `M_base`.

For the second term use (5.4) together with the rigorous monotone bounds

`exp(gDelta) <= 1/(1-g Delta_hi)`,
`exp(gDelta)-1 > g Delta_lo`.                              (6.4)

This gives the monotone certified envelope

`m < M_base
   + theta_hi (g+1)^2 /
     [12 g Delta_lo (1-g Delta_hi)]`.                      (6.5)

The RL136 exact verifier certifies

`m<2^75`

at

`g=56,336,298,016`,                                       (6.6)

and certifies that this same monotone envelope is no longer below `2^75` at

`g=56,336,298,017`.                                       (6.7)

Because `(g+1)^2/g=g+2+1/g` is nondecreasing for `g>=1` and `1/(1-gDelta_hi)` is increasing on the certified range, (6.5) is monotone. Thus (6.6) is a **contiguous through-`g` theorem**, not a pointwise check.

### Theorem RL136.4

Every hypothetical realization of the first reduced survivor with

`1<=g<=56,336,298,016`

has least odd state

`m<2^75`.

Classification: **analytic physical inequality + exact rational interval certificate**.

No external least-cycle floor is used. This improves RL135's `28,000,000,000` endpoint by slightly more than a factor of two.

---

## 7. RL136.5 — low-shell and last-translate physical windows

For any realized `h=-1` phase with discrepancy `delta_j`, (2.3) gives

`y_j < exp(gDelta-delta_j)m`.                              (7.1)

### Determinant +1 through `g=16`

RL134/RL135 certify

`6Delta<d_(+1)<7Delta`.

For every determinant `+1` translate through `g=16`, the slack in (7.1) is less than `10Delta`. With RL136.4's `m<2^75`, the verifier certifies

`y_j-m < 339,502,211,350`.                                 (7.2)

### Determinant +2 through `g=16`

RL135 certifies

`11Delta<d_(+2)<12Delta`.

Hence through `g=16` the slack is less than `5Delta`, and

`y_j-m < 169,751,105,674`.                                 (7.3)

### Last admissible translate in any positive shell

For a fixed positive determinant shell, let `k` be its last admissible translate. By definition the remaining discrepancy slack is at most one `Delta`. Therefore, throughout the RL136.4 range,

`y_j-m < (exp(Delta)-1)2^75
       < 33,950,221,135`.                                  (7.4)

These are conditional-on-realization physical windows; no shell occurrence is inferred.

Classification: **analytic physical band + exact arithmetic**.

---

## 8. Priority-A contact/no-contact attack for `g<=6`

RL135 proves `h_j>=0` for every proper prefix when `g<=6`.

At the repeated reduced block markers define

`H_t=h_(tL)`, `0<=t<=g`.

Then `H_0=H_g=0`.

- a canonical contact occurs exactly when some internal `H_t=0`;
- the no-contact branch has every internal `H_t>=1`.

This converts Priority A into a rooted rational-Dyck return problem over repeated mechanical blocks. It is useful bookkeeping, but it does **not** by itself control the complete family of length-`s` sliding windows required by RL123.5.

The canonical-contact numerator difference was red-teamed again: without a new support/spacing input it reduces to the inherited ownership identity `S=D_full(y-m)`. It is not promoted as a new obstruction.

The no-contact marker inequalities likewise constrain only anchored repeated-block positions. They do not provide a global `L1` sliding-window dispersion bound and therefore do not trigger the radius-three engine.

Status: **live structural dichotomy, but no closure**.

---

## 9. Red teams

### RL20 fake-model discriminator — PASS

RL136.1, RL136.2, RL136.4, and RL136.5 use actual least-state inequalities and actual affine cycle states. A fixed-content fake word does not acquire these premises merely from its counts.

### RL79 generalized-increment discriminator — PASS

The decisive isolation step uses the ordinary recurrence `3y+1=2^a y'`. For generalized increment `s`, the estimate after `a>=2` becomes `(3y+s)/4`; the ordinary `4m/3` contradiction does not survive unchanged as `s` scales. The dyadic/triadic fibres also take the inherited generalized form, while the numerator ceiling scales with `|s|`. No generalized increment is cancelled.

### RL81 physical-versus-quotient — PASS

Every state in RL136.1, RL136.2, and RL136.5 is an actual state of the assumed primitive ordinary cycle. Candidate determinant positions are never promoted to physical states without realization.

### Primitivity — PASS / load-bearing

Primitivity is used when the isolation argument rules out a premature return to the least state and when distinct excursion entries/exits are used as distinct physical states.

### External provenance — PASS

RL136.1--RL136.5 do not use the inherited external `R#>=2^71`. The externally conditional frontier remains inherited only.

### RL110 sparse-support barrier — PASS

No conclusion is drawn from `S=D(x'-x)` alone. The new fibre statement is produced directly from legal ordinary-run ownership around a physically realized defect excursion.

### Closure scope — PASS

No multiplicity is excluded. No `L` frontier is advanced. Gate A and Gate B remain open. Global nontrivial-cycle exclusion and Collatz remain open.

---

## 10. Correction/demotion ledger

No inherited theorem is demoted.

One attempted strengthening is explicitly **not promoted**:

- isolation/packing does not imply that an `h=-1` excursion exists. The branch `P(g)=0` remains logically possible under the inherited inequalities.

The RL123 global sliding-window route remains blocked because the present rooted defect data do not supply global window dispersion.

---

## 11. Strategic consequence

RL135 said that the path can dip at most one unit below the mechanical floor over an enormous multiplicity range. RL136 now shows that, through more than 320 billion multiplicities, such a dip is not a free lattice event: it is a single physical excursion carrying a linked dyadic-entry, mod-4 near-minimum, and mod-3 exit signature.

At the same time, the determinant-strip population is triangular rather than rectangular, extending the internal `m<2^75` range to `56,336,298,016`.

The live obstruction is therefore sharper:

> **Either force a nonzero/large population of these owned excursions and consume their fibres, or prove that the no-negative branch itself has enough repeated-block/sliding-window rigidity to trigger an existing global obstruction.**

That is the RL137 target.

# RL151 — nonlocal successor-mass ownership coupling

Date: 2026-08-28

## 0. Outcome and classification

RL151 starts from the verified RL150 local multi-excursion independence barrier.
It does **not** reopen local shell/depth or concatenation arguments.

Within the inherited RL136 isolation range

`1 <= g <= 320,125,202,432`,

RL151 proves a genuinely global ordinary-owned coupling among all realised
negative excursions:

1. **RL151.1 — successor-mass budget.** If `J={j:h_j=-1}`, and
   `Q_- = sum_(j in J) q_j`, `Q_+ = sum_(j notin J) q_j`, then

   `Q_+ >= (2/3) Q_-`, hence `Q_- <= (3/5)(Q_-+Q_+)`.

   This couples all realised negative excursions through the one shared
   full-cycle affine mass budget. It is not supplied by the RL150 separated
   local templates.

2. **RL151.2 — multiplicity-independent least-state ceiling.** In the same
   range,

   `m <= (10/7) R/[3(exp(Delta)-1)]`

   and the inherited rigorous logarithm/rho enclosure certifies

   `m < 52,568,258,083,959,326,340,410 < 2^76`.

   This tightens the inherited broad one-defect `m<2^76` envelope over the
   entire RL136 isolated range. It does not reach `2^75` uniformly.

3. **RL151.3 — reciprocal-depth ownership identity.** If an isolated
   negative excursion at `j` has exact entry depth `d_j=H_j+c_j`, then

   `q_(j-1) = 3 q_j / 2^(d_j+1)`.

   Thus the predecessor mass attached to the whole excursion population is
   an inverse-depth weighted sum. RL149 shows current local resources cannot
   lower-bound that inverse-depth mass, so no unsupported conversion to the
   RL148 direct-depth packing bound is claimed.

No multiplicity is excluded. The primitive ordinary frontiers are unchanged.
Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.

Classification: **analytic ordinary-owned global coupling and corollaries +
exact rational constant certificate; no branch closure**.

---

## 1. Incoming authority and verification economy

Incoming authoritative commit:

`79a41e4710f5776b48aa8cc313c39a4ed46b6c7f`.

The RL150 incoming sidecar, manifest, and fast verifier are frozen as passed.
Verification economy is applied; no historical expensive certificate is
rerun.

Load-bearing inherited results are:

- RL135: for `g<=771,316,334,039`, every proper prefix has `h_j>=-1`;
- RL136: for `g<=320,125,202,432`, every `h_j=-1` phase is isolated,
  has `a_j=1`, and exits to `h_(j+1)=0`;
- RL136/RL148: realised negative excursions are actual ordinary physical
  states and carry the owned entry/negative/exit fibres;
- RL137: the all-nonnegative branch has the baseline multiplicity-independent
  ceiling `R/[3(exp(Delta)-1)]<2^75`;
- RL149: determinant shell does not control exact entry depth using the
  inherited local recurrence and prefix squeeze;
- RL150: separated local excursion templates do not manufacture a
  cross-excursion cyclic relation.

The present argument adds a full-cycle aggregate relation; it does not
contradict RL150.

---

## 2. Notation and the full-ownership mass

Assume a hypothetical primitive positive ordinary accelerated cycle with full
counts `(gA,gL)`, rooted at its least odd state `m`. Put `N=gL` and

`3 y_j+1 = 2^(a_j) y_(j+1)`, `a_j>=1`,

`S_j=a_0+...+a_(j-1)`,

`q_j=2^(S_j)/3^j`,

`rho_j=2^(floor(Aj/L))/3^j`,

`h_j=floor(Aj/L)-S_j`.

Then

`q_j=rho_j 2^(-h_j)`.

The ordinary affine recurrence also gives the exact owned increment identity

`q_(j+1) y_(j+1) = q_j y_j + q_j/3`.                       (2.1)

Hence, over the full cycle,

`Q := sum_(j=0)^(N-1) q_j
   = 3(exp(g Delta)-1)m`.                                  (2.2)

Let

`R_g := sum_(j=0)^(N-1) rho_j`.

Exact mechanical block repetition gives

`R_g = [(exp(g Delta)-1)/(exp(Delta)-1)] R`,                (2.3)

where `R=sum_(r=0)^(L-1) rho_r`.

Equations (2.1)--(2.3) are the shared full-ownership budget unavailable to
the RL150 independent local templates.

---

## 3. RL151.1 — successor-mass budget

Assume `g<=320,125,202,432`, and let

`J={j: h_j=-1}`.

RL136 isolation gives, for every `j in J`,

`a_j=1`, `h_(j+1)=0`.

Therefore

`q_(j+1) = (2/3) q_j`.                                     (3.1)

Different negative phases have different successors, and every such
successor lies outside `J`. Therefore, with

`Q_- = sum_(j in J) q_j`,
`Q_+ = sum_(j notin J) q_j`,

we have

`Q_+ >= sum_(j in J) q_(j+1)
     = (2/3) Q_-`.                                         (3.2)

Consequently

`Q_- <= (3/5) Q`,                                          (3.3)

where `Q=Q_-+Q_+`.

### Theorem RL151.1

Across the whole isolated-negative range, all realised negative excursions
jointly occupy at most three fifths of the actual affine `q`-mass.

This is a **global aggregate relation**. Local recurrence still permits the
RL150 separated templates; what changes here is that all realised templates
must compete for one owned cycle-closing mass budget.

---

## 4. RL151.2 — uniform least-state ceiling

For `j notin J`, `h_j>=0`, hence `q_j<=rho_j`. For `j in J`,
`h_j=-1`, hence `q_j=2rho_j`. Thus

`Q <= R_g + sum_(j in J) rho_j
   = R_g + Q_-/2`.                                         (4.1)

Using (3.3),

`Q <= R_g + 3Q/10`,

so

`Q <= (10/7) R_g`.                                         (4.2)

Combine (2.2), (2.3), and (4.2). The common factor
`exp(g Delta)-1` cancels exactly:

`m <= (10/7) R/[3(exp(Delta)-1)].`                         (4.3)

The exact RL151 verifier reuses the inherited rigorous atanh-series
logarithm enclosure and the RL134/RL135 one-period rho envelope. It certifies

`R < 99,205,514,478`

and, using `exp(Delta)-1 > Delta`,

`m < 52,568,258,083,959,326,340,410`.                      (4.4)

This is below `2^76` but above `2^75`; it is a state ceiling, not a
contradiction.

Compared with the elementary `h>=-1` estimate `q_j<=2rho_j`, the coefficient
improves from `2` times the mechanical baseline to `10/7`, a factor `5/7`.

---

## 5. Population and exact-depth corollaries

### 5.1 Global excursion-population upper bound

RL136 gives, at every negative phase,

`m < q_j y_j`
and
`y_j < 4m/3`.

Hence

`q_j > 3/4`.                                                (5.1)

If `P=|J|`, then

`(3/4)P < Q_- <= (3/5)Q`.

Using (2.2),

`P < (12/5)(exp(g Delta)-1)m`.                             (5.2)

This is a genuine full-cycle population upper bound. It does not force
`P>0` and it does not provide an exact-depth population lower bound.

### 5.2 Reciprocal-depth ownership identity

Let an isolated negative excursion at `j` have predecessor height
`H_j>=0`, mechanical increment `c_j in {1,2}`, and exact entry depth

`d_j=H_j+c_j`.

RL136 gives

`a_(j-1)=d_j+1`.

Since `q_j/q_(j-1)=2^(a_(j-1))/3`,

`q_(j-1)=3q_j/2^(d_j+1)`.                                 (5.3)

Therefore the predecessor mass over all realised excursions is exactly

`sum_(j in J) q_(j-1)
 = (3/2) sum_(j in J) q_j 2^(-d_j)`.                       (5.4)

The predecessor indices are physical and distinct. However, RL149 proves
that the inherited local shell/prefix resources leave `d_j` free. Thus
(5.4) supplies an inverse-depth weighted object, while RL148 physical packing
becomes stronger with positive powers of depth. No lower bound converting
(5.4) into the required direct-depth mass is presently available.

A further tempting strengthening is explicitly rejected: a nonnegative
phase can be both the successor of one negative excursion and the predecessor
of the next when the negative phases are two indices apart. Successor and
predecessor masses therefore cannot be added as disjoint resources.

---

## 6. Red teams

### RL20 fake-model discriminator — PASS

The decisive equations (2.2) and (4.3) use the actual ordinary affine
cycle-closing identity rooted at the physical least state. A fixed-content
local template does not acquire this premise.

### RL79 generalized-increment discriminator — PASS

The isolation input `a_j=1` is the ordinary `+1` result of RL136 and is
load-bearing in the exact successor ratio (3.1). No generalized-increment
claim is made.

### RL81 physical-versus-quotient — PASS

`J`, its successors, predecessors, `q_j`, and the cycle-closing mass all
refer to actual phases of the assumed ordinary cycle.

### Primitivity — PASS / inherited

The argument retains the primitive least-state setting used by RL136 and
RL137. It does not manufacture a realised excursion from a candidate
determinant position.

### Double-counting red team — PASS

Only the successor set is used to prove (3.2). Entry predecessors are not
added to successor mass because those sets can overlap.

### External provenance — PASS

No external least-cycle floor is used in RL151.1--RL151.3 or the numerical
ceiling (4.4).

### Closure scope — PASS

No multiplicity is excluded and no frontier advances. Gate A and Gate B
remain open. Global non-trivial-cycle exclusion and Collatz remain open.

---

## 7. Strategic consequence

RL150 showed that two isolated local templates can coexist without a local
cross-excursion law. RL151 supplies the missing relation at the correct
level: realised excursions are globally coupled because their mandatory
`2/3` successors consume one shared affine ownership mass.

That coupling is quantitatively useful: it improves the broad isolated-range
least-state ceiling from the inherited one-defect factor `2` to `10/7` of
the mechanical baseline. But it still does not close the branch.

The remaining negative-defect obstruction is now more specific:

> Convert the reciprocal-depth ownership mass (5.4), or another genuinely
> global ownership quantity, into a lower bound that can be paired with the
> RL148 positive-depth physical packing. If no such conversion exists without
> reintroducing the RL149/RL150 local independence barriers, pivot away from
> the negative-defect branch.

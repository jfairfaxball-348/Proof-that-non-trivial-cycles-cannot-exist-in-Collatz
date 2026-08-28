# RL152 — global depth budget and reciprocal-width bridge

Date: 2026-08-28

## 0. Outcome and classification

RL152 starts from the verified RL151 successor-mass coupling and attacks the
requested depth-weighted ownership bridge without reopening the RL149 local
shell/depth route or the RL150 separated-template route.

Within the inherited RL136 isolation range

`1 <= g <= 320,125,202,432`,

RL152 proves three genuinely global ordinary-owned interfaces for the realised
negative-excursion population.

1. **RL152.1 — full-cycle entry-depth budget.** If `J={j:h_j=-1}` and an
   isolated negative excursion at `j` has exact entry depth `d_j`, then

   `sum_(j in J) d_j <= g(A-L)`.

   For the current reduced survivor,

   `A-L = 80,448,749,305`.

   This is a full-cycle content budget: each depth is exactly the number of
   ordinary even shortcut steps consumed by the accelerated predecessor
   transition.

2. **RL152.2 — reciprocal ownership lower bound.** Put

   `Q_- = sum_(j in J) q_j`,
   `M_- = sum_(j in J) q_j 2^(-d_j)`.

   Every realised negative excursion satisfies

   `3/4 < q_j < 4/3`.

   If `J` is nonempty, weighted Jensen therefore gives

   `M_- > Q_- 2^(-4g(A-L)/(3Q_-))`.

   Equivalently, RL151's total predecessor ownership mass

   `Q_pre = sum_(j in J) q_(j-1) = (3/2) M_-`

   obeys the corresponding positive but population-sensitive lower bound.

3. **RL152.3 — reciprocal ownership to physical width.** Let `W` be the
   physical ordinary-shortcut cycle width and let `E_d` be the number of
   realised isolated negative excursions of exact depth `d`. RL148 gives

   `W >= (E_d-1)2^(d+2)+1`

   for every exact-depth stratum. Summing the reciprocally weighted
   consequences over all depths gives

   `W >= 12 sum_(d>=1) E_d 2^(-d) - 11`.

   Since `q_j<4/3`,

   `W > 9 M_- - 11`

   and hence, using RL151's exact predecessor identity,

   `W > 6 Q_pre - 11`.

   Thus the reciprocal-depth ownership object from RL151 is now consumed
   directly by the positive-depth physical fibre theorem from RL148.

These results close the **missing bridge**, but they do not close the
negative-defect branch. The remaining dependency is occurrence/concentration:
the inherited theory gives no nontrivial lower bound on `Q_-`, on the negative
population, or on repeated exact-depth strata. A singleton-depth distribution
is compatible with all promoted bridge inequalities and can make the new
width bound no stronger than the baseline `W>=1`.

Accordingly RL152 freezes the present negative-defect dependency frontier and
pivots RL153 to the independent `g=1` primitive-owner branch.

No multiplicity is excluded. Gate A and Gate B remain open. Global nontrivial
cycle exclusion and the Collatz conjecture remain open.

Classification: **analytic ordinary-owned global bridge + exact arithmetic
sanity certificate + explicit method barrier / branch pivot; no new exclusion**.

---

## 1. Incoming authority and verification economy

Incoming authoritative commit:

`ed10318593e9a79c65988253c27ee6c211bb0ac2`.

The committed RL151 outer sidecar, fresh-unpack record, internal manifest, and
fast verifier are frozen as passed. The RL151 fast verifier was independently
reproduced before new mathematics began. Verification economy is applied; no
historical expensive certificate is rerun.

Load-bearing inherited results are:

- RL135: every proper prefix has `h_j>=-1` through
  `g=771,316,334,039`, and in particular `h_j>=0` through `g<=6`;
- RL136: through `g=320,125,202,432`, every negative phase is an actual
  isolated excursion with `a_j=1`, with an actual ordinary entry fibre;
- RL136: for every negative phase, `q_j y_j>m`,
  `q_j y_j<exp(g Delta)m`, and `y_j<4m/3`;
- RL148: exact-depth realised entry boundaries occupy one residue class modulo
  `2^(d+2)`, giving the exact-depth width bound;
- RL149: the inherited local determinant shell and prefix squeeze do not
  control exact entry depth;
- RL150: separated local excursion templates do not manufacture a nonlocal
  cyclic relation;
- RL151: `Q_-<=3Q/5` and
  `q_(j-1)=3q_j/2^(d_j+1)` for every realised isolated excursion;
- RL122: `W` denotes the width of the actual ordinary shortcut cycle, so the
  RL148 entry-boundary states and the global physical width are in the same
  owned state space.

No external least-cycle floor is used.

---

## 2. Notation

Assume a hypothetical primitive positive ordinary accelerated cycle has full
counts `(gA,gL)`, rooted at its least odd state `m`. Write

`3 y_j+1 = 2^(a_j) y_(j+1)`,  `a_j>=1`,

`S_j=a_0+...+a_(j-1)`,

`q_j=2^(S_j)/3^j`,

`h_j=floor(Aj/L)-S_j`.

Let

`J={j:h_j=-1}`,  `P=|J|`.

For `j in J`, RL136 isolation gives an exact entry depth

`d_j = a_(j-1)-1 >= 1`.

Let `E_d` be the number of `j in J` with `d_j=d`.

Define the reciprocal count and ownership moments

`T_- = sum_(j in J) 2^(-d_j) = sum_(d>=1) E_d 2^(-d)`,

`M_- = sum_(j in J) q_j 2^(-d_j)`.

RL151 gives

`Q_pre := sum_(j in J) q_(j-1) = (3/2) M_-`.             (2.1)

Finally, let

`Z_0=A-L=80,448,749,305`.

For the full multiplicity-`g` accelerated cycle,

`sum_i (a_i-1) = gA-gL = gZ_0`.                           (2.2)

The left side is exactly the total number of ordinary even shortcut steps
compressed into the accelerated transitions.

---

## 3. RL152.1 — full-cycle entry-depth budget

Every negative excursion at `j` uses the predecessor accelerated transition
`j-1 -> j`, and

`d_j=a_(j-1)-1`.

Different negative indices have different predecessor indices. Hence their
depth contributions are a sub-sum of the nonnegative terms in (2.2):

`sum_(j in J) d_j
 = sum_(j in J) (a_(j-1)-1)
 <= sum_i (a_i-1)
 = gZ_0`.                                                  (3.1)

### Theorem RL152.1

Across all realised isolated negative excursions,

`sum_(j in J) d_j <= 80,448,749,305 g`.                    (3.2)

This is global ordinary ownership. It does not refer to determinant shells,
candidate positions, or concatenated local templates.

A useful count form follows from AM-GM. If `P>0`,

`T_-/P
 >= (prod_(j in J) 2^(-d_j))^(1/P)
 = 2^(-(sum d_j)/P)
 >= 2^(-gZ_0/P)`,                                         (3.3)

so

`T_- >= P 2^(-gZ_0/P)`.                                   (3.4)

The dependence on `P` is essential.

---

## 4. RL152.2 — reciprocal ownership lower bound

RL151 already supplied `q_j>3/4` at every negative phase.

For the upper side, the inherited physical prefix squeeze gives

`q_j y_j < exp(g Delta)m`.

Every cycle state satisfies `y_j>=m`, while the RL136 isolation certificate
gives

`g Delta < log(4/3)`

through the whole present range. Therefore

`q_j < exp(g Delta) < 4/3`.                               (4.1)

Thus

`3/4 < q_j < 4/3`                                         (4.2)

for every realised negative excursion.

Let

`Q_- = sum_(j in J) q_j`.

For `Q_->0`, use weights `w_j=q_j/Q_-`. The function
`x -> 2^(-x)` is convex, so weighted Jensen gives

`M_-/Q_-
 = sum w_j 2^(-d_j)
 >= 2^(-sum w_j d_j)`.                                    (4.3)

By (4.1) and (3.1),

`sum_(j in J) q_j d_j
 < (4/3) sum_(j in J) d_j
 <= (4/3)gZ_0`.                                            (4.4)

Combining (4.3)--(4.4),

`M_- > Q_- 2^(-4gZ_0/(3Q_-))`.                            (4.5)

Using (2.1),

`Q_pre > (3/2) Q_- 2^(-4gZ_0/(3Q_-))`.                    (4.6)

### Theorem RL152.2

The reciprocal-depth ownership mass has a genuine global lower bound once the
actual negative mass is specified. The missing datum is no longer depth
control by itself; it is a nontrivial lower bound on the amount of negative
mass/population that must exist.

This theorem does not reverse RL151's `Q_-<=3Q/5`, which is an upper bound.

---

## 5. RL152.3 — consume RL148 into a reciprocal-width bridge

RL148 proves, for each exact depth `d>=1`,

`W >= (E_d-1)2^(d+2)+1`.                                  (5.1)

Rearrange:

`E_d <= 1 + (W-1)/2^(d+2)`.                               (5.2)

Multiply by `2^(-d)` and sum over all `d>=1`:

`T_-
 <= sum_(d>=1) 2^(-d)
  + (W-1) sum_(d>=1) 2^(-2d-2)`.                          (5.3)

The geometric sums are exact:

`sum_(d>=1)2^(-d)=1`,

`sum_(d>=1)2^(-2d-2)=1/12`.

Therefore

`T_- <= 1 + (W-1)/12`,                                    (5.4)

or equivalently

`W >= 12T_- - 11`.                                        (5.5)

By (4.1),

`M_- < (4/3)T_-`, hence `T_->(3/4)M_-`. Therefore

`W > 9M_- - 11`.                                          (5.6)

Using the RL151 predecessor identity (2.1),

`W > 6Q_pre - 11`.                                        (5.7)

### Theorem RL152.3

RL151's inverse-depth predecessor ownership mass now has a direct
ordinary-physical consumer: it forces physical cycle width through the RL148
exact-depth fibres.

Combining (4.5) and (5.6) gives the fully global conditional inequality

`W > 9 Q_- 2^(-4gZ_0/(3Q_-)) - 11`.                       (5.8)

Alternatively (3.4) and (5.5) give, for `P>0`,

`W >= 12P 2^(-gZ_0/P) - 11`.                              (5.9)

These are genuine bridge inequalities, not branch exclusions.

---

## 6. Why the bridge does not close the branch

The bridge loses force when the negative population is sparse or spread over
distinct depths. The current frozen theory has no theorem forcing `P`, `Q_-`,
or any exact-depth multiplicity to be large.

A sharp abstract compatibility witness for the promoted inequalities is:

`E_d=1` for `1<=d<=P`, and `E_d=0` otherwise.

This is **not** asserted to be a physical cycle. It only tests what the
present inequalities themselves can exclude.

For this distribution,

`sum d E_d = P(P+1)/2`,

`T_-=1-2^(-P)`,

while every individual RL148 stratum has `E_d-1=0`, so it forces only
`W>=1`. The aggregate bridge gives

`W >= 1-12*2^(-P)`,                                       (6.1)

which is no stronger than the physical baseline.

Already at `g=1`, the global depth budget permits this singleton-depth pattern
for every

`P<=401,119`,

because

`401,119*401,120/2 = 80,448,426,640
 <= 80,448,749,305 = Z_0`.                                (6.2)

Again, this is an inequality-level evasion witness, not computational evidence
for a cycle.

Therefore a further attack on this branch requires a genuinely new theorem of
one of the following kinds:

- negative-excursion occurrence with a quantitative population or mass floor;
- exact-depth concentration/repetition;
- another global ownership law that prevents singleton-depth dispersion.

RL149 rules out obtaining this from the inherited local shell/prefix
interface, and RL150 rules out obtaining it by merely concatenating separated
local templates. Repeating either route would not be productive.

The negative-defect dependency frontier is therefore frozen here pending such
a new input.

---

## 7. Red teams

### RL149 shell/depth independence — PASS

The depth budget is the exact full-cycle identity
`sum_i(a_i-1)=g(A-L)` restricted to realised predecessor transitions. No
determinant shell is mapped to a depth.

### RL150 separated-template barrier — PASS

No relation is inferred by concatenating local excursion templates. The new
relations use full-cycle content ownership and global physical width.

### Physical-versus-mechanical ownership — PASS

`J`, `d_j`, the predecessor transitions, the RL148 entry boundaries, and `W`
all refer to actual states/transitions in the assumed ordinary cycle.
Mechanically admissible candidates are not counted as realised excursions.

### Double counting — PASS

The proof never adds successor mass and predecessor mass as disjoint
resources. The depth budget counts distinct predecessor transitions, while
the width bridge counts actual entry-boundary fibres.

### Fake-model / generalized-increment discriminator — PASS

The full even-step budget and the RL148 ordinary entry fibres are specific to
the ordinary `+1` owner. No fixed-content fake template or generalized
increment is promoted as satisfying them.

### External provenance — PASS

No external least-cycle floor is used.

### Scope — PASS

No multiplicity is excluded. Gate A/B, global nontrivial-cycle exclusion, and
Collatz remain open.

---

## 8. Strategic consequence and pivot

RL152 resolves the interface asked for at kickoff:

> reciprocal-depth ownership can be converted into positive-depth physical
> packing.

The conversion is explicit: `W>6Q_pre-11`. The remaining obstruction is
upstream: current theory does not force enough negative ownership for that
width lower bound to become contradictory.

The next session should therefore not continue tuning the same negative-defect
depth inequalities. RL153 pivots to the independent `g=1` branch. This is
particularly clean because RL135 already gives `h_j>=0` for `g<=6`, so `g=1`
does not depend on the negative-excursion machinery, while RL146's successful
height-one closure explicitly required `g>1` and therefore left `g=1`
untouched.

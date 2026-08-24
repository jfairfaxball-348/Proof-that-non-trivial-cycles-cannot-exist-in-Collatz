# RL77 — Product/growth/continued-fraction full-phase scale coupling and lattice barrier

Date: 2026-08-24

## 0. Executive outcome

RL77 attacked the deliberate RL76 pivot:

# **Product / growth / continued fraction + modern full phase**

inside the retained RL64 one-excursion/full-phase architecture.

The incoming RL76 outer sidecar, internal manifest and fast verifier suite all pass. Under the verification-economy rule, the frozen RL76 proof-state ledger is retained.

RL77 does **not** close Gate A, Gate B, RL/nontrivial-cycle exclusion, or the Collatz conjecture. It does, however, produce three useful analytic upgrades and one decisive route diagnosis.

1. The RL19 odd-step product can be inserted directly into the RL64/RL65 half-cycle. This gives an **exact half-cycle product budget** and a full-phase-wide two-sided phase window:

   `5 - (8/27)(2/3)^r <= N(zeta-1) < 79N/[9(N-2)]`.

2. Combining the inherited RL73 continued-fraction gate with the modern phase window sharpens the first low-reduced-denominator branch: the surviving RL73 convergent cannot occur at any nontrivial gcd multiple. If the reduced pair is the RL73 survivor, then

   `g=gcd(a,ell)=1`,

   so the full exponents themselves are exactly

   `a=123,139,092,617,126,647,266`,

   `ell=77,692,117,359,936,589,403`.

   Thus the old “first convergent ray” collapses to a **single exponent pair**. The phase state is additionally localized to

   `2^71 <= N <= 2,578,333,030,765,879,156,036`,

   with `N==19 mod24`.

3. The canonical RL74/RL76 pump exponent vectors

   `c=101 : (length,weight)=(3,2)`,

   `c=10  : (length,weight)=(2,1)`

   form a unimodular basis of the exponent lattice. Writing

   `Sigma=2ell-a`, `Delta=2a-3ell`,

   gives exactly

   `a=3Sigma+2Delta`, `ell=2Sigma+Delta`,

   `gcd(Sigma,Delta)=gcd(a,ell)`,

   and

   `boxed: zeta=(8/9)^Sigma (4/3)^Delta`.

   Therefore the proposed “two-scale pump CF” using `8/9` and `4/3` is **not a new Diophantine dimension**. Without an independent bound on the residual context, it is a GL(2,Z) reparametrization of the original `2^a/3^ell` approximation.

4. RL76's physical scale normal form and the RL19 segment product combine to an exact **closed-pump product-excess law**. If a closed pump `c` with physical fixed point `alpha` is repeated `q` times from physical entry state `x`, then

   `boxed: Pi(c^q)-1 = alpha[(P/R)^q-1]/x`.

   Since a pump subproduct is bounded by the full half-cycle product budget, a deep positive `c=10` pump forces an exponentially large physical entry scale. But RL76 already shows precisely how the free integer scale parameter `m` supplies that scale. Hence the product theorem prices depth by **physical size**, not by a uniform contradiction.

The main strategic conclusion is therefore negative but precise:

> Modern full phase + product + generic continued fractions still leave the physical scale and complementary exponent context unbounded. The canonical `8/9` versus `4/3` two-scale idea collapses exactly to the original exponent lattice unless a new ownership theorem bounds the residual context.

This meets the RL77 stop criterion. The next session should pivot to the RL75 deliberate alternative:

# **D|Q-sensitive bounded-radius Gate-B reconnaissance**

rather than run another generic CF scan or another local Gate-A digit extension.

---

## 1. Frozen inherited state used

Retain exactly the RL76 ledger:

- radius-3 primitive/full-`D` local obstruction: closed;
- Gate A even terminal `k`: analytically impossible;
- Gate A `k<=25`: closed by exact finite-certificate corollary;
- first globally open terminal exponent: odd `k>=27`;
- every hypothetical odd `27<=k<=165` Gate-A violation has the RL73 giant post-first-mismatch height-one macro;
- RL76 closed-pump physical normal form and exact weight/scale conservation;
- RL76 determinant normal form `mM_q=K_ctx` for fixed context;
- RL76 proof that reciprocal/harmonic mass does not price `c=10` depth;
- RL75 primitive proper-pump nondegeneracy and `N==19 mod24`;
- Gate A globally open; Gate B globally open.

The full-phase half-word notation is:

- `a` = half-word length;
- `ell=r+3` = half-word weight;
- `M=2^a-3^ell>0`;
- `zeta=2^a/3^ell>1`;
- `v=111 y 0^(t+1)` with internal `y` of weight `r`;
- `V=Q(v)=19*3^r+8Q(y)`;
- phase states `N+4 --v--> N`;
- `N>=R0=2^71`, `N==19 mod24`;
- rank defect `mathcalD>=0`;
- terminal exponent `k`.

RL65 gives

`(N-2)M = 237*3^r - 12mathcalD - 2^(a-k+1)`.       (1.1)

RL73 gives

`zeta-1 < 79/[9(N-2)]`.                               (1.2)

---

## 2. The exact segment product identity

For any positive shortcut-Collatz segment with binary word `w`, let

- `n=|w|`;
- `s=wt(w)`;
- `P=2^n`, `R=3^s`;
- physical entry and exit states be `X,Y`.

At an even bit,

`X_(i+1)/X_i=1/2`.

At an odd bit,

`X_(i+1)/X_i=(3/2)(1+1/(3X_i))`.

Multiplying along the segment gives the exact identity

`boxed: Pi(w;X) := product_(odd bits)(1+1/(3X_i))`

`boxed: Pi(w;X) = (P/R)(Y/X).`                         (2.1)

Classification: **analytic identity**. This is the RL19 odd-step product in local segment form.

### 2.1 Full-phase half-cycle specialization

For the genuine full-phase half `v`,

`X=N+4`, `Y=N`, `P/R=zeta`.

Hence

`boxed: Pi_v = zeta N/(N+4).`                          (2.2)

The exact full-phase equation

`MN=V+4*3^ell`

is equivalent to

`2^a N = 3^ell(N+4)+V`.

Therefore

`boxed: Pi_v = 1 + V/[3^ell(N+4)].`                   (2.3)

This identifies the entire half-cycle product excess exactly with the normalized full-phase numerator `V`.

---

## 3. New theorem A — full-phase-wide two-sided product and phase window

Let the one-positions of `y` be

`0<=b_1<...<b_r`.

Then `b_j>=j-1`, so

`Q(y)=sum_j 2^(b_j)3^(r-j)`

`>= sum_j 2^(j-1)3^(r-j)`

`=3^r-2^r`.                                            (3.1)

Since

`V=19*3^r+8Q(y)`

and `3^ell=27*3^r`,

`V/3^ell >= 1 - (8/27)(2/3)^r`.                       (3.2)

Put

`epsilon_r=(8/27)(2/3)^r`.

Using (2.3),

`boxed: Pi_v-1 >= (1-epsilon_r)/(N+4).`               (3.3)

Since

`Pi_v-1=[N(zeta-1)-4]/(N+4)`,

we obtain

`boxed: zeta-1 >= [5-epsilon_r]/N.`                   (3.4)

Combining with RL73 gives the modern full-phase-wide window

`boxed:`

`[5-epsilon_r]/N <= zeta-1 < 79/[9(N-2)].`            (3.5)

Equivalently, for the logarithmic linear form

`Lambda=a log 2-ell log 3=log zeta`,

`boxed:`

`log(1+[5-epsilon_r]/N) <= Lambda < 79/[9(N-2)].`      (3.6)

The half-product excess itself has the exact upper bound

`boxed:`

`Pi_v-1 < (43N+72)/[9(N-2)(N+4)].`                    (3.7)

Indeed this is obtained by substituting RL73's upper phase squeeze into

`Pi_v-1=[N(zeta-1)-4]/(N+4)`.

Classification: **analytic synthesis**, using the RL19 product identity, RL64/RL65 full-word reconstruction, and the retained RL73 phase squeeze. The elementary lower numerator inequality is compatible with the older RL20 numerator/packing programme; the new point is the clean full-phase-wide splice into the modern RL64/RL65 architecture.

### 3.1 Terminal-`k` refinement

Dividing (1.1) by `3^ell` gives

`(N-2)(zeta-1)`

`=79/9 - 4mathcalD/3^(r+2) - 2^(1-k) zeta`.

Dropping only `mathcalD>=0` and solving for `zeta-1` yields

`boxed:`

`zeta-1 <= [79/9-2^(1-k)]/[N-2+2^(1-k)].`             (3.8)

This is exact but numerically only a tiny strengthening for `27<=k<=165`. It does not change the route decision.

---

## 4. New theorem B — reduced CF successor window

Write

`g=gcd(a,ell)`, `a=gp`, `ell=gq`, `gcd(p,q)=1`,

and

`beta=log_2 3`.

Then

`delta := p/q-beta = Lambda/[gq log(2)] >0`.             (4.1)

Define the Legendre scale

`T(g,N)=9g(N-2)log(2)/158`.                              (4.2)

If

`q<T(g,N)`,

then (3.6) implies

`delta<1/(2q^2)`,

so `p/q` is a continued-fraction convergent of `beta`.

Let `q_+` be the denominator of the next convergent. Standard consecutive-convergent bounds give

`1/[q(q+q_+)] < delta < 1/(q q_+)`.                   (4.3)

Combining (4.3) with the two sides of (3.6) yields

`boxed:`

`q_+ > 9g(N-2)log(2)/79 - q`,                            (4.4)

and

`boxed:`

`q_+ < g log(2) / log(1+[5-epsilon_r]/N).`               (4.5)

In particular, if `q<T(g,N)`, then (4.4) gives

`q_+>T(g,N)`.

So the full-phase data force a sharp dichotomy:

- either the reduced denominator already lies beyond the Legendre scale;
- or the reduced ratio is a genuine convergent whose **successor denominator is of order `gN`**.

Classification: **analytic CF consequence**. This is structurally stronger than a bare approximation statement, but still does not bound `gN`.

### Why this is not closure

Both `g` and `N` remain globally unbounded. Equations (4.4)–(4.5) therefore localize the next convergent relative to `gN` but do not make the convergent index finite globally.

This is precisely the failure mode anticipated in the RL75 route tournament: generic CF becomes useful only after a new RL-specific restriction controls `g`, `N`, or the complementary context.

---

## 5. New theorem C — the first RL73 convergent branch de-scales to one exponent pair

RL73 already certifies the universal reduced-denominator gate

`Q_gate=93,226,756,704,262,400,759`,

and the unique surviving above-`beta` convergent at or below that gate:

`p0=123,139,092,617,126,647,266`,

`q0= 77,692,117,359,936,589,403`.                     (5.1)

Let

`lambda0=p0 log(2)-q0 log(3)`.

The RL77 lightweight exact-arithmetic check gives

`lambda0 < 79/[9(R0-2)] < 2 lambda0`,                 (5.2)

with `R0=2^71`.

Suppose the reduced ratio is `p0/q0`. Then

`Lambda=g lambda0`.

Since `N>=R0`, RL73's upper phase squeeze gives

`g lambda0 < 79/[9(R0-2)] <2lambda0`.

Hence

`boxed: g=1.`                                         (5.3)

Therefore the entire low-reduced-denominator branch is not an infinite family of multiples. It is exactly one exponent pair:

`boxed: (a,ell)=(p0,q0).`                              (5.4)

Every other full-phase datum must have reduced denominator

`boxed: q>=93,226,756,704,262,400,760.`                (5.5)

This is a genuine strengthening of the inherited branch classification.

### 5.1 Phase-state localization on the exact pair

On (5.4), `Lambda=lambda0`. The upper phase squeeze implies

`N < 2 + 79/(9lambda0)`.

The exact numerical enclosure in the verifier gives

`2 + 79/(9lambda0)`

`=2578333030765879156036.3714...`.

Thus

`boxed:`

`2^71 <= N <= 2,578,333,030,765,879,156,036`,         (5.6)

and RL75 still gives

`boxed: N==19 (mod24).`                                (5.7)

The lower product window (3.5) gives a weaker lower bound than `2^71` on this exact pair, so it does not eliminate the survivor.

Classification: **analytic corollary + exact rational log-interval certificate**, consuming the already-frozen RL73 convergent scan rather than rerunning it.

### 5.2 Strategic meaning

The first branch is now maximally concrete, but not closed. It is essentially the historical safe-CF stress exponent pair. Re-entering the old fixed-survivor campaign without a new invariant would violate the RL77 stop rule.

---

## 6. New theorem D — canonical pump coordinates are a unimodular exponent basis

Define

`Sigma=2ell-a`,

`Delta=2a-3ell`.                                      (6.1)

Because

`3/2 < log_2 3 < 2`

and `a/ell>log_2 3`, both `Sigma` and `Delta` are positive.

The transformation is unimodular:

`[Sigma]   [-1  2][a  ]`

`[Delta] = [ 2 -3][ell]`,

with determinant `-1`.

Its inverse is

`boxed: a=3Sigma+2Delta`,

`boxed: ell=2Sigma+Delta`.                             (6.2)

Consequently

`boxed: gcd(Sigma,Delta)=gcd(a,ell)=g.`                (6.3)

Now observe that the two canonical synchronized pumps have exponent vectors

- `c=101`: `(3,2)`, normalized-weight multiplier `8/9`;
- `c=10`: `(2,1)`, normalized-weight multiplier `4/3`.

Using (6.2),

`boxed:`

`zeta=2^a/3^ell=(8/9)^Sigma(4/3)^Delta`.               (6.4)

Equivalently,

`boxed:`

`log zeta = Delta log(4/3)-Sigma log(9/8)`,            (6.5)

and

`boxed:`

`(9/8)^Sigma(3/4)^Delta=1/zeta`.                       (6.6)

Classification: **analytic theorem / coordinate synthesis**.

### 6.1 Why the apparent two-scale Diophantine route collapses

The determinant of the two pump exponent vectors `(3,2)` and `(2,1)` is `-1`. They therefore form a `Z`-basis of the whole exponent lattice.

Thus a continued-fraction attack on

`Delta log(4/3) ~= Sigma log(9/8)`

is not independent of the original attack on

`a log(2) ~= ell log(3)`.

It is the same rank-two lattice written in the canonical pump basis.

For an actual extracted `c=101` repeat count `p` and `c=10` repeat count `q`, the residual context has pump coordinates

`Sigma_ctx=Sigma-p`,

`Delta_ctx=Delta-q`.                                  (6.7)

Unless a new theorem bounds `(Sigma_ctx,Delta_ctx)`, the residual context can absorb arbitrary changes in `(p,q)`. Therefore no bounded-parameter two-logarithm equation has yet been produced.

This is the precise algebraic reason the RL75 “competing pump Diophantine” route does not become stronger merely by switching from `log_2 3` to the ratios `8/9` and `4/3`.

### 6.2 Exact coordinates of the RL73 first pair

On (5.4),

`Sigma0=32,245,142,102,746,531,540`,

`Delta0=13,201,833,154,443,526,323`.                  (6.8)

The second value is exactly the RL73 global skew floor value at the surviving convergent.

---

## 7. New theorem E — closed-pump product excess and physical-scale lower bound

Let a closed synchronized pump `c` have

`P=2^n`, `R=3^s`, `C=Q(c)`,

and physical affine fixed point

`alpha=C/(P-R)`.

Suppose `c` is repeated `q>=1` times as a positive integral physical subtrajectory, entering at state `x` and exiting at state `y`.

Since

`y-alpha=(R/P)^q(x-alpha)`,                            (7.1)

and by the segment product identity

`Pi(c^q)=(P/R)^q y/x`,

we obtain the exact cancellation

`boxed:`

`Pi(c^q)-1 = alpha[(P/R)^q-1]/x`.                      (7.2)

For the nontrivial proper pumps relevant here, which contain at least one `1`, `C>0`; hence the sign of `alpha` is the sign of `P-R`, so the right side is positive.

Classification: **analytic synthesis** of RL19 and RL76.

### 7.1 Full-phase scale consequence

If this pump occurs as a subsegment of the full half `v`, every omitted odd-product factor is `>1`, hence

`Pi(c^q)<=Pi_v`.

Using (3.7),

`boxed:`

`x > [9(N-2)(N+4)/(43N+72)]`

`    * |alpha| * |(P/R)^q-1|`.                        (7.3)

So full phase **does** charge repeated pump depth: it requires physical entry scale.

But it does not cap that scale.

### 7.2 Canonical positive pump `c=10`

Here

`alpha=1`, `P/R=4/3`.

Thus

`Pi(10^q)-1=[(4/3)^q-1]/x`,                            (7.4)

and

`x > [9(N-2)(N+4)/(43N+72)] [(4/3)^q-1]`.             (7.5)

On the RL76 `v`-half paired realization,

`x=1+3*4^q m`.

Hence (7.5) becomes only a **lower bound on the free scale integer `m`**. For every fixed `N,q`, choosing `m` sufficiently large makes (7.4) arbitrarily small.

Therefore the full-phase product budget does not give a uniform `q` bound.

### 7.3 Canonical negative pump `c=101`

Here

`alpha=-7`, `P/R=8/9`.

Thus

`Pi(101^q)-1=7[1-(8/9)^q]/x`.                          (7.6)

On the RL76 paired realization,

`x=-7+3*8^q m`.

Again the scale integer can make the product cost arbitrarily small. The numerator in (7.6) is itself bounded by `7`, while the physical entry scale can grow exponentially.

### 7.4 Canonical-prefix stress calculation

The exact full half begins with `111`. Starting from `N+4`, that prefix reaches

`x_111=(27N+127)/8`.

Its product is

`Pi_111=1+19/[27(N+4)]`.

If one formally appends `p` copies of the negative quotient pump `101`, the product through that prefix is

`boxed:`

`Pi_[111(101)^p]`

`=1+[75-56(8/9)^p]/[27(N+4)].`                        (7.7)

As `p->infinity`, its excess tends to

`25/[9(N+4)]`,                                         (7.8)

which is strictly below the inherited full-half upper coefficient `43/[9N]` at large `N` (and below the exact upper (3.7) for every `N>2`).

This is **not** a construction of arbitrary full-phase completions: fixed-`N` pump integrality and the remaining word still matter. It is a sharp product-method stress test showing that the full-phase product upper bound has no asymptotic objection to the canonical negative scale-prepayment mechanism.

---

## 8. What the serious product/CF attack did and did not achieve

### 8.1 Achieved

- exact full-half product budget in modern full-phase coordinates;
- full-phase-wide lower as well as upper phase window;
- a general reduced-CF successor window tied to `gN`;
- elimination of all gcd multiples of the RL73 first convergent;
- exact first-pair phase-state interval;
- unimodular pump-coordinate normal form;
- proof that the `8/9` versus `4/3` two-scale CF is a coordinate rewrite unless residual context is bounded;
- exact product-excess/physical-scale law for every closed pump.

### 8.2 Still missing

No theorem bounds any of the following uniformly:

- the physical pump-entry scale `x`;
- RL76's free integer `m`;
- the fixed-context integer `K_ctx`;
- the phase state `N` from above;
- `g=gcd(a,ell)` in the huge-reduced-denominator branch;
- the residual pump coordinates `(Sigma_ctx,Delta_ctx)` after extracting actual pumps;
- the complementary exponent/growth context.

The product theorem therefore converts repeat depth into a **scale demand**, but RL76 already supplies an unbounded scale reservoir. The CF theorem converts phase into a **successor-denominator demand**, but `gN` is unbounded. The two failures are the same obstruction in different coordinates.

---

## 9. Mandatory red-team tests

### 9.1 No silent upper bound on cycle states

Passed. RL77 never assumes one. The pump scale result is explicitly a lower bound on state size and is recorded as non-closing because no upper bound is inherited.

### 9.2 No generic CF masquerading as new RL structure

Passed. The new CF statement is derived only after inserting the RL64/RL65 full-phase half-product/numerator window. More importantly, the canonical two-pump CF is explicitly demoted when the unimodular lattice calculation shows that it is merely a coordinate transform without residual-context control.

### 9.3 RL76 reciprocal-packing barrier

Passed. RL77 does not try to price `c=10` depth by reciprocal mass. It derives the exact product-excess law and confirms that the missing quantity is still physical scale.

### 9.4 RL20 `D∤Q` radius-4 fake model

The new product/phase theorems require genuine RL64 full phase and therefore do not apply to the RL20 fake model. This is the correct discrimination direction: the theorems are ownership-sensitive.

However, they still do not force a contradiction on genuine data. Hence they do not close Gate B or provide a radius bridge.

---

## 10. RL77 route decision

The RL77 stop criterion is met.

A serious product/CF attack has produced genuine structural upgrades, but the physical scale parameter and complementary context remain unbounded. The canonical competing-pump Diophantine idea collapses to the original exponent lattice through an exact unimodular transformation.

Therefore do **not** spend RL78 on:

- a larger generic CF scan;
- another Baker/two-log bound with arbitrary context coefficients;
- endpoint `Psi`;
- raw `(2-N)M`;
- another Gate-A q-digit selector;
- reciprocal packing of the canonical `c=10` chain.

Pivot to the RL75 deliberate alternative:

# **D|Q-sensitive bounded-radius Gate-B reconnaissance**

The exact next target is supplied in

`RL78_DQ_SENSITIVE_BOUNDED_RADIUS_GATE_B_RECONNAISSANCE_TARGET.md`.

---

## 11. Correction / demotion ledger additions

Retain all RL72–RL76 corrections and add:

1. **First convergent multiples removed.** The RL73 low-denominator survivor cannot occur at gcd scale `g>=2`; the branch is the single exact exponent pair `(p0,q0)`.
2. **Two-pump CF reclassified.** The canonical `101` and `10` exponent vectors form a unimodular basis. Generic Diophantine work on `(8/9)^p(4/3)^q` is not independent of the original `2^a/3^ell` near-resonance unless the residual context is independently bounded.
3. **Product depth pricing sharpened.** A closed pump has exact product excess `alpha[(P/R)^q-1]/x`; full phase prices repeat depth by physical entry scale, not by repeat count alone.
4. **Scale remains the obstruction.** Since RL76 leaves the physical scale integer/context unbounded, the new product budget does not yield a uniform pump-depth theorem.
5. **CF successor localization is not a finite global scan.** The next convergent denominator is controlled relative to `gN`, but `gN` is not globally bounded.
6. **No claim that the formal canonical-prefix stress family is a full-phase completion.** It is only a product-budget stress calculation; integrality, ownership and completion remain required.

---

## 12. Exact proof state after RL77

### New proved analytic mathematics / synthesis

- exact segment odd-product identity (2.1) inserted into the RL64 full half;
- exact full-half product representation (2.2)–(2.3);
- full-phase-wide lower product/phase window (3.3)–(3.6);
- terminal-`k` upper phase refinement (3.8);
- reduced-CF successor window (4.4)–(4.5);
- first-convergent de-scaling `g=1`;
- unimodular canonical pump-coordinate theorem (6.2)–(6.6);
- exact closed-pump product-excess law (7.2);
- full-phase pump-entry scale lower bound (7.3);
- canonical-prefix product stress formula (7.7).

### New exact arithmetic certificate

The RL77 verifier checks:

- algebraic product identities on bounded exact examples;
- the universal `Q(y)>=3^r-2^r` lower bound on bounded words;
- the pump-coordinate unimodular identities and gcd preservation;
- `c=10` and `c=101` exact product-excess formulas;
- the RL73 survivor logarithmic inequalities proving `g=1`;
- the exact integer upper endpoint in (5.6).

The verifier is an audit/falsification certificate, not the proof of the infinite statements.

### Global closure state

Unchanged:

- radius-3 primitive/full-`D` local obstruction: **closed**;
- Gate A even `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

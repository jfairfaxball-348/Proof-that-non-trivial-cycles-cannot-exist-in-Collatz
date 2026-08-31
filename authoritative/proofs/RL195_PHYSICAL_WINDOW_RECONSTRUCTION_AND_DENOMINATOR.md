# RL195 — physical window reconstruction and its denominator boundary

RL195 independently reviewed analytic proof, with exact small regression
checks. No actual high-branch word is constructed or excluded.

Incoming handover: RL194; incoming job: RL195.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
The parent completed the fresh incoming gate and recorded
`.rl-work/RL195/authoritative-snapshot.json`, SHA256
`6f3387b61864ff25cb90be2eb271515a845e62cc062218f1d6ebb25ba5934dd7`.

## 1. Scope, definitions, and the exact provenance boundary

Use the sole high branch `(37,0,23,-1)` and

`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u0=103768467013`, `Ap-u0 L=1`, `z=L-p`,
`lambda=2^A/3^L>1`, `alpha=3^p/2^u0>1`,
`beta=(alpha-1)/(lambda-1)`.

Let `b_i=floor(Ai/L)`, `c_i=b_(i+1)-b_i`.  A globally admissible height
word in this note means a nonnegative integral L-periodic word with `h_0=0`
and, importantly,

`a_i=c_i+h_i-h_(i+1)>=1` for every i.                    (1)

The weaker bound `h_(i+1)<=h_i+1` alone is not a substitute for (1): when
`c_i=1`, positive acceleration requires `h_(i+1)<=h_i`.
Put `S_i=b_i-h_i`, `q_i=2^S_i/3^i=rho_i 2^(-h_i)` and
`rho_i=2^b_i/3^i`, with the established quasiperiodic lifts after L.
Then `S_0=0`, `S_(i+1)-S_i=a_i`, and `sum_(i<L)a_i=A`.
Equivalently, the inherited physical construction is exactly
`S_i=sum_(j=0)^(i-1)a_j` and `h_i=floor(Ai/L)-S_i`.
This definition, explicitly recorded in RL175 section1 and RL181 section1,
gives `h_(i+1)=h_i+c_i-a_i` at **every** phase.  There is no exception
at a mechanical switch, at the p-shift carry source z, or across the
period boundary (where `b_(i+L)=b_i+A` and `S_(i+L)=S_i+A`).
The p-shift gap has a special carry formula; the one-step height law does
not.  In particular, a height-zero vertex with c_i=1 has a_i=1 and its
chronological successor is also height zero.

For a physical orbit, `3y_i+1=2^a_i y_(i+1)` and `y_(i+L)=y_i`.
Define `T_i=q_i y_i`,

`C_i=sum_(j=i)^(i+p-1)q_j`, `Y_i=sum_(j=i)^(i+L-1)q_j`.

The telescope `T_(i+1)-T_i=q_i/3`, its `0 -> p` arc identity and full
closure identity already occur in **RL175.1**.  The formula
`K_i=alpha T_(i+p)-T_i`, normalized p-shift chain, and its carry treatment
are already **RL181.1**.  They are inherited restatements here, not new
discoveries.  The complete lifted positive inversion
`3K_i=alpha C_i+beta Y_i` is incoming **RL194**.

Only the named RL175 and RL181 report/proof/correction files were consulted
to establish this boundary.  No broad historical novelty claim is made.
The denominator theorem below is proved directly and uses no sparse
resultant or historical same-root elimination as a new obstruction.

## 2. Physical arc transport: exact but inherited

From `q_(i+1)=2^a_i q_i/3` and the physical affine recurrence,

`3(T_(i+1)-T_i)=q_i`.                                  (2)

Summing a lifted arc of any length n gives

`3(T_(i+n)-T_i)=sum_(j=i)^(i+n-1)q_j`.                 (3)

In particular,

`C_i=3(T_(i+p)-T_i)`,
`Y_i=3(lambda-1)T_i`.                                  (4)

Substitution in the incoming positive inversion yields precisely

`K_i=alpha T_(i+p)-T_i`.                                (5)

Thus (4) does not add another independent equation to the physical window
inversion.  Positivity and `0<p<L` imply the exact physical pair squeeze

`1<T_(i+p)/T_i<lambda`,
`alpha-1<K_i/T_i<lambda alpha-1`.                       (6)

The ordinary normalized state is `x_i=y_i/2^h_i`.  At every noncarry source
`i`, (5) gives `K_i=rho_i(x_((i+p) mod L)-x_i)`; at the unique source z it
gives `K_z=rho_z(2x_0-x_z)`.  Hence (6) refines the inherited chain only by
displaying its relative-state squeeze; it does not establish new physical
incidence, an H21 count, or a stronger spacing theorem.

## 3. Unique positive rational reconstruction

Conversely, begin with any globally admissible height word satisfying (1),
without assuming an odd-integral orbit.  Define

`y_i=Y_i/[3(lambda-1)q_i]`.                             (7)

These numbers are positive and L-periodic.  Since
`Y_(i+1)-Y_i=(lambda-1)q_i`, equation (7) implies (2) and therefore
`3y_i+1=2^a_i y_(i+1)`.  The same construction gives every identity
(2)--(5), including the positive window inversion, automatically.

It is unique: any L-periodic solution must satisfy the second equation of
(4), which forces (7).  Thus the positive affine recurrence and the window
identities by themselves reconstruct a positive **rational** cyclic orbit.
They must not be called an odd-integral realization before the arithmetic
condition below is imposed.

The canonical `rho_i<1` for `0<i<L`, together with nonnegative h and the
strict increase of T along a positive arc, also gives `y_i>y_0` for
`0<i<L`.  This least-state observation is conditional on the supplied
mechanical envelope and does not supply integrality.

## 4. Exact odd-denominator theorem

Let

`D=2^A-3^L>0`, `d=3^p-2^u0`.

No construction of these enormous integers is required for the proof.
For a source i and `0<=k<=L`, put

`s_(i,k)=sum_(j=i)^(i+k-1)a_j`,
`R_i=sum_(k=0)^(L-1) 3^(L-1-k) 2^s_(i,k)`.

The empty cumulative sum is zero.  Formula (7) becomes

`y_i=R_i/D`.                                           (8)

Every R_i is a positive odd integer: its k=0 term is odd, and (1) makes
all later terms even.  Also `gcd(D,6)=1`.  The cyclic numerator recurrence

`2^a_i R_(i+1)=3R_i+D`                                 (9)

shows that `gcd(D,R_i)` is independent of i.  Consequently every y_i has
the same reduced, odd denominator

`D_red=D/gcd(D,R_0)`.                                   (10)

### 4.1 The Bezout shift is a unit modulo D

One has

`gcd(D,d)=1`.                                           (11)

Indeed, modulo a common divisor g of D and d,
`2^A=3^L` and `3^p=2^u0`.  Raising to p and L respectively gives
`2^(Ap)=2^(u0 L)`.  Since `Ap-u0 L=1`, g divides `2^(u0 L)`; but g is
odd, so g=1.  This is a symbolic exact proof, not a numerical gcd test on
the actual giant D.

### 4.2 The normalized gap retains exactly the orbit's odd denominator

Define the integral p-arc numerator

`P_i=sum_(k=0)^(p-1) 3^(p-1-k) 2^s_(i,k)`.

The p-step affine identity is

`2^s_(i,p) y_(i+p)=3^p y_i+P_i`.

Using (5) and `q_(i+p)/q_i=2^s_(i,p)/3^p`, the normalized gap satisfies

`Delta_i=K_i/rho_i=(d*y_i+P_i)/2^(u0+h_i)`.             (12)

This formula includes the unique carry automatically because the p-step
arc is lifted.  Inserting (8), its numerator before cancelling powers of
two is `d R_i+P_i D`.  By (11),

`gcd(D,d R_i+P_i D)=gcd(D,R_i)`.

Therefore the **odd part of the reduced denominator of every Delta_i is
exactly D_red**.  No odd denominator can disappear merely by passing to
one of these normalized p-shift gaps.

### 4.3 Equivalence and its branch application

For a globally admissible height word, the following are equivalent:

1. its reconstructed rational orbit consists of positive odd integers;
2. `D | R_0`;
3. at least one normalized gap Delta_i is dyadic (has power-of-two reduced
   denominator);
4. every normalized gap Delta_i is dyadic.

For 2 -> 1, all R_i/D are integral by (9), positive by (8), and odd because
both R_i and D are odd.  Their exact recurrence then makes a_i the actual
2-adic valuation of `3y_i+1`.  The remaining equivalences follow from
(10)--(12).

At the canonical root, `rho_0=1` and `Delta_0=K_0`.  Consequently, if a
globally admissible height word satisfies the **exact** branch moment

`alpha C_0+beta Y_0=3*2^37`,                             (13)

then its reconstructed orbit is already positive odd-integral.  The
additional incoming anchors, including `h_p=0`, can be imposed separately;
the denominator implication itself does not need `h_p=0`.

This is an equivalence/ownership boundary, **not** a construction of a word
satisfying (13), not an atom realization, and not a cycle exclusion.  The
existence or impossibility of a complete admissible word with the required
exact moment remains unproved here.

## 5. Precisely scoped transport barrier

There are two distinct regimes, and they must not be conflated.

- Given a height word but no exact dyadic normalization, positive rational
  reconstruction satisfies every displayed transport identity automatically.
  Those identities alone do not enforce odd integrality.
- Given a complete admissible height word **and exact** K0=2^37, odd
  integrality is not an additional missing test: the denominator theorem
  already forces it.  Rechecking that arithmetic through the same telescope
  does not create an independent contradiction.

Replacing (13) by a numerical interval, a necessary moment bound, or a few
local prefix constraints loses this equivalence.  Such relaxations remain
one-way filters.  In particular, RL194's finite owned-prefix survivors do
not supply a complete height word, full monodromy, or (13), so this theorem
does not promote them to physical realizations.

The result identifies exactly what a genuinely new window argument must
control: existence of a globally admissible, chronologically placed height
word satisfying the exact fixed-gap moment, or a new inequality/congruence
that makes such a word impossible.  It does not rule out stronger local
incidence, numerator ownership, or congruence methods.  RL175's sparse
resultant route and its scope limitation are not revived.

## 6. Exact verifier and finite coverage

Run `python3 verification/verify_rl195_window_reconstruction.py` from the package root.
The script checks the actual small Bezout constants symbolically, without
constructing `2^A` or `3^L`.

For regression it exhausts all256 assignments `h_0=0`,
`h_1,...,h_4 in {0,1,2,3}` for `(A,L,p,u0)=(8,5,2,3)`, retains exactly
the7 words satisfying every a_i>=1, and verifies rational reconstruction,
all5 cyclic recurrences and carry-completed gaps per word, all lifted arc
lengths1..5 from each canonical source, positive window inversion, the
relative-state squeeze, and exact denominator preservation.  A separate
trivial1-cycle regression supplies a positive odd-integral case.

The all-zero toy word gives `y_0=319/13` and `K_0=48/13`: it satisfies the
positive rational transport laws but is not odd-integral.  It is not an
actual-constant high-branch counterexample and does not satisfy K0=2^37.

Classification: analytic reconstruction and denominator-equivalence proof;
inherited telescope/owned-gap restatements; precisely scoped method barrier.
The small cases are exact algebraic regressions only.  No actual phase scan
is begun or claimed, no range of actual high-branch words is certified, and
all H21, spacing, rank-set and global obligations remain unchanged.

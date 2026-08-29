# RL174 — correction and physical p-shift gap floor

Date: 2026-08-29

## Outcome and classification

RL174 triggered a stop-and-repair while attacking the RL173 physical-gap target.
RL173's exact arithmetic certificate computed the advertised functional

`F3=sum_i q_i(3^(-G_i)-1)`,

but the report incorrectly identified that accelerated odd-phase functional with
RL19's physical arbitrary-rotation weighted-difference term.  After compressing
to accelerated odd phases, an exponent-prefix change `G_i` multiplies
`q_i=2^(S_i)/3^i` by `2^(G_i)`, not by `3^(-G_i)`.

The correction is local to the RL173 bridge interpretation.  RL173's numerical
values `-52/81` and `176/27` remain exact values of the auxiliary `F3`
functional, but they do not prove anything about the sign of the physical
accelerated p-shift difference.

RL174 repairs the sign barrier and then continues the live target.  New promoted
results are:

1. **RL174.1 — corrected accelerated rotation identity** (analytic, ordinary
   `+1`): for the accelerated p-rotation,
   `F2=sum_i q_i(2^(G_i)-1)=3(lambda-1)(y_p-y_0)`.
2. **RL174.2 — repaired local sign-nonforcing barrier** (exact algebra + exact
   rational witnesses): the corrected `F2` still has both signs under the
   bounded local nonnegative-defect grammar.
3. **RL174.3 — physical p-shift gap/flow floor** (analytic, coprime `g=1`
   first-survivor least-root scope):
   `y_p-y_0>(lambda-1)m` and
   `F2>3m(lambda-1)^2`.
4. **RL174.4 — absolute first-survivor floors**: internally,
   `F2>1/186000000000`; conditional on the inherited external minimum
   `m>=2^71`,
   `y_p-y_0>=2,120,000,002` and `F2>1/176`.
5. **RL174.5 — height-zero p-phase upper window** (analytic + exact interval
   arithmetic, no external minimum): if `h_p=0`, then `F2<2/3`.

No non-trivial cycle is excluded.  Gate A, Gate B, global non-trivial-cycle
exclusion, and Collatz remain open.

## 1. Stop-and-repair: the RL173 coordinate mismatch

For an accelerated odd-state word `(a_0,...,a_(L-1))`, put

`S_j=sum_(i<j)a_i`, `q_j=2^(S_j)/3^j`, `lambda=2^A/3^L`.

For rotation by `p`, extend `S` by `S_(j+L)=S_j+A` and set

`G_i=S_(p+i)-S_p-S_i`.

The rotated accelerated prefix weight is therefore

`q_i^(p)=2^(S_(p+i)-S_p)/3^i = q_i 2^(G_i)`.              (1.1)

This is the exact point at which RL173 mixed coordinate systems.  In RL19's
*binary-time* identity, the weight is `2^i 3^(-P_i)` and a change in the odd
prefix count `P_i` indeed contributes a factor `3^(-G_i)`.  In the accelerated
odd-phase coordinate used by RL173, `G_i` is an exponent-prefix change, so its
factor is `2^(G_i)`.

The RL173 verifier remains a valid exact audit of its declared auxiliary
functional `F3`; the demotion is the physical interpretation of that
functional and the use of its two old witnesses as a physical sign barrier.

## 2. RL174.1 — corrected accelerated rotation identity

Assume the ordinary accelerated recurrence

`3y_j+1=2^(a_j)y_(j+1)`

cyclically, and define `z_j=q_j y_j`.  Then

`z_(j+1)-z_j=q_j/3`.                                      (2.1)

Summing one full cycle, using `z_L=lambda y_0`, gives

`sum_(i=0)^(L-1) q_i = 3(lambda-1)y_0`.                   (2.2)

Apply the same identity after rotating the word and physical root by `p`.
Equation (1.1) gives

`sum_i q_i 2^(G_i)=3(lambda-1)y_p`.                        (2.3)

Subtracting (2.2) proves

### Theorem RL174.1

`F2 := sum_i q_i(2^(G_i)-1)
    = 3(lambda-1)(y_p-y_0)`.                              (2.4)

This is the corrected accelerated p-shift physical difference identity.

## 3. RL174.2 — the local sign barrier survives the repair

The correction does not make the physical sign locally forced.  The following
bounded positive exponent words satisfy `gcd(A,L)=1`, `2^A>3^L`, `h_0=0`, and
`h_j=floor(Aj/L)-S_j>=0`:

- `(a_0,a_1)=(1,4)` has `(A,L,p,h)=(5,2,1,(0,1))` and
  `F2=14/3>0`;
- `(a_0,a_1,a_2)=(2,5,4)` has
  `(A,L,p,h)=(11,3,2,(0,1,0))` and `F2=-28/9<0`.

Their unique positive rational cyclic trajectories also satisfy (2.4)
exactly.  Neither is asserted to be an integral physical Collatz cycle.
Therefore local nonnegative-defect grammar still does not force the sign of
the *correct* accelerated p-shift physical functional.

For comparison, RL173's original words `(1,4)` and `(1,4,3)` give the exact
auxiliary values `F3=-52/81` and `F3=176/27`, but their corrected values are
`F2=14/3` and `F2=2/9`, both positive.  Those old witnesses are therefore
superseded for the physical sign-barrier claim.

## 4. RL174.3 — quantitative physical p-shift gap

Return to the inherited coprime `g=1` first survivor

`A=217,976,794,617`, `L=137,528,045,312`,

with a hypothetical least-rooted physical odd cycle `m=y_0`.  The inherited
Bezout constants are

`p=A^(-1) mod L=65,470,613,321`,
`u=(Ap-1)/L=103,768,467,013`,

so `Ap=uL+1` and `0<p<L`.

RL133 supplies `h_p>=0`.  Since `floor(Ap/L)=u`,

`S_p=u-h_p`,

and the lifted defect at the p-phase is

`E_p=Ap-LS_p=1+Lh_p>0=E_0`.                               (4.1)

Because `0<p<L`, RL169.1 applies to the chronological pair `(0,p)` and gives

`y_p-m>(lambda-1)m`.                                      (4.2)

Combining (4.2) with the corrected physical identity (2.4) yields

### Theorem RL174.3

`F2>3m(lambda-1)^2`.                                      (4.3)

This is the quantitative physical input missing from RL173.  It is not a
local-defect statement: the strict gap comes from actual least-root physical
state order plus the ordinary `+1` chronological increment used in RL169.

## 5. RL174.4 — exact absolute floors

Put

`Delta=A log(2)-L log(3)>0`, so `lambda=exp(Delta)`.

Since `exp(Delta)-1>Delta`, (4.3) gives

`F2>3m Delta^2`.                                           (5.1)

There is also an entirely internal integer floor.  The p-phase and the least
state are distinct odd physical states, hence `y_p-m>=2`.  From (2.4),

`F2>=6(lambda-1)>6Delta`.                                  (5.2)

The exact rational logarithm enclosure in
`RL174_CERTIFICATES/verify_p_shift_gap_repair.py` certifies

`6Delta > 1/186000000000`,                                (5.3)

so every hypothetical physical cycle in this fixed `g=1` survivor branch
satisfies

`F2 > 1/186000000000`.                                    (5.4)

Now additionally invoke the inherited **EXTERNAL COMPUTATIONAL INPUT**
`m>=2^71`.  Equation (4.2) and `lambda-1>Delta` give

`y_p-m > 2^71 Delta > 2,120,000,000`.                     (5.5)

The difference of two odd states is even, hence

`y_p-m >= 2,120,000,002`.                                 (5.6)

Likewise (5.1) gives

`F2 > 3*2^71 Delta^2 > 1/176`.                            (5.7)

The numerical strengthening (5.5)--(5.7) is conditional on the inherited
external least-state floor; the identity and symbolic inequalities are not.

## 6. RL174.5 — an internal height-zero upper window

The inherited below-side neighbour is `(u,p)`, and RL134 certifies

`d_-:=u log(2)-p log(3)` with `-6Delta<d_-<-5Delta`.

At the p-phase,

`q_p=2^(S_p)/3^p=exp(d_-)/2^(h_p)`.                        (6.1)

If `h_p=0`, the inherited physical suffix squeeze `q_p y_p<lambda m`
implies

`y_p/m < exp(Delta-d_-) < exp(7Delta)`.                   (6.2)

RL134 also proves internally `m<2^75` for this `g=1` survivor.  Therefore

`F2=3(lambda-1)(y_p-m)
   <3*2^75 (exp(Delta)-1)(exp(7Delta)-1)`.                 (6.3)

For `0<x<1`, `exp(x)-1<x/(1-x)` (equivalently
`exp(x)<1/(1-x)`, from `-log(1-x)>x`).  The exact logarithm enclosure verifies
`7Delta<1` and reduces (6.3) to a rational inequality strictly below `2/3`.
Thus

### Theorem RL174.5

`h_p=0  =>  F2<2/3`.                                      (6.4)

Equivalently, `F2>=2/3` forces `h_p>=1`.  This is a real transported-height
consumer, but it does not yet force either side of that dichotomy.

## 7. Exact audit and red teams

`RL174_CERTIFICATES/verify_p_shift_gap_repair.py` uses exact `Fraction`
arithmetic.  It:

- reproduces RL173's `F3=-52/81` and `F3=176/27` values;
- verifies that those same words have corrected `F2=14/3` and `F2=2/9`;
- verifies the repaired opposite-sign witnesses `14/3` and `-28/9`;
- verifies (2.4) on those rational cyclic trajectories;
- checks `Ap-Lu=1` for the first survivor;
- uses 100-term exact atanh-series enclosures for `log 2` and `log 3`;
- rechecks `5 theta<1` and `-6Delta<d_-<-5Delta`;
- certifies (5.3), (5.5), (5.7), and the `h_p=0` bound (6.4).

Red-team outcomes:

- **Coordinate/base mismatch:** REPAIRED. Binary-time `3^{-G}` and accelerated
  exponent-time `2^G` are no longer conflated.
- **Ordinary increment:** PASS. The corrected identity uses the ordinary
  `+1` recurrence through `z_(j+1)-z_j=q_j/3`.
- **Physical/quotient:** PASS. Rational witnesses are labelled local only;
  physical gap claims are made only under an assumed physical cycle.
- **Phase order:** PASS. `p` is a long chronological index, and RL169 is used
  only because `0<p<L` and `E_0<E_p` are proved.
- **External input:** PASS. The `m>=2^71` consequences are explicitly
  conditional; the internal floor and `h_p=0` upper bound are not.
- **No false closure:** PASS. No cycle is constructed or excluded.

## 8. Next target

RL175 should consume the corrected physical floor rather than return to the
superseded `F3` functional.  Seek an upper bound or structural decomposition
for

`F2=sum_i q_i(2^(G_i)-1)`

from the transported height profile, p-arc structure, or exact closure data
that can be compared with the internal floor and, separately, the stronger
external-floor conditional `F2>1/176`.

The first useful split is `h_p=0` versus `h_p>=1`: RL174 now supplies an
internal upper window in the zero-height case but not yet a contradiction.
Preserve the `g=1`, ordinary-`+1`, physical-state, phase-order, correction
ledger, and external-floor qualifications.

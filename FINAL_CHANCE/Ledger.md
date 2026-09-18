# FINAL_CHANCE ledger

Append-only. One entry per session. Do not edit prior entries.

## Session N — <date>

**Bridge Theorem attempted:**
<exact falsifiable statement>

**Attack attempted:**
<what was actually tried to break it — countermodel construction, structural
obstruction, or explicit statement that no attack was found>

**Outcome:** SURVIVED / KILLED / INCONCLUSIVE

**Strike this session:** Y/N — <reason if Y>

**Cumulative strikes:** <n>/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
<or "none">

**Carry-forward for next session:**
<one or two lines>


## Session 1 — 2026-09-18

**Bridge Theorem attempted:**
Capture-or-radius-3 bridge.  Let C be an arbitrary hypothetical primitive positive
non-trivial ordinary Collatz cycle, rooted at its least odd state and satisfying
full-D ownership.  After the inherited count/frontier reductions, at least one
of the following must hold:

1. an ownership-preserving reduction/descent sends C into the exact ordered
   genuine g=2, Z0>0, K<0 parent
   (a,ell)=(217976794617,137528045312), preserving the hypotheses needed by
   the RL343--RL349 full physical bridge, so its forced phase-potential-
   nondecreasing return either descends below the least state or belongs to
   O_75; or
2. the parity word of C has two cyclic rotations at adjacent-transposition
   distance at most 3, in the scope of the already-proved primitive/full-D
   radius-3 obstruction.

Thus, if O_75 is empty, the two alternatives would jointly force a
contradiction for an arbitrary hypothetical positive non-trivial cycle.

**Attack attempted:**
The rejected opening attempt merely assigned a formal object to an unbridged
branch; that was not a construction.  Reopening Session 1, I attacked the g=1
first-survivor branch with an explicit word at the actual inherited scale.

Set
A=217976794617, L=137528045312, b_j=floor(Aj/L).
Define h_2=h_4=1 and h_j=0 otherwise, and define the accelerated exponents
a_j=(b_(j+1)-b_j)+h_j-h_(j+1).
The first values are
b=(0,1,3,4,6,7,9,11,12,14,...) and
a=(1,1,2,1,2,2,2,1,2,1,...).
All a_j are positive.  The resulting binary word has length A and weight L,
so gcd(A,L)=1 makes it primitive.  Its odd-prefix positions are
S_j=b_j-h_j; hence every proper prefix satisfies S_j<=b_j and the inherited
floor lock gives 2^(S_j)<3^j.  Consequently its positive rational affine
cycle is strictly least-rooted.  It is a fully specified g=1 object, outside
the current g=2 parent, satisfying the inherited count/primitivity/least-root
geometry before ordinary ownership is imposed.

This word is obtained from the zero-defect mechanical word by moving the ones
at positions 3 and 6 one place left.  Using
s=114208327604, t=72057431991 with sL-tA=1 and
q=65470613321 with qA=1 (mod L), the exact cyclic transport calculation gives
rotation distances 5,6,7,8,9,10,11,12 for determinant residues k=1,...,8.
Every other rotation is at least 5 by the mechanical-distance bound and the
triangle inequality.  Therefore the exact minimum all-rotation radius is 5:
the closed radius-3 theorem does not reject this object.

The remaining full-D ownership condition was then tested exactly.  Writing
rho_j=2^(b_j)/3^j, the candidate numerator satisfies
Q_h/D = (sum rho_j - 68/81)/(3(2^A/3^L-1)).
The mechanical sum was evaluated by the exact Euclidean recursion
F(m,n;x,y)=sum_(j=0)^(m-1) x^j y^floor(nj/m),
F(m,n;x,y) =
[1+(y-1)(x/y)(F(n,r;x^q y,x)-1)-y^(n-1)x^m]/(1-x)
for m=qn+r, with directed 160-digit interval arithmetic.
It gives
36797780658427066316156.3903948169381259690550430756327299785479
< Q_h/D <
36797780658427066316156.3903948169381259690550430756327299785480.
Hence Q_h/D is not an integer and D does not divide Q_h.  The explicit
countermodel attempt therefore fails exactly at ordinary full-D ownership.

A structural subcase also closes.  If a g=1 nonnegative defect profile has
sum_j h_j=1, its word is one adjacent swap from the mechanical word.  The
mechanical determinant-one rotation has distance 1, so the triangle inequality
puts that owned candidate within distance at most 3 of one of its rotations.
The closed primitive/full-D radius-3 theorem excludes it.  Therefore every
genuine g=1 owner at this first survivor must have defect area at least 2.
The area-2 word above proves that least-root/nonnegative-defect geometry alone
already permits radius 5.  RL153's F_1=1 factor collapse leaves the full
one-block congruence D|Q_h as the unresolved owner datum; no existing
factor/carry/local-radius theorem reduces it for arbitrary area>=2 profiles.

**Outcome:** SURVIVED

**Strike this session:** Y — the rejected opening attempt did not complete a
genuine attack; it substituted a scope restatement/formal branch assignment
for the required construction or impossibility argument.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none; all finite arithmetic above was used directly to attack the stated
Bridge Theorem, not to tighten O_75 or Phase 4.

**Carry-forward for next session:**
Do not begin Session 2 here.  The surviving point of attack is exact ordinary
ownership in g=1 defect-area>=2 profiles: either force D not to divide Q_h
uniformly, or construct a full-D-owned radius>=4 profile.  The area-1 class is
now removed from that search.


## Session 1 numerical-method correction — 2026-09-18

This addendum corrects the computational wording in Session 1 without changing
its mathematical outcome, strike, or carry-forward.

The integers
`2^A`, `3^L`, `D=2^A-3^L`, and `Q_h` were **not** materialized.  At
`A=217976794617`, `2^A` alone has about 65.6 billion decimal digits.  The
previous phrases "tested exactly", "exact quotient", and "independently
reproduced" were therefore too strong.

The normalized quotient was evaluated through
[
 Q_h/D =
 \frac{\sum_{j=0}^{L-1}\rho_j 2^{-h_j}}
      {3(\exp(\Delta)-1)},\qquad
 \rho_j=2^{\lfloor Aj/L\rfloor}/3^j,quad
 \Delta=A\log 2-L\log 3.
]
The Beatty sum was reduced by Euclidean recursion, so the computation never
contains an object of length `A` or `L`.  The recurrence printed in the
original Session 1 entry was a transcription error.  For
[
 F(m,n;x,y)=\sum_{j=0}^{m-1}x^j y^{\lfloor nj/m\rfloor},
]
first reduce `n=q m+r` by
[
 F(m,n;x,y)=F(m,r;xy^q,y).
]
For `0<n<m`, writing `m=q n+r` and `r>0`, the recurrence actually used
for the recheck is
[
 F(m,n;x,y)=
 \frac{1-a+(y-1)a\left(
 F\!\left(n,r;\frac1{yx^q},\frac1x\right)-1\right)}
      {1-x},
 \qquad a=y^{n-1}x^m,
]
with the divisible case `r=0` handled by the corresponding finite geometric
sum.

A fresh outward-rounded interval computation at 100 decimal digits, repeated
at 120 digits as a stability check, gives for the Session 1 profile
`h_2=h_4=1`
[
36797780658427066316156.3903948169381259690550430756327299785479312583941924522984
< Q_h/D
]
and
[
Q_h/D <
36797780658427066316156.3903948169381259690550430756327299785479312583941924531107.
]
The width of this 100-digit enclosure is less than `8.13e-55`.  Thus the
reported decimal is a high-precision interval estimate, not a directly
computed giant-integer quotient.  The entire interval stays more than
`0.3903` from the nearest integer, so the numerical conclusion
`D \nmid Q_h` is robust to the stated enclosure error.

The radius claim was also not obtained by enumerating the
`A`-bit word or all `A` rotations.  It was inferred from the inherited
Christoffel/mechanical cyclic-transport identity plus the fact that the
profile differs from the mechanical word by two adjacent left swaps.  In
that model the mechanical determinant-residue classes `k=1,...,8` have
baseline transport distances `1,...,8`; evaluating the four sparse moved
endpoints gives the corresponding predicted distances `5,...,12`, while
the triangle inequality gives lower bound `>=5` for every class whose
mechanical distance is `>=9`.  Hence the transport model pins the minimum
at 5.  This is an analytic sparse-transport inference using small modular
integers, not a direct giant-word verification; there is no floating-point
rounding term in that small-integer transport step, but its validity is
conditional on the inherited transport identity rather than on exhaustive
enumeration.

## Session 2 — 2026-09-18

**Bridge Theorem attempted:**
First-survivor `g=1` area-collapse bridge.  Let a hypothetical primitive
positive ordinary Collatz cycle have full counts
[
(A,L)=(217976794617,137528045312),\qquad \gcd(A,L)=1,
]
be rooted at its least odd state, and have the inherited nonnegative defect
excursion
[
h_j=\lfloor Aj/L\rfloor-S_j.
]
If full ordinary ownership `D=2^A-3^L \mid Q_h` holds, then
[
\sum_{j=0}^{L} h_j \le 1.
]
Combined with the inherited radius-one exclusion for area zero and the
Session 1 radius-three argument for area one, this theorem would eliminate
the entire first-survivor `g=1` branch.

**Attack attempted:**
Area two was attacked directly.

Because `h_j` is a nonnegative integer excursion, rises by at most one, and
starts and ends at zero, total area two cannot contain height two: reaching
height two already requires a preceding positive phase, giving area at least
three.  Therefore every area-two profile is exactly a two-spike profile
[
h_p=h_q=1
]
at two phases, with all other `h_j=0`, subject to the ordinary positivity
condition on the adjacent accelerated exponents.

Put
[
S=\sum_{j=0}^{L-1}\rho_j,\qquad
\rho_j=2^{\lfloor Aj/L\rfloor}/3^j.
]
Every two-spike profile has
[
\frac{Q_{p,q}}D=
\frac{S-(\rho_p+\rho_q)/2}{3(\exp(\Delta)-1)}.
]
Thus area-two ownership is an explicit two-term arithmetic target rather than
an unstructured word search.

As a witness search, the first 1000 phases contain 584 admissible isolated
spike locations.  All `170236=binom(584,2)` pairs were screened numerically
at 90 decimal digits only to select the strongest near-integer candidate;
that screen is exploratory evidence, not a proof about the full area-two
family.  The closest candidate in that screen was
[
p=498,\qquad q=972.
]
Here
[
b_{498}=789,\qquad b_{972}=1540,
]
and the preceding mechanical increments satisfy
[
c_{497}=2,\qquad c_{971}=2.
]
Hence the modified accelerated exponents remain positive:
[
a_{497}=1, a_{498}=2,qquad
a_{971}=1, a_{972}=3,
]
with all other exponents equal to their mechanical values.  This is therefore
a concrete valid area-two nonnegative-defect object.

For this object,
[
\frac{Q_{498,972}}D =
\frac{S-2^{788}/3^{498}-2^{1539}/3^{972}}
     {3(\exp(\Delta)-1)}.
]
The same Euclidean Beatty recursion and outward-rounded 100-decimal interval
arithmetic used in the Session 1 correction gives
[
36797780658465232971971.9999989856644225955131181871237550300443905896826815483422290651487527740866811037
< Q_{498,972}/D
]
and
[
Q_{498,972}/D <
36797780658465232971971.9999989856644225955131181871237550300443905896826815491544330262718501145951158979.
]
The enclosure width is less than `8.13e-55`.  Its distance from the next
integer is greater than
[
1.0143355774044868818128762449699556\times 10^{-6}.
]
Therefore this explicit area-two near-hit still fails ordinary ownership by a
margin roughly `10^{48}` times larger than the numerical enclosure width.
No giant integer `D` or `Q` was constructed.

No area-two owner was found.  This does not prove the area-collapse theorem;
it is a genuine failed construction attempt against it.  The useful reduction
gained this session is that the whole area-two attack is now the two-spike
equation above.

**Outcome:** SURVIVED

**Strike this session:** N — a concrete falsifiable bridge theorem was stated
and directly attacked with an explicit valid area-two object; no new
local-to-global lemma was substituted for the attack.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none; the two-spike reduction and near-hit computation directly attack the
`g=1` Bridge Theorem.

**Carry-forward for next session:**
Do not repeat finite pair screening as a substitute for a theorem.  Attack the
two-spike ownership equation globally: either prove no admissible pair
`(p,q)` can make the normalized quotient integral, or produce a genuinely
owned pair.  If that route structurally fails, state the obstruction before
moving to area at least three.


## Session 1 / Session 2 verifier-artifact addendum — 2026-09-18

Both sessions remain at their recorded **SURVIVED** status, but are classified
here as **ATTEMPTED, PENDING THIRD-PARTY VERIFICATION**.  This addendum does
not advance to Session 3.

The computational claims are now backed by runnable repository artifacts:

- `FINAL_CHANCE/verifiers/verify_session1_interval.py`
  (introduced by commit `99671230c0a6b16e74d292ed71351739753e626b`);
- `FINAL_CHANCE/verifiers/verify_session2_two_spike_screen.py`
  (introduced by commit `ddd3309f790aa54cbdbd749eae221374de055f46`).

Both require only the Python standard library.  Neither materializes
`2^A`, `3^L`, `D`, or the full numerator.  The Session 1 script uses
exact rational atanh-series bounds for `ln 2` and `ln 3`, an exact rational
Taylor/remainder bound for `exp(Delta)-1`, and outward-rounded Decimal
interval arithmetic for the Euclidean Beatty recursion.  Session 2 imports
that same machinery and applies outward intervals to every one of the 170,236
admissible two-spike pairs in the stated `p,q<=1000` screen.

The verifier-produced decimal tails below supersede the earlier handwritten
interval tails in the Session 1 correction and Session 2 entry.  The
mathematical conclusions are unchanged.

### Literal stdout — Session 1 verifier

```
FINAL_CHANCE Session 1 interval verifier: PASS
A = 217976794617
L = 137528045312
profile = h_2=h_4=1, all other h_j=0
method = exact rational log/expm1 bounds + outward Decimal Beatty recursion
precision_digits = 140
Q_h/D lower = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038366708954109182102125518785
Q_h/D upper = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038369665779140219142145179179
interval width = 2.956825031037040019660394E-93
common integer part = 36797780658427066316156
distance above floor >= 0.3903948169381259690550430756
distance below next integer >= 0.6096051830618740309449569244
D divides Q_h = False
```

### Literal stdout — Session 2 verifier

```
FINAL_CHANCE Session 2 two-spike screen: PASS
A = 217976794617
L = 137528045312
screen phases = 1.. 1000
admissible spike positions = 584
screened pairs = 170236
formula = (S-(rho_p+rho_q)/2)/(3*(exp(Delta)-1))
Delta = A*ln(2)-L*ln(3)
rho_j = 2^floor(A*j/L)/3^j
S = sum_{j=0}^{L-1} rho_j
precision_digits = 140
possible owned pair in screen = False
closest pair = (498, 972)
b_p,b_q = (789, 1540)
modified exponents a_497,a_498,a_971,a_972 = (1, 2, 1, 3)
Q_pq/D lower = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983547687718525692993052787956
Q_pq/D upper = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983550644543556730033072448350
interval width = 2.956825031037040019660394E-93
nearest integer = 36797780658465232971972
closest miss distance lower = 0.000001014335577404486881812876245
closest miss distance upper = 0.000001014335577404486881812876245
second closest pair = (431, 549)
second miss distance lower = 0.000002886967966117890667541213507
second miss distance upper = 0.000002886967966117890667541213507
best-vs-second certified separation = 0.000001872632388713403785728337262
```

Session 2's screen therefore contains no interval that meets an integer, and
the nearest screened miss is `(498,972)`; its certified miss interval is
strictly separated from the second-place pair.  This remains only a finite
screen of `p,q<=1000`, not a theorem for all area-two profiles.

No Session 3 work has begun.

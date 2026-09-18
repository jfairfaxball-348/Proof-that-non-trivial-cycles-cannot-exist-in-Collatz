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


## Session 1 — 2026-09-18

**Bridge Theorem attempted:**
Every hypothetical positive non-trivial ordinary Collatz cycle can be reduced, without losing
ordinary +1 ownership, primitivity, least-state ordering, or the inherited least-state floor, to
the exact ordered genuine g=2, Z0>0, K<0 parent
(a,ell)=(217976794617,137528045312). Therefore a contradiction for that parent (in particular
O_75=empty together with its inherited bridge) would contradict an arbitrary hypothetical cycle.

**Attack attempted:**
The attack was reopened and aimed first at the explicit outside-parent branch g=1, where
g=gcd(A,L). For the first reduced survivor the exact coprime counts are

A=217976794617,  L=137528045312,  gcd(A,L)=1,
D=2^A-3^L>0.

A primitive positive exponent/parity word with full ordinary ownership D|N_0 is not merely a
formal model: the cyclic numerator identity
2^(a_j) N_(j+1)=3N_j+D
propagates D-divisibility to every phase, and y_j=N_j/D are then positive integers satisfying
3y_j+1=2^(a_j)y_(j+1). Thus an explicit g=1 object satisfying the requested encoding,
ownership and positivity conditions would be an actual positive ordinary non-trivial cycle.

I then attempted the alternative structural exclusion of g=1 using the strongest inherited exact
constraints. Rooted at the least state, every proper prefix has nonnegative defect
h_j=floor(Aj/L)-S_j>=0; h identically zero is already excluded. Full ownership for every remaining
nonzero excursion is exactly one dense distinguished-root congruence
P_h(rho)=0 (mod D), where
P_h(T)=sum_(j<L) 2^(H-h_j) T^(Aj mod L)
and every residue 0,...,L-1 occurs exactly once.

Three natural closure attempts fail for specific proved reasons:
(1) splitting the height layers gives only one combined ownership relation, not independently
owned layer congruences;
(2) the scalar carry-order proof for g>1 loses its block factor at g=1 (F_1=1), and mixed heights
admit an exact local order-collapse counterexample;
(3) replacing the distinguished-root condition by a resultant is insufficient: the exact
(A,L)=(13,8) positive-excursion example has Res(2T^8-1,P_h)=D while P_h(rho)!=0 mod D.
All rotated affine integrality conditions are also rank-one consequences of the same single
D|N_0 condition, so they supply no additional independent closure equation.

A two-sided finite construction was also checked at depth 75. It is not presently finite under the
proved constraints: there are exactly
15,537,359,898,820,273,235,593,329,305,889
legal nonnegative positive-exponent prefixes of length 75, while the terminal defect can be as
large as 80,448,749,261. No proved global modulus/ordering theorem reduces those quantities to a
tractable exhaustive set.

Therefore neither an explicit fully owned outside-g=2 witness nor an impossibility proof was
obtained. The precise surviving obstruction is the dense distinguished-root congruence coupled to
least-state ordering in the coprime g=1 branch; every attempted decomposition used above is
provably non-discriminating or loses ownership.

**Outcome:** INCONCLUSIVE

**Strike this session:** Y — the original submitted Session 1 did not complete the mandatory
construction/impossibility attack and merely restated a pre-existing scope obligation. Reopening
and completing the attack does not erase that session-level failure.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none

**Carry-forward for next session:**
Do not return to O_75. Any continuation must attack the remaining g=1 distinguished-root/least-state
condition itself, or produce an explicit ordinary-owned object in another outside-parent branch.

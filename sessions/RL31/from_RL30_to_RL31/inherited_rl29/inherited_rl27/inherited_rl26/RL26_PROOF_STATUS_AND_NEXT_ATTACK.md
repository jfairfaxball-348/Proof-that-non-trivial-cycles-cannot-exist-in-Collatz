# RL26 proof status and next attack

Date: 2026-08-21

## Executive state

**RL is open.** The session nevertheless made certified progress on both the global packing and the order-3 cubic bridge.

The proof state is deliberately separated below into analytic theorems, exact finite certificates, external-input consequences, and method evidence.

## A. Analytic results now available

### A1. Strongest global packing theorem

`continuation/RL24_TYPEI_HIGH_START_SUPPORTING_LINE.md`

For `R>=161`, trajectory ownership of the first type-I terminal high gives

`h_0 >= (9R+5)/4`

and sharpens the first type-I high/high pair to

`F(a)F(b) <= (81R+73)/(81R+45)`.

Combining this with exact global valuation accounting yields a supporting-line majorant `C_H(R)` with

`log(lambda)/L <= C_H(R)`

and

`lim R*C_H(R) = 457841/1843200 ~= 0.248394639756944`.

This supersedes the earlier RL24 coarse and tilted constants numerically; those notes remain in the bundle as audit trail.

### A2. Global cubic range upper bounds

`continuation/RL25_CUBIC_RANGE_ORIENTATION_AND_HARD_SECTOR.md`

In the near-resonant order-3 balanced branch,

`Delta < Y[(4/5)e - 3 + 3(2/3)^e]`.

If `H>G`, orientation ownership improves this to

`Delta < Y[(8/15)e - 2 + 2(2/3)^e]`.

The factor of order `e` remains the principal Track-B defect.

### A3. Orientation/residue cubic lattice split

The four exact lower scales before the universal factor `4` are:

- `R==1 mod3`, `G>H`: `3B+Y`;
- `R==1 mod3`, `H>G`: `3B+2Y`;
- `R==2 mod3`, `G>H`: `3B+2Y`;
- `R==2 mod3`, `H>G`: `2B+3Y`.

Thus only `R==1 mod3`, `G>H` retains the weakest lattice vector.

### A4. Five-bit least-state sieve

`continuation/RL26_FIVE_BIT_LOW_STATE_AND_CUBIC_HARD_SECTOR_SIEVE.md`

For near-minimum odd phases in the stated branch and `R>=161`, leastness excludes residues `3,11,19,23 mod32`, leaving

`s mod32 in {7,15,27,31}`.

The weak cubic vector survives only for root residue

`R==27 mod32`.

Combining with `R==1 mod3` gives

`R==91 mod96`.

The inherited hard-root classes refine as

`43 mod144 -> 187 mod288`,

`91 mod144 -> 91 mod288`.

Therefore the inherited exceptional weak-close class becomes

`R==91 mod288`.

At exact weak-vector equality the gap geometry is

`G=12, H=4`.

The hard least root has forced prefix `11011...`.

## B. Exact finite certificates

These are rigorous within their finite stated ranges but must not be promoted to unconditional global cycle statements.

1. RL24 continued-fraction check, conditional on inherited external `R>=2^71`:

   `L/gcd(A,L) >= 57,397,300,723`.

2. RL25 terminal-pair scan for `e<188`:

   `(65,41), (149,94), (214,135), (233,147)` are the only pairs satisfying the stated near-resonant inequality.

3. RL26 small first-pair localization: at `(b,e)=(65,41)`, the five-bit hard-sector sieve leaves only `(G,H)=(12,4)`, `R==91 mod96`.

These finite certificates are strategically useful for pattern recognition, not substitutes for the global external-floor regime.

## C. External dependency retained

The bound

`R>=2^71`

is inherited **EXTERNAL COMPUTATIONAL INPUT**. The new analytic RL24--RL26 arguments do not prove this floor. Any statement using it must remain labeled conditional on that input.

Exact radius 3 remains closed only under its inherited audited hypotheses/dependencies; see the retained earlier ledgers/handover for that dependency chain.

## D. Method evidence / non-cycle witnesses

### D1. RL23 exact local saturation family

`R=361+486t` realizes exact type-II two-low block saturation and terminates at

`z=(4R-1)/3`,

which is exactly the predecessor geometry of the RL20 exceptional `(1,1)` weak final return.

After the RL26 fifth-bit refinement, hard-compatible infinite subfamilies remain at

`t==3 or 35 mod48`.

This is a finite trajectory-segment witness, **not a cycle**.

### D2. Local dynamical barrier

Arbitrarily long exact least-respecting finite segments approach normalized coefficient

`1/(6 log2) ~= 0.24044917348`.

This is a method obstruction for purely local uniform packing, not a theorem that a cycle achieves the coefficient.

## E. Why the frontier is now narrow

Three previously separate obstructions now align:

1. the Track-B weakest cubic vector;
2. the inherited RL20 exceptional weak final return;
3. the RL23 exact local packing saturation mechanism.

After RL26 they meet in the same exceptional root/gap geometry:

`R==91 mod288`, `G=12`, `H=4`, hard prefix `11011...`

when all inherited weak-close hypotheses are imposed.

Residue sieving alone cannot eliminate this geometry because the saturation family still has infinitely many compatible parameters.

## F. Primary next theorem to seek

Prove a **nonlocal adjacent-block ownership lemma** in the exceptional geometry. The natural object is not another one-block product bound but the combined numerator/valuation data on the blocks adjacent to:

- the least root and its forced `11011...` departure;
- the two balanced states at gaps `12` and `4`;
- the exceptional final `(1,1)` return.

A successful lemma should do at least one of the following:

1. show that the exact `G=12,H=4` cubic extremizer cannot coexist with the weak final return in one closed cycle;
2. force additional shared parity/valuation information, thereby raising the cubic lattice lower bound;
3. show that saturation blocks have insufficient global frequency under the exact valuation sum `sum nu_i=A`;
4. replace the current numerator-range upper `O(eY)` by a bound with a substantially smaller dependence on `e` in the unique weak sector.

## G. Low-priority / avoid

- Do not reopen radius 3 absent verifier/dependency failure.
- Do not spend the next session squeezing the six independent local packing cores: the saturation/barrier evidence says this is unlikely to cross the needed qualitative CF gate.
- Keep the `g=2` simultaneous-factor branch secondary unless it supplies a mechanism directly useful for the exceptional cubic sector.
- Do not confuse small terminal-pair finite scans with the global `R>=2^71` regime.

# RL61 authoritative whole-tree proof state

**Audit date:** 2026-08-23  
**Scope:** the bundled `Collatz_Rsharp` RL research programme through the frozen RL60 state.  
**Audit posture:** skeptical reconstruction; no new deep proof attack was undertaken before the tree reset.

## Executive conclusion

The RL branch is **not closed**. The Collatz conjecture is **not proved** by this project state.

The current frozen terminal-tail object is **not the last open RL branch**. It is the sole surviving object only inside a **restricted safe continued-fraction (safe-CF) stress regime** developed under Gate A. Eliminating it would close that restricted subtree; it would **not** prove the uniform Gate-A theorem and would **not** discharge Gate B.

At the whole-tree level, the audit identifies two genuinely global unresolved obligations in the present architecture:

1. **Gate A — uniform terminal-area/valuation control.** For every retained one-excursion/full-phase terminal geometry, prove
   \[
   H\ge t+3,
   \]
   or replace this by a stronger contradiction that excludes every such geometry.
2. **Gate B — a genuinely global bridge to a closed obstruction.** Use full RL ownership/divisibility/global phase information to force an already-closed local configuration (for example the exact radius-3 theorem) or obtain a direct contradiction. The old local-grammar and RL48 half-period routes do not do this.

A theorem strong enough to rule out the entire retained full-phase object could bypass the explicit Gate-A/Gate-B split, but no such theorem is currently established.

## Gate 0: integrity and provenance

The frozen handover passed the integrity gate.

- Outer archive SHA256 expected and obtained:
  `8c5b5a9c7abd1b552cc9de2202ca276f8eb0e8958c6c27f9561d0c6dee598dd9`.
- Every entry in `SHA256SUMS_RL60_FREEZE_TO_RL61.txt` verified.
- The inherited RL59→RL60 archive sidecar verified unchanged.
- The inherited RL59→RL60 verifier suite passed in this audit environment.
- Selected historical RL18/RL19/RL20 verifiers used to reconstruct radius 3 and the bridge history passed. A full RL20 batch was not promoted as freshly replayed because one long historical verifier exceeded the execution window; this is recorded as a replay limitation, not a theorem failure.

## Authoritative nomenclature

### Radius 3

“Radius 3” means the historical **exact cyclic adjacent-transposition radius-3 theorem** for primitive, `D`-divisible self-rotations satisfying the hypotheses in the RL7–RL19 case tree. It is a **local obstruction theorem**. RL19 closes its final cubic skew leaf.

The phrase **“order-3 extremal” is not an authoritative historical theorem name in the recovered source bundles**. It appeared only in later shorthand. It must not be silently identified with the exact radius-3 theorem.

### Gate A

Gate A is the missing **uniform one-excursion terminal inequality**
\[
H\ge t+3,
\]
with the retained terminal geometry
\[
q=z+t,\qquad t\ge2\text{ even},\qquad H=e-z+1.
\]
The equivalent terminal form `e >= q+2` is a statement about every retained one-excursion/full-phase object, not merely about one continued-fraction denominator.

### Gate B

Gate B is the missing **global RL-to-closed-obstruction bridge**. It must use information that distinguishes a genuine RL object from local endpoint/coboundary countermodels—most importantly global ownership, the full denominator/divisibility condition, and/or equivalent full-phase invariants.

### One-excursion/full-phase

This is the retained structural regime after the inherited reductions leading to the Gate-A terminal problem. It carries exact coupled phase and terminal information. The audit accepts the bundled reduction architecture as the inherited baseline; it does not re-prove every pre-RL18 reduction from first principles.

### Safe-CF

The safe-CF regime is a **restricted denominator/approximation subtree of Gate A** in which the phase squeeze plus the stable external verification floor reaches a Legendre/continued-fraction classification. It is not synonymous with Gate A.

The safe denominator gate is
\[
\ell\le 92{,}524{,}042{,}457{,}747{,}860{,}050.
\]
Below it, exactly one above-`log_2 3` convergent survived the RL50 stress classification:
\[
 a=123{,}139{,}092{,}617{,}126{,}647{,}266,
\]
\[
 \ell=77{,}692{,}117{,}359{,}936{,}589{,}403,
\]
\[
 q=a-\ell=45{,}446{,}975{,}257{,}190{,}057{,}863.
\]
Denominators outside the safe gate remain outside this reduction.

### Current frozen survivor

The RL60 terminal-tail survivor belongs to the **safe-CF subtree of Gate A**, not to the radius-3 theorem. Its exact frozen coupling is
\[
R=z-27,\qquad K=q-z+3,\qquad K+z=q+3.
\]
`K` is odd. RL59/RL60 supply strong terminal-tail consequences, but do not eliminate the object.

## Whole-tree status

| Component | Exact status after RL61 audit | Scope / consequence |
|---|---|---|
| Historical exact radius-3 case tree | **Closed local theorem** | Applies only when the exact radius-3 hypotheses have already been produced. |
| Final RL19 cubic skew radius-3 leaf | **Analytic theorem** | Closed without LMN and without a finite cutoff. |
| Older radius-3 subbranches | **Analytic / finite with explicit inherited dependencies** | Some branches depend on the Laurent–Mignotte–Nesterenko two-logarithm theorem plus finite checking. |
| “Local endpoint grammar forces radius ≤3” | **Dead route** | RL20 exact countermodel. Does not kill the desired global bridge theorem. |
| RL48 direct half-period/four-swap invocation of radius 3 | **Dead route** | RL49 shows the cyclic distance is always even, so it cannot equal exact radius 3. |
| Gate B globally | **Open** | Needs a new genuinely global bridge or a direct full-phase contradiction. |
| One-excursion terminal reduction | **Inherited analytic baseline** | Produces `q=z+t`, even `t>=2`, and Gate-A target. |
| Uniform Gate A `H>=t+3` | **Open** | Global within the retained one-excursion architecture. |
| RL47 q-specific finite exclusions | **Exact finite certificates** | Local instances; not uniform Gate A. |
| RL48 separable rank-relaxation strategy | **Method barrier proved** | Cannot close large-`z` Gate A with only that relaxation; target remains open. |
| Height-one synchronized subsystem | **Exact Collatz conjugacy / warning** | Shows why unconstrained pumping can merely re-embed the shortcut Collatz problem. |
| Safe-CF classification | **Restricted stress regime** | One fixed convergent remains after the continued-fraction reduction. |
| Safe-CF terminal-tail survivor | **Open restricted branch** | Frozen after RL60; not the sole RL survivor. |
| RL60 K31/K33/K35/K37/K39 internal thresholds | **Re-audited exact finite certificates** | Independently re-run in RL61; finite computation, not analytic theorem. |
| External Barina path-record reduction to `K<=129` | **Audited external computational certificate** | Valid conditional on the externally published completeness of the path-record table below `2^71`; stronger than the internal K39 floor for this survivor. |
| Denominator regime above/outside safe-CF gate | **Open / not classified by safe-CF** | A neglected part of uniform Gate A. |
| Full RL closure | **Open** | Requires discharge of the global missing obligations. |

## Radius-3 closure in the tree

Before RL19, the final exact-radius-3 leaf had
\[
\gcd(A,L)=3,\qquad \gcd(A,m)=1,
\]
with
\[
A=3a,\quad L=3\ell,\quad \gcd(a,\ell)=1,\quad ap-m\ell=1,
\]
and the full-denominator sparse condition
\[
1+3\rho^u+9\rho^{u+v}\equiv0\pmod D,
\qquad u+v+w=3a.
\]
RL19 closes this final primitive cubic leaf analytically using the interlacing geometry, the one-gap boundary obstruction, the Eisenstein lift/norm for interior skew, exact resultant nonvanishing in the extreme cases, and periodicity/non-primitivity at equal gaps. Therefore **radius 3 itself is not the current bottleneck**.

## Gate-B history and current state

RL20 proves that the local least-root/final-return grammar alone cannot force a radius-3 pair: an exact packed countermodel has all-rotation minimum distance 4, while failing the genuine RL divisibility condition `D | Q`. This is precisely why a future bridge must use global RL information.

RL43–RL48 reconstructed stronger same-root/full-denominator phase structure. RL48's four-swap construction gave a promising two-way phase relation, but RL49 corrected the crucial geometry: for `d=uv` and the half rotation `vu`,
\[
\operatorname{dist}_{cyc}(uv,vu)=2(a-t-3+H),
\]
which is always even. Hence the direct radius-3 invocation is impossible.

Still-live Gate-B programmes include the RL20 **balanced-return weighted-difference** route, **strict-excursion packing**, or a genuinely new construction that uses full ownership/divisibility to manufacture a pair satisfying the exact closed radius-3 hypotheses. None is yet a theorem.

## Gate-A status and safe-CF scope

RL46/RL47 identify the exact missing inequality
\[
H\ge t+3.
\]
RL48 then proves a barrier to the particular cap/room plus total-displacement separable relaxation: once `z=q-t >= 42`, that relaxation alone cannot exclude every strict violation. This is a dead **method**, not a counterexample to Gate A.

RL50 shows that the synchronized height-one subsystem becomes the exact shortcut Collatz map under `n=(J-1)/2`. Therefore any proposed argument that forgets the full-phase constraints and attempts to settle arbitrary height-one pumping is methodologically unsafe: it risks assuming the global problem one is trying to solve.

The safe-CF reduction covers only the Legendre-compatible denominator range stated above. Killing its one surviving convergent therefore **does not imply the uniform Gate-A theorem**.

## Frozen RL60 increment after re-audit

The internal terminal-ancestor thresholds were independently replayed through
\[
N(39)=122{,}167{,}958{,}641.
\]
The exact threshold table is:

| K | minimal start `N(K)` | `J_min=2N+1` | derived z floor |
|---:|---:|---:|---:|
| 25 | 11,184,810 | 22,369,621 | 9,457,747 |
| 27 | 13,256,071 | 26,512,143 | 11,209,181 |
| 29 | 125,687,199 | 251,374,399 | 106,279,619 |
| 31 | 715,827,882 | 1,431,655,765 | 605,295,637 |
| 33 | 1,908,874,353 | 3,817,748,707 | 1,614,121,697 |
| 35 | 10,180,663,219 | 20,361,326,439 | 8,608,649,047 |
| 37 | 45,812,984,490 | 91,625,968,981 | 38,738,920,711 |
| 39 | 122,167,958,641 | 244,335,917,283 | **103,303,788,559** |

The conversion uses the RL59 terminal-mass estimate and exact parity arithmetic. These are finite certificates, not analytic bounds for arbitrary Collatz trajectories.

The external path-record reduction was also freshly checked. For the fixed safe-CF survivor it yields
\[
25\le K\le129,\qquad K\text{ odd},
\]
so
\[
t=K-3\in\{22,24,\ldots,126\}
\]
and, from `K+z=q+3`,
\[
45{,}446{,}975{,}257{,}190{,}057{,}737
\le z\le
45{,}446{,}975{,}257{,}190{,}057{,}841.
\]
This is classified as an **external computational certificate** rather than an internal analytic theorem.

## Distance to closure

### Is the current safe-CF survivor the last open branch?

**No.** It is one restricted Gate-A subtree.

### If it is eliminated, what closes?

The safe-CF/Legendre-covered survivor subtree closes. The uniform Gate-A problem outside that stress regime remains; Gate B remains.

### Gate A globally

**Open.** The smallest clean theorem target is still the uniform `H>=t+3` for every retained one-excursion/full-phase terminal geometry, or a stronger universal contradiction.

### Gate B globally

**Open.** Radius 3 is already locally closed, but no valid theorem currently forces every genuine RL object into its hypotheses. The direct RL48 half-period match is dead.

### Neglected branches during RL50–RL60

The terminal-tail campaign concentrated on the one safe-CF survivor. Comparatively neglected were:

- the non-safe / above-Legendre denominator part of Gate A;
- RL20's balanced-return weighted-difference bridge;
- RL20's strict-excursion packing bridge;
- arbitrary-radius/global packing structures that use full RL divisibility rather than local endpoint grammar.

### Is anything redundant now?

For the fixed safe-CF survivor, the audited external `K<=129` certificate is numerically stronger than the internal `K>=39`-derived `z` floor. The K39 certificate is **not logically worthless**: it is an independent internal certificate that survives if one refuses the external path-record input. It should therefore remain in the ledger as a fallback, not be deleted.

### Smallest genuinely missing lemmas

1. **Gate A:** a phase-coupled proof of `H>=t+3` for every retained one-excursion terminal geometry, not merely finite `q` or safe-CF cases.
2. **Gate B:** a global ownership/divisibility lemma that either produces an exact radius-3 primitive `D`-divisible pair with all required support/orientation/gcd hypotheses, or yields a direct contradiction before radius 3 is needed.

Until both obligations are discharged, or a stronger theorem bypasses them, RL remains open.

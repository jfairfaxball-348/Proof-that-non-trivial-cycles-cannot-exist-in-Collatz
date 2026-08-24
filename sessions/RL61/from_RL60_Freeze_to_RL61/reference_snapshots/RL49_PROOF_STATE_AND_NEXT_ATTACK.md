# RL49 proof state and next attack

Date: 2026-08-22

## Executive state

RL49 does **not** close the RL branch. It does, however, repair a serious theorem-match error and replace the failed radius-3 shortcut with a substantially tighter arithmetic/structural target.

The current live object is a hypothetical retained one-excursion/full-phase pair

`N --u--> N+4 --v--> N`,

with equal half lengths/weights `|u|=|v|=a`, `wt(u)=wt(v)=ell`, `zeta=2^a/3^ell>1`, and the inherited exact prefix/terminal/rank constraints.

## A. Analytic results established in RL49

### A1. Exact correction of the radius-3 match

For `d=uv` and the half-period rotation `vu`, the cyclic adjacent-transposition distance is

`dist_cyc(uv,vu)=2(a-t-3+H)`.

This is an exact identity. It is always even, so the RL19 exact-radius-3 theorem cannot be invoked on this half-period pair.

A hypothetical full-phase word in the retained one-excursion branch is also primitive; the failed theorem hypothesis is the radius condition, not primitivity.

**Status:** analytic, verifier-backed.

### A2. Full-phase resonance squeeze

With `D=Qx-Qy>=0`, `k=t+3`, and `zeta=2^a/3^ell`, the RL48 phase formula gives

`N(zeta-1)=2zeta+61/9-zeta/2^(k-1)-12D/3^ell`.

Since `zeta^2<16/15`, one has `zeta<31/30`, hence

`N(zeta-1)<398/45`.

**Status:** analytic.

### A3. Height-one synchronized-mass telescoping

At height `d=1`, let `g=2^i/3^p`. On `00`, `gT` is invariant. On `11`,

`g'T'-gT = 2g/3 = 2w`,

where `w=g/3` is the aligned rank weight. Thus on every maximal synchronized height-one segment

`sum_(11) 2w = (gT)_exit-(gT)_entry`.

This exactly removes the neutral-pumping defect that defeated the earlier separable rank relaxation.

**Status:** analytic, regression-verified on the audited RL47 witness.

### A4. Zero-position telescoping coordinates

For internal zero-position sums `Zx,Zy` and normalized quantities `X=Qx/3^r`, `S=Qy/3^r`,

`X=1-g_end+Zx`,

`S=1-g_end+Zy`,

`E=X-S=Zx-Zy`.

The compressed rank identity is

`3Zx-Zy = 12 + (27/2) zeta (1+2^(-k))`.

Under full phase,

`27 N(zeta-1)=127+8S`,

so equivalently

`N(zeta-1)=5+(8/27)(Zy-g_end)`.

**Status:** analytic identities, exact verifier-backed.

### A5. Strengthened phase/Farey denominator floor

Accepting the external recursive-sufficiency extension described below, the phase squeeze implies no full-phase candidate with

`ell < 205632218873398596256`.

The first currently live upper convergent is

`a   = 325919355854421968365`,

`ell = 205632218873398596256`,

`q   = 120287136981023372109`.

The Farey step is analytic once the external state floor is admitted.

**Status:** conditional analytic + exact arithmetic certificate.

## B. External dependencies

### B1. Certified Collatz prefix floor

The strengthened denominator floor uses Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471-480 (2025), specifically the recorded recursive-sufficiency extension from the verified `2^71` prefix to

`R_ext = 4*3^44+2 = 3939083608734444931526`.

This is an **external theorem dependency**. A skeptical next session should independently inspect the paper's proposition/remark and confirm that the interpretation as a lower bound for every state of a hypothetical nontrivial positive cycle is legitimate before relying on the strengthened numerical floor. The internal phase inequality `N(zeta-1)<398/45` does not depend on this paper.

### B2. Inherited radius-3 proof dependencies

RL18/RL19 carry their own external dependency audit, including the older two-logarithm input used in inherited branches. These matter only if a future arithmetic transplant actually invokes the radius-3 sparse theorem. They are not needed for A1-A4 above.

## C. Exact/computational certificates

The release verifier reruns:

- repaired RL48->RL49 baseline suite;
- half-rotation metric identity/regressions;
- phase-resonance/continued-fraction calculations;
- height-one mass telescoping;
- strengthened Ansari/Farey gate;
- zero-position telescoping identities.

The large denominator floor is not a brute-force enumeration of all denominators. It comes from Legendre + exact continued fractions + a Farey-neighbour extension.

## D. Dead or rejected routes

1. **Direct radius-3 shortcut:** `N<->N+4` or a third-bit parity split does not imply RL19 radius 3. Rejected analytically.
2. **Generic bounded-radius bridge:** RL20 already contains countermodels; do not try to show arbitrary RL words have bounded transposition radius.
3. **Separable rank relaxation:** RL48 proved it cannot exclude the live large branch because synchronized height-one mass can be pumped. Replace it with exact telescoping.
4. **Blind larger-q scans:** the surviving scale is `~2e20`; enumeration is strategically wrong. Use symbolic/macroscopic inequalities.

## E. The live proof target

The preferred theorem is:

> **Coupled full-phase one-excursion lemma.** Under the retained one-excursion geometry, exact prefix cap, full-phase quotient condition, and terminal condition `T+1=2^(t+3)`, one must have `H>=t+3`.

Even better:

> **Full-phase impossibility theorem.** No retained one-excursion object satisfies full phase at all.

Either result would be a major closure step. The second would bypass the old Gate-A/Gate-B split.

## F. Recommended technical attack

1. Define normalized monotone lifts on both halves. For a prefix with `i` columns and `p` odd steps, use a state-normalization of the form `2^i B_i/3^p`. Even steps leave the lift fixed; odd steps add an explicit positive increment.
2. Under full phase, one half is trapped between its endpoints. The `v`-lift runs from `N+4` to `zeta N`, so the total strip width is

   `N(zeta-1)-4 < 218/45`.

3. Decompose the one-excursion path into maximal synchronized height-one macroblocks and genuine skew/higher-height excursions.
4. Replace every height-one synchronized macroblock by its exact `(gT)_exit-(gT)_entry` boundary contribution.
5. Under the contradiction hypothesis `H<=t+2`, use `H` to bound the number/size of displaced ranks and the maximum height/displacement.
6. Combine the prefix cap, the compressed zero-position identities, and the narrow strip to obtain a lower bound on required lift growth that exceeds `218/45`, or derive an incompatible terminal valuation.
7. Use the huge `ell` floor only as a scale separator if needed; do not make continued fractions the main proof engine.
8. Only invoke RL19 sparse uniqueness if a derived object is shown line-by-line to satisfy its actual global radius/sparse hypotheses.

## G. Falsification discipline

Every proposed inequality should first be checked on:

- the audited RL47 `(a,ell,t)=(65,41,2)` structural witness (not full phase);
- the inherited RL45 `(65,41,t=0)` proper-factor countermodel;
- synthetic one-excursion paths, especially long synchronized height-one pumps;
- the first presently live continued-fraction scale symbolically, not by enumerating its columns.

Do not infer a theorem from these tests; use them to reject false lemmas cheaply.

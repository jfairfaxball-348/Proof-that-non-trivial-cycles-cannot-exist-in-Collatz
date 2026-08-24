# RL50 proof-state update

Date: 2026-08-22

## Executive state

RL50 has **not** closed the RL branch. It has, however, made three important corrections/advances before any further large-scale attack:

1. repaired a reproducibility defect in the RL49 handover verifier;
2. independently audited and demoted the Ansari-based strengthened external floor;
3. derived a new normalized-lift macro calculus and a uniform phase zero-budget theorem `z>=17`.

The live closure target remains the coupled full-phase/area theorem

`H >= t+3`, equivalently `v2(T+1)<=H` at terminal height one.

## A. Reproducibility repair

The original outer handover ZIP checksum matched its sidecar exactly.

The first release-verifier run stopped because `rl49_research/verify_rl49_half_rotation_metric.py` contained a stale absolute path to an old session workspace. This was a reproducibility/plumbing failure, not a mathematical failure.

The extracted research copy was repaired to resolve the bundled RL48 verifier relative to its own location. After repair, the complete RL49->RL50 handover suite passed.

The original release manifest was not silently rewritten. The extracted tree is now an RL50 working copy with an explicitly documented local repair.

## B. External dependency correction

### Accepted

Barina 2025: computational convergence verification through `2^71`.

### Demoted / presently inadmissible

Ansari 2025 as justification for a certified prefix `4*3^44+2`.

The printed Lemma 3.1 induction identity `F_{n+1}=F'_n\A'` fails at `n=1` by direct residue calculation modulo 36. Therefore the recursive-sufficiency chain on which Proposition 3.2 / Remark 3.1 depends is not presently accepted in this project without a corrected proof.

Consequently RL49's strengthened phase/Farey floor

`ell >= 205632218873398596256`

is demoted. Its arithmetic remains valid as a conditional calculation only.

### Safe continued-fraction stress point

Using only `2^71`, the rigorous Legendre gate is

`ell <= 92524042457747860050`,

and the unique above-beta convergent surviving the RL49 phase inequality below that gate is

`(a,ell,q) = (123139092617126647266, 77692117359936589403, 45446975257190057863)`.

## C. New analytic identities

With internal `g=2^i/3^{p_x}`, height `d`, local gap coordinate `T`, and

`R=gT/3^d`, the normalized lifts satisfy

`U-V=(8/9)R`,

`Delta U=(8/27)xg`,

`Delta V=(8/27)yg/3^d`,

`Delta R=(g/3)(x-y/3^d)`.

On every synchronized fixed-height macroblock,

`Delta V = 8 Delta R/[9(3^d-1)]`.

**Status:** analytic; exact witness regression passed.

## D. New phase zero-budget theorem

From the post-x-zero prefix cap,

`g_i <= (9/16)zeta^2`.

From the safe phase squeeze plus `N>=2^71`,

`zeta^2<136/135`, hence every x-zero weight is `<17/30`.

The exact compressed zero identity gives `Zx>17/2`. Therefore there are at least 16 internal x-zero columns:

`#x-zero >=16`, `z>=17`, `t<=q-17`.

**Status:** analytic; exact rational/verifier-backed.

## E. What remains open

The new theorem is not yet the desired Gate-A closure. The unresolved bottleneck is still the exact height-one valuation mechanism in the inherited Markov quotient

`J=T+3^d-2^d`,

`K=H+d(d+1)/2-1`.

The desired statewise theorem is

`J>0 => v2(J)<=K`.

A `10` descent preserves the violation margin exactly, so the hard part is height one. At `d=1`, odd `J` has two zero-area synchronized maps

`00: J -> (J+1)/2`,

`11: J -> (3J+1)/2`.

Exactly one keeps `J` odd; the other is an even exit. Any next proof must control the 2-adic valuation of these even exits using the phase/prefix/macro data rather than treating synchronized ranks independently.

## F. Recommended next attack

1. Quotient every synchronized fixed-height block using the new `Delta V / Delta R` formula.
2. At height one, replace an arbitrary synchronized string by the deterministic odd-continuation macro plus a single even exit.
3. Carry `g` (or one bounded product such as `g(J-1)`) together with `(H,J)` so the phase prefix cap is not lost.
4. Prove that an even height-one exit with `v2(J)>H` would require either:
   - too much zero mass (`Zx`/`Zy`),
   - too much normalized `v`-lift inside the full-phase strip, or
   - a forbidden prefix-cap excursion.
5. Use the safe huge continued-fraction survivor only as a symbolic stress point, not as an enumeration target.

## G. Files

- `RL50_EXTERNAL_FLOOR_AUDIT_AND_DEMOTION.md`
- `verify_rl50_external_floor_audit.py`
- `RL50_NORMALIZED_LIFT_ZERO_BUDGET_AND_MACROS.md`
- `verify_rl50_lift_zero_budget.py`
- `RL50_EXTERNAL_FLOOR_AUDIT_RUN.txt`
- `RL50_LIFT_ZERO_BUDGET_RUN.txt`
- `RL50_SAFE_PHASE_GATE_RERUN.txt`

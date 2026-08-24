# RL50 final proof state and RL51 roadmap

Date: 2026-08-22

## Executive status

The RL branch is **not closed**. Radius 3 remains an inherited proved/certified component, but the old direct full-phase -> radius-3 shortcut is dead and must not be resurrected.

The live target remains Gate A:

`H >= t+3`, equivalently the inherited terminal valuation inequality `v2(T+1) <= H` at terminal height one.

RL50 materially tightened the genuine full-phase branch and identified the coupling that RL47's rank relaxation was missing.

## 1. Reproducibility state

The source RL49->RL50 outer SHA-256 matched its supplied sidecar.

The inherited `verify_rl49_half_rotation_metric.py` contains a stale absolute workspace path. The original inherited file is preserved unchanged for provenance. This handover supplies `verification/verify_rl49_half_rotation_metric_portable.py`, which resolves the bundled RL48 baseline relative to the handover root.

Run first:

`bash verification/run_all_rl50_handover_verifiers.sh`

Any failure is a stop-and-repair event.

## 2. External-dependency state

### Stable accepted external input

Use Barina's peer-reviewed computational verification through `2^71` as the safe external floor.

### Demoted input

Do **not** use Ansari 2025 to promote the floor to `4*3^44+2`. RL50's exact residue audit finds that the printed induction identity used in Lemma 3.1 already fails at `n=1` modulo 36. The stronger RL49 Farey arithmetic remains valid only conditionally on an independently supplied stronger floor.

### Live project status

RL50 separately observed Barina's live project page at `2075*2^60` on 2026-08-22. Treat this only as a live external-computation corollary, not as part of the stable proof ledger unless independently re-audited.

## 3. Safe continued-fraction stress point

Using only `N>=2^71`, the rigorous Legendre denominator gate is

`ell <= 92524042457747860050`.

There is one surviving above-`log_2(3)` convergent below this gate:

`a   = 123139092617126647266`

`ell =  77692117359936589403`

`q   =  45446975257190057863`.

This is a symbolic stress point, not an enumeration target.

## 4. RL50 structural advances

### 4.1 Normalized lifts and all-height synchronized telescope

With `g=2^i/3^(p_x)`, height `d`, local gap `T`, and

`R=gT/3^d`,

RL50 has exact normalized lifts with

`U-V=(8/9)R`,

`Delta U=(8/27)xg`,

`Delta V=(8/27) y g / 3^d`,

`Delta R=(g/3)(x-y/3^d)`.

Every synchronized fixed-height macro satisfies

`Delta V = 8 Delta R / [9(3^d-1)]`.

### 4.2 Height-one Collatz conjugacy

At height one, `J=T+1` and put

`n=(J-1)/2`.

The deterministic odd-preserving synchronized continuation is exactly the shortcut Collatz map on `n`. In particular the canonical negative pump

`J: -13 -> -19 -> -9 -> -13`

is the negative shortcut cycle

`n: -7 -> -10 -> -5 -> -7`.

Therefore a proof that isolates arbitrary height-one synchronized pumping risks simply re-embedding Collatz. The full-phase/prefix/excursion information is essential.

### 4.3 Monotone J-lift and exact defect energy

Define

`W = gJ/3^d`.

`W` is nondecreasing on all four quotient edges, with `10` the only zero-increment edge. Its full start-to-terminal budget is

`Delta W = 13/3 + (9/2) zeta`.

Define local defect energy

`epsilon_i = 3 Delta W_i - Delta S_i - Delta Zx_i`.

Then `epsilon_i>=0` and globally

`sum epsilon_i = 2E`.

Zero energy occurs exactly on height-one synchronized `00/11` motion and on `10` descents.

For the sole safe continued-fraction survivor:

`S > 45/4`,

`0 <= E < 5/3`,

so total defect energy is `<10/3`.

The separate live `2075*2^60` floor would sharpen this to `E<3/2` if re-accepted.

### 4.4 Post-excursion localization

Before the first positive-energy `01`, the exact negative-cycle grammar has bounded free mass. Combining this with `S>45/4`, `E<5/3`, and the prefix cap forces, after the first genuine excursion departure, at least

- 7 height-one `11` columns, and
- 2 height-one `00` columns.

Thus the sole safe survivor must return to height one and execute at least nine additional free synchronized columns after its first genuine excursion departure.

### 4.5 Zero displacement carries both H and E

Let internal x-zero positions be `u_j` and matching y-zero positions `v_j`, with

`r_j=v_j-u_j>=0`.

Then exactly

`H = sum_j r_j`.

If `w_j` is the x-prefix weight at the j-th zero, then

`E = sum_j w_j [1-(2/3)^(r_j)]`.

Thus Gate-A area `H` and phase defect `E` are two measures of the same displacement vector.

### 4.6 Complete height-one return excursions

At height one define

`L = g(J-1)/2`.

For every complete genuine excursion from height one back to height one,

`Delta L_exc = S_exc + (3/2)E_exc`,

`0 <= S_exc <= E_exc`,

hence

`(3/2)E_exc <= Delta L_exc <= (5/2)E_exc`.

For the sole safe survivor all genuine excursions combined have

`Delta L < 25/6`.

Its first positive height-one return therefore satisfies

`L < 25/6`,

and with the safe prefix cap,

`W < 142/45`.

### 4.7 Sequential prefix-cap zero counts

The exact x-prefix scalar evolves by

`x=1: g -> (2/3)g`,

`x=0: g -> 2g`,

with the safe phase prefix cap. A denominator-independent exact branch-and-bound proves:

- 18 internal x-zeros cannot reach the uniform required `Zx>17/2`;
- 25 internal x-zeros cannot reach the survivor-required `Zx>143/12`.

Therefore:

**Uniform genuine full phase:**

`# internal x-zeros >=19`, hence `z>=20`, `t<=q-20`.

**Sole safe continued-fraction survivor:**

`# internal x-zeros >=26`, hence `z>=27`, `t<=q-27`.

These supersede earlier RL50 `z>=17` / candidate `z>=20` bounds.

## 5. RL47 rank-transport splice

Revisit the inherited RL47 exact rank transport. Its displacement enhancement can be written

`Lambda = sum_j w_j(3-2^(-delta_j))`.

With the RL50 phase quantities,

`Lambda = 2X + E`.

So `E` is exactly the coupling that RL47's older separable area relaxation was missing.

For `z=27`, the strengthened sequential cap leaves only a very small stable gap: exclusion would require approximately

`E < 1.6499581...`,

where the safe published-floor theorem currently gives only

`E < 1.6633648...`.

This miss (~`0.0134`) is real.

Conditionally on the separately tracked live floor giving `E<3/2`, `z=27` would be eliminated. For the sole survivor `q` is odd and `t` is even, so `z=q-t` is odd; eliminating `z=27` would jump to `z>=29`.

However, for `z>=28` the old separable rank envelope is structurally too loose even with `E=0`. Do not spend RL51 merely polishing that envelope.

## 6. Current bottleneck

Gate A is still open. The most focused remaining obstruction is:

1. remove the tiny **stable** `z=27` sliver using an exact coupled x/y prefix constraint or terminal-power congruence; then
2. switch methods for the `z>=29` regime, because the separable rank relaxation has a proved barrier.

The terminal condition `J_end=2^k` and the exact first-positive-return window

`L<25/6`, `W<142/45`

are the intended next coupling points.

## 7. RL51 recommended attack order

### Attack A — close the stable z=27 sliver

Do not use the live external floor as a substitute. Starting from the safe `E<5/3`, combine both x- and y-prefix caps, the exact zero displacement pairing, and/or `J_end=2^k` to save the missing ~`0.0134` in the rank-transport inequality.

A finite state search is acceptable only if its state space is denominator-independent and the exact certificate is bundled.

### Attack B — terminal-power backward macro

If `z=27` is eliminated, stop trying to strengthen the old independent rank envelope. Start at terminal `J=2^k` and run backward through maximal height-one synchronized blocks, using the exact invariants of `00/11`, the small total excursion energy, and the first-positive-return window.

Useful height-one invariants include the normalized `L=g(J-1)/2`; also investigate exact dyadic divisibility carried backward by synchronized `00/11` blocks.

### Attack C — excursion endpoint grammar

Compress each genuine height-one-to-height-one excursion to endpoint data `(g,J,L,E_exc,S_exc)` using

`Delta L=S_exc+3E_exc/2`, `S_exc<=E_exc`.

Use the global `E<5/3` budget to bound the number/type of expensive departures from the Collatz-conjugate zero-energy grammar.

### Attack D — only then reconnect to radius 3

Do not attempt a direct phase-polynomial/radius-3 match. Radius 3 becomes useful only after a valid global-to-local or terminal bridge is actually proved.

## 8. Prohibited shortcuts / red-team reminders

- Do not claim RL or Collatz is solved.
- Do not use Ansari's `4*3^44+2` floor as an accepted theorem.
- Do not treat the live Barina status as equivalent to the peer-reviewed stable floor without re-audit.
- Do not enumerate `~10^20` columns/denominators.
- Do not assume the height-one odd-preserving dynamics is easy: it is exactly Collatz-conjugate.
- Do not infer Gate A from small `E` alone; late tiny weights can hide large unweighted displacement `H`.
- Do not continue the separable RL47 rank envelope past its documented barrier.

## 9. Key files

Read in this order after the verifier run:

1. `RL50_FINAL_PROOF_STATE_AND_RL51_ROADMAP.md` (this file)
2. `rl50_research/RL50_ZERO_DISPLACEMENT_AND_EXCURSION_RETURN_MACROS.md`
3. `rl50_research/RL50_MONOTONE_J_LIFT_AND_DEFECT_ENERGY.md`
4. `rl50_research/RL50_HEIGHT1_CONJUGACY_AND_SURVIVOR_DEFECT_SQUEEZE.md`
5. `rl50_research/RL50_NORMALIZED_LIFT_ZERO_BUDGET_AND_MACROS.md`
6. `rl50_research/RL50_EXTERNAL_FLOOR_AUDIT_AND_DEMOTION.md`
7. inherited RL47/RL48 rank-transport and phase-defect notes under `inherited_rl49_to_rl50/baseline_rl48/inherited/...`.

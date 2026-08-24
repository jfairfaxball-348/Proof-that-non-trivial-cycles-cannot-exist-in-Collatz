# RL58 final proof state and RL59 terminal-embeddability roadmap

Date: 2026-08-23

## Executive status

RL58 did **not** prove Gate A, Gate B, RL, or Collatz, and did not eliminate the sole safe continued-fraction survivor.

It did independently audit and promote both RL57 discovery certificates:

- `M0_26 <= 17/3`;
- `Zx_26 <= 77/10`.

Therefore the survivor satisfies

- `M0_late > 5/4`;
- `Zx_late > 253/60`.

The late suffix contains at least three aligned zeros, at least two separated aligned runs, and at least eight x-zeros in total.

RL58 also found an exact synchronized positive cycle `J=3<->5` that can generate more than `5/4` aligned mass while satisfying the local cap, zero defect, and the sharpened Psi ceiling. Thus the immediate missing lemma is terminal arithmetic, not a generic mass inequality.

## A. Inherited audited baseline retained

Unless a bundled verifier fails, retain:

- `Zx>143/12` strictly;
- `E<5/3` strictly;
- sequential x-zero cap `w_j<17/30`;
- exact defect identity `E=sum_j w_j[1-(2/3)^r_j]`;
- safe-CF survivor with remaining odd `z>=41`;
- z=37 and z=39 closures;
- terminal `J_end=2^K`, `Q_end=2^K+1`;
- `H<K`, terminal `K` odd, and audited `K>=25`;
- radius-3 inherited/certified;
- global Gate A open;
- no valid global Gate-B/RL-to-radius-3 bridge proved.

The complete RL57->RL58 outer handover is preserved under `inherited_rl57_to_rl58/`.

## B. RL58 promoted finite certificates

### B1. Aligned prefix

Independent exact rational gap-based C++ audit:

`RL58_GAP_AUDIT target=17/3 hit=0`.

Promote

`M0_26 <= 17/3`.

Since analytically `M0>83/12`,

`M0_late > 83/12-17/3 = 5/4`.

Immediate consequences:

- at least three late aligned x-zeros;
- at least two separated late aligned runs;
- one uninterrupted all-`00` run cannot supply the requirement because its mass is `<17/15`.

### B2. Total prefix

Independent exact rational gap-based C++ audit:

`RL58_GAP_TOTAL_AUDIT target=77/10 hit=0`.

Promote

`Zx_26 <= 77/10`.

Hence

`Zx_late > 143/12-77/10 = 253/60`.

Since each x-zero weight is `<17/30`, the late suffix contains at least eight x-zeros.

## C. Sharpened terminal potential interface

The inherited sharp phase squeeze gives

`zeta-1 < 199/53126622932283508654080`.

For odd `K>=25`,

`Psi_end < (27/4)(1+delta)(1+2^-25) = 6.750000201165676...`.

Together with the audited `Zx_late>253/60`,

`Psi_cut < 2.533333534499010...`.

This is an analytic consequence of inherited audited phase control plus the RL58-audited `77/10` certificate.

## D. Local grammar status

At height one, displacement `r=0` occurs on a synchronized `00` edge. For even `Q != 2`, `v2(Q-2)` is the maximum possible length of an uninterrupted all-`00` continuation, not necessarily the actual chosen run length.

The complete `r=1` return macro is

`01 (00)^(n-1) 10`,

with

`n=v2(3Q-7)`

and

`Delta Psi=(7/6)M`.

For odd terminal `K`,

`v3(Q_end)=v3(2^K+1)=1+v3(K)`.

## E. Exact obstruction discovered in RL58

At height one,

`J=3 --11--> 5 --00--> 3`

is an exact synchronized positive pump.

For one pump:

- `g -> (4/3)g`;
- aligned zero mass added: `(2/3)g`;
- zero defect;
- `Delta i=2`, `Delta p=1`;
- one aligned x-zero.

For `m` repeated pumps starting with `g0`,

`g_m=g0(4/3)^m`,

`A_m=2g0((4/3)^m-1)`.

Four pumps from `g0=7/20` give `245/162>5/4` aligned mass while respecting the local cap and remaining below the sharpened Psi cut ceiling.

Therefore defect + cap + Psi do not prove `M0_late<=5/4`.

This does **not** show the pump is compatible with the terminal endpoint. RL59 must decide that.

## F. RL59 proof sequence

### Gate 1 — integrity/regression

Run

`bash verification/run_all_rl58_to_rl59_verifiers.sh`.

Treat any failure as stop-and-repair.

### Gate 2 — exact maximal pump-block transformation

For a maximal block of `m` consecutive `J=3->5->3` pumps, derive symbolically:

- changes in `(i,p)` and any inherited exponent counters;
- zero count and aligned mass;
- scalar `g` transformation;
- Xi/Psi transformation;
- phase variables entering terminal `zeta`, `K`, `H`, or denominator relations;
- all legal predecessor branches entering `J=3`;
- all legal successor branches leaving `J=3` or `J=5`.

Do this before broad computational search.

### Gate 3 — terminal entry/exit arithmetic

Work backward from

`Q_end=2^K+1`, odd `K>=25`,

using

`11: Q->2Q/3`,

`10: Q->2Q+1`,

`00: Q->2Q-(3^d-1)`,

`01: Q->2Q/3-3^(d-1)`.

Determine when the backward suffix can hit the pump locus `Q=4` (`J=3`) or `Q=6` (`J=5`). Track at least

- `Q mod 3^n`;
- `v3(Q)`;
- `v2(Q-2)`;
- event counts and scalar scaling;
- terminal `v3(Q_end)=1+v3(K)`.

The ideal new lemma is a congruence/divisibility obstruction to a sufficiently long pump block.

### Gate 4 — split by pump multiplicity

Determine the largest terminal-compatible number of consecutive pumps, or prove a theorem of the form

`m >= m0  =>  K in K_exceptional`,

where `K_exceptional` is finite or otherwise exactly controllable.

A result excluding enough pumping to meet `M0_late>5/4` would eliminate the safe-CF survivor.

### Gate 5 — finite exact certification if appropriate

If an analytic congruence theorem leaves finitely many `K` or terminal residue cases, certify them exactly. Keep the analytic lemma and finite certificate separate in the ledger.

## G. Known non-routes

Do not begin RL59 by:

- arguing separated aligned runs must consume positive defect; synchronized `11` separation has zero defect;
- using only the Psi ceiling to prove `M0_late<=5/4`; the four-pump witness defeats that;
- assuming `Psi_cut` has a useful positive lower bound; a necessary-condition prefix with negative Psi exists;
- spending substantial time tightening `17/3` toward `557/100` before resolving terminal arithmetic.

The `557/100` target remains exploratory and unpromoted.

## H. Pivot criterion

If RL59 rigorously demonstrates that arbitrarily many synchronized pumps can be embedded while preserving **all** exact terminal endpoint, phase, exponent, and survivor constraints, then the local mass route has exposed an unrestricted Collatz-conjugate subsystem. At that point pivot back to the global Gate-A/Gate-B bridge rather than raising local thresholds again.

Do not pivot merely because the local cycle exists. The unresolved question is terminal-compatible embedding.

## I. Success classifications

**Strong:** prove enough synchronized pumping is terminal-incompatible to contradict `M0_late>5/4`, eliminating the safe-CF survivor.

**Significant:** prove a terminal divisibility theorem bounding pump multiplicity or reducing it to finitely many explicit terminal cases.

**Useful:** fully classify pump entry/exit grammar and derive an exact block transformation plus new terminal congruence restrictions.

**Pivot:** rigorously demonstrate an unrestricted terminal-compatible Collatz-conjugate subsystem, justifying return to Gate A / Gate B.

**Failure/repair:** invalidate an RL58 promoted certificate or inherited interface; repair the first broken item before extension.

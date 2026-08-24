# RL54 final proof state and RL55 audit roadmap

Date: 2026-08-23

## Executive status

RL and Collatz are **not closed**.

The exact inherited radius-3 branch remains certified. RL49 invalidated the old direct half-period/full-phase -> radius-3 shortcut. Gate A `H>=t+3` remains open globally, and Gate B / a valid global-to-radius-3 bridge remains open.

Inside the sole inherited safe continued-fraction survivor, RL53 certified the threshold

`z >= 41`.

RL54 has **not** yet eliminated z=41. It did, however, sharpen the z=41 frontier and expose a more promising structural route.

## A. Inherited proof state that should remain unchanged unless an audit fails

1. Exact radius-3 branch: inherited certified result.
2. RL49 correction: natural half-period rotation has cyclic transposition distance `2(a-t-3+H)`, not radius 3; the old direct Gate-B shortcut is invalid.
3. Within the inherited safe continued-fraction survivor, odd cases `z=27,29,31,33,35,37,39` are eliminated.
4. Therefore the sole stable survivor satisfies `z>=41`.

This is **not** a statement about all denominators and is **not** a global Gate-A theorem.

## B. RL54 z=41 exact recurrence

RL54 found a self-seeding defect recurrence that bypasses the handover's expensive initial target `(1,40)`.

For `t=0,...,11`, assuming the last `t` late x-zero weights have already been made terminal-negligible, the exact defect inequality forces the next terminal class to have relaxed cap

`(X,Y)=(t,17)`.

The `Y=17` invariant fails exactly at `t=12`; two fixed cleanup stages use y-cap 18. Thus a layer-by-layer z=41 route needs

`L(t,17)` for `0<=t<=11`, then `L(12,18), L(13,18), L(14,18)`.

The exact rational verifier is:

`rl54_research/verify_rl54_z41_self_seeding_recurrence.py`

## C. RL54 finite terminal certificates

The currently recorded sharp terminal maxima are

`L(0,17)=41`
`L(1,17)=46`
`L(2,17)=47`
`L(3,17)=51`
`L(4,17)=54`
`L(5,17)=59`
`L(6,17)=64`
`L(7,17)=65`
`L(8,17)=70`.

The new RL54 computation is the last one:

`L_terminal(8,17)=70`.

It was obtained by the deterministic exact-x split solver

`rl54_research/verify_rl54_terminal_exactx_split.cpp`

with recorded run

`rl54_research/RL54_Z41_TERMINAL_X8_Y17_EXACT_RUN.txt`.

This advances the z=41 tiny-weight induction through the last nine late x-zero weights. The next sharp layer would be `(9,17)`.

**Audit status:** treat `L(8,17)=70` as an exact finite certificate backed by source and a completed run, but independently rerun/red-team it before promoting it in a new proof ledger.

## D. Uniform defect reduction

Let

`R=z-27`.

RL54 derived, in exact rational arithmetic, the following uniform relaxed terminal budgets inside the inherited survivor:

- through stage `n>=29`, terminal y-cap `R+3` suffices;
- the final two cleanup stages need y-cap `R+4`.

Hence a single terminal-negligibility statement for the largest relaxed cap `(R,R+4)` would dominate the full late-zero cascade for a fixed z.

Verifier:

`rl54_research/verify_rl54_uniform_defect_recurrence.py`.

Important: this is only an **analytic reduction**. It is not itself a terminal theorem and does not prove all z.

## E. Critical correction to the first uniformization target

RL54 then found that the proposed fixed conclusion

`every late weight < 2^-1000 uniformly for all R`

cannot be true over the whole family.

With terminal exponent

`K=q-z+3`

and `R=z-27`, one has the exact invariant

`K+R=q-24 = 45446975257190057839`.

The final x-zero satisfies the lower bound

`w_last >= g_end/2 = 27*zeta / 2^(K+2)`.

Thus for sufficiently small K (in particular the verifier records the obstruction already for `K<=1001`) a fixed `2^-1000` upper bound on the last weight is impossible regardless of terminal arithmetic.

**Audit requirement:** independently reconstruct all definitions (`K`, `R`, `g_end`, `zeta`, final-zero normalization) and verify that the quantifiers really cover the intended inherited survivor before accepting this correction.

## F. New normalized terminal coordinate

RL54 proposes the coordinate

`P = 2^r J`,

where `r` is the remaining late-x-zero allowance.

In this coordinate the backward grammar was rewritten so that the affine correction terms are nonpositive and the `10` move is the sole pure doubling move. At the terminal state the key cancellation is

`P_end = 2^(R+K) = 2^(q-24)`,

independent of R.

This is a structural observation, not yet a complete theorem. The next audit should derive the four transformed moves independently from the inherited `J` grammar and check all divisibility/state-domain conditions.

## G. Exact legal-prefix mass optimization

A second RL54 attack incorporated the actual Markov `J` recurrence into the first-26 x-zero mass optimization.

The verifier reports the exact maximum mass among legal prefixes with 26 x-zeros under the inherited sequential cap as

`34057930625026471931596 / 2954312706550833698643`

=`11.528207745072855...`.

The survivor requires

`Zx > 143/12 = 11.916666666666666...`.

Therefore a contradiction would already follow from the much weaker aggregate bound

`Zx_late < Delta`,

where

`Delta = 4590516512150518575599 / 11817250826203334794572`

=`0.3884589215938109...`.

This is potentially far more useful than forcing every late weight below `2^-1000`.

Verifier:

`rl54_research/verify_rl54_legal_prefix_mass_and_uniform_obstruction.py`.

**Audit requirement:** this is a finite exhaustive/dynamic computation. Verify that its state variables, forced-y rule, height legality, sequential cap, exact weight update and objective agree exactly with the inherited analytical model. In particular check that no legal branch is pruned by an assumption valid only after the terminal bootstrap.

## H. Greedy-prefix local obstruction

The same verifier reports that the old relaxed greedy first-26 x-zero schedule is not a legal Markov prefix: it reaches `(d,J)=(1,-6)` after column 19 and the prescribed x-bit at column 20 has no legal y-bit.

This is strategically important because a future mass argument need not necessarily reach a giant final terminal contradiction: sufficiently strong forcing toward the relaxed greedy schedule may hit a local grammar obstruction first.

**Audit requirement:** reconstruct this prefix by hand or by an independent tiny script. Determine precisely what “greedy” means here and whether the earlier RL53/RL54 statements “first 26 are greedy, u_26=70” were using a relaxed x-only optimization rather than full Markov legality. Repair the wording/proof ledger accordingly; do not allow two different notions of “greedy” to be conflated.

## I. Fixed cut-state window (promising but audit-sensitive)

Using the terminal scaling and a greedy cut, RL54 derived a positive upper bound

`J_cut < 1379`

for the worst `delta=4` case, while the inherited monotone-W lift gives a lower bound approximately

`J_cut > -1318`.

If valid under the intended hypotheses, this collapses an astronomical endpoint problem to fewer than 2700 integer cut states.

This should be red-teamed carefully because it depends on the exact cut, suffix count identities, zeta bound, sign cases and the same “greedy” terminology issue above.

## J. What is definitely still open

- z=41 inside the stable survivor;
- all z>=41 uniformly;
- a theorem proving `Zx_late < 0.3884589215938109...`;
- a rigorous useful theorem in the normalized `P=2^r J` coordinate;
- Gate A globally;
- a valid Gate B / bridge to radius 3;
- denominators outside the inherited safe continued-fraction gate;
- RL closure;
- Collatz.

## K. RL55 audit/review objectives

The next session should **not** begin by computing `L(9,17)`.

Priority order:

### 1. Reproducibility and proof classification

- verify all checksums;
- rerun the lightweight RL54 verifiers;
- rerun the RL53 frontier audit;
- independently rerun `L(8,17)=70` if resources permit;
- classify every RL54 claim as analytic theorem, exact finite certificate, inherited dependency, audit-pending computation, or conjectural strategy.

### 2. Red-team the legal-prefix optimizer

This is the highest-value new claim. Independently derive the state recursion and objective. Check memoization/dominance logic and all admissibility constraints. Confirm or refute `11.528207745...`.

### 3. Resolve the two notions of “greedy”

Audit every earlier use of “first 26 greedy”. If the old statement is only an x-only relaxed extremizer and is not a legal full Markov prefix, rewrite the logical chain explicitly. Determine whether any prior z=37/z=39 closure accidentally required full legality or merely used the relaxed bound before a separate terminal contradiction.

### 4. Audit the uniform correction and `P` normalization

Independently derive `K+R=q-24`, the last-weight lower bound, and the four `P`-moves. Decide exactly which range of R/K is relevant and whether a two-regime theorem (large K terminal-small / small K bounded-height or finite-state) is natural.

### 5. Set a ranked roadmap

Compare at least these routes:

A. prove the aggregate late-mass bound `Zx_late<Delta`;
B. exploit the fixed `P_end` normalization to obtain an R-uniform potential/finite-state theorem;
C. exploit the bounded `J_cut` interval after an appropriate cut;
D. continue z=41 terminal certificates only as a fallback or diagnostic;
E. return to Gate A / global bridge work if the audit shows the terminal route cannot plausibly uniformize.

Rank them by mathematical leverage, dependency risk, and computational scalability.

## L. Non-claims / warnings

Do not claim any of the following:

- RL is solved;
- Collatz is solved;
- Gate A is proved globally;
- Gate A alone closes RL through radius 3;
- the safe continued-fraction survivor covers all denominators;
- z=41 is eliminated;
- `(R,R+4)` terminal-negligibility is proved uniformly;
- all late weights are uniformly `<2^-1000`;
- the new legal-prefix mass bound is an analytic theorem without an audit of its exhaustive finite search;
- the old half-period rotation is a radius-3 bridge.

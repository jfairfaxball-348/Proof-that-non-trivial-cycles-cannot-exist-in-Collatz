# RL57 final proof state and RL58 audit roadmap

Date: 2026-08-23

## Executive status

RL57 did **not** prove Gate A, Gate B, RL, or Collatz, and did not eliminate the sole safe continued-fraction survivor.

It did complete the requested independent audit of the RL56 `33/4` coupled-K prefix certificate and uncovered a potentially cleaner proof interface: force large **aligned** (`r=0`) late zero mass and then attack only separated height-one `00` runs with terminal arithmetic.

The key proof-state distinction is:

- `33/4`: independently audited and promoted;
- `77/10`: exact fresh computation, independent-audit pending;
- `17/3`: exact fresh computation, independent-audit pending;
- local `r=0` / `r=1` grammar formulas: session derivations, should be rechecked line-by-line before theorem use.

## A. Inherited baseline retained from RL56/RL55

Unless an inherited verifier fails, retain:

- strict total requirement `Zx>143/12`;
- strict defect budget `E<5/3`;
- sequential x-zero cap `w_j<17/30`;
- exact defect identity
  `E=sum_j w_j[1-(2/3)^r_j]`;
- the safe-CF survivor has remaining odd `z>=41`;
- z=37 and z=39 closures remain intact;
- terminal grammar uses `J_end=2^K`, `H<K`;
- the inherited oddness/parity interface makes terminal `K` odd;
- radius-3 remains inherited/certified;
- global Gate A remains open;
- no valid global Gate-B/RL-to-radius-3 bridge is proved.

The entire RL56->RL57 handover is preserved under `inherited_rl56_to_rl57/`.

## B. RL57 audit results promoted

### B1. Bundle integrity

The supplied RL56->RL57 outer archive recomputes to

`ccdf108169dedcf5c8eee4c6a35c70e418d01a281141182e369d459835eef591`,

matching its supplied `.sha256` file. The inherited internal checksum manifest also passed during RL57.

### B2. `K>=25` interface

RL57 rechecked the notation splice behind the inherited claim:

- terminal `J=2^K` gives `v2(J)=K`;
- Gate-A counterexample geometry has `H<K`;
- at terminal height one the RL45 internal quotient parameter collapses to `H`;
- the inherited RL45 certificate rules out the relevant `v2(J)>H` states through `H<=23`;
- terminal `K` is odd.

Thus `K<=23` is excluded and `K=24` is parity-excluded, leaving

`K>=25`.

### B3. `Xi/Psi` potential mechanism

RL57 independently rederived the four legal forward increments of

`Xi = g[(T-1)/3^(d-1)+1/2^(d-1)]`,

`Psi = g+Xi/2`,

and found the RL56 signs/equalities consistent. In particular, on every x-zero edge,

`Delta Psi >= w`,

so for a legal segment

`Zx(segment) <= Psi(end)-Psi(start)`.

### B4. Independent audit of the `33/4` certificate

A compact exact C++ search, structurally separate from the bundled Python implementation, returns

`INDEPENDENT_CPP TARGET 33/4 hit False`

with

- nodes: `3,676,571`;
- memo states: `542,063`;
- prune counts: `[0,0,73533,1006639,675890]`;
- maximum selected K: `25`.

These decision statistics reproduce the RL56 computation exactly. The source and fresh output are under `verification/new_rl57/`.

Promote:

`Zx_26 <= 33/4`.

Hence, using `Zx>143/12`,

`Zx_late > 143/12 - 33/4 = 11/3`.

The inherited RL56 consequence `Psi_cut<3.084` may therefore also be used on this survivor-local branch.

## C. New RL57 exact computations — audit pending

### C1. Defect-aware necessary prefix prune

Let a prefix have `d-1` unmatched x-zeros. The current raw difference `D=Zx-Zy` can fall, when those pending zeros are eventually matched, by at most

`(d-1)*(2/3)*(17/30) = (d-1)*17/45`,

because each pending zero has weight `<17/30` and its smallest positive displacement is one.

Therefore survivor compatibility with `E<5/3` requires

`D - (d-1)*17/45 < 5/3`.

The RL57 search implements the survivor-favouring rejection

`D >= 5/3 + (d-1)*17/45  => impossible`.

With the coupled-K terminal viability constraints, a fresh exact run gives

`DEFECT_NOMEMO target=77/10 hit=0`.

Candidate certificate:

`Zx_26 <= 77/10`.

If independently audited, then

`Zx_late > 143/12 - 77/10 = 253/60`.

Do **not** promote this before reimplementation because the current code uses the same RL57 state/search framework that discovered it.

### C2. Global aligned-mass lower bound

From the exact defect identity, every displaced zero (`r>=1`) contributes at least `w/3` to `E`. Therefore

`sum_{r>=1} w < 3E < 5`.

Since `Zx>143/12`, the aligned mass `M0=sum_{r=0} w` obeys the strict analytic bound

`M0 > 143/12 - 5 = 83/12`.

This deduction is analytic once the inherited total and defect bounds are accepted.

### C3. Aligned first-26 search

RL57 augmented the exact prefix state with aligned mass `A`, incremented exactly on height-one `00` x-zero edges, plus the defect-aware viability prune above.

Fresh exact output:

`ALIGNED target=17/3 hit=0`.

Candidate certificate:

`M0_26 <= 17/3`.

If independently audited, combine with `M0>83/12` to obtain

`M0_late > 83/12 - 17/3 = 5/4`.

Because every zero weight satisfies `w<17/30`, this would force at least **three** late aligned zeros: two zeros together have mass `<17/15<5/4`.

This is the main RL58 audit target.

## D. Target-8 diagnostic

The old viability relaxation has a target-8 first-26 witness with total prefix mass about `8.172852`.

RL57 replayed its x-path exactly and found:

- first 25 matched-zero defect
  `4870305608057692485004 / 2954312706550833698643`
  `=1.6485409947...`;
- 26th pending x-zero weight
  `1180591620717411303424 / 2954312706550833698643`
  `=0.3996163365...`;
- even if the pending zero later gets the minimal displacement one, the final defect is at least
  `1.7817464402... > 5/3`.

So this witness is defect-incompatible. The exact replay script is supplied in `verification/new_rl57/verify_target8_witness_defect.py`.

This diagnostic explains why adding the inherited defect budget can materially strengthen the prefix bound.

## E. Local grammar found in RL57 — recheck before promotion

### E1. `r=0`

Rank displacement zero occurs on a height-one `00` edge. At height one, with `Q=J+1`, a forward `00` step satisfies

`Q-2 -> (Q-2)/2`.

Away from the fixed `Q=2` case, a maximal consecutive height-one `00` run beginning at `Q` has length

`v2(Q-2)`.

If the first zero in the run has weight `g`, a run of length `m` carries aligned mass

`g(2^m-1)`.

Since the final zero of the run is still `<17/30`, any single such run has total mass

`<17/15`.

Therefore the candidate strict late requirement `M0_late>5/4` cannot be supplied by a single consecutive `00` run; at least two separated late aligned runs would be required.

### E2. `r=1`

The session reconstruction gives a maximal displacement-one macro of the form

`01 (00)^(n-1) 10`,

at heights `1 -> 2 -> ... -> 2 -> 1`.

A candidate arithmetic characterization derived in-session is

`v2(3Q-7)=n`

for the height-one entry variable `Q`, and the potential calculation gives

`Delta Psi = (7/6) M`

for the zero mass `M` in such a macro.

These formulas are useful fallback structure but should be independently derived in RL58 before use. The primary route should first try to avoid the `r=1` grammar entirely via the stronger aligned-mass localization.

### E3. Terminal `3`-adic fact

At the terminal point

`Q_end = 2^K+1`,

with odd `K>=25`. LTE gives

`v3(Q_end)=v3(2^K+1)=1+v3(K)`.

This exactly controls the terminal backward `11` run. A final aligned `00` is not itself forbidden: its backward predecessor can be `Q=2^(K+1)`. Hence the contradiction must constrain **multiple separated** aligned runs and their intervening excursions, not merely rule out one last `00`.

## F. RL58 audit/proof sequence

### Gate 1 — integrity and regression

Run `verification/run_all_rl57_to_rl58_verifiers.sh`. Stop on any failure.

Then, if practical, rerun the inherited RL56->RL57 verifier suite as a regression check.

### Gate 2 — independent `17/3` implementation

Reimplement the aligned-prefix decision in a genuinely different structure. Preferred options:

- dynamic programming keyed by exact `(i,p,d,J,K-compatible interval)` with aligned objective stored separately;
- a rational branch-and-bound implementation that does not reuse RL57 Pareto code;
- a second language implementation.

Audit every prune direction, especially:

- sequential cap strictness;
- forced-y transition rule;
- same-K selector;
- W interval;
- Xi/Psi cut constraints;
- total-mass viability;
- defect lower-bound prune;
- aligned-objective upper bounds;
- memo/Pareto dominance;
- strictness at exactly `17/3`.

If the independent result differs, repair before proceeding.

### Gate 3 — secondary audit of `77/10`

Independently reimplement the defect-aware total-prefix target. This is useful corroboration but is secondary if `17/3` survives.

### Gate 4 — promote or reject aligned localization

If `M0_26<=17/3` is independently verified, promote the strict theorem

`M0_late>5/4`.

Then explicitly promote:

- at least three late aligned zeros;
- at least two separated late height-one `00` runs;
- one-run cap `<17/15`.

### Gate 5 — terminal divisibility attack

Use the inherited exact backward maps

`11: Q -> 2Q/3`,

`10: Q -> 2Q+1`,

`00: Q -> 2Q-(3^d-1)`,

`01: Q -> 2Q/3-3^(d-1)`,

with:

- odd `K>=25`;
- `Q_end=2^K+1`;
- `v3(Q_end)=1+v3(K)`;
- the strict candidate requirement `M0_late>5/4`;
- exact event counts and the sequential cap.

Primary theorem target:

`M0_late <= 5/4`.

Because the lower bound is strict, a weak upper bound is sufficient.

The likely proof object is not a single run but the transition grammar between two or more separated height-one `00` runs. Track the exact `Q mod 3^n`, `v3(Q)`, and `v2(Q-2)` data through the intervening excursion.

## G. Fallback hierarchy

If `17/3` fails independent audit:

1. repair the first invalid prune or dominance relation;
2. retain the independently verified `33/4` theorem and `Zx_late>11/3`;
3. return to the original RL56 target `M_{r<=1}>2/3` and exact displacement-0/1 grammar.

If `17/3` survives but `M0_late<=5/4` is false:

1. identify an explicit repeatable separated-`00` macro;
2. compute its weight growth and exact `Q` transformation;
3. test terminal compatibility via `Q mod 3^n` and `v3(Q)`;
4. if only finitely many terminal `K` remain, certify them exactly;
5. if an unrestricted Collatz-conjugate subsystem remains, stop raising survivor-local thresholds and pivot back to the global Gate-A/Gate-B bridge problem.

## H. Success classifications for RL58

**Strong:** independently verify `17/3` and prove `M0_late<=5/4`, eliminating the safe-CF survivor.

**Significant:** independently verify `17/3` and prove a terminal divisibility theorem reducing separated aligned runs to a bounded explicit remainder.

**Useful:** independently verify `17/3` and `77/10`, plus fully audit the `r=0`/`r=1` local grammar.

**Failure/repair:** invalidate any new RL57 certificate or local lemma; repair the first broken interface before extension.

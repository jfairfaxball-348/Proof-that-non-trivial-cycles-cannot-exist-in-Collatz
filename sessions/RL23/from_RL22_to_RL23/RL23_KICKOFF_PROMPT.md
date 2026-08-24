# RL23 research-session kickoff

Continue the Collatz R-sharp / RL research from this handover as a skeptical research mathematician.

## Start-up discipline

1. Read `continuation/RL22_PROGRESS_FREEZE.md` first.
2. Read the RL21/RL22 notes needed for the two live fronts below.
3. Run every verifier in `continuation/verify_rl21_*.py` and `continuation/verify_rl22_*.py` before extending the proof.
4. There are 10 available RL21/RL22 verifier scripts in this bundle. Treat any failure as a stop-and-repair event.
5. Do **not** redo the already-audited radius-3 branches or RL20/RL22 work unless a verifier fails or a new argument directly exposes a contradiction in a frozen lemma.
6. Maintain a strict ledger distinguishing proved analytic facts, results conditional on the inherited external least-state floor `R >= 2^71`, exact finite certificates/computational evidence, and exploratory conjectures.

RL remains open. Exact radius 3 remains closed under the inherited audited hypotheses/dependencies. The live bottleneck is the global bridge.

## Track A — push global integer packing beyond 1/4

The current strongest theorem, valid for `R >= 160`, is

`log(lambda)/L <= log(1 + 1/(4R-1)) <= 1/(4R-1)`.

Under the inherited external floor `R >= 2^71`, the exact continued-fraction certificate gives

`L/gcd(A,L) >= 57,212,717,233`.

The next relevant convergent denominator is `65,470,613,321`, so the current gate does not cross it.

Primary files:
- `continuation/RL22_TERMINAL_HIGH_PACKING_AND_CF_GATE.md`
- `continuation/verify_rl22_terminal_high_cf_gate.py`
- `continuation/RL22_LOW_CHAIN_PACKING_AND_CF_GATE.md`
- `continuation/verify_rl22_low_chain_cf_gate.py`

Try to exploit transition ownership of high states more sharply than the terminal-high block decomposition. Look for longer exact induced odd-map blocks, injective pairings/matchings with stronger high-state lower bounds, restrictions on consecutive high transition types, or a telescoping block product stronger than the current one.

Goal: either prove an analytic coefficient strictly below `1/4` (ideally enough to cross `65,470,613,321`) or prove a rigorous obstruction showing that this local packing method saturates at `1/4`.

Do not use universal proper-prefix supercriticality: leastness does not imply it because additive prefix terms can rescue an undercritical multiplicative prefix.

## Track B — global upper bound for the order-3 cubic ownership mode

For a three-way balanced return with equal-density macroblocks, write

`B=2^b`, `Y=3^e`, `C=B^2+BY+Y^2`,

with block numerators `U,V,W` and balanced integer states

`R`, `x=R+G`, `y=R+H`.

The cubic relative condition is equivalent to

`U-W = HY + GB`,

`V-W = H(B+Y) - GY`.

Thus the Eisenstein lattice coordinates are the physical state gaps. If the three states share `r` parity bits then `2^r | G,H`. In the near-resonant three-way balanced branch the three states begin `11`, and primitivity gives the global lower bound

`max(|U-W|, |V-W|) >= 4(2B+Y)`.

Primary files:
- `continuation/RL22_CUBIC_PREFIX_LATTICE_OWNERSHIP.md`
- `continuation/verify_rl22_cubic_prefix_lattice.py`
- `continuation/RL21_BALANCED_CYCLOTOMIC_MODES.md`
- `continuation/verify_rl21_balanced_cyclotomic_cofactor.py`

Seek a genuinely GLOBAL upper bound on `|U-W|` and/or `|V-W|`, using actual cycle ownership, suffix domination, block endpoint inequalities, or another integer-state mechanism, strong enough to meet or contradict the lower bound `4(2B+Y)`.

This is the preferred bridge into the already-closed cubic/radius-3 Eisenstein machinery.

Important scope rule: the stronger `Q`-range uniqueness statements in `RL22_CUBIC_PREFIX_LATTICE_OWNERSHIP.md` are **conditional** on an additional strict-supercritical macroblock-prefix package. They are not global cycle theorems.

## Secondary branch — g=2 simultaneous factors

Continue this only if it helps the main bridge. For `g=2`, the full integer-cycle condition splits into

`X-Y | U+V`,

`X+Y | U-V`.

The second factor alone is insufficient: an exact countermodel at `(a,ell)=(65,41)` has integer gap `x-R=4` and satisfies `X+Y | U-V` while failing the absolute `X-Y` factor.

Primary files:
- `continuation/RL21_G2_PROPER_FACTOR_DECOMPOSITION.md`
- `continuation/verify_rl21_g2_proper_factor_countermodel.py`
- `continuation/RL21_BALANCED_RETURN_DIVISIBILITY_AND_COUNTERMODEL.md`
- `continuation/verify_rl21_balanced_return_countermodel.py`
- `continuation/RL21_INTEGER_GAP_SYNCHRONIZATION.md`
- `continuation/verify_rl21_integer_gap_synchronization.py`

## Retired / forbidden shortcuts

Do not revive without genuinely new input:

- second-rotation full-`D` divisibility as an independent constraint;
- bounded transport radius from local slope geometry alone;
- the uncorrected RL20 coboundary increment (R20G.12 dropped `3^{-E_{j+1}}`);
- universal all-proper-prefix supercriticality from leastness;
- cubic relative congruence alone as uniqueness;
- proper-factor gap divisibility alone as the full `g=2` cycle condition.

Read `continuation/RL21_RL20_GEOMETRY_REPAIR.md` before using any RL20 strip/coboundary identities.

## Research discipline and closeout

Work Track A and Track B in parallel. Prefer analytic lemmas plus exact symbolic verifiers over larger scans. If a proposed theorem fails, freeze a minimal exact countermodel and state exactly which hypothesis is missing.

Before closing the session, produce:

1. an updated proof-status/branch ledger;
2. exact verifier(s) for every newly frozen lemma or countermodel;
3. a short assessment of distance to a genuine RL contradiction;
4. a zipped handover bundle and kickoff for the next session if RL remains open.

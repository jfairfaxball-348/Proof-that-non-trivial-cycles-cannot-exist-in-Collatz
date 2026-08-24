# START HERE — RL27

The next session should not redo radius-3 closure or the already-audited RL21--RL26 branches unless a verifier fails.

## 1. Startup

1. Verify `SHA256SUMS.txt`.
2. Run every `continuation/verify_rl*.py` script. There should be **19 PASSes**.
3. Read, in this order:
   - `RL26_PROOF_STATUS_AND_NEXT_ATTACK.md`
   - `continuation/RL24_TYPEI_HIGH_START_SUPPORTING_LINE.md`
   - `continuation/RL25_CUBIC_RANGE_ORIENTATION_AND_HARD_SECTOR.md`
   - `continuation/RL26_FIVE_BIT_LOW_STATE_AND_CUBIC_HARD_SECTOR_SIEVE.md`
   - `continuation/RL23_LOCAL_PACKING_SATURATION_WITNESS.md`
   - `continuation/RL23_LOCAL_DYNAMICAL_PACKING_BARRIER.md`

If any verifier fails, stop and repair before using the associated lemma.

## 2. Frozen proof frontier

### Track A

For `R>=161`, the strongest analytic rational packing majorant has asymptotic coefficient

`457841/1843200 ~= 0.248394639756944`.

Under the inherited external input `R>=2^71`, the exact finite CF certificate gives

`L/gcd(A,L) >= 57,397,300,723`.

The next relevant denominator remains `65,470,613,321`, so the qualitative CF gate is not crossed.

Purely local packing is strategically constrained by the exact RL23 saturation family and the finite-window asymptotic barrier `1/(6 log 2) ~= 0.24044917`. Do not spend a session merely retuning the same independent local block inequalities.

### Track B

In the near-resonant order-3 balanced branch, with `z=B/Y` and `Delta` the cubic numerator range:

`Delta < Y[(4/5)e - 3 + 3(2/3)^e]` globally within the branch.

If `H>G`, the stronger orientation bound is

`Delta < Y[(8/15)e - 2 + 2(2/3)^e]`.

The four orientation/root-residue lattice minima before the common factor `4` are:

- `R==1 mod3`, `G>H`: `3B+Y` — unique weak sector;
- `R==1 mod3`, `H>G`: `3B+2Y`;
- `R==2 mod3`, `G>H`: `3B+2Y`;
- `R==2 mod3`, `H>G`: `2B+3Y`.

The five-bit least-state sieve forces near-minimum odd phases to lie in

`{7,15,27,31} mod32`.

Only root residue `27 mod32` retains the weak vector. Hence the weak sector is confined to

`R==91 mod96`.

Inside the inherited exceptional RL20 weak-close branch it is

`R==91 mod288`.

At exact shortest-vector equality:

`G=12, H=4`.

The hard root therefore begins `11011...`.

## 3. Primary RL27 attack

Attack the surviving exceptional geometry by coupling **all four** of the following pieces simultaneously:

1. forced least-root prefix `11011...` and `R==91 mod288` in the inherited weak-close branch;
2. exact cubic extremal geometry `G=12, H=4`;
3. the RL20 exceptional final return `(n_close,t_close)=(1,1)`;
4. the RL23 Track-A saturation mechanism / valuation-density anchors.

The target is a genuinely nonlocal lemma about the **adjacent block numerator and valuation structure**. Useful outcomes include:

- exclusion of the extremal geometry in a true cycle;
- a forced extra common prefix / gap divisibility beyond the universal level;
- a frequency restriction on the high-valuation exceptional block;
- a numerator-difference cancellation that removes a substantial part of the remaining factor `e`;
- a closure/valuation incompatibility between the root side and the exceptional final return.

## 4. What not to overclaim

- The finite terminal-pair result `(b,e)=(65,41)` is an **exact finite certificate only**. It is not the global cycle regime under the inherited `R>=2^71` floor.
- The CF floor `57,397,300,723` depends on inherited external computation `R>=2^71`.
- The RL23 saturation witnesses are finite exact trajectory segments, not cycles.
- `R==91 mod288`, `G=12`, `H=4` characterize the surviving extremal/weak-close geometry under the stated branch hypotheses; they do not themselves produce a contradiction.

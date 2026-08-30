# RL188 — extremal triple-terminal spacing and N35 crossover

Date: 2026-08-30

## 0. Outcome and classification

RL188 continues the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)` from the RL187 target.

It does **not** eliminate the `{35,36,37}` triple family outright, close the high branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

It does prove the requested span-inflation alternative. The sole RL187 density-`3/38` witness cannot recur at 38, 39, or 40 chronological phases. Consequently extremal triple terminals are separated by at least 41 phases, the effective `N_35` density drops to `3/41`, and the previously vacuous `N_35` cap crosses below the clean-start population.

Promoted results:

1. **RL188.1 — exact full-prefix terminal-rank core** (analytic + exact finite integer/rational certificate).
2. **RL188.2 — odd predecessor reset and exact 38-phase triple block** (analytic).
3. **RL188.3 — 38/39/40 terminal-spacing obstruction** (analytic + exact finite integer/rational certificate).
4. **RL188.4 — `N_35` crossover at density `3/41`** (analytic combinatorics + exact integer certificate).

No correction or demotion is required.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`B=A-L=80448749305`, `R=2L-A=57079296007`,
`CLEAN=10075174499`.

Retain RL181/RL183/RL184:

- every ordinary normalized p-gap lies strictly in
  `(128081997553,293591818782)`;
- the chronological mechanical residue advances by `B mod L`;
- `c=1` below `R` and `c=2` at or above `R`;
- on a common-mechanical ordinary pair transition,
  `2^c delta' = 3 delta + epsilon`,
  where `epsilon=2^-b-2^-a` and `|epsilon|<1`;
- `3|C_i` iff the predecessor defect `G_(i-1)` is even;
- the clean family consists of `10075174499` physical 40-edge corridors, with the carry and ordinary mechanical-switch crossings removed over the relevant 39 transitions.

Retain RL187:

- the sole density-`3/38` witness for `N_35` is one co-owned terminal family
  `tau={35,36,37}`;
- its shared terminal invariant is
  `(C_tau,H)=(3^37,21)`;
- without that triple, every block has `N_35` density at most `2/37`;
- the raw RL187 joint terminal-rank compatibility for the triple begins at
  `r=65145319435`;
- `N_36<=7238318174`, `N_37<=7052720272`;
- ordinary corrected-flow variation remains `>443`.

All statements below stay internal to the same high branch and RL184 clean starts.

## 2. RL188.1 — full 37-zero-prefix gap corridor

Fix a physical triple terminal at phase `t`. Its `tau=37` start is at `t-37`, and the 37 preceding pair defects are zero.

For a zero-defect transition the normalized p-gap obeys

`2^c delta' = 3 delta`.

The terminal gap is exact:

`delta_t = 3^37 / 2^21`.

For a proposed terminal mechanical residue `r`, the actual 37-bit mechanical word is not free: it is the unique factor obtained by rotating backward from `r` by `B mod L`. Propagating `delta_t` backward through that exact word and imposing the inherited strict gap corridor at **every** one of the 38 physical p-edges removes the outer portions of the RL187 raw terminal-rank interval.

The exact surviving necessary core is

`72797034370 <= r <= 103818202602`.

Its width is

`31021168233`

integer ranks.

No rank in this interval is asserted to be physically realized. This is a necessary localization theorem only.

A useful byproduct is that the normalized gap at the `tau=37` start can only be

`2^37` or `2^38`.

## 3. RL188.2 — predecessor reset and exact block span

RL187 gives

`C_t = 3^37 odd(C_(t-37)) = 3^37`.

Hence the `tau=37` starting numerator has odd part one: it is a power of two and is not divisible by 3.

RL182's exact first ternary digit therefore gives

`G_(t-38)` odd.

In particular, `G_(t-38) != 0`.

Thus an extremal triple is not merely contained in a block of span at least 38. The immediately preceding phase is already a nonzero defect, so its defect block has exact span 38.

This statement uses the physical predecessor sensor; it is not inferred from an arbitrary ternary word.

## 4. RL188.3 — extremal terminals cannot occur 38, 39, or 40 phases apart

Let

`E=[72797034370,103818202602]`

and let its diameter be

`31021168232`.

Chronological phase advance adds `B mod L` to the mechanical residue.

### Separation 38

`38B mod L = 31435476726`.

Both this displacement and its cyclic complement exceed the diameter of `E`. Therefore two triple terminals cannot both lie in `E` at chronological separation 38.

### Separation 40

`40B mod L = 54804930024`.

Again both the displacement and its complement exceed the diameter of `E`. Separation 40 is impossible for the same exact rank reason.

### Separation 39

Rank alone does not exclude 39, so use the boundary dynamics.

Every `r in E` lies in the late mechanical class, so `c_t=2`. One chronological step later,

`r_(t+1)=r+B mod L`

lies in

`[15717738363,46738906595]`,

strictly below `R`, so `c_(t+1)=1`.

The clean 40-edge corridor contains the two ordinary common-mechanical transitions `t -> t+1 -> t+2`. Write their defect corrections as `epsilon_0,epsilon_1`, with `|epsilon_j|<1`. Then

`4 delta_(t+1)=3 delta_t+epsilon_0`,
`2 delta_(t+2)=3 delta_(t+1)+epsilon_1`.

Therefore

`delta_(t+2)
 = 9 delta_t/8 + 3 epsilon_0/8 + epsilon_1/2`

lies strictly within `7/8` of

`9 delta_t/8 = 3^39/2^24`.

If another triple terminal occurred at `t+39`, its `tau=37` start would be exactly `t+2`, whose normalized gap must be either `2^37` or `2^38` by RL188.1. Both values are more than `7/8` away from `3^39/2^24` (in fact by tens of billions). Contradiction.

Finally, a later triple terminal cannot lie within 37 phases because its required preceding 37-zero run would contain the earlier nonzero terminal.

Hence consecutive triple terminals are separated by at least 41 chronological phases.

## 5. RL188.4 — `N_35` density `3/41` and crossover

Partition the cyclic defect sequence into blocks ending at nonzero defects, as in RL187.

A nontriple block has `N_35` density at most `2/37`. A triple block owns three `N_35` starts and, by RL188.2, has span 38.

If there are no triple blocks, the global density is already below `3/41` because

`2/37 < 3/41`.

Otherwise group each triple block with the following nontriple blocks up to the next triple block. If those intervening blocks have total span `S`, RL188.3 gives `S>=3`.

- If they own no `N_35` starts, the group density is at most
  `3/(38+S) <= 3/41`.
- If they own at least one `N_35` start, then `S>=36`, and their total owned count `K` satisfies `K<=2S/37`. Hence
  `3+K <= 3+2S/37 <= 3(38+S)/41`,
  since the last inequality is equivalent to `29S>=333`, true for `S>=36`.

Every group therefore has density at most `3/41`, so

`N_35 <= floor(3L/41) = 10063027705`.

This is below the clean-start count by

`10075174499 - 10063027705 = 12146794`.

Thus at least

`12146794`

clean starts have first nonzero defect at offset at most 34.

This is the first genuine `N_35` crossover. It is a distribution theorem, not a contradiction closing the branch.

## 6. Charging consequence and remaining barrier

The inherited RL187 weighted-flow certificate remains valid unchanged. The new `N_35` crossover separates a nonempty `tau<=34` population from the extremal late tail, but the inherited charge assigns the same weight to all `tau<=35` starts. RL188 therefore does not promote a larger corrected-flow floor merely from this crossover.

A stronger consumer now needs to exploit the newly forced `tau<=34` population with offset-sensitive defect height, sign, boundary cost, or phase location, rather than treating `tau<=35` as one charge class.

## 7. Verification and scope

`verification/verify_rl188_extremal_triple_spacing_n35_crossover.py` independently reconstructs the RL187 triple rows, derives the raw joint rank support, propagates the exact 37-step mechanical gap word, certifies the rank core, checks the 38/40 displacement exclusions, checks the exact 39-step affine mismatch, and certifies the `3/41` density and integer crossover.

No arbitrary mechanical word, ternary residue, or affine map is promoted as physical. The triple itself remains an open physical possibility. No branch or global closure claim is made.

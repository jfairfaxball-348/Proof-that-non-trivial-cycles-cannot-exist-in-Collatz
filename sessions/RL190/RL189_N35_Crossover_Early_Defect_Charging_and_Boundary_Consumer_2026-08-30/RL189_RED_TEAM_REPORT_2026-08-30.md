# RL189 red-team report

Date: 2026-08-30

## Scope

Adversarial review of the two promoted RL189 claims: spacing `>=43` and the two-level early-defect charging obstruction.

## Checks passed

1. **Corridor indexing.** The spacing-41 proof does not borrow an unproved `tau=34` extension. An extremal terminal is co-owned by a clean `tau=35` start; a 40-edge corridor beginning at `t-35` contains the four transitions through `t+4` required by the hypothetical second triple's `tau=37` start.

2. **Rank overlap.** `41B mod L=135253679329`; the exact simultaneous terminal-rank overlap is `[75071400353,103818202602]`. `42B mod L=78174383322` gives empty overlap.

3. **Mechanical words.** The separation-41 overlap splits exactly at `90789138715/90789138716`, yielding only `2121` and `2122`.

4. **Affine error.** Iterating `|epsilon|<1` gives strict radii `119/64` and `119/128`; both are tiny compared with the exact distances to the permitted `2^37,2^38` triple-start gaps.

5. **Density grouping.** For an intervening nontriple span with at least one `N_35` start, `S>=36`; the new inequality reduces to `25S-555>=0`, so no small-span exception is hidden.

6. **Charging direction.** The guaranteed lower-bound coefficients have the correct cap direction because the proposed split is monotone. The height-21 family `{33,34,35}` alone gives `2x+y<=2^-22`, and the old flat point is independently inherited as feasible against all families.

## Claims deliberately rejected

- No isolated-triple impossibility.
- No physical-realization claim for the terminal-rank core.
- No flow improvement beyond RL187's `>443`.
- No claim that all finer phase/sign charging schemes fail.
- No branch or global closure.

## Verdict

PASS for promotion with the scope locks above.

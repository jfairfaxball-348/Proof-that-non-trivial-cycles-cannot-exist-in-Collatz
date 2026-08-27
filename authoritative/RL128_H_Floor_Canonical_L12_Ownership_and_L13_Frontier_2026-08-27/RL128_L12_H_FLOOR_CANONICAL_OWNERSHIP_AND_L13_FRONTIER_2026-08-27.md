# RL128 — `L=12` H-floor tail, canonical ownership, and the `L>=13` frontier

## Outcome and classification

RL128 excludes the complete `L=12` parameter range and advances the inherited primitive ordinary frontier:

> Every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L>=13`.

The result combines proved analytic mathematics with an exact finite certificate. It does **not** close Gate A or Gate B, exclude all nontrivial cycles globally, or prove Collatz.

## 1. Exact positivity threshold and analytic tail cut

For `L=12`, write

`D=2^(12+Z)-3^12`,

`B=(2^Z-1)(3^12-2^12)`,

and use the inherited physical width ceiling `D W <= B` together with the RL123 floor

`W >= H(12,Z)=min_t max(E_0(Z,t),E_1(12,t),6(t-1))`.

The denominator is negative at `Z=7` and positive at `Z=8`, so the positive ordinary range begins at `Z=8`.

Exact finite evaluation gives

- `H(12,40)=121`;
- `H(12,41)=129`;
- no `H`/width contradiction occurs for any `8<=Z<=40`.

For `Z>=12` the minimization set is fixed at `t=1,...,12`. Each `E_0(Z,t)` is nondecreasing in `Z`, so every fixed-`t` maximum and hence their pointwise minimum `H(12,Z)` is nondecreasing. Therefore `H(12,Z)>=129` for all `Z>=41`.

On the width side, exact simplification gives

`129D-B = 1039*2^Z - 68,028,544`.

The right side is positive from `Z=16` onward. Hence for every `Z>=41`, `B/D<129`, contradicting `W>=H(12,Z)>=129`.

Thus only the finite strip `8<=Z<=40` requires ownership enumeration.

Classification: **proved analytic mathematics**, within the inherited ordinary physical-ownership framework.

## 2. Cyclic-root divisibility is rotation invariant

For a binary word `w` of length `A=L+Z` with `L` ones, let `Q(w)` be the inherited shortcut numerator and `D=2^A-3^L`. Let `w'` be the one-bit cyclic left shift.

If the leading bit is `0`, all one-positions decrease by one and

`Q(w')=Q(w)/2`.

If the leading bit is `1`, the leading one becomes the final one. Directly from the ordered numerator formula,

`2Q(w')=3Q(w)+D`.

Now `D` is odd and `D` is coprime to `3`. In either case,

`D | Q(w)  <=>  D | Q(w')`.

Iterating the one-bit shift proves that `D|Q` is invariant under **every cyclic root** of the word. Therefore the finite certificate need test only one root of each canonical primitive run-pair orbit; all bit roots are covered analytically.

Classification: **proved analytic/combinatorial lemma**.

## 3. Primitive run-pair compression

Every transition-rooted word is represented by positive alternating run pairs

`(o_1,z_1),...,(o_t,z_t)`.

A proper binary period must carry a transition root to another transition root, so a transition-rooted binary word is periodic exactly when its cyclic run-pair list is a repetition of a shorter pair block. Consequently pair-periodicity is an exact primitivity test in this enumeration.

For every primitive pair orbit the verifier selects the lexicographically least pair rotation. The orbit weight is `t`. The certificate aborts unless summed orbit weights equal the complete ordered primitive capacity-profile count.

Classification: **proved combinatorial compression**, with a machine-checked orbit-weight invariant.

## 4. Corrected constrained capacity enumeration

For every `Z=8,...,40`, the verifier computes `U=floor(B/D)` and enumerates every positive odd-run composition of `12` and every positive zero-run composition of `Z` that can satisfy the inherited physical capacity inequalities.

It applies only valid inherited floors:

- the one-fibre odd-side bound;
- the one-fibre zero-side bound;
- the `6(t-1)` boundary floor;
- the depth-sensitive CRT fibre bounds with **empty fibres ignored**, retaining the RL126 repair.

Two early rejections are exact consequences of the same inequalities, not heuristic sieves:

1. the aggregate zero-side `E_0(Z,t)` floor may reject a run count `t` before composition generation;
2. because every zero run is nonempty, the `k=1` CRT counts depend only on the odd composition and may be checked before zero enumeration.

The remaining CRT counts are computed exactly from run-position masks. No branch is discarded unless one of the inherited capacity inequalities is already impossible.

## 5. Exact finite certificate

The gap-free `Z=8,...,40` certificate records:

- capacity-feasible ordered profiles: `1,559,151,385`;
- periodic profiles: `8,839`;
- ordered primitive profiles: `1,559,142,546`;
- canonical primitive run-pair representatives: `160,979,484`;
- orbit-weight total: `1,559,142,546`;
- canonical `D|Q` tests: `160,979,484`;
- divisibility hits: `0`.

The equality

`orbit_weight = capacity_profiles - periodic`

is exact both row-by-row and in total. The capacity population is already empty for `Z=37,38,39,40`.

Because cyclic-root divisibility is analytically invariant, one exact `D|Q` test per canonical primitive representative covers every cyclic binary root. The zero-hit result therefore excludes the complete finite residual strip.

Together with the analytic `Z>=41` tail, all positive `L=12` candidates are excluded, proving the stated `L>=13` frontier in the inherited primitive ordinary framework.

Classification: **exact finite certificate + analytic coverage lemma**.

## 6. Verification provenance and implementation red teams

The certificate was generated gap-free over all 33 values `Z=8,...,40`. During development, the optimized pair-periodicity/canonical-root implementation was checked against the earlier direct binary-periodicity/all-root implementation on overlapping ranges, including the previously recorded `Z=22` case; the finalized implementation was additionally cross-checked against the earlier counts on `Z=8,...,12` and `Z=30` with exact equality.

The fast suite performs:

- exact `H`/width arithmetic checks;
- structural audit of all 33 certificate rows, totals, `U`, zero-hit status and orbit identities;
- independent exact regeneration at representative low/middle/high endpoints `Z=8,16,23,27,34,36,40`.

`verification/run_full_rl128_certificate.sh` is supplied for complete gap-free reproduction of every row.

RL20 ownership, RL79 scaling, RL81 physical-state ownership, primitivity separation, Raw/Farey scope, finite-certificate scope, and the RL126 empty-fibre correction all carry forward unchanged. A divisibility hit would remain only a necessary-condition event; none occurs here.

## 7. RL129 kickoff

Continue the same corrected programme at `L=13`: establish the exact positive `Z` range and smallest inherited `H(13,Z)`/width tail contradiction, then run a gap-free nonempty-fibre constrained capacity certificate on the finite residual. Preserve the cyclic-root invariance lemma and orbit-weight ownership compression proved here.

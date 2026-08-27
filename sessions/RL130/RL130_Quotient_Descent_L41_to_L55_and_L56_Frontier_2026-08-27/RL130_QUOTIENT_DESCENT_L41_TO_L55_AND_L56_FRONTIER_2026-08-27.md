# RL130 — quotient descent for `L=41..55` and the `L>=56` frontier

## Outcome and classification

RL130 excludes every primitive positive ordinary shortcut-cycle candidate with `41<=L<=55` and advances the inherited low-odd-count frontier from `L>=41` to `L>=56`. This is not Gate A/B closure, global nontrivial-cycle exclusion, or a proof of the Collatz conjecture.

- The quotient-rotation identities, universal transition-root bound, and monotonicity in `Z` are inherited **proved analytic mathematics**.
- The table below is an **exact finite arithmetic certificate**.
- Descent of every odd quotient through `6,496,657,853` is an **exact finite certificate**.
- The promoted primitive ordinary frontier `L>=56` follows from those inputs plus the inherited primitivity argument.

## Exact quotient ceiling

For a shortcut word with `L` ones and `Z` zeroes, take a cyclic transition root that starts in `1` and ends in `0`. The inherited result gives `Q <= 2^(Z-1)(3^L-2^L)`. If `D=2^(L+Z)-3^L` divides `Q`, the quotient `n=Q/D` follows the halved Collatz map under cyclic rotation. Its largest possible value at fixed `L` is reached at the smallest `Z` for which `D>0`, because the exact ratio is strictly decreasing thereafter. Exact integer evaluation yields:

| L | first positive Z | quotient ceiling |
|---:|---:|---:|
|41|24|727,618,641|
|42|25|48,112,900|
|43|26|42,033,752|
|44|26|168,743,266|
|45|27|112,134,919|
|46|27|1,022,322,057|
|47|28|318,914,455|
|48|29|300,103,100|
|49|29|1,020,725,483|
|50|30|784,921,997|
|51|30|4,377,141,931|
|52|31|2,161,006,927|
|53|32|2,156,480,283|
|54|32|6,496,657,853|
|55|33|5,548,555,735|

The global ceiling is `6,496,657,853`, at `(L,Z)=(54,32)`.

## Exact descent certificate and primitivity

The compiled verifier scans each of the `3,248,328,927` odd starts through that ceiling. For each start, exact halved-Collatz iteration ends at `1` or a smaller positive integer; induction over odd starts then proves descent to the trivial `1<->2` orbit. The largest observed pre-lower-value excursion is `3,562,942,561,397,226,080`, below `2^64`, and the verifier explicitly aborts on an arithmetic overflow.

An integrality event yields a cyclic quotient parity word. Since every such quotient here reaches `1<->2`, its parity word is a repetition of `10`. That cannot be the primitive word of a nontrivial candidate. Therefore the full interval `41<=L<=55` is excluded.

## Denominator diagnostic

Set `alpha=log_2(3)`, `A=ceil(L*alpha)`, and `delta=A-L*alpha`. Substitution of `3^L=2^(A-delta)` into the quotient ratio gives exactly `R_L=2^(Z-1)(1-(2/3)^L)/(2^delta-1)`. So the quotient route has an intrinsic `2^Z` scale, with an extra factor when `L*alpha` lies just below an integer. For diagnostics only, the continued fraction of `alpha` begins `[1;1,1,2,2,3,1,5,2,23,...]`; upper convergent `65/41` gives the first small `delta` in this block. This does not change the exact finite proof or yield a global ceiling law.

## Scope and obligations

No inherited mathematical theorem is demoted. The RL126 empty-depth-fibre repair and RL129 outer-sidecar integrity repair remain explicit inherited ledger entries. Ownership, scaling, physical representative, Raw/Farey, and finite-certificate limitations remain in force.

Frozen scope: primitive ordinary frontier `L>=56`; Gate A open; Gate B open; global nontrivial-cycle exclusion open; Collatz conjecture not proved.

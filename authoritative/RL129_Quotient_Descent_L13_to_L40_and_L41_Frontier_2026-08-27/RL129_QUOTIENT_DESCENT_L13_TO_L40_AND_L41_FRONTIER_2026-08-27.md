# RL129 — quotient descent for `L=13..40` and the `L>=41` frontier

## Outcome and classification

RL129 excludes every primitive positive ordinary shortcut-cycle candidate with `13<=L<=40` and advances the inherited low-odd-count frontier from `L>=13` to:

> Every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L>=41`.

The new route is substantially simpler than the finite capacity enumeration originally proposed for RL129.  It uses the RL128 cyclic-rotation algebra to turn any divisibility event `D|Q` into a bounded positive integer Collatz cycle, then eliminates every possible quotient by an exact finite descent certificate.

This is **not** a closure of Gate A or Gate B, does not globally exclude nontrivial cycles, and does not prove the Collatz conjecture.

Classification:

- quotient/rotation identities and the universal quotient bound: **proved analytic mathematics**;
- `L=13..40` quotient-ceiling table: **exact finite arithmetic certificate**;
- descent of every odd integer through the global ceiling: **exact finite certificate**;
- promoted primitive ordinary frontier `L>=41`: **proved from the preceding analytic lemmas plus exact certificates**.

## 1. Inherited notation

For a binary shortcut word `w` of length `A=L+Z`, with `L` one-bits and `Z` zero-bits, write

`D = 2^A - 3^L`

and, if the one positions are

`0 <= p_0 < ... < p_(L-1) <= A-1`, write the inherited numerator

`Q(w) = sum_{j=0}^{L-1} 2^(p_j) 3^(L-1-j)`.

A positive integral cycle representative requires `D>0` and `D|Q`.

RL128 proved that `D|Q` is invariant under one-bit cyclic rotation.  If `w'` is the one-bit left rotation of `w`, then:

- if the leading bit is `0`, `Q(w')=Q(w)/2`;
- if the leading bit is `1`, `2Q(w')=3Q(w)+D`.

RL129 keeps these identities and extracts their quotient consequence.

## 2. Quotient dynamics lemma

Assume `D|Q(w)` and put `n=Q(w)/D`.

For a one-bit left rotation `w -> w'`, put `n'=Q(w')/D`.  The inherited rotation identities give exactly

- leading bit `0`: `n'=n/2`;
- leading bit `1`: `n'=(3n+1)/2`.

Parity is automatic.  A zero-leading word has even `Q`, hence even `n` because `D` is odd.  A one-leading word has odd `Q`, hence odd `n`.

After all `A` cyclic rotations the word returns to itself, so the successive quotients form a positive integer cycle under the halved Collatz map

`T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.

Thus a `D|Q` event is not merely an abstract divisibility event: it supplies an integer quotient cycle with the same parity word.

## 3. Universal transition-root bound for `Q`

Every cyclic word containing both symbols has a transition root that starts with `1` and ends with `0`.  Use such a root.  Then `p_0=0`, the final bit is zero, and

`p_(L-1) <= A-2`.

Because the one positions are strictly increasing, for every `j`

`p_j <= A-L-1+j = Z-1+j`.

Therefore

`Q <= sum_{j=0}^{L-1} 2^(Z-1+j) 3^(L-1-j)`

and the finite geometric identity gives

`Q <= 2^(Z-1) (3^L - 2^L)`.

If `D|Q`, the chosen transition root starts with `1`, so `Q` and the quotient `n=Q/D` are odd.  Consequently

`n <= floor( 2^(Z-1)(3^L-2^L) / (2^(L+Z)-3^L) )`.

No physical-width floor, CRT capacity enumeration, Farey sieve, or run-profile scan is used in this bound.  Those inherited restrictions can only shrink the candidate population further.

## 4. The quotient ceiling decreases with `Z`

Fix `L`, let `C=3^L-2^L>0`, and put `x=2^Z`.  In the positive-denominator range,

`R_L(Z) = 2^(Z-1) C / (2^(L+Z)-3^L) = C x / (2(2^L x-3^L))`.

As a function of positive `x` beyond the pole, this is strictly decreasing, since its derivative has numerator `-C*3^L < 0` up to the positive square denominator.

Therefore the largest possible quotient for fixed `L` occurs at the **smallest** integer `Z` for which `D>0`.  An unbounded scan over `Z` is unnecessary.

The exact verifier computes that smallest `Z` for each `L=13,...,40`, evaluates the integer quotient ceiling there, and checks the discrete monotonicity identity by exact cross multiplication.

## 5. Exact `L=13..40` quotient certificate

The exact ceilings are:

| L | first positive Z | quotient ceiling |
|---:|---:|---:|
|13|8|403|
|14|9|338|
|15|9|1,509|
|16|10|914|
|17|10|13,008|
|18|11|2,652|
|19|12|2,414|
|20|12|8,833|
|21|13|6,375|
|22|13|43,146|
|23|14|17,811|
|24|15|17,308|
|25|15|55,036|
|26|16|44,871|
|27|16|213,474|
|28|17|121,814|
|29|17|2,587,328|
|30|18|357,039|
|31|19|318,595|
|32|19|1,218,108|
|33|20|845,251|
|34|20|6,538,683|
|35|21|2,381,808|
|36|22|2,278,708|
|37|22|7,484,047|
|38|23|5,932,914|
|39|23|30,400,121|
|40|24|16,216,346|

The global maximum is therefore

`n <= 30,400,121`,

attained by the bound at `L=39, Z=23`.

All arithmetic in this table is exact integer arithmetic.

## 6. Exact descent certificate below the global ceiling

Because the transition-root quotient is odd, the verifier checks every odd integer

`1 <= n <= 30,400,121`.

There are exactly `15,200,061` such starts.

The C++ verifier processes odd starts in increasing order.  For a current odd start `n`, it iterates the exact halved Collatz map until it reaches `1` or any positive value `<n`.  Reaching a smaller value is sufficient by induction: if the smaller value is odd it was already verified; if it is even, repeated exact halving reaches an already verified smaller odd value (or `1`).

The complete scan passes with no overflow and no exception.

Hence every possible quotient arising from `D|Q` for `13<=L<=40` reaches the trivial `1 <-> 2` cycle.

If a cyclic parity word itself returns after `A` rotations while its quotient orbit is `1 <-> 2`, its parity word is a repetition of `10`.  For `L>=13` that word is nonprimitive.  Therefore no primitive nontrivial candidate in `13<=L<=40` can satisfy the necessary integrality condition.

This establishes the promoted frontier `L>=41`.

## 7. Independent red teams

`verification/verify_rl129_rotation_redteam.py` exhaustively checks all nonconstant binary words of lengths `2..12` and confirms:

- the two one-bit rotation identities for `Q`;
- the universal transition-root `Q` bound whenever a word starts in `1` and ends in `0`;
- the induced quotient update on every small exact `D|Q` event with `D>0`.

The red-team totals are:

- rotation words checked: `8,166`;
- transition-root bounds checked: `2,047`;
- exact divisible rotation events checked: `12`.

`verification/verify_rl129_quotient_bounds.py` independently regenerates the `L=13..40` positivity thresholds and exact quotient ceilings and asserts the global maximum `30,400,121` at `(L,Z)=(39,23)`.

`verification/verify_rl129_descent.cpp` independently certifies descent for all `15,200,061` odd starts in the required range.

## 8. Scope and inherited ledgers

No inherited promoted theorem is demoted.

The RL126 empty-depth-fibre correction remains in force, although RL129's promoted proof does not need the CRT capacity machinery.  RL20 ownership, RL79 scaling, RL81 physical-state ownership, primitivity separation, Raw/Farey scope, finite-certificate discipline, verification economy, and sustained-attack rules remain inherited.

The originally proposed RL129 `L=13` H-floor/capacity enumeration is superseded by this stronger quotient route and is not needed for the promoted result.  No incomplete exploratory capacity count is used as evidence.

Frozen global scope after RL129:

- primitive ordinary low-odd-count frontier: `L>=41`;
- Gate A: open;
- Gate B: open;
- global nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

## 9. RL130 direction

RL130 should extend the quotient-descent frontier beyond `L=40`.  The same exact formula gives a first target ceiling of `727,618,641` at `L=41`, so the route remains computationally plausible.  The next session should combine exact incremental descent certification with analytic study of the minimal-positive-`Z` denominator to determine how far the quotient method can be pushed efficiently and whether it can be coupled to an inherited global gate.

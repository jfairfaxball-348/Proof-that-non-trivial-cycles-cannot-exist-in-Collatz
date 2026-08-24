# RL69 — third backward digit, phase match, mod-54 lift, and nested `H>=6`

Date: 2026-08-24

## Status

RL69 continues from the checksum-clean authoritative RL68 state under the mandatory **verification economy rule**. The current RL68 outer sidecar, freshly unpacked internal `SHA256SUMS.txt`, `verification/run_fast_rl68_verifiers.sh`, and root/inside-ledger byte identity all passed before new mathematics was attempted. Historical expensive certificates were not recursively rerun.

RL69 does **not** prove uniform odd-`k` Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The principal new advances are:

1. the RL68 `Q` digit already recovers the parity of the rank immediately before `p`, including the zero-displacement case;
2. that state-side bit matches exactly the next (`q=3`) full-phase rank-tail digit;
3. the RL68 nested selector lifts from `delta_* mod 6` to `delta_* mod 18`;
4. after retaining the first visible low-height correction on each side of `b_p`, one obtains the full residue of the state immediately before `b_p` modulo `9`;
5. the higher digit lifts `delta_*` further to a unique class modulo `54`;
6. the nested terminal lower bound improves analytically from `H>=5` to `H>=6`.

The remaining obstruction is still global: the state and phase ladders now agree through one more rank, but no size/order contradiction forces `H>=k` for every odd terminal exponent.

---

## 1. Frozen notation

Retain RL68 notation. In a nested `g=0` last-two-active interface,

`b_p < b_* < a_p < a_*`,

with

`beta=b_*-b_p`, `lambda=a_p-b_*`, `mu=a_*-a_p`,

so

`delta_p=beta+lambda`, `delta_*=lambda+mu`.

Let `C` be the height-three `J`-state immediately before `a_p`, `T_C=C-19`, and let `R` be the height-one state immediately after `a_*`. RL67/RL68 give

`C-10=2^(delta_*-lambda)(2R-5)`.

RL68 defines

`Z=(2^lambda(C-19)+1)/3`

and

`Q=2^(beta-1) Z (mod 9)`.

It proves `Q in {1,7}` and, if `b_p` has a preceding y-one `b_(p-1)`, then with

`gamma=b_p-b_(p-1)`

one has

- `Q=1` iff `gamma` is odd;
- `Q=7` iff `gamma` is even.

All congruences below use the exact RL recurrence and preserve ordered rank data. No separable rank relaxation is used.

---

## 2. One-rank-earlier parity is already in `Q`

Assume the immediate preceding rank `q=p-1` exists. Put

`r_q=a_q-b_p`.

Then

`delta_q=a_q-b_q=(a_q-b_p)+(b_p-b_q)=r_q+gamma`.

### Theorem 2.1 — immediate-rank parity selector

The parity of `delta_q` is determined exactly by `Q` and `r_q mod 2`:

- if `Q=1`, then `delta_q == r_q+1 (mod2)`;
- if `Q=7`, then `delta_q == r_q (mod2)`.

Equivalently, if `eta_Q=1` for `Q=1` and `eta_Q=0` for `Q=7`, then

`boxed: delta_q == r_q+eta_Q (mod2)`.

This includes `delta_q=0`: a zero-displacement rank is correctly selected as even.

### Proof

RL68 gives `gamma mod2` from `Q`. Since `delta_q=r_q+gamma`, the result is immediate. QED.

Classification: **analytic corollary of RL68**.

This is the first direct extension of the nested backward ladder from the previous active rank `p` to the rank immediately before `p`.

---

## 3. Exact match with the next full-phase rank-tail digit

Let

`E_j=2^(b_j)(2^(delta_j)-1)`.

For the three-rank tail define

`C_3=E_*+3E_p+9E_q`.

The RL66 phase ladder gives, under full-phase extendability,

`N == 2-2^(1-k)-4*3^(s+1)2^(-a)C_3 (mod 3^(s+4))`.

Let

`R_2 = 2-2^(1-k)-4*3^(s+1)2^(-a)(E_*+3E_p)`.

Modulo `3`,

- `E_q==0` if `delta_q` is even;
- `E_q==2^(b_q)` if `delta_q` is odd.

### Theorem 3.1 — state/phase match one rank earlier

Under full-phase extendability,

`boxed: N == R_2 - chi_q 4*2^(b_q-a)3^(s+3) (mod 3^(s+4))`,

where

`chi_q=0` if `delta_q` is even and `chi_q=1` if `delta_q` is odd.

By Theorem 2.1, `chi_q` is determined from the RL68 state-side digit `Q` and the local offset `a_q-b_p`.

Thus the next full-phase digit is:

- zero exactly when the state-side one-rank-earlier selector says `delta_q` is even;
- nonzero exactly when it says `delta_q` is odd.

Classification: **analytic theorem**, conditional on the same frozen full-phase hypothesis as the RL66/RL67 phase ladder.

This is a genuine state/phase ladder match, but it is not yet a contradiction: both sides can remain compatible.

---

## 4. The RL68 `Q` digit lifts `delta_*` from mod `6` to mod `18`

RL68 gives

`Z=(2^(delta_*)(2R-5)-9*2^lambda+1)/3`.

Since

`Q == 2^(beta-1) Z (mod9)`,

we have

`Z == 2^(1-beta) Q (mod9)`.

Multiplying the terminal formula for `Z` by `3` gives:

### Theorem 4.1 — mod-27 terminal compatibility

`boxed: 2^(delta_*)(2R-5)`

`       == 9*2^lambda -1 +3*2^(1-beta)Q (mod27)`.

Here `2^(1-beta)Q` is evaluated modulo `9` before multiplication by `3`.

Because `2R-5` is a unit modulo `3`, it is invertible modulo `27`. Also `2` has order `18` modulo `27` (`2^9==-1 mod27`). Therefore:

### Corollary 4.2 — exact mod-18 selector

`boxed: (R mod27, lambda mod6, beta mod6, Q) determines delta_* mod18 uniquely.`

Classification: **analytic corollary**.

This strictly refines RL68's `delta_* mod6` table. It is still a congruence selector, not a size bound.

---

## 5. The third backward digit: `T` immediately before `b_p` modulo `9`

The next lift requires retaining the first low-height correction that becomes visible modulo `27`.

Assume `q=p-1` exists and write `A=a_q`; if it does not exist, take the three correction trits below to be zero.

Define three local correction trits in `Z/3Z`:

`chi = 1` if `A=b_p`, else `0`;

`kappa = 2^(A-b_p-1) (mod3)` if `b_p<A<b_*`, else `0`;

and

- `alpha=0` if `A<b_*`;
- `alpha=1` if `A=b_*`;
- `alpha=2^(A-b_*) (mod3)` if `A>b_*`.

These are the only corrections visible at the next 3-adic precision.

### Lemma 5.1 — post-`b_*` correction compression

Let `T_-` be the state immediately before `b_*`. Then

`boxed: Z == T_- + 9 alpha (mod27)`.

### Proof

RL68's exact ordered descent polynomial shows that, after division by `3`, every earlier x-closure except the latest one is divisible by `27`. Rank order makes the latest earlier x-position exactly `A=a_(p-1)` when it lies at or after `b_*`.

- If `A<b_*`, no earlier x-term survives after `b_*`.
- If `A=b_*`, the simultaneous x-term occurs at pre-height three and contributes `27/3=9`.
- If `A>b_*`, the last y-silent closure contributes `18*2^(A-b_*-1)=9*2^(A-b_*) mod27`.

QED.

### Lemma 5.2 — between `b_p` and `b_*`

Let `T_p^+` be the state immediately after `b_p`. Then

`boxed: 2^(beta-1)T_- == T_p^+ + 9 kappa (mod27)`.

Only a closure at pre-height three can survive modulo `27`; by rank order this is precisely `a_(p-1)` when `b_p<A<b_*`.

### Lemma 5.3 — the `b_p` update

Let `T_p^-` be the state immediately before `b_p`. Then

`boxed: 2T_p^+ +1 == 3T_p^- +9 chi (mod27)`.

If `A=b_p`, the immediate preceding rank closes at pre-height two and contributes `9`; every other simultaneous earlier closure occurs at pre-height at least three and vanishes modulo `27`.

Combining the three lemmas gives the new digit.

### Theorem 5.4 — third backward digit

Define

`U = 2^(beta-1)(Z-9alpha)-9kappa (mod27)`.

Then

`boxed: U == T_p^+ (mod27)`

and the unique residue `V mod9` satisfying

`boxed: 3V == 2U+1-9chi (mod27)`

is exactly

`boxed: V == T_p^- (mod9)`.

Classification: **analytic theorem**.

RL68 knew only the nonzero trit `T_p^- mod3`. RL69 recovers the full residue modulo `9` while retaining the one visible correction from the rank immediately before `p`.

---

## 6. The third backward digit lifts `delta_*` to mod `54`

Reverse Theorem 5.4 at the same precision. From `V`, define

`U_V = (3V+9chi-1)/2 (mod27)`

and

`W = 2^(1-beta)(U_V+9kappa)+9alpha (mod27)`.

Then `W==Z mod27`.

Substitute the terminal form of `Z`:

### Theorem 6.1 — mod-81 terminal compatibility

`boxed: 2^(delta_*)(2R-5)`

`       == 9*2^lambda -1 +3W (mod81)`.

Since `2R-5` is a unit modulo `81` and `2` has order `54` modulo `81`, this yields:

### Corollary 6.2 — exact mod-54 selector

`boxed: (R mod81, lambda, beta, V, alpha, kappa, chi)`

`       determines delta_* mod54 uniquely.`

Classification: **analytic corollary**.

This is a threefold lift over RL68's mod-18-free state: mod `6` -> mod `18` -> mod `54` as the backward state precision increases.

It still does not bound the integer size of `delta_*`.

---

## 7. Nested terminals satisfy `H>=6`

RL68 proved `H>=5`. RL69 eliminates equality.

Recall

`delta_p+delta_*=beta+2lambda+mu>=4`.

Assume `H=5`.

There are only two structural possibilities.

### Case A — the last two active ranks consume all five units

Then there is no earlier active rank and

`beta+2lambda+mu=5`.

Since `beta,lambda,mu>=1`, the only possibilities are

`(beta,lambda,mu)=(1,1,2)` or `(2,1,1)`.

The previous active rank `p` is therefore the first active rank, so its entry is one of the canonical RL67 first-mismatch values

`P_0 in {-6,-28,-4}`.

For `(1,1,2)`, the exact active block is

`01,01,10,00,10`

and direct composition gives

`boxed: R=(9P_0+102)/32`.

For `(2,1,1)`, the block is

`01,00,01,10,10`

and

`boxed: R=(9P_0+136)/32`.

For each of the three allowed `P_0`, the resulting value is either nonintegral or below the inherited terminal-suffix requirement `R>=3`. Hence Case A is impossible.

### Case B — the last two active ranks consume four units

Then

`beta=lambda=mu=1`,

so `delta_p=delta_*=2`, and exactly one earlier active rank `q` has displacement `1`.

Because `delta_q=1`, its x-one is in the column immediately after its y-one. Therefore either:

1. `q` closes before the next y-one and is isolated; or
2. its closing x-one is shared with the y-one of `p`.

No zero-displacement rank can occupy that same column because x-one positions are strictly increasing.

#### B1. `q` isolated

The RL67 first-isolated classification says displacement `1` forces

`P_0=-6` and the height-one exit `A=-3`.

From `-3`, the only possible even synchronized exits before the next mismatch are `-4` and `0` (RL67's exact small synchronized orbit).

The minimal nested last-two-active block

`01,01,10,10`

has

`boxed: R=(9P+62)/16`.

For `P=-4` or `P=0`, the value is nonintegral (and in the first case below `3`). Contradiction.

#### B2. `q` shares its closing column with `p`

The whole active block is

`01,11,01,10,10`.

Direct composition gives

`boxed: R=(27P_0+160)/32`.

For all `P_0 in {-6,-28,-4}`, this is below `3`. Contradiction.

Thus `H=5` is impossible.

### Theorem 7.1

`boxed: every nested terminal path has H>=6.`

Classification: **analytic theorem**.

This strengthens the nested local floor but does not close global `k=5`, because separated/cross `H=3,4` cases remain analytically open.

---

## 8. Exact bounded audit

`verification/verify_rl69_third_backward_digit.py` independently recomputes canonical RL states directly from the exact recurrence through `MAX_M=18`.

Fresh results:

- bounded canonical terminal paths: `2,596`;
- nested `g=0` terminal interfaces: `1,222`;
- nested interfaces with `q=p-1` present: `1,222`;
- one-rank-earlier parity-selector checks: `1,222`;
- bounded full-phase `q=3` digit matches: `1,113`;
- nested `delta_* mod18` lifts: `1,222`;
- third backward `T mod9` checks: `1,222`;
- nested `delta_* mod54` lifts: `1,222`;
- nested `H>=6` checks: `1,222`;
- status: `RL69 third-backward-digit verifier: PASS`.

The script also independently reconstructs the four affine blocks used in the analytic `H=5` obstruction.

The bounded verifier is a falsification/audit tool. It is not the infinite proof of the analytic statements above.

---

## 9. Routes tested but not upgraded

### F1. Treat phase matching as a contradiction

Rejected. The new `q=3` state digit and phase digit agree exactly, but agreement is compatibility, not an impossibility theorem.

### F2. Treat `delta_* mod18` or `mod54` as a size bound

Rejected. A residue class modulo `18` or `54` does not control the unbounded representative.

### F3. Blindly lift the RL68 stack invisibility

Rejected. At the next modulus, the lowest-height earlier closure becomes visible. RL69 keeps exactly that correction through `alpha`, `kappa`, and `chi`; higher closures vanish only after their divisibility is proved.

### F4. Claim an odd-terminal-tail class is eliminated unconditionally

Not done. The all-`00`, mixed, nonmaximal all-`11`, and maximal all-`11` splits remain compatible with the new local congruence selectors in general. No unconditional tail-class elimination was proved in RL69.

### F5. Promote `J<=2^H`

Not done. Its inherited conjectural status is unchanged.

---

## 10. Exact proof state after RL69

Retain every RL62-RL68 correction, theorem, finite certificate, and demotion.

New RL69 analytic upgrades are limited to:

1. immediate rank `q=p-1` displacement parity is selected by RL68 `Q` plus `a_q-b_p mod2`;
2. that parity matches the next full-phase rank-tail digit modulo `3^(s+4)`;
3. the nested terminal selector lifts `delta_*` to a unique class modulo `18`;
4. an exact third backward state digit recovers `T` immediately before `b_p` modulo `9` with only three local correction trits;
5. that digit lifts `delta_*` to a unique class modulo `54`;
6. every nested terminal path satisfies `H>=6`.

Gate A remains open globally for unbounded odd `k`. Gate B remains frozen/open/audit-dependent.

The live obstruction has moved again: the local state ladder and the full-phase rank-tail ladder now agree through the rank immediately before `p`, but compatibility has not yet been converted into a nonseparable size/order contradiction.

---

## 11. Recommended RL70 attack

1. **Push one more rank using the new `V mod9` digit.** Let `q=p-1`. Propagate from `T_p^- mod9` back across `b_q`, retaining the unique height-two closure term if `q` closes before `b_p`. The goal is a compact residue for the state immediately before `b_q`, not a full prefix replay.
2. **Match the `q=4` full-phase digit.** The next phase term is `27 E_(p-2)`. Seek a state-side selector for `delta_(p-2) mod2` from the new backward digit.
3. **Exploit the mod-54 selector against small-area violations.** In a hypothetical `H<k`, combine the selected positive representative of `delta_* mod54` with `delta_p+delta_*<=H` before allowing an arbitrary `+54t`. This is most promising first for small odd `k` beyond `5`.
4. **Optional global `k=5` track:** classify separated/cross `H=3,4`. Nested now has the stronger strict bound `H>=6`, but global analytic `k=5` still depends entirely on those two geometries.
5. Keep the odd terminal-tail split explicit but do not claim elimination without a genuine incompatibility.
6. Keep `J<=2^H` conjectural and keep Gate B frozen unless Gate A closes or a directly reusable radius-3 hypothesis appears.

A strong RL70 result would match the state and phase ladders through `p-2` or use the mod-54 selector to eliminate an infinite low-area congruence family. A meaningful partial result would analytically close separated/cross `H=3,4`, yielding global analytic Gate-A closure for terminal `k=5`.

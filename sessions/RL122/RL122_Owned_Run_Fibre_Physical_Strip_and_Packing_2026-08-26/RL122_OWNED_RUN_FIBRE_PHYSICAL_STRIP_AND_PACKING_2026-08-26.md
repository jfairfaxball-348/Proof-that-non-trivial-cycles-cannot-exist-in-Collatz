# RL122 — owned run-fibre physical strip and packing theorem

Date: 2026-08-26

## 0. Outcome and classification

RL122 executes Priority C of the RL121/RL122 global-bridge target after Priority A and Priority B supplied no established producer/consumer theorem in the inherited record.

RL122 proves a genuinely new **ordinary-owned physical-strip theorem**.  It uses actual legal runs in the ordinary shortcut cycle to put distinct physical cycle states into arithmetic fibres, and then combines those forced physical spacings with RL110's independent fixed-content numerator-diameter ceiling.

**No Gate A closure, Gate B closure, nontrivial-cycle exclusion, or Collatz proof is claimed.**

New promoted mathematics:

1. **RL122.1 — zero-run dyadic fibre lemma** (analytic).
2. **RL122.2 — odd-run triadic endpoint fibre lemma** (analytic).
3. **RL122.3 — owned run-fibre physical-strip theorem** (analytic).
4. **RL122.4 — full-ownership packing inequality** (analytic).
5. **RL122.5 — low odd-count corollary:** every hypothetical primitive nontrivial positive ordinary shortcut cycle must have `L >= 6` (analytic, using the inherited closed radius-three local engine).

The theorem is global in the primitive ordinary cycle word.  It uses no first-Farey, raw-`g=1`, or finite-cascade scope.

---

## 1. Incoming authority

Let a hypothetical primitive positive ordinary shortcut cycle have cyclic parity word

`w = d_0 ... d_(A-1)`,  `d_i in {0,1}`,

with:

- `L = sum d_i` odd shortcut steps;
- `Z = A-L` even shortcut steps;
- `D = 2^A - 3^L > 0`;
- physical cycle states `x_i` rooted at the `A` cyclic rotations.

For the ordinary unit-increment numerator `Q(r_i)`, inherited full ownership gives

`Q(r_i) = D x_i`.

The inherited RL109 interface supplies actual owned rotation states and the inherited RL110 theorem supplies the fixed-content diameter ceiling

`max_i Q(r_i) - min_i Q(r_i) <= B(A,L)`

where

`B(A,L) = (2^Z - 1)(3^L - 2^L)`.

The primitive/full-`D` radius-three engine remains a **closed local theorem only**: when its owned closest-pair radius hypothesis `R_* <= 3` is established, that local branch is excluded.

---

## 2. Run-fibre definitions

For `k >= 1`, define cyclic counts:

- `Z_k(w)` = number of cyclic positions whose next `k` symbols are all `0`;
- `O_k(w)` = number of cyclic positions whose next `k` symbols are all `1`.

Equivalently, `Z_k` counts starts of cyclic all-even runs of length at least `k`, while `O_k` counts starts of cyclic all-odd runs of length at least `k`.

Let the physical width of the cycle be

`W = max_i x_i - min_i x_i`.

Because the cycle is positive and nontrivial, its minimum state is odd: if a minimum state were even, the next shortcut step would divide it by two and produce a strictly smaller positive state.

---

## 3. RL122.1 — zero-run dyadic fibre lemma

Suppose cyclic position `i` begins with `k` zeros.  Then the next `k` shortcut steps are even, so

`x_(i+k) = x_i / 2^k`.

Since `x_(i+k)` is an integer physical state,

`2^k | x_i`.

Thus the `Z_k(w)` physical starting states belonging to these zero-run starts are distinct multiples of `2^k`.

Primitivity/simple-cycle ownership makes distinct cyclic positions correspond to distinct physical states.  Since the global minimum is odd, none of these zero-run starting states equals the minimum.  Therefore, whenever `Z_k(w) >= 1`,

`W >= (Z_k(w)-1) 2^k + 1`.                         (3.1)

Classification: **analytic**.

The `+1` is a real physical effect: it comes from the odd global minimum lying strictly below every even zero-run start.

---

## 4. RL122.2 — odd-run triadic endpoint fibre lemma

At an ordinary odd shortcut step,

`x' = (3x+1)/2`.

Hence

`x' + 1 = 3(x+1)/2`.

Iterating through `k` consecutive odd shortcut steps gives

`2^k (x_(i+k)+1) = 3^k (x_i+1)`.                  (4.1)

Because `gcd(2^k,3^k)=1`,

`3^k | (x_(i+k)+1)`,

so every endpoint of a cyclic `k`-odd run satisfies

`x_(i+k) == -1 (mod 3^k)`.

The `O_k(w)` endpoints are distinct physical states, again by primitivity/simple-cycle ownership.  Therefore

`W >= (O_k(w)-1) 3^k`.                             (4.2)

Classification: **analytic**.

---

## 5. RL122.3 — owned run-fibre physical strip

Define

`P_0(w) = max_{k: Z_k(w)>=1} ((Z_k(w)-1)2^k + 1)`

and

`P_1(w) = max_{k: O_k(w)>=1} ((O_k(w)-1)3^k)`,

with an empty maximum interpreted as `0`.  Put

`P(w) = max(P_0(w), P_1(w))`.

Combining (3.1) and (4.2):

### Theorem RL122.3

Every hypothetical primitive nontrivial positive ordinary shortcut cycle satisfies

`W >= P(w)`.                                            (5.1)

Classification: **analytic global ordinary-owned physical-strip theorem**.

This is not a reformulation of `S=D(x_v-x_u)`: `P(w)` is determined by legal ordinary-cycle run fibres and produces an independent lower bound on the physical width before any selected sparse difference is chosen.

At `k=1`,

`Z_1(w)=Z`,  `O_1(w)=L`,

so the universal coarse consequence is

`P(w) >= max(2Z-1, 3L-3)`.                            (5.2)

---

## 6. RL122.4 — full-ownership packing inequality

Full ownership gives

`Q(r_i)=D x_i`.

Therefore the exact numerator diameter over owned rotations is

`max_i Q(r_i)-min_i Q(r_i) = D W`.                    (6.1)

RL110 independently bounds every fixed-content numerator difference by

`B(A,L)=(2^Z-1)(3^L-2^L)`.                            (6.2)

Combining (5.1), (6.1), and (6.2):

### Theorem RL122.4

Every hypothetical primitive nontrivial positive ordinary shortcut cycle must satisfy

`D P(w) <= (2^Z-1)(3^L-2^L)`.                        (6.3)

Equivalently, any primitive ordinary parity word satisfying

`D P(w) > (2^Z-1)(3^L-2^L)`

is analytically excluded from being a nontrivial positive ordinary shortcut cycle.

Classification: **analytic global exclusion criterion**.

This is the missing kind of resource identified by RL110/RL121: a physical-width force coming from actual ownership plus legal ordinary runs, consumed by an independent numerator ceiling.

---

## 7. RL122.5 — low odd-count corollary

The inherited radius-one-step bound gives

`R_* <= min(L,Z)`.

Hence any nontrivial primitive word with `min(L,Z)<=3` lies in the already-closed radius-three local engine.

It remains to treat `L=4,5` with `Z>=4`.

### Case `L=4`

Here

`D = 16*2^Z - 81`,
`B = 65(2^Z-1)`,

and (5.2) gives `P>=9`.

For `Z>=4`,

`9D - B
 = 9(16*2^Z-81) - 65(2^Z-1)
 = 79*2^Z - 664
 > 0`.

Thus `DP>B`, contradicting RL122.4.

### Case `L=5`

Here

`D = 32*2^Z - 243`,
`B = 211(2^Z-1)`,

and (5.2) gives `P>=12`.

For `Z>=4`,

`12D - B
 = 12(32*2^Z-243) - 211(2^Z-1)
 = 173*2^Z - 2705
 > 0`.

Thus `DP>B`, again contradicting RL122.4.

Therefore:

### Corollary RL122.5

Every hypothetical primitive **nontrivial** positive ordinary shortcut cycle must have

`L >= 6`.                                                (7.1)

The known trivial cycle is not excluded by this statement; it is outside the nontrivial-cycle claim.

Classification: **analytic corollary**, using RL122.4 plus the inherited radius-three engine.

---

## 8. Mandatory red teams

### RL20 fake-model discriminator — PASS

The RL20 radius-four fake is not an owned ordinary cycle: its ordinary numerator fails `D|Q`.  RL122 only calls `x_i=Q(r_i)/D` a physical state after full ordinary ownership is established.  Therefore the fake does not satisfy the theorem's premise and is not spuriously excluded by local word geometry alone.

### RL79 generalized-increment discriminator — PASS

For generalized odd increment `s`,

`Q_s = s Q_1`.

The run identities become:

- zero runs still give starts divisible by `2^k`;
- odd runs give `2^k(x_(i+k)+s)=3^k(x_i+s)`, so endpoints satisfy `x_(i+k) == -s (mod 3^k)`.

These residue spacings survive, but the numerator diameter ceiling scales by `|s|` because all generalized word numerators scale by `s`.

Thus the ordinary packing inequality becomes, in the generalized system,

`D P_s <= |s| B`,

not the ordinary `DP<=B`.  The decisive ordinary `s=1` strength therefore does **not** survive generalized-increment scaling unchanged.  No factor `s` is cancelled.

### RL81 physical-versus-quotient discriminator — PASS

No quotient label is treated as physical.  The physical states are the actual states of the assumed ordinary cycle, equivalently `Q(r_i)/D` only after full ownership.

### Primitivity — PASS / load-bearing

Primitivity/simple-cycle ownership is used to ensure the run-fibre starts/endpoints are distinct physical states.  Without distinctness the spacing lower bounds would not follow.

### Raw/Farey scope — PASS

RL122.1–RL122.5 use the full cyclic parity word only.  They make no first-Farey, raw-`g=1`, full-phase, or multiplicity restriction.

### Finite-work scope — PASS

The promoted theorems are analytic.  The accompanying verifier is a finite sanity check only and is not used to enlarge the theorem scope.

---

## 9. Correction/demotion ledger

No inherited theorem is demoted.

One precision is frozen explicitly: RL122.5 excludes only **nontrivial** primitive positive ordinary shortcut cycles with `L<=5`; it must not be phrased as exclusion of every positive primitive cycle because the known trivial cycle exists.

No Gate status changes:

- Gate A: open globally;
- Gate B: open globally;
- nontrivial-cycle exclusion: open globally;
- Collatz: not proved.

---

## 10. What changed strategically

RL121's third return-policy interface is no longer absent in the same form.

Before RL122, the global owned sparse interface had exact divisibility but no independent physical/support size force.  RL122 supplies an independent physical-width lower bound `P(w)` and consumes it through the independent RL110 numerator ceiling.

The remaining problem is now sharper:

> Is the run-fibre packing resource strong enough, after exact combinatorial optimization and interaction between several fibres, to violate the RL122.4 inequality for every nontrivial primitive ordinary cycle word?

This is assigned to RL123.  Do not return to generic p-adic, cocycle, Fourier, transducer, inverse, S-unit, or bulk-cascade formulations unless a genuinely new input changes their frozen barriers.

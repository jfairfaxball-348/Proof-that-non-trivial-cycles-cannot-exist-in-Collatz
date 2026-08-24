# RL68 — nested descent and backward digit ladder

Date: 2026-08-24

## Status

RL68 continues from the checksum-clean authoritative RL67 state under the mandatory **verification economy rule**. At session start the current RL67 outer sidecar, freshly unpacked internal `SHA256SUMS.txt`, and `verification/run_fast_rl67_verifiers.sh` all passed. Historical expensive certificates were not recursively rerun.

RL68 resolves the principal **nested `g=0` interface-parity obstruction** left by RL67. It does **not** prove uniform odd-`k` Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The main new facts are:

1. the earlier x-ranks outstanding after `b_*` form an exact ordered y-silent descent stack;
2. this stack has an exact affine `T`-polynomial whose corrections are all multiples of `27`;
3. modulo `9`, the terminal side therefore recovers the parity of the y-gap `beta=b_*-b_p`, and hence recovers `delta_p mod 2` in the previously unresolved nested case;
4. the same selector lifts the last-active information from `delta_* mod 2` to `delta_* mod 6` once the local `beta` parity is fixed;
5. one further backward 3-adic digit recovers the nonzero residue of the `T`-state immediately before `b_p`;
6. every nested terminal path has the analytic lower bound `H>=5`.

Together with RL67, **every last/previous-active interface now has an exact previous-active parity selector**. The remaining Gate-A obstruction has moved one layer earlier: parity compatibility is no longer the missing nested datum, but there is still no uniform size/order mechanism forcing `H>=k` for all odd `k`.

---

## 1. Frozen notation and local `T` recurrences

Retain all RL67 notation. In particular:

- canonical start `(d,T,H)=(1,-14,0)` and `J=T+3^d-2^d`;
- terminal state `(d,J)=(1,2^k)`, with `k` odd by RL66;
- one-positions `a_1<...<a_r`, `b_1<...<b_r`;
- displacements `delta_j=a_j-b_j>=0`, `H=sum_j delta_j`;
- last active rank `j_*`, previous active rank `p<j_*`;
- terminal height-one state after `a_*:=a_(j_*)` is `R`;
- in the nested `g=0` case, `p=j_*-1` and
  `b_p<b_*<a_p<a_*`.

For a state of height `d`, put

`D_d=3^d-2^d`, so `J=T+D_d`.

The exact RL recurrence gives the two local formulas used throughout RL68:

- if `y=0`,
  `boxed: T'=(T+x 3^(d-1))/2`;                    (1.1)
- if `y=1`,
  `boxed: T'=(3T+x 3^d-1)/2`.                     (1.2)

No approximation is involved.

In the nested case define

`beta=b_*-b_p >=1`,

`lambda=a_p-b_* >=1`,

`mu=a_*-a_p >=1`.

Then exactly

`boxed: delta_p=beta+lambda`,                       (1.3)

`boxed: delta_*=lambda+mu`.                         (1.4)

RL67 already proved that the state immediately before `a_p` has height three; call its `J`-value `C`. It also proved

`boxed: C-10=2^(delta_*-lambda)(2R-5)`.             (1.5)

At height three, `D_3=19`, so the corresponding `T`-value is

`T_C=C-19`.

---

## 2. Ordered earlier-x stack after `b_*`

Let

`c_1<...<c_t`

be the x-one positions strictly between `b_*` and `a_p` belonging to ranks earlier than `p`:

`{c_1,...,c_t}={a_q:q<p, b_*<a_q<a_p}`.

Because x-one positions are rank-ordered, these are a contiguous terminal block of the earlier outstanding x-ranks.

### Lemma 2.1 — exact stack height

Immediately after column `b_*`, the height is exactly

`boxed: d=t+3`.                                     (2.1)

At the successive closures `c_i`, the pre-step heights are

`t+3, t+2, ..., 4`,

and after `c_t` the height is three until `a_p`.

### Proof

Immediately before `a_p`, RL67 gives height three: the baseline plus the still-open ranks `p` and `j_*`. Moving backward from `a_p` to just after `b_*`, every x-one `c_i` reopens one earlier outstanding rank and no y-one occurs. Hence there are exactly `t` extra outstanding ranks after `b_*`, giving `t+3`. Forward in time each `c_i` closes one of them in rank order. QED.

Classification: **analytic theorem**.

---

## 3. Exact nested y-silent descent polynomial

Let `S` be the `J`-state immediately after `b_*`. By Lemma 2.1 its height is `t+3`; write

`T_S=S-D_(t+3)`.

There are `lambda-1` columns strictly between `b_*` and `a_p`, all with `y=0`. At `c_i`, formula (1.1) contributes `3^(d-1)=3^(t+3-i)` in one-based indexing.

### Theorem 3.1 — ordered descent polynomial

With `c_i` one-based as above,

`boxed:`

`2^(lambda-1)(C-19)`

` = T_S + sum_(i=1)^t 2^(c_i-b_*-1) 3^(t+3-i)`.    (3.1)

Equivalently,

`boxed:`

`T_S = 2^(lambda-1)(C-19)`

`      - sum_(i=1)^t 2^(c_i-b_*-1) 3^(t+3-i)`.      (3.2)

### Proof

Across a `y=0` step, (1.1) is

`2T'=T+x3^(d-1)`.

Unrolling over the `lambda-1` steps from immediately after `b_*` to immediately before `a_p` gives

`2^(lambda-1) T_C = T_S + sum 2^(step offset) 3^(preheight-1)`.

The only nonzero x-terms occur at the ordered positions `c_i`; Lemma 2.1 gives preheight `t+4-i`, hence exponent `t+3-i`. Since `T_C=C-19`, (3.1) follows. QED.

Classification: **analytic theorem**.

### Corollary 3.2 — stack invisibility through modulus `27`

Every correction term in (3.1) contains at least `3^3`. Therefore

`boxed: 2^(lambda-1)(C-19) == T_S (mod 27)`.         (3.3)

This is the key nonseparable cancellation: the full ordered stack is retained exactly in (3.1), but the entire stack vanishes simultaneously modulo `27`.

---

## 4. The missing nested parity digit

Let `T_-` be the `T`-state immediately before `b_*`.

At `b_*`, `y=1`. If `x=0`, (1.2) gives

`2T_S=3T_- -1`.

If `x=1`, that x-one closes an earlier outstanding rank while rank `p` is still open, so the pre-step height is at least three. Hence its extra term `3^d` is divisible by `27`. In either case

`boxed: 2T_S+1 == 3T_- (mod 27)`.                   (4.1)

Between `b_p` and `b_*` there are `beta-1` columns with `y=0`. Any x-one there closes an earlier rank while `p` is open, so its pre-step height is at least three and its contribution in (1.1) is divisible by `9`. Immediately after `b_p`, every `y=1` step has

`T == 1 (mod 3)`.

Thus

`boxed: T_- == 2^(-(beta-1)) (mod 3)`.              (4.2)

Substituting (4.2) into (4.1) modulo `9` gives exactly two possibilities.

### Theorem 4.1 — nested mod-9 gap selector

`boxed: 2^(lambda-1)(C-19) == 1 (mod 9)` if `beta` is odd,

`boxed: 2^(lambda-1)(C-19) == 7 (mod 9)` if `beta` is even.     (4.3)

### Proof

By Corollary 3.2, modulo `9` the left side is `T_S`. If `beta` is odd, then `beta-1` is even and (4.2) gives `T_-==1 mod3`; (4.1) gives

`T_S==(3*1-1)/2==1 mod9`.

If `beta` is even, `T_-==2 mod3`, so

`T_S==(3*2-1)/2==7 mod9`.

QED.

Classification: **analytic theorem**.

### Corollary 4.2 — previous-active parity recovered in the nested case

Since `delta_p=beta+lambda`, define

`Theta = 2^(lambda-1)(C-19) mod9`.

Then `Theta` is never anything except `1` or `7`, and

- `Theta=1` means `beta` odd, hence `delta_p == lambda+1 (mod2)`;
- `Theta=7` means `beta` even, hence `delta_p == lambda (mod2)`.

Therefore

`boxed: the nested g=0 interface determines delta_p mod2 exactly`.       (4.4)

This closes the principal interface-parity obstruction explicitly identified at RL67 close-out.

---

## 5. Terminal-only form and a `delta_* mod 6` lift

Use the inherited nested transfer (1.5):

`C-19 = 2^(delta_*-lambda)(2R-5)-9`.

Multiply by `2^(lambda-1)`. Modulo `9` the `-9` term disappears.

### Theorem 5.1 — terminal nested gap selector

Put

`boxed: Theta_* = 2^(delta_*-1)(2R-5) (mod9)`.       (5.1)

Then

`boxed: Theta_*=1` iff `beta` is odd,

`boxed: Theta_*=7` iff `beta` is even.               (5.2)

Thus the parity of the y-gap before the last active rank is visible **from the terminal last-active data alone**.

Classification: **analytic theorem**.

RL66/RL67 already give

`R == 1+2^(delta_*) (mod3)`,

which determines only `delta_* mod2`. The mod-9 selector is stronger. Since `2` generates the unit group modulo `9`, `(R mod9, beta mod2)` determines `delta_* mod6` uniquely.

### Corollary 5.2 — exact mod-6 table

The only possible `R mod9` values are `0,2,3,5,6,8`. The unique `delta_* mod6` class is:

| `R mod9` | `beta` even | `beta` odd |
|---:|---:|---:|
| 0 | 3 | 5 |
| 2 | 2 | 4 |
| 3 | 5 | 1 |
| 5 | 0 | 2 |
| 6 | 1 | 3 |
| 8 | 4 | 0 |

Here `0` denotes divisibility by `6`.

Classification: **analytic corollary**.

This is a genuine lift from a parity selector to a six-class selector. It is still a congruence restriction, not a size bound on `delta_*`.

---

## 6. One further backward 3-adic digit

The same exact descent gives one more state digit beyond the newly recovered `beta` parity.

Define

`boxed: Z = (2^lambda(C-19)+1)/3`.                   (6.1)

This is an integer. Indeed, twice (3.1), followed by the exact `b_*` update, writes its numerator as a sum of terms each divisible by `3`.

### Theorem 6.1 — pre-`b_*` digit recovery

`boxed: Z == T_- (mod9)`.                            (6.2)

### Proof

By (3.3),

`2^(lambda-1)(C-19) == T_S (mod27)`.

Twice this congruence and add one. By (4.1),

`2^lambda(C-19)+1 == 3T_- (mod27)`.

Divide by `3`, obtaining (6.2) modulo `9`. QED.

Now let `T_p^+` and `T_p^-` be the states immediately after and immediately before `b_p`. As above, all x-corrections between `b_p` and `b_*` are multiples of `9`, so

`boxed: Q := 2^(beta-1) Z == T_p^+ (mod9)`.          (6.3)

At `b_p`, any simultaneous earlier x-closure contributes a multiple of `9`; therefore

`T_p^+ == (3T_p^- -1)/2 (mod9)`.                    (6.4)

The canonical start has `T=-14==1 mod3`; every `y=1` reset gives `T==1 mod3`, and every legal `y=0` step multiplies a nonzero mod-3 residue by `2^(-1)`. Hence `T_p^- mod3` is always `1` or `2`, never `0`.

### Corollary 6.2 — second nested backward digit

`boxed: Q in {1,7}`, with

- `Q=1` iff `T_p^-==1 (mod3)`;
- `Q=7` iff `T_p^-==2 (mod3)`.

So the terminal/nested interface now reaches one state **before** the previous active y-one.

If `b_p` has a preceding y-one `b_(p-1)` and `gamma=b_p-b_(p-1)`, then the same mod-3 propagation gives

- `Q=1` iff `gamma` is odd;
- `Q=7` iff `gamma` is even.

Classification: **analytic theorem/corollary**.

Using (1.5), `Z` can also be written without `C` as

`boxed: Z = (2^(delta_*)(2R-5)-9*2^lambda+1)/3`.     (6.5)

This is the first exact nested backward digit beyond `delta_p` parity and is the natural launch point for RL69.

---

## 7. Analytic nested lower bound `H>=5`

The nested geometry alone gives

`delta_p+delta_* = beta+2lambda+mu >=4`.

So `H>=4`.

### Theorem 7.1 — every nested terminal path has `H>=5`

Assume `H=4`. Then there can be no other active rank, and equality in the preceding lower bound forces

`beta=lambda=mu=1`,

so

`delta_p=delta_*=2`.

Thus `p` is the first active rank. Before `b_p` the canonical path is synchronized, so the first-mismatch entry is one of the RL67 values

`P_0 in {-6,-28,-4}`.

The entire two-active nested block is then exactly

`01,01,10,10`.

Direct composition gives its height-one exit

`boxed: R=(9P_0+62)/16`.                             (7.1)

But every allowed `P_0<=-4`, so

`R <= 26/16 < 2`,

contradicting the inherited terminal-suffix entry theorem `R>=3`.

Therefore `H=4` is impossible and

`boxed: H>=5` in every nested terminal path.         (7.2)

Classification: **analytic theorem**.

This analytically makes the nested interface Gate-A safe at `k=5`. It does **not** analytically close `k=5` globally because separated and cross interfaces remain separate cases; the inherited `H<=24` finite certificate remains only a finite certificate.

---

## 8. Complete previous-active parity recovery across all interfaces

RL67 already established:

1. if `g>=1`, the synchronized bridge digit recovers `delta_p mod2`;
2. if `g=0` and separated, the all-`00` bridge plus `A mod3` recovers `delta_p mod2`;
3. if `g=0` and cross, `C mod3` recovers `delta_p mod2`.

RL68 Theorem 4.1/Corollary 4.2 adds the only missing case:

4. if `g=0` and nested, the mod-9 selector recovers `delta_p mod2`.

### Corollary 8.1

`boxed: every canonical terminal path has an exact state/interface selector for the parity of its previous active displacement.`

Classification: **analytic corollary**, combining inherited RL67 theorems with RL68.

This removes the specific “nested case still hides `delta_p`” obstruction from the RL67 ledger. It does not by itself turn the phase digit into a contradiction because both the state side and the full-phase side can remain mutually compatible.

---

## 9. Independent exact audit evidence

`verification/verify_rl68_nested_descent.py` independently recomputes canonical RL states directly from the exact recurrence through `MAX_M=18` and audits every bounded nested terminal interface.

Fresh results:

- bounded canonical terminal paths: `2,596`;
- nested `g=0` terminal interfaces: `1,222`;
- exact ordered nested-descent polynomial checks: `1,222`;
- nested mod-9 terminal gap-selector checks: `1,222`;
- nested previous-active parity recoveries: `1,222`;
- nested `delta_* mod6` lifts: `1,222`;
- nested second backward-digit checks: `1,222`;
- nested `H>=5` checks: `1,222`;
- maximum earlier-x stack depth seen: `3`;
- bounded stack-depth histogram: `{0: 912, 1: 256, 2: 51, 3: 3}`;
- status: `RL68 nested-descent verifier: PASS`.

The verifier is a falsification/audit tool. The infinite statements above are classified as analytic only because their proofs do not depend on the bounded scan.

---

## 10. Rejected or insufficient routes

### F1. Drop the earlier x-stack and pretend the nested descent is all-`00`

Rejected. The exact stack is generally nonempty. RL68 retains every ordered closure in (3.1). Only after the exact formula is established may the terms be discarded modulo `27` because their divisibility is proved.

### F2. Treat the mod-9 selector as Gate-A closure

Rejected. It recovers parity and a `delta_* mod6` class, but supplies no uniform upper/lower size comparison between `H`, `k`, and the full-phase quotient.

### F3. Promote the second backward digit to full earlier-prefix reconstruction without keeping correction terms

Rejected. Beyond the protected moduli, lower-height x-closures contribute nontrivially. Any further lift must either subtract the ordered descent polynomial exactly or prove a new height/divisibility mechanism.

### F4. Revive the conjectural `J<=2^H` height-one bound

Not done. RL67's status remains unchanged: bounded evidence only, and naive magnitude-only macro induction remains disproved.

---

## 11. Exact proof state after RL68

Retain all RL62–RL67 classifications and corrections. New analytic upgrades are limited to the statements proved in this note.

Gate A remains open globally for unbounded odd terminal exponents. The new situation is sharper:

- even terminal `k` remains analytically eliminated (RL66);
- terminal `k=3` remains analytically Gate-A safe (RL67);
- every canonical terminal path has at least two active ranks and `H>=3` (RL67);
- nested `g=0` terminal paths now satisfy `H>=5` (RL68);
- the previous-active displacement parity is now recoverable in **all** last/previous-active interface geometries;
- the nested terminal data additionally select `delta_* mod6` and expose one further backward `T`-digit;
- the inherited exact `H<=24` certificate remains finite-only;
- Gate B remains frozen/open/audit-dependent.

The principal obstruction has therefore moved from “recover `delta_p` in the nested interface” to:

**turn the complete backward digit information into a nonseparable size/order restriction, or continue the exact backward ladder far enough to expose an earlier active-rank obstruction that cannot be phase-compatible.**

---

## 12. Recommended RL69 attack

1. **Exploit the second backward nested digit.** Start from
   `Z=(2^lambda(C-19)+1)/3` and
   `Q=2^(beta-1)Z mod9`.
   Expose the rank immediately before `p`, retaining any zero-displacement gap exactly. Seek a state-side digit matching the next nonzero term of the full-phase rank-tail ladder.
2. **Lift with exact subtraction, not blind modulus.** Equation (3.1) gives every nested x-stack correction explicitly. Subtract the known low-height closure terms before increasing the 3-adic modulus; do not assume they vanish at higher powers.
3. **Use the `delta_* mod6` table against the terminal-tail split.** Revisit the inherited odd-`k` tail classes (all-`00`, mixed, nonmaximal all-`11`, maximal all-`11`) and test whether their exact `R mod9` formulas plus local gap parity eliminate any infinite congruence class.
4. **Small-`k` analytic track.** RL68 makes nested `k=5` safe. If economical, classify cross/separated hypothetical `H=3,4` terminal paths to see whether `k=5` can be upgraded from finite certificate to a global analytic theorem.
5. Keep the canonical height-one inequality `J<=2^H` conjectural unless a genuinely history-sensitive invariant is proved.
6. Keep Gate B frozen unless Gate A closes or a directly reusable radius-3 hypothesis appears.

A strong RL69 result would either eliminate an infinite odd-`k` terminal-tail congruence class using the new mod-6 selector, or extend the nested backward ladder through the rank before `p` in a form that matches the next full-phase digit. A meaningful partial result would analytically close `k=5` across cross and separated interfaces as well.

# RL70 — fourth backward parity, q=4 phase match, and the mod-54 residue floor

Date: 2026-08-24

## Status

RL70 continues from the checksum-clean authoritative RL69 state under the mandatory **verification economy rule**.  At session start the RL69 outer sidecar, freshly unpacked internal `SHA256SUMS.txt`, `verification/run_fast_rl69_verifiers.sh`, and root/inside-ledger byte identity all passed.  GitHub `authoritative/` contained the expected RL69 ZIP, sidecar, session ledger, fresh-unpack record, and mathematics note with the same file sizes as the supplied authoritative files.  No recursive historical audit was performed.

RL70 does **not** prove uniform odd-`k` Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The principal new advances are:

1. the RL69 state `V=T_p^- (mod 9)` can be pushed one y-rank earlier across `b_q`, `q=p-1`, by retaining exactly one possible height-two closure term;
2. this gives the state immediately before `b_q` modulo `3`;
3. when `r=p-2` exists, that trit recovers `delta_r mod2` exactly;
4. the state-side bit matches the next (`q=4`) full-phase rank-tail digit modulo `3^(s+5)`;
5. the RL69 mod-54 selector has a genuine low-area consequence: its least positive representative is a lower bound for `delta_*`, and in any hypothetical nested violation with odd `k<=57` it is the **exact** value of `delta_*`.

The new ladder match is again compatibility, not contradiction.  A further backward rank now requires one more 3-adic digit of the state before `b_q`; the present step consumes the available precision from mod `9` to mod `3`.

---

## 1. Frozen notation

Retain all RL69 notation and classifications.

In a nested `g=0` last-two-active interface,

`b_p < b_* < a_p < a_*`,

with last active rank `j_*` and previous active rank `p=j_*-1`.  Put

`beta=b_*-b_p`, `lambda=a_p-b_*`, `mu=a_*-a_p`,

so

`delta_p=beta+lambda`, `delta_*=lambda+mu`.

RL69 recovers the state immediately before `b_p` modulo `9`:

`boxed: V == T_p^- (mod9)`.

Let

`q=p-1`

when this rank exists, and write

`b_q=b_(p-1)`, `a_q=a_(p-1)`, `delta_q=a_q-b_q`,

`gamma=b_p-b_q`.

Let `T_q^-` and `T_q^+` denote the `T`-states immediately before and after the y-one at `b_q`.

The exact RL recurrence used below is

- for `y=0`,

  `2T' = T + x 3^(d-1)`;

- for `y=1`,

  `2T' = 3T + x 3^d -1`.

No separable rank relaxation is used.

---

## 2. Exact interval polynomial from `b_q` to `b_p`

There is no y-one strictly between the consecutive y-ranks `b_q` and `b_p`.  Iterating the exact `y=0` recurrence from immediately after `b_q` to immediately before `b_p` gives

`2^(gamma-1) T_p^-`

` = T_q^+ + sum_c 2^(c-b_q-1) 3^(d(c)-1)`,            (2.1)

where the sum is over x-one positions

`b_q < c < b_p`,

and `d(c)` is the exact pre-step height at that closure.

### Lemma 2.1 — unique visible height-two closure

Modulo `9`, every term in (2.1) vanishes except possibly the closure of rank `q` itself.

More precisely:

- if `0<delta_q<gamma`, then `a_q` lies strictly between `b_q` and `b_p`; because `a_q` is the latest x-position among ranks `<=q`, every earlier rank has already closed when `q` closes, so the pre-step height at `a_q` is exactly `2`;
- every earlier closure in the interval has pre-step height at least `3`, hence contributes a multiple of `9`;
- if `delta_q>=gamma`, rank `q` has not closed strictly before `b_p`, and every closure in the interval is an earlier rank while `q` is still open, so again its pre-step height is at least `3`.

Define

`tau_q = 2^(delta_q-1) (mod3)` if `0<delta_q<gamma`,

`tau_q = 0` otherwise.

Then

`boxed: T_q^+ == 2^(gamma-1)V - 3 tau_q (mod9)`.       (2.2)

Classification: **analytic theorem/corollary of the exact ordered recurrence and RL69 `V` digit**.

The important point is structural: no whole-prefix replay is needed.  Exactly one low-height closure is visible, and it is determined by the placement of rank `q`.

---

## 3. Crossing the y-one `b_q`

At the y-one `b_q`,

`2T_q^+ = 3T_q^- + x 3^d -1`.

A simultaneous x-one can contribute modulo `9` only in one case.

### Lemma 3.1 — unique visible simultaneous correction

Define

`sigma_q=1` if `delta_q=0`, and `sigma_q=0` otherwise.

Then

`boxed: 3T_q^- == 2T_q^+ +1 -3 sigma_q (mod9)`.      (3.1)

#### Proof

If `delta_q=0`, then `a_q=b_q`.  Since `a_q` is the largest x-position among ranks `<=q`, every earlier rank has already closed before this column.  Thus the pre-step height is `1`, and the simultaneous `x=1` term is exactly `3` modulo `9`.

If `delta_q>0`, rank `q` does not close at its own y-one.  Any earlier rank closing simultaneously at `b_q` must still be outstanding before the column, so the pre-step height is at least `2`; its contribution `3^d` is divisible by `9`.  QED.

Combine (2.2) and (3.1).  Put

`U_q = 2^(gamma-1)V -3 tau_q (mod9)`.

The right side of

`3S == 2U_q+1-3sigma_q (mod9)`                         (3.2)

is divisible by `3`, and there is a unique `S mod3` satisfying it.

### Theorem 3.2 — fourth backward state trit

`boxed: S == T_q^- (mod3)`.                            (3.3)

Classification: **analytic theorem**.

This is the requested push of the RL69 `V mod9` digit across the y-one `b_(p-1)`.

---

## 4. The rank `p-2` parity selector

Assume now that

`r=p-2`

exists.  Put

`theta=b_q-b_r`.

Immediately after any y-one, the exact recurrence gives

`T == 1 (mod3)`,

because

`2T' = 3T + x3^d -1 == -1 (mod3)`.

Between `b_r` and `b_q`, every step has `y=0`.  Whenever `x=1` in such a step, legality forces pre-height `d>=2`, so its x-correction is divisible by `3`.  Therefore

`T_q^- == 2^(-(theta-1)) (mod3)`.

Hence

- `S=1` iff `theta` is odd;
- `S=2` iff `theta` is even.

Since

`delta_r=a_r-b_r=(a_r-b_q)+(b_q-b_r)`,                 (4.1)

we obtain:

### Theorem 4.1 — exact `delta_(p-2)` parity selector

Let `eta_S=1` for `S=1` and `eta_S=0` for `S=2`.  Then

`boxed: delta_r == (a_r-b_q)+eta_S (mod2)`.            (4.2)

Equivalently,

`chi_r := delta_r mod2`

is determined exactly by the fourth backward state trit `S` and the local offset `a_r-b_q mod2`.

Classification: **analytic corollary**.

The zero-displacement case is included correctly: an even selector value includes `delta_r=0` without promoting it to a positive displacement.

---

## 5. Exact match with the `q=4` full-phase rank-tail digit

Let

`E_j=2^(b_j)(2^(delta_j)-1)`.

Define the four-rank tail

`C_4=E_*+3E_p+9E_q+27E_r`,

and the three-rank base

`C_3=E_*+3E_p+9E_q`.

Under the frozen full-phase extendability hypothesis, the RL66/RL67 rank-tail ladder gives

`N == 2-2^(1-k)-4*3^(s+1)2^(-a) C_4`

`     (mod 3^(s+5))`.                                  (5.1)

Let

`R_3 = 2-2^(1-k)-4*3^(s+1)2^(-a) C_3`.

Modulo `3`,

`E_r==0` if `delta_r` is even,

`E_r==2^(b_r)` if `delta_r` is odd.

Therefore:

### Theorem 5.1 — state/phase match through rank `p-2`

Under full-phase extendability,

`boxed: N == R_3 - chi_r 4*2^(b_r-a)3^(s+4)`

`       (mod 3^(s+5))`,                                (5.2)

where `chi_r` is exactly the state-side selector from Theorem 4.1.

Thus the next full-phase digit is zero precisely when the backward state ladder says `delta_(p-2)` is even, and is the unique nonzero rank-tail correction precisely when the state ladder says it is odd.

Classification: **analytic theorem conditional on the frozen full-phase hypothesis**.

This is a strong ladder extension, but it is still a compatibility statement.  No contradiction with full-phase extendability follows merely from the fact that the two constructions agree.

---

## 6. The mod-54 selector becomes a genuine low-area floor

RL69 proves that the nested terminal data select a unique congruence class

`delta_* (mod54)`.

Let

`c_54 in {1,2,...,54}`

be the least positive representative of that selected class, with residue `0 mod54` represented by `54`.  Because `delta_*>0`, there is an integer `t>=0` such that

`delta_*=c_54+54t`.                                    (6.1)

Since `p` and `j_*` are active and

`H=sum_j delta_j`,                                    (6.2)

we immediately have:

### Theorem 6.1 — residue-floor area bound

`boxed: H >= delta_p + c_54 = beta+lambda+c_54`.       (6.3)

Consequently, a hypothetical nested Gate-A violation `H<k` must satisfy

`boxed: beta+lambda+c_54 <= k-1`.                      (6.4)

This is the first direct size/order use of the RL69 mod-54 selector: although a congruence class does not upper-bound `delta_*`, its least positive representative is a rigorous **lower** bound, which is the useful direction for Gate A.

### Corollary 6.2 — exact low-`k` displacement

In nested geometry `delta_p=beta+lambda>=2`.  If `t>=1` in (6.1), then

`delta_p+delta_* >= 2+55=57`.

Therefore, in any hypothetical nested violation with odd

`boxed: k<=57`,

one must have

`boxed: t=0, hence delta_*=c_54 exactly`.               (6.5)

Thus for low-area odd exponents through `57`, the mod-54 selector is not merely a residue selector inside a violating configuration; it fixes the full last-active displacement.

Classification: **analytic theorem/corollary**.

This does not close those exponents globally.  One still needs to show that the selected `c_54` and the earlier-rank area cannot satisfy (6.4) in every remaining interface/tail class.

---

## 7. Precision-budget barrier after the new step

The new backward step also identifies exactly why the same argument cannot simply be iterated indefinitely at the current precision.

RL69 supplies `V=T_p^- mod9`.  Equation (3.1) contains a factor `3T_q^-`; dividing a congruence modulo `9` by `3` leaves only

`T_q^- mod3`.

That is sufficient to recover the parity of the preceding y-gap and hence `delta_(p-2) mod2`, but it is **not** sufficient to push another y-one backward in the same compact manner.  To cross `b_r` and recover the state before it modulo `3`, one needs the state immediately after `b_r` modulo `9`, which in turn requires

`T_q^- mod9`.

Therefore the next compact ladder extension requires one of:

1. lift the RL70 pre-`b_q` state from mod `3` to mod `9` by carrying one additional 3-adic digit from the terminal side; or
2. derive an alternative invariant that avoids the one-digit loss at a backward y-one.

At the natural direct lift, the next pre-height corrections (one level above those retained by RL69/RL70) will become visible and must be subtracted exactly before division.

Classification: **analytic method limitation / next-obstruction lemma**.

---

## 8. Exact bounded audit

`verification/verify_rl70_fourth_backward_parity.py` independently recomputes canonical RL states directly from the exact recurrence through `MAX_M=18`.

Fresh results:

- bounded canonical terminal paths: `2,596`;
- nested `g=0` terminal interfaces: `1,222`;
- nested interfaces with `q=p-1` present: `1,222`;
- `q` zero-displacement cases: `47`;
- `q` closures strictly between `b_q` and `b_p`: `239`;
- `q` closures exactly at `b_p`: `287`;
- `q` closures after `b_p`: `649`;
- pre-`b_q` mod-3 recoveries: `1,222`;
- `delta_(p-2)` parity-selector checks: `1,212`;
- full-phase `q=4` digit matches: `1,103`;
- status: `RL70 fourth-backward-parity verifier: PASS`.

The four placement counts sum to all `1,222` nested interfaces, so the verifier audits every correction geometry appearing in the bounded sample, including zero displacement and closure on either side of `b_p`.

The bounded verifier is a falsification/audit tool.  It is not the infinite proof of Sections 2–7.

---

## 9. Routes tested but not upgraded

### F1. Treat the q=4 phase match as a contradiction

Rejected.  The state and phase ladders agree exactly through rank `p-2`; agreement is compatibility, not impossibility.

### F2. Ignore the q closure between `b_q` and `b_p`

Rejected.  When `0<delta_q<gamma`, rank `q` closes at exact pre-height two and contributes `3*2^(delta_q-1)` modulo `9`.  Omitting it gives the wrong backward trit.  All deeper closures vanish only after the height argument in Lemma 2.1.

### F3. Ignore simultaneous closure at `b_q`

Rejected.  The zero-displacement case `delta_q=0` contributes the visible `3` term in (3.1).  Earlier simultaneous closures are invisible only because their pre-height is at least two.

### F4. Treat `c_54` as an upper bound

Rejected.  `delta_*=c_54+54t` has no uniform upper bound.  The valid consequence is the lower bound `delta_*>=c_54`, and the exact-value upgrade only inside a sufficiently low-area hypothetical violation.

### F5. Claim a terminal-tail class is eliminated by the residue floor

Not proved.  Equation (6.4) is a genuine sieve, but RL70 did not prove that every all-`00`, mixed, nonmaximal all-`11`, or allowed maximal all-`11` tail violates it.

### F6. Push to rank `p-3` without lifting precision

Rejected.  The backward y-one division consumes one 3-adic digit.  The current compact state is only mod `3` before `b_q`; another direct crossing requires a mod-`9` lift first.

---

## 10. Exact proof state after RL70

Retain every RL62–RL69 correction, theorem, finite certificate, and demotion.

New RL70 analytic upgrades are limited to:

1. an exact y-silent interval polynomial from `b_q` to `b_p` whose only mod-`9` visible interior correction is the height-two closure of rank `q`;
2. an exact correction at `b_q` for the zero-displacement simultaneous closure;
3. recovery of `T` immediately before `b_q` modulo `3` from RL69 `V mod9`;
4. exact parity recovery of `delta_(p-2)` when that rank exists;
5. exact match with the `q=4` full-phase rank-tail digit modulo `3^(s+5)`;
6. the residue-floor bound `H>=delta_p+c_54`, and exact identification `delta_*=c_54` inside any hypothetical nested violation with odd `k<=57`;
7. identification of the one-digit precision loss that now blocks another compact backward step.

Gate A remains open globally for unbounded odd `k`.  Gate B remains frozen/open/audit-dependent.  No result here upgrades `J<=2^H` from conjectural bounded evidence.

The live nested obstruction has moved one rank earlier again: state/phase compatibility now reaches `p-2`, while the next direct step requires a terminal-side precision lift sufficient to recover `T_q^- mod9` rather than only mod3.

---

## 11. Recommended RL71 attack

1. **Lift the pre-`b_q` state from mod3 to mod9.**  Start from the RL69 terminal expression for `Z` and carry the descent one power of `3` higher.  At that precision, retain the next visible pre-height correction terms explicitly; do not assume the ordered stack is invisible.
2. **Push across `b_r`, `r=p-2`.**  Once `T_q^- mod9` is available, repeat the RL70 height-two correction analysis to recover the state immediately before `b_r` modulo3 and seek `delta_(p-3) mod2`.
3. **Match the `q=5` phase digit.**  The next rank-tail term is `81E_(p-3)` and should appear modulo `3^(s+6)`.
4. **Exploit the residue-floor sieve before lifting representatives.**  For any candidate family, compute the RL69 least residue `c_54` first.  If `beta+lambda+c_54>=k`, Gate A is immediate for that family.  For odd `k<=57` under a hypothetical violation, set `delta_*=c_54` exactly before any further case split.
5. **Keep the four inherited odd terminal-tail classes explicit.**  Test (6.4) against their exact `R mod81`/suffix formulas, but do not claim a class eliminated unless the incompatibility is uniform.
6. Keep Gate B frozen and keep `J<=2^H` conjectural unless a separate proof is supplied.

A strong RL71 result would lift `T_q^-` to mod9 and match the state/phase ladders through rank `p-3`, or use the residue-floor inequality to eliminate an infinite terminal-tail congruence family.  A meaningful partial result would prove a uniform lower bound on `c_54` for one of the inherited tail classes.

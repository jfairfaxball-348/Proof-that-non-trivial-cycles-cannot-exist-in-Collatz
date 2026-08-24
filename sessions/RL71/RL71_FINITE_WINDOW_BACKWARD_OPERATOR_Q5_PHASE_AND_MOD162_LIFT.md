# RL71 — finite-window backward operator, q=5 phase match, and mod-162 lift

Date: 2026-08-24

## Status

RL71 continues from the checksum-clean authoritative RL70 state under the mandatory **verification economy rule**.

The current RL70 outer SHA-256 sidecar, freshly unpacked internal `SHA256SUMS.txt`, `verification/run_fast_rl70_verifiers.sh`, and root/inside-ledger byte identity all passed before new mathematics was attempted. GitHub `authoritative/` was also checked and contained the expected RL70 authoritative artifacts. Historical expensive certificates were not recursively rerun.

RL71 does **not** prove uniform odd-`k` Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The principal new advances are:

1. an **exact consecutive-y backward polynomial** valid at every rank, not just the last few nested ranks;
2. a **finite-window visibility theorem**: modulo `3^M`, only the latest `M-1` ranks can affect one consecutive-y backward crossing;
3. an exact nested terminal polynomial showing that, at modulus `3^M`, only the latest `M-2` earlier ranks can affect recovery of the previous-active state;
4. at `M=4`, the two newly visible ranks give `T_p^- mod27` and then `T_(p-1)^- mod9` exactly;
5. one further RL70-style crossing gives the state before `b_(p-2)` modulo `3`, selecting `delta_(p-3) mod2` when that rank exists;
6. that bit matches the next (`q=5`) full-phase rank-tail digit modulo `3^(s+6)`;
7. the nested terminal selector lifts from `delta_* mod54` to a unique class modulo `162`;
8. the least positive mod-162 representative gives the stronger floor `H>=delta_p+c_162`, and inside any hypothetical nested violation with odd `k<=165`, `delta_*=c_162` exactly;
9. the repeated state/phase matches are now seen to be structurally extendable finite-window compatibility. Merely pushing q=6, q=7, ... is therefore not by itself a promising contradiction mechanism; the next programme should combine the exact ladder with a genuinely coupled size/order or ownership invariant.

---

## 1. Frozen notation

Retain all RL62–RL70 notation, theorem classifications, corrections, and demotions.

In a nested `g=0` last-two-active interface,

`b_p < b_* < a_p < a_*`,

with last active rank `j_*` and previous active rank `p=j_*-1`, put

`beta=b_*-b_p`, `lambda=a_p-b_*`, `mu=a_*-a_p`,

so

`delta_p=beta+lambda`, `delta_*=lambda+mu`.

Let

`q=p-1`, `r=p-2`, `h=p-3`

when the corresponding ranks exist.

For any rank `j`, let `a_j` and `b_j` be its x-one and y-one positions and

`delta_j=a_j-b_j`.

The exact `T` recurrence remains

- for `y=0`,

  `2T' = T + x 3^(d-1)`;

- for `y=1`,

  `2T' = 3T + x 3^d -1`,

where `d` is the exact pre-step height.

Let `T_j^-` and `T_j^+` denote the states immediately before and after the y-one at `b_j`.

As in RL68–RL70, let `C` be the height-three state immediately before `a_p`, write `T_C=C-19`, let `T_*^-` be the state immediately before `b_*`, and define

`boxed: Z=(2^lambda T_C+1)/3`.

Let `R` be the height-one `J` state immediately after `a_*`.

No separable rank relaxation is used anywhere below.

---

## 2. Exact consecutive-y backward polynomial

The RL70 one-rank step is a special case of an exact rank-by-rank identity.

Fix any consecutive y-ranks `j` and `j+1`, and put

`g_j=b_(j+1)-b_j`.

There is no y-one strictly between these two columns.

### Lemma 2.1 — exact pre-height of an interior x-closure

Suppose rank `i<=j` closes at

`b_j<a_i<b_(j+1)`.

Then at `a_i` the exact pre-step height is

`boxed: d=j-i+2`.

#### Proof

By x-rank order,

`a_i<a_(i+1)<...<a_j`.

Since `a_i>b_j`, all ranks `i,i+1,...,j` have already had their y-ones and none has yet had its x-one. Every earlier rank `<i` has x-position `<a_i` and is already closed. Thus the baseline plus exactly `j-i+1` open ranks are present, giving `d=1+(j-i+1)=j-i+2`. QED.

### Theorem 2.2 — exact consecutive-y interval polynomial

`boxed:`

`2^(g_j-1) T_(j+1)^-`

` = T_j^+`

`   + sum_(i<=j, b_j<a_i<b_(j+1))`

`       2^(a_i-b_j-1) 3^(j-i+1)`.                    (2.1)

At the y-one `b_j`,

`boxed:`

`2T_j^+ +1`

` = 3T_j^-`

`   + sum_(i<=j, a_i=b_j) 3^(j-i+1)`.                (2.2)

The second sum has at most one term because x-one positions are strictly increasing.

#### Proof

Across every y-zero step,

`2T'=T+x3^(d-1)`.

Unroll from immediately after `b_j` to immediately before `b_(j+1)`. Lemma 2.1 gives the exponent `d-1=j-i+1`, yielding (2.1).

At `b_j`, if an earlier rank `i` closes simultaneously, then before the y-one of rank `j` the open earlier ranks are exactly `i,...,j-1`, so the pre-step height is `j-i+1`. Substitution into the y-one recurrence gives (2.2). QED.

Classification: **analytic theorem**.

### Corollary 2.3 — finite-window visibility

Fix `M>=2`. Modulo `3^M`, every correction in (2.1)–(2.2) from

`i<=j-M+1`

vanishes. Therefore only the latest

`j, j-1, ..., j-M+2`

can affect a backward crossing at precision `3^M`.

Consequently, if `T_(j+1)^- mod3^M` is known, then the local positions of only those latest `M-1` ranks determine

`T_j^+ mod3^M`

and, after (2.2) and division by `3`, determine

`boxed: T_j^- mod3^(M-1)`.

Classification: **analytic corollary / finite-window backward operator**.

This is the exact structural reason one backward y-one consumes one 3-adic digit.

---

## 3. Exact nested terminal finite-window polynomial

The terminal-side RL68/RL69 descent also admits an exact all-rank form.

Retain `q=p-1`.

### Theorem 3.1 — exact nested terminal polynomial

The exact integer `Z` satisfies

`boxed:`

`Z = T_*^-`

`    + sum_(i<=q, a_i>=b_*)`

`        2^(a_i-b_*) 3^(q-i+2)`.                     (3.1)

Between `b_p` and `b_*`,

`boxed:`

`2^(beta-1)T_*^- = T_p^+`

` + sum_(i<=q, b_p<a_i<b_*)`

`     2^(a_i-b_p-1) 3^(q-i+2)`.                      (3.2)

At `b_p`,

`boxed:`

`2T_p^+ +1 = 3T_p^-`

` + sum_(i<=q, a_i=b_p) 3^(q-i+2)`.                  (3.3)

#### Proof

RL68's exact ordered stack after `b_*` has closure heights descending to four. For rank `i<=q` with `a_i>b_*`, the pre-height at its post-`b_*` closure is `q-i+4`. Combining the exact y-silent descent with the `b_*` y-one and dividing by the defining factor `3` in `Z` reduces the 3-exponent by one, giving `3^(q-i+2)` and the power-of-two transport `2^(a_i-b_*)`. If `a_i=b_*`, the simultaneous y-one term gives the same exponent with power-of-two factor `1`, so (3.1) is uniform.

Between `b_p` and `b_*`, rank `p` is open and `j_*` has not yet opened. If rank `i<=q` closes there, the exact pre-height is `q-i+3`, giving the y-zero correction exponent `q-i+2` in (3.2).

At `b_p`, if rank `i<=q` closes simultaneously, the pre-step height is `q-i+2`, which gives (3.3). QED.

Classification: **analytic theorem**.

### Corollary 3.2 — terminal finite-window visibility

Fix `M>=3`. Modulo `3^M`, every rank in (3.1)–(3.3) with

`i<=q-M+2`

vanishes. Thus only the latest `M-2` earlier ranks

`q, q-1, ..., q-M+3`

can affect recovery of `T_p^-` at terminal precision `3^M`.

Hence `Z mod3^M` plus those `M-2` local x-positions determines

`boxed: T_p^- mod3^(M-1)`.

Classification: **analytic corollary**.

RL69 is the case `M=3` (only rank `q` visible). RL71 uses `M=4` (exactly ranks `q` and `r` visible).

---

## 4. The mod-27 lift of `T_p^-`

Take `M=4`, so the working terminal modulus is `81`.

Let `r=p-2` when it exists. If it does not exist, all `r` corrections below are zero.

Define the post/at-`b_*` correction residues

`A_q = 2^(a_q-b_*) mod9` if `a_q>=b_*`, else `0`,

`A_r = 2^(a_r-b_*) mod3` if `a_r>=b_*`, else `0`.

Define the corrections strictly between `b_p` and `b_*`:

`K_q = 2^(a_q-b_p-1) mod9` if `b_p<a_q<b_*`, else `0`,

`K_r = 2^(a_r-b_p-1) mod3` if `b_p<a_r<b_*`, else `0`.

Define simultaneous indicators

`X_q=1` iff `a_q=b_p`, else `0`,

`X_r=1` iff `a_r=b_p`, else `0`.

By Corollary 3.2, every earlier rank is invisible modulo `81`.

### Theorem 4.1 — lifted previous-active state

Put

`Z_0 = Z-9A_q-27A_r (mod81)`,

`U_p = 2^(beta-1) Z_0 -9K_q-27K_r (mod81)`.

Then

`boxed: Z_0 == T_*^- (mod81)`,

`boxed: U_p == T_p^+ (mod81)`.

The unique residue `V_27 mod27` satisfying

`boxed:`

`3V_27 == 2U_p+1-9X_q-27X_r (mod81)`              (4.1)

is exactly

`boxed: V_27 == T_p^- (mod27)`.                      (4.2)

Classification: **analytic theorem**.

This is a strict precision lift over RL69's `T_p^- mod9`.

---

## 5. The mod-9 lift of `T_q^-`

Put

`gamma=b_p-b_q`.

Define the corrections strictly between `b_q` and `b_p`:

`L_q = 2^(a_q-b_q-1) mod9` if `b_q<a_q<b_p`, else `0`,

`L_r = 2^(a_r-b_q-1) mod3` if `b_q<a_r<b_p`, else `0`.

Define simultaneous indicators at `b_q`:

`Y_q=1` iff `a_q=b_q`, else `0`,

`Y_r=1` iff `a_r=b_q`, else `0`.

Corollary 2.3 with `M=3` shows that ranks earlier than `r` are invisible modulo `27`.

### Theorem 5.1 — fifth backward state digit

Put

`U_q = 2^(gamma-1)V_27 -3L_q-9L_r (mod27)`.

Then

`boxed: U_q == T_q^+ (mod27)`.

The unique residue `S_9 mod9` satisfying

`boxed:`

`3S_9 == 2U_q+1-3Y_q-9Y_r (mod27)`                 (5.1)

is exactly

`boxed: S_9 == T_q^- (mod9)`.                        (5.2)

Classification: **analytic theorem**.

RL70 had only `T_q^- mod3`; RL71 recovers the full mod-9 state.

---

## 6. Push across `b_r` and recover `delta_(p-3)` parity

Assume `r=p-2` exists. Put

`theta=b_q-b_r`.

The RL70 `M=2` step can now be applied with input `S_9=T_q^- mod9`.

Define

`tau_r = 2^(delta_r-1) mod3` if `0<delta_r<theta`, else `0`,

`sigma_r=1` iff `delta_r=0`, else `0`.

Put

`U_r = 2^(theta-1)S_9 -3tau_r (mod9)`.

Then the unique `S_r mod3` satisfying

`boxed: 3S_r == 2U_r+1-3sigma_r (mod9)`              (6.1)

obeys

`boxed: S_r == T_r^- (mod3)`.                        (6.2)

Now assume `h=p-3` exists and put

`phi=b_r-b_h`.

Exactly as in RL69/RL70,

- `S_r=1` iff `phi` is odd;
- `S_r=2` iff `phi` is even.

Since

`delta_h=(a_h-b_r)+phi`,

we obtain:

### Corollary 6.1 — exact `delta_(p-3)` parity selector

Let `eta_r=1` for `S_r=1` and `eta_r=0` for `S_r=2`. Then

`boxed: delta_h == (a_h-b_r)+eta_r (mod2)`.           (6.3)

Classification: **analytic corollary**.

---

## 7. Exact q=5 state/phase match

Let

`E_j=2^(b_j)(2^(delta_j)-1)`.

Define

`C_5=E_*+3E_p+9E_q+27E_r+81E_h`,

`C_4=E_*+3E_p+9E_q+27E_r`.

Under the frozen full-phase extendability hypothesis, the inherited rank-tail ladder gives

`N == 2-2^(1-k)-4*3^(s+1)2^(-a)C_5`

`     (mod3^(s+6))`.                                  (7.1)

Modulo `3`,

`E_h==0` if `delta_h` is even,

`E_h==2^(b_h)` if `delta_h` is odd.

Let `chi_h=delta_h mod2`, determined exactly by Corollary 6.1.

### Theorem 7.1 — state/phase match through rank `p-3`

With

`R_4=2-2^(1-k)-4*3^(s+1)2^(-a)C_4`,

full-phase extendability gives

`boxed:`

`N == R_4 - chi_h 4*2^(b_h-a)3^(s+5)`

`     (mod3^(s+6))`.                                  (7.2)

Thus the q=5 phase digit is zero precisely when the state-side selector says `delta_(p-3)` is even, and is the unique nonzero rank-tail correction precisely when the state-side selector says it is odd.

Classification: **analytic theorem conditional on the frozen full-phase hypothesis**.

Again, this is compatibility, not contradiction.

---

## 8. Reverse reconstruction and the mod-162 selector

The lifted state can be reversed at the same precision.

From `V_27`, define

`U_p(V) = (3V_27-1+9X_q+27X_r)/2 (mod81)`.

Then define

`W_81 = 2^(1-beta)(U_p(V)+9K_q+27K_r)`

`       +9A_q+27A_r (mod81)`.

Theorem 4.1 gives

`boxed: W_81 == Z (mod81)`.                            (8.1)

The exact terminal formula retained from RL68 is

`Z=(2^(delta_*)(2R-5)-9*2^lambda+1)/3`.

Multiplying by `3` and reducing modulo `243` gives:

### Theorem 8.1 — mod-243 terminal compatibility

`boxed:`

`2^(delta_*)(2R-5)`

` == 9*2^lambda -1 +3W_81 (mod243)`.                 (8.2)

The factor `2R-5` is a unit modulo `3`. Also `2` has order

`162`

modulo `243`.

### Corollary 8.2 — exact mod-162 selector

`boxed:`

`(R mod243, lambda, beta, V_27, A_q,A_r,K_q,K_r,X_q,X_r)`

`determines delta_* mod162 uniquely.`

Classification: **analytic corollary**.

This extends the nested last-active selector ladder

`mod6 -> mod18 -> mod54 -> mod162`.

---

## 9. Stronger residue-floor area bound

Let

`c_162 in {1,...,162}`

be the least positive representative of the selected `delta_* mod162` class, with residue zero represented by `162`.

Then

`delta_*=c_162+162t`, `t>=0`.

Because both `p` and `j_*` are active,

`H>=delta_p+delta_*`.

### Theorem 9.1 — mod-162 residue floor

`boxed: H>=delta_p+c_162=beta+lambda+c_162`.          (9.1)

Therefore every hypothetical nested Gate-A violation `H<k` must satisfy

`boxed: beta+lambda+c_162<=k-1`.                      (9.2)

Classification: **analytic theorem**.

### Corollary 9.2 — exact last-active displacement for odd `k<=165`

Nested geometry gives `delta_p>=2`. If `t>=1`, then

`delta_p+delta_* >= 2+(1+162)=165`.

Hence in any hypothetical nested violation with odd

`boxed: k<=165`, 

one has `H<=k-1<=164`, so `t>=1` is impossible. Therefore

`boxed: delta_*=c_162 exactly`.                        (9.3)

Classification: **analytic corollary**.

This is a substantial extension of RL70's `k<=57` exact-value window. It is still a sieve, not a global Gate-A theorem.

---

## 10. Structural continuation and strategic pivot

The exact finite-window formulas explain the pattern seen in RL68–RL71.

### Theorem 10.1 — one digit, one rank

At any fixed consecutive-y backward crossing, increasing the working modulus from `3^M` to `3^(M+1)` makes at most one additional earlier rank visible: the rank whose correction exponent is exactly `M`.

Likewise, in the nested terminal recovery, increasing the terminal working modulus from `3^M` to `3^(M+1)` makes at most one additional earlier rank visible.

Classification: **analytic corollary of Theorems 2.2 and 3.1**.

### Consequence

For every fixed finite depth, the backward state ladder can in principle be continued by retaining a finite suffix of the ordered rank stack. The repeated state/phase digit agreements are therefore not isolated miracles; they reflect two exact encodings of the same rank displacements.

This changes the strategic interpretation of the obstruction:

- **useful:** the finite-window operator is now a reusable exact lemma, and higher state precision can be generated without replaying the whole prefix;
- **not useful by itself:** extending q=6, q=7, ... and observing further state/phase agreement is not a contradiction mechanism;
- **needed next:** combine the finite-window state data, the rank-tail phase ladder, and the residue floors with a genuinely coupled **size/order**, **full-denominator ownership**, **defect-energy**, or **global packing/weighted-difference** theorem.

This is the main reason RL72 should be a global audit/synthesis session rather than another automatic one-digit extension.

---

## 11. Exact bounded audit

`verification/verify_rl71_fifth_backward_digit.py` independently recomputes canonical RL states from the exact recurrence through `MAX_M=18`.

Fresh results:

- bounded canonical terminal paths: `2,596`;
- exact consecutive-y polynomial checks: `20,115`;
- nested `g=0` terminal interfaces: `1,222`;
- exact nested terminal polynomial checks: `1,222`;
- `T_p^- mod27` lifts: `1,222`;
- `T_(p-1)^- mod9` lifts: `1,222`;
- pre-`b_(p-2)` mod-3 pushes: `1,212`;
- `delta_(p-3)` parity-selector checks: `1,161`;
- full-phase q=5 digit matches: `1,052`;
- nested `delta_* mod162` lifts: `1,222`;
- mod-162 residue-floor checks: `1,222`;
- nonzero second-earlier-rank corrections were actually encountered in every correction zone:
  - after/at `b_*`: `146`;
  - strictly between `b_p` and `b_*`: `113`;
  - simultaneous at `b_p`: `241`;
  - strictly between `b_q` and `b_p`: `107`;
  - simultaneous at `b_q`: `365`;
- status: `RL71 fifth-backward-digit verifier: PASS`.

The nonzero `r=p-2` counts are important audit evidence: the new second-rank terms are not cosmetic. Omitting them fails at the new precision.

The bounded verifier is a falsification/audit tool. It is not the infinite proof of Sections 2–10.

---

## 12. Rejected or insufficient routes

### F1. Continue the q-digit ladder and call compatibility a contradiction

Rejected. The exact finite-window theorem explains why state and phase can continue to agree. Agreement is expected consistency, not impossibility.

### F2. Lift from mod27 to mod81 while keeping only rank q

Rejected. Rank `r=p-2` contributes at the new visible 27-level. The bounded audit encounters such nonzero corrections hundreds of times.

### F3. Treat `delta_* mod162` as an upper bound

Rejected. The valid consequence is the lower bound `delta_*>=c_162`; representatives `c_162+162t` remain unbounded in general.

### F4. Claim all odd `k<=165` nested cases closed

Rejected. Inside a hypothetical violation one gets `delta_*=c_162` exactly, but one still needs a uniform incompatibility with the remaining rank area / tail / full-phase constraints.

### F5. Replace the exact finite-window formulas by a separable cap on ranks

Rejected. RL48's inherited barrier remains decisive. RL71 preserves ordered positions and exact 3-adic correction weights.

### F6. Reopen Gate B merely because the state ladder is longer

Rejected. Gate B remains frozen/open/audit-dependent. A valid bridge must use genuine global ownership/divisibility or another exhaustive contradiction, not local phase compatibility alone.

---

## 13. Exact proof state after RL71

Retain every RL62–RL70 correction, theorem, finite certificate, and demotion.

New RL71 analytic upgrades are limited to:

1. the exact consecutive-y backward polynomial (2.1)–(2.2);
2. the finite-window visibility theorem for any fixed 3-adic precision;
3. the exact all-rank nested terminal polynomial (3.1)–(3.3);
4. recovery of `T_p^- mod27` using exactly ranks `q` and `r` at the new precision;
5. recovery of `T_q^- mod9` using exactly ranks `q` and `r` at the new precision;
6. recovery of the state before `b_r` modulo `3`, selecting `delta_(p-3) mod2` when that rank exists;
7. exact q=5 state/phase agreement through rank `p-3`;
8. a unique nested `delta_* mod162` selector;
9. the stronger area floor `H>=delta_p+c_162` and exact `delta_*=c_162` inside any hypothetical nested violation with odd `k<=165`;
10. the structural conclusion that higher digit matching is finitely extendable and should not be pursued as a contradiction by itself.

Gate A remains open globally. Gate B remains open/frozen/audit-dependent. No result upgrades `J<=2^H` from conjectural bounded evidence.

---

## 14. Recommended next step: RL72 global audit and synthesis

Do **not** make the default RL72 task “push to q=6”.

RL72 should be a global audit/roadmap/review/planning and **lemma-synthesis** session using the searchable GitHub `sessions/RLxx/` archive.

The audit should:

1. start from the RL61 whole-tree audit as the previous global baseline;
2. incorporate the RL62 repair and every valid RL63–RL71 theorem;
3. build a session-by-session lemma catalogue with exact hypotheses, status, dependencies, outputs, and whether each lemma remains live after later repairs;
4. explicitly audit the major historical lemma clusters:
   - exact radius-3 closure and its hypotheses (RL7–RL19),
   - RL19/RL20 global weighted-difference / population / packing identities,
   - the RL20 local-grammar countermodel and surviving balanced-return / strict-excursion routes,
   - RL43–RL50 phase, defect, same-root, radius-3 bridge, and rank-relaxation work,
   - RL54–RL61 defect/potential/terminal-tail work and all later corrections,
   - RL63–RL71 ownership, full-phase, rank-tail, interface, backward-state, and residue-floor lemmas;
5. identify compatible theorem chains that have never been tried together;
6. attempt at least one concrete synthesis, preferably with a contradiction template such as
   `D | W` and `0<|W|<D`,
   or a genuinely coupled lower bound forcing Gate A;
7. rank the remaining top-level obligations by global leverage and identify any branch that can now actually be closed;
8. preserve the verification economy rule: use searchable mirrors and existing provenance/audit ledgers first, and re-run historical expensive verifiers only when a synthesis depends on an unresolved definition or a contradiction appears.

The dedicated RL72 target note in this bundle expands this programme.

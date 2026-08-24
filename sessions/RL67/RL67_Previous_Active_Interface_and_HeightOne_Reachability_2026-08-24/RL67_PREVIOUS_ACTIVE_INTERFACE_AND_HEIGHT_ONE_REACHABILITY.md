# RL67 — previous-active interface and height-one reachability

Date: 2026-08-24

## Status

This note continues from the checksum-clean RL66 state under the mandatory **verification economy rule**. The incoming RL66 outer sidecar, freshly unpacked internal manifest, and `verification/run_fast_rl66_verifiers.sh` all passed before new mathematics was attempted. No historical expensive certificate was recursively rerun.

RL67 does **not** prove odd-`k` Gate A in general, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture. It does sharpen the live odd-`k` obstruction in four ways:

1. every canonical terminal path has at least **two** active displacement ranks;
2. every terminal path has `H>=3`, hence Gate A is analytically closed for the smallest remaining exponent `k=3`;
3. the last/previous-active interface is put into an exact separated/cross/nested normal form, with 2-adic transfer identities and a previous-active parity digit;
4. the RL66 phase ladder is extended by one exact digit carrying the parity of the previous active displacement.

A stronger empirical height-one inequality `J<=2^H` survived a new bounded falsification scan, but RL67 explicitly does **not** promote it to a theorem. A naive magnitude-only induction is disproved by exact abstract local macros, so any proof of that inequality must use canonical reachability, not only local transition size.

---

## 1. Frozen notation

Retain RL66 notation:

- canonical internal start `(d,T,H)=(1,-14,0)` and `J=T+3^d-2^d`, so the start is `J=-13`;
- terminal state `(d,J)=(1,2^k)` with `k` odd by RL66;
- one-positions `a_1<...<a_r`, `b_1<...<b_r`;
- rank displacements `delta_j=a_j-b_j>=0` and `H=sum_j delta_j`;
- last active rank `j_*`, with `b_*=b_(j_*)`, `a_*=a_(j_*)`, `delta_*>0`;
- terminal synchronized suffix length `n`, with `s` occurrences of `11`;
- terminal-suffix entry `R:=J_tail`, the height-one state immediately after `a_*`;
- rank terms `E_j=2^(b_j)(2^(delta_j)-1)`;
- full phase, when imposed, has `a=m+k+1`, `ell=r+3`, `M=2^a-3^ell`, and positive quotient `N`.

RL66 proved

`R == 1+2^(delta_*) (mod3)`

and the rank-tail phase ladder

`N == 2-2^(1-k)-4*3^(s+1)2^(-a)C_q (mod 3^(s+q+1))`.

No RL67 statement changes the frozen RL62–RL66 proof classifications.

---

## 2. A lower bound on the terminal-tail entry

### Lemma 2.1 — `R>=3`

For every canonical terminal path, the synchronized terminal-suffix entry satisfies

`boxed: R>=3`.

If the terminal synchronized suffix is empty, `R=2^k>=8`. Otherwise reverse the legal height-one synchronized suffix from `2^k` using

- reverse `00`: `J -> 2J-1`;
- reverse `11`: `J -> (2J-1)/3` when integral and legal.

Starting from `2^k>=8`, every legal reverse state remains a positive odd integer; the smallest legal value reached in such a reverse chain is at least `3`.

Classification: **analytic theorem**.

---

## 3. Exact isolated-last-active transfer

Suppose the path is at height one immediately before `b_*`; write that state as `P`. Then there is no earlier outstanding x-rank at `b_*`. Because `j_*` is the last active rank, the last active block is exactly

`01, 00^(delta_*-1), 10`.

At height one, `01` sends

`P -> (3P+6)/2`

at height two. At height two, `00` has fixed point `5`, and `10` sends `J -> J/2`. A direct calculation gives:

### Theorem 3.1 — isolated transfer identity

`boxed: 3P-4 = 2^(delta_*) (2R-5)`.                 (3.1)

Since `2R-5` is odd,

`boxed: delta_* = v2(3P-4)`.                         (3.2)

By Lemma 2.1, `2R-5>=1`; hence

`boxed: P>=2`.                                       (3.3)

Thus an isolated final active rank must start from a **positive** even height-one state.

A useful 2-adic corollary is

`P == 4*3^(-1) (mod 2^(delta_*))`;

in particular, if `delta_*>=3`, then `P==4 (mod8)` and `v2(P)=2`.

Classification: **analytic theorem**.

---

## 4. A canonical terminal path has at least two active ranks

### Theorem 4.1

Every canonical terminal path has at least two indices with `delta_j>0`.

### Proof

Assume there is exactly one active rank, namely `j_*`. Then every earlier rank has zero displacement, so the entire prefix before `b_*` is synchronized at height one. Starting from canonical `J=-13`, the synchronized maps

`00: J -> (J+1)/2`,

`11: J -> (3J+1)/2`

preserve `J<=0` whenever they are legal. Hence the state `P` immediately before `b_*` satisfies `P<=0`.

With no earlier active rank, nothing is outstanding at `b_*`; therefore the last active rank is isolated and Theorem 3.1 applies. But (3.3) gives `P>=2`, a contradiction.

QED.

Classification: **analytic theorem**.

This strengthens RL66 Lemma 2.1, which proved only that at least one active rank exists.

---

## 5. Exact canonical synchronized prefix before the first active rank

The canonical start gives a particularly small synchronized pre-active automaton.

For odd height-one `J`, exactly one synchronized choice keeps the next state odd:

- if `J==1 (mod4)`, `00` keeps the output odd;
- if `J==3 (mod4)`, `11` keeps the output odd.

Starting from `-13`, the stay-odd synchronized trajectory is the 3-cycle

`boxed: -13 -> -19 -> -9 -> -13`.

Choosing the other synchronized branch exits to an even height-one state, forcing the first mismatch. The only possible first-mismatch entry states are therefore

`boxed: P_0 in {-6,-28,-4}}`.                       (5.1)

If the first active rank is isolated, Theorem 3.1 fixes its displacement and exit state exactly:

`boxed: (-6,1,-3), (-28,3,-3), (-4,4,2)}`            (5.2)

where each triple is `(P_0, delta, R)`.

Classification: **analytic theorem**.

This is a canonical-start fact; it is not a statement about arbitrary height-one inputs.

---

## 6. No terminal path has `H<=2`

### Theorem 6.1

`boxed: every canonical terminal path has H>=3`.      (6.1)

### Proof

By Theorem 4.1 there are at least two active ranks, so `H>=2`. Suppose `H=2`. Then there are exactly two active ranks and both have displacement `1`.

Let the first active rank start at the first mismatch.

**Case 1: the first active rank closes before the second active y-one.**
Then it is isolated. From (5.2), displacement `1` forces the first-mismatch entry `P_0=-6` and the first active exit is `-3`.

With only one active rank left, the intervening path is synchronized at height one. From `-3`, the stay-odd synchronized states are `-3 -> -1 -> -1`; the possible even synchronized exits are `-4` and `0`. But

`v2(3(-4)-4)=4`,

`v2(3(0)-4)=2`,

so neither can start an isolated active rank of displacement `1` by Theorem 3.1. Contradiction.

**Case 2: the second active y-one occurs before the first active rank closes.**
Because the first displacement is `1`, its x-one is in the very next column. Hence the only possible overlap is a shared `11` column: the two active ranks form the height-two block

`01,11,10`.

If `P_0` is its height-one entry, direct composition gives the height-one exit

`R=(9P_0+24)/8`.

Every possible canonical first-mismatch state in (5.1) satisfies `P_0<=-4`, hence `9P_0+24<0`. Therefore the active block exits nonpositively. No later active rank exists, so the remaining path is synchronized and cannot reach positive terminal `2^k`. Contradiction.

Thus `H=2` is impossible, and `H>=3`.

QED.

Classification: **analytic theorem**.

### Corollary 6.2 — analytic closure of `k=3`

RL66 proves terminal `k` is odd, and the terminal definition has `k>=3`. For `k=3`, Theorem 6.1 gives

`H>=3=k`.

Hence Gate A is analytically resolved for `k=3`.

This does not materially replace the inherited `H<=24` exact finite certificate; it is a theorem-level strengthening for the smallest odd exponent.

---

## 7. Previous-active rank and the zero-rank gap

Let `p<j_*` be the previous active rank, whose existence is guaranteed by Theorem 4.1, and put

`g=j_*-p-1`.

Then ranks `p+1,...,j_*-1` have zero displacement.

### Theorem 7.1 — `g>=1` forces a separated previous active return

If `g>=1`, then

`a_p < a_(p+1)=b_(p+1) < ... < a_(j_*-1)=b_(j_*-1) < b_*`.

Consequently:

1. the previous active rank has completely returned the path to height one at `a_p`;
2. every column from `a_p+1` through `b_*-1` is synchronized at height one;
3. this bridge contains exactly `g` columns `11`;
4. the last active rank is isolated, so Theorem 3.1 applies.

Let

`A = J` immediately after `a_p`,

`P = J` immediately before `b_*`,

and let `u=(u_0,...,u_(L-1))` be the synchronized bridge word of length

`L=b_*-a_p-1`,

with `sum u_i=g`.

Since `P>=2` and synchronized height-one maps preserve nonpositivity, necessarily

`boxed: A>0`.                                         (7.1)

Thus a positive height-one return already occurs **before** the last active rank whenever `g>=1`.

Classification: **analytic theorem**.

---

## 8. Exact synchronized-bridge digit and previous-active parity

For a height-one synchronized bridge `u`, define

`B(u)=sum_(i=0)^(L-1) 2^i 3^(sum_(h=i+1)^(L-1) u_h)`.

Unrolling

`J_(i+1)=(3^(u_i)J_i+1)/2`

gives the exact bridge equality

`boxed: 2^L P = 3^g A + B(u)`.                        (8.1)

Because the next y-rank after `b_p` occurs only after `a_p` in this separated geometry, the RL66 mod-3 argument applies to the previous active rank as well:

`boxed: A == 1+2^(delta_p) (mod3)`.                  (8.2)

Combining (8.1) and (8.2):

### Theorem 8.1 — previous-active bridge digit

`boxed: 2^L P-B(u) == 3^g(1+2^(delta_p)) (mod 3^(g+1))}`.  (8.3)

Equivalently,

- if `delta_p` is odd,
  `2^L P-B(u) == 0 (mod 3^(g+1))`;
- if `delta_p` is even,
  `2^L P-B(u) == 2*3^g (mod 3^(g+1))`.

Thus the `(g+1)`-st 3-adic bridge digit recovers the parity of the previous active displacement without opening the earlier canonical prefix.

Classification: **analytic theorem**.

This is a state-side analogue of the RL66 rank-tail phase-digit ladder.

---

## 9. One more exact full-phase digit from the previous active rank

The RL66 rank recursion has, with `g` zero ranks between `p` and `j_*`,

`C_(g+2)=E_(j_*) + 3^(g+1) E_p`.

Take `q=g+2` in the RL66 phase ladder. Define the already-known last-active residue

`R_g = 2-2^(1-k)`

`      -3^(s+1)2^(-(k+n+delta_*))(2^(delta_*)-1)`.

Then modulo `3^(s+g+3)` only `E_p mod3` is newly exposed. Since

`E_p=2^(b_p)(2^(delta_p)-1)`, 

`E_p==0 (mod3)` for even `delta_p`, and `E_p==2^(b_p) (mod3)` for odd `delta_p`.

### Theorem 9.1 — previous-active phase digit

Under full-phase extendability,

`boxed: N == R_g - chi_p * 4*2^(b_p-a) 3^(s+g+2)`

`       (mod 3^(s+g+3))`,                            (9.1)

where

`chi_p=0` if `delta_p` is even,

`chi_p=1` if `delta_p` is odd.

So the next phase digit is **zero** for an even previous displacement and **nonzero** for an odd previous displacement.

Classification: **analytic theorem**, conditional on the same frozen full-phase hypothesis as the RL66 digit ladder.

This is genuine progress on the RL67 target: the previous active rank is now visible both in the canonical height-one bridge state and in the full-phase quotient. It still does not bound `N` by size.

---

## 10. Exact `g=0` last-two-active trichotomy

Now take `g=0`, so `p=j_*-1`. Put

`rho=a_p-b_*`.

There are exactly three geometries.

### 10.1 Separated: `rho<0`

Then `a_p<b_*`, the last active rank is isolated, and Theorem 3.1 applies. The bridge from the previous active exit `A` to `P` contains no `11` rank because `g=0`, so it is all-`00` of length

`L=b_*-a_p-1`.

Hence

`boxed: A = 1+2^L(P-1)`.                              (10.1)

Together with `A==1+2^(delta_p) (mod3)`, this fixes the parity of `delta_p` from the terminal-derived `P` and the zero-column bridge length `L`.

### 10.2 Shared column / cross: `rho=0`

Here `a_p=b_*`. The shared column is `11`; immediately before it the height is exactly `d=2`. Let that height-two state be `C`.

After the shared `11`, the path remains at height two, then follows `00^(delta_*-1),10`. Direct composition gives

`boxed: 3C-7 = 2^(delta_*) (2R-5)`,                  (10.2)

hence

`boxed: delta_*=v2(3C-7)`.                            (10.3)

The previous active displacement parity is already encoded in `C mod3`. After the previous y-one, `T==1 mod3`; there are `delta_p-1` y-zero steps before the shared column. Since `C=T+5` at height two,

`boxed: C==0 (mod3) if delta_p is odd`,

`boxed: C==1 (mod3) if delta_p is even`.              (10.4)

A valid cross interface never has `C==2 mod3`.

### 10.3 Nested: `rho>0`

Put

`lambda=a_p-b_*`, so `1<=lambda<delta_*`.

Immediately before `a_p`, all earlier x-ranks have closed, both y-ranks `p` and `j_*` are present, and neither x-rank `p` nor `j_*` has yet closed; therefore the height is exactly `d=3`. Let that state be `C`.

The column `a_p` is `10`, dropping to height two. Then only `00` columns occur until the final `10` at `a_*`. Therefore

`boxed: C-10 = 2^(delta_*-lambda)(2R-5)`,             (10.5)

and

`boxed: delta_*-lambda = v2(C-10)`.                   (10.6)

The mod-3 state records the overlap parity:

`boxed: C==2 (mod3) if lambda is odd`,

`boxed: C==0 (mod3) if lambda is even`.               (10.7)

This nested case is the only member of the trichotomy in which RL67 has not yet recovered the parity of `delta_p` from the terminal interface alone; the earlier descending x-ranks before `a_p` remain the live nonseparable obstruction.

Classification of 10.1–10.3: **analytic theorem**.

---

## 11. Strong height-one reachability candidate — evidence only

During RL67, a much stronger possible invariant emerged:

`CONJECTURAL: for every canonical reachable state with d=1 and J>0, J<=2^H`.    (11.1)

If (11.1) were proved, then at a terminal state `J=2^k` it would immediately imply `H>=k`, closing Gate A.

The independent RL67 falsification scan compresses states by exact `(d,T,H)` and checks every reachable state through depth `22`. It found no violation:

- positive height-one checks: `9,821`;
- maximal ratio witness: at depth `10`, `J=8`, `H=3`, giving equality `J/2^H=1`;
- status: no bounded counterexample.

This is **computational evidence only**.

### 11.1 Why RL67 does not promote (11.1)

A magnitude-only induction across a synchronized height-one bridge followed by an isolated active excursion is false for abstract legal local states.

Two exact counterexamples are:

1. `A=1`, synchronized `11` gives even `P=2`; then `v2(3P-4)=1` and the isolated active excursion exits at `R=3`. Thus `R>2^1 A`.
2. `A=7`, three synchronized `11` steps give `7->11->17->26`; then `v2(3*26-4)=1` and the isolated active excursion exits at `R=21`. Thus `R>2^1 A`.

These inputs are not asserted to be canonically reachable with a small enough `H`; that is exactly the point. Any proof of (11.1) must exploit the **canonical reachable subset**, not just a local size inequality for arbitrary positive height-one states.

The unique synchronized choice that keeps an odd height-one state odd is

`G(J)=(J+1)/2` for `J==1 mod4`,

`G(J)=(3J+1)/2` for `J==3 mod4`.

For example `3<->5` is a stay-odd cycle. This explains why arbitrary synchronized pumping cannot be handled by a simple decreasing magnitude potential. RL67 therefore records (11.1) as a high-value conjectural route, not a theorem.

Classification: **exact bounded evidence + rejected proof shortcut**.

---

## 12. Independent RL67 audit

`verification/verify_rl67_previous_active_interface.py` independently audits the new formulas from the exact RL recurrence.

Fresh bounded terminal results at `MAX_M=18`:

- canonical terminal paths: `2,596`;
- terminal at-least-two-active checks: `2,596`;
- terminal `H>=3` checks: `2,596`;
- isolated last-active transfer checks: `743`;
- `g>=1` synchronized bridge checks: `329`;
- `g>=1` previous-active parity-digit checks: `329`;
- previous-active phase-digit checks: `2,178`;
- interface cases: `631` cross, `1,222` nested, `743` separated.

The same verifier independently checks:

- first synchronized-prefix even exits `(-6,-28,-4)`;
- first isolated-active triples `(-6,1,-3)`, `(-28,3,-3)`, `(-4,4,2)`;
- the `H=2` obstruction logic;
- the depth-22 height-one reachability falsification scan described in section 11;
- the two exact abstract macro counterexamples to naive magnitude induction.

The verifier is a falsification/audit tool. It does not establish the infinite theorems; those are proved algebraically above.

---

## 13. What RL67 changes in the live obstruction

Inherited RL66 already eliminated even terminal `k`. RL67 now adds:

1. `k=3` is analytically Gate-A safe because every terminal path has `H>=3`;
2. every terminal path has at least two active ranks;
3. for `g>=1`, the last active rank is isolated and the previous active rank has already returned to a **positive** height-one state;
4. the synchronized bridge across `g` zero ranks gives an exact 3-adic digit selecting `delta_p mod2`;
5. the full-phase quotient gains the matching previous-active digit modulo `3^(s+g+3)`;
6. `g=0` is no longer a single opaque case: it is separated, cross, or nested, with exact 2-adic transfer identities in all three cases;
7. only the nested interface still hides the previous active displacement parity behind an earlier descending-rank stack.

Gate A remains open for the uniform odd-`k` problem (in particular the unbounded `k>=5` sector). The inherited `H<=24` result remains an exact finite certificate only. Gate B remains frozen/open/audit-dependent.

---

## 14. Recommended RL68 attack

1. **Nested `g=0` case first.** Starting from (10.5), expose the x-ranks still outstanding between `b_*` and `a_p`. Derive the exact y-silent descent polynomial from the state immediately after `b_*` to the height-three state `C`, retaining rank order. The goal is to recover `delta_p mod2` (or stronger) in the nested case without separable relaxation.
2. **Bridge digit lift for `g>=1`.** Equation (8.1) gives the previous active state exactly after dividing by `3^g`; combine the exact separated previous-active geometry with one more 3-adic digit of that state to seek information beyond parity of `delta_p`.
3. **Canonical height-one reachability track.** Treat `J<=2^H` only as a conjecture. Search for an invariant that uses the exact canonical first-mismatch cycle (5.1), active-interface valuations, and the reachable subset of the stay-odd map `G`. Do not use magnitude-only macro induction; RL67 gives exact counterexamples to that shortcut.
4. Keep the odd terminal-tail split from RL66 explicit (all-`00`, mixed, nonmaximal all-`11`, maximal all-`11`).
5. Use bounded scans only as falsification laboratories. Do not extend blind depth as a substitute for the uniform theorem.
6. Keep Gate B frozen unless Gate A closes or a directly reusable radius-3 hypothesis appears.

A strong RL68 result would recover the previous-active parity/state digit in the nested case or prove a canonical-reachability inequality strong enough to imply `J<=2^H`. A meaningful partial result would derive the exact nested y-silent descent recurrence with the third-last active rank exposed.

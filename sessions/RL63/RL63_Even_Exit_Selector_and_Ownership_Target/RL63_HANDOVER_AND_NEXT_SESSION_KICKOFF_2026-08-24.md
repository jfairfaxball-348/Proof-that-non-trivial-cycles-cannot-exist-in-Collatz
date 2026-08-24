# RL63 — even-exit selector, unrestricted pump obstruction, and ownership target

Date: 2026-08-24

## Status

**AUTHORITATIVE OUTGOING RESEARCH STATE. Gate A remains open.**

RL63 began from the checksum-clean RL62 terminal-potential repair state, reran all three incoming verifier programmes successfully, and continued the revised Gate-A programme. The main new result is not a closure but a sharp structural reduction: dangerous height-one synchronized exits lie in explicit 2-adic entry cylinders, and an infinite exact all-`11` family shows that those cylinders are genuinely populated in the unrestricted local quotient. Therefore the missing Gate-A theorem must use full-phase reachability/ownership of macro entries; no local synchronized scalar or valuation argument can suffice.

No claim here proves Gate A, Gate B, RL, nontrivial-cycle exclusion, or the Collatz conjecture.

---

## 1. Incoming RL62 integrity and regression status

Authoritative incoming archive:

`RL62_RL59_Terminal_Potential_Repair_2026-08-24.zip`

Outer SHA-256:

`b827ce98c42e520324dd5c7b9f018a3f51351348e13e323043c4c38b1d7b2396`

The supplied sidecar matched exactly. The internal `SHA256SUMS.txt` passed for every file.

Fresh RL63-session replays:

- terminal-potential sign verifier: **PASS**, exact expected output;
- RL45 H<=24 explicit-structure C++ verifier: **PASS**, exact output match;
- RL45 H<=24 packed-key independent C++ verifier: **PASS**, exact output match.

At H=24 both RL45 implementations retain the exact finite certificate:

- reachable states: `8,664,154`;
- maximum `d=8`;
- maximum `|J|=110,392,611,511,170`;
- maximum positive-state margin `v2(J)-K=-3`;
- no violation.

Classification: **exact finite certificate, independently cross-implemented; not a uniform proof.**

---

## 2. Frozen correction from RL62 — do not regress

RL59 used the wrong sign in the height dependence of a positive terminal potential.

With exact convention

`d=1+p_y-p_x`, `g=2^i/3^(p_x)`,

RL62 rederived the correct bound

\[
Jg\le \frac92\,\zeta\,3^d,
\]

not RL59's decreasing-height expression

\[
Jg\le \frac12\,\zeta\,3^{4-d}.
\]

The exact inherited RL47 witness `(a,ell,t)=(65,41,2)` reaches `(i,p,d,J)=(58,37,2,64)` immediately before the final `10`; its `Jg` is exactly **9 times** the false RL59 height-two cap and exactly attains the corrected cap. The concrete RL59 Type-B exit has `P_exit=480`; the old cap is about `145.37`, but the corrected cap is about `1308.33`, so the claimed contradiction disappears.

### Still valid after the repair

Retain, subject to their original provenance:

1. exact RL47/RL48 phase-word normalization and one-excursion identities;
2. exact defect/zero-position identities, including inherited `E=Zx-Zy` normalization;
3. synchronized height-one telescope `Psi=g(J+1)/2`, where `00` adds `g` and `11` adds `0`;
4. shortcut-Collatz conjugacy of the synchronized height-one subsystem;
5. raw terminal-ancestor `N(K)` searches as standalone finite facts;
6. pre-RL59 fixed-survivor prefix certificates with their own dependencies;
7. exact RL45 `(d,H,J)` Markov quotient and the reduction of uniform Gate A to terminal valuation;
8. phase squeeze / safe continued-fraction calculations not using the false RL59 terminal potential.

### Demoted until replacement proof exists

Do not use as theorem:

1. RL59 `Jg <= zeta*3^(4-d)/2` for `d>1`;
2. Type-B maximal-pump neutralization using that cap;
3. generic terminal bounding of every nonterminal positive synchronized pump by that potential;
4. post-final-`10` `J0*g0 <= (3/2)zeta` from the false height-two estimate;
5. `M_final>45/8` and `M_final>23/4` where dependent on it;
6. forced terminal counts/runs and huge z-floors derived from those mass bounds;
7. RL61 `T.pot` analytic ledger entry;
8. RL61 `T.K25-39` derived z-floor column (raw `N(K)` remains finite data);
9. RL61 external `K<=129` reduction as currently proved, because its admissible start bound used the false terminal mass estimate.

---

## 3. Uniform versus fixed-survivor constants

### Structural/uniform within full-phase hypotheses

Retain:

- exact defect and zero-position identities;
- synchronized-block telescopes;
- exact prefix x-zero cap `g <= (9/16) zeta^2`;
- conditional on the accepted external computational floor `N>=2^71` plus analytic phase squeeze, `zeta^2<136/135`, hence the **uniform sequential cap** `g<17/30`.

The `17/30` use must always carry its external-floor provenance.

### Fixed safe-CF survivor only

Do **not** transplant into uniform Gate A:

- `E<5/3`;
- strengthened `Zx>143/12`;
- large finite terminal-tail bootstrap constants tied to the survivor and/or the false RL59 mass route.

The safe-CF survivor may be used as a falsification/stress-test instance only.

---

## 4. Frozen RL45 Gate-A quotient

Definitions:

\[
J=T+3^d-2^d,
\qquad
K=H+\frac{d(d+1)}2-1.
\]

Start:

`(d,H,J)=(1,0,-13)`.

Transitions:

- odd `J`:
  - `00`: `J'=(J+3^d-2^d)/2`, `d'=d`;
  - `11`: `J'=(3J+2^d-1)/2`, `d'=d`;
- even `J`:
  - `01`: `J'=(3J+3^(d+1)-2^d-1)/2`, `d'=d+1`;
  - `10`: `J'=J/2`, `d'=d-1` if `d>1`;
- all edges: `H'=H+d-1`.

Uniform candidate:

\[
J>0\Longrightarrow v_2(J)\le K.
\]

At terminal `d=1`, `K=H`, exactly the Gate-A valuation inequality.

RL45 proved/certified only a finite range; RL62 extends the exact finite certificate through H=24. **Uniform Gate A remains open.**

---

## 5. New RL63 analytic results

Detailed proofs are in `RL63_EVEN_EXIT_SELECTOR_LEMMA.md`.

### 5.1 Exact T maps

RL63 derives:

- `00: T'=T/2`;
- `11: T'=(3T+3^d-1)/2`;
- `01: T'=(3T-1)/2`;
- `10: T'=(T+3^(d-1))/2`.

Classification: **proved algebraically**.

### 5.2 Exact K increments and 10 invariance

- `00/11`: `Delta K=d-1`;
- `01`: `Delta K=2d`;
- `10`: `Delta K=-1`.

On a legal nonzero `10`, `v2(J)` also falls by exactly one, so

\[
\boxed{v_2(J')-K'=v_2(J)-K.}
\]

Classification: **proved algebraically**.

Interpretation: a `10` return cannot create or repair valuation excess; it transports the same excess margin.

### 5.3 Exact synchronized affine selector

At `d=1`, encode `00` by `x=0`, `11` by `x=1`. For a legal synchronized word `w=(x_0,...,x_{n-1})`, let

\[
s=\sum x_r,
\qquad
C(w)=\sum_{r=0}^{n-1}2^r3^{\sum_{q=r+1}^{n-1}x_q}.
\]

Then

\[
\boxed{2^nJ_n=3^sJ_0+C(w).}
\]

A dangerous positive even exit with `v2(J_n)>H` must satisfy

\[
\boxed{3^sJ_0+C(w)\equiv0\pmod{2^{n+H+1}}.}
\]

For fixed `(w,H)` this is one 2-adic residue class of macro entries because `3^s` is invertible modulo powers of two. First-even legality adds exact odd-prefix congruences.

Classification: **proved analytic lemma**.

This gives the desired ownership interface in explicit arithmetic form: the next theorem must show that genuinely reachable/full-phase-owned macro entries do not lie in these dangerous cylinders.

### 5.4 Infinite unrestricted all-11 obstruction family

For a maximal `11^n` height-one block, write

\[
J_0+1=2^nq,\quad q\text{ odd}.
\]

Then for `0<=r<=n`,

\[
J_r=2^{n-r}3^rq-1,
\]

so all `J_r` for `r<n` are odd and the first even exit is

\[
J_n=3^nq-1.
\]

For any `H>=0,n>=1`, choose odd

\[
q\equiv3^{-n}\pmod{2^{H+1}}.
\]

Then `v2(J_n)>H`.

Classification: **proved infinite exact family**.

### Consequence

This formally kills the strategy “prove Gate A using only unrestricted height-one synchronized dynamics.” The local subsystem itself contains arbitrarily dangerous exits. The proof must use the **admissible-entry restriction** supplied by global reachability/full phase/zero positions/ownership (or an equivalent invariant).

This is the main conceptual advance of RL63.

### 5.5 Reachable equality witness

Exact path

`00 01 10 00 00 01 11 10 11 11`

reaches `(d,H,J)=(1,3,8)`, where `v2(J)=K=H=3`.

Classification: **exact finite witness**. It shows the desired inequality is sharp; it is not a counterexample.

---

## 6. New failures / rejected routes

### F1. Pure local synchronized valuation bound — disproved as a route

The all-`11` family above supplies legal unrestricted height-one blocks with `v2(J_exit)>H` for every H. Any proposed proof that ignores how the block entry was globally produced is therefore structurally incapable of proving Gate A.

### F2. Repairing RL59 by another scalar terminal potential — still frozen

RL62 already showed the corrected positive bound is the older non-decaying W-type bound. RL63 found no reason to revive that route. Neutral `11` blocks make the obstruction especially explicit: `Psi=g(J+1)/2` is constant across `11`, while the exit valuation can be made arbitrarily dangerous in the unrestricted local quotient.

No verifier or foundational inconsistency failed in RL63; these are research-route eliminations, not stop-and-repair events.

---

## 7. External/historical dependency still needed for the next theorem

The next step requires the **precise inherited full-phase macro-entry ownership predicate**, not a remembered paraphrase.

The connected GitHub repository was checked and the relevant historical archives are present, including RL47->RL48 and RL48->RL49. The connector in this session could retrieve standalone markdown but did not expose binary ZIP contents directly. Therefore RL63 deliberately did **not** invent a substitute ownership definition.

A fresh session should use the GitHub archive to recover the exact relevant source definitions/certificates before claiming the cylinder exclusion theorem. Candidate provenance to inspect first:

- `Archive/Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip`
- `Archive/Collatz_Rsharp_RL48_to_RL49_Handover_2026-08-22.zip`
- if needed, the RL43/RL44 phase-normalization provenance referenced in those bundles.

The standalone `Archive/RL47_RADIUS3_BRIDGE_AND_CLOSURE_ROADMAP.md` confirms the historical programme already viewed low-H phase data as a rank-displacement/ownership problem; it is orientation only, not a replacement for exact definitions.

---

## 8. Exact current proof ledger

### Proved analytic mathematics

- RL62 terminal-potential sign correction and factor-9 counterexample to RL59's false cap;
- inherited exact phase/defect/synchronized identities listed above, subject to their provenance;
- RL63 exact T transitions;
- RL63 exact K increments and `10` margin invariance;
- RL63 synchronized affine composition and dangerous-entry congruence;
- RL63 unrestricted all-`11` dangerous family;
- logical necessity of an entry/reachability/ownership restriction for any height-one macro proof.

### Exact finite certificates

- RL45 quotient no violation through H<=24, with two exact independent C++ encodings; both freshly replayed in RL63;
- exact RL63 equality witness `(d,H,J)=(1,3,8)`;
- finite sanity checks in `verify_rl63_even_exit_selector.py` (2,800 legal synchronized macro instances and 136 explicit all-`11` family instances). These checks support implementation audit but are not the proof of the infinite statements.

### Computational/external dependencies

- uniform `g<17/30` requires the accepted external `N>=2^71` floor plus phase squeeze;
- historical phase/ownership definitions/certificates remain inherited and must be retrieved exactly before the next cylinder-exclusion theorem is promoted.

### Conjectures/open obligations

- full-phase ownership-sensitive macro-entry cylinder exclusion;
- uniform Gate A;
- Gate B / same-root radius-3 bridge;
- RL closure and any larger Collatz conclusion.

### Demoted / forbidden for theorem use

All RL59/RL61 consequences listed in section 2 that depend on the false decreasing-height terminal potential.

---

## 9. Verifier inventory in RL63

Fast checks:

- `verification/verify_rl62_rl59_terminal_potential_sign.py`
- `verification/verify_rl63_even_exit_selector.py`

Full regression:

- `verification/verify_rl62_rl45_H24_extension_struct.cpp`
- `verification/verify_rl62_rl45_H24_extension_packed.cpp`

Expected outputs are bundled. `verification/run_fast_rl63_verifiers.sh` and `verification/run_full_rl63_verifiers.sh` automate comparisons.

---

# Self-contained kickoff for the next fresh session

Continue the Collatz R#/RL research from the authoritative **RL63 even-exit selector and ownership-target handover**.

Treat the RL63 bundle and its `.sha256` sidecar as authoritative incoming state. Verify the outer checksum and internal `SHA256SUMS.txt` first. Run the fast verifiers immediately; run the full H<=24 dual C++ regression unless resource constraints make that genuinely impractical. Any mismatch is a stop-and-repair event.

Preserve the RL62 correction: do not reuse RL59's false decreasing-height terminal potential or any RL59/RL61 tail-mass/z-floor result that depended on it. Keep fixed-survivor constants separate from uniform Gate A.

The main analytic target is now sharper than “study height-one pumping”:

> **Full-phase macro-entry cylinder exclusion.** For every genuinely reachable/owned height-one synchronized macro entry `(H,J_0)` and every legal first-even synchronized word `w`, prove that the dangerous congruence
> `3^s J_0 + C(w) == 0 (mod 2^(n+H+1))`
> cannot hold.

Proceed in this order:

1. Recover the **exact** historical ownership/full-phase macro-entry definition from the GitHub archive, beginning with RL47->RL48 / RL48->RL49 provenance. Do not reconstruct it from memory if the source is unavailable.
2. Translate that ownership predicate into arithmetic constraints on `J_0` (or `Q_0=J_0+1`), `H`, the synchronized word, zero positions, and any rank/displacement data actually present in the inherited definitions.
3. Attack the simplest genuine obstruction first: maximal all-`11` blocks. Their dangerous condition is exactly `q == 3^(-n) mod 2^(H+1)` for `J_0+1=2^n q`. Determine what full-phase reachability says about this odd `q`.
4. Then extend from all-`11` to mixed `00/11` words using the exact affine selector `C(w)` and prefix-odd cylinder constraints.
5. Use `10` margin invariance to avoid pretending that a return edge repairs a pre-existing valuation defect. Keep track of where positive valuation margin can actually be created under the full global constraints.
6. Use the H<=24 quotient certificate only as a falsification laboratory for candidate invariants; do not replace the desired uniform theorem with a larger blind scan.
7. Keep Gate B/radius-3 same-root work frozen unless Gate A progress produces a direct reusable bridge invariant. Radius-3 remains inherited/certified; the global bridge remains open.

A strong next-session result is an analytic theorem excluding the all-`11` dangerous residue class for every genuine full-phase entry, followed by a reduction of mixed words to finitely many ownership patterns. A significant result is an exact ownership-to-2-adic translation that leaves one explicit congruence lemma. A failure result should identify a genuinely reachable counterfamily and force a strategy pivot.

**Standalone session operating rule:** work as far as productive. Before finishing, freeze the exact proof state, record results/failures/dependencies/verifier status, and create the next numbered authoritative handover plus matching SHA-256 sidecar with a fresh-session kickoff. Do not silently work around verifier failures or foundational inconsistencies.

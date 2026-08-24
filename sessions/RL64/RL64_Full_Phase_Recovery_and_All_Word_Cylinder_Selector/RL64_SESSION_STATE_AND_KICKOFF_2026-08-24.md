# RL64 SESSION STATE AND KICKOFF

Date: 2026-08-24

## 0. Authority and scope

**AUTHORITATIVE OUTGOING RL64 RESEARCH STATE. Gate A remains open.**

This session continued from the authoritative incoming bundle

`RL63_Even_Exit_Selector_and_Ownership_Target_2026-08-24.zip`

with supplied sidecar

`RL63_Even_Exit_Selector_and_Ownership_Target_2026-08-24.zip.sha256`.

Incoming outer SHA-256:

`13e201b275cf614727e22d0620381a584d491433d4bbdb7a2edef77d4164ce78`.

The outer sidecar matched exactly; every entry in the incoming internal `SHA256SUMS.txt` verified; `verification/run_fast_rl63_verifiers.sh` passed; and `verification/run_full_rl63_verifiers.sh` passed at session start, including both independent H<=24 C++ implementations. No incoming integrity, verifier, foundational-definition, or authoritative-provenance failure occurred.

The connected GitHub repository was used only as the supporting historical archive, as instructed. RL63 remained the authoritative incoming mathematical state.

No result in RL64 proves Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

---

## 1. Exact inherited proof state retained

### Proved/inherited analytic mathematics retained

Subject to the provenance frozen in RL63/RL62:

- RL62 correction of the false RL59 terminal-potential sign;
- exact RL45 quotient
  - `J=T+3^d-2^d`,
  - `K=H+d(d+1)/2-1`,
  - start `(d,H,J)=(1,0,-13)`,
  - terminal `d=1` target `v2(J)<=H`;
- exact RL63 T maps, K increments, and legal nonzero-`10` invariance of `v2(J)-K`;
- RL63 synchronized affine selector
  - `2^n J_n=3^s J_0+C(w)`,
  - dangerous cylinder `3^sJ_0+C(w)==0 mod 2^(n+H+1)`;
- RL63 unrestricted all-`11` dangerous family;
- inherited exact phase/word/zero-position/rank-displacement identities with their original provenance, including `H=sum delta_j` where that historical notation applies;
- safe continued-fraction/phase-squeeze facts not depending on the false RL59 potential.

### Exact finite certificates retained

The H<=24 RL45 quotient certificate remains an exact finite result only:

- reachable states: `8,664,154`;
- maximum `d=8`;
- maximum `|J|=110,392,611,511,170`;
- maximum positive-state margin `v2(J)-K=-3`;
- no violation;
- two independent C++ implementations.

It is **not** a uniform Gate-A proof.

### Demotions/forbidden routes retained

Do not revive:

- RL59 `Jg <= zeta*3^(4-d)/2` for `d>1`;
- any Type-B/maximal-pump neutralization based on that false cap;
- generic terminal bounding from that potential;
- post-final-`10` mass bounds and forced z-floors derived from it;
- RL61 `T.pot`, RL61 `T.K25-39` derived z-floors, or the inherited `K<=129` reduction where they rely on that false premise;
- fixed-safe-CF survivor constants such as `E<5/3` or `Zx>143/12` as if they were uniform Gate-A facts;
- any claim that H<=24 computation closes the uniform theorem.

---

## 2. Historical source recovery completed in RL64

RL63's main provenance obligation was to recover the exact historical full-phase/macro-entry source rather than reconstruct it from memory. RL64 materially repairs that obligation.

GitHub repository:

`jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`

Exact historical archives inspected:

- `Archive/Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip`
  - archived sidecar: `fa164c65c0910fc25ee5724328b2ea15914204049f15e0a00b2781a8ffc979e9`;
- `Archive/Collatz_Rsharp_RL48_to_RL49_Handover_2026-08-22.zip`
  - archived sidecar: `053548eb5f09566d7772389322e3b59a66531ea3a5c5b98aad3ed51d5baa2572`.

Two exact historical internal files are frozen in RL64:

1. `historical/RL47_verify_rl47_phase_coordinate.py`;
2. `historical/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`.

The recovered source bytes were decoded from the GitHub archived ZIP representations and checked against their ZIP local-entry metadata/CRC during recovery. The connector did not provide a raw historical ZIP mounted in the sandbox, so the **historical outer ZIP hashes were not independently recomputed locally**. This is recorded as a supporting-archive provenance limitation, not as a failure of the checksum-clean authoritative incoming RL63 state.

### Exact historical phase definition recovered

RL47 defines

`Phi(d,T,i,p)=2^i(T+3^d-1)/3^(p+d)`

and verifies the edge telescope

`Delta Phi=(2^i/3^p)*((1-x)-(1-y)/3^d)`.

At `d=1`, using `J=T+1`,

`Phi=2^i(J+1)/3^(p+1)`.

Every `11` edge has exactly `Delta Phi=0`.

### Exact historical full-word/terminal geometry recovered

RL48 gives

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`

under the RL45/RL47 conventions; the internal pair path starts after the mandatory `(0,1)` and ends before the omitted terminal `(1,0)`. It proves the exact full-phase/four-swap construction and identifies the internal coordinate as

`T_i=3^(d_i)A_i-B_i`.

The internal start is `T=-14`; terminal is

`T=2^(t+3)-1`.

Thus, at terminal `d=1`,

`J_terminal=T+1=2^(t+3)`.

### Terminology repair: “ownership”

The exact RL47 phase verifier and RL48 full-phase bridge recovered here do **not** define a separately named Boolean “ownership predicate”. RL63's word “ownership” is best treated as shorthand for **global full-phase extendability**: a local quotient state/prefix must arise inside and be completable to the exact historical full-word geometry.

RL64 therefore does not invent or backdate a named predicate. Future work should either:

- write the existential full-phase completion requirements explicitly; or
- introduce a new definition such as “full-phase extendable prefix”, clearly labelled as a new definition derived from the exact historical sources.

This clarification prevents a remembered paraphrase from silently becoming an inherited theorem.

RL64 therefore introduces, explicitly as a **new definition**, `RL64_FULL_PHASE_EXTENDABLE_PREFIX_DEFINITION.md`. It spells out the existential completion data `(a,ell,t,x,y)`, exact internal RL recurrence/parity legality, canonical terminal `J=2^(t+3)`, and exact RL48 full-phase divisibility `M | V+4Y`. A “full-phase extendable macro state” means a quotient state lying on a prefix of at least one such full completion.

Detailed provenance is in `RL64_HISTORICAL_FULL_PHASE_RECOVERY_NOTES.md`.

---

## 3. Genuinely new RL64 analytic results

Full proofs are in `RL64_ALL_WORD_CYLINDER_AND_PHASE_SELECTOR_THEOREM.md`.

### 3.1 New synchronized-zero defect identity

For `w=(x_0,...,x_(n-1))`, `x=0` for `00`, `x=1` for `11`, define

`s=sum x_r`,

`D(w)=sum_{r:x_r=0} 2^r 3^(sum_{q>r}x_q)`.

This is new local RL64 notation and is not inherited `E=Zx-Zy`.

Then

`boxed: 2^n(J_n+1)=3^s(J_0+1)+2D(w)`

and

`boxed: C(w)=3^s+2D(w)-2^n`.

Classification: **analytic theorem**.

### 3.2 Every synchronized word has exactly one legal first-even cylinder

For every `w in {00,11}^n`, the congruence

`3^sJ_0+C(w)==0 mod 2^(n+1)`

has one odd residue class, and it is exactly the class for which all prior states are odd and `J_n` is the first even state. As the `2^n` words vary, these are all odd classes modulo `2^(n+1)`.

Classification: **analytic theorem**.

### 3.3 RL63's local obstruction extends to every mixed word

For every word `w` and every `H>=0`, the dangerous condition

`v2(J_n)>H`

selects exactly one lift modulo `2^(n+H+1)`. That lift reduces to the legal first-even cylinder. Hence **every synchronized word**, not just all-`11`, contains infinitely many positive legal unrestricted local entries with dangerous exit.

Stronger: every word-cylinder contains infinitely many positive entries with exact exit valuation `L` for every `L>=1`. Thus local valuation excess is unbounded in every synchronized word-cylinder.

Classification: **analytic theorem**.

Consequence: a mixed-word local valuation argument cannot rescue Gate A. The missing theorem must exclude specific globally full-phase-extendable macro entries.

### 3.4 Exact historical phase-selector congruence

At a genuine historical `d=1` macro entry define the integer phase numerator

`P=3^(p+1)Phi=2^i(J_0+1)`.

For a synchronized word `w` of length `n`, weight `s`, the dangerous condition is exactly

`boxed: 3^sP + 2^(i+1)D(w) == 2^(i+n) mod 2^(i+n+H+1)`.

For maximal all-`11`, this specializes in the 2-adic localization to

`Phi/2^(i+n) == 3^(-(p+n+1)) mod 2^(H+1)`.

Classification: **analytic theorem/translation from exact recovered historical Phi**. It identifies the prohibited class but does not yet prove exclusion.

### 3.5 Terminal ownership collapses the unrestricted selector

If a synchronized block is the final historical height-one block, write `k=t+3`. Exact RL48 terminal geometry gives `J_n=2^k`. Therefore the macro entry must satisfy the **equality**

`boxed: 3^sJ_0+C(w)=2^(n+k)`

or equivalently

`boxed: 3^s(J_0+1)+2D(w)=2^n(2^k+1)`.

For a mixed word this gives the exact 3-adic compatibility condition

`D(w) == 2^(n-1)(2^k+1) mod 3^s`

when `s>=1`.

Classification: **analytic theorem**.

### 3.6 All-`11` terminal suffix theorem

For a terminal all-`11` suffix of positive length `n`, if `J_0+1=2^nq`, then exact terminal ownership forces

`boxed: 3^nq=2^k+1`.

So the unrestricted RL63 freedom to choose arbitrary odd

`q == 3^(-n) mod 2^(H+1)`

is gone: `q=(2^k+1)/3^n` is fixed by `(k,n)`.

For `n>=1`, `k` must be odd. By LTE,

`v3(2^k+1)=1+v3(k)` for odd `k`,

hence

`boxed: n<=1+v3(k)`.

If `k` is even, no positive-length terminal all-`11` suffix exists.

Classification: **analytic theorem**.

This is a real ownership-sensitive advance, but it still does not imply `H>=k`.

---

## 4. New exact finite verifier evidence

`verification/verify_rl64_all_word_cylinders.py` independently checks the new formulas over bounded ranges with exact integer/Fraction arithmetic.

Fresh output:

- word identity/legal-cylinder checks: `1022`;
- dangerous-lift checks: `7154`;
- exact-valuation lift checks: `5110`;
- historical phase-numerator congruence checks: `42924`;
- terminal ownership/backward checks: `3810`;
- all-`11` terminal/LTE checks: `137`;
- status: `RL64 all-word cylinder verifier: PASS`.

This is an **exact finite audit**, not the proof of the infinite statements.

The recovered historical RL47 verifier also reruns and prints `RL47 phase-coordinate verifier: PASS`.

---

## 5. Failed/rejected approaches and why

### F1. Treating all-`11` as the only local obstruction

Rejected. RL64 proves every synchronized word has an unrestricted dangerous lift and unbounded exact exit valuation. Mixed synchronized words are not locally safer in the sense needed by Gate A.

### F2. Defining “ownership” from memory

Rejected. Exact historical source recovery found full-phase coordinate/word extendability data, but no separately named Boolean ownership predicate in the recovered RL47/RL48 sources. RL64 records the exact source instead of inventing a predicate.

### F3. Using only the 2-adic selector after terminal ownership is imposed

Insufficient. For a terminal block the 2-adic selector must also satisfy an exact equality/3-adic compatibility condition. Any future mixed-word proof that studies only the RL63 modulus and ignores terminal/full-word completion is structurally incomplete.

### F4. Scalar terminal-potential revival

Not attempted/revived. The RL62 sign correction remains decisive. RL64's new theorems do not depend on the false RL59 route.

### F5. Final full H<=24 rerun during close-out

The full RL64 runner was attempted after the new work. It printed `FAST_RL64_VERIFIERS PASS` and `FAST_RL63_VERIFIERS PASS`, then the command window timed out while the inherited H<=24 C++ regression was executing. Therefore no **new close-out full-suite PASS** is claimed. The same checksum-clean inherited full RL63 suite, including both C++ H<=24 implementations, had already completed successfully at the beginning of this session. The final fresh-unpack procedure reruns the fast RL64 suite and integrity checks.

---

## 6. Verifier inventory and final status

### Incoming RL63 verification at session start

From the checksum-clean incoming bundle:

- `sha256sum -c SHA256SUMS.txt` — **PASS**;
- `bash verification/run_fast_rl63_verifiers.sh` — **PASS**;
- `bash verification/run_full_rl63_verifiers.sh` — **PASS**.

The full run included:

- `verify_rl62_rl45_H24_extension_struct.cpp` — output matched;
- `verify_rl62_rl45_H24_extension_packed.cpp` — output matched.

### RL64 verification

- `python3 verification/verify_rl64_all_word_cylinders.py` — **PASS**;
- `python3 historical/RL47_verify_rl47_phase_coordinate.py` — **PASS**;
- `bash verification/run_fast_rl64_verifiers.sh` — **PASS**;
- `bash verification/run_full_rl64_verifiers.sh` — **attempted but close-out invocation timed out during inherited H<=24 regression; do not mark as final PASS**.

Exact run outputs/attempt note are bundled under `verification/`.

---

## 7. Exact main unresolved mathematical obstruction

Gate A remains:

`H>=k=t+3`

at the canonical terminal state `J=2^k`, equivalently terminal `v2(J)<=H`.

RL64 narrows the dangerous terminal suffix problem as follows:

- unrestricted local 2-adic danger exists in every synchronized word;
- genuine terminal ownership replaces the free local entry by the exact equality
  `3^s(J_0+1)+2D=2^n(2^k+1)`;
- all-`11` suffixes satisfy `n<=1+v3(k)` and have fixed `q`;
- mixed suffixes satisfy an exact `3^s` divisibility condition through `D(w)`;
- historical phase at the macro entry is exactly `P=2^i(J_0+1)` and has the recovered edge telescope;
- inherited rank transport supplies `H=sum delta_j` in its proper provenance.

The missing theorem is now an **ownership-sensitive area/terminal theorem**: prove that a globally completable internal pair word satisfying the exact full-phase/terminal conventions cannot have `k>H`.

The challenge is no longer to identify the dangerous local cylinders. It is to show that the exact global word/rank/phase constraints cannot land in the terminal-owned equality classes when the accumulated area is too small.

---

## 8. Recommended next attack

1. **Audit and use the new RL64 “full-phase extendable prefix” definition** in `RL64_FULL_PHASE_EXTENDABLE_PREFIX_DEFINITION.md`; do not silently add hypotheses. If an older exact source supplies extra rank/zero-position conditions, record them separately with provenance.
2. **Attack the terminal all-`11` suffix first.** Substitute
   `q=(2^k+1)/3^n` and `n<=1+v3(k)` into the exact historical phase/rank-displacement identities. The goal is an analytic contradiction to `H<k`, not another local congruence.
3. Use the exact RL47 phase telescope. Since `11` contributes zero to `Delta Phi`, the entire final all-`11` suffix freezes `Phi`; all information must therefore come from the last non-`11` event and the earlier height excursion. Isolate that last event and express the entry phase numerator `P` in terms of the preceding `10`/`00`/`01` geometry.
4. **Then handle mixed terminal synchronized words** using
   `D(w) == 2^(n-1)(2^k+1) mod 3^s` together with the same phase/rank data. Work backward from `J=2^k`; inverse `00` is `J_prev=2J-1`, while inverse `11` is `(2J-1)/3` and requires `J==2 mod3`. This gives an exact 3-adic backward automaton for candidate terminal suffixes.
5. Connect the suffix data to `H=sum delta_j` rather than to a scalar terminal potential. A promising target is a lemma bounding terminal `k` by total rank displacement once the terminal suffix has been reduced by the new 3-adic constraints.
6. Use the H<=24 certificate only to falsify candidate invariants and inspect equality/near-equality patterns. Do not extend blind finite scanning as a substitute for the uniform theorem.
7. Keep Gate B frozen unless Gate A is actually repaired or a direct reusable invariant emerges. Do not infer any global closure from the recovered RL48 four-swap source without re-auditing the exact radius-3 dependency chain.

A strong next-session result would prove `H>=k` for the terminal all-`11` suffix class and reduce mixed suffixes to a precise analytic lemma. A significant partial result would derive a rigorous lower bound on `H` from the terminal 3-adic/phase conditions that grows with `k`.

---


## 9. Final archival close-out

The standard standalone-session closure procedure was completed after the mathematical work was frozen.

- `RL64_SESSION_STATE_AND_KICKOFF_2026-08-24.md` at repository/root level is byte-identical to the copy inside the handover directory/ZIP.
- A final pre-packaging run of `bash verification/run_fast_rl64_verifiers.sh` passed.
- The inherited RL63 outer sidecar was rechecked inside `inherited/` and passed.
- `SHA256SUMS.txt` was generated over every bundled file other than the manifest itself, using paths relative to the RL64 handover root, and `sha256sum -c SHA256SUMS.txt` passed before packaging.
- The authoritative ZIP was created as `RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip`, and its matching `.sha256` sidecar was independently checked with `sha256sum -c`.
- The finished ZIP was unpacked into a fresh directory; the internal manifest passed there and `bash verification/run_fast_rl64_verifiers.sh` passed there.

The expensive full RL64 runner was **not rerun to completion during final packaging**. Earlier in this same session the checksum-clean inherited RL63 full suite, including both independent H<=24 C++ implementations, passed completely. A later RL64 full close-out attempt passed the RL64 fast suite and inherited RL63 fast suite, then exceeded the command window while rerunning that inherited H<=24 regression. Because the full regression had already passed from the verified incoming state and final packaging required a clean fresh-unpack integrity/fast verification, the packaging close-out records the full suite as **not freshly completed at final archive time**, not as a failure.

With those qualifications, the ZIP, sidecar, and this session-state file are the authoritative RL64 handover outputs. No mathematical claim is upgraded by the packaging process.

---

# Self-contained kickoff prompt for RL65

Continue the Collatz R♯ / RL research from the authoritative RL64 handover bundle and matching `.sha256` sidecar. Treat `RL64_SESSION_STATE_AND_KICKOFF_2026-08-24.md` as the searchable proof-state ledger, but verify the outer ZIP sidecar, internal `SHA256SUMS.txt`, and bundled fast verifiers before using the mathematics. Any checksum, verifier, foundational-definition, or provenance failure is a stop-and-repair event.

Preserve every RL62/RL63 demotion. In particular, do not revive RL59's false decreasing-height terminal potential; do not move fixed-survivor constants into uniform Gate A; do not treat H<=24 as a uniform theorem; and do not claim Gate A, Gate B, RL, nontrivial cycles, or Collatz closed without a complete audited proof.

RL64 recovered exact historical source material from GitHub and froze it inside the bundle:

- `historical/RL47_verify_rl47_phase_coordinate.py`, defining
  `Phi=2^i(T+3^d-1)/3^(p+d)` and its exact edge telescope;
- `historical/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`, fixing the full words
  `u=110x10^t`, `v=111y0^(t+1)`, internal start `T=-14`, and terminal `T=2^(t+3)-1`.

Do not invent a historical named “ownership predicate”. The exact recovered sources do not define one under that name. RL64 already introduces **as a new definition** `RL64_FULL_PHASE_EXTENDABLE_PREFIX_DEFINITION.md`; audit and use that explicit existential completion definition rather than a remembered paraphrase.

The new RL64 analytic facts to use are:

1. for every synchronized word `w`,
   `2^n(J_n+1)=3^s(J_0+1)+2D(w)`;
2. every synchronized word has exactly one legal first-even cylinder and one dangerous lift for every `H`; local excess is unbounded for every word, so purely local height-one arguments cannot prove Gate A;
3. at historical `d=1`, `P=3^(p+1)Phi=2^i(J_0+1)`, and the dangerous selector is
   `3^sP+2^(i+1)D == 2^(i+n) mod 2^(i+n+H+1)`;
4. for a **terminal-owned** synchronized block, `J_n=2^k`, `k=t+3`, so
   `3^s(J_0+1)+2D=2^n(2^k+1)`;
5. for a terminal all-`11` suffix,
   `3^n q=2^k+1`, hence `k` is odd and `n<=1+v3(k)`;
6. mixed terminal suffixes satisfy
   `D(w)==2^(n-1)(2^k+1) mod3^s`.

Main target: prove the ownership-sensitive terminal area inequality `H>=k`.

Attack order:

- audit/use the bundled exact-source-derived full-phase extendability definition;
- isolate the terminal all-`11` suffix class and combine its fixed `q`, short 3-adic length, exact Phi telescope, and inherited `H=sum delta_j` rank-displacement identity to attack `H<k`;
- identify the last non-`11` event before that suffix and express the frozen suffix Phi through that event;
- then extend to mixed terminal suffixes using the exact `D(w)` 3-adic compatibility and backward inverse automaton;
- use finite H<=24 data only as a falsification laboratory.

The next session is standalone. Before ending, freeze all new proofs, failures, demotions, dependencies, verifier status, and the next exact obstruction into RL65; create the authoritative RL65 ZIP, matching `.sha256`, and root/inside-ZIP `RL65_SESSION_STATE_AND_KICKOFF_<actual-date>.md`; generate and verify an internal checksum manifest; and rerun fresh-unpack fast integrity/verifier checks. Report any full verifier not rerun and why.

**Known-invalid routes future agents must not revive:** RL59 terminal-potential cap and its descendants; unrestricted local synchronized valuation bounds; treating all-`11` as the only local dangerous word; treating “ownership” as a remembered unnamed theorem; using finite H<=24 as closure; importing fixed-survivor constants into the uniform problem.

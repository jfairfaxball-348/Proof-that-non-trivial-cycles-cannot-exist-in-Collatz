# RL218 certified facts and proof ledger — recovered closeout

Date: 2026-09-01.

## Closeout correction

The earlier RL218 interruption closeout was based on a transport premise that is no longer true. The exact Codex scratch archive is present in GitHub as blob `bf6b9bd06442bfaec51cb6ef786af4858c916806` (606,019 bytes) and has been reviewed sufficiently to recover its checkpoint, proof-quality backward-word algebra, verifier outcomes, and incomplete-work boundaries.

This is a **mechanical/provenance correction to the closeout record**, not a demotion of inherited mathematics.

## Promoted RL218 analytic results

RL218 promotes the following analytic mathematics, with no change to the global H21 rank frontier.

1. **Legal backward-word normal form.** For shortcut Collatz
   `T(n)=n/2` for even `n` and `T(n)=(3n+1)/2` for odd `n`, backward moves are
   `D(Y)=2Y` and `O(Y)=(2Y-1)/3`. For a raw word `w` of length `n` with `h`
   odd-inverse letters,
   `W(s)=(2^n s-C_w)/3^h`, where
   `C_w=sum_{i:w_i=O} 2^(n-i) 3^h_(i-1)`.
   For positive integral seed `s`, the entire raw word is legal iff the single terminal congruence
   `3^h | (2^n s-C_w)` holds.

2. **Odd-only exponent form.** Writing a word as
   `D^(e1-1)O ... D^(eh-1)O D^t`, with
   `Q_0=0`, `Q_j=2^e_j Q_(j-1)+3^(j-1)`,
   the j-th odd inverse is
   `x_j=(2^E_j s-Q_j)/3^j`, and legality is equivalent to
   `3^h | (2^E_h s-Q_h)`.
   For odd output `y` and odd seed `s`, the canonical exact branch test is
   `E=v2(3^h y+Q_h)` together with `s=(3^h y+Q_h)/2^E`.

3. **RL217 lattice pullback.** Substituting each prefix root
   `y(k)=y_*+3*2^58 k` gives
   `N(k)=A+3^(h+1) 2^58 k`, `A=3^h y_*+Q_h`.
   If `v2(A)<58`, the valuation is constant over all k. If `v2(A)>=58`, then for
   `E=58+d` exact valuation is one congruence class
   `k=kappa_d (mod 2^(d+1))`.
   Intersecting this with an RL217 phase-51 cylinder is an exact modular operation.

4. **Fixed-certified-seed singleton barrier.** For one fixed odd certified-blue seed `s`
   and one fixed legal word, exact equality with the RL217 root lattice gives at most one
   `k`: `k=(2^E s-A)/(3^(h+1)2^58)`. Therefore a finite fixed-seed/fixed-word
   pullback is only a finite union of exact singletons. A non-singleton k-class can be
   certified blue only if an independent theorem/certificate proves a corresponding
   endpoint progression blue. This closes the tempting but invalid “branch legality implies
   blue membership” shortcut.

## Exact bounded negative results recovered from the scratch

These are exact finite negative screens and are preserved as non-deleting certified research results.

- **RL80 LTE comb screen:** every one of **45,046** reconstructed inherited prefix bases
  fails the necessary congruence for the explicit RL80 analytic blue comb. Scratch verifier
  reported PASS with prefix-row digest
  `24a57291eaf8685ff84f8e2ebe02b751a5597b84a86d4d9140d2f3bfb7b4dd90`
  and `(Q,j,screen-residue)` digest
  `bca5aecb93b3b4c1d9c64e42fac6b37452b64409d401008d202d2559710b57e2`.
  This closes that explicit comb as a source of RL217 candidate membership; it deletes no
  RL217 candidate.

- **Seed-1 reverse tree:** exact legal reverse-tree search through depths **0..86** against
  all **45,045** live RL217 lattices reported **43,370** relevant odd in-range endpoints and
  **zero** lattice matches. It deletes no candidate and says nothing about depths >86.

## Explicitly not promoted

- The interrupted certified-interval / forward-floor automaton did not complete its intended
  horizon and is **NOT PROMOTED**.
- The 40,003-candidate forward-floor sample is computational evidence only.
- No backward depth >86 is covered by the bounded certificate.
- No residue match, valuation class, density statement, proximity statement, or legal
  backward branch is promoted as certified-blue membership without exact equality to a
  certified-blue endpoint/set.

## Inherited frontier unchanged

- necessary terminal ranks: **13,415,865,871**;
- above p: **7,091,831,284**;
- below p: **6,324,034,587**;
- e=16 phase-51 survivors: **139,581,280** across **45,045** live prefixes;
- phase-51 selector: **3,132,617** disjoint 2-adic cylinders, max precision **25 bits**;
- e=16 terminal rank **34,124,151,203** remains live;
- both states, all four mod18 classes, and all **469** reachable eta classes remain live.

Gate A remains open globally. Gate B remains open globally. Global nontrivial-cycle exclusion remains open.

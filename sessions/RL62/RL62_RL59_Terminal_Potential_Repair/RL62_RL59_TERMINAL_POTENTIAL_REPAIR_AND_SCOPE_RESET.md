# RL62 — RL59 terminal-potential repair and Gate-A scope reset

Date: 2026-08-24

## Status

**STOP-AND-REPAIR RESULT.**

The RL59→RL60 handover is checksum-clean, but the central RL59 positive terminal-potential inequality has a height-sign error. The error is independently exposed by an exact inherited RL47 structural witness and by the concrete RL59 Type-B exit arithmetic. Consequently, all later conclusions that logically use that terminal potential or the derived final-tail mass lower bound must be demoted pending a replacement proof.

This repair does **not** invalidate the older exact full-phase identities, the RL45 terminal-valuation reduction, the raw shortcut-terminal ancestor searches, or the safe phase/continued-fraction calculations that do not use the false terminal potential.

Gate A remains open.

---

## 1. Bundle integrity and verifier status

The outer `Collatz_Rsharp_RL59_to_RL60_Terminal_Tail_Bootstrap_Handover_2026-08-23.zip` SHA-256 matches its sidecar. Every entry in the internal `SHA256SUMS_RL59_TO_RL60.txt` manifest verifies.

The bundled verifier suite was rerun. The analytic/arithmetic checks and the exact K25/K27 boundaries reproduced. The long K29 live search exceeded the session execution cap; its bundled output remains checksum-verified. This distinction matters because verifier success only confirms the encoded calculation, not the truth of an incorrectly derived premise.

---

## 2. Exact height convention and the sign error

The inherited RL47/RL48 convention is

\[
d=1+p_y-p_x,
\qquad g=\frac{2^i}{3^{p_x}}.
\]

At an internal state with current x-one count `p=p_x`, the current y-one count is

\[
p_y=p+d-1.
\]

Both internal words have total one count `ell-3`. Hence the remaining one counts are

\[
X_{\rm rem}=\ell-3-p,
\]

and

\[
Y_{\rm rem}=\ell-3-(p+d-1)
           =\ell-p-d-2
           =X_{\rm rem}-(d-1).
\]

Thus a suffix returning from height `d` to height 1 contains exactly `d-1` **more future x-ones than future y-ones**.

RL59 Section 1 states

\[
J\le \zeta\frac{3^{p-d+4}}{2^{i+1}},
\qquad
Jg\le \zeta\frac{3^{4-d}}2.
\]

That exponent is obtained only if the future one-count relation is taken with the opposite sign. With the inherited height convention, the dropped-affine normalized-P calculation instead gives

\[
\boxed{
J\le \zeta\frac{3^{p+d+2}}{2^{i+1}}
}
\]

or equivalently

\[
\boxed{
Jg\le \zeta\frac{3^{d+2}}2
     =\frac92\zeta\,3^d.
}
\]

At height one the old and corrected formulas coincide. At height two the corrected cap is larger by a factor of 9. More generally their ratio is `3^(2d-2)`.

The corrected inequality is exactly the older monotone-W terminal estimate; therefore RL59 did not obtain a new decaying-in-height terminal potential.

---

## 3. Exact inherited counterexample to the RL59 potential

Use the exact audited RL47 structural witness with

\[
(a,\ell,t)=(65,41,2).
\]

Its inherited edge word is replayed by `verify_rl62_rl59_terminal_potential_sign.py` using the exact RL45/RL47 `J` recurrences. Immediately before the final internal `10` descent the state is

\[
(i,p,d,J)=(58,37,2,64).
\]

Therefore

\[
g=\frac{2^{58}}{3^{37}},
\qquad
Jg=\frac{2^{64}}{3^{37}}.
\]

Since

\[
\zeta=\frac{2^{65}}{3^{41}},
\]

RL59's height-two claim gives

\[
\frac92\zeta
=\frac{2^{64}}{9\,3^{37}},
\]

whereas the exact witness has

\[
Jg=9\left(\frac92\zeta\right).
\]

The corrected bound gives

\[
\frac{81}{2}\zeta
=\frac{2^{64}}{3^{37}}
=Jg,
\]

so it is attained with equality on this witness.

This witness is a structural full-phase-grammar witness rather than a claimed owned cycle. That is sufficient to refute the RL59 derivation because ownership is not used in the asserted terminal-grammar inequality.

---

## 4. Concrete RL59 Type-B obstruction fails after the correction

The bundled RL59 Type-B verifier uses the exit state

\[
(i,p_x,d,J)=(84,53,2,15)
\]

with five late x-zero events, so

\[
P_{\rm exit}=2^5\cdot15=480.
\]

At height two,

\[
p_y=p_x+d-1=54.
\]

Hence the true future one counts are

\[
X_{\rm rem}=\ell-56,
\qquad
Y_{\rm rem}=\ell-57.
\]

The RL59 verifier instead comments and uses `y-ones = ELL-55`, reversing the height imbalance by two one-events.

With the safe rational upper bound `zeta < 136/135`, RL59's old cap is

\[
\frac{136}{135}\frac{3^{55}}{2^{80}}
\approx145.3699016<480,
\]

which appeared to exclude the Type-B exit.

The corrected cap is

\[
\frac{136}{135}\frac{3^{57}}{2^{80}}
\approx1308.329114>480.
\]

Therefore the claimed Type-B contradiction does not follow.

---

## 5. Proof-state impact

### Still valid / not affected by this repair

1. Exact RL47/RL48 phase-word normalization and one-excursion identities.
2. Exact defect identity and zero-position telescoping, including `E=Zx-Zy` in the inherited normalization.
3. Exact synchronized height-one telescope `Psi=g(J+1)/2`, with `00` adding `g` and `11` adding zero.
4. Exact shortcut-Collatz conjugacy of the synchronized height-one subsystem.
5. Raw terminal-ancestor searches `N(K)` as standalone finite facts about the shortcut map, subject to their ordinary finite-verifier provenance.
6. The pre-RL59 fixed-survivor prefix certificates, provided their own inherited dependencies are retained.
7. The RL45 exact `(d,H,J)` Markov quotient and its reduction of uniform Gate A to the terminal valuation statement.
8. The phase squeeze / safe continued-fraction calculations that do not invoke the RL59 terminal potential.

### Must be demoted pending replacement proof

1. RL59's positive terminal potential `Jg <= zeta*3^(4-d)/2` for `d>1`.
2. The Type-B maximal-pump neutralization that uses the height-two cap.
3. The claim that every nonterminal positive synchronized pump block is terminally bounded by that potential.
4. The post-final-`10` estimate `J0*g0 <= (3/2)zeta` derived from the false height-two potential.
5. The final-tail lower bounds `M_final>45/8` and `M_final>23/4` insofar as their proofs use that estimate.
6. Consequences derived from those mass bounds: forced counts/runs in the terminal synchronized tail and the conversion from raw `N(K)` thresholds to enormous `z` floors.
7. RL61's `T.pot` ledger entry as an analytic fixed-survivor theorem.
8. RL61's `T.K25-39` **derived z-floor column**. The raw `N(K)` values themselves remain finite shortcut-map certificates.
9. RL61's external `K<=129` fixed-survivor reduction as currently proved, because RL61 explicitly derives its admissible start bound from the terminal mass bound. The external path-record table is not thereby invalidated; the interface theorem feeding it is.

This is a correction to the RL61 whole-tree audit ledger: the audit replayed arithmetic downstream of an inherited false analytic premise and therefore did not catch the sign error.

---

## 6. Universal versus fixed-survivor late constants

The RL59 bundle was requested in order to determine which late-tail estimates could be safely transplanted into the new RL62 uniform Gate-A macroblock attack.

### Structural / uniform within the full-phase hypotheses

- The exact defect / zero-position identities.
- The synchronized-block telescopes.
- The exact prefix x-zero cap
  \[
  g\le\frac9{16}\zeta^2.
  \]
- Conditional on the accepted external computational floor `N>=2^71` together with the analytic phase squeeze, the phase estimate gives `zeta^2<136/135`, hence the **uniform sequential cap**
  \[
  \boxed{g<17/30}.
  \]
  This is not tied to the one safe-CF convergent; its numerical use is conditional on the external `2^71` floor.

### Fixed safe-CF survivor only

- `E<5/3` in the late RL50–RL59 survivor attack.
- The strengthened `Zx>143/12` that uses that `E<5/3` bound in the exact phase identity.
- The large finite terminal-tail bootstrap numbers that depend on the particular convergent and, after RL59, on the false terminal mass estimate.

Thus the RL62 coupled macroblock program may retain the structural identities and the `17/30` per-zero cap (with its external-floor provenance), but it must not import `E<5/3`, `Zx>143/12`, or RL59's terminal-mass forcing as uniform Gate-A statements.

---

## 7. Return to the clean Gate-A core: RL45 terminal valuation

RL45 defines

\[
J=T+3^d-2^d,
\qquad
K=H+\frac{d(d+1)}2-1.
\]

The exact Markov quotient starts at

\[
(d,H,J)=(1,0,-13)
\]

and obeys the parity-determined transitions

- if `J` is odd:
  - `00`: `J'=(J+3^d-2^d)/2`, `d'=d`;
  - `11`: `J'=(3J+2^d-1)/2`, `d'=d`;
- if `J` is even:
  - `01`: `J'=(3J+3^(d+1)-2^d-1)/2`, `d'=d+1`;
  - `10`: `J'=J/2`, `d'=d-1` for `d>1`;
- every internal step updates
  \[
  H'=H+d-1.
  \]

The uniform valuation candidate is

\[
\boxed{J>0\Longrightarrow v_2(J)\le K.}
\]

At terminal height one, `K=H`, so this is exactly the desired Gate-A valuation inequality.

RL45 certified this through `H<=23`.

### Fresh RL62 H=24 extension

Two independently implemented exact C++ state encodings reproduce every bundled RL45 state count through `H=23` and both extend the certificate to `H=24`.

At `H=24`:

- exact reachable state count: **8,664,154**;
- maximum height: `d=8`;
- maximum absolute `J`: `110,392,611,511,170`;
- maximum positive violation margin `v2(J)-K`: **-3**;
- therefore no positive valuation violation occurs.

Status: **fresh exact finite certificate**, independently cross-implemented in this session; still not a uniform analytic proof.

---

## 8. Revised research direction

The RL59 terminal-tail route should be frozen rather than repaired by another scalar bound: the corrected positive bound is exactly the older `W` bound and loses the hoped-for decay with height.

The Rank-1 strategy should instead combine two clean ingredients:

1. **RL62 coupled full-phase macroblocks / ownership.** A hypothetical Gate-A violation has bounded non-height-one skeleton and exact phase/zero-position/ownership constraints.
2. **RL45 valuation quotient.** Gate A is reduced to excluding `v2(J)>K`, with all difficult behavior concentrated in zero-area height-one synchronized macros and their even exits.

The next analytic target is therefore not a generic terminal-mass estimate. It is:

> **Ownership-sensitive even-exit lemma.** Show that a height-one synchronized macro whose even exit would create `v2(J)>H` cannot simultaneously satisfy the full-phase prefix/zero-position/ownership constraints.

The safe-CF survivor remains useful as a stress-test instance, not as the main closure target.

---

## 9. Verifiers in this repair bundle

- `verify_rl62_rl59_terminal_potential_sign.py`
  - checks the exact remaining-one count identity;
  - replays the RL47 structural witness;
  - proves the factor-9 failure at height two;
  - checks the corrected Type-B cap.
- `verify_rl62_rl45_H24_extension_struct.cpp`
  - exact RL45 quotient exploration through `H=24` using an explicit state structure.
- `verify_rl62_rl45_H24_extension_packed.cpp`
  - independent packed-key implementation of the same finite certificate.
- corresponding `.out` files preserve the exact run results.

## 10. Bottom line

There is **no Gate-A closure** in this pass. Instead, this pass prevents the project from building further on a false terminal lemma, restores the correct proof ledger, identifies which late constants are actually portable to the uniform attack, and extends the clean RL45 valuation certificate by one exact level.

The central open statement remains uniform Gate A.

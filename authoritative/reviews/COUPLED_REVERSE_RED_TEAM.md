Review provenance note: source paths and SHA256 values below identify the reviewed
unsealed source copies. The final portable proof/verifier paths are under proofs/ and
verification/; their final bytes are authenticated by the package manifest and fresh suite.

# RL201 independent red team — coupled reverse strips

Date: 2026-08-31. Frozen RL201 component.
Reviewer: independent p-chain/moment subagent. Review performed during the
parent's `CLOSEOUT_LOCK`; no new mathematical route or scan was started.

Reviewed artifacts:

- `.rl-work/RL201/coupled_reverse/PROOF.md`
- `.rl-work/RL201/coupled_reverse/verify_coupled_reverse.py`

Verdict: **PASS for the stated local coupled-strip mathematics**, after the
verification-only canonical-anchor clarification identified below. No
inherited or candidate analytic theorem was found false, and no range or
proof-state demotion is indicated.

Final reviewed SHA256:

- `PROOF.md`: `389468224fa5da3e4a531b61310b73daf7da0115514e95fab54eee613c2bf09e`
- `verify_coupled_reverse.py`: `ae09f051c815963a0767a62307621a5a1636278b38ff94e0c58243a0855e62e4`

## 1. Independent algebra checks

1. **Fixed exponent words.** Directly subtracting two reverse recurrences
   `Y_j=(2^a_j Y_(j-1)-1)/3` yields
   `delta Y_j=2^(34+E_j)*delta eta/3^j`. For
   `delta eta=3^(m+1)t`, every `0<=j<=m` translation is an even multiple
   of three. Both words remain literally fixed; no exponent is reselected.

2. **Unit, positivity and valuation.** Translation by a nonnegative even
   multiple of three preserves positive odd unit states. The identity
   `3Y_j+1=2^a_j Y_(j-1)` has an odd right-hand target, proving the exact
   prescribed two-adic valuation, not merely a divisibility lower bound.

3. **Height propagation.** Reverse propagation gives
   `h_j=1+E_j-C_j`; fixed exponents and fixed mechanical bits keep all
   heights and any imposed template height bounds unchanged.

4. **Actual seam and carry.** With `Ap-uL=1`,
   `epsilon(i)=b(i+p)-b(i)-u` is one exactly at rank L-1. The telescoping
   identity `C_j^+-C_j^-=-epsilon_j` follows because the H21 initial edge
   is noncarry. Normalized translation is
   `2^(33+C_j^sigma)3^(m+1-j)t`. Thus it cancels from
   `W_j=2^epsilon_j Z_j^+-Z_j^-` exactly, including the carry layer. An
   ordinary uncompleted difference would not cancel at the carry. Fixed
   mechanical weights and fixed dyadic numerator denominators therefore
   preserve precisely the stated local K and numerator data.

5. **All 42 terminal cases.** For each `1<=nu<=21`, the odd residue
   `s=3^(-34)+2^nu mod2^(nu+1)` gives exact valuation nu. Using eta=s-21
   selects positive sign/even eta; using eta=s selects negative sign/odd
   eta. Since `gcd(3^(m+1),2^(nu+1))=1`, CRT supplies each sign/valuation
   while fixing eta modulo `3^(m+1)`, hence modulo nine. Arbitrarily large
   positive representatives justify nonnegative translation t. This
   proves parity blindness within a compatible state template; it does
   not assert blindness between two different fixed leading words.

6. **Tau36 parity.** From the inherited tau35 residues, reverse integrality
   forces minus/plus exponent parity odd/even in 011 and even/odd in 111.
   The common mechanical bit one then gives even/odd source heights in
   both states. Tau36 is noncarry over the refined core, so its defect is
   odd and nonzero. State111 forces the lower-labelled height at least
   two; state011 permits zero. The claimed absolute-height selector is
   conditional and is not presented as an established height-zero fact.

7. **Optional state-partner formula.** At tau36, replacing a1 by a1+1 and
   a2 by a2-1 preserves the two-step cumulative exponent and every height
   from that layer backwards. With
   `D=2^36(eta1-eta0)+1`, direct substitution gives difference
   `2^h D/9` at layer two. Subsequent propagation gives
   `2^(h_j+C_j-3)D/3^j`. The hypotheses ensure positive exponents and an
   even multiple of three at all layers j>=2. At layer one,
   `Y_1^111=2Y_1^011+D/3` is odd and exchanges unit residues. Completed
   gaps agree after normalization; tau35's physical numerator doubles
   because its common height changes from zero to one. The proof properly
   identifies this as two different templates, not one-word state blindness.

## 2. Reproducible exact verification

Command rerun independently:

`python3 verification/verify_rl201_coupled_reverse.py`

Result: PASS for all **168** advertised arithmetic witnesses: two fixture
ranks, two fixed state templates per rank, two signs, and every valuation
1 through 21. Printed seeds, maximal heights and digests matched the proof.

- Rank `30000000000`, depth16, phase `74483362526`: 84 witnesses,
  no carry, maximal height35, seeds18/43207982, digest
  `98c2c15ac7385a5292338dd445fad061586e8646ec91e2127498a512e068e6d7`.
- Rank `31435476725`, depth6, phase `72057431995`: 84 witnesses,
  carry exactly at reverse layer4, maximal height9, seeds18/1610, digest
  `dab85bc6ce3d00a42c4ddbcd74701aac7df1671dfdb8576a50017f5b13de1c44`.

An additional exact label check enumerated each fixture's finite displayed
time labels `(a-j+offset) modL` for offsets0,p and `-34<=j<=depth`.
All 102 labels of the first fixture and all 82 labels of the second are
distinct modulo L. This verifies the proof's no-internal-identification
claim for these fixtures only. No all-rank or height-word scan was made.

## 3. Canonical-anchor clarification and scope audit

The seam fixture's plus trajectory at reverse layer4 is canonical phase
zero and has height **four**. It therefore does **not** impose the inherited
global normalization h0=0. This does not falsify the named local consumer:
the fixture does not require all canonical height anchors or global vertex
identifications. It must nevertheless be explicit in the fixture description
so readers do not mistake an actual rank/mechanical-bit regression for a
full canonical-height model. The general translation theorem remains
conditional on a compatible starting template and preserves whatever fixed
height fields that template actually supplies; these examples do not prove
existence with every global canonical anchor imposed.

The author added this verification-only scope clarification to the fixture
description, plus exact phase/height assertions and explicit JSON scope in
the verifier. The reviewer read the amendment and reran the amended verifier:
PASS, with all 168 witnesses and both witness digests unchanged. The issue is
resolved. No all-anchor-compatible witness is claimed.

Other checked limits:

- Necessary ranks and arithmetic witnesses are not physical occurrences.
- The words are finite local reverse strips; no full periodic height word,
  monodromy, cycle closure or fixed absolute-position moment is imposed.
- Identifying separated time/trajectory vertices can destroy the translation
  because their absolute shifts generally differ; such constraints are
  explicitly excluded from the theorem.
- A signed successor-K interval is outside the consumer and may remove
  terminal cases; no all-global-consumer blindness is asserted.
- The optional partner lemma changes the leading exponent pairs and tau35
  height, so a prescribed leading state or height can obstruct it.
- Finite witness coverage supports the implementation checks; the infinite
  translation/CRT claim rests on the complete analytic argument, not on
  extrapolation from the 168 examples.

No H21 charge, branch, Gate A/B, nontrivial-cycle or Collatz conclusion is
claimed or supported by this local result.

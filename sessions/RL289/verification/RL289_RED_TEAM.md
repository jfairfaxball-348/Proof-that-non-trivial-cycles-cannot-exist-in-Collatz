# RL289 proof-state and scope red team

Date: 2026-09-09

Result: `PASS`

## 1. Gate-A overclaim check

PASS.

RL289 does not claim

`nu_2(K-1)<=H+d-1`

globally and does not claim the balanced specialization

`nu_2(J)<=H`.

The exact residual remains

`k>=25`, `k` odd, `H_can<k`.

## 2. Inherited finite certificate check

PASS.

The RL285 exhaustive `H<=22` certificate is inherited only. RL289 does not duplicate it, enlarge its range, or relabel regression depth as a new certificate.

## 3. Ballot-bijection converse check

PASS.

The converse from a prefix-dominant residue pair to a genuine canonical prefix explicitly relies on the inherited RL283 theorem that full denominator divisibility at every prefix reconstructs integrality/parity legality.

It is not presented as an independent new proof of that reconstruction theorem.

## 4. Rejected-tube legality check

PASS.

The `d=0` rejected sibling tube is used only as a formal full paired parity-tree object.

No branch of that tube is claimed to be a legal canonical trajectory while `d=0`.

The theorem promoted is geometric:

`nu_2(J)` equals the depth of this complete adjacent rejected tube.

## 5. Recent-suffix/global-phase check

PASS.

The finite-suffix transparency theorem is a barrier, not a positive selector.

It explicitly prevents a bounded recent-history argument from being promoted as a global Gate-A proof.

## 6. Mixed endpoint-code independence check

PASS.

The bounded endpoint codes `(a,b)` and carry `c` give an exact representation, but the report records genuine state-merging diamonds with different `H`.

Thus `H` is treated as a Bellman path cost, not an endpoint scalar.

No finite-state closure is misrepresented as a proof.

## 7. Pure 3-adic suffix route check

PASS.

The report records an exact zero-area fake family satisfying the terminal endpoint congruence.

Therefore ordered reverse ranks plus endpoint congruence are explicitly classified as insufficient without fixed-seed 2-adic coupling.

## 8. Signed-defect/high-rank correction check

PASS and REQUIRED.

Earlier exploratory work found a discrete-log/high-absolute-rank rigidity in signed-defect coordinates.

That leverage is demoted in the frozen report because neutral `(101)` seed repetitions raise absolute rank by two while leaving the post-departure physical trajectory `(d,J,H)` unchanged.

The frozen classification is:

`SIGNED_DEFECTS_ARE_FINITE_3ADIC_TRUNCATIONS_OF_FIXED_SEED_SHADOWS_PROVED`

and

`ABSOLUTE_SIGNED_RANK_AS_GATE_A_COMPLEXITY_PARAMETER_DEMOTED_AS_NEUTRAL_PREFIX_GAUGE_ARTIFACT`.

No successor is instructed to treat absolute rank as physical complexity.

## 9. Source-ray/common-phase identities check

PASS with scope correction.

Affine signed-defect source rays and common-phase carry identities derived during RL289 remain algebraically correct, but they are not promoted as a Gate-A contraction because they are gauge representations of fixed-seed shadow data.

## 10. Cycle-lemma seam check

PASS.

For all `k` ballot-restoring minimum rotations of the formal terminal extension, the fixed-seed seam defect has exact valuation `0`, `2`, or `1` according to the cut.

Therefore the report does not claim that cyclic rotation reconstructs a legal fixed-seed path.

## 11. Real-magnitude bound check

PASS.

The exploratory bound `0<J<2^(H+1)` is explicitly rejected after the genuine counterexample `(1,10934,12)`.

It is not promoted or used downstream.

## 12. Gate B / fifth selector / Radius 6+ scope check

PASS.

They remain frozen and untouched.

## 13. Verifier scope check

PASS.

The portable verifier is a regression verifier for exact identities and barriers. It does not claim exhaustive global Gate A coverage.

It checks depth-16 canonical edges, the depth-12 ballot count sequence, rejected-tube branches, and cycle-seam identities.

The output explicitly says:

`inherited_H22_certificate=NOT_DUPLICATED`

and

`gate_A=NOT_CLAIMED`.

## 14. Successor target check

PASS.

RL290 is instructed to use gauge-invariant post-departure fixed-seed/seam information and is explicitly forbidden from treating:

- absolute signed rank;
- pure 3-adic endpoint codes;
- bounded recent suffixes;
- cycle-lemma rotations;
- larger raw height-cap enumeration

as principal routes.

Final red-team result:

`RL289_RED_TEAM: PASS`

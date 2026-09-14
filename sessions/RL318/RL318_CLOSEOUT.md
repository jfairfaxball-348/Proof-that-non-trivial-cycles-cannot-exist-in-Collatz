# RL318 closeout — external frontier contraction and cut-safe first-survivor handover

Date: 2026-09-14
Completed RL: RL318
Successor RL: RL319
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `dbc49cfb64272761fdf2304aee4c1f3321b4c06c`

## 1. Executive conclusion

RL318 does not prove Gate A, Gate B, global positive non-trivial-cycle exclusion, or the Collatz conjecture.

It does materially simplify the conditional research frontier.

A peer-reviewed external convergence verification through `2^71` is frozen as an external finite computational certificate dependency.  When this dependency is admitted, the inherited RL131 continued-fraction machinery plus RL315 reduced-shadow transfer gives

`ell >= 49,547,666,544`

for every `g>1` reduced survivor.

This conditionally replaces the internal-only frontier `ell>=190,537` and eliminates RL317's first internal fibre by an enormous margin.

The first above-resonance continued-fraction survivor after the external wall is

`(a,ell)=(217,976,794,617,137,528,045,312)`.

RL318 then audited whether the newer RL315--RL317 dual-shadow machinery can exploit the older first-survivor programme at this scale.  Generic RL310 packing does not exclude the pair.  Historical nonnegative-defect and contact-polynomial results remain useful, but the most tempting direct splice was found to require an unproved identification between the global least-root cut and the arbitrary balanced cut.

The session therefore closes with a corrected, narrower target rather than an unsafe local claim.

## 2. External `2^71` dependency

RL318 freezes the following finite statement:

`every positive n<2^71 converges to 1`

under the shortcut Collatz map.

Frozen provenance:

- David Barina, "Improved verification limit for the convergence of the Collatz conjecture";
- Journal of Supercomputing 81 (2025), article 810;
- DOI `10.1007/s11227-025-07337-0`;
- source repository `xbarin02/collatz`;
- publication-cited source commit `53c2a0608075d6fe3f10cc6eeeaf50e400c86338`.

The external exhaustive computation was not rerun.  The current mutable project-site extension beyond `2^71` is not consumed.

Full scope and provenance are frozen in `authoritative/RL318_EXTERNAL_2P71_DEPENDENCY.md`.

## 3. Exact consumer replay

The new portable verifier

`sessions/RL318/verification/verify_rl318_external_floor_consumer.py`

checks the consumer arithmetic exactly and records PASS.

It verifies:

- `2^71=2,361,183,241,434,822,606,848`;
- RL317 first-fibre state ceiling `1,311,372,708,449 < 2^71`;
- RL131 denominator wall `qmax=49,547,666,543`;
- conditional reduced frontier `ell>=49,547,666,544`;
- first above-resonance survivor `(217,976,794,617,137,528,045,312)`;
- generic RL310 packing remains non-excluding with margin greater than `21.6x`.

Verifier text SHA-256:

`5185ca1e15382550cf195d14fc2ab86c2ecba7a26059bd4160538621fb208b2e`.

This replay does not reproduce Barina's exhaustive computation and does not rerun the expensive inherited RL131/RL317 certificates.

## 4. Conditional frontier movement

The external floor is not merely enough to eliminate the RL317 first fibre.

The inherited RL131 continued-fraction certificate with `R0=2^71`, transferred to reduced shadows by RL315, gives the contiguous reduced-count exclusion

`ell < 49,547,666,544`.

Thus the live conditional problem jumps to the historical first-survivor scale

`(217,976,794,617,137,528,045,312)`.

The internal-only proof state is unchanged at `ell>=190,537`.

## 5. First-survivor historical resources reactivated

At this exact pair the repository already contains strong ordinary-owned results from RL134 onward.

In particular:

- RL135.2: for `g<=6`, every proper prefix in the true least-root physical normalization has mechanical defect `h_j>=0`;
- RL135.3: for `g<=6`, the true least odd state has `m<2^75`;
- RL136/RL137: broader defect-excursion and state-ceiling theorems;
- RL139--RL142: full-ownership contact-polynomial obstructions for several compressed/bounded-interface height-one patterns.

These results were proved before the RL316--RL317 dual-shadow factorization and are now legitimate splice resources.

## 6. Generic packing barrier

RL318 tested whether the new first-survivor scale is simply killed by RL310 physical segment packing once the external floor is used.

It is not.

The exact verifier uses a rigorous lower bound on the packing right-hand side and a rigorous upper bound on `2 Delta`.  The packing allowance exceeds the required left-hand side by more than a factor `21.6`.

This route is therefore a clean method barrier unless an additional ordinary-owned term is introduced.

## 7. Cross-content scratch

RL317's nonzero-residue branch supplies a content-`h` physical copy and a coprime-content `T_h` shadow.

At the balanced boundaries their signed separation changes from `+E` to `-E`.  Therefore the relative order must cross inside the row.  Same-parity evolution only rescales the signed gap, and a first mismatch of physical-odd/shadow-even orientation does not produce the necessary first sign crossing; a later reverse mismatch is required.

This is structural information only.  Direct recurrence analysis shows that such a reverse mismatch can change sign without violating the available integrality/coprimality conditions.  No contradiction is promoted.

The exact row affine identities

`F_tau(M)=N+r/X`,
`F_sigma(N)=M-r/X`

also give a one/two-unit rounding trichotomy because `0<r<X+Y<2X`.  This does not become a physical endpoint theorem after the shadow mismatch clock and remains scratch.

## 8. Rejected 35-step splice

A promising route appeared when combining the first-survivor state windows with the physical two-row gap.

If an RL317 balanced cut were known to be the RL135 canonical least-root contact, the state window would force the boundary gap below `2^35`, and the two physical rows would therefore first disagree at `v2(G)<=34`.

However, RL315's universal balanced cut is only existential among genuine rotations.  RL135's quantitative state/contact bounds are rooted at the global least odd state.  RL318 found no theorem identifying these two cuts.

Therefore the following are **not** promoted:

- unconditional `G<2^35` for the RL317 balanced rows;
- unconditional first-disagreement-within-35 theorem;
- any least-state prefix congruence transferred to the arbitrary balanced cut.

This correction is binding.

## 9. Historical contact-polynomial splice

RL139--RL142 were checked as possible consumers of the newer dual-shadow geometry.

They do not automatically close `g=2`:

- RL140's multiplicity-two theorem requires a height-one one-deviant-block profile with at most three changed contact residues;
- RL141/RL142 require bounded consecutive/cyclic interfaces with enough untouched blocks;
- arbitrary RL317 ordered-row geometry has not been shown to satisfy those hypotheses.

The contact-polynomial programme remains available once a bounded interface is actually proved.

## 10. Exact surviving branches

RL318 leaves the RL317 dichotomy intact:

1. `epsilon=0`: two distinct rankwise ordered physical balanced rows with genuine `D0` ownership;
2. `epsilon>0`, `H not|epsilon`: content-`h` physical copy paired with a coprime-content `T_h` cycle.

Standalone homogeneous `T_h` invariants remain barred by RL79.

## 11. Successor frontier

RL319 must be cut-safe.

The preferred problem is:

> At the first external survivor and `g=2`, can RL135.2's global least-root nonnegative-defect theorem be transported to a balanced length-`a` cut by a proved theorem, or can its full-word ordinary `+1` consequences be consumed directly by RL316--RL317's full-`D` factorization without transporting the cut?

A bounded balanced-interface theorem would immediately reactivate RL139--RL142 and the RL317 mismatch/row-decoding machinery.

If cut transport is false or too weak, RL319 should derive the exact obstruction and switch to a no-transport full-word ownership consumer rather than enumerate supports.

See `authoritative/RL319_CUT_SAFE_FIRST_EXTERNAL_SURVIVOR_G2_TARGET.md`.

## 12. Scope and difficulty

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.
`g=1` remains separate.
Lean formalisation remains separate.

`PARENT_DIFFICULTY_DELTA = EASIER`

The reason is the large conditional frontier contraction, not a claim that the local `g=2` obstruction has been solved.

# RL136 session state and RL137 kickoff

Date: 2026-08-27

## Completed RL136 state

Incoming base:

`fb5066f21a4b63f86d5e96b51c03d87a1d5a59b5`.

The first reduced survivor remains

`(A,L)=(217,976,794,617,137,528,045,312)`.

RL136 promotes:

- any physical `h=-1` phase requires more than `1/theta>5` reduced blocks to remain;
- every negative phase with at most `320,125,202,432` reduced-block units remaining is isolated and exits immediately to `h=0`;
- therefore all negative phases are isolated for every `g<=320,125,202,432`;
- an isolated negative excursion has an owned dyadic-entry / mod-4 negative-state / mod-3 exit-state signature;
- the exceptional population obeys the triangular shell envelope
  `P(g)<=sum_(1<=r<g theta)(g-floor(r/theta))`;
- the internal least-state ceiling improves to
  `m<2^75` for every `g<=56,336,298,016`;
- low-shell and last-translate physical windows are sharpened as recorded in the RL136 report.

No multiplicity is excluded.

Frozen frontiers remain:

- internal primitive ordinary frontier: `L>=190,537`;
- conditional on inherited external `R#>=2^71`: `L>=49,547,666,544`.

Gate A remains open. Gate B remains open. Global nontrivial-cycle exclusion remains open. Collatz is not proved.

## New barrier precision

The missing resource is now an **occurrence lower bound or no-negative obstruction**.

RL136 does not prove `P(g)>0`. Hence the new entry/exit fibres cannot yet be converted into a multiplicity exclusion.

For `g<=6`, contact/no-contact block markers give a rooted rational-Dyck dichotomy, but anchored marker information still does not control the global sliding-window dispersion required by RL123.5.

## Verification economy

The incoming RL135 bundle is accepted after its recorded sidecar, fresh-unpack, internal-manifest, reconstruction/hash, and fast-verifier checks.

The outgoing RL136 bundle has its own exact arithmetic verifier and fresh-unpack verification record.

## RL137 direction

Continue with `RL137_DEFECT_OCCURRENCE_OR_NONNEGATIVE_BLOCK_DISPERSION_TARGET.md`.

Do not return to bare determinant enumeration. Every new shell calculation must either produce a physical occurrence/packing consequence or directly sharpen the no-negative branch.

# RL135 session state and RL136 kickoff

Date: 2026-08-27

## Completed RL135 state

Incoming corrected base:

`528465486fa9bd6d09bf0df08dc2d269ff71cc29`.

The first reduced survivor remains

`(A,L)=(217,976,794,617,137,528,045,312)`.

RL135 promotes:

- every proper prefix has `h>=-1` for
  `1<=g<=771,316,334,039`;
- every proper prefix has `h>=0` for `1<=g<=6`;
- `m<2^75` for every `1<=g<=28,000,000,000`;
- `m<2^76` for every `1<=g<=771,316,334,039`;
- any realized canonical contact for `g<=6` lies less than
  `169,751,105,674` above the least odd state;
- exact determinant `±2` continuation through `g=16`;
- conditional on inherited external `m>=2^71`, explicit shallow-defect and
  absolute-state population floors through `g=16`.

No multiplicity has been excluded.

Frozen frontiers remain:

- internal primitive ordinary frontier: `L>=190,537`;
- conditional on inherited external `R#>=2^71`:
  `L>=49,547,666,544`.

Gate A remains open. Gate B remains open. Global nontrivial-cycle exclusion
remains open. Collatz is not proved.

## New barriers recorded

1. A canonical-contact numerator difference that reduces to
   `D_full(y-m)` is just ordinary ownership and does not close the branch.
2. One mean-contact sliding window does not control the RL123 global
   sliding-window `L1` dispersion and does not trigger radius three.

## Verification economy

The incoming repaired RL134 bundle is accepted after its recorded sidecar,
fresh-unpack, internal manifest, reconstruction/hash, and fast-verifier
checks. Do not recursively re-run historical expensive certificates unless a
new dependency fails or an apparent contradiction triggers stop-and-repair.

The outgoing RL135 bundle has its own exact arithmetic verifier and
fresh-unpack verification record.

## RL136 direction

Continue with `RL136_OWNED_DEFECT_EXCURSION_AND_CONTACT_PACKING_TARGET.md`.

The main live object is no longer an unrestricted multiplicity lattice. It is
a prefix defect path constrained to `h>=0` through `g=6`, and to `h>=-1`
through a very large certified range, with sparse exactly located negative
shells at low multiplicity.

Do not restart bare CF/product scans or treat determinant candidates as
physical prefixes without ownership.

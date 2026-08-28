# RL153 — primitive `g=1` direct-owner attack target

Pivot away from the frozen negative-defect dependency and attack the first
reduced survivor at multiplicity `g=1` directly:

`(A,L) = (217,976,794,617, 137,528,045,312)`.

Frozen facts relevant to this branch:

- RL135 gives `h_j>=0` for `g<=6`, so `g=1` has no negative-defect excursion;
- RL146 closes primitive height-one owners only for `g>1`; its final
  contradiction is repeated reduced blocks / cyclic carry order and does not
  apply at `g=1`;
- RL147 shows that simple binary layering does not automatically extend the
  RL146 strict-order mechanism.

Primary target:

- use single-block full ownership, the exact affine/numerator identities,
  physical run-fibre width, determinant/prefix restrictions, and any genuinely
  one-block residue/carry invariant to exclude `g=1` or reduce it to an exact
  smaller residual class;
- separate the height-one and higher nonnegative-height cases explicitly;
- prefer an analytic owner-level contradiction or a compact exact finite
  certificate over another broad local enumeration.

Restrictions:

- do not invoke RL146's `g>1` imprimitivity conclusion at `g=1`;
- do not reopen the RL147 naive layer-by-layer carry argument without a new
  one-block resource;
- do not use negative-excursion machinery on the `g=1` branch;
- keep external least-cycle floors explicitly classified if used.

If `g=1` resists, record the exact owner-level obstruction and hand over the
smallest surviving subcase rather than returning to the frozen
negative-defect depth route.

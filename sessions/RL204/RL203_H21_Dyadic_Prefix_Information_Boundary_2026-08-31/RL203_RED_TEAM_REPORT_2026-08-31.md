# RL203 red-team report

Date: 2026-08-31. PASS for the scoped RL203 claim set, conditional on the exact
finite verifier and clean package gate passing during closeout.

Checks:

1. **Identity inflation.** The normalized `U_a` formula is only an exact
   algebraic consequence of the inherited endpoint moment. The rewrite itself
   is not promoted as an eta/sign selection.
2. **Bit indexing.** `2^34 eta` first affects the normalized unit at bit 34;
   modulus `2^35` sees parity. Eta modulo `2^22` requires modulus `2^56`.
3. **Local-tail circularity.** The forced geometric-prefix residue is explicitly
   classified as tautological with RL199's terminal orientation, not independent
   evidence.
4. **Phase/rank confusion.** Offsets are chronological phase offsets below p;
   canonical ranks are computed with `r=aB mod L`.
5. **Anchor/core boundary.** Offsets 1..33 are removed by the positive-tail
   collision with anchor p. Exact ranks for offsets 34..38 lie outside the
   inherited rank core; offset 39 is the first in-core candidate.
6. **Depth arithmetic.** `Ap-uL=1` gives
   `b_(p-d)=u-ceil((Ad-1)/L)` and at d=39 the normalized `2^u` prefix depth is
   exactly 63, safely beyond the `2^56` Hensel-resolution truncation.
7. **2-adic prefix parity.** `P_a` is odd in `Z_2` because its q0 term is one
   and all later physical q terms are even, so the stated root-prefix depth is
   exact rather than an accidental lower bound.
8. **Overreach.** No a>p reflection, rank deletion, eta-class selection, H21
   ownership release, branch/Gate or global conclusion is claimed.

Required verifier: `verification/verify_rl203_dyadic_prefix_boundary.py`.

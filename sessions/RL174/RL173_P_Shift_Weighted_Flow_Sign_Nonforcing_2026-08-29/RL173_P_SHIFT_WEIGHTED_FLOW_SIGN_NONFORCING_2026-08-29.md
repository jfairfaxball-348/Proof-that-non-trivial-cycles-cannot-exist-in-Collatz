# RL173 — p-shift weighted-flow sign nonforcing

RL173 proves that local nonnegative defect grammar and exact p-shift transport
do not force the positive sign required by the least-root physical
weighted-difference identity.

For a positive word, set `G_i=S_(p+i)-S_p-S_i` and

`F=sum_i q_i(3^(-G_i)-1)`.

This is the left side of RL19's weighted-difference identity for rotation by
`p`. Two exact local words with `gcd(A,L)=1`, positive exponents, `D>0`, and
nonnegative defect have opposite signs:

- `(A,L,a,h,p)=(5,2,(1,4),(0,1),1)` gives `F=-52/81`;
- `(A,L,a,h,p)=(8,3,(1,4,3),(0,1,0),2)` gives `F=176/27`.

Neither word is asserted to be a physical cycle. They establish only that
the local grammar and p-shift carry-plus-height transport cannot derive the
least-root positive sign. In a genuine least-root cycle the positivity comes
from the physical state gap on the right side of the weighted-difference
identity, an input not supplied by the local profile.

`RL173_CERTIFICATES/verify_p_shift_sign_nonforcing.py` checks both witnesses
with exact rational arithmetic.

No cycle is constructed or excluded.

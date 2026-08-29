# RL177 Early p-Shift Mismatch and Gap-Valuation Target

## Main objective

Exploit the RL176 forced early first mismatch in the preferred physical
branch `h_p=0`:
\[
1\le J\le36,\qquad
v_2(g_p)=S_J+\min(a_J,a_{p+J}),
\]
with
\[
G_i=0\ (0\le i\le J),\qquad
G_{J+1}=a_{p+J}-a_J\ne0.
\]

Convert this local 2-adic interface into either:

1. a stronger independent modulus/lower bound for the integer gap
   \(g_p\); or
2. a quantitative contribution/compensation law for
   \[
   F_2=\sum_i q_i(2^{G_i}-1)
   =3(\lambda-1)g_p
   <\frac12-\frac{\Delta}{16}
   \]
   that contradicts the RL175 half-barrier.

## Frozen input

Preserve:

- `A=217976794617`, `L=137528045312`,
  `p=65470613321`, `u=103768467013`, `Ap-uL=1`;
- `m=y_0` least odd state and `y_p` unique second-smallest in `h_p=0`;
- corrected defect `G_i=S_{p+i}-S_p-S_i`;
- `F2=3(lambda-1)g_p`;
- `4 | g_p`;
- `4 <= g_p <= 185999999996`;
- first mismatch `1 <= J <= 36`;
- exact valuation
  `v2(g_p)=S_J+min(a_J,a_{p+J})`;
- the first mismatch is inside the carry-free window
  `J+1 << t=L-p`.

The inherited external minimum `m>=2^71` may be used only with explicit
external qualification; if used it gives
`g_p>=10608333336`.

## Primary attack A: sign of the first corrected defect

Split cleanly on
\[
d:=G_{J+1}=a_{p+J}-a_J.
\]

### A1. Positive first defect

If `d>0`, isolate the first positive term
\[
q_{J+1}(2^d-1)
\]
and seek a certified lower bound or a restriction on later negative
compensation.  Use the carry-free mechanical relation in this early
window and the nonnegative physical defect constraints; do not assume an
unaudited density statement.

### A2. Negative first defect

If `d<0`, quantify how much later positive defect flow is required to
make the total `F2` positive.  Try to force at least one compensating
positive phase with a lower weight strong enough to violate the
half-barrier.

## Primary attack B: valuation branches

Use
\[
v_2(g_p)=S_J+\min(a_J,a_{p+J})\le37.
\]

In particular interrogate the high-valuation branches first:

- `v2(g_p)=37` forces `g_p=2^37`;
- `v2(g_p)=36` forces `g_p=2^36`.

Substitute these exact gaps into every available endpoint and p-shift
identity before widening to lower valuations.

## Primary attack C: finite local defect automaton

Because `J<=36`, an exact finite local enumeration is permitted if it is
derived only from certified rules:

- accelerated exponents `a_j>=1`;
- the mechanical floor increments from `b_j=floor(Aj/L)`;
- nonnegative physical heights `h_j=b_j-S_j`;
- equality of shifted/unshifted exponent prefixes before `J`;
- first mismatch at `J`;
- corrected `G_i`.

The purpose is not brute-force Collatz search.  It is to classify the
finite set of legal local first-mismatch types and extract a theorem or
exact certificate.

## Avoid

- Do not reuse the RL175 ownership resultant/root condition as though it
  were an independent gap obstruction.
- Do not revert to the old p-shift defect.
- Do not infer the sign of `G_{J+1}` without proof.
- Do not silently import the external `m>=2^71` bound into the internal
  proof state.
- Do not move to the `h_p>=1` branch until the early-mismatch attack has
  been worked as far as productive.

## Success condition

Preferred: close `h_p=0`.

Strong partial success: prove a new independent modulus or a signed-flow
lower bound that materially narrows one/both first-mismatch sign
branches, with exact verification where finite arithmetic is involved.

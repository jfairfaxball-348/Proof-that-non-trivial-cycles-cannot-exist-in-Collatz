# RL316 proof ledger — row energy, dual shadows, and exact barriers

Date: 2026-09-14
Status: FROZEN WITH RL316 CLOSEOUT

## A. Newly proved analytic mathematics

1. **Prefix-potential identity.**  For a length-`a`, weight-`n` binary word
   `w`, with prefix count `P_j`,

   `sum_(j<a) 2^j 3^(n-P_j)=4Q(w)+2^a-3^n`.

2. **Exact general canonical row energy.**  For the RL315 canonical interface,
   each normalized row energy is an explicit difference of prefix potentials.
   Summing all rows gives exactly

   `4(qH-Q(d))`.

   Under full ownership this is `4H(q-D0 x_0)`.  Thus unsigned row-total
   regrouping is not an independent ownership consumer.

3. **`g=2` meet/join envelopes.**  For balanced rows `w_0,w_1`, the `h`-th
   odd position of the reduced shadow `tau` is the later of the two row
   positions.  The earlier positions define a dual word `sigma`, and

   `q_0+q_1=q_tau+q_sigma`.

4. **Primitive envelope-gap threshold.**  Every genuine primitive `g=2`
   survivor satisfies

   `q_tau-q_sigma>=X+Y`.

5. **Exact dual-shadow bracket.**  Label the balanced boundary states
   `R<x=R+G`.  With `epsilon=q_tau-Q(w_0)>=0`,

   `q_tau=D0 R+XG+epsilon`,

   `q_sigma=D0 R-YG-epsilon`.

   Therefore the rational fixed states `r_tau=q_tau/D0` and
   `r_sigma=q_sigma/D0` obey

   `0<r_sigma<R<x<r_tau`,

   `r_tau-x=R-r_sigma`,

   `r_tau+r_sigma=R+x`.

6. **Cofactor quotient and dyadic row decoding.**  The RL315 quotient

   `n=q_tau-D0 R`

   satisfies

   `n=XG+epsilon`,

   `n+q_sigma=D0 x`.

   For fixed `tau`, `n mod X` determines the complete outgoing balanced row
   through fixed-weight injectivity of `Q(w) mod X`.

## B. Exact inherited certificate replayed

The frozen RL21 `(a,ell)=(65,41)` `X+Y`-factor countermodel was replayed by the
RL316 portable verifier.  It satisfies

`Q(u)-Q(v)=4(X+Y)`,

`epsilon=0`,

`q_tau-q_sigma=4(X+Y)`,

and the quotient lower edge `n=4X`, while

`X-Y` does not divide `Q(u)+Q(v)`.

RL38's unique area-seven local crossing was also replayed and saturates
`q_tau-q_sigma=X+Y` at `(a,ell)=(6,2)`.

These are inherited exact certificates used as red teams, not new finite
cycle exclusions.

## C. Computational evidence only

- The two portable regressions checked 2,645 general canonical words, 224,325
  balanced row pairs, and 111,350 ordered dual-shadow pairs.
- An exploratory exhaustive scan found no distinct simultaneous-factor pair
  through `a<=22`.

The scan is not promoted as a certificate and is irrelevant to the inherited
internal frontier `ell>=190537`.

## D. Method barriers

1. Unsigned row totals telescope exactly to inherited numerator ownership.
2. Binary interface legality, the envelope gap, `X+Y` ownership, and dyadic
   row decoding remain jointly insufficient without the absolute `X-Y`
   state-sum factor; the frozen RL21 witness saturates all of them.
3. The dual shadows are rational fixed orbits.  In particular
   `r_sigma<R` is not a contradiction to leastness of genuine integer cycle
   states.
4. No local denominator ownership is inferred.

## E. Open obligations and scope

- Prove or finitely certify a genuine `D0=X-Y` consumer for the exact
  dual-shadow bracket.
- If that route remains equivalent to the simultaneous-factor problem,
  independently replay the first reduced fibre before using any RL315 scratch
  constants.
- Keep `g=1` separate.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.

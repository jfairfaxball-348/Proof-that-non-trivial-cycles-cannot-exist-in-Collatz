# RL159 — joint distinguished-root Smith normal form and tautology barrier

## 1. Scope

RL159 attacks the exact RL158 target. It keeps the corrected phase normalization

- `D = 2^A - 3^L`, with `gcd(A,L)=1`;
- `M=A-L`, hence `gcd(L,M)=1`;
- `B1(T)=2T^L-1`;
- `B2(T)=3T^M-2`;
- choose integers `p,u` with `Ap-uL=1` and put `rho=2^u 3^(-p) (mod |D|)`;
- `P_h(T)` is the corrected dense primitive inherited from RL157/RL158.

No singleton owner, Gate A, Gate B, nontrivial-cycle exclusion, or Collatz theorem is proved here.

Classification of the main RL159 result: **proved analytic mathematics / exact method barrier**.

## 2. Joint Sylvester lattice theorem

Let `d=|D|`. Form the `A x A` Sylvester coefficient matrix `S=S(B1,B2)` in the basis

`1,T,...,T^(A-1)`

using the rows

`T^i B1`, `0 <= i < M`,

and

`T^j B2`, `0 <= j < L`.

Then

`|det S| = |Res(B1,B2)| = d`.

Define the distinguished evaluation homomorphism

`ev_rho : Z^A -> Z/dZ`,

`(c_0,...,c_(A-1)) |-> sum c_k rho^k (mod d)`.

Every row of `S` lies in `ker(ev_rho)` because `rho` satisfies both distinguished binomials modulo `d`. The row lattice of `S` has index `d`, while `ker(ev_rho)` also has index `d` because `ev_rho` is surjective (the constant vector maps to `1`). Therefore

`row_Z(S) = ker(ev_rho)`.

Consequently

`Z^A / row_Z(S) ~= Z/dZ`,

and the integer Smith normal form is exactly

`diag(1,...,1,d)`.

This is stronger than merely knowing the determinant: the entire nontrivial Smith component is one cyclic distinguished-root coordinate.

## 3. Exact Bezout normal form

The lattice identity immediately gives an exact bounded-degree Bezout normal form.

For every integer polynomial `Q(T)` with `deg Q < A`, choose any integer `r_Q` satisfying

`r_Q == Q(rho) (mod d)`.

Then there exist unique coefficient vectors for polynomials `U,V` with

`deg U < M`, `deg V < L`

such that

`Q(T) - r_Q = U(T) B1(T) + V(T) B2(T)`.

In particular, taking `Q=0` and `r_Q=d` gives an integral Bezout identity for `d`; taking `Q=T` gives an integral identity for `T-rho_bar`, where `rho_bar` is any chosen integer representative of the physical root modulo `d`.

Equivalently, after localization away from `6`,

`Z[1/6,T]/(B1,B2) ~= Z[1/6]/(D)`,

with `T` identified with the distinguished `rho`. The integral Sylvester statement above shows that no hidden odd-primary component is lost by that localization.

## 4. Adding the dense primitive: exact determinantal divisor

Append the coefficient row of any `P(T)` with `deg P < A` to the Sylvester matrix. Let `delta_A(S;P)` denote the gcd of its maximal `A x A` minors, equivalently the index of the augmented row lattice in `Z^A`.

Because the unaugmented quotient is the cyclic group `Z/dZ` and the new row maps to `P(rho)`, one has the exact formula

`delta_A(S;P) = gcd(d, P(rho))`.

Hence

`delta_A(S;P)=d  <=>  P(rho)=0 (mod d)`.

For `P=P_h`, this is indeed strictly more discriminating than the one-binomial condition

`d | Res(2T^L-1,P_h)`,

because it remembers the distinguished physical character. But it is **exactly equivalent** to the original physical ownership condition `P_h(rho)=0 (mod d)` and supplies no independent size, sign, positivity, factor-count, or packing leverage.

Classification: **proved analytic equivalence / method barrier**.

## 5. RL158 counterexample red-team

For `(A,L)=(13,8)`:

`d=1631=7*233`, `M=5`, `rho=1377`,

`P(T)=2+2T+T^2+2T^3+2T^4+2T^5+2T^6+T^7`,

and `P(rho)=17 (mod 1631)`.

The augmented maximal-minor divisor is therefore

`gcd(1631,17)=1`.

So the joint invariant rejects exactly the RL158 false positive.

The following exact identities independently audit the normal form. With `B1=2T^8-1`, `B2=3T^5-2`:

`1631 = U_D B1 + V_D B2`, where

`U_D = 10368T^4 + 8748T^3 + 9216T^2 + 7776T + 6561`,

`V_D = -6912T^7 - 5832T^6 - 6144T^5 - 5184T^4 - 4374T^3 - 4608T^2 - 3888T - 4096`.

Also

`T-1377 = U_T B1 + V_T B2`, where

`U_T = -8748T^4 - 7380T^3 - 7776T^2 - 6561T - 5535`,

`V_T = 5832T^7 + 4920T^6 + 5184T^5 + 4374T^4 + 3690T^3 + 3888T^2 + 3280T + 3456`.

Finally

`P(T)-17 = U_P B1 + V_P B2`, where

`U_P = -42T^4 - 30T^3 - 39T^2 - 30T - 21`,

`V_P = 28T^7 + 20T^6 + 26T^5 + 20T^4 + 14T^3 + 19T^2 + 14T + 18`.

These identities show concretely that once the joint distinguished-root ideal is imposed, `P` contributes only its physical residue `17`.

## 6. Root-of-unity twist red-team

The RL158 character ambiguity cannot survive the joint ideal. If `x` and `y` are simultaneous nonzero roots of `B1,B2` over a field of characteristic coprime to `6`, then `z=x/y` satisfies

`z^L=z^M=1`.

Since `gcd(L,M)=1`, `z=1`, so `x=y`.

The stronger integral Bezout identity for `T-rho_bar` shows uniqueness directly modulo `d` and every divisor of `d`: any simultaneous solution must equal the distinguished root. Thus the joint ideal fixes the character exactly; there is no remaining prime-by-prime twist loophole.

## 7. Method-barrier conclusion

RL159 answers the RL158 question decisively:

- the joint binomial interface **does** recover the distinguished physical root;
- its Sylvester module is exactly one cyclic `d`-component;
- adding `P_h` gives the scalar/minor condition `gcd(d,P_h(rho))`;
- demanding the full `d` component is exactly `P_h(rho)=0 mod d`;
- therefore joint elimination is a tautological re-encoding of physical ownership, not a new contradiction mechanism.

The route should not be iterated through larger Macaulay matrices, extra subresultants, or equivalent minors unless genuinely new non-evaluation structure is added.

## 8. Strategic consequence

The immediate narrow elimination branch has reached a clean barrier. Per user instruction, RL160 should not simply manufacture another nearby algebraic encoding. It should perform a **whole-history crossover audit** across the completed RL sessions, asking which older proved lemmas/certificates can combine with the current singleton-owner/physical-root frontier, which have been genuinely superseded or blocked, and which were merely dropped from active citation because later handovers compressed the proof state.

# RL317 proof ledger — dual-shadow factor and first-fibre replay

Date: 2026-09-14
Status: FROZEN WITH RL317 CLOSEOUT

## A. Newly proved analytic mathematics

1. **Full dual-shadow composition.** In a genuine `g=2` balanced return,
   `Q(tau sigma)=D0(HR-epsilon)` and
   `Q(sigma tau)=D0(Hx+epsilon)`.
2. **Exact cofactor ownership and descent.** Full `D` ownership of either
   shadow composition is equivalent to `H|epsilon`. If
   `epsilon=kH>0`, the shadow word is a positive primitive `g=2` integer cycle
   containing `R-k<R`. Hence a least-state candidate has `epsilon=0` or
   `H` not dividing `epsilon`.
3. **Ordered-row zero branch.** `epsilon=0` implies `tau=u`, `sigma=v`; it does
   not imply row repetition.
4. **Complementary remainder pair.** For `epsilon=kH+r`, `0<r<H`, the two
   full-D remainders are `D0(H-r)` and `D0r`.
5. **Integer-shadow mismatch clock.** `ceil(R-epsilon/H)` follows the lower
   shadow word for exactly `v2(r)<=a` steps and then has the opposite parity.
6. **Defect-signature decoding.** For fixed `tau`, `n mod X` determines
   `(epsilon,k,r,v2(r))` through the inherited row decoder.
7. **Exact generalized-increment reduction.** With
   `d=gcd(H,epsilon)`, `h=H/d`, `E=epsilon/d`, the shadow is the canonical
   coprime-content `T_h` cycle at `hR-E,hx+E`, paired with the content-`h`
   scaled physical orbit at `hR,hx`.

## B. New exact finite certificate

The independent portable first-fibre replay certifies:

- contiguous coverage `41<=ell<=190537`, 190,497 values;
- first reduced fibre `(a,ell)=(301994,190537)`;
- exact `56theta<1<57theta`;
- for `1<=g<=56`, `R<=710,220,447,737`;
- using RL131's certified descent through `23,506,639,475`,
  `g<=9,355,556`;
- at the cap, `R<=1,311,372,708,449`.

Certificate SHA-256:
`dfdb70f67b657410e2219ed3aca79d2116bb5c9c3e8fa434a837bc5d948e0edb`.

## C. Inherited exact certificate used under verification economy

RL131's all-start descent through `23,506,639,475` is inherited as an exact
finite certificate. Its expensive 11,753,319,738-odd-start run was not rerun.
The new verifier independently checks the arithmetic that consumes its endpoint.

## D. Computational regression evidence only

- 111,350 ordered dual-shadow row pairs;
- 221 `D0`-owned nonzero-remainder pairs;
- 1,024,422 factor/content cases;
- 1,017,228 two-clock cases.

These bounded word/model checks support regressions only.

## E. Method barriers and unpromoted work

1. Standalone quotient/carry, moment, product, permutation, or homogeneous
   shadow invariants reduce to inherited RL79 `T_h` structure and cannot force
   `h=1`.
2. RL315's claimed distinct descent run through `19,671,092,983` is not
   promoted. Its arithmetic cap is reproduced, but RL131 already certifies a
   larger range.
3. The RL316 `a<=22` scan remains evidence only.
4. No local denominator ownership is inferred. RL206 and RL233 remain binding.

## F. Open obligations and scope

- Close the `epsilon=0` ordered-row branch or force row repetition.
- Consume the `epsilon>0`, `h>1` cross-content pairing using a genuinely
  non-homogeneous ordinary-`+1` theorem.
- If using the first fibre, work the certified split `g<=56` and
  `57<=g<=9,355,556` without support grammar.
- Keep `g=1` separate.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.

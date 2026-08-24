# RL45 Research Progress Report

Date: 2026-08-22

## Executive result

The RL45 session made progress on both priority tracks but did **not** close the surviving RL branch.

1. **Terminal valuation route:** the conjecture survives a substantially stronger exact test after an analytic state reduction from `(d,e,T,z,...)` to the exact Markov quotient `(d,H,J)`.  The uniform theorem is still open.
2. **Radius-3 resultant route:** the proposed universal 3-free resultant benchmark is falsified as a proof strategy by the already-audited `(65,41)` proper-factor countermodel.  The obstruction is enormous, not marginal.
3. **New analytic phase fact:** after reduction modulo `3T^q-2`, distinct one-runs occupy distinct exponent classes modulo `q`; coefficient collection does not create the hoped-for cancellations.

## Integrity checks

Before research:

- outer RL44->RL45 manifest: PASS;
- nested RL43->RL44 checksum: PASS;
- nested RL43 manifest: PASS;
- `verification/run_all_rl43_verifiers.sh`: PASS (all four RL43 verifiers).

No stop-and-repair event occurred.

## A. Terminal valuation theorem

### Target

`v2(D_E-9*3^p) <= rho_E`.

### New analytic reduction

Define

`H=rho_E-h+1`,
`J=T+3^d-2^d`,
`K=H+d(d+1)/2-1`.

The exact transition system depends only on `(d,H,J)`.

Parity of `J` determines the compatible edge family:

- `J` odd: only `00,11`;
- `J` even: only `01,10`.

The resulting formulas are recorded in `RL45_TERMINAL_VALUATION_REDUCTION.md`.

The sufficient invariant is weakened from RL44's quotient-size candidate to

`J>0 => v2(J)<=K`.

At `d=1`, this is exactly `v2(T+1)<=H`.

A `10` descent preserves `v2(J)-K` exactly, so every higher-height violation would descend to height one.  This proves that the hard part is entirely the height-one zero-cost dynamics.

### Exact certificate

`verify_rl45_terminal_H23.py` explores exact `H` levels `0..23`, with no cutoff on `e`, `p`, or excursion length once states are quotiented by `(d,H,J)`.

It finds no positive `v2(J)>K` state.

The only positive equality state is

`(H,d,J,K)=(3,1,8,3)`,

corresponding to the sharp gap-9 crossing `T=7`, outgoing gap `4`.

**Status:** uniform theorem still conjectural; exact evidence materially strengthened.

### Identified proof bottleneck

At height one, zero-cost horizontal maps are

`J -> (J+1)/2` and `J -> (3J+1)/2` on odd `J`.

They contain exact zero-cost cycles/fixed points (for example `3<->5` and `1`).  This explains why a naive local induction in `H` fails.  A proof needs an analytic quotient/potential for the even exits of this height-one system.

## B. Quantitative radius-3 transplant

### Exact reduced polynomial

For `b=sq+r` and `c=b+kq`, modulo `f=3T^q-2`,

`3(T^b-T^c)`

reduces to

`[2^s(3^k-2^k)/3^(s+k-1)] T^r`,

with a positive coefficient.

Writing `Z` for zeros preceding a run gives

`b = q m + ell(1-Z)`.

Because `q=z+t_out` and run-start zero counts are distinct in `0,...,z-1`, `gcd(ell,q)=1` implies distinct runs occupy distinct residues modulo `q`.

Thus the reduced polynomial has no inter-run coefficient cancellation.

### Falsification of the proposed universal benchmark

`verify_rl45_resultant_obstruction.py` uses the audited `(a,ell,q)=(65,41,24)` proper-factor countermodel.

It computes the exact resultant directly and after reduction and verifies that their 3-free parts agree.

Result:

`|Res(3T^24-2,P)|_(3') > 2^592 (2^65-3^41)`.

So the hoped-for universal bound

`|Res|_(3') < X-Y`

is impossible from the current geometric/proper-factor hypotheses alone.

**Status:** this specific benchmark route is falsified; the structural radius-3 bridge remains valid.

### Replacement target

The next resultant attack should compare arithmetic **common factors**, not absolute norm size.  On the audited countermodel,

`gcd(|Res(f,P)|_(3'),X-Y)=1`,

so this statistic cleanly sees the failed phase condition there.  The sharper target is a **same-root** three-polynomial subresultant/Bezout invariant for

`f=3T^q-2`, `L=2T^ell-1`, and `P`,

because a plain gcd of the two resultants can in principle pick up unrelated roots of `f`.  The comparator remains exact:

`Res(f,L)=X-Y`.

## C. Multiple excursions

No theorem-level multi-excursion full-denominator compression was completed in this pass.

A useful warning is that reducing the sparse proper-factor difference `U-V` modulo `X-Y` is automatically available but is not the missing full-denominator information; it is satisfied by the RL43 countermodel.  The real multi-excursion difficulty remains compression of `V+YG` while controlling synchronized inter-excursion blocks.

## Updated proof ledger

**Analytic:**

- exact `(d,H,J)` Markov reduction;
- parity-determined transition families;
- descent preservation of `v2(J)-K`;
- reduction of the terminal theorem to height one;
- one-excursion reduced-run no-collision lemma modulo `q`.

**Exact finite certificate:**

- no positive valuation violation through `H<=23` in the quotient automaton;
- unique positive equality state through that range;
- exact `(65,41)` resultant obstruction, including direct/reduced resultant agreement.

**Falsified strategy:**

- a universal geometry-only bound `|Res(3T^q-2,P)|_(3')<X-Y`.

**Still conjectural/open:**

- the uniform terminal valuation theorem;
- `rho_E>=a` / `e>=q+2` in the live one-excursion branch;
- a replacement radius-3 uniqueness theorem based on gcd/subresultants;
- multi-excursion full-denominator phase compression.

## Recommended next attack

1. Work at height one on the exact `(d,H,J)` quotient.  Seek a potential for the odd zero-cost maps that bounds the 2-adic valuation of every even exit by the accumulated `H`.
2. In parallel replace the failed absolute-resultant benchmark by a gcd/subresultant comparison with `L(T)=2T^ell-1`.
3. Do not spend the main effort extending the old `e<=40` phase scan; the new `H` quotient is the more relevant finite laboratory for the valuation theorem.

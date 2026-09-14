# RL318 proof ledger — external-floor splice and forced cross-content crossing

Date: 2026-09-14
Status: FROZEN WITH RL318 CLOSEOUT

## A. Newly established / promoted analytic consequences

1. **First-survivor physical gap ratio.** For a genuine `g=2` balanced return at reduced counts `(a,ell)`, positivity of `V=(X-Y)R-YG` gives
   `G/R < (X-Y)/Y = exp(Delta)-1`, hence `x/R<exp(Delta)`.
2. **Cross-content forced sign crossing.** In the RL317 nonzero-residue branch, with `d=gcd(H,epsilon)`, `h=H/d`, `E=epsilon/d`, the physical content-`h` `T_h` trajectory and coprime shadow trajectory have signed boundary gap `+E` at the start of a balanced row and `-E` at the end.
3. **No equality phase.** The physical trajectory is divisible by `h` at every phase, while the shadow trajectory is coprime to `h`; therefore the signed gap is never zero.
4. **First mismatch cannot cross.** Before the first mismatch, same-parity steps preserve the positive sign. At the inherited first mismatch orientation (physical odd / shadow even), the next gap is `P+(delta+h)/2>0`.
5. **Forced reverse mismatch.** Since the final gap is negative, some later physical-even / shadow-odd mismatch must occur. The first crossing step obeys `delta'=(delta-2S-h)/2<0` with `0<delta<2S+h`.
6. **Bounded full-row affine endpoint defect.** For `epsilon=kH+r`, `0<r<H`, `M=R-k`, `N=x+k`, one has `F_tau(M)=N+r/X` and `F_sigma(N)=M-r/X`; since `H<2X`, the affine rounding defect is at most two.

## B. Conditional external-certificate frontier recovered

Using the peer-reviewed external convergence verification through `2^71`, the exact RL131 continued-fraction certificate, and RL315 reduced-shadow extraction:

`ell >= 49,547,666,544`

for every `g>1` reduced survivor, conditional on the external least-state floor.

The first above-side survivor is

`(a,ell)=(217,976,794,617,137,528,045,312)`.

Internal-only remains `ell>=190537`.

## C. Inherited first-survivor results reactivated

At the first external survivor, RL134--RL137 already prove for `g=2`:

- every proper accelerated prefix has nonnegative mechanical defect;
- positive prefixes are confined to canonical reduced-block contact geometry;
- the least odd state satisfies `m<2^75` internally;
- conditional on the external floor, `2^71<=m<2^75`.

These are inherited results, not newly re-proved by RL318.

## D. New exact barrier / red-team results

1. RL310 generic physical segment packing does not exclude `g=2` at the first external survivor; the right-hand allowance exceeds the left-hand defect requirement by a factor greater than 21.
2. RL140's `g=2` contact-polynomial obstruction requires at most three changed contact residues. RL318 has not proved such a bound for the dual-shadow interface.
3. RL141/RL142 bounded-interface theorems require hypotheses not automatically available when `g=2`.
4. The affine `+1/-1/+2/-2` endpoint rounding identities do not identify actual integer trajectory endpoints after a parity mismatch.

## E. Preserved method barriers

- Bare CF/product does not kill the first external survivor.
- Fixed-depth complete residue-prefix descent does not kill it.
- Count-only gcd restrictions do not kill it.
- Standalone homogeneous `T_h` invariants remain blocked by RL79.
- No local denominator ownership is inferred.
- RL206 and RL233 remain binding.
- `g=1` remains separate.

## F. Open obligations

1. **Primary:** exploit the first reverse mismatch / strict crossing in the cross-content branch to derive a contradiction, bounded carry, or support-independent invariant.
2. **Secondary:** use true `D0` ownership plus first-survivor nonnegative-defect structure to force equality of the rankwise ordered rows in the `epsilon=0` branch.
3. Maintain separate internal-only and external-conditional frontiers.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.

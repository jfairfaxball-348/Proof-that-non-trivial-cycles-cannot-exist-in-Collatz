# RL123 session state and RL124 kickoff

Date: 2026-08-27

## Completed RL number

`RL123`

## BASE_HEAD

`de21a8f738e120459313c92e152205b26b3ce8ca`

This is the verified incoming RL122 promotion commit.

## Frozen promoted results

For a hypothetical primitive nontrivial positive ordinary shortcut cycle with cyclic run count `t`:

1. For any positive composition `a_1+...+a_t=n`,

   `sum_i (a_i-k+1)_+ >= max(n-t(k-1),0)`,

   simultaneously sharp on balanced run lengths.

2. If `C_(j,k)` odd-to-even boundaries have preceding odd-run depth at least `j` and following zero-run depth at least `k`, then

   `W >= (C_(j,k)-1) 2^k 3^j`.

3. With `P_plus=max(P,P_CRT)`,

   `D P_plus <= (2^Z-1)(3^L-2^L)`.

4. The parameter-only floor

   `H(L,Z)=min_t max(E_0(Z,t),E_1(L,t),6(t-1))`

   satisfies `W>=H(L,Z)`.

5. For cyclic shift `s`, if `h_i^(s)` is the length-`s` sliding one-count,

   `dist_cyc(w,rot_s(w)) = min_c sum_i |h_i^(s)-c|`.

   In particular,

   `dist_cyc(w,rot_2(w))=min(2L,2Z,A-2t)`.

6. Mixed analytic/exact-certificate corollary:

   every hypothetical primitive nontrivial positive ordinary shortcut cycle has

   `L>=10`.

## Exact finite certificate

After analytic semi-infinite packing cuts, the residual ranges for `L=6,7,8,9` contain exactly

`8,606,677`

rooted fixed-content words.

The exact verifier finds six `D|Q` hits, all repeated alternating trivial-cycle words at `(7,7)`, `(8,8)`, `(9,9)`. Primitive divisibility hits: `0`.

This certificate has no scope outside the explicitly enumerated residual ranges.

## Red-team state

- RL20: passed; physical packing requires actual full ordinary ownership.
- RL79: passed; CRT spacing survives generalized increment but the numerator ceiling scales by `|s|`.
- RL81: passed; only actual owned states are physical.
- primitivity: load-bearing for distinct boundary states; periodic alternating residual hits are explicitly nonprimitive.
- Raw/Farey: no restriction.
- finite work: exact residual scope only; analytic theorems are not finite-scan promotions.

## Correction/demotion ledger

No inherited theorem is demoted.

Precision carried forward: RL123.1 is an exact unrestricted run-composition envelope and a primitive lower floor; no blanket claim is made that every balanced equality configuration is primitive.

## Verification economy

RL122 was accepted from the intact GitHub authoritative state at commit `de21a8f738e120459313c92e152205b26b3ce8ca`. The user-uploaded ZIP copy was corrupted in transit, but the repository copy, sidecar, unpacked tree, and RL122 promotion commit were intact. No historical expensive certificate was rerun beyond dependencies needed for RL123.

## RL124 kickoff

Proceed directly to `RL124_DEPTH_SENSITIVE_CRT_CAPACITY_AND_L10_RESIDUAL_TARGET.md`.

The live residual strip begins at `L=10`, `6<=Z<=24`. Do not brute-force all `417,221,532` rooted words as the first move. Use deeper CRT capacity, exact width ceilings, and sliding-window/closest-radius coupling to compress the strip first.

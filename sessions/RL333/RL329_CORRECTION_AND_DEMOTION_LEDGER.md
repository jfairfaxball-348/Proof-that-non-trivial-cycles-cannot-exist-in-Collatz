# RL329 correction and demotion ledger

Date: 2026-09-15
Status: FROZEN WITH RL329 CLOSEOUT

## Promoted material unaffected

No correctness defect was found in the promoted owned-successor density theorem or its final carry contraction. The portable verifier and independent structural red team are both green.

The promoted load-bearing result is exactly the theorem chain recorded in `RL329_PROOF_LEDGER.md`: exact thresholded singleton ownership, exact large-to-large linkage, exact owned-large-to-short successor reconstruction, exact two-positive layer, the 280-state / 22,991-edge automaton proving `Z<=22K+66`, and the self-consistent cap `n<=32562630353`.

## Material explicitly not promoted

The following session work is preserved but must not be used as authoritative theorem state unless separately reconstructed and promoted later:

1. p=4, p=5, and p=6 positive-run survivor/link counts recorded in the working checkpoint;
2. longer all-ones-run exploratory scans, including absence diagnostics for selected `N(49)->N(49)` cases;
3. any extrapolation from finite positive-run enumeration to arbitrary run length;
4. any claim that the affine-constant identity by itself proves monotone physical-state descent;
5. constant-height plateau bounds beyond the heights and forbidden gap lengths explicitly checked by the frozen certificate;
6. any claim that the p=3 diagnostic closes R1 or removes all long-positive-run obstructions.

## Subordinate exact diagnostics

The p=3 verifier and constant-height plateau verifier are retained as exact session diagnostics within their stated finite scopes. They are not required by the promoted carry contraction.

The p=3 certificate establishes only that the specific RL328 unrestricted three-positive `N(49)->N(49)` edge has no high-carry physical realization and records the exact retained p=3 bridge/link set in its enumerated scope.

The constant-height certificate establishes only the displayed plateau bounds for its enumerated heights and inherited high-carry band.

## Method barrier promoted

`RL329_FINITE_RUN_ENUMERATION_BARRIER.md` is retained as a proved analytic method barrier: if exact ownership is known only through run length `P` while all longer runs are admitted conservatively, the fallback `N(49)->N(49)` cycle with run length `P+1` forces asymptotic density coefficient at least `49/(P+1)`.

This barrier is about proof architecture, not impossibility of stronger Collatz theorems.

## Scope warnings retained

RL324 local matched-rank propagation remains invalid.

The root-aligned `G<2^35` theorem is not available in the live late-row-root branch.

The external `2^71` least-state floor remains conditional.
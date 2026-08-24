# RL81 SESSION STATE AND KICKOFF

Date: 2026-08-24

## 0. Authority and scope

**AUTHORITATIVE OUTGOING RL81 RESEARCH STATE — ROUTE-PIVOT REISSUE.**

The RL81 mathematics, certificates, barriers, and global closure ledger are unchanged from the original RL81 close-out. This reissue changes the selected RL82 attack after an explicit strategy pivot.

Detailed RL81 mathematics:

`RL81_AUXILIARY_BASIN_TRANSFER_PHYSICAL_LIFT_BARRIER.md`

Selected next target:

`RL82_RLFLAT_CYCLE_MAXIMUM_BACKWARD_OWNERSHIP_TARGET.md`

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.

## 1. Verification economy rule — retained

After the current bundle checksum, internal manifest, and fast verifier pass, accept the frozen incoming proof-state ledger as authoritative. Do not recursively rerun historical expensive certificates unless a new load-bearing argument depends on an unresolved historical definition, a verifier fails, or an apparent contradiction triggers stop-and-repair.

## 2. Incoming RL80 gate

The RL80 outer sidecar matched.

Fresh internal manifest: PASS.

Fresh fast verifier: PASS.

No historical expensive suite was recursively rerun.

## 3. Frozen inherited closure state

- radius-3 primitive/full-`D`: closed local obstruction;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by exact finite-certificate corollary;
- Gate A odd `27<=k<=165`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

## 4. New RL81 coordinate theorem

At height one the genuine physical states `A,B` and auxiliary quotient satisfy

`J=3A-B+1`.

RL50's `n,R,L` are functions of the quotient separation, while `U,V` retain the physical common mode through rational powers-of-`2`/`3` normalization.

## 5. New terminal physical lift

At canonical terminal exponent `k=t+3`,

`B=2^(k-2)N`,
`A=[2^(k-2)(N+4)-1]/3`,
`J=2^k`.

The physical midpoint `N` cancels completely from `J`.

## 6. New all-11 common-mode theorem

For a terminal all-`11` suffix of length `j` with

`q=(2^k+1)/3^j`,

the auxiliary trajectory is

`J_r=2^(j-r)3^r q-1`.

But for every suitable parameter `a`,

`A_0=2^j a-1`,
`B_0=2^j(3a-q)-1`

has exactly the same auxiliary trajectory.

The terminal-tail integrality condition is

`3^(j+1)a == 2 (mod 2^(k-2))`.

Its solutions form an infinite progression, and the resulting physical midpoint satisfies

`N=[3^(j+1)a-2^k-2]/2^(k-2)`.

Incrementing `a` by `2^(k-2)` increments `N` by `3^(j+1)` while leaving `J` unchanged.

A subprogression has `N==3 (mod8)` and is arbitrarily large.

Classification: analytic route-barrier theorem.

## 7. RL66 bounded equality certificate

Across all currently open odd `27<=k<=165` and every RL66-allowed all-`11` depth:

- `J_0` is never `N` or `N+4`;
- `n_0=(J_0-1)/2` is never `N` or `N+4`.

Exact finite certificate:

- 71 allowed `(k,j)` cases;
- 284 equality-negative checks.

## 8. Basin-transfer decision

The exact RL48/RL50 reconstruction supplies no basin-preserving operation from blue `J_0` or `n_0` to a genuine physical cycle integer.

- direct equality: absent; midpoint equalities closed on the open range;
- dyadic lift: physical states depend on `N`, not on the blue quotient alone;
- forward Collatz steps: auxiliary orbit stays below the terminal physical block on the current open range;
- legal backward predecessors: no inherited equality identifies a physical state with such a predecessor.

`U,V` do not repair this because recovering `A,B` from them uses powers of `3`.

Therefore the blue route is frozen as a recognition theorem plus transfer barrier.

## 9. Mixed-tail decision

Do not expand mixed/all-`00` basin numerics.

All-`11` is the strongest possible overlap with ordinary Collatz on `J` and already fails at physical transfer. Mixed tails add the fact that `00` on odd `J` is not the ordinary even Collatz branch.

## 10. RL81 exact verifier

`python3 verification/verify_rl81_auxiliary_transfer.py`: PASS.

Counts:

- RL80 blue auxiliary checks: 212;
- RL66-allowed all-`11` cases: 71;
- midpoint equality negative checks: 284;
- terminal-tail physical lift checks: 318;
- maximum all-`11` depth in open range: 5.

## 11. Correction/demotion additions

- blue auxiliary basin capture is not physical cycle-state basin capture;
- terminal suffix quotient has an explicit common-mode kernel;
- RL50 normalized `U,V` are physical rational lifts, not basin coordinates;
- direct midpoint equality is closed on the bounded open all-`11` range;
- mixed-tail basin expansion is frozen;
- any future basin revival must couple to physical `N` by a basin-preserving theorem.

The originally proposed RL82 unit-lattice/content route is **deferred, not disproved**.

## 12. Post-close strategy pivot — RL♭ / cycle maximum

The selected RL82 attack now flips the original extremal viewpoint and studies the **maximum** of a hypothetical nontrivial positive shortcut-Collatz cycle.

Define as new working notation

`RL♭ = M = max C`.

The elementary kickoff deductions are:

- `M` is even;
- its immediate predecessor `P` is odd;
- in a nontrivial cycle the preceding state `Q` is also forced odd;
- writing `M=18r+8`, one has
  `Q=8r+3 -> P=12r+5 -> M=18r+8`;
- extending one more backward ownership layer forces `r!=0 (mod3)`, hence
  `M==26 or44 (mod54)`.

These are not closure claims. They establish that **maximality prunes the inverse Collatz tree** and gives a new exact object to interrogate.

A bounded audit of the seed formulas is included as

`verification/verify_rl82_rlflat_seed.py`.

## 13. RL82 decision

Primary target:

**RL♭ / maximum-state backward ownership and top-of-cycle arithmetic.**

---

# Self-contained kickoff for RL82

Continue the Collatz R-sharp / RL research from the authoritative RL81 route-pivot bundle and matching `.sha256` sidecar.

First verify only the current RL81 gate:

1. outer RL81 sidecar;
2. freshly unpacked internal `SHA256SUMS.txt`;
3. `bash verification/run_fast_rl81_verifiers.sh`.

Apply the verification-economy rule after those pass.

The primary target is:

`RL82_RLFLAT_CYCLE_MAXIMUM_BACKWARD_OWNERSHIP_TARGET.md`.

Mandatory context:

- the RL81 auxiliary-basin transfer route is frozen at a physical common-mode barrier;
- do not resume blue-tree/density/residue expansion without a new physical-state transfer theorem;
- the earlier unit-lattice/content route is deferred, not invalidated;
- define `RL♭` only as new RL82 working notation for the maximum state `M` of a hypothetical nontrivial positive cycle;
- maximality is to be used as a hard inverse-ownership ceiling: every predecessor on the cycle must be a legal shortcut-Collatz predecessor `<=M`;
- the exact seed already gives two forced odd predecessors and `M==26 or44 (mod54)` after the next backward layer;
- do not turn the attack into a brute-force scan of maximum values; seek a symbolic residue/parity automaton and a global consumer for it;
- do not identify `RL♭` with RL48 `N`, `N+4`, or auxiliary `J` without an exact proof.

Work this maximum-state route as far as is productive within the session. A strong result would be an analytic backward-ownership theorem or a genuine bridge from top geometry to a global cycle invariant; a clean no-go/barrier is also valuable if the residue tree cannot be compressed.

Before ending, freeze proofs, finite certificates, external certificates, computational evidence, conjectures, barriers, corrections and verifier status separately; create the next numbered authoritative bundle and sidecar; verify internal manifest and fresh-unpack fast suite.

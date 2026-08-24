# RL48 -> RL49 Handover — Start Here

Date: 2026-08-22

This handover marks a deliberate audit breakpoint in the Collatz R-sharp / RL program. RL48 substantially simplified the proposed radius-3 bridge. The next session should **not** resume broad exploration first: it should audit the exact inherited RL18/RL19 radius-3 theorem against the new explicit four-swap construction and decide whether Gate B is actually closed.

## Mandatory first commands

From the bundle root:

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl48_handover_verifiers.sh
```

Any checksum or verifier failure is a stop-and-repair event.

Then read, in order:

1. `RL48_PROOF_STATE_AND_BRIDGE_LEDGER.md`
2. `rl48_continued/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`
3. `rl48_continued/RL48_RADIUS3_MATCH_COROLLARY.md`
4. `rl48_initial/RL48_SAME_ROOT_SELECTOR_AND_PHASE_COLLAPSE.md`
5. `rl48_initial/RL48_RANK_RELAXATION_BARRIER.md`
6. `RL49_BRIDGE_AUDIT_KICKOFF_PROMPT_2026-08-22.md`
7. `RL48_REPRODUCIBILITY_LEDGER.md`

## Executive proof state

### Analytic results established in RL48

- The RL47 separable cap/room + total-displacement relaxation cannot exclude any retained candidate with `z=q-t>=42`. Gate A therefore requires a genuinely new coupling invariant if it remains necessary.
- Because `gcd(q,ell)=1`, the common root of `f(T)=3T^q-2` and `L(T)=2T^ell-1` modulo `M=2^a-3^ell` is explicit and unique; the earlier different-root contamination issue is removed.
- At that root, the phase polynomial collapses to `P(rho)=4+Q(v)/3^ell (mod M)`, so the full phase condition is exactly `M | Q(v)+4*3^ell`.
- The general full one-excursion words are reconstructed as
  `u=110 x 1 0^t`, `v=111 y 0^(t+1)`.
- The RL47 terminal identity gives the proper-factor identity directly:
  `Q(u)-Q(v)=4(2^a+3^ell)`.
- Concatenation factors exactly as
  `Q(uv)=(2^a+3^ell)(Q(v)+4*3^ell)`.
- Therefore the full phase condition is equivalent to existence of a positive integer `N` with genuine Collatz half-trajectories
  `N --u--> N+4` and `N+4 --v--> N`.
- The forced `110/111` prefixes imply `N=3 (mod 8)`; after the two common leading odd steps the trajectories form the canonical gap-9 entrance, with RL coordinate `T=-14`.
- Along the internal pair dynamics, `T_i=3^(d_i) A_i-B_i`, giving a direct physical interpretation of the RL coordinate.

### Exact finite / computational state retained from RL47/RL48

- RL47 q=79 no-strict-violation certificate remains inherited.
- q=134 exact stress cases `t=2,4,...,16` were rerun through `t=16` and return `hit 0`.
- Both RL48 verifier suites pass.
- The inherited RL47 `(65,41), t=2` witness and RL45 `(65,41), t=0` proper-factor countermodel both satisfy the reconstructed proper-factor/four-swap algebra but fail the full phase scalar, as required.

### Not yet proved

- **Do not claim Gate B closed yet.** The exact audited RL18/RL19 radius-3 theorem statement and all of its hypotheses have not yet been matched line-by-line to the new `N <-> N+4` construction.
- The uniform Gate-A theorem `H>=t+3` is still open. It may become unnecessary for the full-phase branch if the radius-3 theorem already excludes every four-swap configuration; this logical dependence must be audited rather than assumed.
- Global RL closure is not yet established.

## Missing historical input

The present handover contains the full RL47->RL48 provenance plus RL48 work, but it does **not** contain the original RL18/RL19 radius-3 source bundle. The next session should retrieve the exact audited theorem from the project's earlier handovers if accessible. If it is not accessible, do not reconstruct a stronger theorem from memory and do not declare closure; record the missing theorem text as the blocking provenance item.

## Strategic instruction

Do not return to global resultants or extend q=134 merely for larger finite coverage before the radius-3 theorem match is resolved. RL48 has changed Gate B from an algebraic construction problem into a theorem-hypothesis audit.

# RL299 closeout

Date: 2026-09-11
Base commit: `428d1d1b0c0d0444e6e920345692db8e40a34995`
Successor: RL300

## Final classification

`RESONANCE_RECORD_REDUCTION_PLUS_EXACT_PHYSICAL_FRONTIER_TO_A630138896_WITH_J_IMBALANCE_BARRIER`

## Promoted state

1. Exact rational continued-fraction/logarithm verification compresses future quotient-envelope records to the sparse upper record sequence through U5.
2. Gap-free physical certificates through U4 give stopping maxima 589, 612, and 676 on the successively enlarged envelopes.
3. These certificates plus the record theorem eliminate every retained selector through `a=630138896`.
4. The sharper physical inequality uses `J=O-E`: `2W(m)<=m+J+1`.
5. The B-family has exact four-odd-step ancestor `16h+15`; on `h==0 mod3` that ancestor is reverse-tree minimal, proving a uniform ancestry-method barrier.

## Not promoted

Large conditional extensions based on public external Collatz computations are frozen only as provenance-dependent leads. They are not the authoritative unconditional frontier.

The selector resonance coordinate `H` is not identified with canonical Gate-A `H_can`.

No Gate A/B closure or global cycle exclusion is claimed.

## Verification

- `verification/verify_rl299_fast.py`: GREEN in closeout candidate and fresh unpack.
- `verification/verify_rl299_physical_full.c`: compiled in closeout; all three reported extremal witnesses replayed exactly.
- U4 shard ranges are gap-free and frozen in `RL299_FULL_PHYSICAL_REPLAY_LOG.txt`.
- Full U4 exhaustive replay was completed during RL299 and is reproducible with the portable C verifier, but was not rerun during closeout.
- Internal SHA256 manifest verified against the promoted individual-file handover set; the fast verifier was rerun from the closeout copy.

## Successor

`RL300_PHYSICAL_IMBALANCE_RECORD_SPIKE_TARGET.md`

RL300 should attack U5 via a compact bound on `J=O-E` or a stronger coupled physical invariant, not via arbitrary direct volume. A fully imported quantitative external certificate is permitted with exact provenance; convergence-only results are not enough.

## Catalogue status

`stale/deferred` — connector closeout; generated knowledge catalogues were not hand-edited and are outside the promotion gate.

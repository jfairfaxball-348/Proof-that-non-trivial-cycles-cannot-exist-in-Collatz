# RL50 session kickoff prompt — coupled narrow-strip / area attack

Continue the Collatz R#/RL research from the attached `Collatz_Rsharp_RL49_to_RL50_Handover_2026-08-22.zip` as a skeptical research mathematician.

## Mandatory verification first

1. Verify the outer ZIP checksum.
2. Extract the bundle.
3. Run `bash verification/run_all_rl49_handover_verifiers.sh`.
4. Treat any checksum/verifier failure as a stop-and-repair event.
5. Read `RL49_PROOF_STATE_AND_NEXT_ATTACK.md` and the three RL49 research notes before extending anything.

Do not revive the invalid RL48 claim that a depth-three split or the `N<->N+4` pair is automatically an RL19 radius-3 object. RL49 proved the actual half-period cyclic adjacent-transposition distance is

`2(a-t-3+H)`,

so that route is closed.

## Main research objective

Attack the **coupled narrow-strip / area incompatibility** directly on genuine full-phase objects.

The target theorem is:

> No retained one-excursion path satisfying the exact prefix cap, the full-phase quotient condition, and `T+1=2^(t+3)` can have `H<=t+2`.

A stronger theorem proving full phase impossible outright is preferred if the algebra supports it.

## Inputs that should be used together

Under full phase:

`N --u--> N+4 --v--> N`,

`zeta=2^a/3^ell`,

`N(zeta-1)<398/45`,

and the normalized `v`-trajectory is confined to a strip of width

`N(zeta-1)-4 < 218/45`.

At height one, synchronized mass is not free: on every maximal synchronized segment

`sum_(11)2w=(gT)_exit-(gT)_entry`.

The zero-position/rank coordinates satisfy

`X=1-g_end+Zx`,

`S=1-g_end+Zy`,

`E=Zx-Zy`,

`3Zx-Zy=12+(27/2)zeta(1+2^(-k))`,

and under full phase

`27N(zeta-1)=127+8S`.

If the external Ansari 2025 prefix extension is independently accepted/audited, also impose

`ell >= 205632218873398596256`.

## Suggested attack sequence

1. Reconstruct the exact normalized monotone lift for each half, including the exact increment attached to each odd step and its relation to `g`, `h`, rank weights, and prefix heights.
2. Partition the path into maximal height-one synchronized macroblocks and nontrivial excursion pieces.
3. Telescope all synchronized macroblocks to endpoints before applying inequalities.
4. Assume `H<=t+2`. Extract sharp consequences: number of moved ranks, maximum displacement/height, total duration above height one, and possible boundary values of `gT`.
5. Use the exact prefix cap to control `g`/`h` on the genuine excursion pieces.
6. Prove that the compulsory positive lift increments cannot fit inside the full-phase strip `<218/45`, or that the terminal value `T=2^(t+3)-1` is incompatible with the compressed boundary budget.
7. If a direct inequality remains too weak, derive a finite macro grammar indexed by the small area budget `H` rather than by the enormous length `ell`. Search/verify this grammar symbolically and then prove the pattern it reveals.
8. Use the first live continued-fraction pair only as a symbolic stress test. Do not enumerate `~2e20` columns.

## Secondary route

If the narrow-strip argument exposes a sparse phase polynomial or a genuinely small cyclic transport object, compare it line-by-line with the recovered RL19 radius-3/sparse uniqueness theorem. Only invoke RL19 after verifying every global hypothesis. An arithmetic transplant is allowed; a semantic analogy is not.

## Required proof hygiene

Maintain separate labels for:

- analytic theorem;
- exact finite/computer certificate;
- inherited theorem/dependency;
- external theorem dependency;
- conjecture/heuristic.

Any use of Ansari's recursive-sufficiency prefix extension must remain explicitly conditional until independently audited from the source.

At session end, update the proof-state ledger and provide exact verifiers for every new computational claim. If a true closure is reached, include a line-by-line dependency chain showing exactly which theorem closes which remaining gate; do not announce a Collatz/RL proof from numerical evidence alone.

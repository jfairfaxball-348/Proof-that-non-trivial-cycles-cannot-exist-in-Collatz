# RL283 closeout

Date: 2026-09-08

## Authority snapshot

- `BASE_HEAD`: `0da7eab0ffcb8816e54e349d621279b289f9043f`
- incoming authority `START_HERE.md` blob: `34f3e9f0ddb7de225dd56dded25b9019636f77df`
- incoming target blob: `2fcaf871686140d028bd01f3e57ee20b30ad940f`
- incoming RL: `RL283`
- successor RL: `RL284`

## Frozen classification

Primary:

`UPSTREAM_2ADIC_EQUIVALENCE_AND_RELAXATION_BARRIERS_PROVED`

Promoted analytic subordinate results:

- `HIGH_DIVISIBILITY_RECONSTRUCTS_PREFIX_LEGALITY_PROVED`
- `ADJACENT_SWAP_VALUATION_LIPSCHITZ_BARRIER_PROVED`
- `ZERO_RANK_2ADIC_SCALAR_DEPENDENCY_PROVED`
- `TWO_SHADOW_AFFINE_REPRESENTATION_PROVED`
- `TERMINAL_EXTENSION_SINGLE_REVERSED_RANK_REFORMULATION_PROVED`
- `EXACT_ORDERED_RANK_ENDPOINT_REFORMULATION_EQUIVALENT_TO_GATE_A_PROVED`
- `NONCROSSING_RANK_RELAXATION_BARRIER_PROVED`

No inherited promoted theorem is corrected or demoted.

The conjectural guide `J<=2^H` is falsified, but it was never authoritative mathematics.

## Gate-A proof state

Gate A remains open:

`H_can>=k`

at terminal `d=1,J=2^k`.

The exact authoritative residual is unchanged:

`k>=25`, `k` odd, `H_can<k`.

The preferred sufficient theorem remains open:

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

RL283 does not narrow the residual using unpromoted bounded regression.

## Main promoted advances

1. Full final divisibility of a formal ordered equal-weight pair forces prefix divisibility and hence reconstructs exact parity legality at every prefix.
2. Therefore dangerous high-divisibility ordered-rank counterexamples are genuine reachable checkpoint counterexamples; the apparent relaxation is equivalent to Gate A in the dangerous region.
3. A sharp adjacent-swap witness changes the cleared-numerator valuation from `1` to `13`, ruling out per-cell valuation-Lipschitz induction.
4. Integerized zero-rank 2-adic structure reduces exactly to the inherited `B` telescope, so it supplies no independent scalar invariant.
5. The exact two-shadow identity
   `T=3^d C_x(-7)-C_y(-7)`
   and at `d=1`
   `2^m J=3U_x-U_y+2^m`
   gives a compact joint affine representation.
6. Terminal extension
   `X=x10^k`, `Y=y0^k1`
   has exactly one reversed final one-rank, of displacement `-k`; the prior rank displacement is exactly `H`.
7. The fixed-endpoint equation
   `3Q_X-Q_Y=14*3^R+2^L`
   together with that rank structure is an exact re-encoding of Gate A, not an easier algebraic theorem.
8. Strengthening the RL48 separable relaxation by imposing strict noncrossing order on both rank sequences still fails for `z>=42`; the relaxed maximum remains above the exact terminal target.

## Unpromoted evidence / formulations

- `nu_2(J)<=H` and several shifted variants survive every inherited exact `H<=22` checkpoint.
- Exact genuine-terminal regression through extended length `L<=16` finds `379` terminals and zero `H<k` violations.
- The two-template boundary hazard `Beta(n)` is a precise alternate formulation of the remaining boundary risk, but no global `Beta(n)<=H` theorem is proved.

## Verification

Portable regression verifier:

`verification/verify_rl283_structural.py`

Clean execution records:

- two-shadow prefix checks: `805`;
- high-divisibility prefix cases: `60`;
- adjacent-swap cleared numerators: `8192`, `7706`;
- adjacent-swap valuations: `13`, `1`;
- exact extended terminals with `L<=16`: `379`;
- Gate-A violations in that bounded regression: `0`;
- strengthened noncrossing-barrier core inequalities: PASS.

The inherited RL282 exact `H<=22` certificate is accepted under verification economy and is not rerun by the RL283 fast suite.

Recorded deterministic stdout:

`verification/RL283_FAST_VERIFIER_OUTPUT.txt`

Closeout proof-state/scope red team:

`verification/RL283_RED_TEAM.md`

Result: PASS.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL283/` tree is the complete lossless handover.

`SHA256SUMS.txt` covers every frozen RL283 payload except itself.

No ZIP is used, so no outer `.zip.sha256` sidecar applies.

Candidate files are reconstructed in clean local temporary storage, the manifest is checked, and the portable verifier is rerun before promotion.

## Successor — explicit strategic pivot

By direct user instruction, RL284 is **not** a continuation that silently replaces the Gate-A route.

It is an explicit exploratory pivot:

`RL284_SCALE_INDEPENDENT_STRUCTURAL_IRREVERSIBILITY_PIVOT_TARGET.md`

The objective is to test exact scale-independent structural contradictions for non-trivial Collatz cycles: cocycles, winding/order invariants, exact Lyapunov increments, irreversible labelled events, parity-dissipation structure, and a critical prime-factor overlay.

The established Gate-A upstream programme remains frozen intact. RL284 may supersede it only if the pivot earns promotion through an actual theorem-sized advance, scalable reduction, or decisive barrier. Otherwise the recommended return target is the RL283 theorem:

`globally reachable positive even d=1 checkpoint => nu_2(J)<=H`.

Gate B, fifth selector, Radius 6+, and unrelated work remain frozen.

## Catalogue

Generated knowledge catalogues are unchanged and `stale/deferred` under connector-worker closeout policy.

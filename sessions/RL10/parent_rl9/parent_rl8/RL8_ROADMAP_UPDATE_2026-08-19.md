# RL-8 Roadmap Update — 2026-08-19

## Rank 1 — two-edge resonance + determinant

RL-L53 replaces arbitrary length-two weighted-path search by a specific arithmetic target. For a coprime self-rotation, derive the actual transposition separation `(u,v)` and attack

`D | 2^u+3^v`.

Always also compute

`k=uL-vA`.

Then use

`D | 2^|k|-(-1)^L`,

`D | 3^|k|-(-1)^A`.

The next theorem should force `|k|` small, force an incompatible parity/sign class, or show the common divisor on the right cannot contain the full `D` for RL-compatible endpoints.

Do not enumerate arbitrary two-edge paths further.

## Rank 2 — minimum-state mechanical envelopes

RL-L54 gives:

- every proper suffix ending at `R#` is multiplicatively subcritical;
- under the inherited `R#>=2^71` floor, every proper prefix through length 183 is supercritical.

Encode the root departure and final-return physical parity blocks inside these two envelopes. Target a path/distance theorem between the distinguished root and return rotations, not a generic word theorem.

## Rank 3 — weighted block cancellation modulo `D0`

Bare residual-factor descent is dead. Use the exact block congruence

`sum_j 3^(-E_j) Q(B_j) == 0 (mod D0)`

and ask whether RL root/return grammar forces:

- a unique term modulo a prime factor of `D0`;
- a monotone/one-sided imbalance path `E_j`;
- or a shorter repeated block only after the boundary gates are imposed.

The counterexample `100001` must be explicitly excluded by any proposed strengthened descent lemma.

## Rank 4 — positive-density Christoffel displacement

Still needed for a direct quantitative cycle bound. Use the new prefix/suffix slope barriers as local constraints, but do not mistake the 183-step window for an asymptotic density theorem.

## Rank 5 — final-return split

Continue the inherited split `n_close=1` versus `n_close>=2`. In the stronger branch, combine the return exponent/discrete-log class with the suffix mechanical envelope and the two-edge determinant if a short distinguished-rotation path can be forced.

## Guardrails

- RL remains open.
- Binomial-resonance absence through `A<=200` is finite evidence.
- `R#>=2^71` is inherited external input, not re-proved here.
- Bare `D0` descent is refuted; only a grammar-enhanced descent remains viable.

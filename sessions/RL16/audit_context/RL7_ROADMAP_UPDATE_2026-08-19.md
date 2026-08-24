# RL-7 Roadmap Update — 2026-08-19

## Rank 1 — weighted transposition paths of length >=2 between cycle rotations

RL-L51 closes the single-edge case completely: a word has an adjacent self-rotation iff it is primitive Christoffel, and RL-L52 already excludes that case internally.

Every rotation of a genuine cycle is still `D`-divisible. Use RL-L27/RL-L36 endpoint grammar to compare distinguished rotations, but now seek a short **multi-edge** monotone or sign-controlled path whose exact total numerator change lies in `(0,D)`.

Do not search arbitrary parity words. Search only endpoint-compatible rotation pairs and record exact weighted transposition paths.

## Rank 2 — upgrade one Christoffel defect to linearly many

RL-L50's one-move penalty is only a `~1/(4L)` relative correction. It cannot close a huge-cycle branch.

Find a root/xi grammar theorem forcing `Omega(L)` displaced ones relative to the Christoffel envelope, preferably with a uniform lower bound on total transposition weight.

Treat `s=v2(R#+1)=2` as the likely extremal/hard branch because `110...` matches the critical Christoffel prefix. Branches `s>=3` begin over-dense relative to the critical Christoffel word and may admit stronger displacement counts.

## Rank 3 — residual-denominator descent

Use RL-L47's invariant

`D_res=D/gcd(C,D)`.

For `g=gcd(A,L)>1`, test the factor

`D_0=2^(A/g)-3^(L/g)`.

Look for an induced shorter affine identity modulo `D_0`. If it forces a repeated/shorter admissible word, RL-L48 gives the descent contradiction.

## Rank 4 — split the final-return exponent

RL-L46 yields:

- always `D/2^A > 1/[2(R#+1)]`;
- if `n_close>=2`, `D/2^A > 7/[8(R#+1)]`.

Combine the stronger branch with the exact 3-adic discrete-log class of RL-L36. Handle `n_close=1` separately; `t=1` is a universal inverse return and likely requires a different invariant.

## Rank 5 — computation only as theorem diagnostics

New finite work should test one of:

- endpoint rotation transposition distance and exact weighted change;
- number/weight of forced Christoffel corrections by root branch `s`;
- residual denominator descent through a proper factor of `D`;
- final-return `n_close>=2` resonance exclusion.

Do not simply increase compressed `P,n,t` bounds.

## Guardrails

- RL remains open.
- Knight/Hercher/Barina remain external inputs.
- RL-L50 is a quantitative improvement, not a cycle proof.
- The one-edge transposition route is fully classified and exhausted; new transposition work must use path length at least two or a global weighted-distance invariant.

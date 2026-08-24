# RL-6 Roadmap Update — 2026-08-19

## Rank 1 — attack `D|C_good` with the two root endpoint gates

RL-L44 unifies generic and exact-boundary words. The global condition is now:

`D=2^A-3^L` divides one good-rotation numerator `C_good`,

plus finitely many explicit boundary gates when boundaries occur.

The next theorem should use both endpoint facts of the k=0 least-root rotation:

- first departure is forced-low (`a_0>1`) and lands strictly above the root;
- final return has `t` odd, is strict-high (`a_close<1`), and lies in the exact root discrete-log class modulo `2*3^(n_close-1)`.

Primary target: find a divisor `p|D` for which these endpoint gates force the affine cocycle numerator to be nonzero mod `p`, or prove that every compatible residue lifts to a smaller denominator word, contradicting minimality.

## Rank 2 — exploit the new denominator-defect interval

RL-L45 gives, at the least anchor,

`(1-2^-t_close)/(R#+1) < D/2^A < E_mu/(R#+1)`.

This is a word-level near-resonance constraint before numerator divisibility.

Targets:

1. combine the interval with the exact final-return discrete-log class;
2. use continued-fraction/linear-form information only if it acts on the compressed `(A,L,P,E_mu)` data rather than reproducing a classical cycle bound;
3. test whether the low first coefficient and high closing coefficient sharpen `E_mu` enough to isolate a denominator lift class.

## Rank 3 — make the boundary gates residue-local

The boundary grammar is now exact, but the current formula uses a rotation numerator. Reduce each gate modulo `3^(c+1)` by recursive composition so that no huge integer numerator is needed.

Look for incompatibilities between successive boundary gates, especially when a positive cancellation depth forces a large jump in the next `n`.

Do not treat this as the primary global obstruction unless it starts excluding infinite families of `D`-divisible words.

## Rank 4 — theorem-driven finite diagnostics only

The generalized criterion has already been audited in the old small domain. Do not blindly enlarge `P,n,t`.

Any larger search should test one of:

- a proposed prime-divisor obstruction to `D|C_good`;
- a denominator-lift/descent relation;
- a residue-local boundary incompatibility;
- the RL-L45 near-resonance interval.

## Rank 5 — k>0 remains separate

RL-L37 still gives relative-order rigidity through reverse depth `2R#`. Extend it by replacing the uniform correction bound with a cumulative reciprocal-height budget. The RL-6 k=0 boundary work does not close the strict-preperiod case.

## Guardrails

- RL remains open.
- Do not multiply local Haar costs as if plateaus were independent.
- Do not return to root-only xi sieving as the primary closure route.
- Do not scale finite compressed-word enumeration without an infinite invariant.
- Hercher `m>=92` and Barina's verification bound remain external inputs, not internally reproved theorems.
- The good-rotation theorem solves the *3-adic boundary bookkeeping*, not `D|C_good` itself.

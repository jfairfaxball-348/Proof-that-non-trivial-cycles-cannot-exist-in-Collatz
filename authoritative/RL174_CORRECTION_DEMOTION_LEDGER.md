# RL174 correction / demotion ledger

## Stop-and-repair trigger

While resolving the RL174 physical-gap target, the RL173 sentence identifying

`F3=sum_i q_i(3^(-G_i)-1)`

with RL19's physical weighted-difference left side was re-derived and found to
mix binary-time and accelerated odd-phase coordinates.

## Exact correction

For accelerated weights `q_i=2^(S_i)/3^i` and
`G_i=S_(p+i)-S_p-S_i`, rotation by `p` gives

`q_i^(p)=q_i 2^(G_i)`.

Therefore the physical accelerated difference is

`F2=sum_i q_i(2^(G_i)-1)=3(lambda-1)(y_p-y_0)`.

The factor `3^(-G_i)` belongs to the binary-time RL19 form when `G_i` measures
a change in the odd-prefix count, not to the accelerated exponent-prefix
quantity used in RL173.

## Demoted RL173 claims

**Status: DEMOTED / SUPERSEDED AS PHYSICAL IDENTIFICATION.**

1. The identification of RL173's `F3` with the physical accelerated
   p-shift weighted-difference functional is demoted.
2. The old witnesses `(1,4)` and `(1,4,3)` no longer support the physical
   sign-nonforcing claim; their corrected `F2` values are both positive.

## Preserved RL173 facts

- The arithmetic `F3=-52/81` and `F3=176/27` is correct for the auxiliary
  functional actually implemented by the RL173 verifier.
- No cycle was constructed or excluded.

## Repaired replacement

The qualitative sign-nonforcing barrier remains true for the corrected
functional: `(1,4)` gives `F2=14/3`, while `(2,5,4)` gives `F2=-28/9`, with
both words satisfying the same bounded positive-exponent, `D>0`, coprime,
nonnegative-defect local grammar. Neither is promoted as a physical cycle.

No pre-RL173 theorem is demoted by this repair.

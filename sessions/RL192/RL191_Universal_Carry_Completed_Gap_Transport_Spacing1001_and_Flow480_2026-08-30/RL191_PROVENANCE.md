# RL191 Provenance

Date: 2026-08-30

## Incoming repository state

- repository: `jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`
- branch: `main`
- incoming commit: `69bffb574ff185d927e7ed1128bca7a44e228b4e`
- incoming root tree: `8684261951e77e34652bd9b0b66e5c600d392f2b`
- incoming authoritative tree: `9de803d894b90442e8ac3ba1910a44ca3bd7c3a9`
- incoming authoritative session: RL190
- incoming target: `RL191_PHASE46_EXCEPTIONAL_TRANSITION_AND_H21_EARLY_CORE_CAPACITY_TARGET.md`

## Verification economy

The current authoritative state and fast verifier were accepted as the frozen inherited proof state after consistency checks.  Historical sessions were consulted only for concrete dependencies needed by RL191, principally the RL181 full-period `K/rho` identities and RL187 charging vocabulary/conversion.

## RL191 computation

The exact RL191 verifier was developed and replayed locally with Python integer/Fraction arithmetic.  It certifies the universal-gap finite separation scan, density consequence, population arithmetic, all inherited charging-family inequalities, and the resulting flow bounds.

No external web mathematics or uncited external certificate is introduced.

## Promotion rule

RL190's complete incoming `authoritative/` tree is archived losslessly under the RL191 session archive.  The successor `authoritative/` tree contains only RL191 closeout state plus the RL192 target and RL191 fast verifier.  Promotion is performed by one Git tree/commit/ref transition after local package verification.

# RL273 — Radius-5 `|kappa|=5` sector activation

Date prepared: 2026-09-07
Status: **PREPARED, NOT STARTED**

Incoming classification: `RADIUS5_KAPPA3_SECTOR_CLOSED`.

## Inherited exact state

RL270 closes the complete Radius-5 `|kappa|=1` sector.

RL271 and RL272 together close the complete Radius-5 `|kappa|=3` sector:
- flat `[4,1]`;
- flat `[3,1,1]`;
- flat `[2,2,1]`;
- flat `[2,1,1,1]`;
- flat `[1,1,1,1,1]`;
- height-two mass-four-plus-one.

Therefore the only determinant sector still open for the Radius-5 local theorem is `|kappa|=5`.

RL265's exact topology classification allows skew five in all nine Radius-5 topology families:
- `[5]`;
- `[4,1]`;
- `[3,2]`;
- `[3,1,1]`;
- `[2,2,1]`;
- `[2,1,1,1]`;
- `[1,1,1,1,1]`;
- height-two connected mass five;
- height-two mass-four-plus-one.

## Determinant-five framework

After recording exact source/target reversal, orient to `kappa=+5`.

Then

`qA-mL=5`,

so

`gcd(A,L)|5`

and

`gcd(m,A)|5`.

Do not assume either gcd is one. Handle gcd-one and gcd-five sectors explicitly.

Retain the complete positive

`D=2^A-3^L`;

never replace it by a proper factor.

## Primary target

Begin the exact arithmetic closure of the remaining `|kappa|=5` Radius-5 sector.

Required workflow:
1. recover the RL265 sign/orientation and topology cases exactly;
2. derive topology-specific zero-flow cuts, boundary identities and support estimates rather than importing a constant from another family;
3. treat gcd-one and gcd-five determinant sectors explicitly;
4. prove an infinite-to-finite reduction before any large enumeration;
5. test the complete positive `D=2^A-3^L` in every finite certificate;
6. preserve negative-domain, proper-factor, nonprimitive, cyclic-wrap, sign/order, median-choice and numerator-index red teams;
7. use an independent reconstruction/checking implementation and an independent small-range replay before promotion;
8. do not reopen the closed `|kappa|=1` or `|kappa|=3` sectors except to audit a specifically named promoted dependency.

Preferred outcomes for this generation:
- a closed `|kappa|=5` topology leaf;
- an explicit exact finite reduction for one or more leaves;
- or a sharply stated exact arithmetic barrier identifying the missing lemma.

The eventual desired Radius-5 outcome is `RADIUS5_LOCAL_THEOREM_CLOSED`, but do not claim it unless every `|kappa|=5` topology has actually been closed.

Frozen:
- Gate A;
- fifth retained selector;
- selector enumeration;
- general Radius-n programme.

Radius 4 remains locally promoted. Gate B, Radius 5 and global non-trivial-cycle exclusion remain open.

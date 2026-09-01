# Independent targeted repair review: RL203 source versus terminal rank

Status: **Completed targeted correction audit; PASS.** Ordinary research was
paused on the root worker's instruction. No tracked history or authority was
edited, and no broad historical scan was run.

## First invalid dependency

The exact inherited proof read was
`51daff8:authoritative/proofs/RL203_DYADIC_PREFIX_INFORMATION_BOUNDARY.md`,
section 4. It correctly computes the **source** ranks
`r_a=aB modL` for `a=p−e`, but compares them against the **terminal** core
`[25583192106,41775866136]`. It therefore incorrectly reports earliest
necessary `e=39` and the bounds `u−S_a>=63` and root depth at least `100`.

The source/terminal distinction is explicit in the inherited definitions:

- `sessions/RL202/RL201_H21_Absolute_Endpoint_Moment_and_Coupled_Prehistory_2026-08-31/proofs/RL201_ABSOLUTE_ENDPOINT_MOMENT.md`,
  section 1: tau34 **source** rank lies in `[40886621976,57079296006]` and
  equals `aB modL`.
- The same package's `RL201_INHERITED_INTERFACE_AND_SCOPE.md`: terminal rank
  is in `[25583192106,41775866136]`, while the tau34 source rank is
  `(r−34B) modL` in `[40886621976,57079296006]`.
- `sessions/RL203/RL202_H21_Root_Anchor_Speed_Cone_and_Height_Collision_2026-08-31/proofs/RL202_ABSOLUTE_ROOT_ANCHOR.md`,
  section 4: the terminal rank of source phase `a` is `((a+34)B) modL`.

Thus this is a mathematical coordinate/scope correction, not a packaging
defect. The preceding endpoint identities are not its invalid dependency.

## Exact independent arithmetic

Use the inherited constants

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`.

Direct integer arithmetic verifies `Ap−uL=1`, `pB=1 modL`, and

`34B modL=122224615442=L−15303429870`.

The positive tau34 tail at offsets `0,...,33` excludes `1<=e<=33`, because
the source then encounters the zero-height anchor at `p`. For the subsequent
six integer offsets the exact values are:

| e | Source rank `(p−e)B modL` | Terminal rank `(p−e+34)B modL` | In the corresponding cores? | `u−S_a` |
|---:|---:|---:|:---:|---:|
| 34 | 15303429871 | 1 | No | 55 |
| 35 | 72382725878 | 57079296008 | No | 57 |
| 36 | 129462021885 | 114158592015 | No | 59 |
| 37 | 49013272580 | 33709842710 | Yes | 60 |
| 38 | 106092568587 | 90789138717 | No | 62 |
| 39 | 25643819282 | 10340389412 | No | 63 |

At `e=37`, terminal phase is `p−3=65470613318`, outside both RL202 root
windows `[0,2^24)` and `[L−2^24,L)`. Its terminal rank `33709842710` is not
among the exact 12 inherited isolated deletions or the four new RL202 anchor
collision deletions. Hence it survives the recorded **necessary-rank
predicate**. This is not a physical H21 occurrence or a globally admissible
height word.

The old `e=39` source rank happens to lie inside the terminal interval, but it
is outside the source interval and its actual terminal rank is outside the
terminal interval. It is therefore not the first retained necessary source.

The output `RL203_SOURCE_TERMINAL_COORDINATE_CHECK.json` records the complete
six-offset arithmetic, exact inherited deletion list recovered from its source,
and all values used in this review.

## Corrected depth bound

For a below-`p` physical tau34 source, `h_a=1`, `S_a=b_a−1`, and

`b_(p−e)=u−ceil((Ae−1)/L)`.

Therefore

`u−S_a=ceil((Ae−1)/L)+1`.

For `e=37`, exact division gives

`58L<37A−1<=59L`,

so `u−S_a=60`. The ceiling is nondecreasing with `e`. The valid necessary
source separation is consequently

`p−a>=37`, `u−S_a>=60`.

The normalized contribution from the explicit first root term
`3*2^(u+37)` begins at depth at least

`u+37−S_a>=97`.

The other root term is `−2^u P_a`. For a physical below-`p` source, `a>0`
because the zero-height phase `0` cannot be the height-one source. Since
`q_0=1` and every `q_j` for `j>=1` is even in `Z_2`, `P_a` is an odd unit.
That contribution starts exactly at depth `u−S_a`, hence at least `60`.
These are contributions to the expression, not an assertion that the full
moment has that valuation after the remaining tail is included.

Both depths still exceed `56`. Thus both root contributions vanish modulo
`2^56` after normalization, as required for the qualitative below-`p`
information boundary.

## Affected and preserved proof state

- Correct `e>=39` to `e>=37`, `u−S_a>=63` to `u−S_a>=60`, and the explicit
  first root-normalization depth `>=100` to `>=97` wherever that dependency is
  live. The earlier numeric separation claim is invalid at its stated scope.
- Preserve the exact normalized endpoint identity, first eta-sensitive bit
  at precision `35`, and the inherited Hensel resolution `56` from sections
  1–3: they do not use the mistaken rank comparison.
- Preserve the conclusion that these two explicit root contributions vanish
  at the existing `2^56` resolution for below-`p` necessary sources. Its
  corrected proof uses `60` and `97`, not the invalid stronger depths.
- Do not infer a physical realization at `e=37`; its role is necessary-rank
  survival and a sharpness witness for this stated predicate.
- Do not change the inherited necessary-rank set or its count
  `16,188,727,234`: RL203 had not claimed to remove ranks, and the RL202
  terminal-coordinate certificates are unaffected by this later misuse.
- No eta class, sign, valuation, physical incidence, charge, Gate, or global
  exclusion follows from the correction. The `a>p` case remains outside the
  one-sided boundary theorem.

**Independent verdict:** the root's proposed coordinate correction and
preservation of the qualitative 56-bit boundary are valid at this exact scope.

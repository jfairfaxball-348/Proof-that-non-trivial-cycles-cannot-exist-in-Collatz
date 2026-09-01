# RL222 red-team report

Date: 2026-09-01.

Verdict: **PASS with zero deletions**.

## Checks

1. **Sign check.**  The denominator lower-bound argument uses inherited
   `0<ln(2^A/3^L)` only to establish `D>0`; no floating-point approximation is used.
2. **Residue check.**  Exact modular exponentiation independently recomputes
   `3^L mod 2^76 = 7653485309995355851777` and
   `D mod 2^76 = 67904378415918967567359`.
3. **Separation check.**  The exact root cap is
   `31285589992934194300574`, smaller than the residue lower bound by `36618788422984773266785`.
4. **No circular deletion.**  `Qfull=D*y0` is an ownership identity at physical-word
   scope.  Re-encoding it modulo `D^2` is not counted as an independent predicate.
5. **Physical/arithmetic type guard.**  The 139,581,280 tuples remain arithmetic
   necessary candidates; no physical H21 realization is inferred.
6. **Tail-scope check.**  `Qtail=T(c)` is asserted only as the full-return equality.
   The attainable word-side numerator has not been assumed to exist.
7. **2-adic falsification check.**  The leading-prefix residue equality modulo
   `2^m` was derived on both sides and found identical for every locally generated
   prefix.  It is explicitly barred from being used as a selector.
8. **Witness replay.**  The RL221 common witness passes the affine e=16 lift and
   phase-16 recurrence identities and remains within the inherited root band.
9. **Global locks.**  Candidate/prefix/rank deletions remain `0/0/0`; Gate A, Gate B,
   branch contradiction, physical H21 incidence/charge, and global exclusion remain open.

No inherited mathematical correction/demotion is required.

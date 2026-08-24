# External sources used in RL-11

RL-11 introduces one external theorem not previously used in the RL handovers.

## Laurent–Mignotte–Nesterenko explicit two-logarithm estimate

Michel Laurent, Maurice Mignotte, Yuri V. Nesterenko, **“Formes linéaires en deux logarithmes et déterminants d’interpolation”** / **“Linear forms in two logarithms and interpolation determinants”**, *Journal of Number Theory* **55** (1995), no. 2, 285–321. DOI: `10.1006/jnth.1995.1141`.

The exact form used in RL-L73 is also restated in J.-H. Evertse's *Linear Forms in Logarithms* course notes, Exercise 4, p. 12:

For positive rationals `a1,a2 != 1`, nonzero integers `b1,b2`, and

`Lambda=b1 log a1-b2 log a2 !=0`,

`log|Lambda| >= -22 M^2 log H(a1) log H(a2)`,

where

`M=max(log(|b1|/log H(a2)+|b2|/log H(a1))+0.06,21)`.

Public course-note PDF used to verify the displayed formula:

`https://pub.math.leidenuniv.nl/~evertsejh/dio2011-linforms.pdf`

## Role in RL-11

The theorem is used only after RL-L72 has established the self-contained upper bound

`0 < A log2-L log3 < 2 (sqrt(3)/2)^L`.

It supplies the infinite cutoff `L<52000`. All values below that cutoff are handled by exact integer arithmetic in `verify_rl11_mixed_radius3_closure.py`.

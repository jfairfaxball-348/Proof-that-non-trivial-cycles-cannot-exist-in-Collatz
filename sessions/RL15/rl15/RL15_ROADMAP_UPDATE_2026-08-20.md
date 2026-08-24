# RL15 roadmap update — 2026-08-20

## Rank 1 — coefficient-5 `P3 [2,1]` boundary
Try to transplant RL-L96 directly.  The identity `3 tau^h=4` is parameteric and survives independently of simplex shape.  Derive the exact coefficient-5 boundary polynomial, rotate it through all equivalent presentations, and minimize its degree before taking the short resultant with `3X^h-4`.

## Rank 2 — `j=2, P2` lift
Look for the analogous short defect exponent obtained by combining `theta^L=2`, `theta^A=3` with the `j=2` congruence.  The successful RL15 pattern is: find a binomial whose degree is a fixed fraction below the simplex side, then use a rotated sparse polynomial and a shape-free resultant envelope.

## Rank 3 — `gcd(A,L)=3` cubic-cofactor branch
Retain the RL14 explicit descent `S_k`; compare it with any short-defect binomial available after factoring the common cubic scale.

## Do not reopen
Do not revisit `j=1,P3,[1,1,1]` interiors: RL-L98 closes them all, including scalene and equal-gap cases.

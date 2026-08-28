# RL144 correction / demotion ledger

## RL143 height-one interval exclusion — DEMOTED / RETRACTED

Affected claim: exclusion of the height-one branch for
`303,279,262,681 <= g <= 771,316,334,039`.

First invalid dependency: the RL143 lower-width argument identifies the number
of depth-2 odd-to-even CRT boundary states with `O_2=gL-t`.

Correct definitions:

- `O_2 = sum_i max(o_i-1,0)` counts all starts of two consecutive odd steps;
- `C_(2,1) = #{i:o_i>=2,z_i>=1}` counts one terminal boundary per qualifying
  odd run.

These coincide only when every odd run has length at most two. Height one does
not imply that; RL144 proves only the valid universal bound `o_i<=4`.

The RL143 numeric verifier therefore certified an inequality whose
combinatorial lower bound was not established.

Replacement authoritative statement:

`W >= (162/13)(g(2L-A)-3)`

for a hypothetical primitive ordinary height-one cycle.

This corrected floor closes no multiplicity in the inherited one-defect range
when compared with the favorable carried state/width ceiling.

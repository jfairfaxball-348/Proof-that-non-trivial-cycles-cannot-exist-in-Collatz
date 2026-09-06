# RL266 correction / demotion ledger

Date: 2026-09-06

## Corrections made before promotion

1. **Discarded component-as-single-particle formula.**  
   An early scratch derivation treated a constant-sign transport component of length `r` as one particle moving `r` steps and produced a `(2^r-1)`-type component expression. Exact testing falsified that representation: a run may move several distinct particles (for example a block shift such as `011 -> 110`). It is not used anywhere in the promoted proof.

2. **Replacement.**  
   The promoted derivation uses one exact monomial per nonzero flow edge. Whole-component compression is performed only after the exact edge identity is established. The portable verifier checks direct `Q` differences against that edge identity on every finite certificate candidate.

3. **Conservative coefficient use.**  
   A stronger scratch classification of coefficient pairs in a high-density subcase is not needed for promotion and is not promoted. The proof uses only the universal audited component sets
   `C3 in {7,9,13,19}`, `C2 in {3,5}` and the safe coefficient sum bound `24`.

## Demotions

No inherited RL238/RL239/RL265 result is demoted.

No claim beyond the `[3,2]`, `|kappa|=1`, positive-domain full-`D` leaf is promoted.

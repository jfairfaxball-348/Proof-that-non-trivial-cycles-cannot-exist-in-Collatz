# RL211 red-team report

Date: 2026-08-31. Verdict: PASS for the scoped claims.

1. Recomputed `b_0..b_4=0,1,3,4,6` and mechanical digits `1,2,1,2`.
2. Exhausted every nonnegative height path with `h0=h1=0`, `h4=1` and positive
   acceleration; exactly three paths survive.
3. Recomputed composition numerators `85,73,65` independently.
4. Re-derived the H21 source/root-gap identity and checked the power of two:
   `y_(p+4)-y_4=3^4*2^32`.
5. Recomputed eta residues `45,3,56 mod81`; only 45 has an inherited allowed
   mod-9 state residue.
6. Checked all three lifts of 45 modulo243. Their `(y0,yp) mod3` pairs are
   `(1,0),(0,2),(2,1)`; only 207 has two units.
7. Confirmed RL199 mapping: eta 0 mod9 is state011, eta 8 mod9 is state111.
8. Confirmed modulo243 does not determine eta parity, so terminal sign is not selected.
9. Re-read RL195 denominator theorem: normalized gaps need only be dyadic. The rejected
   “integral gap” shortcut is not present in the promoted theorem.
10. Confirmed no rank count, physical incidence/charge, branch/Gate/global closure changes.

No correction/demotion event is required.

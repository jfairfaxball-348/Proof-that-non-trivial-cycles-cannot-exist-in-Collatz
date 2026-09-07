# RL272 certified facts

Date: 2026-09-07

Classification: **RADIUS5_KAPPA3_SECTOR_CLOSED**.

1. The sole inherited open `|kappa|=3` Radius-5 topology was height-two mass-four-plus-one.
2. By exact source/target reversal it suffices to orient to `kappa=+3`, where the flow is a positive `1,2,1` core plus a separate negative singleton.
3. After a zero-flow cut and cyclic normalization, with singleton position `u` and `v=R_u-1`, the exact numerator difference is
   `Q(tau^m x)-Q(x)=3^(L-R_u-1)(15*3^v-2^u)`.
4. The complementary representative is `15*2^(A-u)-3^(L-v)`, and
   `2^(A-u)(15*3^v-2^u)-3^v(15*2^(A-u)-3^(L-v))=-D`.
5. The arc bounds `v<=u` and `L-v<=A-u` give the universal theorem-candidate bound
   `D<=16*3^floor(A/2)`.
6. In the non-bracketing determinant-three case, the exact elementary bound closes every `A>=45`.
7. In the bracketing case, `Lambda<=32(sqrt(3)/2)^A`; this is stronger than the already-promoted RL266 LMN hypothesis and inherits the cutoff `A<=51389`.
8. An exact integer scan of all `A<=51389` satisfying the universal size bound leaves 90 `(A,L)` pairs and no pair with `A>27`.
9. Exhaustive canonical reconstruction for `6<=A<=27`, all singleton positions and all shifts gives 149 positive-domain states and zero full-`D` numerator-difference hits.
10. Those 149 states split `gcd(A,L)=1/3` as 114/35; all happen to have `gcd(m,A)=3`. The latter is recorded only as a finite-certificate diagnostic.
11. The finite certificate uses no primitivity filter and contains five proper-factor-only difference cases.
12. An independent all-word/all-optimal-median replay through `A<=15` gives 708 relevant optimal-flow occurrences, split 354/354 by orientation, zero formula mismatches, zero full-`D` difference hits and zero actual full-`D` words.
13. The negative-domain sentinel `A=11,L=7,D=-139,Q=18904,n=-136` is reproduced and remains outside scope.
14. Together with RL271's five flat closures, the complete Radius-5 `|kappa|=3` sector is closed.
15. Radius 5 remains open only in the `|kappa|=5` sector. Gate A, Gate B, fifth selector, selector enumeration, general Radius-n and global exclusion remain untouched/open as previously stated.

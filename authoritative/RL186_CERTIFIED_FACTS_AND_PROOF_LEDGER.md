# RL186 certified facts and proof ledger

Date: 2026-08-30

Scope: every new statement remains internal to the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)`.

## Inherited frozen facts

- RL181 K corridor: `128,081,997,553 < K_i < 146,795,909,391`.
- Every normalized ordinary p-gap lies strictly between `128,081,997,553` and `293,591,818,782`.
- RL184 clean 40-edge shallow-start corridor floor: `10,075,174,499`.
- RL184 zero-prefix law: `2^(sum d_j) C_n = 3^n C_0`, with every `d_j>=1`.
- RL184 extremal 39-zero rigidity: `C_0=2^39`, all `d_j=1`, terminal common height 24, terminal numerator `3^39`.
- RL185 ordinary corrected flow: `f_i=rho_i(2^-b-2^-a)` with `rho_i>1/2`.
- RL185 exact total corrected flow satisfies `0<F2=sum_i f_i<1/2`.
- The unique carry flow is positive and exceeds `1/2`.

## RL186.1 — exact first-defect numerator law

**Class:** proved analytic mathematics.

For a clean corridor whose first nonzero defect is at offset `tau>0`, the prefix defects `G_0,...,G_(tau-1)` vanish. If `D=sum_(j<tau)d_j`, then

`2^D C_tau = 3^tau C_0`.

The first-defect numerator `C_tau` is odd by the RL183 parity sensor. Hence

`D=v_2(C_0)` and `C_tau=3^tau odd(C_0)`.

In particular `2^tau | C_0`.

## RL186.2 — exact late-tail height vocabulary

**Class:** proved analytic mathematics + exact finite integer certificate.

Combining RL186.1 with the two shallow starting-height possibilities, the strict physical normalized-gap corridor, and RL185's mechanical height envelope gives the following complete necessary endpoint-maximum sets for first-defect offsets `tau=28,...,39`:

- 28: `7..18`;
- 29: `8..18`;
- 30: `10,12..19`;
- 31: `12..20`;
- 32: `13,15..20`;
- 33: `15..21`;
- 34: `16,18..21`;
- 35: `18..22`;
- 36: `19..22`;
- 37: `21,23`;
- 38: `23`;
- 39: `24`.

Thus a first defect at offset 38 is forced to height 23 and the inherited extremal offset-39 event is forced to height 24.

## RL186.3 — first-defect coverage capacity

**Class:** proved analytic combinatorics + exact integer certificate.

Select the **first** nonzero defect in every clean corridor. A physical first defect of endpoint maximum `H=1,...,24` can discharge at most

`28,27,26,24,22,21,20,19,18,17,14,14,14,11,11,11,8,8,7,6,5,2,2,1`

clean starts respectively.

These caps satisfy

`cap_first(H)<=2^(24-H)`.

Consequently the RL185 charging argument already improves to

`sum_(ordinary i)|f_i| > 10,075,174,499/2^25 >300`.

## RL186.4 — late-zero-block shallow-start capacity

**Class:** proved analytic combinatorics + exact integer arithmetic certificate.

In the inherited `tau=39` extremal run, `C_0=2^39` and `d_0=1`, so

`C_1=3*2^38`.

If the next zero-defect edge were again shallow, its common height would be at most one and its normalized gap would be at least `C_1/2=3*2^37`, which exceeds `293,591,818,782`. Therefore the next edge is not shallow. Because every extremal `d_j=1` and `c_j>=1`, common height is nondecreasing along the remaining zero run, so no later edge in that run is shallow.

Partition the cyclic defect sequence into zero blocks ending at a nonzero defect. Among positions whose first-defect offset is at least 37, a block can contain at most two clean shallow starts; if it contains two it spans at least 39 phase positions. A block with only one has smaller density. Therefore the cyclic density is at most `2/39`, giving

`N_37 := # clean starts with tau>=37 <= floor(2L/39) = 7,052,720,272`.

Hence at least

`3,022,454,227`

clean starts have `tau<=36`, and their selected first defects have endpoint maximum at most 22.

## RL186.5 — amplified weighted and signed flow

**Class:** proved analytic mathematics + exact rational/integer certificate.

For `H<=22`, the refined first-defect caps give

`cap_first(H) 2^(H+1) <= 5*2^22 = 20,971,520`.

For `H=23,24` the corresponding worst charging constant is `2^25`.

Using the RL186.4 late-tail cap, the ordinary absolute corrected-flow variation satisfies

`sum_(ordinary i)|f_i|`
`> 3,022,454,227/(5*2^22) + 7,052,720,272/2^25`
`= 7,430,404,397/20,971,520`
`>354`.

Adding the positive carry gives full absolute flow `>354.5`. Since the exact signed total is in `(0,0.5)`, both signs carry corrected-flow mass `>177`. Therefore both positive and negative total K-variation exceed `59`.

This is total/directional variation, not a chronological prefix excursion.

## Finite certificate status

`verification/verify_rl186_first_defect_tail_capacity.py` checks the late-tail numerator enumeration, exact first-defect height sets, refined coverage table, uniform `2^(24-H)` cap, the numerical tail-density consumer, the `>354` weighted lower bound, and the inherited rational enclosure `0<F2<1/2`.

## Closure status

No high-branch or global gate is closed. The directional K-variation floor rises from `>25` in RL185 to `>59`, but the inherited K corridor remains roughly `1.87e10` wide. The remaining obligation is a much stronger multiscale zero-prefix/late-tail capacity theorem or, only after sufficient amplification, a chronological sign-reversal obstruction.

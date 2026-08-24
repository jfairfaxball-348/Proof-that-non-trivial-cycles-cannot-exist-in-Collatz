# RL53 terminal/defect bootstrap: z=37 and z=39

Date: 2026-08-23

## Scope

This note concerns only the sole stable continued-fraction survivor inherited from RL50--RL52. It does not establish Gate A uniformly over all denominators, does not repair Gate B, and does not prove RL or Collatz.

The inherited exact inputs are

- `Zx > 143/12`;
- `E < 5/3`;
- `w_j < 17/30` sequentially;
- `E = sum_j w_j(1-(2/3)^r_j)`;
- terminal power `J_end=2^k` and exact backward coordinate `Q_d`.

RL53 keeps the exact zero-event grammar but accelerates it using native 128-bit residues at precision `3^80`, an x-zero-free `11/10` segment solver, the `Q == 2 (mod 3)` trap, exact-x decomposition, and deterministic chunking for the largest layers. Any exhausted 3-adic precision is a verifier failure.

## z=37

Exact terminal maxima used in the cascade:

`(1,36)=97 -> (3,22)=69 -> (5,14)=52 -> (7,15)=57 -> (8,14)=59 -> (9,14)=60`.

These successively force all ten late x-zero weights `x_27,...,x_36` below `2^-1000`. Exact rational defect lower bounds are checked by `rl53_research/verify_rl53_z37_bootstrap.py`.

With all ten late weights negligible, the exact best non-greedy first-26 mass is only

`11.798579834936028 < 143/12`,

so the first 26 x-zero weights must be the unique greedy schedule and `u_26=70`. Five delayed matching first-26 y-zeros then contribute

`2.059051471067492 > 5/3`,

so at most four are delayed. Including the ten later y-zero indices gives final suffix budgets `(10,14)`. The exact maximum is

`L_terminal(10,14)=60`,

while the genuine suffix has length

`ell-38 = 77692117359936589365`.

Contradiction. Therefore `z=37` is impossible.

## z=39

Exact terminal cascade:

- `(1,38)=104` forces `x_37,x_38` tiny;
- `(3,26)=78` forces `x_35,...,x_38` tiny;
- `(5,17)=60` forces `x_33,...,x_38` tiny;
- `(7,16)=60` forces `x_31,...,x_38` tiny;
- `(8,15)=58` forces `x_30,...,x_38` tiny;
- `(9,15)=61` forces `x_29,...,x_38` tiny;
- `(10,16)=65` forces `x_28,...,x_38` tiny;
- `(11,16)=67` forces all twelve late weights `x_27,...,x_38` tiny.

The exact rational defect lower bounds at the successive monotone cuts are:

- after 2 tiny, 15 delayed first-26 gives `2.072485986091879 > 5/3`;
- after 4 tiny, 13 delayed at `u_33` gives `2.1030369252644814 > 5/3`;
- after 6 tiny, 10 delayed at `u_31` gives `1.6918511096256965 > 5/3`;
- after 8 tiny, 8 delayed at `u_30` gives `1.6822851126754583 > 5/3`;
- after 9 tiny, 7 delayed at `u_29` gives `1.6770234774006962 > 5/3`;
- after 10 tiny, 7 delayed at `u_28` gives `2.09765037322183 > 5/3`;
- after 11 tiny, 6 delayed at `u_27` gives `2.060564266359511 > 5/3`.

These are checked exactly, with rational arithmetic, by `verify_rl53_z39_bootstrap.py`.

Once all twelve late x-zero weights are tiny, the first 26 are again forced to be the unique greedy schedule, hence `u_26=70`. The same five-delayed defect cost exceeds `5/3`, so at most four first-26 matching y-zeros are delayed. Adding `y_27,...,y_38` gives final suffix budgets `(12,16)`.

The exact terminal maximum is

`L_terminal(12,16)=67`.

The exact-eleven and exact-twelve heavy components were split into deterministic partitions. Complete logs are preserved:

- `z39_exact11_chunks.txt`: 128/128 partitions, global max 67;
- `z39_exact12_chunks.txt`: 512/512 partitions, global max 67.

`verify_rl53_chunk_certificates.py` checks complete coverage, no duplicates, and the global maxima.

The genuine greedy suffix after `u_26=70` has length

`ell-36 = 77692117359936589367`,

contradicting the exact terminal bound 67. Thus `z=39` is impossible.

## Certified stable-survivor threshold

The inherited parity condition makes `z` odd. RL51/RL52 had eliminated `27,29,31,33,35`; RL53 eliminates `37,39`. Therefore the sole stable continued-fraction survivor now satisfies

`z >= 41`.

This remains a restricted stable-survivor theorem, not a global Gate-A theorem.

# RL210 global prefix-overlap certificate

Date: 2026-08-31. Exact finite companion to RL210-T1/T2/T3.

The portable verifier `verification/verify_rl210_global_prefix_overlap.py`
reproduces the following facts from integer arithmetic only.

1. `b_23=36`, `b_24=38`, `b_56=88`; the first-divergence selector therefore
   has exact coarse index range `24<=m<=37` once the analytic valuation lemma is
   applied.
2. At `m=24`, exhaust every strictly increasing pair of exponent continuations
   obeying `S_t,S'_t<=b_t` modulo `2^40`. With `S_24=37<S'_24=38`, the possible
   normalized residues are `1,3,7 mod8`, while the required residue is `5 mod8`;
   this orientation is impossible. With `S'_24=37<S_24=38`, residue 5 occurs,
   so that orientation is **not excluded** by this certificate.
3. For exact above-p source offsets `1<=e<56`, terminal transport
   `r=(p+e+34)B modL` and the complete current discrete predicate leave exactly
   six necessary ranks:

| e | terminal phase | terminal rank | n_e=b_e-1 |
|---:|---:|---:|---:|
| 4 | 65470613359 | 31435476727 | 5 |
| 16 | 65470613371 | 34124151203 | 24 |
| 28 | 65470613383 | 36812825679 | 43 |
| 33 | 65470613388 | 26472436268 | 51 |
| 40 | 65470613395 | 39501500155 | 62 |
| 45 | 65470613400 | 29161110744 | 70 |

All six terminal phases lie strictly outside the RL208/RL209 first/last-`2^35`
root-layer regions, so those later cuts do not alter this small-offset list.
The short-prefix lock criterion `n_e<37` and `b_(e-1)<n_e` holds exactly for
`e=4,16` among these six.

The current above-p count is 7,091,831,284. Therefore exactly **7,091,831,278**
current necessary above-p ranks have `e>=56` and are subject to RL210-T2's global
first-divergence selector. The remaining six are the table above.

This certificate deletes no rank. Arithmetic compatibility of an abstract prefix
shape is not a claim of a physical H21 realization.

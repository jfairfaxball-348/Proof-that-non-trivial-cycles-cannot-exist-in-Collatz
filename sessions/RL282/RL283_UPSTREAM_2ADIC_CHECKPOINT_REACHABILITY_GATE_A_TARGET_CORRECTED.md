# RL283 — upstream 2-adic checkpoint reachability Gate-A target

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED
Authority repair: 2026-09-08 — incorporates the exact RL282 `H<=22` checkpoint certificate.

## Incoming classification

RL282 closed as

`TERMINAL_BACKWARD_HEIGHT_DIGIT_PRICING_AND_LOCAL_TAIL_BARRIER_PROVED`

with promoted analytic subordinate results:

- `ONE_ZERO_MOD3_OUTPUT_SHELL_PROVED`;
- `ARBITRARY_POSITIVE_BOUNDARY_SUFFIX_AFFINE_COMPRESSION_PROVED`;
- `TERMINAL_ONE_ZERO_HEIGHT_DIGIT_PRICING_PROVED`;
- `BOUNDARY_INVERSE_RUN_RECURRENCE_PROVED`;
- `PURE_ZERO_FINAL_TAIL_LOCAL_REALIZABILITY_FAMILY_PROVED`;
- `POSITIVE_TAIL_MASS_AND_F_BARRIER_PROVED`;
- `UPSTREAM_CHECKPOINT_REACHABILITY_IDENTIFIED_AS_GATE_A_OBSTRUCTION`.

Post-promotion RL282 correction additionally promotes exact finite certificates:

- `HEIGHT_22_POSITIVE_CHECKPOINT_AUTOMATON_CERTIFIED`;
- `K5_TO_K23_GATE_A_CASES_CLOSED_CERTIFIED`.

Gate A remains

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator is now restricted to

`k>=25`, `k` odd, `H_can<k`.

Gate B is separate/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen.

## Exact inherited RL282 state

Preserve all RL281/RL280/RL279 results and additionally:

1. Every reachable positive one-zero output satisfies
   `nu_3(J_out)=1`, equivalently `J_out==3 or 6 (mod 9)`.
2. For any legal final positive boundary suffix `w` of length `L`, with `r` one-bits and affine constant `C_w`,
   `2^(k+L)=3^r J_0+C_w`.
3. If `J_0` is a one-zero output shell state,
   `nu_3(2^(k+L)-C_w)=r+1`.
4. Put
   `N_w(k)=2^(k+L+1)-2C_w+3^(r+1)`.
   Then exactly
   `N_w(k)=3^r(2J_0+3)`,
   so a preceding one-zero excursion of height `h` requires
   `h<=nu_3(N_w(k))-r`.
5. Each extra allowable cheap height unit for a fixed suffix selects one ternary lift of the terminal exponent class.
6. The inverse boundary block is
   `R_t(A)=2(2^t A/3^t-1)` for `A=J+1`,
   defined for `0<=t<=nu_3(A)`.
7. Deep inverse undershoot forces available preceding one-zero height exactly `1`; only near-full/full valuation branches can support larger cheap height.
8. Final-tail arithmetic is not sufficient for Gate A: for every odd `k>=3` and every `h>=2`, there are infinitely many locally legal positive terminal blocks
   `J_in --0 1^h--> J_0 --0^q--> 2^k`
   with total height `h`.
9. Along that family,
   `S_block -> Q_T`
   and
   `F_T-F_in -> 4Q_T`;
   therefore terminal 3-adic thinning plus the inherited positive mass/`F` ceilings cannot alone exclude low-height local tails.
10. The local checkpoint valuation inequality is not block-monotone: a legal height-one first return `30 -> 24` raises `nu_2(J)` from `1` to `3`.
11. Exact `H<=22` positive-checkpoint certificate:
    - nonpositive states: `3,254,996`;
    - first-positive entries: `169`;
    - positive even checkpoint states: `146,341`;
    - odd boundary origins macro-closed: `13,583`;
    - maximum exact stay-odd trace: `263`;
    - no arbitrary `J` or word-length cutoff.
12. Exact power-of-two minima inside the complete cap:
    `k5:H9`, `k7:H15`, `k9:H15`, `k11:H18`, `k13:H18`, `k15:H22`.
13. No terminal `2^17`, `2^19`, `2^21`, or `2^23` occurs anywhere with `H<=22`.
14. Therefore all odd `k=5,7,...,23` are Gate-A safe. Combined with the inherited theorem that terminal `k` is odd and the inherited `k=3` closure, the live residual is exactly
    `k>=25`, `k` odd, `H_can<k`.

The exploratory `H=23..26` search remains evidence only and is not authoritative.

## Mission

Attack the **upstream global reachability** obstruction on the corrected residual.

The preferred sufficient theorem is:

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

At a terminal `J=2^k` this immediately proves Gate A for every remaining `k>=25`.

A stronger observed candidate is

`J<=2^H`

at reachable positive `d=1` states, but this is not established and should be treated only as a conjectural guide.

Preferred order:

1. Quotient the inherited mandatory height-3 sign-change core and work from the first positive checkpoint forward.
2. Search for a state invariant or finite-dimensional residue invariant carried by **global reachability from the initial state**, not merely by local positive blocks.
3. Use the exact normalized `(d,J,H)` recurrence and/or the global `x/y` rank identities to control 2-adic divisibility at positive even checkpoints.
4. Explicitly account for the fact that individual excursions can increase `nu_2(J)` by more than their local height.
5. Use RL282's final-tail barrier to avoid spending effort on proving stronger terminal-tail 3-adic sparsity: such sparsity is already known to be insufficient.
6. If the direct `nu_2(J)<=H` theorem fails, isolate the smallest additional state variable needed to restore a monotone/inductive inequality.
7. Seek either:
   - a uniform upstream reachability theorem closing Gate A; or
   - the strongest correct scalable recurrence that reduces the remaining obstruction without another unprincipled height cutoff.

## Supporting computation policy

Finite reachable-state computation may be used to discover or falsify candidate invariants.

The exact `H<=22` automaton is now an authoritative finite certificate and must be preserved.

Do not promote the exploratory `H=23..26` observations without a separately packaged gap-free certificate.

Do not make larger raw height-cap enumeration the principal programme.

## Forbidden repeats

Do not:

- restart final positive boundary-tail 3-adic classification as the principal programme;
- try to close Gate A from positive zero count or `S_positive<15` alone;
- assume local `nu_2(J)` monotonicity across excursions;
- make larger raw `H`-cap enumeration the principal programme;
- reopen completed RL280/RL281 excursion interiors;
- classify accelerated `3n+1` boundary cycles;
- restart fixed-zero enumeration;
- merge Gate B into Gate A without a new proved coupling;
- scan the fifth selector;
- start Radius 6+.

Gate B remains frozen unless a newly proved coupling genuinely requires it.

# RL281 — positive-checkpoint Gate-A closure target

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED

## Incoming classification

RL280 closed as

`SHARP_POSITIVE_EXCURSION_STATE_SCALE_LYAPUNOV_PROVED`

with subordinate results:

- `SHARP_EXCURSION_STATE_VERSUS_HEIGHT_INEQUALITY_PROVED`;
- `EXCURSION_COUPON_DECOMPOSITION_PROVED`;
- `NESTED_ZERO_WEIGHT_AMPLIFICATION_PROVED`;
- `SHARP_EXCURSION_ZERO_COMPLEXITY_HEIGHT_ENVELOPE_PROVED`;
- `EXACT_DEPTH_TWO_EXTREMAL_NORMAL_FORM_PROVED`;
- `SHARP_FIRST_RETURN_STATE_SCALE_THEOREM_PROVED`;
- `EXTREMAL_2ADIC_3ADIC_RIGIDITY_PROVED`;
- `POSITIVE_CHECKPOINT_RETURN_LYAPUNOV_PROVED`;
- `GLOBAL_ENDPOINT_POTENTIAL_DEPENDENCY_IDENTIFIED`.

Gate A remains

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator still satisfies

`m0>=8`, equivalently `z>=k+6`.

Gate B is separate/open/frozen. The fifth selector was not scanned. Radius 6+ is frozen.

## Exact inherited RL280 state

Preserve all RL279 results and additionally:

1. First-return excursion exact factorization:
   `P_out/P_in = 2(4/3)^h 3^(z-1)(3/2)^E`,
   with `E>=0`.
2. For `-2<=c<=0`,
   `Phi_c=Q(K+1+2^(d-1)(c-1))/3^d`
   is globally nondecreasing and strictly increases on ascents.
3. Excursion height/coupon decomposition:
   `h=sum h_j`,
   `D_E=sum c_j(1-(2/3)^h_j)`.
4. Nested zero law:
   `g_(j+1)<=h_j-1`,
   hence
   `c_(j+1)>=3c_j(2/3)^h_j`.
5. Sharp excursion envelope:
   `D_E >= c_entry[1+((2^z-4)/3)(2/3)^(h-z)]`.
6. Equality is unique:
   `x=0 1^(h-z) 0^(z-1) 1`,
   `y=1^(h-z+1) 0^z`,
   i.e. the depth-two extremal family.
7. Exact local endpoint identity:
   `Q_out K_out-Q_in K_in=2S_E+D_E`.
8. Sharp first-return state/scale theorem:
   `Q_out(K_out-7/2+2^(3-z)) >= Q_in(K_in+3)`,
   equality exactly for the depth-two family.
9. Equality arithmetic rigidity:
   with `s=h-z`, `w=2K_out-7`,
   `3^(s+1)(K_in+3)=2^(s+1)(8+2^(z-1)w)`.
10. Positive checkpoint:
    `d=1,J>0,J even`,
    with
    `F=Q(J+3)`.
    Across the next excursion plus any positive zero-height boundary transient and exit,
    `F_next>F_in+Q_in/3`;
    if the excursion has at least two zeros,
    `F_next>F_in+Q_in`.
11. Terminal ceiling:
    `F_T<110/3`,
    so every positive checkpoint satisfies
    `Q(J+3)<110/3`.
12. The aggregate `Phi_c` terminal telescope is affine-dependent on the existing `2S+D` identity; do not double-count it as a second independent scalar constraint.

## Mission

Use the positive-checkpoint compression to attack Gate A directly.

Preferred order:

1. Express every positive excursion-entry scale `Q_i` as its exact global zero weight `c_t`.
2. Combine strict growth of `F=Q(J+3)` with
   `17/2<S<21`,
   the exact coupon budget,
   terminal scale,
   and `m0>=8`.
3. Determine how a hypothetical `H_can<k` path could generate the required sequence of increasingly small positive entry weights without exceeding the terminal `F` ceiling.
4. Treat the depth-two equality family as the only genuinely cheap local obstruction. Use its exact 2-adic/3-adic congruence law instead of re-enumerating arbitrary excursion interiors.
5. Quotient positive neutral boundary transients by the proved `F`/endpoint monotonicities; do not classify Collatz cycles.
6. Seek either:
   - a uniform contradiction closing Gate A, or
   - the strongest correct finite-dimensional residual obstruction if uniform closure still fails.

## Preferred success criterion

Prove that no retained terminal can have

`H_can<k`.

A genuinely scalable contraction of the remaining positive-checkpoint/equality-family state space is also meaningful if it materially reduces the uniform Gate-A obstruction.

## Forbidden repeats

Do not:

- restart the internal first-return excursion classification already completed in RL280;
- treat the aggregate endpoint potential as independent of `2S+D`;
- make flat eight-zero enumeration the principal programme;
- attempt to classify all accelerated-`3n+1` boundary cycles;
- revive zero-budget-only height growth;
- restart selector enumeration;
- merge Gate B into Gate A without a new proved coupling;
- start Radius 6+.

Gate B remains frozen unless a new proved coupling requires it.

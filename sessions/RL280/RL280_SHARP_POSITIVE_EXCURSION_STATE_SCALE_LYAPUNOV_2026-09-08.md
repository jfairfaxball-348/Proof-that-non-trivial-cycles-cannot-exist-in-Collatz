# RL280 — sharp positive-excursion state/scale compression and positive-checkpoint Lyapunov law

Date: 2026-09-08

## Classification

Primary:

`SHARP_POSITIVE_EXCURSION_STATE_SCALE_LYAPUNOV_PROVED`

Promoted subordinate results:

- `SHARP_EXCURSION_STATE_VERSUS_HEIGHT_INEQUALITY_PROVED`
- `EXCURSION_COUPON_DECOMPOSITION_PROVED`
- `NESTED_ZERO_WEIGHT_AMPLIFICATION_PROVED`
- `SHARP_EXCURSION_ZERO_COMPLEXITY_HEIGHT_ENVELOPE_PROVED`
- `EXACT_DEPTH_TWO_EXTREMAL_NORMAL_FORM_PROVED`
- `SHARP_FIRST_RETURN_STATE_SCALE_THEOREM_PROVED`
- `EXTREMAL_2ADIC_3ADIC_RIGIDITY_PROVED`
- `POSITIVE_CHECKPOINT_RETURN_LYAPUNOV_PROVED`
- `GLOBAL_ENDPOINT_POTENTIAL_DEPENDENCY_IDENTIFIED`

Gate A remains open. Gate B is unchanged/open and frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming exact state

RL280 starts from RL279 with:

- the exact normalized state `K=J+2^d-1`;
- the four affine `(d,K)` transitions;
- height increment `H'=H+d-1`;
- prefix potential `P=2^(H+n)/3^r`;
- physical scale `Q=P/2^H=2^n/3^r`;
- zero weights `c_t=2^(t-1)(2/3)^(u_t)`;
- exact height/coupon identity
  `H_can=sum h_t`,
  `D=sum c_t(1-(2/3)^h_t)`;
- exact terminal identity
  `2S+D=12+X(1/2+2^(-k-1))`;
- uniform zero-mass corridor `17/2<S<21`;
- terminal scale
  `X=2^(k+2)c_last(2/3)^tau`;
- boundary accelerated-`3n+1` conjugacy and endpoint monotonicities;
- every positive neutral boundary cycle scale-expands, every negative neutral boundary cycle scale-contracts;
- `J>0` forward invariance;
- exact seven-zero Gate-A safety, hence
  `H_can<k => m0>=8 => z>=k+6`.

The RL280 target was a scalable theorem for a height-positive first-return excursion

`d=1 -> d>1 -> d=1`.

## 2. Exact first-return factorization

Consider a first-return excursion beginning at `d=1` with odd `K`. The first column is forced to have `x=0` and ascends to `d=2`.

Let:

- `L` be the excursion length;
- `h=Delta H`;
- `r` be the number of `x=1` bits;
- `z=L-r` be the number of `x=0` bits;
- `E=h-(L-1)`.

All post-entry pre-return starting levels satisfy `d>=2`, hence `E>=0`.

Since a column multiplies `P` by `2^d/3^x`,

`P_out/P_in = 2^(L+h)/3^r`.

Using `r=L-z` and `L=h+1-E` gives the exact factorization

`boxed:
 P_out/P_in
 = 2 (4/3)^h 3^(z-1) (3/2)^E`.

Therefore

`boxed:
 P_out/P_in >= 2 (4/3)^(Delta H)`.

Equality holds exactly when `z=1` and `E=0`, namely when the excursion has only its mandatory entry zero and remains at depth two until return.

For the physical scale `Q=P/2^H`,

`boxed:
 Q_out/Q_in
 = 2 (2/3)^h 3^(z-1) (3/2)^E`.

This explains why a height-only physical-scale expansion theorem is false: the one-zero extremal family contracts `Q` for sufficiently large height.

Classification: **exact analytic first-return factorization**.

## 3. Global endpoint-potential extension

For any real/rational parameter `c` with `-2<=c<=0`, put

`a_d(c)=1+2^(d-1)(c-1)`

and define

`Phi_c(d,K,Q)=Q (K+a_d(c))/3^d`.

A direct check of the four exact transitions gives:

- `K` even, `x=1`:
  `Delta Phi_c = -Q a_d(c)/3^(d+1)`;
- `K` even, `x=0`:
  `Delta Phi_c = Q(3^d+2^(d-1)(c-1))/3^d`;
- `K` odd, `x=1`:
  `Delta Phi_c = 0`;
- `K` odd, `x=0`:
  `Delta Phi_c = Q(3^(d+1)-1+2^(d-1)(c-1))/3^(d+1)`.

For `-2<=c<=0` all increments are nonnegative, and every ascent `K` odd, `x=0` is strict.

Thus

`boxed:
 Phi_c is nondecreasing along every legal canonical trajectory,
 and strictly increases on every ascent.`

At `d=1`, the cases `c=0` and `c=-2` extend, up to a fixed factor, RL279's boundary endpoint quantities `Q(n+1)` and `Qn`.

For a height-positive first-return excursion of height `h`,

`boxed:
 P_out (K_out+c) > 2^h P_in (K_in+c)
 for every -2<=c<=0.`

In particular,

`P_out K_out > 2^h P_in K_in`

and

`P_out(K_out-2) > 2^h P_in(K_in-2)`.

The family is asymptotically sharp; no fixed factor `(1+epsilon)2^h` is available uniformly.

Classification: **exact analytic state-versus-height theorem**.

## 4. Excursion coupon decomposition and nested zero law

Let the excursion's local `x` zero ranks be

`u_1,...,u_z`

and the corresponding `y` zero ranks be

`v_1,...,v_z`.

Put

`h_j=v_j-u_j>=1`.

The total excursion height is exactly

`boxed:
 Delta H = sum_(j=1)^z h_j`.

Before the `(j+1)`-st `x` zero, the `j`-th corresponding `y` zero cannot yet have occurred because the excursion remains at `d>1`. Hence, for

`g_(j+1)=u_(j+1)-u_j`,

`boxed:
 g_(j+1) <= h_j-1`.

Let the local zero weights be normalized by the entry weight `c_1=c_entry`:

`c_j/c_1 = 2^(j-1)(2/3)^(u_j-u_1)`.

The inherited zero-to-zero multiplier now yields the sharper excursion law

`boxed:
 c_(j+1) >= 3 c_j (2/3)^(h_j)`.

The global coupon defect splits exactly across first-return excursions; zero-height boundary zeros have `h_t=0` and contribute nothing. Thus the defect of an excursion is

`boxed:
 D_E=sum_(j=1)^z c_j(1-(2/3)^(h_j))`.

Classification: **exact analytic excursion/coupon decomposition**.

## 5. Sharp zero-complexity/height envelope

Write `rho=2/3`, `h=Delta H`, and `c=c_entry`.

Iterating the nested zero law and optimizing the resulting exact lower bound at fixed `(z,h)` gives

`boxed:
 D_E >=
 c [1 + ((2^z-4)/3) rho^(h-z)]`.

This contains the one-zero result

`D_E >= c(1-rho^h)`.

For `z>=2`,

`boxed:
 D_E >= c`.

For `z>=3`,

`D_E-c >= ((2^z-4)/3)c rho^(h-z)`.

At minimum height `h=z`,

`boxed:
 D_E >= ((2^z-1)/3)c`.

Consequently, for `z>=3`, if `D_E<=C c` with `C>1`, then necessarily

`boxed:
 h-z >= log_(3/2)((2^z-4)/(3(C-1)))`.

### Equality classification

Equality in the sharp envelope holds exactly when

`h_1=h-z+1`,
`h_2=...=h_z=1`

and every nested zero inequality saturates.

Let `s=h-z`. The unique equality words are

`boxed:
 x = 0 1^s 0^(z-1) 1,
 y = 1^(s+1) 0^z`.

These excursions remain entirely at depth `d=2` after entry and descend only in the final column.

Thus the complete cheap family is a single explicit depth-two normal form; `01^h` is its `z=1` member.

Classification: **sharp analytic lower envelope with exact equality class**.

## 6. Sharp first-return state/scale theorem

For an excursion define

`S_E=sum_j c_j`.

The exact endpoint telescope is

`boxed:
 Q_out K_out - Q_in K_in = 2S_E + D_E`.

Using the nested-zero bounds gives the sharp zero-count-dependent return estimate

`boxed:
 2S_E+D_E
 >=
 3Q_in + (7/2-2^(3-z)) Q_out`.

Therefore every first-return excursion satisfies

`boxed:
 Q_out (K_out-7/2+2^(3-z))
 >=
 Q_in (K_in+3)`.

Equality holds exactly for the depth-two normal form of Section 5.

### Arithmetic rigidity of equality

For an equality excursion put

`s=h-z`,
`w=2K_out-7`.

Then `w` is odd and

`boxed:
 3^(s+1)(K_in+3)
 =
 2^(s+1)(8+2^(z-1)w)`.

For fixed `(h,z)`, the equality family therefore occupies:

- one residue class for `K_in` modulo `2^(h+1)`;
- one residue class for `w` modulo `3^(s+1)`.

The extremal family is consequently arithmetically rigid rather than freely tunable.

Classification: **sharp analytic first-return state/scale theorem plus exact equality rigidity**.

## 7. Aggregate endpoint-potential dependency

Summing the `c=0` endpoint potential over a complete terminal path gives exactly

`3(Phi_0,terminal-Phi_0,initial)=2S+D`.

After inserting the initial and terminal states this is precisely the already-promoted RL279 identity

`2S+D=12+X(1/2+2^(-k-1))`.

The `c=-2` member is affine-dependent as well.

Therefore the global endpoint-potential equation is not an independent scalar constraint and must not be double-counted against the RL279 zero-rank identity.

The new endpoint potentials are useful locally/segmentwise, not as an additional global terminal equation.

Classification: **dependency/barrier identification preventing a false independent constraint**.

## 8. Positive-checkpoint Lyapunov theorem

Define a positive checkpoint by

`d=1`, `J>0`, `J` even.

A nonterminal positive checkpoint has odd `K=J+1`, so the next legal column is the forced ascent beginning a positive first-return excursion.

After the excursion returns to `d=1`:

- if the returned `J` is even, it is already the next checkpoint;
- if the returned `J` is odd, follow any number of positive zero-height boundary-retaining steps, then take the complementary exit step to an even-`J` checkpoint.

Define

`boxed:
 F=Q(J+3)`.

Using the sharp first-return state/scale theorem and the already-promoted positive boundary endpoint monotonicity gives:

`boxed:
 F_next > F_in + Q_in/3`.

If the excursion contains at least two zeros,

`boxed:
 F_next > F_in + Q_in`.

Hence in particular

`boxed:
 F_next > F_in`.

This quotients arbitrary positive boundary transients/cycles without classifying the accelerated `3n+1` subsystem.

Classification: **strict positive-phase Lyapunov theorem**.

## 9. Terminal ceiling and reciprocal state/scale bound

At a retained terminal,

`J_T=2^k`

and

`Q_T=X/2^(k+1)`.

Therefore

`F_T = X(1/2+3/2^(k+1))`.

Since `k>=3` and `X<160/3`,

`boxed:
 F_T < 110/3`.

Because `F` strictly increases over positive checkpoint blocks, every positive checkpoint on a retained terminal path satisfies

`boxed:
 Q_i(J_i+3) < 110/3`.

Equivalently,

`boxed:
 J_i < 110/(3Q_i)-3`.

At an excursion entry, `Q_i` is exactly the corresponding zero weight `c_t`. Thus positive boundary state and absolute zero weight are now directly coupled.

Also,

`sum_i Q_i < 3(F_T-F_first) < 110`

over positive excursion checkpoints, with stronger unit price for excursions containing at least two zeros.

Classification: **terminally capped state/scale Lyapunov consequence**.

## 10. Verification

Portable verifier:

`sessions/RL280/verification/verify_rl280_excursions.py`

checks directly from the inherited exact `(d,K)` recurrence:

- global `Phi_c` monotonicity on a broad exact integer grid;
- strict ascent increments;
- exact first-return `P/Q` factorization;
- exact height/zero-lag decomposition;
- nested zero inequality;
- sharp defect envelope;
- exact depth-two equality classification;
- exact endpoint telescope;
- sharp zero-count first-return state/scale inequality;
- equality arithmetic identity and residue rigidity;
- positive-checkpoint block increment laws;
- terminal `F<110/3` ceiling algebra.

Recorded clean-run output:

- `18,680` global endpoint-potential checks;
- `4,800` strict ascent checks;
- `13,909` first-return excursions;
- `399` exact depth-two equality excursions;
- `39` equality parameter pairs;
- `45,170` positive-checkpoint block checks;
- minimum normalized checkpoint increment `1241/2187 > 1/3`.

The verifier passes.

## 11. Exact remaining obstruction

Gate A is still

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical violator still satisfies

`m0>=8`, equivalently `z>=k+6`.

RL280 has compressed the positive height-producing dynamics to:

1. a sharp first-return state/scale inequality;
2. a unique depth-two equality family;
3. explicit 2-adic/3-adic rigidity of that equality family;
4. a strict positive-checkpoint Lyapunov quantity `F=Q(J+3)`;
5. the terminal ceiling `F<110/3`.

The successor should combine these with the inherited zero-mass/coupon/terminal-scale identities to test whether a dangerous `H_can<k` path can sustain the required sequence of small positive excursion-entry weights.

It should not restart the internal excursion classification or make flat eight-zero enumeration the principal programme.

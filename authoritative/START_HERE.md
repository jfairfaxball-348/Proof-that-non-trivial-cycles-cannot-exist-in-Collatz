# Authoritative start — RL281

Date prepared: 2026-09-08

Incoming completed generation: **RL280 — sharp positive-excursion state/scale compression and positive-checkpoint Lyapunov law**.

RL280 primary classification:

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

Promoted exact state:

- every first-return excursion has exact `P/Q` factorization and sharp state-versus-height pricing;
- excursion coupon defect splits exactly and obeys the nested zero law;
- for `z` excursion zeros and height `h`,
  `D_E >= c_entry[1+((2^z-4)/3)(2/3)^(h-z)]`;
- equality is exactly the depth-two family
  `x=0 1^(h-z) 0^(z-1) 1`,
  `y=1^(h-z+1) 0^z`;
- every first-return excursion satisfies
  `Q_out(K_out-7/2+2^(3-z)) >= Q_in(K_in+3)`,
  with equality exactly for that depth-two family;
- equality obeys the exact 2-adic/3-adic relation
  `3^(s+1)(K_in+3)=2^(s+1)(8+2^(z-1)(2K_out-7))`,
  `s=h-z`;
- at positive even-`J` checkpoints,
  `F=Q(J+3)` satisfies
  `F_next>F_in+Q_in/3`,
  and `F_next>F_in+Q_in` for excursions with at least two zeros;
- retained terminals satisfy `F_T<110/3`, hence every positive checkpoint satisfies
  `Q(J+3)<110/3`;
- the aggregate endpoint-potential terminal telescope is dependent on the inherited `2S+D` identity and must not be double-counted.

Gate A remains open with exact target

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator still satisfies

`m0>=8`, equivalently `z>=k+6`.

Read

`RL281_POSITIVE_CHECKPOINT_GATE_A_CLOSURE_TARGET.md`

first.

RL281 is **prepared but NOT STARTED**.

Priority: combine the positive-checkpoint Lyapunov/state-scale law with `17/2<S<21`, the exact coupon budget, terminal scale, and the rigid depth-two equality congruences. Do not restart internal excursion classification.

Gate B remains separate/open and frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

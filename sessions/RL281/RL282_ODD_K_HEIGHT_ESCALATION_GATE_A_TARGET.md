# RL282 — odd-k height-escalation Gate-A target

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED

## Incoming classification

RL281 closed as

`TWO_PHASE_GATE_A_COMPRESSION_PROVED`

with subordinate results:

- `SHARP_EXCURSION_ZERO_MASS_ENVELOPE_PROVED`;
- `POSITIVE_BLOCK_FULL_MASS_PRICING_PROVED`;
- `DEPTH_TWO_EQUALITY_ENTRY_SCALE_SUPPRESSION_PROVED`;
- `ONE_ZERO_2ADIC_HEIGHT_RIGIDITY_PROVED`;
- `POSITIVE_BOUNDARY_ZERO_MASS_TELESCOPE_PROVED`;
- `POSITIVE_PHASE_ZERO_MASS_CEILING_PROVED`;
- `NEGATIVE_PHASE_DUAL_POTENTIAL_BUDGET_PROVED`;
- `NEGATIVE_TO_POSITIVE_GATEWAY_DICHOTOMY_PROVED`;
- `MOD3_REACHABILITY_INVARIANT_PROVED`;
- `MINIMUM_POSITIVE_HEIGHT_THREE_PROVED`;
- `K3_GATE_A_CASE_CLOSED_PROVED`.

Gate A remains

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator is now restricted to

`k>=5`, `k` odd, `H_can<k`.

Gate B is separate/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen.

## Exact inherited RL281 state

Preserve all RL280/RL279 results and additionally:

1. Excursion zero-mass envelope:
   `S_E >= q[1+(2^z-2)(2/3)^(h-z)]`,
   with equality exactly in the depth-two normal form.
2. Positive checkpoint block cost:
   `F_next-F_in > 2S_E+D_E-2q`,
   hence
   `F_next-F_in > q[1+((7*2^z-16)/3)(2/3)^(h-z)]`.
3. Every positive excursion with `z>=2` satisfies
   `F_next-F_in>S_E`.
4. For positive depth-two equality excursions with `z>=5`,
   `nu_2(J_in+4)=h-z+4`,
   giving exponential entry-state/scale suppression.
5. One-zero excursion law:
   `3^h(J_in+4)=2^h(2J_out+3)` and
   `h=nu_2(J_in+4)` whenever `J_in!=-4`.
6. Positive-boundary telescope:
   `B=Q(J+1)/2`;
   boundary `x=0` zeros increase `B` exactly by their zero weight and boundary `x=1` steps leave it fixed.
7. Total positive-phase zero mass satisfies
   `S_positive<15`.
8. Negative dual potential:
   `C=Q(J-1)`;
   every first-return excursion entry costs at least `5Q_in/3` in `C`, so complete nonpositive-return excursion entry scales sum to `<42/5`.
9. Direct strictly-negative-to-positive one-zero crossing is impossible; such a crossing has `z>=2`.
10. The only cheap sign-change gateway is
    `J=0 --011,h=2--> J=3`
    with scale factor `8/9`.
11. Reachability invariant:
    `J mod 3 in {0,(-1)^d}`.
    Therefore terminal `k` is odd.
12. Every positive `d=1` state has `H_can>=3`; consequently `k=3` is Gate-A safe.

## Mission

Close the residual odd-exponent Gate-A problem.

The exact live target is now:

`k>=5`, `k` odd, terminal `J=2^k`, prove `H_can>=k`.

Preferred order:

1. Quotient the mandatory height-3 sign-change core rather than reclassifying the negative boundary subsystem.
2. Work from the exact terminal power-of-two condition and the mod-3 invariant to derive a scalable restriction on backward/forward reachable `d=1` states for successive odd `k`.
3. Use the one-zero valuation law `h=nu_2(J+4)` to price every cheap positive height increment arithmetically.
4. Use the full-mass pricing theorem for every `z>=2` positive excursion; do not reopen arbitrary excursion interiors.
5. Combine the resulting height-escalation law with the terminal scale, `17/2<S<21`, coupon identity, and the `S_positive<15` phase budget.
6. Seek either:
   - a uniform theorem `H_can>=k` for all odd `k>=5`, closing Gate A; or
   - the strongest correct scalable recurrence/finite-dimensional residual obstruction if one final step remains.

A terminal-backward recurrence or valuation automaton is in scope if it is proved from the current exact `(d,J)` transition law. Treat any finite observations only as evidence until a gap-free theorem/certificate is established.

## Forbidden repeats

Do not:

- restart flat eight-zero or higher fixed-zero enumeration as the principal programme;
- reclassify the completed RL280 first-return excursion interiors;
- classify accelerated `3n+1` boundary cycles;
- double-count endpoint potentials already dependent on the global endpoint identity;
- restart selector enumeration;
- merge Gate B into Gate A without a new proved coupling;
- start Radius 6+.

Gate B remains frozen unless a newly proved coupling requires it.
